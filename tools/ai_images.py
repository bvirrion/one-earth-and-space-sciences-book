#!/usr/bin/env python3
"""Generate a batch of AI illustrations with OpenAI image generation via Codex.

    python3 tools/ai_images.py --book 1 batch.txt [--work DIR]

batch.txt holds one image per paragraph:

    g2-sugar-in-tea | 3:2
    a glass of hot tea on a kitchen table, a spoon stirring in a sugar cube ...

The first line is ``<file stem> | <aspect>`` (3:2, 1:1 or 2:3); the following
lines are the editor's prompt. The shared STYLE suffix is appended.

For each image not already present in images/book<N>/ai/:
  1. `codex exec` is run in a scratch working directory (NEVER the repo: a
     repo cwd hangs it) with stdin closed (an open stdin hangs it too);
  2. the PNG it writes (never "the newest file under
     ~/.codex/generated_images": another agent's image) is transcoded to JPEG with the HTML
     reader's recipe (ffmpeg -q:v 3 -pix_fmt yuvj420p) into the book's ai/
     directory, and the PNG is never copied into the repo;
  3. the prompt is appended to images/book<N>/ai/PROMPTS.md.

When Codex reports a usage limit, the batch sleeps 30 minutes and retries the
same image (the run can be left detached for hours). Every image must still be
looked at before it is inserted: this tool generates, it does not review.
"""
import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

STYLE = ("Clean realistic illustration style, natural colours, soft even lighting, "
         "plain white or neutral background unless the scene says otherwise, "
         "absolutely no text, no letters, no labels, no arrows, no numbers, no captions, "
         "no logos, no brand names.")
SIZES = {"3:2": "landscape aspect 3:2 (1536x1024)", "1:1": "square aspect 1:1 (1024x1024)",
         "2:3": "portrait aspect 2:3 (1024x1536)"}
LIMIT_RE = re.compile(r"usage limit|rate limit|quota|try again", re.I)


def codex_model():
    cfg = Path.home() / ".codex/config.toml"
    if cfg.is_file():
        m = re.search(r'^\s*model\s*=\s*"([^"]+)"', cfg.read_text(), re.M)
        if m:
            return m.group(1)
    return "codex default"


def read_batch(path):
    items = []
    for block in re.split(r"\n\s*\n", open(path, encoding="utf8").read().strip()):
        lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
        if not lines or lines[0].startswith("#"):
            continue
        stem, aspect = [x.strip() for x in lines[0].split("|")]
        if aspect not in SIZES:
            sys.exit("bad aspect %r for %s" % (aspect, stem))
        items.append((stem, aspect, " ".join(lines[1:])))
    return items


# A JPEG this small is a grey stub made by tools/ai_stubs.py so that the book
# builds while the generator is rate-limited: it is regenerated, not skipped.
STUB_MAX = 20000


def generate(prompt, aspect, work):
    out = work / "image.png"
    if out.exists():
        out.unlink()
    instr = ("Use your image generation tool to generate exactly ONE image, %s. "
             "Do not edit or add anything to the prompt below. Prompt:\n\n%s %s\n\n"
             "Then copy the generated PNG file to ./image.png in the current directory "
             "and print its absolute path. Do nothing else." % (SIZES[aspect], prompt, STYLE))
    start = time.time()
    r = subprocess.run(["codex", "exec", "--skip-git-repo-check", "-s", "workspace-write",
                        "-C", str(work), instr],
                       stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=1200)
    if out.is_file() and out.stat().st_size > 10000:
        return out, ""
    # No fallback to "the newest PNG under ~/.codex/generated_images": with
    # several agents generating at once it can pick up another book's image
    # (Earth series Book 4 report, 2026-10-23). A missing ./image.png is a
    # failure, retried by the caller.
    return None, (r.stderr or "") + (r.stdout or "")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--book", type=int, required=True)
    ap.add_argument("batch")
    ap.add_argument("--work", default=None, help="scratch directory (not the repo)")
    args = ap.parse_args()

    dest = Path("images/book%d/ai" % args.book)
    dest.mkdir(parents=True, exist_ok=True)
    work = Path(args.work or os.environ.get("TMPDIR", "/tmp")) / "ai_images_work"
    work.mkdir(parents=True, exist_ok=True)
    log = dest / "PROMPTS.md"
    if not log.exists():
        log.write_text("# AI image prompts --- Book %d\n\n"
                       "Every image in this directory was generated with OpenAI image generation "
                       "driven through the Codex CLI (`codex exec`, built-in image tool), from the "
                       "prompt recorded below (aspect ratio noted), and visually reviewed for "
                       "scientific accuracy (geology, weather, sky) before insertion into the book. Rejected generations are "
                       "not kept.\n\nShared style suffix appended to every prompt: *\"%s\"*\n"
                       % (args.book, STYLE))

    for stem, aspect, prompt in read_batch(args.batch):
        jpg = dest / (stem + ".jpg")
        if jpg.exists() and jpg.stat().st_size > STUB_MAX:
            print("  skip   %s (exists)" % stem, flush=True)
            continue
        while True:
            t0 = time.time()
            png, err = generate(prompt, aspect, work)
            if png:
                break
            if LIMIT_RE.search(err):
                print("  limit  %s: sleeping 30 min" % stem, flush=True)
                time.sleep(1800)
                continue
            print("  FAIL   %s: %s" % (stem, err[-400:]), flush=True)
            break
        if not png:
            continue
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(png), "-q:v", "3",
                        "-pix_fmt", "yuvj420p", str(jpg)], check=True)
        png.unlink()
        with open(log, "a", encoding="utf8") as f:
            f.write("\n## %s\n\n*aspect %s* --- %s\n\n<!-- %s, agent model %s -->\n"
                    % (stem, aspect, prompt, datetime.date.today().isoformat(), codex_model()))
        print("  ok     %s (%.0f s)" % (stem, time.time() - t0), flush=True)


if __name__ == "__main__":
    main()

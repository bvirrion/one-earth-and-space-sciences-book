#!/usr/bin/env python3
"""Grey stubs for AI illustrations a book references but that are not generated yet.

    python3 tools/ai_stubs.py --book 1          # create the missing stubs
    python3 tools/ai_stubs.py --book 1 --list   # list stubs still in place

The Codex image generator can be rate-limited for hours. Rather than leave
the repository unbuildable (a missing \\includegraphics file is a fatal
pdfTeX error), each referenced images/book<N>/ai/<stem>.jpg that does not
exist gets a plain grey 1200x800 JPEG of a few kilobytes. tools/ai_images.py
treats any JPEG under 20 kB as a stub and regenerates it, so a batch can be
re-run over the same list; tools/gates.sh warns while any stub remains. A
book is not finished while it carries a stub.
"""
import argparse
import glob
import re
import subprocess
import sys
from pathlib import Path

STUB_MAX = 20000
YEARS = {1: "grade-[1-9]", 2: "grade-1[0-2]", 3: "bachelor-1", 4: "bachelor-2", 5: "bachelor-3"}


def referenced(book):
    refs = set()
    for f in glob.glob("parts/%s/**/*.tex" % YEARS[book], recursive=True):
        refs |= set(re.findall(r"images/book%d/ai/[A-Za-z0-9_.-]+\.jpg" % book,
                               open(f, encoding="utf8").read()))
    return sorted(refs)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", type=int, required=True)
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    stubs = []
    for r in referenced(a.book):
        p = Path(r)
        if p.exists() and p.stat().st_size > STUB_MAX:
            continue
        if not p.exists() and not a.list:
            subprocess.run(["ffmpeg", "-loglevel", "error", "-f", "lavfi", "-i",
                            "color=c=0xBBBBBB:s=1200x800", "-frames:v", "1",
                            "-q:v", "5", str(p)], check=True)
        if p.exists():
            stubs.append(r)
    for s in stubs:
        print(s)
    if a.list:
        return 1 if stubs else 0
    print("%d stub(s) in place" % len(stubs), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

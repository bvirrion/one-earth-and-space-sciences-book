#!/usr/bin/env python3
"""Chemistry twin gate: every translated file must carry its English twin's
chemistry and its English twin's data sources, unchanged.

    python3 tools/check_chem_twin.py [--quiet] parts/<year>/<lang> [parts/<year>/solutions/<lang>]

Two classes, both compared file by file against the English twin found by path
(parts/<year>/<lang>/X.tex <-> parts/<year>/X.tex):

  chem    the ordered sequence of \\ce{}, \\chemfig{}, \\ghs{},
          \\omperiodictable[...] and \\schemestart..\\schemestop schemes, as
          tools/id_apply.py's `chem` census computes it (a scheme's word-only
          \\arrow labels blanked, since those are visible text). id_apply
          enforces this at write time; this gate enforces it on what is ON DISK,
          after every post-write edit, overfull fix and link pass. Most of the
          books' \\ce{} sit in running prose, outside every math span, so no
          other census sees a formula an agent reordered, dropped, or
          "localised" -- a state symbol (aq) -> (ac) is a chemistry change.
  ledger  the multiset of `% ledger: <id>, ...` ids. Every printed number for a
          real substance is traced to a sourced ledger row by a comment on the
          line before it; a translation that lost the comment ships the number
          untraced, and tools/check_ledger.py only checks that the ids that ARE
          there resolve.

Written 2026-10-04 for the first chemistry translations. Exit 1 on any finding,
2 on a path that is neither a directory nor a .tex file (a gate must never
report success over nothing).
"""
from __future__ import annotations

import argparse
import collections
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from id_apply import chem_spans, unwrap_omterm  # noqa: E402

LEDGER = re.compile(r"%\s*ledger:\s*([^\n]*)")


def ledger_ids(text):
    ids = collections.Counter()
    for m in LEDGER.finditer(text):
        for x in m.group(1).split(","):
            x = x.strip().split()[0] if x.strip() else ""
            if x:
                ids[x] += 1
    return ids


def twin_of(path: pathlib.Path) -> pathlib.Path:
    # parts/<year>/<lang>/X.tex -> parts/<year>/X.tex (solutions likewise)
    return path.parent.parent / path.name


def files_of(args):
    out = []
    for a in args:
        p = pathlib.Path(a)
        if p.is_dir():
            out.extend(sorted(p.glob("[0-9]*.tex")))
        elif p.is_file() and p.suffix == ".tex":
            out.append(p)
        else:
            print("check_chem_twin: not a directory or .tex file: %s" % a,
                  file=sys.stderr)
            sys.exit(2)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("paths", nargs="+")
    args = ap.parse_args()
    files = files_of(args.paths)
    findings = []
    for f in files:
        en = twin_of(f)
        if not en.is_file():
            continue
        a = unwrap_omterm(en.read_text(encoding="utf-8"))
        b = unwrap_omterm(f.read_text(encoding="utf-8"))
        sa, sb = chem_spans(a), chem_spans(b)
        if sa != sb:
            i = next((k for k, (x, y) in enumerate(zip(sa, sb)) if x != y),
                     min(len(sa), len(sb)))
            findings.append((f, "chem", "span #%d of %d/%d: EN %r / TR %r" % (
                i, len(sa), len(sb), sa[i][:80] if i < len(sa) else None,
                sb[i][:80] if i < len(sb) else None)))
        la, lb = ledger_ids(a), ledger_ids(b)
        if la != lb:
            findings.append((f, "ledger", "missing %s / extra %s" % (
                dict(la - lb), dict(lb - la))))
    for f, cls, msg in findings[: (20 if args.quiet else 10 ** 9)]:
        print("        %s: %s: %s" % (f, cls, msg))
    if findings:
        print("  chemistry twin gate: %d issue(s) in %d files"
              % (len(findings), len(files)))
        return 1
    print("  chemistry twin gate: OK (%d files)" % len(files))
    return 0


if __name__ == "__main__":
    sys.exit(main())

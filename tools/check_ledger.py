#!/usr/bin/env python3
"""The data-ledger gate: every number about a real substance is sourced.

    python3 tools/check_ledger.py              # every ledger, every part
    python3 tools/check_ledger.py parts/grade-11

Ledgers are sources/data_ledger.md (shared: atomic weights, constants) and
sources/ledger/book<N>.md (one per book). Checked:

1. row ids are unique across all ledger files;
2. every row has a source key listed in the Sources table of its own file or
   of the shared file, and an access date YYYY-MM-DD;
3. every ``% ledger: <id>, <id> ...`` comment under the given paths names ids
   that exist. The id list ends at the first ``(`` or ``;``; what follows is
   free text (``% ledger: air:N2, air:O2 (rounded to 78 / 21)``).

Standard library only. Exit 1 on any failure.
"""
import glob
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SHARED = os.path.join(ROOT, "sources", "data_ledger.md")
ID = re.compile(r"^[a-z][A-Za-z0-9]*:[A-Za-z0-9][A-Za-z0-9_.+\-]*$")
ROW = re.compile(r"^\|\s*([a-z][A-Za-z0-9]*:[^\s|]+)\s*\|")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def ledger_files():
    return [SHARED] + sorted(glob.glob(os.path.join(ROOT, "sources", "ledger", "*.md")))


def read_ledger(path):
    """(source keys, [(id, cells, lineno)])"""
    keys, rows = set(), []
    section = None
    for n, line in enumerate(open(path, encoding="utf8"), 1):
        if line.startswith("## "):
            section = line[3:].strip().lower()
            continue
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if section == "sources":
            if cells and cells[0] not in ("key", "") and not set(cells[0]) <= set("-"):
                keys.add(cells[0])
        elif section == "rows":
            m = ROW.match(line)
            if m:
                rows.append((m.group(1), cells, n))
    return keys, rows


def refs(paths):
    """[(file, lineno, id)] from % ledger: comments."""
    out = []
    files = []
    for p in paths:
        if os.path.isdir(p):
            files += sorted(glob.glob(os.path.join(p, "**", "*.tex"), recursive=True))
        elif os.path.isfile(p):
            files.append(p)
    for f in files:
        for n, line in enumerate(open(f, encoding="utf8"), 1):
            m = re.search(r"%\s*ledger:\s*(.*)$", line)
            if not m:
                continue
            ids = re.split(r"[(;]", m.group(1), 1)[0]
            for tok in [t.strip() for t in ids.split(",")]:
                if tok:
                    out.append((f, n, tok))
    return out


def check(paths):
    errors = []
    shared_keys, _ = read_ledger(SHARED)
    seen = {}
    for path in ledger_files():
        keys, rows = read_ledger(path)
        rel = os.path.relpath(path, ROOT)
        for rid, cells, n in rows:
            if rid in seen:
                errors.append("%s:%d: id %s already defined at %s" % (rel, n, rid, seen[rid]))
            seen[rid] = "%s:%d" % (rel, n)
            if len(cells) < 6:
                errors.append("%s:%d: %s has %d cells, expected 6 (id|quantity|value|unit|source|accessed)"
                              % (rel, n, rid, len(cells)))
                continue
            for k in [k.strip() for k in re.split(r"[;,]", cells[4]) if k.strip()]:
                if k not in keys and k not in shared_keys:
                    errors.append("%s:%d: %s cites source key %r, not in a Sources table" % (rel, n, rid, k))
            if not cells[4].strip():
                errors.append("%s:%d: %s has no source" % (rel, n, rid))
            if not DATE.match(cells[5]):
                errors.append("%s:%d: %s has no access date (YYYY-MM-DD)" % (rel, n, rid))
    for f, n, tok in refs(paths):
        rel = os.path.relpath(f, ROOT) if os.path.isabs(f) else f
        if not ID.match(tok):
            errors.append("%s:%d: %r is not a ledger id (list ids, then free text after '(' or ';')"
                          % (rel, n, tok))
        elif tok not in seen:
            errors.append("%s:%d: ledger id %s has no row" % (rel, n, tok))
    return errors, len(seen)


def main(argv):
    paths = argv[1:] or [os.path.join(ROOT, "parts")]
    errors, nrows = check(paths)
    for e in errors:
        print(e)
    if errors:
        print("check_ledger: %d problem(s)" % len(errors))
        return 1
    print("check_ledger: OK (%d rows)" % nrows)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

#!/usr/bin/env python3
"""Every chemical equation in the book conserves atoms and charge.

    python3 tools/check_ce_balance.py parts/grade-11            # one year
    python3 tools/check_ce_balance.py parts/grade-11/07-redox.tex
    python3 tools/check_ce_balance.py parts                     # everything

WHY. An unbalanced equation is the classic invisible defect of a chemistry
book: it builds, it reads well, every other gate passes, and a student who
checks it loses confidence in the whole page. So every \\ce{...} that contains
an arrow (->, <=>, <->, ...) is parsed (tools/chem.py) and its atoms and its
charge are counted on both sides.

An equation that is unbalanced ON PURPOSE -- the "balance this equation"
exercise, a skeleton the reader must complete -- carries the comment
``% ce-unbalanced-ok`` on the line where its \\ce{ starts. Any expression the
parser cannot read fails too (same escape), so a formula never slips through
unchecked; word equations (``methane + oxygen -> ...``) are skipped.

Exit status 0 when clean, 1 when something is unbalanced or unreadable, 2 on
a path that is neither a .tex file nor a directory (a gate handed a wrong
path must not print OK over zero files).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import chem  # noqa: E402

OK_MARK = "ce-unbalanced-ok"


def ce_calls(text):
    """(start offset, argument) for every \\ce{...}, braces balanced."""
    for m in re.finditer(r"\\ce\s*\{", text):
        depth, i = 1, m.end()
        while i < len(text) and depth:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        yield m.start(), text[m.end():i - 1]


def strip_comments(text):
    # keep line structure (offsets -> line numbers), blank out comments
    return re.sub(r"(?<!\\)%[^\n]*", lambda m: " " * len(m.group(0)), text)


def check_file(path):
    raw = open(path, encoding="utf8").read()
    text = strip_comments(raw)
    lines = raw.split("\n")
    bad, checked = [], 0
    for pos, arg in ce_calls(text):
        lineno = text.count("\n", 0, pos) + 1
        if OK_MARK in lines[lineno - 1]:
            continue
        expr = re.sub(r"\s+", " ", arg)
        try:
            res = chem.balance(expr)
        except (chem.ParseError, ValueError, ZeroDivisionError) as e:
            bad.append((lineno, expr, "unreadable: %s" % e))
            continue
        if res == "":
            continue
        checked += 1
        if res:
            bad.append((lineno, expr, res))
    return checked, bad


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    files = []
    for a in argv:
        if os.path.isdir(a):
            for root, _, fs in os.walk(a):
                files += [os.path.join(root, f) for f in fs if f.endswith(".tex")]
        elif os.path.isfile(a) and a.endswith(".tex"):
            files.append(a)
        else:
            print("not a .tex file or a directory: %s" % a)
            return 2
    total, nbad = 0, 0
    for f in sorted(files):
        checked, bad = check_file(f)
        total += checked
        for lineno, expr, why in bad:
            nbad += 1
            print("%s:%d: %s\n    \\ce{%s}" % (f, lineno, why, expr))
    print("%s: %d equations checked in %d files, %d problems"
          % ("OK" if not nbad else "FAIL", total, len(files), nbad))
    return 1 if nbad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

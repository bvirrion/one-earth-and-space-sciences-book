#!/usr/bin/env python3
"""Every chapter carries its band's exercise set and weekend problem.

    python3 tools/check_exercise_calibration.py parts/grade-11

The series calibration (CONTRIBUTING.md, "Style rules"):

  band            exercises                    weekend problem
  grades 1-5      10-11, mostly one star       none
  grades 6-9      exactly 12                   one, 10-14 questions
  grades 10-12    exactly 15: 5/6/4 stars      one, 18-22 questions
  bachelor 1-3    exactly 12: 4/5/3 stars      one, 22-28 questions

Stars never decrease from one exercise to the next. A question is a top-level
\\item of the problem (nested lists are sub-questions). A placeholder chapter
(no exercise at all, "To be written") is skipped, so the gate can run over a
year that is half written.
"""
import pathlib
import re
import sys

EXO = re.compile(r"\\begin\{exercise\}\[\s*\$((?:\\star\s*)+)\$\s*\]")
PROBLEM = re.compile(r"\\begin\{problem\}(.*?)\\end\{problem\}", re.S)
LIST = re.compile(r"\\(begin|end)\{(enumerate|itemize)\}|\\item\b")


def band(year):
    m = re.match(r"(grade|bachelor)-(\d+)$", year)
    if not m:
        return None
    kind, n = m.group(1), int(m.group(2))
    if kind == "bachelor":
        return dict(n=(12, 12), ramp=(4, 5, 3), q=(22, 28))
    if n <= 5:
        return dict(n=(10, 11), ramp=None, q=None)
    if n <= 9:
        return dict(n=(12, 12), ramp=None, q=(10, 14))
    return dict(n=(15, 15), ramp=(5, 6, 4), q=(18, 22))


def questions(body):
    depth, count = 0, 0
    for m in LIST.finditer(body):
        if m.group(1) == "begin":
            depth += 1
        elif m.group(1) == "end":
            depth -= 1
        elif depth == 1:
            count += 1
    return count


def check_file(path, b):
    src = path.read_text(encoding="utf8")
    src = "\n".join(l.split("%")[0] if not l.lstrip().startswith("%") else "" for l in src.splitlines())
    stars = [m.group(1).count("\\star") for m in EXO.finditer(src)]
    n_env = src.count("\\begin{exercise}")
    probs = PROBLEM.findall(src)
    if n_env == 0 and not probs:
        return []  # placeholder
    out = []
    if n_env != len(stars):
        out.append("%d exercise(s) without a [$\\star...$] difficulty" % (n_env - len(stars)))
    lo, hi = b["n"]
    if not lo <= len(stars) <= hi:
        out.append("%d exercises, band wants %s" % (len(stars), lo if lo == hi else "%d-%d" % (lo, hi)))
    if any(a > b_ for a, b_ in zip(stars, stars[1:])):
        out.append("stars decrease somewhere: %s" % "".join(map(str, stars)))
    if b["ramp"]:
        got = tuple(stars.count(k) for k in (1, 2, 3))
        if got != b["ramp"]:
            out.append("star ramp %d/%d/%d, band wants %d/%d/%d" % (got + b["ramp"]))
    elif b["q"] is None and stars and stars.count(1) * 2 < len(stars):
        out.append("young band: most exercises should be one star (%s)" % "".join(map(str, stars)))
    if b["q"] is None:
        if probs:
            out.append("this band has no weekend problem")
    else:
        if len(probs) != 1:
            out.append("%d weekend problems, band wants 1" % len(probs))
        else:
            q = questions(probs[0])
            if not b["q"][0] <= q <= b["q"][1]:
                out.append("weekend problem has %d questions, band wants %d-%d" % ((q,) + b["q"]))
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    bad = 0
    for arg in argv[1:]:
        d = pathlib.Path(arg)
        b = band(d.name)
        if b is None or not d.is_dir():
            print("check_exercise_calibration: %s is not a parts/<grade-N|bachelor-N> directory" % arg)
            return 2
        for f in sorted(d.glob("[0-9]*.tex")):
            for msg in check_file(f, b):
                print("%s: %s" % (f, msg))
                bad += 1
    if bad:
        print("check_exercise_calibration: %d problem(s)" % bad)
        return 1
    print("check_exercise_calibration: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

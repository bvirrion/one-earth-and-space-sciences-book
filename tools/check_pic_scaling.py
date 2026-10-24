#!/usr/bin/env python3
"""In a scaled tikzpicture, every glassware \\pic must carry [transform shape].

    python3 tools/check_pic_scaling.py parts/grade-2

A picture-level scale= moves a pic but does not scale its drawing (TikZ
applies only the shift to a pic), so the beaker stays 2 cm wide while the
liquid layer or label drawn beside it is scaled: the figure comes out wrong
and every other gate stays green. Found on the grade-2 pilot, 2026-10-02.
Exit 1 on a finding, 2 on a bad path.
"""
import os
import re
import sys

PIC = re.compile(r"\\begin\{tikzpicture\}(\[[^\]]*\])?(.*?)\\end\{tikzpicture\}", re.S)


def main(argv):
    files = []
    for a in argv:
        if os.path.isdir(a):
            for root, _, fs in os.walk(a):
                files += [os.path.join(root, f) for f in fs if f.endswith(".tex")]
        elif os.path.isfile(a):
            files.append(a)
        else:
            print("not a file or directory: %s" % a)
            return 2
    bad = 0
    for f in sorted(files):
        text = open(f, encoding="utf8").read()
        for m in PIC.finditer(text):
            opts, body = m.group(1) or "", m.group(2)
            scaled = re.search(r"\bscale\s*=", opts) or re.search(r"\[[^\]]*\bscale\s*=", body)
            if not scaled:
                continue
            for p in re.finditer(r"\\pic(\[[^\]]*\])?", body):
                if "transform shape" not in (p.group(1) or ""):
                    line = text.count("\n", 0, m.start() + len(m.group(0)) - len(body) + p.start()) + 1
                    print("%s:%d: \\pic without [transform shape] in a scaled picture" % (f, line))
                    bad += 1
    print("%s: %d findings" % ("OK" if not bad else "FAIL", bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

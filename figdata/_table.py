"""Shared helper for figure-data scripts: where a table goes, and how it is written.

A script figdata/<year>/<name>.py computes its curve in functions the test in
tests/<year>/test_<name>.py imports, and writes its table only when run:

    import os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from _table import write_table

    def curve(...): ...

    if __name__ == "__main__":
        write_table(__file__, ("V_mL", "pH"), rows)            # -> figdata/out/<year>-<name>.dat
        write_table(__file__, ("x", "y"), rows2, part="b")     # -> figdata/out/<year>-<name>-b.dat

pgfplots reads it with \\addplot table[x=V_mL, y=pH] {figdata/out/<year>-<name>.dat};
Numbers are written with a fixed format so that `make figdata` leaves no diff.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def out_path(script, part=None, ext=".dat"):
    script = os.path.abspath(script)
    year = os.path.basename(os.path.dirname(script))
    name = os.path.splitext(os.path.basename(script))[0]
    return os.path.join(OUT, "%s-%s%s%s" % (year, name, "-" + part if part else "", ext))


def fmt(v, digits=6):
    if isinstance(v, str):
        return v
    s = "%.*g" % (digits, v)
    return "0" if s in ("-0", "-0.0") else s


def write_table(script, header, rows, part=None, digits=6):
    path = out_path(script, part)
    os.makedirs(OUT, exist_ok=True)
    with open(path, "w", encoding="utf8") as f:
        f.write(" ".join(header) + "\n")
        for r in rows:
            f.write(" ".join(fmt(v, digits) for v in r) + "\n")
    return path

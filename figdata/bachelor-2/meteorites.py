"""Meteorite falls and finds by class group (Year 2, planet-formation-meteorites), from
data/derived/bachelor-2-meteorites.csv (NASA export of the Meteoritical Bulletin Database,
ledger data:b4-meteorites).

  part frac    idx group falls_pct finds_pct    (idx 1 = first group of the CSV)
  part values  what value
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

CSV = os.path.join(HERE, "..", "..", "data", "derived", "bachelor-2-meteorites.csv")
SHORT = {"ordinary chondrite": "ordinary", "carbonaceous chondrite": "carbonaceous",
         "enstatite chondrite": "enstatite", "other chondrite": "other-chondrite",
         "HED achondrite": "HED", "other achondrite": "other-achondrite", "iron": "iron",
         "stony-iron": "stony-iron", "unclassified": "unclassified"}


def load(path=CSV):
    with open(path, encoding="utf8") as f:
        return [(r["group"], int(r["falls"]), int(r["finds"]), int(r["finds_antarctic"]))
                for r in csv.DictReader(f)]


def fractions(rows):
    nf = sum(r[1] for r in rows)
    nd = sum(r[2] for r in rows)
    return [(i + 1, SHORT[g], 100.0 * fa / nf, 100.0 * fi / nd)
            for i, (g, fa, fi, _) in enumerate(rows)], nf, nd


if __name__ == "__main__":
    rows = load()
    fr, nf, nd = fractions(rows)
    write_table(__file__, ("idx", "group", "falls_pct", "finds_pct"), fr, part="frac", digits=4)
    by = {g: r for g, *r in rows}
    chond = sum(by[g][0] for g in by if g.endswith(" chondrite"))
    vals = [("falls", nf), ("finds", nd),
            ("antarctic_finds_pct", 100.0 * sum(r[3] for r in rows) / nd),
            ("chondrite_falls_pct", 100.0 * chond / nf),
            ("ordinary_falls_pct", 100.0 * by["ordinary chondrite"][0] / nf),
            ("hed_falls_pct", 100.0 * by["HED achondrite"][0] / nf),
            ("iron_falls_pct", 100.0 * by["iron"][0] / nf),
            ("iron_finds_pct", 100.0 * by["iron"][1] / nd)]
    write_table(__file__, ("what", "value"), vals, part="values", digits=4)

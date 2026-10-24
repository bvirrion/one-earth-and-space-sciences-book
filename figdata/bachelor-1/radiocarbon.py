"""Radiocarbon age against calendar age: the IntCal20 curve (Year 1,
radiometric-methods).

The IntCal20 Northern Hemisphere calibration curve (Reimer et al. 2020), dataset
bachelor-1-intcal20.csv (ledger data:b3-intcal20, reimer20:intcal20): conventional
radiocarbon age (14C yr BP) and its one-sigma uncertainty against calendar age
(cal yr BP, 0 = AD 1950), every year to 5 cal kBP, then every 5, 10 and 20 years.

  part curve    cal c14 lo hi     (0-12 cal kBP every 10 yr, in kyr; +- one sigma)
  part zoom     cal c14 lo hi     (2300-2900 cal BP every year, in yr)
  part values   what value
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
DATA = os.path.join(ROOT, "data", "derived", "bachelor-1-intcal20.csv")

LIBBY = 5568.0      # yr, half-life of the conventional age (sp77:conventional-age)
MODERN = 5700.0     # yr, half-life of 14C (iaea:c14)


def read():
    """{cal_bp: (c14_age, c14_sigma)}."""
    out = {}
    with open(DATA, encoding="utf8") as f:
        for r in csv.DictReader(f):
            out[int(r["cal_bp"])] = (int(r["c14_age"]), int(r["c14_sigma"]))
    return out


def window(cur, a, b, step=1):
    return [(c, cur[c][0], cur[c][0] - cur[c][1], cur[c][0] + cur[c][1])
            for c in range(a, b + 1, step) if c in cur]


def calendar_range(cur, c14, sigma, a=0, b=55000):
    """(oldest, youngest, count) of the calendar years whose curve value lies
    within c14 +- sigma (the curve's own uncertainty ignored)."""
    hits = [c for c in cur if a <= c <= b and abs(cur[c][0] - c14) <= sigma]
    return (max(hits), min(hits), len(hits)) if hits else None


if __name__ == "__main__":
    cur = read()
    write_table(__file__, ("cal", "c14", "lo", "hi"),
                [(c / 1000.0, y / 1000.0, lo / 1000.0, hi / 1000.0)
                 for c, y, lo, hi in window(cur, 0, 12000, 10)], part="curve")
    write_table(__file__, ("cal", "c14", "lo", "hi"), window(cur, 2300, 2900), part="zoom")
    old, young, _ = calendar_range(cur, 2480, 15, 2000, 3000)
    vals = [("rows", len(cur)), ("cal_max", max(cur)),
            ("c14_at_2000", cur[2000][0]), ("sigma_at_2000", cur[2000][1]),
            ("c14_at_8000", cur[8000][0]), ("c14_at_12000", cur[12000][0]),
            ("offset_at_12000", 12000 - cur[12000][0]),
            ("plateau_oldest_for_2480pm15", old), ("plateau_youngest_for_2480pm15", young),
            ("libby_over_modern", MODERN / LIBBY)]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

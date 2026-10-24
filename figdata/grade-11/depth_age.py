"""Depth of the ocean floor against its age (grade 11, ocean-ridges).

Each 1-degree cell with an age (Seton et al. 2020 grid, data/derived/grade-11-seafloor-
age.csv, ledger data:b2-seafloor-age) is matched with its ETOPO1 elevation (data/
derived/etopo-1deg.csv, data:etopo1). Cells are grouped by age (bins of 5 Myr, the first
of 2.5 Myr); the median depth of each bin and its interquartile range are written.

Parsons and Sclater (1977, ps77:depth-age): d = 2500 + 350 sqrt(t) m from 0 to 70 Myr,
and d = 6400 - 3200 exp(-t/62.8) m beyond 20 Myr. The script fits d = a + b sqrt(t) to the
bin medians up to 70 Myr (least squares) to check the published coefficients.

The cells include seamounts, plateaus and thick sediments near the continents; the
median keeps them from pulling the curve.

  part bins     age depth q1 q3 n em ep   (depth positive downward, m; em, ep the
                distances from the median to the quartiles, for error bars)
  part sqrt     age depth              Parsons-Sclater square-root law, 0-70 Myr (its stated range)
  part exp      age depth              Parsons-Sclater exponential, 20-180 Myr
  part numbers  key value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EDGES = [0.0, 2.5] + [5.0 * k for k in range(1, 37)]       # 0, 2.5, 5, ..., 180


def ps_sqrt(t):
    return 2500.0 + 350.0 * math.sqrt(t)


def ps_exp(t):
    return 6400.0 - 3200.0 * math.exp(-t / 62.8)


def cells():
    """[(age Myr, depth m)] for every dated 1-degree cell below sea level."""
    elev = {}
    with open(os.path.join(ROOT, "data", "derived", "etopo-1deg.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            elev[(r["lat"], r["lon"])] = float(r["elev_m"])
    out = []
    with open(os.path.join(ROOT, "data", "derived", "grade-11-seafloor-age.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            e = elev.get((r["lat"], r["lon"]))
            if e is not None and e < 0:
                out.append((float(r["age"]), -e))
    return out


def quantile(v, q):
    v = sorted(v)
    x = q * (len(v) - 1)
    i = int(math.floor(x))
    j = min(i + 1, len(v) - 1)
    return v[i] + (x - i) * (v[j] - v[i])


def bins(cs=None):
    cs = cs if cs is not None else cells()
    out = []
    for lo, hi in zip(EDGES[:-1], EDGES[1:]):
        d = [dep for a, dep in cs if lo <= a < hi]
        if len(d) >= 20:
            out.append((0.5 * (lo + hi), quantile(d, 0.5), quantile(d, 0.25), quantile(d, 0.75), len(d)))
    return out


def fit_sqrt(bs, tmax=70.0):
    """Least-squares a, b of d = a + b sqrt(t) through the bin medians with t <= tmax."""
    pts = [(math.sqrt(t), d) for t, d, _, _, _ in bs if t <= tmax]
    n = len(pts)
    mx = sum(x for x, _ in pts) / n
    my = sum(y for _, y in pts) / n
    b = sum((x - mx) * (y - my) for x, y in pts) / sum((x - mx) ** 2 for x, _ in pts)
    return my - b * mx, b


def numbers():
    bs = bins()
    a, b = fit_sqrt(bs)
    near = lambda t: [d for tt, d, _, _, _ in bs if abs(tt - t) < 1e-9][0]
    return {"fit_a": a, "fit_b": b, "median_2.5_5": near(3.75), "median_60_65": near(62.5),
            "median_120_125": near(122.5), "ps_64": ps_sqrt(64.0), "ps_exp_64": ps_exp(64.0),
            "ps_exp_inf": 6400.0, "n_cells": sum(r[4] for r in bs)}


if __name__ == "__main__":
    bs = bins()
    write_table(__file__, ("age", "depth", "q1", "q3", "n", "em", "ep"),
                [r + (r[1] - r[2], r[3] - r[1]) for r in bs], part="bins", digits=6)
    write_table(__file__, ("age", "depth"), [(t, ps_sqrt(t)) for t in [k * 0.5 for k in range(0, 141)]],
                part="sqrt", digits=6)
    write_table(__file__, ("age", "depth"), [(t, ps_exp(t)) for t in range(20, 181, 2)], part="exp", digits=6)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

"""Depth of the ocean floor against its age (Year 1, rifts-ridges-margins).

Every one-degree ocean cell that has both a depth and an age:
  * depth from ETOPO1 sampled at one degree (shared dataset etopo-1deg.csv, ledger
    data:etopo1): the depth of the sea floor, sediments included;
  * age from the Seton et al. (2020) age grid, median of each one-degree cell
    (shared dataset grade-11-seafloor-age.csv, ledger data:b2-seafloor-age).
Cells shallower than 1000 m below sea level (islands, seamount summits, shelves
and the cells cut by a coast) are left out.

The cells are binned by age (2-Myr bins to 180 Ma); each bin gives the median
depth and the quartiles. A least-squares fit of d = d_r + C sqrt(t) to the bin
medians younger than 70 Ma gives the constants "from data"; the curves of the
cooling half-space (d = 2500 + 350 sqrt t) and of the cooling plate
(d = 6400 - 3200 exp(-t / 62.8)), both in metres with t in Myr, are those of
Parsons and Sclater (1977), ledger rows parsons:plate-model and ps77:depth-age.

  part bins    t n q1 median q3          (t = bin centre, Myr; depths in m)
  part models  t halfspace plate fit     (every Myr, 0 to 180)
  part values  what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
ETOPO = os.path.join(ROOT, "data", "derived", "etopo-1deg.csv")
AGES = os.path.join(ROOT, "data", "derived", "grade-11-seafloor-age.csv")
BIN = 2.0
TMAX = 180.0
MIN_DEPTH = 1000.0
FIT_TMAX = 70.0


def halfspace(t, d_r=2500.0, c=350.0):
    """Depth (m) of sea floor of age t (Myr), cooling half-space."""
    return d_r + c * math.sqrt(t)


def plate(t):
    """Depth (m), cooling plate (Parsons and Sclater 1977)."""
    return 6400.0 - 3200.0 * math.exp(-t / 62.8)


def halfspace_coefficient(alpha, rho_m, rho_w, t_m, kappa):
    """C in d = d_r + C sqrt(t), m per sqrt(Myr): (2/sqrt(pi)) alpha_eff T_m sqrt(kappa),
    with alpha_eff = alpha rho_m / (rho_m - rho_w) and kappa in m2/s."""
    myr = 1e6 * 365.25 * 86400.0
    return 2.0 / math.sqrt(math.pi) * alpha * rho_m / (rho_m - rho_w) * t_m * math.sqrt(kappa * myr)


def cells():
    """[(age Myr, depth m)] for every cell with both values."""
    depth = {}
    with open(ETOPO, encoding="utf8") as f:
        for r in csv.DictReader(f):
            depth[(float(r["lat"]), float(r["lon"]))] = -float(r["elev_m"])
    out = []
    with open(AGES, encoding="utf8") as f:
        for r in csv.DictReader(f):
            key = (float(r["lat"]), float(r["lon"]))
            d = depth.get(key)
            if d is not None and d >= MIN_DEPTH:
                out.append((float(r["age"]), d))
    return out


def quantile(sorted_vals, q):
    """Linear-interpolation quantile of a sorted list."""
    if not sorted_vals:
        raise ValueError("empty")
    x = q * (len(sorted_vals) - 1)
    i = int(math.floor(x))
    j = min(i + 1, len(sorted_vals) - 1)
    return sorted_vals[i] + (x - i) * (sorted_vals[j] - sorted_vals[i])


def bins(data=None):
    data = cells() if data is None else data
    groups = {}
    for t, d in data:
        if 0.0 <= t < TMAX:
            groups.setdefault(int(t // BIN), []).append(d)
    out = []
    for k in sorted(groups):
        v = sorted(groups[k])
        out.append(((k + 0.5) * BIN, len(v), quantile(v, 0.25), quantile(v, 0.5), quantile(v, 0.75)))
    return out


def fit_sqrt(rows, tmax=FIT_TMAX):
    """Least squares d = a + c sqrt(t) on (t, median) pairs with t < tmax."""
    pts = [(math.sqrt(t), m) for t, _, _, m, _ in rows if t < tmax]
    n = len(pts)
    sx = sum(x for x, _ in pts)
    sy = sum(y for _, y in pts)
    sxx = sum(x * x for x, _ in pts)
    sxy = sum(x * y for x, y in pts)
    c = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    a = (sy - c * sx) / n
    return a, c


if __name__ == "__main__":
    data = cells()
    rows = bins(data)
    write_table(__file__, ("t", "n", "q1", "median", "q3"), rows, part="bins", digits=6)
    a, c = fit_sqrt(rows)
    models = [(t, halfspace(t), plate(t), a + c * math.sqrt(t)) for t in [float(k) for k in range(0, 181)]]
    write_table(__file__, ("t", "halfspace", "plate", "fit"), models, part="models", digits=6)
    old = [m for t, _, _, m, _ in rows if 150.0 <= t < 180.0]
    vals = [("n_cells", len(data)), ("fit_dr", a), ("fit_c", c),
            ("c_book", halfspace_coefficient(3.2e-5, 3300.0, 1000.0, 1350.0, 1e-6)),
            ("median_150_180", sorted(old)[len(old) // 2] if old else float("nan")),
            ("halfspace_80", halfspace(80.0)), ("plate_80", plate(80.0))]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

"""How much of the Earth's surface lies at each elevation (grade 11,
lithosphere-asthenosphere).

Source: ETOPO1 sampled at 1 degree (shared dataset data:etopo1,
data/derived/etopo-1deg.csv); each cell is weighted by its area (cos latitude).
The surface over Antarctica and Greenland is the top of the ice.

  part bins     lo hi mid share_pct land       500 m bins, -11000 to 9000 m
  part curve    share_above_pct elev_m         the hypsometric curve (fraction of the
                                               surface higher than each elevation)
  part tibet    lat lon elev_m                 the plateau box used in the problem
  part numbers  key value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BIN = 500.0
TIBET = (31.0, 35.0, 80.0, 95.0)        # lat1, lat2, lon1, lon2 (cell centres), chosen box
QAIDAM = (36.5, 38.0, 91.0, 96.0)


def cells():
    with open(os.path.join(ROOT, "data", "derived", "etopo-1deg.csv"), encoding="utf8") as f:
        return [(float(r["lat"]), float(r["lon"]), float(r["elev_m"])) for r in csv.DictReader(f)]


def weight(lat):
    return math.cos(math.radians(lat))


def histogram(cs=None):
    cs = cs or cells()
    total = sum(weight(a) for a, _, _ in cs)
    out = []
    lo = -11000.0
    while lo < 9000.0:
        hi = lo + BIN
        s = sum(weight(a) for a, _, e in cs if lo < e <= hi)
        out.append((lo, hi, 0.5 * (lo + hi), 100.0 * s / total, 1 if lo >= 0 else 0))
        lo = hi
    return out


def modes(hist=None):
    """Highest bin above sea level and highest bin below it: (mid, share)."""
    hist = hist or histogram()
    land = max((h for h in hist if h[0] >= 0), key=lambda h: h[3])
    sea = max((h for h in hist if h[1] <= 0), key=lambda h: h[3])
    return (land[2], land[3]), (sea[2], sea[3])


def curve(cs=None, n=200):
    cs = sorted(cs or cells(), key=lambda c: -c[2])
    total = sum(weight(a) for a, _, _ in cs)
    out, acc = [(0.0, cs[0][2])], 0.0
    step = len(cs) // n
    for k, (a, _, e) in enumerate(cs):
        acc += weight(a)
        if k % step == 0 or k == len(cs) - 1:
            out.append((100.0 * acc / total, e))
    return out


def mean_in(box, cs=None):
    cs = cs or cells()
    la1, la2, lo1, lo2 = box
    sel = [(a, e) for a, b, e in cs if la1 <= a <= la2 and lo1 <= b <= lo2]
    return sum(weight(a) * e for a, e in sel) / sum(weight(a) for a, e in sel)


def numbers():
    cs = cells()
    total = sum(weight(a) for a, _, _ in cs)
    land = [(a, b, e) for a, b, e in cs if e > 0]
    sea = [(a, b, e) for a, b, e in cs if e <= 0]
    wl = sum(weight(a) for a, _, _ in land)
    nonant = [(a, e) for a, _, e in land if a > -60]
    (lm, ls), (sm, ss) = modes(histogram(cs))
    return {"land_fraction": wl / total,
            "mean_land_m": sum(weight(a) * e for a, _, e in land) / wl,
            "mean_land_no_antarctica_m": sum(weight(a) * e for a, e in nonant) / sum(weight(a) for a, _ in nonant),
            "mean_ocean_m": sum(weight(a) * e for a, _, e in sea) / sum(weight(a) for a, _, _ in sea),
            "land_mode_mid_m": lm, "land_mode_pct": ls, "sea_mode_mid_m": sm, "sea_mode_pct": ss,
            "tibet_mean_m": mean_in(TIBET, cs), "qaidam_mean_m": mean_in(QAIDAM, cs),
            "share_above_2000_pct": 100.0 * sum(weight(a) for a, _, e in cs if e > 2000) / total,
            "share_below_3000_pct": 100.0 * sum(weight(a) for a, _, e in cs if e < -3000) / total}


if __name__ == "__main__":
    cs = cells()
    write_table(__file__, ("lo", "hi", "mid", "share_pct", "land"), histogram(cs), part="bins")
    write_table(__file__, ("share_above_pct", "elev_m"), curve(cs), part="curve")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

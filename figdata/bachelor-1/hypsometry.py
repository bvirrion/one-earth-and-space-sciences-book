"""The Earth's hypsometry (Year 1, isostasy-gravity): the hypsometric curve and the
histogram of elevations, from ETOPO1 sampled at 1 degree (shared dataset
data/derived/etopo-1deg.csv, ledger data:etopo1; ice-surface elevations).

Each node stands for the 1-degree cell centred on it, of exact area
R^2 * dlon * (sin(lat + 0.5 deg) - sin(lat - 0.5 deg)); the weights sum to 4 pi R^2.

  part curve      area_pc elev       elevation exceeded by area_pc per cent of the
                                     surface (the hypsometric curve), every 0.5 %
  part histogram  elev pc            per cent of the surface in 500-m bins (centre)
  part values     what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
ETOPO = os.path.join(ROOT, "data", "derived", "etopo-1deg.csv")
R = 6371.0e3        # m, ledger earth:Rmean
BIN = 500.0         # m


def cells():
    """[(elevation m, area m2)] for every 1-degree node."""
    out = []
    d = math.radians(1.0)
    with open(ETOPO, encoding="utf8") as f:
        for r in csv.DictReader(f):
            lat = float(r["lat"])
            a = R * R * d * (math.sin(math.radians(lat + 0.5)) - math.sin(math.radians(lat - 0.5)))
            out.append((float(r["elev_m"]), a))
    return out


_C = None


def _cells():
    global _C
    if _C is None:
        _C = sorted(cells(), key=lambda c: -c[0])
    return _C


def total_area():
    return sum(a for _, a in _cells())


def fraction_below(level=0.0):
    tot = total_area()
    return sum(a for e, a in _cells() if e < level) / tot


def mean_elevation(sel=None):
    cs = [(e, a) for e, a in _cells() if sel is None or sel(e)]
    return sum(e * a for e, a in cs) / sum(a for _, a in cs)


def hypsometric_curve(step_pc=0.5):
    """Elevation exceeded by each fraction of the surface."""
    cs = _cells()
    tot = total_area()
    out, acc, i = [], 0.0, 0
    targets = [k * step_pc for k in range(int(100 / step_pc) + 1)]
    for t in targets:
        while i < len(cs) - 1 and (acc + cs[i][1]) / tot * 100.0 < t:
            acc += cs[i][1]
            i += 1
        out.append((t, cs[i][0]))
    return out


def histogram():
    tot = total_area()
    h = {}
    for e, a in _cells():
        k = math.floor(e / BIN)
        h[k] = h.get(k, 0.0) + a
    return [((k + 0.5) * BIN, 100.0 * h[k] / tot) for k in sorted(h)]


def modes():
    """Centres of the most populated bin above and below sea level."""
    hist = histogram()
    land = max((p, e) for e, p in hist if e > 0)[1]
    sea = max((p, e) for e, p in hist if e < 0)[1]
    return land, sea


if __name__ == "__main__":
    write_table(__file__, ("area_pc", "elev"), hypsometric_curve(), part="curve", digits=6)
    write_table(__file__, ("elev", "pc"), histogram(), part="histogram", digits=6)
    land_mode, sea_mode = modes()
    vals = [("fraction_below_sea_level", fraction_below(0.0)),
            ("mean_elevation", mean_elevation()),
            ("mean_land_elevation", mean_elevation(lambda e: e >= 0)),
            ("mean_ocean_depth", -mean_elevation(lambda e: e < 0)),
            ("land_mode_bin_centre", land_mode),
            ("sea_mode_bin_centre", sea_mode),
            ("total_area_over_4piR2", total_area() / (4 * math.pi * R * R))]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

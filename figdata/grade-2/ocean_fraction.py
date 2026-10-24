"""How much of the Earth's surface is ocean (grade 2, water-on-earth).

Reads the ETOPO1 relief at 1 degree (data/derived/etopo-1deg.csv; ledger
data:etopo1) and adds up the area of the cells below sea level, each cell
weighted by cos(latitude) (a 1-degree cell near a pole is much smaller than
one at the equator). The result, about 71 %, is the "7 squares out of 10" of
the chapter and is checked against the USGS figure (ledger usgs-wss:ocean-cover).
Lakes below sea level (the Caspian) count as sea here: a few hundredths of a
percent, invisible at the precision printed.

  part grid : a 10 x 10 grid of squares, `blue` = 1 for the first N squares
              (N = the rounded percentage), read row by row from the top left.
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def cells():
    with open(os.path.join(ROOT, "data", "derived", "etopo-1deg.csv"), encoding="utf8") as f:
        return [(float(r["lat"]), float(r["lon"]), float(r["elev_m"])) for r in csv.DictReader(f)]


def ocean_fraction(rows=None):
    rows = rows or cells()
    tot = sea = 0.0
    for lat, _lon, z in rows:
        w = math.cos(math.radians(lat))
        tot += w
        if z < 0:
            sea += w
    return sea / tot


def grid(percent):
    """(col, row, blue) for a 10 x 10 grid: the first `percent` squares are blue."""
    out = []
    for k in range(100):
        row, col = divmod(k, 10)
        out.append((col, 9 - row, 1 if k < percent else 0))
    return out


if __name__ == "__main__":
    f = ocean_fraction()
    pct = round(100 * f)
    write_table(__file__, ("col", "row", "blue"), grid(pct), part="grid")
    write_table(__file__, ("fraction", "percent"), [(round(f, 4), pct)])
    print("ocean fraction %.4f -> %d %%" % (f, pct))

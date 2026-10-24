"""Free-air gravity anomaly and depth across the Kuril Trench (Year 1, active-margins).

Data: the Scripps satellite marine gravity model and topography, one box around the
Kuril section (shared dataset bachelor-1-grav-kuril.csv, ledger data:b3-grav-kuril):
lon, lat, free-air anomaly (mGal), depth (m, positive below sea level), on a grid of
about 4 by 3 arc-minutes.

The profile follows the section of slab_seismicity.py: it starts at the PB2002 trench
point and runs perpendicular to the trench toward the overriding plate; x < 0 is
seaward. Each sample is the bilinear interpolation of the four grid nodes around it
(the grid is regular in lon and lat).

  part profile  x faa depth            (x in km, every 5 km from -250 to 450)
  part values   what value
"""
import bisect
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _table import write_table  # noqa: E402
import slab_seismicity as ss  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
GRID = os.path.join(ROOT, "data", "derived", "bachelor-1-grav-kuril.csv")
XMIN, XMAX, DX = -250.0, 450.0, 5.0


def grid():
    """(lons, lats, faa dict, depth dict) keyed by (lon, lat)."""
    faa, dep = {}, {}
    with open(GRID, encoding="utf8") as f:
        for r in csv.DictReader(f):
            k = (float(r["lon"]), float(r["lat"]))
            faa[k] = float(r["faa_mgal"])
            dep[k] = float(r["depth_m"])
    lons = sorted({k[0] for k in faa})
    lats = sorted({k[1] for k in faa})
    return lons, lats, faa, dep


def bilinear(lons, lats, table, lon, lat):
    """Bilinear interpolation of a regular lon-lat table; None outside the grid."""
    i = bisect.bisect_right(lons, lon) - 1
    j = bisect.bisect_right(lats, lat) - 1
    if i < 0 or j < 0 or i + 1 >= len(lons) or j + 1 >= len(lats):
        return None
    x0, x1, y0, y1 = lons[i], lons[i + 1], lats[j], lats[j + 1]
    u, v = (lon - x0) / (x1 - x0), (lat - y0) / (y1 - y0)
    try:
        q = [table[(x0, y0)], table[(x1, y0)], table[(x0, y1)], table[(x1, y1)]]
    except KeyError:
        return None
    return (1 - u) * (1 - v) * q[0] + u * (1 - v) * q[1] + (1 - u) * v * q[2] + u * v * q[3]


def profile(g=None):
    """[(x km, faa mGal, depth m)] along the Kuril section."""
    lons, lats, faa, dep = grid() if g is None else g
    origin, _, toward, _, _ = ss.trench()
    out = []
    n = int(round((XMAX - XMIN) / DX))
    for k in range(n + 1):
        x = XMIN + k * DX
        lon, lat = ss.destination(origin[0], origin[1], toward if x >= 0 else (toward + 180.0) % 360.0, abs(x))
        a = bilinear(lons, lats, faa, lon, lat)
        d = bilinear(lons, lats, dep, lon, lat)
        if a is not None and d is not None:
            out.append((x, a, d))
    return out


def extremes(rows):
    """Trench low (x, faa), outer-rise high seaward of it, the deepest point, the mean
    depth of the abyssal floor 150-250 km seaward, and the forearc-arc high landward."""
    low = min(rows, key=lambda r: r[1])
    sea = [r for r in rows if r[0] < low[0] - 50.0]
    rise = max(sea, key=lambda r: r[1])
    deep = max(rows, key=lambda r: r[2])
    abyss = [r[2] for r in rows if -250.0 <= r[0] <= -150.0]
    land = [r for r in rows if low[0] < r[0] <= 250.0]
    high = max(land, key=lambda r: r[1])
    return low, rise, deep, sum(abyss) / len(abyss), high


if __name__ == "__main__":
    rows = profile()
    write_table(__file__, ("x", "faa", "depth"), rows, part="profile", digits=6)
    low, rise, deep, abyss, high = extremes(rows)
    vals = [("low_x", low[0]), ("low_faa", low[1]), ("rise_x", rise[0]), ("rise_faa", rise[1]),
            ("deep_x", deep[0]), ("deep_depth", deep[2]), ("abyss_depth", abyss),
            ("trench_relief", deep[2] - abyss), ("high_x", high[0]), ("high_faa", high[1])]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

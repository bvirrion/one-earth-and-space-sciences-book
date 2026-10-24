"""The flood zone of the Varden Hills river and a village, for grade 9,
chapter 2 (living with natural risks), and its weekend problem.

Built on the shared region (figdata/shared/region.py): the ground elevation
topo(x, y), the river line river_y(x) and its level river_z(x). The flood
zone is every point whose ground lies at most H_FLOOD metres above the river
level at the same x: the area a flood H_FLOOD metres deep over the river
would cover. Because the hills rise steadily away from the river, the zone
is a band; its two edges are found by bisection at each x.

The village (HOUSES) and the three possible school sites (SITES) are
exercise data, placed relative to the river line; the fault is the region's
normal fault (its ground trace is read from the shared table).

Map window WINDOW (m). Coordinates are written in km.

  part zone      : x_km y_km      (closed polygon of the flood zone)
  parts zone2, zone10 : the same for floods 2 m and 10 m above the river
  part contours  : x_km y_km      (every 10 m, index contours left out)
  part index     : x_km y_km      (every 50 m)
  part index-lab : x_km y_km z    (one label per index contour)
  part river     : x_km y_km
  part houses-in, houses-out : x_km y_km
  part sites     : x_km y_km name
  main table     : item value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region as rg  # noqa: E402

WINDOW = (3500.0, 7000.0, 2700.0, 5500.0)     # xmin, xmax, ymin, ymax (m)
H_FLOOD = 5.0                                 # m above the river: the flood of the problem
STEP = 20.0

# houses: (x, signed distance from the river line in y, m) -- exercise data
HOUSES = [(4300, 120), (4380, -160), (4450, 210), (4520, -90), (4600, 160), (4660, -200),
          (4720, 210), (4790, -140), (4850, 380), (4900, 110), (4960, -370), (5020, 190),
          (5080, -60), (5150, 420), (5200, -200), (5260, 200), (5330, 140), (5400, -380),
          (5470, 200), (5530, -120), (5600, 520), (5680, 380), (4560, 460), (4800, -470),
          (5050, -560), (5350, 600), (4250, -380), (5750, -200)]
# every house lies at least 60 m (about 2 mm on the printed map) from the zone edge
# school sites: name, x, signed distance from the river (m) -- exercise data
SITES = [("A", 4700.0, 60.0), ("B", 6300.0, 800.0), ("C", 3800.0, -1000.0)]


def height_above_river(x, y):
    return rg.topo(x, y) - rg.river_z(x)


def in_zone(x, y, h=H_FLOOD):
    return height_above_river(x, y) <= h


def edge(x, side, h=H_FLOOD):
    """Distance (m) from the river line to the zone edge, on one side (+1 north, -1 south)."""
    lo, hi = 0.0, 2000.0
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        if height_above_river(x, rg.river_y(x) + side * mid) <= h:
            lo = mid
        else:
            hi = mid
    return lo


def zone_polygon(h=H_FLOOD, dx=25.0):
    x0, x1 = WINDOW[0], WINDOW[1]
    xs = list(np.arange(x0, x1 + 0.1, dx))
    north = [(x, rg.river_y(x) + edge(x, +1, h)) for x in xs]
    south = [(x, rg.river_y(x) - edge(x, -1, h)) for x in reversed(xs)]
    return north + south + [north[0]]


def house_points():
    return [(x, rg.river_y(x) + d) for x, d in HOUSES]


def houses_in_zone():
    return [p for p in house_points() if in_zone(*p)]


def slope_percent(x, y, d=10.0):
    gx = (rg.topo(x + d, y) - rg.topo(x - d, y)) / (2 * d)
    gy = (rg.topo(x, y + d) - rg.topo(x, y - d)) / (2 * d)
    return 100.0 * math.hypot(gx, gy)


def fault_trace():
    """The region's fault trace on the ground (m), read from the shared table."""
    pts = []
    path = os.path.join(HERE, "..", "out", "shared-region-fault.dat")
    with open(path, encoding="utf8") as f:
        next(f)
        for line in f:
            p = line.split()
            if len(p) == 2:
                pts.append((1000 * float(p[0]), 1000 * float(p[1])))
    return pts


def distance_to_fault(x, y):
    tr = fault_trace()
    best = 1e18
    for (ax, ay), (bx, by) in zip(tr, tr[1:]):
        vx, vy = bx - ax, by - ay
        t = max(0.0, min(1.0, ((x - ax) * vx + (y - ay) * vy) / (vx * vx + vy * vy)))
        best = min(best, math.hypot(x - ax - t * vx, y - ay - t * vy))
    return best


def site_table():
    out = []
    for name, x, d in SITES:
        y = rg.river_y(x) + d
        out.append((name, x, y, height_above_river(x, y), slope_percent(x, y), distance_to_fault(x, y),
                    in_zone(x, y)))
    return out


def _grid():
    x0, x1, y0, y1 = WINDOW
    xs = np.arange(x0, x1 + 0.1, STEP)
    ys = np.arange(y0, y1 + 0.1, STEP)
    z = np.array([[rg.topo(x, y) for x in xs] for y in ys])
    return xs, ys, z


if __name__ == "__main__":
    km = lambda pts: [(round(x / 1000, 4), round(y / 1000, 4)) for x, y in pts]  # noqa: E731
    write_table(__file__, ("x_km", "y_km"), km(zone_polygon()), part="zone")
    for h in (2, 10):
        write_table(__file__, ("x_km", "y_km"), km(zone_polygon(h=float(h))), part="zone%d" % h)
    xs, ys, z = _grid()
    rows, irows, labs = [], [], []
    for lv in range(100, 460, 10):
        lines = [rg.simplify(l, 2.0) for l in rg.trace(z, xs, ys, lv)]
        lines = [l for l in lines if len(l) > 1]
        target = irows if lv % 50 == 0 else rows
        for l in lines:
            target += ([()] if target else []) + km(l)
        if lv % 50 == 0 and lines:
            longest = max(lines, key=len)
            mx, my = longest[len(longest) // 2]
            labs.append((round(mx / 1000, 4), round(my / 1000, 4), lv))
    write_table(__file__, ("x_km", "y_km"), rows, part="contours")
    write_table(__file__, ("x_km", "y_km"), irows, part="index")
    write_table(__file__, ("x_km", "y_km", "z"), labs, part="index-lab")
    write_table(__file__, ("x_km", "y_km"), km([(x, rg.river_y(x)) for x in np.arange(WINDOW[0], WINDOW[1] + 1, 25.0)]),
                part="river")
    inside = houses_in_zone()
    write_table(__file__, ("x_km", "y_km"), km(inside), part="houses-in")
    write_table(__file__, ("x_km", "y_km"), km([p for p in house_points() if p not in inside]), part="houses-out")
    st = site_table()
    write_table(__file__, ("x_km", "y_km", "name"), [(round(x / 1000, 4), round(y / 1000, 4), n) for n, x, y, *_ in st],
                part="sites")
    rows = [("houses", len(HOUSES)), ("houses_in_zone", len(inside)),
            ("river_z_at_4700", round(rg.river_z(4700), 1)), ("river_z_at_6250", round(rg.river_z(6250), 1))]
    for n, x, y, h, s, dfault, inz in st:
        rows += [("site_%s_height_m" % n, round(h, 1)), ("site_%s_ground_m" % n, round(rg.topo(x, y), 1)),
                 ("site_%s_slope_pct" % n, round(s, 1)), ("site_%s_fault_m" % n, round(dfault)),
                 ("site_%s_in_zone" % n, int(inz))]
    write_table(__file__, ("item", "value"), rows)
    for r in rows:
        print(r)

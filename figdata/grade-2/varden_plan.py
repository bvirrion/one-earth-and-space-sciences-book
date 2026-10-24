"""A simple map of the Varden Hills for young readers (grade 2, drawing-to-map).

Imports the series' region (figdata/shared/region.py, never edited) and keeps
only what a seven-year-old reads on a map: the high ground (above HILL_Z m),
the river, one road with its bridge, a farm, a village and a wood. The map is
10 km x 8 km; the chapter draws it on a grid of 1 km squares (its scale:
1 square = 1 km).

  part hills    : x_km y_km rings of ground above HILL_Z (fill even odd)
  part road     : the road, west to east
  part wood     : the wood (closed)
  part points   : name x_km y_km (bridge, farm, village)
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

HILL_Z = 400.0
STEP = 50.0
FARM = (2500.0, 3500.0)        # centres of 1 km squares: the exercises count whole squares
VILLAGE = (7500.0, 5500.0)
WOOD = (8500.0, 1500.0, 900.0, 600.0)          # centre x, y, semi-axes (m)
ROAD = [(0.0, 2900.0), (2500.0, 3200.0), (5000.0, 3400.0), (5800.0, 4300.0),
        (7500.0, 5300.0), (10000.0, 6000.0)]


def hills():
    xs = np.arange(0.0, region.WIDTH + STEP / 2, STEP)
    ys = np.arange(0.0, region.HEIGHT + STEP / 2, STEP)
    z = np.array([[region.topo(x, y) for x in xs] for y in ys])
    codes = (z > HILL_Z).astype(int)
    return region.unit_polygons(codes, xs, ys, tol=20.0).get(1, [])


def road_points(n=40):
    pts = []
    for (x0, y0), (x1, y1) in zip(ROAD, ROAD[1:]):
        for k in range(n):
            t = k / n
            pts.append((x0 + t * (x1 - x0), y0 + t * (y1 - y0)))
    pts.append(ROAD[-1])
    return pts


def bridge():
    """Where the road crosses the river: the sign change of y - river_y(x)."""
    pts = road_points(400)
    out = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        a, b = y0 - region.river_y(x0), y1 - region.river_y(x1)
        if a == 0 or a * b < 0:
            t = a / (a - b)
            out.append((x0 + t * (x1 - x0), y0 + t * (y1 - y0)))
    return out


def wood(n=48):
    cx, cy, a, b = WOOD
    return [(cx + a * math.cos(2 * math.pi * k / n), cy + b * math.sin(2 * math.pi * k / n))
            for k in range(n + 1)]


def on_floor(x, y):
    return abs(y - region.river_y(x)) <= region.FLOOR_HALF


if __name__ == "__main__":
    km = lambda p: (round(p[0] / 1000, 3), round(p[1] / 1000, 3))  # noqa: E731
    rows = []
    for r in hills():
        rows += [km(p) for p in r] + [("nan", "nan")]
    write_table(__file__, ("x_km", "y_km"), rows, part="hills")
    write_table(__file__, ("x_km", "y_km"), [km(p) for p in ROAD], part="road")
    write_table(__file__, ("x_km", "y_km"), [km(p) for p in wood()], part="wood")
    (bx, by), = bridge()
    write_table(__file__, ("name", "x_km", "y_km"),
                [("bridge",) + km((bx, by)), ("farm",) + km(FARM), ("village",) + km(VILLAGE)],
                part="points")
    print("bridge at", km((bx, by)))

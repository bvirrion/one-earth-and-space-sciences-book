"""The V-rule, computed (Year 1, geological-maps).

A synthetic valley 2 km x 2 km (x east, y north, metres): the river flows
NORTH down the axis x = 0 with a gradient of 30 m per km, and the valley sides
rise at 60 m per km:  z = 400 - 0.03 y + 0.06 |x|.  Five planar contacts, all
striking east-west and passing through (0, 1000, 370), are cut by this ground;
the outcrop is traced where ground = plane (marching squares, the tracer of
figdata/shared/region.py). The cases are the five of the V-rule theorem:

  h  horizontal
  u  dipping 10 degrees upstream (south)
  d  dipping 10 degrees downstream (north), steeper than the valley floor
  g  dipping 1 degree downstream, gentler than the valley floor (1.72 deg)
  v  vertical

  part contours            x_km y_km   the 10 m contours (jumps between lines)
  part <case>              x_km y_km   the outcrop trace of each case
  part apex                case y_axis_km y_side_km   the trace on the axis and
                                         400 m to the side
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
from region import trace, simplify  # noqa: E402

GRAD, SIDE = 0.03, 0.06
P0 = (0.0, 1000.0, 370.0)
CASES = {"h": ("horizontal", 0.0, 1), "u": ("upstream", 10.0, -1),
         "d": ("downstream steep", 10.0, 1), "g": ("downstream gentle", 1.0, 1),
         "v": ("vertical", 90.0, 1)}


def ground(x, y):
    return 400.0 - GRAD * y + SIDE * abs(x)


def plane_minus_ground(case, x, y):
    """Signed: ground - plane elevation (vertical plane: y - y0)."""
    _, dip, sense = CASES[case]
    if dip == 90.0:
        return y - P0[1]
    zp = P0[2] - sense * math.tan(math.radians(dip)) * (y - P0[1])   # sense +1: lower to the north
    return ground(x, y) - zp


def outcrop_y(case, x):
    """y of the outcrop at abscissa x (bisection on y in [-20 km, 20 km])."""
    a, b = -20000.0, 20000.0
    fa = plane_minus_ground(case, x, a)
    for _ in range(200):
        m = (a + b) / 2
        fm = plane_minus_ground(case, x, m)
        if (fa > 0) == (fm > 0):
            a, fa = m, fm
        else:
            b = m
    return (a + b) / 2


def grid():
    xs = np.linspace(-1000, 1000, 201)
    ys = np.linspace(0, 2000, 201)
    return xs, ys


if __name__ == "__main__":
    xs, ys = grid()
    z = np.array([[ground(x, y) for x in xs] for y in ys])
    rows = []
    for lv in range(340, 470, 10):
        for line in trace(z, xs, ys, lv):
            rows += ([()] if rows else []) + [(round(x / 1000, 4), round(y / 1000, 4)) for x, y in simplify(line, 1.0)]
    write_table(__file__, ("x_km", "y_km"), rows, part="contours")
    apex = []
    for c in CASES:
        f = np.array([[plane_minus_ground(c, x, y) for x in xs] for y in ys])
        lines = trace(f, xs, ys, 0.0)
        rows = []
        for line in lines:
            rows += ([()] if rows else []) + [(round(x / 1000, 4), round(y / 1000, 4)) for x, y in simplify(line, 1.0)]
        write_table(__file__, ("x_km", "y_km"), rows, part=c)
        apex.append((c, round(outcrop_y(c, 0.0) / 1000, 4), round(outcrop_y(c, 400.0) / 1000, 4)))
    write_table(__file__, ("case", "y_axis_km", "y_side_km"), apex, part="apex")

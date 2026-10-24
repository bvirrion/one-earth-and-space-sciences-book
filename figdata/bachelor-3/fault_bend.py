"""A fault-bend fold by fault-parallel flow (Year 3, thrust belts and orogenic
wedges).

Flat--ramp--flat thrust: lower flat y = 0 for x < X_BEND, a ramp at THETA
rising RAMP_H to the upper flat y = RAMP_H. The hanging wall is cut into dip
domains by the bisectors of the two bends; in each domain every particle moves
parallel to the fault segment beneath it, at the same speed, for a total
distance (slip) S. Crossing a bisector conserves area (the normal component
of the velocity is the same on both sides), and a bed parallel to the fault
keeps its thickness.

  part fault          x y       the fault
  part bed1..bed6     x y       hanging-wall beds after the slip S
                                (bed1 at 0.25 above the lower flat ... bed6 the top, 1.6)
  part values         what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

THETA = 30.0
RAMP_H = 1.0
X_BEND = 4.0
SLIP = 2.5
BEDS = (0.25, 0.5, 0.75, 1.0, 1.3, 1.6)
X_MIN, X_MAX = 0.0, 12.0
STEP = 0.002


def geometry(theta=THETA, ramp_h=RAMP_H, x_bend=X_BEND):
    t = math.radians(theta)
    p1 = np.array([x_bend, 0.0])
    p2 = np.array([x_bend + ramp_h / math.tan(t), ramp_h])
    flat = np.array([1.0, 0.0])
    ramp = np.array([math.cos(t), math.sin(t)])
    # bisector normals: unit vector along the sum of the two segment directions
    # (the same direction serves both bends, whose angles are equal and opposite)
    n1 = (flat + ramp) / np.linalg.norm(flat + ramp)
    return p1, p2, flat, ramp, n1, n1


def fault_y(x, theta=THETA, ramp_h=RAMP_H, x_bend=X_BEND):
    t = math.radians(theta)
    return float(np.clip((x - x_bend) * math.tan(t), 0.0, ramp_h))


def domain(p, geo=None):
    p1, p2, flat, ramp, n1, n2 = geo or geometry()
    if np.dot(p - p1, n1) < 0:
        return 0
    if np.dot(p - p2, n2) < 0:
        return 1
    return 2


def velocity(p, geo=None):
    geo = geo or geometry()
    d = domain(p, geo)
    return geo[3] if d == 1 else geo[2]


def advect(p, s=SLIP, step=STEP, geo=None):
    geo = geo or geometry()
    p = np.array(p, dtype=float)
    n = int(round(s / step))
    for _ in range(n):
        # midpoint rule; at a bisector the direction changes, the speed does not
        v1 = velocity(p, geo)
        v2 = velocity(p + 0.5 * step * v1, geo)
        p = p + step * v2
    return p


def bed_after(y0, s=SLIP, n=241):
    xs = np.linspace(X_MIN - s - 1.0, X_MAX, n)
    out = []
    for x in xs:
        if y0 <= fault_y(x) + 1e-9:
            continue            # footwall at this height
        q = advect((x, y0), s)
        if X_MIN <= q[0] <= X_MAX:
            out.append((float(q[0]), float(q[1])))
    return out


def polygon_area(pts):
    a = 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        a += x1 * y2 - x2 * y1
    return 0.5 * a


if __name__ == "__main__":
    xs = np.linspace(X_MIN, X_MAX, 241)
    write_table(__file__, ("x", "y"), [(x, fault_y(x)) for x in xs], part="fault")
    for i, y0 in enumerate(BEDS, start=1):
        write_table(__file__, ("x", "y"), bed_after(y0), part=f"bed{i}")
    p1, p2 = geometry()[:2]
    vals = [("ramp_horizontal", p2[0] - p1[0]), ("ramp_length", float(np.linalg.norm(p2 - p1))),
            ("uplift_top", max(y for _, y in bed_after(BEDS[-1])) - BEDS[-1])]
    write_table(__file__, ("what", "value"), vals, part="values")

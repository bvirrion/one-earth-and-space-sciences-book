"""Maps of the whole Earth, grade 9, chapter 5: satellite positioning in two
dimensions (exercise data). Three beacons A, B, C on a flat map send signals;
a receiver R knows its distance to each one. The circle around A and the
circle around B cross at two points: R and a false point F; the circle
around C passes through R only, so three distances fix the position.

The travel-time example uses the speed of light (ledger const:c) and the
altitude of the GPS satellites, about 20,200 km (ledger gps:constellation).

  part beacons : x y label
  part circles : x y          (three circles, separated by blank rows)
  part points  : x y label    (R and F)
  part problem : item value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

BEACONS = {"A": (1.0, 7.0), "B": (12.0, 9.0), "C": (9.0, 3.0)}   # km
RECEIVER = (4.0, 3.0)
C_KM_S = 299792.458                     # const:c
GPS_ALT_KM = 20200.0                    # gps:constellation


def dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def distances():
    return {k: dist(v, RECEIVER) for k, v in BEACONS.items()}


def circle_intersections(c0, r0, c1, r1):
    d = dist(c0, c1)
    a = (r0 * r0 - r1 * r1 + d * d) / (2 * d)
    h = math.sqrt(max(r0 * r0 - a * a, 0.0))
    xm = c0[0] + a * (c1[0] - c0[0]) / d
    ym = c0[1] + a * (c1[1] - c0[1]) / d
    return [(xm + h * (c1[1] - c0[1]) / d, ym - h * (c1[0] - c0[0]) / d),
            (xm - h * (c1[1] - c0[1]) / d, ym + h * (c1[0] - c0[0]) / d)]


def locate():
    """Position from the three distances: the crossing of circles A and B
    that also lies on circle C; returns (position, false point)."""
    r = distances()
    p, q = circle_intersections(BEACONS["A"], r["A"], BEACONS["B"], r["B"])
    ep = abs(dist(p, BEACONS["C"]) - r["C"])
    eq = abs(dist(q, BEACONS["C"]) - r["C"])
    return (p, q) if ep < eq else (q, p)


def travel_time_s(km=GPS_ALT_KM):
    return km / C_KM_S


def circle(c, r, n=120):
    return [(c[0] + r * math.cos(2 * math.pi * k / n), c[1] + r * math.sin(2 * math.pi * k / n)) for k in range(n + 1)]


if __name__ == "__main__":
    write_table(__file__, ("x", "y", "label"), [(x, y, k) for k, (x, y) in BEACONS.items()], part="beacons")
    r = distances()
    rows = []
    for k, c in BEACONS.items():
        rows += [()] + [(round(x, 4), round(y, 4)) for x, y in circle(c, r[k])]
    write_table(__file__, ("x", "y"), rows[1:], part="circles")
    pos, false = locate()
    write_table(__file__, ("x", "y", "label"),
                [(round(pos[0], 3), round(pos[1], 3), "R"), (round(false[0], 3), round(false[1], 3), "F")], part="points")
    prob = {"d_%s_km" % k: v for k, v in r.items()}
    prob["false_x"], prob["false_y"] = false
    prob["false_to_C_km"] = dist(false, BEACONS["C"])
    prob["travel_time_s"] = travel_time_s()
    write_table(__file__, ("item", "value"), [(k, round(v, 4)) for k, v in prob.items()], part="problem")
    for k, v in prob.items():
        print(k, round(v, 4))
    print("position", pos)

"""Maps of the whole Earth, grade 9, chapter 5: the topographic map of part of
the Varden Hills (the series' invented region, figdata/shared/region.py), a
topographic profile along C--D, and the footpath of the weekend problem.

The map shows the window WINDOW (km) at 1 : 50 000 (1 km = 2 cm on paper).
Its contours (every 50 m, index contours at 250 and 500 m) and the river are
the shared tables written by region.py (figdata/out/shared-region-*.dat);
this script adds the contour labels, the spot heights, the line C--D and its
profile (sampled from region.topo), the points where C--D crosses each
contour (the profile method), and the footpath S -> B -> W -> T, every leg of
which only climbs or only descends (tested), so that its total climb is read
from the spot heights.

  part labels  : x_km y_km label        (contour labels)
  part spots   : x_km y_km label        (spot heights)
  part cd      : x_km y_km label        (C and D)
  part profile : s_km z_m               (ground along C--D, every 20 m)
  part cross   : s_km z_m               (C--D crossing a contour)
  part path    : x_km y_km              (the footpath)
  part points  : x_km y_km label        (S, B, W, T with their heights)
  part problem : item value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

WINDOW = (2.0, 8.0, 1.8, 6.2)          # xmin, xmax, ymin, ymax in km
SCALE = 50000                          # 1 : 50 000
CM_PER_KM = 100000.0 / SCALE           # 2 cm on paper for 1 km
INTERVAL = 50                          # contour interval (m)
C = (5.0, 2.0)                         # km
D = (5.0, 6.0)
# vertical lines (x km) along which contours are labelled, with their levels
LABEL_LINES = ((2.45, (200, 250, 300, 400)), (7.55, (200, 250, 300, 400)), (6.0, (500,)))
PATH = [("S", (2.9, 2.3)), ("B", (3.8, None)), ("W", (4.6, 4.8)), ("T", (5.38, 5.68))]


def z(xk, yk):
    return region.topo(xk * 1000.0, yk * 1000.0)


def path_points():
    pts = []
    for name, (x, y) in PATH:
        if y is None:                                  # the bridge: on the river
            y = region.river_y(x * 1000.0) / 1000.0
        pts.append((name, (x, y)))
    return pts


def leg_profile(a, b, n=400):
    return [z(a[0] + (b[0] - a[0]) * t / n, a[1] + (b[1] - a[1]) * t / n) for t in range(n + 1)]


def leg_is_monotonic(a, b, tol=0.5):
    zs = leg_profile(a, b)
    d = [q - p for p, q in zip(zs, zs[1:])]
    return all(x >= -tol for x in d) or all(x <= tol for x in d)


def profile(a=C, b=D, ds=0.02):
    L = math.hypot(b[0] - a[0], b[1] - a[1])
    n = int(round(L / ds))
    return [(L * k / n, z(a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n)) for k in range(n + 1)]


def crossings(a=C, b=D, interval=INTERVAL):
    """(s_km, level) where the line a-b crosses a contour level (linear
    interpolation between profile samples)."""
    out = []
    prof = profile(a, b, ds=0.005)
    for (s0, z0), (s1, z1) in zip(prof, prof[1:]):
        lo, hi = sorted((z0, z1))
        lv = (int(lo // interval) + 1) * interval
        while lv <= hi:
            if z1 != z0:
                out.append((s0 + (lv - z0) / (z1 - z0) * (s1 - s0), lv))
            lv += interval
    return out


def contour_labels():
    out = []
    for xl, levels in LABEL_LINES:
        prof = [(y, z(xl, y)) for y in [WINDOW[2] + 0.005 * k for k in range(int((WINDOW[3] - WINDOW[2]) / 0.005) + 1)]]
        done = set()
        for (y0, z0), (y1, z1) in zip(prof, prof[1:]):
            for lv in levels:
                if lv in done:
                    continue
                if (z0 - lv) * (z1 - lv) <= 0 and z0 != z1:
                    out.append((xl, y0 + (lv - z0) / (z1 - z0) * (y1 - y0), lv))
                    done.add(lv)
    return out


def problem():
    pts = path_points()
    p = {}
    legs = []
    for (n0, a), (n1, b) in zip(pts, pts[1:]):
        km = math.hypot(b[0] - a[0], b[1] - a[1])
        legs.append((n0 + n1, km, z(*a), z(*b)))
    climb = 0.0
    descent = 0.0
    for _name, km, za, zb in legs:
        if zb > za:
            climb += round(zb) - round(za)
        else:
            descent += round(za) - round(zb)
    for name, km, za, zb in legs:
        p["leg_%s_km" % name] = km
        p["leg_%s_cm" % name] = km * CM_PER_KM
    for name, (x, y) in pts:
        p["z_%s" % name] = z(x, y)
    p["length_km"] = sum(km for _n, km, _a, _b in legs)
    p["climb_m"] = climb
    p["descent_m"] = descent
    return p


if __name__ == "__main__":
    write_table(__file__, ("x_km", "y_km", "label"),
                [(round(x, 3), round(y, 3), "%d" % lv) for x, y, lv in contour_labels()], part="labels")
    pts = path_points()
    write_table(__file__, ("x_km", "y_km", "label"),
                [(round(x, 3), round(y, 3), "%s\\,(%d)" % (n, round(z(x, y)))) for n, (x, y) in pts], part="points")
    write_table(__file__, ("x_km", "y_km", "label"),
                [(round(x, 3), round(y, 3), "%d" % round(z(x, y))) for n, (x, y) in pts if n == "T"], part="spots")
    write_table(__file__, ("x_km", "y_km", "label"), [(C[0], C[1], "C"), (D[0], D[1], "D")], part="cd")
    write_table(__file__, ("s_km", "z_m"), [(round(s, 3), round(zz, 1)) for s, zz in profile()], part="profile")
    write_table(__file__, ("s_km", "z_m"), [(round(s, 3), lv) for s, lv in crossings()], part="cross")
    write_table(__file__, ("x_km", "y_km"), [(round(x, 3), round(y, 3)) for _n, (x, y) in pts], part="path")
    p = problem()
    write_table(__file__, ("item", "value"), [(k, round(v, 3)) for k, v in p.items()], part="problem")
    for k, v in p.items():
        print(k, round(v, 3))
    print("crossings", [(round(s, 2), lv) for s, lv in crossings()])
    print("labels", [(round(x, 2), round(y, 2), lv) for x, y, lv in contour_labels()])

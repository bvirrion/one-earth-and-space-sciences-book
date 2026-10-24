"""Finding an epicentre with three stations (grade 7, earthquakes).

The faster waves arrive first, the slower ones later; the delay between the
two grows with distance. With the speeds of the shared reference model's
crust (data/derived/prem.csv, ledger data:prem) the distance is

    d = delay * vp * vs / (vp - vs)

about 7 km per second of delay in the upper crust and 9 km in the lower
crust; the exercises use the round value KM_PER_S = 8 (an exercise datum,
said so in the text).

Two invented situations (exercise data, not real places):

* the METHOD example: three stations around an epicentre at (0, 0), whose
  circles are drawn in the text, with one station's seismogram;
* the PROBLEM map: a sea between a western coast, a northern coast and a
  small island with a harbour town; three stations on land, the epicentre
  at sea; only the stations, the coasts and the town are drawn (the reader
  finds the epicentre).

  part rule      : layer vp vs km_per_s
  part m-stations: name x y dist delay
  part m-circles : x y                      (three circles, blank-line separated)
  part m-trace   : t v                      (seismogram of station M1, seeded noise)
  part p-stations: name x y dist delay
  parts p-west, p-north, p-island : x y      (the three land polygons, drawn in that order)
  part p-town    : name x y
  part p-grid    : (none: the grid is drawn by pgfplots)
  main table     : the problem's numbers
"""
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
KM_PER_S = 8.0
TSUNAMI_KMH = 800.0          # nws:tsunami-speed
WARNING_MIN = 5.0            # time to locate the earthquake and send the warning (exercise datum)

# method example: epicentre at the origin
M_EPI = (0.0, 0.0)
M_STATIONS = (("M1", -48.0, 64.0), ("M2", 72.0, 54.0), ("M3", 30.0, -72.0))

# problem: epicentre at sea, three stations on land, a harbour town on an island
P_EPI = (120.0, 90.0)
P_STATIONS = (("A", 24.0, -38.0), ("B", 160.0, 186.0), ("C", 0.0, 90.0))
P_TOWN = ("Port Hale", 264.0, -102.0)


def crust_rule():
    """[(layer, vp, vs, km per second of delay)] from PREM's two crustal layers."""
    out = []
    with open(os.path.join(ROOT, "data", "derived", "prem.csv"), encoding="utf8") as f:
        seen = set()
        for r in csv.DictReader(f):
            if r["region"] != "crust":
                continue
            vp, vs = float(r["vp_km_s"]), float(r["vs_km_s"])
            if (vp, vs) in seen:
                continue
            seen.add((vp, vs))
            out.append(("upper" if not out else "lower", vp, vs, vp * vs / (vp - vs)))
    return out


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def delay_s(d_km, k=KM_PER_S):
    return d_km / k


def stations(epi, sts):
    return [(n, x, y, dist(epi, (x, y)), delay_s(dist(epi, (x, y)))) for n, x, y in sts]


def circle(cx, cy, r, n=180):
    return [(cx + r * math.cos(2 * math.pi * i / n), cy + r * math.sin(2 * math.pi * i / n)) for i in range(n + 1)]


def locate(sts_with_dist):
    """Least-squares epicentre from three (x, y, d): subtract the first circle
    equation from the others (linear in x, y)."""
    (x1, y1, d1), *rest = sts_with_dist
    A, b = [], []
    for x, y, d in rest:
        A.append([2 * (x - x1), 2 * (y - y1)])
        b.append(d1 ** 2 - d ** 2 + x ** 2 - x1 ** 2 + y ** 2 - y1 ** 2)
    sol, *_ = np.linalg.lstsq(np.array(A), np.array(b), rcond=None)
    return float(sol[0]), float(sol[1])


def trace(delay, t_p=10.0, t_end=60.0, dt=0.05, seed=7):
    """A drawn seismogram: a quiet line, small fast wiggles from t_p, larger
    slower ones from t_p + delay, dying out. Shape only: the vertical scale
    is arbitrary."""
    rng = np.random.default_rng(seed)
    t = np.arange(0.0, t_end + dt / 2, dt)
    v = 0.03 * rng.standard_normal(t.size)
    p = t >= t_p
    v[p] += 0.35 * np.exp(-(t[p] - t_p) / 6.0) * np.sin(2 * math.pi * 2.2 * (t[p] - t_p))
    s_t = t_p + delay
    s = t >= s_t
    v[s] += 1.0 * np.exp(-(t[s] - s_t) / 9.0) * np.sin(2 * math.pi * 1.1 * (t[s] - s_t))
    return t, v


def coasts():
    """Three invented coast polygons (closed rings): the west land, the north
    land and the island of the harbour town. Gentle wiggles, deterministic."""
    def wig(i, a=5.0):
        return a * math.sin(0.7 * i) + 0.5 * a * math.sin(1.9 * i)
    # west land: coast running south to north near x = 60, land to the west
    # (it runs on to y = 160, under the north land, so the two lands join)
    wc = [(60.0 + wig(i), -200.0 + 15.0 * i) for i in range(25)]          # y from -200 to 160
    west = wc + [(-60.0, wc[-1][1]), (-60.0, -200.0), wc[0]]
    # north land: coast running west to east near y = 140, land to the north
    nc = [(-60.0 + 15.0 * i, 140.0 + wig(i + 3)) for i in range(30)]      # x from -60 to 375
    north = nc + [(380.0, 280.0), (-60.0, 280.0), nc[0]]
    tx, ty = P_TOWN[1], P_TOWN[2]
    cx, cy, r = tx + 40.0, ty - 6.0, math.hypot(40.0, 6.0)
    island = [(cx + r * math.cos(a) * (1 + 0.06 * math.sin(3 * a)), cy + 0.8 * r * math.sin(a))
              for a in np.linspace(0, 2 * math.pi, 73)]
    return west, north, island


def on_land(pt, ring):
    """Even-odd point-in-polygon test."""
    x, y = pt
    inside = False
    for (x1, y1), (x2, y2) in zip(ring, ring[1:]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            inside = not inside
    return inside


def tsunami_minutes():
    return 60.0 * dist(P_EPI, (P_TOWN[1], P_TOWN[2])) / TSUNAMI_KMH


def minutes_left():
    """The problem's named number."""
    return tsunami_minutes() - WARNING_MIN


if __name__ == "__main__":
    write_table(__file__, ("layer", "vp", "vs", "km_per_s"), [(l, vp, vs, round(k, 2)) for l, vp, vs, k in crust_rule()],
                part="rule")
    ms = stations(M_EPI, M_STATIONS)
    write_table(__file__, ("name", "x", "y", "dist", "delay"), [(n, x, y, round(d, 1), round(t, 2)) for n, x, y, d, t in ms],
                part="m-stations")
    rows = []
    for n, x, y, d, t in ms:
        rows += ([()] if rows else []) + [(round(a, 2), round(b, 2)) for a, b in circle(x, y, d)]
    write_table(__file__, ("x", "y"), rows, part="m-circles")
    t, v = trace(ms[0][4])
    write_table(__file__, ("t", "v"), [(round(a, 2), round(b, 4)) for a, b in zip(t, v)], part="m-trace")
    ps = stations(P_EPI, P_STATIONS)
    write_table(__file__, ("name", "x", "y", "dist", "delay"), [(n, x, y, round(d, 1), round(t, 2)) for n, x, y, d, t in ps],
                part="p-stations")
    # one part per land, drawn in this order: the north land covers the top
    # edge of the west land, which runs on under it
    for name, ring in zip(("p-west", "p-north", "p-island"), coasts()):
        write_table(__file__, ("x", "y"), [(round(a, 2), round(b, 2)) for a, b in ring], part=name)
    write_table(__file__, ("name", "x", "y"), [("{%s}" % P_TOWN[0], P_TOWN[1], P_TOWN[2])], part="p-town")
    write_table(__file__, ("item", "value"),
                [("epi_x", P_EPI[0]), ("epi_y", P_EPI[1]), ("town_km", dist(P_EPI, (P_TOWN[1], P_TOWN[2]))),
                 ("tsunami_min", tsunami_minutes()), ("minutes_left", minutes_left())])

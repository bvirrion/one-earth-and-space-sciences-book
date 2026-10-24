"""The main surface-current gyres on a world map, and a drifting buoy's
journey round the North Atlantic gyre, for grade 8, chapter 4 (the oceans).

Gyres (ledger nos:gyres): five large loops, clockwise north of the equator,
anticlockwise south of it. Each is drawn as a schematic ellipse in
longitude--latitude, cut into four sides with a small gap so that every side
carries its own arrowhead. The side that flows towards the pole along the
western edge of the ocean (the western boundary current, like the Gulf
Stream) and the side that flows west near the equator carry tropical water:
"warm"; the side that flows towards the equator along the eastern edge (like
the Canary Current) carries water from higher latitudes: "cold". The fourth
side (eastward, on the pole side) is counted warm in the northern hemisphere
(the Gulf Stream's continuation) and cold in the southern one. This is the
simplified picture of the chapter, not a map of measured currents.

The North Pacific and South Pacific loops cross the 180 degree meridian:
their points are wrapped to -180..180 and the line is cut where it jumps.

The buoy: four legs round the North Atlantic gyre through fixed waypoints;
distances by the great-circle formula (R from earth:Rmean); speeds in km per
day: the Gulf Stream leg at 100 km a day (inside the 40--120 km a day of
ledger nos:gulf-stream), the others exercise data.

  parts gyres-warm, gyres-cold   : lon lat   (segments separated by blank lines)
  parts heads-warm, heads-cold   : lon lat u v  (arrowheads at segment ends)
  part  buoy                     : lon lat   (the whole route)
  part  buoy-legs                : lon lat name   (leg labels at mid-leg)
  main table                     : leg, km, km_per_day, days; totals
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

R_EARTH = 6371.0
GAP = 7.0                         # degrees of the parameter left between sides

# name, centre lon, centre lat, half-width (deg lon), half-height (deg lat), hemisphere
GYRES = [
    ("North Atlantic", -42.0, 30.0, 28.0, 12.0, "N"),
    ("South Atlantic", -15.0, -25.0, 21.0, 10.0, "S"),
    ("North Pacific", 185.0, 30.0, 42.0, 13.0, "N"),
    ("South Pacific", 215.0, -28.0, 36.0, 11.0, "S"),
    ("Indian Ocean", 80.0, -25.0, 24.0, 10.0, "S"),
]

# sides: (name, t_start, t_end) for a clockwise loop (northern hemisphere)
SIDES_N = [("west", 225.0, 135.0), ("pole", 135.0, 45.0), ("east", 45.0, -45.0), ("equator", 315.0, 225.0)]
SIDES_S = [("west", 135.0, 225.0), ("pole", 225.0, 315.0), ("east", 315.0, 405.0), ("equator", 45.0, 135.0)]
WARM_N = {"west": True, "pole": True, "east": False, "equator": True}
WARM_S = {"west": True, "pole": False, "east": False, "equator": True}

BUOY_LEGS = [
    ("A", "Gulf Stream", 100.0, [(-79.5, 26.0), (-76.0, 33.0), (-70.0, 38.0), (-58.0, 40.5), (-45.0, 42.0)]),
    ("B", "North Atlantic Current", 20.0, [(-45.0, 42.0), (-32.0, 44.5), (-20.0, 43.0)]),
    ("C", "Canary Current", 20.0, [(-20.0, 43.0), (-15.0, 35.0), (-19.0, 26.0), (-25.0, 18.0)]),
    ("D", "North Equatorial Current", 20.0, [(-25.0, 18.0), (-45.0, 15.0), (-62.0, 17.0), (-73.0, 21.5),
                                             (-79.5, 26.0)]),
]


def wrap(lon):
    return (lon + 180.0) % 360.0 - 180.0


def side_points(g, t0, t1, n=30):
    _name, cx, cy, a, b, _h = g
    d = GAP if t1 > t0 else -GAP
    ts = [t0 + d / 2 + (t1 - t0 - d) * k / n for k in range(n + 1)]
    return [(cx + a * math.cos(math.radians(t)), cy + b * math.sin(math.radians(t))) for t in ts]


def split_wrapped(points):
    """Wrap longitudes into -180..180 and cut the line where it jumps."""
    out, cur, prev = [], [], None
    for lon, lat in points:
        w = wrap(lon)
        if prev is not None and abs(w - prev) > 180:
            out.append(cur)
            cur = []
        cur.append((w, lat))
        prev = w
    out.append(cur)
    return [c for c in out if len(c) > 1]


def gyre_sides():
    """[(gyre, side, warm, points)] with unwrapped points, in flow order."""
    out = []
    for g in GYRES:
        sides, warm = (SIDES_N, WARM_N) if g[5] == "N" else (SIDES_S, WARM_S)
        for name, t0, t1 in sides:
            out.append((g[0], name, warm[name], side_points(g, t0, t1)))
    return out


def turning(points):
    """Signed area (shoelace) of a closed loop: > 0 anticlockwise."""
    s = 0.0
    for (x0, y0), (x1, y1) in zip(points, points[1:] + points[:1]):
        s += x0 * y1 - x1 * y0
    return s / 2.0


def great_circle(a, b, r=R_EARTH):
    lo1, la1, lo2, la2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def leg_km(points):
    return sum(great_circle(p, q) for p, q in zip(points, points[1:]))


def buoy_table():
    rows = []
    for key, name, speed, pts in BUOY_LEGS:
        km = leg_km(pts)
        rows.append((key, name, km, speed, km / speed))
    return rows


def rounded_legs():
    """Leg lengths rounded to the nearest 100 km, as printed in the problem."""
    return [(k, n, round(km, -2), s, round(km, -2) / s) for k, n, km, s, _d in buoy_table()]


if __name__ == "__main__":
    warm_rows, cold_rows, hw, hc = [], [], [], []
    for _g, _s, warm, pts in gyre_sides():
        pieces = split_wrapped(pts)
        rows = warm_rows if warm else cold_rows
        for piece in pieces:
            rows += [(round(x, 2), round(y, 2)) for x, y in piece] + [("", "")]
        (x0, y0), (x1, y1) = pieces[-1][-2], pieces[-1][-1]
        n = math.hypot(x1 - x0, y1 - y0)
        (hw if warm else hc).append((round(x1, 2), round(y1, 2), round((x1 - x0) / n * 0.01, 5),
                                     round((y1 - y0) / n * 0.01, 5)))
    write_table(__file__, ("lon", "lat"), warm_rows[:-1], part="gyres-warm")
    write_table(__file__, ("lon", "lat"), cold_rows[:-1], part="gyres-cold")
    write_table(__file__, ("lon", "lat", "u", "v"), hw, part="heads-warm")
    write_table(__file__, ("lon", "lat", "u", "v"), hc, part="heads-cold")
    route = []
    for _k, _n, _s, pts in BUOY_LEGS:
        route += pts if not route else pts[1:]
    write_table(__file__, ("lon", "lat"), route, part="buoy")
    labels = []
    for key, _n, _s, pts in BUOY_LEGS:
        m = pts[len(pts) // 2] if len(pts) % 2 else ((pts[len(pts) // 2 - 1][0] + pts[len(pts) // 2][0]) / 2,
                                                     (pts[len(pts) // 2 - 1][1] + pts[len(pts) // 2][1]) / 2)
        labels.append((round(m[0], 2), round(m[1], 2), key))
    write_table(__file__, ("lon", "lat", "name"), labels, part="buoy-legs")
    rows = [("leg_%s_km" % k, round(km, 1)) for k, _n, km, _s, _d in buoy_table()]
    rows += [("leg_%s_km_rounded" % k, km) for k, _n, km, _s, _d in rounded_legs()]
    rows += [("leg_%s_days_rounded" % k, round(d, 1)) for k, _n, _km, _s, d in rounded_legs()]
    tot_days = sum(d for *_r, d in rounded_legs())
    rows += [("total_km_rounded", sum(km for _k, _n, km, _s, _d in rounded_legs())),
             ("total_days", round(tot_days, 1)), ("total_months_30d", round(tot_days / 30.0, 1))]
    write_table(__file__, ("item", "value"), rows)
    for r in rounded_legs():
        print(r)
    print("total days %.1f months %.1f" % (tot_days, tot_days / 30))

"""A computed weather map of the northern hemisphere for grade 8, chapter 3
(air masses, fronts and weather maps), and the cold front's march towards a
town for the chapter's problem.

The map is an invented situation (no real date, no real coastline), drawn on
a square-kilometre grid 2400 km wide and 1600 km high. Its sea-level pressure
is an analytic field:

  * a background of 1012 hPa (near the standard 1013 hPa, ledger bom:isobars);
  * a depression L, Gaussian, 30 hPa deep, and an anticyclone H, 22 hPa high
    (a moderate low and a typical high, ledger bom:isobars);
  * a narrow trough of 3 hPa along each front, which gives the isobars the
    kink they show on real charts where they cross a front.

Isobars every 4 hPa are traced by marching squares (figdata/shared/region.py
`trace`). The fronts are oriented so that their symbols (drawn on the LEFT of
the path by the style file) point the way the front moves: the cold front runs
from the low towards the south-west and moves east; the warm front runs from
the low towards the south-east and moves north-east. Winds turn anticlockwise
around the low and clockwise around the high (northern hemisphere, ledger
bom:highs-lows mirrored): each arrow runs along the isobars with the low
pressure on its left, turned 20 degrees towards the low, and its length grows
with the pressure gradient (close isobars, strong wind).

The problem: the cold front moves east at SPEED_KMH (exercise data). Its
positions at 06:00 and 09:00 and the town T are written for a zoomed map.

  part isobars : x y            (km; lines separated by blank lines)
  part labels  : x y level      (one label per isobar)
  part centres : x y name p     (L and H with their central pressure)
  part cold    : x y            (cold front, symbols on the left = east)
  part warm    : x y            (warm front, symbols on the left = north-east)
  part winds   : x y u v        (arrow start and vector, km on the map)
  part town    : x y name
  part seq-06, seq-09 : x y     (the cold front at 06:00 and 09:00, zoom)
  main table   : item value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
from region import trace  # noqa: E402

W, H = 2400.0, 1600.0               # km
P0 = 1012.0                         # hPa, background
LOW = (800.0, 1000.0, -30.0, 380.0)     # x, y, amplitude (hPa), width (km)
HIGH = (1950.0, 520.0, 22.0, 480.0)
TROUGH, TROUGH_W = 3.0, 70.0        # hPa, km
STEP = 4.0                          # hPa between isobars
TURN = 20.0                         # degrees, wind turned towards the low
SPEED_KMH = 40.0                    # exercise data: the cold front's speed
TOWN_LAG_KM = 180.0                 # the town lies this far east of the 09:00 front
T_MAP = 9.0                         # hour of the main map


def cold_front(shift=0.0, n=40):
    """Cold front at the map hour, shifted east by `shift` km; from the low
    towards the south-west, so that its LEFT side is the east."""
    out = []
    for k in range(n + 1):
        s = k / n
        out.append((LOW[0] - 220.0 * s + 120.0 * s * (1 - s) + shift, LOW[1] - 850.0 * s))
    return out


def warm_front(n=40):
    """Warm front, from the low towards the south-east: LEFT side = north-east."""
    out = []
    for k in range(n + 1):
        s = k / n
        out.append((LOW[0] + 560.0 * s, LOW[1] - 300.0 * s - 60.0 * s * (1 - s)))
    return out


def dist_to_line(x, y, line):
    pts = np.asarray(line)
    a, b = pts[:-1], pts[1:]
    d = b - a
    t = np.clip(((x - a[:, 0]) * d[:, 0] + (y - a[:, 1]) * d[:, 1]) / (d ** 2).sum(1), 0, 1)
    px, py = a[:, 0] + t * d[:, 0], a[:, 1] + t * d[:, 1]
    return float(np.min(np.hypot(x - px, y - py)))


def gauss(x, y, c):
    cx, cy, amp, w = c
    return amp * np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * w * w))


def pressure(x, y):
    """Sea-level pressure (hPa) at (x, y) km; x, y scalars or arrays."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    p = P0 + gauss(x, y, LOW) + gauss(x, y, HIGH)
    flat = np.broadcast(x, y)
    trough = np.empty(flat.shape)
    xs, ys = np.broadcast_arrays(x, y)
    cold, warm = cold_front(), warm_front()
    for idx in np.ndindex(flat.shape):
        d = min(dist_to_line(xs[idx], ys[idx], cold), dist_to_line(xs[idx], ys[idx], warm))
        trough[idx] = -TROUGH * math.exp(-d * d / (2 * TROUGH_W ** 2))
    return p + trough


def grid(step=20.0):
    xs = np.arange(0.0, W + step / 2, step)
    ys = np.arange(0.0, H + step / 2, step)
    X, Y = np.meshgrid(xs, ys)
    return xs, ys, pressure(X, Y)


def levels(field):
    lo = math.ceil(field.min() / STEP) * STEP
    hi = math.floor(field.max() / STEP) * STEP
    return [lo + STEP * k for k in range(int(round((hi - lo) / STEP)) + 1)]


def isobars(field=None, xs=None, ys=None):
    if field is None:
        xs, ys, field = grid()
    out = []
    for lev in levels(field):
        for line in trace(field, xs, ys, lev):
            if len(line) > 3:
                out.append((lev, line))
    return out


def centre_values():
    """Lowest and highest pressure near each centre (hPa, rounded)."""
    lo = pressure(LOW[0], LOW[1])
    hi = pressure(HIGH[0], HIGH[1])
    return float(lo), float(hi)


def wind(x, y, h=10.0):
    """Wind arrow vector (km on the map) at (x, y): along the isobars with the
    low pressure on the left, turned TURN degrees towards the low; length
    proportional to the pressure gradient, capped."""
    px = (float(pressure(x + h, y)) - float(pressure(x - h, y))) / (2 * h)
    py = (float(pressure(x, y + h)) - float(pressure(x, y - h))) / (2 * h)
    u, v = -py, px                       # k x grad p: low pressure on the left
    a = math.radians(TURN)               # anticlockwise turn = towards the low
    u, v = u * math.cos(a) - v * math.sin(a), u * math.sin(a) + v * math.cos(a)
    g = math.hypot(u, v)
    if g == 0:
        return 0.0, 0.0
    length = min(150.0, 60.0 + 900.0 * g)
    return u / g * length, v / g * length


def wind_arrows(step=200.0):
    out = []
    for x in np.arange(150.0, W - 100.0, step):
        for y in np.arange(120.0, H - 100.0, step):
            if math.hypot(x - LOW[0], y - LOW[1]) < 150 or math.hypot(x - HIGH[0], y - HIGH[1]) < 150:
                continue
            u, v = wind(x, y)
            out.append((float(x), float(y), u, v))
    return out


def front_x_at(y, shift=0.0):
    """x of the cold front (shifted) at latitude y (km), by interpolation."""
    line = cold_front(shift, n=400)
    for (x0, y0), (x1, y1) in zip(line, line[1:]):
        if (y0 - y) * (y1 - y) <= 0 and y0 != y1:
            return x0 + (x1 - x0) * (y - y0) / (y1 - y0)
    raise ValueError("front does not reach y")


TOWN_Y = 380.0


def town():
    return front_x_at(TOWN_Y) + TOWN_LAG_KM, TOWN_Y


def arrival_hour():
    """Hour (decimal) at which the cold front reaches the town."""
    return T_MAP + TOWN_LAG_KM / SPEED_KMH


def hhmm(h):
    m = int(round(h * 60))
    return "%02d:%02d" % (m // 60, m % 60)


def label_points(lines):
    """One label per level: on the ray from L towards the north-west for the
    lows, from H towards the south-east for the highs."""
    out = []
    done = set()
    for rays in (0, 1, 2, 3):
        for lev, line in lines:
            if lev in done or _length(line) < MIN_LABEL_LINE_KM:
                continue
            cx, cy, angs = (LOW[0], LOW[1], (125.0, 160.0, 90.0, 200.0)) if lev < P0 else \
                (HIGH[0], HIGH[1], (-40.0, 0.0, 90.0, 45.0))
            best = _ray_hit(line, cx, cy, angs[rays])
            if best and 60 < best[1] < W - 60 and 60 < best[2] < H - 60:
                out.append((best[1], best[2], "%d" % lev))
                done.add(lev)
    return out


MIN_LABEL_LINE_KM = 400.0           # the tiny ring round the centre is not labelled


def _length(line):
    return sum(math.hypot(x1 - x0, y1 - y0) for (x0, y0), (x1, y1) in zip(line, line[1:]))


def _ray_hit(line, cx, cy, ang):
    """Nearest crossing (r, x, y) of a polyline with the ray from (cx, cy) at
    angle ang (degrees), or None."""
    dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    best = None
    for (x0, y0), (x1, y1) in zip(line, line[1:]):
        ex, ey = x1 - x0, y1 - y0
        den = ex * dy - ey * dx
        if abs(den) < 1e-12:
            continue
        t = ((cx - x0) * dy - (cy - y0) * dx) / den
        r = ((cx - x0) * ey - (cy - y0) * ex) / den
        if 0 <= t <= 1 and r > 0 and (best is None or r < best[0]):
            best = (r, x0 + t * ex, y0 + t * ey)
    return best


if __name__ == "__main__":
    xs, ys, field = grid()
    lines = isobars(field, xs, ys)
    rows = []
    for _, line in lines:
        rows += [(round(x, 1), round(y, 1)) for x, y in line] + [("", "")]
    write_table(__file__, ("x", "y"), rows[:-1], part="isobars")
    write_table(__file__, ("x", "y", "level"), [(round(x, 1), round(y, 1), s) for x, y, s in label_points(lines)],
                part="labels")
    lo, hi = centre_values()
    write_table(__file__, ("x", "y", "name", "p"),
                [(LOW[0], LOW[1], "L", "%d" % round(lo)), (HIGH[0], HIGH[1], "H", "%d" % round(hi))], part="centres")
    write_table(__file__, ("x", "y"), [(round(x, 1), round(y, 1)) for x, y in cold_front()], part="cold")
    write_table(__file__, ("x", "y"), [(round(x, 1), round(y, 1)) for x, y in warm_front()], part="warm")
    write_table(__file__, ("x", "y", "u", "v"), [tuple(round(c, 1) for c in r) for r in wind_arrows()], part="winds")
    tx, ty = town()
    write_table(__file__, ("x", "y", "name"), [(round(tx, 1), ty, "T")], part="town")
    back = -SPEED_KMH * 3.0
    write_table(__file__, ("x", "y"), [(round(x, 1), round(y, 1)) for x, y in cold_front(back)], part="seq-06")
    write_table(__file__, ("x", "y"), [(round(x, 1), round(y, 1)) for x, y in cold_front()], part="seq-09")
    write_table(__file__, ("item", "value"), [
        ("p_low_hPa", round(lo, 1)), ("p_high_hPa", round(hi, 1)),
        ("levels", "%d-%d" % (levels(field)[0], levels(field)[-1])),
        ("front_x_town_lat_09", round(front_x_at(TOWN_Y), 1)),
        ("front_x_town_lat_06", round(front_x_at(TOWN_Y, back), 1)),
        ("moved_06_09_km", round(-back, 1)), ("speed_kmh", SPEED_KMH),
        ("town_x", round(tx, 1)), ("town_lag_km", TOWN_LAG_KM),
        ("hours", round(TOWN_LAG_KM / SPEED_KMH, 2)), ("arrival", hhmm(arrival_hour())),
    ])
    print("low %.1f high %.1f levels %s arrival %s town x %.1f" % (lo, hi, levels(field), hhmm(arrival_hour()), tx))

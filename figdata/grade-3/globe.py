"""The Earth as a globe, seen from two sides (grade 3, continents-and-oceans).

Orthographic projection (what a globe looks like from far away) of the
Natural Earth 1:110m land (data/derived/ne-land-110m.csv; ledger data:ne-land),
for two view centres: one over the Atlantic, one over the Pacific. Each land
ring is first oriented anticlockwise as seen from outside the Earth, then
clipped to the visible half of the sphere (Sutherland-Hodgman against the plane
of the limb); where a ring leaves the visible side and comes back, the gap is
closed along the limb, anticlockwise, so the land stays on the left.

Also writes the equator and the visible poles. Coordinates are on a unit
disk (radius 1), north up, east to the right.

  part <view>-land    : x y rings (a blank line between rings)
  part <view>-equator : x y visible part of the equator
  part <view>-poles   : name x y (visible poles only)
  part <view>-labels  : name x y (names far enough from the edge; ~ for spaces)
  part fractions      : view, share of the disk covered by land
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VIEWS = {"atlantic": (-25.0, 15.0), "pacific": (-165.0, 0.0)}   # (lon, lat) of the view centre


# where each name is written (lon, lat): continents in the middle of their land,
# oceans in open water (checked in the test)
LABELS = {
    "North America": (-100.0, 45.0), "South America": (-60.0, -12.0),
    "Europe": (15.0, 52.0), "Africa": (20.0, 5.0), "Asia": (95.0, 50.0),
    "Australia": (140.0, -23.0), "Antarctica": (60.0, -80.0),
    "Pacific Ocean": (-150.0, 5.0), "Atlantic Ocean": (-38.0, 22.0),
    "Indian Ocean": (78.0, -22.0), "Southern Ocean": (-60.0, -64.0),
}   # the Arctic Ocean is named on the world map: on a globe its name would cover the pole
MIN_DEPTH = 0.35      # a name too close to the edge of the disk is not written


def labels(view):
    out = []
    for name, (lo, la) in LABELS.items():
        x, y, d = project(xyz(lo, la), view)
        if d >= MIN_DEPTH:
            out.append((name, x, y))
    return out


def rings():
    out = {}
    with open(os.path.join(ROOT, "data", "derived", "ne-land-110m.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            out.setdefault(r["ring"], []).append((float(r["lon"]), float(r["lat"])))
    return list(out.values())


def xyz(lon, lat):
    lo, la = math.radians(lon), math.radians(lat)
    return (math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la))


def basis(lon0, lat0):
    """(east, north, out) unit vectors at the view centre."""
    lo, la = math.radians(lon0), math.radians(lat0)
    e = (-math.sin(lo), math.cos(lo), 0.0)
    n = (-math.sin(la) * math.cos(lo), -math.sin(la) * math.sin(lo), math.cos(la))
    o = xyz(lon0, lat0)
    return e, n, o


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def project(p, view):
    e, n, o = basis(*view)
    return dot(p, e), dot(p, n), dot(p, o)       # x, y on the disk, depth (>0 visible)


def densify(ring, step=2.0):
    out = []
    for (a, b) in zip(ring, ring[1:]):
        d = max(abs(b[0] - a[0]), abs(b[1] - a[1]))
        k = max(1, int(d / step))
        out += [(a[0] + (b[0] - a[0]) * t / k, a[1] + (b[1] - a[1]) * t / k) for t in range(k)]
    out.append(ring[-1])
    return out


def oriented(ring):
    """Ring as 3D points, anticlockwise seen from outside.

    Natural Earth rings are cut at the 180th meridian and Antarctica's ring runs
    down to the South Pole, so the sign of the shoelace area in (lon, lat) is the
    sign seen from outside the Earth (east to the right, north up)."""
    area = sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(ring, ring[1:] + ring[:1]))
    ring = ring if area > 0 else ring[::-1]
    return [xyz(lo, la) for lo, la in densify(ring)]


def _limb_arc(p, q, arc_step):
    a0 = math.atan2(p[1], p[0])
    a1 = math.atan2(q[1], q[0])
    while a1 <= a0:
        a1 += 2 * math.pi
    m = int((a1 - a0) / math.radians(arc_step))
    return [(math.cos(a0 + (a1 - a0) * s / (m + 1)), math.sin(a0 + (a1 - a0) * s / (m + 1)))
            for s in range(1, m + 1)]


def clip(pts3, view, arc_step=3.0):
    """Visible parts of an anticlockwise ring, closed along the limb.

    Returns a list of closed polygons on the unit disk. The ring is cut into
    visible chains (entry ... exit); each exit is joined, anticlockwise along
    the limb, to the next chain entry met in that direction (Weiler-Atherton
    for a convex clip region), so the land always stays on the left."""
    e, n, o = basis(*view)
    if pts3[0] == pts3[-1]:
        pts3 = pts3[:-1]
    k = len(pts3)
    vis = [dot(p, o) >= 0 for p in pts3]
    if all(vis):
        poly = [(dot(p, e), dot(p, n)) for p in pts3]
        return [poly + poly[:1]]
    if not any(vis):
        return []
    start = next(i for i in range(k) if not vis[i])       # begin outside
    chains, cur = [], None
    for s in range(k):
        i = (start + s) % k
        a, b = pts3[i], pts3[(i + 1) % k]
        da, db = dot(a, o), dot(b, o)
        if da >= 0:
            cur.append((dot(a, e), dot(a, n)))
        if (da >= 0) != (db >= 0):
            t = da / (da - db)
            c = [a[j] + t * (b[j] - a[j]) for j in range(3)]
            x, y = dot(c, e), dot(c, n)
            r = math.hypot(x, y) or 1.0
            if da >= 0:
                cur.append((x / r, y / r)); chains.append(cur); cur = None
            else:
                cur = [(x / r, y / r)]
    ang = [math.atan2(c[0][1], c[0][0]) for c in chains]
    used, polys = [False] * len(chains), []
    for s0 in range(len(chains)):
        if used[s0]:
            continue
        poly, j = [], s0
        while not used[j]:
            used[j] = True
            poly += chains[j]
            x = chains[j][-1]
            a0 = math.atan2(x[1], x[0])
            nxt = min(range(len(chains)), key=lambda m: (ang[m] - a0) % (2 * math.pi))
            poly += _limb_arc(x, chains[nxt][0], arc_step)
            j = nxt
        polys.append(poly + poly[:1])
    return polys


def land(view, rs=None):
    """Visible land polygons; slivers thinner than a pencil line at the limb are dropped."""
    return [p for r in (rs or rings()) for p in clip(oriented(r), view)
            if len(p) > 3 and polygon_area(p) > 1e-5]


def polygon_area(poly):
    return 0.5 * sum(x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(poly, poly[1:]))


def land_fraction(view, rs=None):
    """Projected (disk) area of land over the disk area: what the eye sees."""
    return sum(polygon_area(p) for p in land(view, rs)) / math.pi


def parallel(lat, view, step=2.0):
    seg, segs = [], []
    for k in range(int(360 / step) + 1):
        x, y, d = project(xyz(-180 + k * step, lat), view)
        if d >= 0:
            seg.append((x, y))
        elif seg:
            segs.append(seg); seg = []
    if seg:
        segs.append(seg)
    return segs


if __name__ == "__main__":
    rs = rings()
    fr = []
    for name, v in VIEWS.items():
        rows = []
        for p in land(v, rs):
            rows += ([()] if rows else []) + [(round(x, 4), round(y, 4)) for x, y in p]
        write_table(__file__, ("x", "y"), rows, part=name + "-land")
        rows = []
        for s in parallel(0.0, v):
            rows += ([()] if rows else []) + [(round(x, 4), round(y, 4)) for x, y in s]
        write_table(__file__, ("x", "y"), rows, part=name + "-equator")
        poles = []
        for nm, la in (("N", 90.0), ("S", -90.0)):
            x, y, d = project(xyz(0.0, la), v)
            if d > 0.05:
                poles.append((nm, round(x, 4), round(y, 4)))
        write_table(__file__, ("name", "x", "y"), poles or [("none", 0, 0)], part=name + "-poles")
        write_table(__file__, ("name", "x", "y"),
                    [(n.replace(' ', '~'), round(x, 3), round(y, 3)) for n, x, y in labels(v)],
                    part=name + "-labels")
        fr.append((name, round(land_fraction(v, rs), 3)))
    write_table(__file__, ("view", "land_fraction"), fr, part="fractions")
    print(fr)

"""The global ocean conveyor belt, drawn as one schematic loop on the world
map, and the deep water's average speed (grade 8, chapter 4).

The route follows ledger nos:conveyor: warm surface water flows north
through the Atlantic (Gulf Stream), gives its heat to the air, sinks in the
far North Atlantic (drawn in the Norwegian Sea, as in the chapter's exercise), creeps south along the deep western Atlantic to the
Southern Ocean, east round Antarctica, north into the Pacific where it
rises, and returns at the surface west through the Indonesian seas, across
the Indian Ocean and round southern Africa. The real circulation has many
branches (the Indian Ocean one among them); this is the simplified single
loop of the chapter's figure, a sketch, not measured currents.

The waypoints are joined by a Catmull-Rom spline; every point of the
spline is tested to be at sea on the Natural Earth 110 m land (except in a
box round the Indonesian islands, which the schematic line crosses).

Speeds: the loop's length on the sphere (R from earth:Rmean) over about
1 000 years (nos:conveyor), against the Gulf Stream's 6.4 km/h
(nos:gulf-stream).

  parts surface, deep : lon lat   (segments separated by blank lines)
  parts heads-surface, heads-deep : lon lat u v
  part  marks         : lon lat label   (where the water sinks and rises)
  main table          : item value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import geo  # noqa: E402

R_EARTH = 6371.0            # earth:Rmean
LOOP_YEARS = 1000.0         # nos:conveyor ("about 1,000 years")
GULF_KM_H = 6.4             # nos:gulf-stream

SURFACE = [(160.0, 9.0), (148.0, 7.0), (132.0, 2.0), (126.0, -6.0), (112.0, -13.0), (85.0, -15.0),
           (60.0, -24.0), (38.0, -37.0), (18.0, -40.0), (2.0, -28.0), (-20.0, -8.0), (-42.0, 8.0),
           (-62.0, 15.0), (-76.0, 14.8), (-86.0, 21.0), (-85.5, 25.0), (-81.0, 23.9),
           (-79.6, 25.8), (-79.3, 27.8), (-77.6, 31.0), (-73.5, 35.0), (-58.0, 41.0), (-40.0, 46.0),
           (-27.0, 54.0), (-14.0, 60.0), (-3.0, 65.0)]
DEEP = [(-11.0, 63.0), (-24.0, 58.5), (-40.0, 54.0), (-48.0, 45.0), (-48.0, 28.0), (-34.0, 2.0),
        (-30.0, -25.0), (-24.0, -45.0), (-5.0, -55.0), (30.0, -56.0), (70.0, -55.0), (110.0, -55.0),
        (140.0, -56.0), (160.0, -50.0), (159.0, -36.0), (160.0, -22.0), (164.5, -11.0), (165.0, 5.0)]
SINK = (-6.0, 66.5)
RISE = (163.0, 8.0)
ISLANDS = (95.0, 140.0, -12.0, 8.0)     # lon_min lon_max lat_min lat_max


def unwrap(points):
    out = [points[0]]
    for lon, lat in points[1:]:
        while lon - out[-1][0] > 180:
            lon -= 360
        while lon - out[-1][0] < -180:
            lon += 360
        out.append((lon, lat))
    return out


def spline(points, n=12):
    """Catmull-Rom through the (unwrapped) waypoints."""
    p = unwrap(points)
    q = [p[0]] + p + [p[-1]]
    out = []
    for i in range(1, len(q) - 2):
        p0, p1, p2, p3 = q[i - 1], q[i], q[i + 1], q[i + 2]
        for k in range(n):
            t = k / n
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t
                                    + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t * t
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t ** 3) for j in (0, 1)))
    out.append(p[-1])
    return out


def wrap(lon):
    return (lon + 180.0) % 360.0 - 180.0


def split_wrapped(points):
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


def inside(pt, ring):
    x, y = pt
    c = False
    for (x0, y0), (x1, y1) in zip(ring, ring[1:] + ring[:1]):
        if (y0 > y) != (y1 > y) and x < x0 + (y - y0) * (x1 - x0) / (y1 - y0):
            c = not c
    return c


def on_land(pt, rings=None):
    rings = rings if rings is not None else geo.land_rings()
    p = (wrap(pt[0]), pt[1])
    return any(inside(p, r) for r in rings)


def in_island_box(pt):
    lon = wrap(pt[0])
    return ISLANDS[0] <= lon <= ISLANDS[1] and ISLANDS[2] <= pt[1] <= ISLANDS[3]


def great_circle(a, b, r=R_EARTH):
    lo1, la1, lo2, la2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def length_km(points):
    return sum(great_circle(p, q) for p, q in zip(points, points[1:]))


def numbers():
    surf = spline(SURFACE)
    deep = spline(DEEP)
    # close the loop: surface end -> sinking -> deep start, deep end -> rising -> surface start
    loop = length_km(surf) + length_km(deep) + great_circle(surf[-1], deep[0]) + great_circle(deep[-1], surf[0])
    km_yr = loop / LOOP_YEARS
    return {"loop_km": loop, "deep_km_per_year": km_yr, "deep_m_per_day": km_yr * 1000 / 365.25,
            "gulf_km_per_day": GULF_KM_H * 24, "ratio": GULF_KM_H * 24 * 365.25 / km_yr}


def heads(points, back=3):
    a, b = points[-1 - back], points[-1]
    return (wrap(b[0]), b[1], b[0] - a[0], b[1] - a[1])


if __name__ == "__main__":
    for name, pts in (("surface", SURFACE), ("deep", DEEP)):
        sp = spline(pts)
        rows = []
        for seg in split_wrapped(sp):
            rows += [()] + [(round(x, 2), round(y, 2)) for x, y in seg]
        write_table(__file__, ("lon", "lat"), rows[1:], part=name)
        # arrowheads every 5th of the way along, and at the end
        hd = []
        n = len(sp)
        for k in (n // 4, n // 2, 3 * n // 4, n - 1):
            lon, lat, u, v = heads(sp[:k + 1])
            norm = math.hypot(u, v) or 1.0
            hd.append((round(lon, 2), round(lat, 2), round(u / norm * 0.01, 5), round(v / norm * 0.01, 5)))
        write_table(__file__, ("lon", "lat", "u", "v"), hd, part="heads-" + name)
    write_table(__file__, ("lon", "lat", "label"),
                [(SINK[0], SINK[1], "sinks"), (RISE[0], RISE[1], "rises")], part="marks")
    nb = numbers()
    write_table(__file__, ("item", "value"), [(k, round(v, 3)) for k, v in nb.items()])
    for k, v in nb.items():
        print(k, round(v, 3))

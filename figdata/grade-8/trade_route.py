"""A trade-wind crossing of the Atlantic, from Praia (Cape Verde) to
Bridgetown (Barbados), for the problem of grade 8, chapter 2 (winds and the
global circulation).

Positions: Natural Earth populated places (data/derived/grade-6-ne-places.csv,
ledger data:b1-ne-places). Earth radius: shared ledger earth:Rmean (6371 km).
The ship's average speed is exercise data (SPEED_KMH).

  part route : lon lat               (the great circle, 41 points)
  part land  : lon lat               (Natural Earth land rings clipped to the
                                      map, rings separated by blank lines)
  part ports : lon lat name
  part trades: lon lat dlon dlat     (north-east trade-wind arrows on a grid,
                                      blowing towards the south-west, at sea)
  main table : item value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R_EARTH = 6371.0                    # km, ledger earth:Rmean
SPEED_KMH = 7.0                     # exercise data: the ship's average speed
FROM, TO = "Praia", "Bridgetown"
BOX = (-75.0, -5.0, 0.0, 35.0)      # lon min, lon max, lat min, lat max


def places():
    with open(os.path.join(ROOT, "data", "derived", "grade-6-ne-places.csv"), encoding="utf8") as f:
        return {r["name"]: (float(r["lon"]), float(r["lat"])) for r in csv.DictReader(f)}


def great_circle(a, b, r=R_EARTH):
    """Great-circle distance (km) between (lon, lat) points, haversine."""
    lo1, la1, lo2, la2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def km_per_degree_lon(lat, r=R_EARTH):
    """Length of one degree of longitude along a parallel (km)."""
    return 2 * math.pi * r / 360.0 * math.cos(math.radians(lat))


def km_per_degree_lat(r=R_EARTH):
    return 2 * math.pi * r / 360.0


def along_parallel(a, b, r=R_EARTH):
    """Simple school estimate: degrees of longitude times the length of a
    degree at the mean latitude, plus the change of latitude (Pythagoras)."""
    lat = (a[1] + b[1]) / 2.0
    dx = abs(b[0] - a[0]) * km_per_degree_lon(lat, r)
    dy = abs(b[1] - a[1]) * km_per_degree_lat(r)
    return math.hypot(dx, dy)


def route_points(a, b, n=40):
    """Points along the great circle (spherical interpolation)."""
    lo1, la1, lo2, la2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    p1 = (math.cos(la1) * math.cos(lo1), math.cos(la1) * math.sin(lo1), math.sin(la1))
    p2 = (math.cos(la2) * math.cos(lo2), math.cos(la2) * math.sin(lo2), math.sin(la2))
    om = math.acos(sum(x * y for x, y in zip(p1, p2)))
    pts = []
    for i in range(n + 1):
        t = i / n
        s1, s2 = math.sin((1 - t) * om) / math.sin(om), math.sin(t * om) / math.sin(om)
        x, y, z = (s1 * u + s2 * v for u, v in zip(p1, p2))
        pts.append((math.degrees(math.atan2(y, x)), math.degrees(math.asin(z))))
    return pts


def days(distance_km, speed_kmh=SPEED_KMH):
    return distance_km / (speed_kmh * 24.0)


def land_rings():
    """Land rings with at least one point in the box, clipped by clamping to
    the box (the axis clips the drawing as well)."""
    rings = {}
    with open(os.path.join(ROOT, "data", "derived", "ne-land-110m.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            rings.setdefault(r["ring"], []).append((float(r["lon"]), float(r["lat"])))
    lo0, lo1, la0, la1 = BOX
    out = []
    for ring in rings.values():
        if any(lo0 - 5 <= x <= lo1 + 5 and la0 - 5 <= y <= la1 + 5 for x, y in ring):
            out.append([(min(max(x, lo0 - 5), lo1 + 5), min(max(y, la0 - 5), la1 + 5)) for x, y in ring])
    return out


def inside(pt, ring):
    """Even-odd point-in-polygon test (lon/lat treated as plane coordinates)."""
    x, y = pt
    c = False
    for (x1, y1), (x2, y2) in zip(ring, ring[1:] + ring[:1]):
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            c = not c
    return c


def on_land(pt, rings=None):
    rings = rings if rings is not None else land_rings()
    return any(inside(pt, r) for r in rings)


def trade_arrows():
    """North-east trades between 10 and 28 degrees north, drawn only where the
    arrow's start and end are both at sea, blowing towards the south-west."""
    rings = land_rings()
    out = []
    for lat in (10, 16, 22, 28):
        for lon in range(-65, -15, 8):
            d = (-2.6, -1.6)
            if not on_land((lon, lat), rings) and not on_land((lon + d[0], lat + d[1]), rings):
                out.append((lon, lat, d[0], d[1]))
    return out


if __name__ == "__main__":
    pl = places()
    a, b = pl[FROM], pl[TO]
    write_table(__file__, ("lon", "lat"), [(round(x, 3), round(y, 3)) for x, y in route_points(a, b)], part="route")
    rows = []
    for ring in land_rings():
        rows += [()] + [(round(x, 3), round(y, 3)) for x, y in ring]
    write_table(__file__, ("lon", "lat"), rows[1:], part="land")
    write_table(__file__, ("lon", "lat", "name"), [(a[0], a[1], FROM), (b[0], b[1], TO)], part="ports")
    write_table(__file__, ("lon", "lat", "dlon", "dlat"), trade_arrows(), part="trades")
    gc = great_circle(a, b)
    write_table(__file__, ("item", "value"), [
        ("from_lon", a[0]), ("from_lat", a[1]), ("to_lon", b[0]), ("to_lat", b[1]),
        ("dlon_deg", round(abs(b[0] - a[0]), 2)),
        ("mean_lat", round((a[1] + b[1]) / 2, 2)),
        ("km_per_deg_lon_at_mean", round(km_per_degree_lon((a[1] + b[1]) / 2), 1)),
        ("km_per_deg_lat", round(km_per_degree_lat(), 1)),
        ("great_circle_km", round(gc, 0)),
        ("school_estimate_km", round(along_parallel(a, b), 0)),
        ("speed_kmh", SPEED_KMH),
        ("km_per_day", SPEED_KMH * 24),
        ("days", round(days(gc), 1)),
    ])

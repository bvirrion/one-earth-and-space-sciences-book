"""Maps of the whole Earth, grade 9, chapter 5: the Mercator projection and
an equal-area projection (Mollweide, from figdata/shared/geo.py) side by side,
with equal circles drawn on the globe (Tissot's idea), and the true and the
drawn areas of Greenland and Africa.

Land: Natural Earth land polygons (ledger data:ne-land); the 1:110m rings for
the maps, the 1:50m rings for the areas. Greenland is a ring of its own; the
African mainland is cut out of the Afro-Eurasian ring at the Isthmus of Suez
(between the two coastline vertices nearest Port Said and Suez), so islands
such as Madagascar are not counted.

Both maps use "degree" units: the Mercator x is the longitude, its y is
degrees(ln tan(45 + lat/2)) (so one unit is one degree of the equator); the
Mollweide coordinates (in Earth radii) are multiplied by 180/pi. The Mercator
map stops at 80 S and 84 N (the projection runs off to infinity at the poles).

  part merc-land, moll-land            : x y    (rings separated by blank rows)
  part merc-greenland, moll-greenland  : x y
  part merc-africa, moll-africa        : x y
  part merc-circles, moll-circles      : x y    (the circles on the globe)
  part merc-grid, moll-grid            : x y    (parallels every 30, meridians every 60)
  part areas                           : item value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import geo  # noqa: E402

R_KM = 6371.0
MERC_LAT = (-80.0, 84.0)
CIRCLE_RADIUS = 7.0                        # degrees of arc on the globe
CIRCLE_LATS = (-60, -30, 0, 30, 60)
CIRCLE_LONS = (-120, -60, 0, 60, 120)
PORT_SAID = (32.30, 31.27)
SUEZ = (32.55, 29.97)
CAPE_AGULHAS = (20.0, -34.8)


# --------------------------------------------------------------------------
# projections, in degree units
# --------------------------------------------------------------------------
def mercator(lon, lat):
    lat = min(max(lat, MERC_LAT[0]), MERC_LAT[1])
    return lon, math.degrees(math.log(math.tan(math.radians(45.0 + lat / 2.0))))


def mollweide(lon, lat):
    x, y = geo.mollweide(lon, lat)
    return math.degrees(x), math.degrees(y)


def mercator_area_factor(lat):
    """How many times the Mercator projection enlarges areas at a latitude."""
    return 1.0 / math.cos(math.radians(lat)) ** 2


# --------------------------------------------------------------------------
# rings and areas
# --------------------------------------------------------------------------
def rings(name):
    out = {}
    for r in geo.read(name):
        out.setdefault(int(r["ring"]), []).append((float(r["lon"]), float(r["lat"])))
    return [out[k] for k in sorted(out)]


def _box(ring):
    lons = [p[0] for p in ring]
    lats = [p[1] for p in ring]
    return min(lons), max(lons), min(lats), max(lats)


def greenland(name="ne-land-50m"):
    for ring in rings(name):
        x0, x1, y0, y1 = _box(ring)
        if x0 < -40 < x1 and y0 < 72 < y1 and y1 > 80:
            return ring
    raise ValueError("Greenland ring not found")


def _nearest(ring, pt):
    return min(range(len(ring)), key=lambda i: (ring[i][0] - pt[0]) ** 2 + (ring[i][1] - pt[1]) ** 2)


def africa(name="ne-land-50m"):
    """The African mainland: the arc of the Afro-Eurasian ring from Suez round
    the Cape to Port Said (the one that passes nearest Cape Agulhas)."""
    big = max((r for r in rings(name) if _box(r)[0] < 20 < _box(r)[1] and _box(r)[2] < 0 < _box(r)[3]),
              key=len)
    ring = big[:-1] if big[0] == big[-1] else big
    a, b = sorted((_nearest(ring, PORT_SAID), _nearest(ring, SUEZ)))
    inner = ring[a:b + 1]
    outer = ring[b:] + ring[:a + 1]
    cape = lambda arc: min((p[0] - CAPE_AGULHAS[0]) ** 2 + (p[1] - CAPE_AGULHAS[1]) ** 2 for p in arc)  # noqa: E731
    arc = inner if cape(inner) < cape(outer) else outer
    return arc + [arc[0]]


def sphere_area_km2(ring):
    """Area of a lon/lat ring on a sphere of radius R_KM (km2), any orientation."""
    s = 0.0
    n = len(ring)
    for i in range(n):
        lon1, lat1 = ring[i]
        lon2, lat2 = ring[(i + 1) % n]
        dl = math.radians(lon2 - lon1)
        if dl > math.pi:
            dl -= 2 * math.pi
        elif dl < -math.pi:
            dl += 2 * math.pi
        s += dl * (2 + math.sin(math.radians(lat1)) + math.sin(math.radians(lat2)))
    return abs(s) * R_KM * R_KM / 2.0


def plane_area(points):
    s = 0.0
    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0


def areas():
    g, a = greenland(), africa()
    p = {}
    p["greenland_Mkm2"] = sphere_area_km2(g) / 1e6
    p["africa_Mkm2"] = sphere_area_km2(a) / 1e6
    p["true_ratio"] = p["africa_Mkm2"] / p["greenland_Mkm2"]
    p["mercator_ratio"] = plane_area([mercator(*q) for q in a]) / plane_area([mercator(*q) for q in g])
    p["mollweide_ratio"] = plane_area([mollweide(*q) for q in a]) / plane_area([mollweide(*q) for q in g])
    p["factor_60"] = mercator_area_factor(60.0)
    p["factor_72"] = mercator_area_factor(72.0)
    return p


# --------------------------------------------------------------------------
# circles on the globe and the graticule
# --------------------------------------------------------------------------
def small_circle(lon0, lat0, radius_deg, n=72):
    """Points at angular distance radius_deg from (lon0, lat0) on the sphere."""
    la0, lo0, d = math.radians(lat0), math.radians(lon0), math.radians(radius_deg)
    out = []
    for k in range(n + 1):
        az = 2 * math.pi * k / n
        la = math.asin(math.sin(la0) * math.cos(d) + math.cos(la0) * math.sin(d) * math.cos(az))
        lo = lo0 + math.atan2(math.sin(az) * math.sin(d) * math.cos(la0),
                              math.cos(d) - math.sin(la0) * math.sin(la))
        out.append((math.degrees(lo), math.degrees(la)))
    return out


def circles():
    return [small_circle(lo, la, CIRCLE_RADIUS) for la in CIRCLE_LATS for lo in CIRCLE_LONS]


def graticule():
    lines = []
    for lat in range(-60, 61, 30):
        lines.append([(lon, lat) for lon in range(-180, 181, 5)])
    for lon in range(-180, 181, 60):
        lines.append([(lon, lat) for lat in range(-90, 91, 2)])
    return lines


def _rows(lines, proj):
    rows = []
    for line in lines:
        rows += [()] + [tuple(round(v, 3) for v in proj(*p)) for p in line]
    return rows[1:]


if __name__ == "__main__":
    land = rings("ne-land-110m")
    for tag, proj in (("merc", mercator), ("moll", mollweide)):
        write_table(__file__, ("x", "y"), _rows(land, proj), part=tag + "-land")
        write_table(__file__, ("x", "y"), _rows([greenland("ne-land-110m")], proj), part=tag + "-greenland")
        write_table(__file__, ("x", "y"), _rows([africa("ne-land-110m")], proj), part=tag + "-africa")
        write_table(__file__, ("x", "y"), _rows(circles(), proj), part=tag + "-circles")
        write_table(__file__, ("x", "y"), _rows(graticule(), proj), part=tag + "-grid")
    p = areas()
    write_table(__file__, ("item", "value"), [(k, round(v, 3)) for k, v in p.items()], part="areas")
    for k, v in p.items():
        print(k, round(v, 3))

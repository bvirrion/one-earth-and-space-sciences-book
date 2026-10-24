"""The Kuril subduction zone read from its earthquakes (Year 1, active-margins).

Data:
  * earthquakes of magnitude 5 or more, 1976-2025, in the box 40-56 N, 138-165 E
    (USGS ComCat; dataset bachelor-1-usgs-kuril.csv, ledger data:b3-usgs-kuril);
  * Holocene volcanoes (shared gvp-holocene.csv, ledger data:gvp);
  * PB2002 boundary steps (shared pb2002-steps.csv, ledger data:pb2002): the trench
    and the convergence rate;
  * the age of the ocean floor (Book 2's grade-11-seafloor-age.csv, ledger
    data:b2-seafloor-age, read only);
  * land from Natural Earth 1:50m (shared ne-land-50m.csv).

The section starts at the PB2002 trench step nearest to TRENCH_NEAR and runs
perpendicular to the trench, toward the overriding plate (Okhotsk). Every event or
volcano is placed by its along-track distance x and cross-track distance y on the
sphere, both measured along great circles from the trench point; those with
|y| <= HALF_WIDTH are kept.

The slab line is the least-squares line z = a + s x through the events deeper than
ZMIN (inside the sinking plate, below the plate interface). The volcanic front is
the volcano of the strip nearest to the trench; the slab depth beneath it is
a + s x_front.

The arc radius: the PB2002 trench steps of the Kuril trench between ARC_LAT are
fitted by a small circle (the plane through them that best fits in 3-D, by least
squares); its angular radius is compared with half the slab dip (Frank 1968).

  part section   x depth mag            events of the strip, -100 <= x <= 800 km
  part volcanoes x name_index           volcanoes of the strip, 0 <= x <= 600 km
  part map-q<c>  lon lat                events of the box by depth class c:
                                        shallow (< 70 km), mid (70-300), deep (> 300)
  part map-volc  lon lat                Holocene volcanoes of the box
  part map-land  lon lat                land rings clipped to the box (nan rows between)
  part map-trench lon lat               subduction lines of the box (PB2002)
  part map-teeth lon lat                teeth on the overriding side
  part map-strip lon lat                outline of the strip (0-800 km, +-150 km)
  part values    what value
"""
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
import geo  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
DERIVED = os.path.join(ROOT, "data", "derived")
R_KM = 6371.0
TRENCH_NEAR = (153.0, 46.0)      # lon, lat: a point off the central Kuril Islands
STEP_NAME = "OK/PA"              # Pacific sinks under Okhotsk; Okhotsk on the left
HALF_WIDTH = 150.0               # km
ZMIN = 70.0                      # km: events deeper than this lie inside the slab
BOX = (138.0, 165.0, 40.0, 56.0)
ARC_LAT = (41.0, 52.0)           # the Kuril trench, Hokkaido to southern Kamchatka
ARC_CENTRAL = (42.5, 50.5)       # a shorter stretch, to show how the radius depends on it
MAP_SCALE_LAT = 48.0             # map x unit = one degree of longitude at this latitude


def read(name):
    with open(os.path.join(DERIVED, name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def unit(lon, lat):
    p, l = math.radians(lat), math.radians(lon)
    return np.array([math.cos(p) * math.cos(l), math.cos(p) * math.sin(l), math.sin(p)])


def lonlat(v):
    v = v / np.linalg.norm(v)
    return math.degrees(math.atan2(v[1], v[0])), math.degrees(math.asin(max(-1.0, min(1.0, v[2]))))


def destination(lon, lat, azimuth, dist_km):
    """Point reached from (lon, lat) along a great circle of initial azimuth (deg)."""
    p, l, a, d = math.radians(lat), math.radians(lon), math.radians(azimuth), dist_km / R_KM
    p2 = math.asin(math.sin(p) * math.cos(d) + math.cos(p) * math.sin(d) * math.cos(a))
    l2 = l + math.atan2(math.sin(a) * math.sin(d) * math.cos(p), math.cos(d) - math.sin(p) * math.sin(p2))
    return (math.degrees(l2) + 540.0) % 360.0 - 180.0, math.degrees(p2)


def bearing(lon1, lat1, lon2, lat2):
    """Initial azimuth (deg) of the great circle from point 1 to point 2."""
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dl = math.radians(lon2 - lon1)
    return math.degrees(math.atan2(math.sin(dl) * math.cos(p2),
                                   math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl))) % 360.0


def along_across(lon0, lat0, azimuth, lon, lat):
    """Along-track x and cross-track y (km, y > 0 to the right) of (lon, lat) relative
    to the great circle leaving (lon0, lat0) with the given azimuth."""
    o = unit(lon0, lat0)
    north = np.array([-math.sin(math.radians(lat0)) * math.cos(math.radians(lon0)),
                      -math.sin(math.radians(lat0)) * math.sin(math.radians(lon0)),
                      math.cos(math.radians(lat0))])
    east = np.cross(north, o)
    a = math.radians(azimuth)
    t = math.cos(a) * north + math.sin(a) * east      # direction of the track at o
    n = np.cross(o, t)                                # pole of the track (left side)
    p = unit(lon, lat)
    y = -math.asin(max(-1.0, min(1.0, float(p @ n)))) * R_KM
    x = math.atan2(float(p @ t), float(p @ o)) * R_KM
    return x, y


def trench():
    """Trench point (lon, lat), strike (deg), azimuth toward the overriding plate,
    PB2002 relative speed (mm/yr) and its azimuth."""
    steps = [s for s in read("pb2002-steps") if s["class"] == "SUB" and s["name"] == STEP_NAME]
    near = unit(*TRENCH_NEAR)
    best = max(steps, key=lambda s: float(unit(float(s["lon"]), float(s["lat"])) @ near))
    t_lon, t_lat = float(best["lon"]), float(best["lat"])
    x, y = along_across(t_lon, t_lat, 0.0, float(best["lon1"]), float(best["lat1"]))
    x0, y0 = along_across(t_lon, t_lat, 0.0, float(best["lon0"]), float(best["lat0"]))
    strike = math.degrees(math.atan2(y - y0, x - x0)) % 360.0   # bearing of the step
    toward = (strike - 90.0) % 360.0                   # the overriding plate is on the left
    return (t_lon, t_lat), strike, toward, float(best["vel_mm_a"]), float(best["vel_az"])


def quakes():
    return [(float(e["lon"]), float(e["lat"]), float(e["depth_km"]), float(e["mag"]))
            for e in read("bachelor-1-usgs-kuril")]


def strip(points, origin, azimuth, xmin, xmax):
    """[(x, *rest)] for points (lon, lat, *rest) in the strip, sorted by x."""
    out = []
    for p in points:
        x, y = along_across(origin[0], origin[1], azimuth, p[0], p[1])
        if abs(y) <= HALF_WIDTH and xmin <= x <= xmax:
            out.append((x,) + tuple(p[2:]))
    return sorted(out)


def lsq_line(pts):
    """Least-squares z = a + s x; returns a, s."""
    n = len(pts)
    sx = sum(x for x, _ in pts)
    sz = sum(z for _, z in pts)
    sxx = sum(x * x for x, _ in pts)
    sxz = sum(x * z for x, z in pts)
    s = (n * sxz - sx * sz) / (n * sxx - sx * sx)
    return (sz - s * sx) / n, s


def small_circle(points):
    """Best small circle through (lon, lat) points: the plane n.p = d fitted by least
    squares in 3-D. Returns (pole lon, pole lat, angular radius in degrees), the pole
    taken on the side of the circle's centre (radius < 90 deg)."""
    p = np.array([unit(lon, lat) for lon, lat in points])
    c = p.mean(axis=0)
    _, _, vt = np.linalg.svd(p - c)
    n = vt[-1]
    d = float(n @ c)
    if d < 0:
        n, d = -n, -d
    return lonlat(n) + (math.degrees(math.acos(min(1.0, d))),)


def arc_points(lat_range=None):
    lat_range = ARC_LAT if lat_range is None else lat_range
    steps = [s for s in read("pb2002-steps") if s["class"] == "SUB" and s["name"] == STEP_NAME]
    return [(float(s["lon"]), float(s["lat"])) for s in steps
            if lat_range[0] <= float(s["lat"]) <= lat_range[1]]


def incoming_age(origin, toward, lo=100.0, hi=400.0):
    """Median age (Myr) of the one-degree cells of the subducting plate between lo and
    hi km seaward of the trench point, within HALF_WIDTH of the section line."""
    ages = []
    for r in read("grade-11-seafloor-age"):
        lon, lat = float(r["lon"]), float(r["lat"])
        if not (BOX[0] - 5 <= lon <= BOX[1] + 15 and BOX[2] - 10 <= lat <= BOX[3]):
            continue
        x, y = along_across(origin[0], origin[1], toward, lon, lat)
        if -hi <= x <= -lo and abs(y) <= HALF_WIDTH:
            ages.append(float(r["age"]))
    ages.sort()
    return ages[len(ages) // 2] if ages else float("nan")


def in_box(lon, lat, pad=0.0):
    return BOX[0] - pad <= lon <= BOX[1] + pad and BOX[2] - pad <= lat <= BOX[3] + pad


def clip_ring(ring, box):
    """Sutherland-Hodgman clipping of a closed lon/lat ring to a rectangle
    (lon0, lon1, lat0, lat1); returns the clipped ring (closed) or []."""
    def clip(pts, inside, cut):
        out = []
        for i, cur in enumerate(pts):
            prev = pts[i - 1]
            if inside(cur):
                if not inside(prev):
                    out.append(cut(prev, cur))
                out.append(cur)
            elif inside(prev):
                out.append(cut(prev, cur))
        return out

    def at_lon(lon):
        return lambda a, b: (lon, a[1] + (b[1] - a[1]) * (lon - a[0]) / (b[0] - a[0]))

    def at_lat(lat):
        return lambda a, b: (a[0] + (b[0] - a[0]) * (lat - a[1]) / (b[1] - a[1]), lat)

    pts = list(ring[:-1]) if ring[0] == ring[-1] else list(ring)
    for inside, cut in ((lambda p: p[0] >= box[0], at_lon(box[0])), (lambda p: p[0] <= box[1], at_lon(box[1])),
                        (lambda p: p[1] >= box[2], at_lat(box[2])), (lambda p: p[1] <= box[3], at_lat(box[3]))):
        if not pts:
            return []
        pts = clip(pts, inside, cut)
    return pts + pts[:1] if len(pts) >= 3 else []


def rows_with_nan(polylines):
    """Rows of several polylines separated by a (nan, nan) row: pgfplots, with
    unbounded coords=jump, fills each ring on its own (an empty-line jump left
    some rings unfilled)."""
    rows = []
    for pts in polylines:
        if rows:
            rows.append((float("nan"), float("nan")))
        rows += [(round(x, 3), round(y, 3)) for x, y in pts]
    return rows


def map_teeth(lines):
    """Teeth on the left of each line, drawn in map units where one degree of longitude
    is cos(MAP_SCALE_LAT) as long as one degree of latitude."""
    k = math.cos(math.radians(MAP_SCALE_LAT))
    scaled = [[(lon * k, lat) for lon, lat in pts] for pts in lines]
    tris = geo.teeth(scaled, spacing=0.7, base=0.32, height=0.27)
    return [[(x / k, y) for x, y in t] for t in tris]


def analysis():
    origin, strike, toward, vel, vel_az = trench()
    q = quakes()
    sec = strip([(lon, lat, z, m) for lon, lat, z, m in q], origin, toward, -100.0, 800.0)
    deep = [(x, z) for x, z, _ in sec if z > ZMIN]
    a, s = lsq_line(deep)
    names = [(float(v["lon"]), float(v["lat"]), v["name"]) for v in read("gvp-holocene")]
    volc = strip(names, origin, toward, 0.0, 600.0)
    x_front = volc[0][0]
    pole_lon, pole_lat, radius = small_circle(arc_points())
    normal = abs(vel * math.cos(math.radians(vel_az - (toward + 180.0))))
    vals = {
        "trench_lon": origin[0], "trench_lat": origin[1], "strike": strike, "toward": toward,
        "n_section": len(sec), "n_fit": len(deep), "fit_a": a, "fit_s": s,
        "dip": math.degrees(math.atan(s)), "max_depth": max(z for _, z, _ in sec),
        "x_front": x_front, "slab_depth_front": a + s * x_front,
        "x_at_120": (120.0 - a) / s, "x_at_100": (100.0 - a) / s,
        "n_volc": len(volc), "vel": vel, "vel_az": vel_az, "vel_normal": normal,
        "age_in": incoming_age(origin, toward), "arc_pole_lon": pole_lon,
        "arc_pole_lat": pole_lat, "arc_radius": radius, "n_arc": len(arc_points()),
        "arc_radius_central": small_circle(arc_points(ARC_CENTRAL))[2],
        "n_box": len(q), "n_box_deep": sum(1 for e in q if e[2] > 300.0),
    }
    return origin, toward, sec, volc, vals


if __name__ == "__main__":
    origin, toward, sec, volc, vals = analysis()
    write_table(__file__, ("x", "depth", "mag"), [(round(x, 2), z, m) for x, z, m in sec], part="section")
    write_table(__file__, ("x", "idx"), [(round(v[0], 2), i) for i, v in enumerate(volc)], part="volcanoes")
    q = quakes()
    for c, lo, hi in (("shallow", -1.0, 70.0), ("mid", 70.0, 300.0), ("deep", 300.0, 1e9)):
        write_table(__file__, ("lon", "lat"),
                    [(e[0], e[1]) for e in q if lo < e[2] <= hi] if c != "shallow"
                    else [(e[0], e[1]) for e in q if e[2] < 70.0], part="map-q" + c)
    write_table(__file__, ("lon", "lat"),
                [(float(v["lon"]), float(v["lat"])) for v in read("gvp-holocene")
                 if in_box(float(v["lon"]), float(v["lat"]))], part="map-volc")
    rings = {}
    for r in read("ne-land-50m"):
        rings.setdefault(int(r["ring"]), []).append((float(r["lon"]), float(r["lat"])))
    pad = (BOX[0] - 1.0, BOX[1] + 1.0, BOX[2] - 1.0, BOX[3] + 1.0)
    keep = [r for r in (clip_ring(rings[k], pad) for k in sorted(rings)) if r]
    write_table(__file__, ("lon", "lat"), rows_with_nan(keep), part="map-land")
    lines = [p for _, _, p in geo.boundary_lines(geo.SUBDUCTION)
             if any(in_box(lon, lat, 3.0) for lon, lat in p)]
    write_table(__file__, ("lon", "lat"), rows_with_nan(lines), part="map-trench")
    write_table(__file__, ("lon", "lat"), rows_with_nan(map_teeth(lines)), part="map-teeth")
    outline, left, right = [], [], []
    for d in range(0, 801, 50):
        foot = destination(origin[0], origin[1], toward, d)
        local = bearing(*foot, *destination(origin[0], origin[1], toward, d + 1.0))
        left.append(destination(*foot, (local - 90.0) % 360.0, HALF_WIDTH))
        right.append(destination(*foot, (local + 90.0) % 360.0, HALF_WIDTH))
    outline = left + right[::-1]
    outline.append(outline[0])
    write_table(__file__, ("lon", "lat"), [(round(a, 4), round(b, 4)) for a, b in outline], part="map-strip")
    write_table(__file__, ("what", "value"), sorted(vals.items()), part="values", digits=6)

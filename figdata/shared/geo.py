"""World base map for every book: land, plate boundaries, earthquakes, volcanoes.

Reads data/derived/ (tools/fetch_data.py) and writes, when run, plot tables for
pgfplots in longitude/latitude degrees (equirectangular, the `ommap` style):

  shared-geo-land.dat         lon lat   land rings (Natural Earth 1:110m), an
                                        empty line between rings (a jump)
  shared-geo-ridge.dat        lon lat   divergent: oceanic spreading ridges and
                                        continental rifts (PB2002 OSR, CRB)
  shared-geo-transform.dat    lon lat   transform faults (OTF, CTF)
  shared-geo-subduction.dat   lon lat   subduction zones, each line ORIENTED so
                                        that the overriding plate is on its LEFT
                                        (draw with the `subduction` style: the
                                        teeth go on the overriding plate)
  shared-geo-collision.dat    lon lat   other convergent boundaries (CCB, OCB)
  shared-geo-teeth.dat        lon lat   the subduction teeth as small filled
                                        triangles on the overriding side
                                        (\addplot[fill=omTrench, draw=none]):
                                        a TikZ decoration cannot place them on
                                        a path with jumps
  shared-geo-school-<kind>.dat          the same five boundary tables and the
                                        teeth for the plates a school map shows:
                                        the Amur and Yangtze plates merged into
                                        Eurasia, Okhotsk into North America, so
                                        the diffuse boundaries across Siberia
                                        and China disappear (SCHOOL_MERGE)
  shared-geo-quakes.dat       lon lat depth mag   M >= 6, 1976-2025 (USGS)
  shared-geo-volcanoes.dat    lon lat   Holocene volcanoes (GVP)

Credit in captions: Natural Earth; plate boundaries from Bird (2003); USGS
ComCat; Smithsonian Global Volcanism Program (ledger data:ne-land, data:pb2002,
data:usgs-comcat, data:gvp).

PB2002 conventions (Bird 2003, checked against known trenches in the test):
the first-named plate of a step lies on the LEFT of its direction of
digitization; in a subduction name "A\\B" plate A sinks under B, in "A/B" plate
B sinks under A.

Projections are pure functions (tested): equirectangular, Mollweide.
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DERIVED = os.path.join(ROOT, "data", "derived")

# School maps: microplates of diffuse continental deformation merged into their
# large neighbour (a boundary between two plates of one group is not drawn).
SCHOOL_MERGE = {"AM": "EU", "YA": "EU", "OK": "NA"}

RIDGE = ("OSR", "CRB")
TRANSFORM = ("OTF", "CTF")
SUBDUCTION = ("SUB",)
COLLISION = ("CCB", "OCB")


def read(name):
    with open(os.path.join(DERIVED, name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


# ----------------------------------------------------------------------------
# projections
# ----------------------------------------------------------------------------
def equirectangular(lon, lat):
    return lon, lat


def mollweide(lon, lat, lon0=0.0):
    """Mollweide x, y in units of the Earth radius (x in [-2 sqrt 2, 2 sqrt 2])."""
    phi = math.radians(lat)
    d = lon - lon0
    while d > 180.0:
        d -= 360.0
    while d < -180.0:
        d += 360.0
    lam = math.radians(d)
    if abs(abs(lat) - 90.0) < 1e-9:
        theta = math.copysign(math.pi / 2, lat)
    else:
        theta = phi
        for _ in range(60):                      # Newton on 2t + sin 2t = pi sin phi
            f = 2 * theta + math.sin(2 * theta) - math.pi * math.sin(phi)
            d = f / (2 + 2 * math.cos(2 * theta))
            theta -= d
            if abs(d) < 1e-12:
                break
    x = 2 * math.sqrt(2) / math.pi * lam * math.cos(theta)
    y = math.sqrt(2) * math.sin(theta)
    return x, y


# ----------------------------------------------------------------------------
# geometry helpers
# ----------------------------------------------------------------------------
def split_dateline(points):
    """Split a lon/lat polyline wherever it jumps across the 180th meridian."""
    out, cur = [], []
    for p in points:
        if cur and abs(p[0] - cur[-1][0]) > 180:
            out.append(cur)
            cur = []
        cur.append(p)
    if cur:
        out.append(cur)
    return out


def land_rings():
    rings = {}
    for r in read("ne-land-110m"):
        rings.setdefault(int(r["ring"]), []).append((float(r["lon"]), float(r["lat"])))
    return [rings[k] for k in sorted(rings)]


def subducting_plate(name):
    """'NZ\\SA' -> 'NZ' (A sinks under B); 'CA/SA' -> 'SA' (B sinks under A)."""
    if "\\" in name:
        return name.split("\\")[0]
    if "/" in name:
        return name.split("/")[1]
    return None


def overriding_plate(name):
    a, b = name.replace("\\", "/").split("/")
    return b if subducting_plate(name) == a else a


def _plates(name):
    return name.replace("\\", "/").replace("-", "/").split("/")


def boundary_lines(classes, merge=None):
    """Chain consecutive PB2002 steps of one boundary and class into polylines.

    Subduction lines are reversed where needed so that the overriding plate is
    on the left of the line's direction."""
    lines, cur, key = [], [], None
    for s in read("pb2002-steps"):
        if s["class"] not in classes:
            if cur:
                lines.append((key, cur))
            cur, key = [], None
            continue
        p0 = (float(s["lon0"]), float(s["lat0"]))
        p1 = (float(s["lon1"]), float(s["lat1"]))
        k = (s["name"], s["class"])
        if cur and k == key and abs(cur[-1][0] - p0[0]) < 1e-6 and abs(cur[-1][1] - p0[1]) < 1e-6:
            cur.append(p1)
        else:
            if cur:
                lines.append((key, cur))
            cur, key = [p0, p1], k
    if cur:
        lines.append((key, cur))
    out = []
    for (name, cls), pts in lines:
        if merge:
            a, b = _plates(name)
            if merge.get(a, a) == merge.get(b, b):
                continue
        if cls in SUBDUCTION:
            # the first-named plate is on the left; the overriding one must be
            first = name.replace("\\", "/").split("/")[0]
            if overriding_plate(name) != first:
                pts = pts[::-1]
        for piece in split_dateline(pts):
            if len(piece) >= 2:
                out.append((name, cls, piece))
    return out


def _rows_with_jumps(polylines):
    rows = []
    for pts in polylines:
        if rows:
            rows.append(())
        rows += [(round(x, 3), round(y, 3)) for x, y in pts]
    return rows


def teeth(polylines, spacing=4.0, base=2.2, height=2.0):
    """Triangles on the LEFT of each polyline, every `spacing` units of length
    (map units: degrees on an equirectangular map), base centred on the line."""
    joined = []
    for pts in polylines:
        if joined and math.hypot(joined[-1][-1][0] - pts[0][0], joined[-1][-1][1] - pts[0][1]) < 1e-6:
            joined[-1] = joined[-1] + list(pts[1:])
        else:
            joined.append(list(pts))
    tris = []
    for pts in joined:
        length = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:]))
        if length < base:
            continue
        run = min(spacing / 2, length / 2)
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            seg = math.hypot(x1 - x0, y1 - y0)
            if seg == 0:
                continue
            tx, ty = (x1 - x0) / seg, (y1 - y0) / seg
            nx, ny = -ty, tx
            s = run
            while s <= seg:
                px, py = x0 + tx * s, y0 + ty * s
                tris.append([(px - tx * base / 2, py - ty * base / 2),
                             (px + tx * base / 2, py + ty * base / 2),
                             (px + nx * height, py + ny * height),
                             (px - tx * base / 2, py - ty * base / 2)])
                s += spacing
            run = s - seg
    return tris


def quakes():
    return [(float(e["lon"]), float(e["lat"]), float(e["depth_km"]), float(e["mag"]))
            for e in read("usgs-m6")]


def volcanoes():
    return [(float(v["lon"]), float(v["lat"])) for v in read("gvp-holocene")]


if __name__ == "__main__":
    write_table(__file__, ("lon", "lat"), _rows_with_jumps(land_rings()), part="land")
    for prefix, merge in (("", None), ("school-", SCHOOL_MERGE)):
        for part, classes in (("ridge", RIDGE), ("transform", TRANSFORM),
                              ("subduction", SUBDUCTION), ("collision", COLLISION)):
            write_table(__file__, ("lon", "lat"), _rows_with_jumps(
                [p for _, _, p in boundary_lines(classes, merge)]), part=prefix + part)
        write_table(__file__, ("lon", "lat"), _rows_with_jumps(
            teeth([p for _, _, p in boundary_lines(SUBDUCTION, merge)])), part=prefix + "teeth")
    write_table(__file__, ("lon", "lat", "depth", "mag"),
                [(round(a, 3), round(b, 3), c, d) for a, b, c, d in quakes()], part="quakes")
    write_table(__file__, ("lon", "lat"), volcanoes(), part="volcanoes")

"""Closing the South Atlantic by a finite rotation (Year 1, plate-kinematics).

Rotation of South America relative to southern Africa from Heine, Zoethout and
Mueller (2013), Solid Earth 4, 215-253, Table 2 (CC BY 3.0) -- ledger heine:sam-saf:
  120.6 Ma (magnetic anomaly M0, young side): pole 51.28 N, 33.67 W, angle 52.35 deg;
  83.5 Ma (anomaly 34): pole 61.88 N, 34.26 W, angle 33.51 deg.
The table prints these pairs as "51.28, -33.67" under columns headed Lon, Lat; read
as latitude then longitude they give the classical North Atlantic poles of the
South America--Africa fit and close the ocean (the other reading sends Recife to
the Southern Ocean; checked in the tests).
A positive angle turns anticlockwise seen from above the pole (right-hand rule
about the outward pole vector). The rotation matrix is built with Rodrigues'
formula R = cos(a) I + (1 - cos(a)) n n^T + sin(a) [n]x.

Coastlines: Natural Earth 1:50m land (shared dataset ne-land-50m.csv, ledger
data:ne-land). Each continent is cut out of its ring as the arc between two land
bridges that contains a reference point: South America between the Pacific and
Caribbean ends of the Colombia-Panama border (77.9 W 7.2 N; 77.4 W 8.7 N), the arc
through Cape Horn; Africa between the head of the Gulf of Suez (32.55 E 29.95 N) and
Port Said (32.30 E 31.26 N), the arc through Cape Agulhas. Each is one closed piece.

  part sa      lon lat   South America today (nan rows separate pieces)
  part sa120   lon lat   rotated to 120.6 Ma
  part sa84    lon lat   rotated to 83.5 Ma
  part af      lon lat   Africa
  part track   lon lat   Recife carried back along its small circle about the 120.6 Ma
               pole, one row per degree of rotation (0 to 52.35 deg)
  part values  what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
LAND = os.path.join(ROOT, "data", "derived", "ne-land-50m.csv")
ROT_120 = (51.28, -33.67, 52.35)
ROT_84 = (61.88, -34.26, 33.51)
NAN = float("nan")


def unit(lat, lon):
    la, lo = math.radians(lat), math.radians(lon)
    return (math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la))


def to_latlon(v):
    return (math.degrees(math.asin(max(-1.0, min(1.0, v[2])))),
            math.degrees(math.atan2(v[1], v[0])))


def rotation_matrix(lat, lon, angle_deg):
    """Rodrigues' formula for a rotation of angle_deg about the axis through (lat, lon)."""
    n = unit(lat, lon)
    a = math.radians(angle_deg)
    c, s = math.cos(a), math.sin(a)
    k = ((0.0, -n[2], n[1]), (n[2], 0.0, -n[0]), (-n[1], n[0], 0.0))
    return tuple(tuple(c * (i == j) + (1 - c) * n[i] * n[j] + s * k[i][j] for j in range(3))
                 for i in range(3))


def apply(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def det(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def rotate_point(rot, lat, lon):
    return to_latlon(apply(rotation_matrix(*rot), unit(lat, lon)))


def _rings():
    rings = {}
    with open(LAND, encoding="utf8") as f:
        for r in csv.DictReader(f):
            rings.setdefault(int(r["ring"]), []).append((float(r["lon"]), float(r["lat"])))
    return rings


def _largest_containing(rings, lon, lat):
    best = None
    for k, pts in rings.items():
        lons = [p[0] for p in pts]
        lats = [p[1] for p in pts]
        if min(lons) <= lon <= max(lons) and min(lats) <= lat <= max(lats):
            if best is None or len(pts) > len(rings[best]):
                best = k
    return rings[best]


def _arc(ring, end1, end2, through):
    """The arc of a closed ring between the points nearest end1 and end2 (lon, lat)
    that contains the point nearest `through`."""
    def nearest(q):
        return min(range(len(ring)), key=lambda k: (ring[k][0] - q[0]) ** 2 + (ring[k][1] - q[1]) ** 2)
    i, j, t = nearest(end1), nearest(end2), nearest(through)
    if i > j:
        i, j = j, i
    inner = ring[i:j + 1]
    outer = ring[j:] + ring[:i + 1]
    return inner if i <= t <= j else outer


def south_america():
    ring = _largest_containing(_rings(), -60.0, -10.0)
    return [_arc(ring, (-77.9, 7.2), (-77.4, 8.7), (-67.3, -55.9))]


def africa():
    ring = _largest_containing(_rings(), 20.0, 0.0)
    return [_arc(ring, (32.55, 29.95), (32.30, 31.26), (20.0, -34.8))]


def rotated(pieces, rot):
    m = rotation_matrix(*rot)
    return [[to_latlon(apply(m, unit(lat, lon)))[::-1] for lon, lat in p] for p in pieces]


def rows(pieces):
    out = []
    for p in pieces:
        if out:
            out.append((NAN, NAN))
        out += [(round(lon, 3), round(lat, 3)) for lon, lat in p]
    return out


if __name__ == "__main__":
    sa = south_america()
    write_table(__file__, ("lon", "lat"), rows(sa), part="sa")
    write_table(__file__, ("lon", "lat"), rows(rotated(sa, ROT_120)), part="sa120")
    write_table(__file__, ("lon", "lat"), rows(rotated(sa, ROT_84)), part="sa84")
    write_table(__file__, ("lon", "lat"), rows(africa()), part="af")
    lat, lon, ang = ROT_120
    steps = [k for k in range(0, int(ang) + 1)] + [ang]
    track = [rotate_point((lat, lon, a), -8.05, -34.9)[::-1] for a in steps]
    write_table(__file__, ("lon", "lat"), track, part="track", digits=6)
    # a point of the Brazilian coast (Recife, about 8.05 S, 34.9 W) and where it goes
    r120 = rotate_point(ROT_120, -8.05, -34.9)
    r84 = rotate_point(ROT_84, -8.05, -34.9)
    vals = [("recife_120_lat", r120[0]), ("recife_120_lon", r120[1]),
            ("recife_84_lat", r84[0]), ("recife_84_lon", r84[1])]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

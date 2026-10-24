"""Curves on the local celestial sphere at latitude 45 deg N, projected exactly
as the style file's pic {celestialsphere} draws it (Year 1,
spherical-astronomy): a sphere of radius R = 2 cm seen from the WEST, from
17.5 deg above the horizon; north to the left. A point of altitude h and
azimuth A (from north through east) is drawn at
    X = -R cos h cos A,
    Y = R (0.9539 sin h + 0.3 cos h sin A),
and it is on the visible (western) half when sin A < 0. Coordinates in cm.

A star X of declination 25 deg at hour angle 50 deg (west of the meridian):
  part star        x y                      the star
  part vertical    x y vis                  zenith -> star -> horizon (azimuth fixed)
  part hourcircle  x y vis                  north celestial pole -> star -> equator
  part values      what value               h, A of the star (degrees)
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402
import _solar as S  # noqa: E402

R, CE, SE = 2.0, 0.9539, 0.3
LAT, DEC, HA = 45.0, 25.0, 50.0


def project(h, A):
    return (-R * math.cos(h) * math.cos(A),
            R * (CE * math.sin(h) + SE * math.cos(h) * math.sin(A)),
            1 if math.sin(A) <= 1e-9 else 0)


def star_hA(lat=LAT, dec=DEC, ha=HA):
    phi, d, H = map(math.radians, (lat, dec, ha))
    return S.altitude(phi, d, H), S.azimuth(phi, d, H)


def vertical_circle(n=40):
    h, A = star_hA()
    return [project(math.radians(90) * (1 - k / n), A) for k in range(n + 1)]


def local_from_equatorial(lat, dec, H):
    """Unit vector (north, east, up) of the point (dec, H) at latitude lat (radians)."""
    p = (math.cos(lat), 0.0, math.sin(lat))            # celestial pole
    m = (-math.sin(lat), 0.0, math.cos(lat))           # equator on the upper meridian
    w = (0.0, -1.0, 0.0)                               # west: H grows westward
    return tuple(math.sin(dec) * p[i] + math.cos(dec) * (math.cos(H) * m[i] + math.sin(H) * w[i])
                 for i in range(3))


def hour_circle(n=60):
    phi, H = math.radians(LAT), math.radians(HA)
    pts = []
    for k in range(n + 1):
        d = math.radians(90 - 90 * k / n)
        x, y, z = local_from_equatorial(phi, d, H)
        h = math.asin(max(-1, min(1, z)))
        A = math.atan2(y, x)
        pts.append(project(h, A))
    return pts


if __name__ == "__main__":
    h, A = star_hA()
    write_table(__file__, ("x", "y"), [project(h, A)[:2]], part="star", digits=5)
    write_table(__file__, ("x", "y", "vis"), vertical_circle(), part="vertical", digits=5)
    write_table(__file__, ("x", "y", "vis"), hour_circle(), part="hourcircle", digits=5)
    write_table(__file__, ("what", "value"),
                [("h_deg", math.degrees(h)), ("A_deg", math.degrees(A))], part="values", digits=5)

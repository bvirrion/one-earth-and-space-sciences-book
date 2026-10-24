"""An invented sea-level pressure map of the mid-latitudes, a depression and an
anticyclone, with the geostrophic wind at a grid of stations (Year 1,
atmospheric-circulation).

The map is a local plane 3600 km x 2400 km centred at 50 N (x east, y north, km). The
pressure is 1013 hPa minus a Gaussian low (28 hPa deep, radius 450 km) plus a Gaussian
high (+20 hPa, radius 650 km): exercise data, not a real day. The geostrophic wind is

    v_g = (1 / (rho f)) k x grad p,   f = 2 Omega sin(phi),

with Omega from the sidereal day (earth:Trot), f taken at the latitude of each station
(phi = 50 deg + y / 111.2 km), and rho = 1.225 kg/m3, the sea-level density of the 1976
standard atmosphere (ussa76:sea-level: 101325 Pa / (287.05 J/kg/K x 288.15 K)).

  part isobars   x y           (every 4 hPa, segments separated by nan rows)
  part labels    x y p         (one label point per isobar)
  part stations  x y speed_kn from_deg speed_ms   (geostrophic wind; direction the wind
                                                    blows FROM, azimuth)
  part values    what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

T_ROT = 23.9345 * 3600.0
OMEGA = 2 * math.pi / T_ROT
RHO = 101325.0 / (287.05 * 288.15)
KN = 0.514444                     # m/s per knot (1852 m per hour)
LOW = (-500.0, 150.0, 28.0, 450.0)
HIGH = (1050.0, -250.0, 20.0, 650.0)
X0, X1, Y0, Y1 = -1800.0, 1800.0, -1200.0, 1200.0


def pressure(x, y):
    """Sea-level pressure (hPa) at (x, y) in km."""
    (xl, yl, dl, rl), (xh, yh, dh, rh) = LOW, HIGH
    return (1013.0 - dl * math.exp(-((x - xl) ** 2 + (y - yl) ** 2) / (2 * rl ** 2))
            + dh * math.exp(-((x - xh) ** 2 + (y - yh) ** 2) / (2 * rh ** 2)))


def gradient(x, y, h=1.0):
    """(dp/dx, dp/dy) in Pa per metre."""
    gx = (pressure(x + h, y) - pressure(x - h, y)) / (2 * h) * 100.0 / 1000.0
    gy = (pressure(x, y + h) - pressure(x, y - h)) / (2 * h) * 100.0 / 1000.0
    return gx, gy


def latitude(y):
    return 50.0 + y / 111.2


def coriolis(lat):
    return 2 * OMEGA * math.sin(math.radians(lat))


def geostrophic(x, y):
    """(u, v) in m/s: v_g = (1/(rho f)) k x grad p = (-dp/dy, dp/dx) / (rho f)."""
    gx, gy = gradient(x, y)
    f = coriolis(latitude(y))
    return -gy / (RHO * f), gx / (RHO * f)


def from_azimuth(u, v):
    """Azimuth (deg from north, clockwise) the wind blows FROM."""
    return (math.degrees(math.atan2(-u, -v))) % 360.0


def contour_segments(level, nx=181, ny=121):
    xs = [X0 + (X1 - X0) * i / (nx - 1) for i in range(nx)]
    ys = [Y0 + (Y1 - Y0) * j / (ny - 1) for j in range(ny)]
    P = [[pressure(x, y) - level for x in xs] for y in ys]
    segs = []
    for j in range(ny - 1):
        for i in range(nx - 1):
            c = [(xs[i], ys[j], P[j][i]), (xs[i + 1], ys[j], P[j][i + 1]),
                 (xs[i + 1], ys[j + 1], P[j + 1][i + 1]), (xs[i], ys[j + 1], P[j + 1][i])]
            pts = []
            for k in range(4):
                (xa, ya, va), (xb, yb, vb) = c[k], c[(k + 1) % 4]
                if (va < 0) != (vb < 0):
                    t = va / (va - vb)
                    pts.append((xa + t * (xb - xa), ya + t * (yb - ya)))
            if len(pts) == 2:
                segs.append(pts)
            elif len(pts) == 4:
                segs += [[pts[0], pts[1]], [pts[2], pts[3]]]
    return segs


def levels():
    return [984.0 + 4 * k for k in range(0, 13)]


def stations(step=600.0):
    out = []
    x = X0 + step / 2
    while x < X1:
        y = Y0 + step / 2
        while y < Y1:
            u, v = geostrophic(x, y)
            s = math.hypot(u, v)
            out.append((x, y, s / KN, from_azimuth(u, v), s))
            y += step
        x += step
    return out


def values():
    v = [("rho", RHO), ("Omega", OMEGA), ("f50", coriolis(50.0)), ("p_low", pressure(*LOW[:2])),
         ("p_high", pressure(*HIGH[:2]))]
    # the strongest geostrophic wind on the map, and the wind half-way between the centres
    st = stations(50.0)
    best = max(st, key=lambda r: r[4])
    v += [("max_ms", best[4]), ("max_x", best[0]), ("max_y", best[1])]
    return v


if __name__ == "__main__":
    rows, labels = [], []
    for lev in levels():
        segs = contour_segments(lev)
        if not segs:
            continue
        for a, b in segs:
            rows += [a, b, (float("nan"), float("nan"))]
        # label at the northernmost point of the isobar that stays clear of the frame
        inner = [p for s in segs for p in s
                 if p[1] <= Y1 - 120.0 and X0 + 120.0 <= p[0] <= X1 - 120.0]
        if not inner:
            continue
        pt = max(inner, key=lambda p: p[1])
        labels.append((pt[0], pt[1], int(lev)))
    write_table(__file__, ("x", "y"), rows, part="isobars", digits=5)
    write_table(__file__, ("x", "y", "p"), labels, part="labels", digits=5)
    write_table(__file__, ("x", "y", "speed_kn", "from_deg", "speed_ms"), stations(), part="stations",
                digits=5)
    write_table(__file__, ("what", "value"), values(), part="values", digits=7)

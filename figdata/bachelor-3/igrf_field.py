"""The main geomagnetic field from IGRF-14 (Year 3, palaeomagnetism).

Data: data/derived/bachelor-3-igrf14.csv (ledger data:b5-igrf), Schmidt semi-
normalised Gauss coefficients g_n^m, h_n^m (nT), degree 1-10 to 1995, 1-13 from 2000.

Field on the sphere of reference radius a = 6371.2 km (geocentric latitude, the
spherical approximation of the Earth's surface), potential
    V = a sum_n (a/r)^(n+1) sum_m (g cos m phi + h sin m phi) P_n^m(cos theta),
B = -grad V; north X = -B_theta, east Y = B_phi, down Z = -B_r. Inclination
I = atan(Z / H), H = sqrt(X^2 + Y^2), total intensity F. Schmidt functions by
the standard recursion; their theta derivative by central differences.
Dipole: B0 = sqrt(g10^2 + g11^2 + h11^2), moment M = 4 pi a^3 B0 / mu0, north
geomagnetic pole at colatitude acos(-g10/B0), longitude atan2(-h11, -g11).

  part incl      lev x y          inclination contours every 20 deg (lev, lon, lat;
                                  lines separated by 'nan nan nan'), epoch 2025
  part intens    lev x y          total-intensity contours every 5000 nT, epoch 2025
  part dipole    year M plat plon dipole moment (1e22 A m2) and north geomagnetic
                                  pole (deg N, deg E), 1900-2025
  part dipeq     x y              the dip equator (I = 0)
  part inclab    lev x y          one label position per inclination level (lon 150 E)
  part intlab    lev x y          one label position per intensity level (lon -120 E)
  part fmin      x y              position of the lowest total intensity (2025)
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
from region import trace  # noqa: E402  (marching squares, read-only use)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
A_REF = 6371.2
MU0 = 4e-7 * math.pi


def read_coeffs(epoch="e2025"):
    g, h = {}, {}
    path = os.path.join(ROOT, "data", "derived", "bachelor-3-igrf14.csv")
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            n, m, v = int(r["n"]), int(r["m"]), float(r[epoch])
            (g if r["gh"] == "g" else h)[(n, m)] = v
    return g, h


def schmidt(nmax, theta):
    """P[n][m](cos theta), Schmidt semi-normalised, array (nmax+1, nmax+1, ...)."""
    c, s = np.cos(theta), np.sin(theta)
    p = np.zeros((nmax + 1, nmax + 1) + np.shape(theta))
    p[0, 0] = 1.0
    if nmax >= 1:
        p[1, 0], p[1, 1] = c, s
    for n in range(2, nmax + 1):
        for m in range(n):
            a = (2 * n - 1) * c * p[n - 1, m]
            b = math.sqrt((n - 1) ** 2 - m ** 2) * p[n - 2, m] if n - 2 >= m else 0.0
            p[n, m] = (a - b) / math.sqrt(n * n - m * m)
        p[n, n] = math.sqrt((2 * n - 1) / (2 * n)) * s * p[n - 1, n - 1]
    return p


def field(lat, lon, coeffs=None, r=A_REF):
    """X, Y, Z (nT) at geocentric latitude/longitude (deg, arrays allowed)."""
    g, h = coeffs or read_coeffs()
    nmax = max(n for n, m in g)
    th = np.radians(90.0 - np.asarray(lat, dtype=float))
    ph = np.radians(np.asarray(lon, dtype=float))
    eps = 1e-6
    p = schmidt(nmax, th)
    dp = (schmidt(nmax, th + eps) - schmidt(nmax, th - eps)) / (2 * eps)
    br = np.zeros(np.shape(th))
    bt = np.zeros(np.shape(th))
    bp = np.zeros(np.shape(th))
    for (n, m), gnm in g.items():
        hnm = h.get((n, m), 0.0)
        f = (A_REF / r) ** (n + 2)
        cm, sm = np.cos(m * ph), np.sin(m * ph)
        br = br + (n + 1) * f * (gnm * cm + hnm * sm) * p[n, m]
        bt = bt - f * (gnm * cm + hnm * sm) * dp[n, m]
        bp = bp + f * m * (gnm * sm - hnm * cm) * p[n, m] / np.sin(th)
    return -bt, bp, -br


def elements(x, y, z):
    hh = np.hypot(x, y)
    return np.degrees(np.arctan2(z, hh)), np.sqrt(x * x + y * y + z * z), hh, np.degrees(np.arctan2(y, x))


def dipole(g, h):
    b0 = math.sqrt(g[(1, 0)] ** 2 + g[(1, 1)] ** 2 + h[(1, 1)] ** 2)
    moment = 4 * math.pi * (A_REF * 1e3) ** 3 * b0 * 1e-9 / MU0
    colat = math.degrees(math.acos(-g[(1, 0)] / b0))
    lon = math.degrees(math.atan2(-h[(1, 1)], -g[(1, 1)]))
    return b0, moment, 90.0 - colat, lon


def contour_rows(fieldgrid, lons, lats, levels):
    rows = []
    for lev in levels:
        for line in trace(fieldgrid, lons, lats, lev):
            if len(line) < 3:
                continue
            rows += [(lev, x, y) for x, y in line] + [("nan", "nan", "nan")]
    return rows[:-1]


if __name__ == "__main__":
    lons = np.arange(-180.0, 180.01, 2.0)
    lats = np.arange(-89.0, 89.01, 2.0)
    LO, LA = np.meshgrid(lons, lats)
    x, y, z = field(LA, LO)
    inc, F, H, D = elements(x, y, z)
    write_table(__file__, ("lev", "x", "y"), contour_rows(inc, lons, lats, range(-80, 81, 20)), part="incl")
    write_table(__file__, ("lev", "x", "y"), contour_rows(F, lons, lats, range(25000, 65001, 5000)),
                part="intens")
    write_table(__file__, ("x", "y"), [r[1:] for r in contour_rows(inc, lons, lats, [0])], part="dipeq")
    def labels(rows_, lon0):
        out = []
        for lev in sorted({r[0] for r in rows_ if r[0] != "nan"}):
            pts = [(abs(r[1] - lon0) + 0.2 * abs(r[2]), r[1], r[2]) for r in rows_ if r[0] == lev]
            if pts:
                best = min(pts)
                out.append((lev, best[1], best[2]))
        return out
    write_table(__file__, ("lev", "x", "y"), labels(contour_rows(inc, lons, lats, range(-80, 81, 20)), 150.0),
                part="inclab")
    write_table(__file__, ("lev", "x", "y"),
                labels(contour_rows(F, lons, lats, range(25000, 65001, 5000)), -120.0), part="intlab")
    k = np.unravel_index(np.argmin(F), F.shape)
    write_table(__file__, ("x", "y"), [(float(LO[k]), float(LA[k]))], part="fmin")
    rows = []
    for yr in range(1900, 2026, 5):
        g, h = read_coeffs("e%d" % yr)
        b0, mom, plat, plon = dipole(g, h)
        rows.append((yr, mom / 1e22, plat, plon))
    write_table(__file__, ("year", "M", "plat", "plon"), rows, part="dipole")
    g, h = read_coeffs()
    b0, mom, plat, plon = dipole(g, h)
    vals = [("B0_2025_nT", b0), ("M_2025", mom / 1e22), ("pole_lat_2025", plat), ("pole_lon_2025", plon),
            ("M_1900", rows[0][1]), ("pole_lat_1900", rows[0][2]), ("pole_lon_1900", rows[0][3]),
            ("F_min", float(F.min())), ("F_max", float(F.max())), ("g10_2025", g[(1, 0)]),
            ("g11_2025", g[(1, 1)]), ("h11_2025", h[(1, 1)])]
    xs, ys, zs = field(np.array([47.0]), np.array([15.0]))
    i47, f47, h47, d47 = elements(xs, ys, zs)
    vals += [("kesta_I_2025", float(i47[0])), ("kesta_D_2025", float(d47[0])), ("kesta_F_2025", float(f47[0]))]
    write_table(__file__, ("what", "value"), vals, part="values")

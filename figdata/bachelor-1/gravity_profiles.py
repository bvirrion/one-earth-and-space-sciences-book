"""Free-air and Bouguer anomalies over a long mountain range (Year 1, isostasy-gravity),
uncompensated and Airy-compensated, from the exact attraction of two-dimensional
rectangular bodies.

Model (round values for the figure): a range 200 km wide and h = 2 km high, of
crustal density rho_c = 2700 kg/m3, on a normal crust 35 km thick over a mantle of
rho_m = 3300 kg/m3 (PREM's crust 2600-2900, uppermost mantle 3380; ledger data:prem).
Airy compensation gives a root r = h rho_c / (rho_m - rho_c) = 9 km.

Anomalous masses, relative to a flat normal crust with its surface at sea level:
the topography (+rho_c, from sea level up to h) and the root (rho_c - rho_m =
-600 kg/m3, from 35 to 35 + r km). Gravity is observed on the topographic surface;
after the free-air correction the free-air anomaly is the attraction of these
masses; the Bouguer anomaly subtracts the infinite slab 2 pi G rho_c e(x) of the
local elevation e (no terrain correction).

Attraction of a 2D body of density contrast drho occupying x1 < x < x2, z1 < z < z2
(z positive downwards from the observer): g = 2 G drho [F(a, z)] summed over corners,
F(a, z) = z arctan(a/z) + (a/2) ln(a^2 + z^2), a = x - x_obs.

  part profiles  x top fa_unc bg_unc fa_airy bg_airy   (x in km, anomalies in mGal,
                                                       top = elevation in km)
  part values    what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

G = 6.67430e-11      # const:G
RHO_C = 2700.0
RHO_M = 3300.0
H = 2000.0           # m
HALF_W = 100e3       # m
T_CRUST = 35e3       # m
MGAL = 1e-5          # m/s2


def airy_root(h=H, rho_c=RHO_C, rho_m=RHO_M):
    return h * rho_c / (rho_m - rho_c)


def _f(a, z):
    t1 = 0.0 if z == 0.0 else z * math.atan(a / z)
    t2 = 0.0 if a == 0.0 else 0.5 * a * math.log(a * a + z * z)
    return t1 + t2


def rect_gz(x0, z_obs, drho, x1, x2, top, bottom):
    """Vertical attraction (m/s2, positive downwards) at (x0, depth z_obs) of the
    body x1 < x < x2, top < depth < bottom (depths positive downwards, metres)."""
    z1, z2 = top - z_obs, bottom - z_obs
    parts = [(z1, z2)] if z1 >= 0.0 or z2 <= 0.0 else [(z1, 0.0), (0.0, z2)]
    a1, a2 = x1 - x0, x2 - x0
    s = 0.0
    for za, zb in parts:
        sign = 1.0
        if zb <= 0.0 and za < 0.0:
            # body above the observer: mirror, and the pull is upwards
            za, zb = -zb, -za
            sign = -1.0
        s += sign * (_f(a2, zb) - _f(a2, za) - _f(a1, zb) + _f(a1, za))
    return 2.0 * G * drho * s


def line_mass_gz(x0, z_obs, drho, x1, x2, top, bottom, nx=400, nz=40):
    """Same, by summing line masses (for the test)."""
    dx, dz = (x2 - x1) / nx, (bottom - top) / nz
    s = 0.0
    for i in range(nx):
        x = x1 + (i + 0.5) * dx - x0
        for j in range(nz):
            z = top + (j + 0.5) * dz - z_obs
            s += z / (x * x + z * z)
    return 2.0 * G * drho * dx * dz * s


def elevation(x, half_w=HALF_W, h=H):
    return h if abs(x) <= half_w else 0.0


def anomalies(x, compensated, half_w=HALF_W, h=H):
    """(free-air, Bouguer) anomalies in m/s2 at horizontal position x (m)."""
    e = elevation(x, half_w, h)
    z_obs = -e                       # observer's depth (negative: above sea level)
    fa = rect_gz(x, z_obs, RHO_C, -half_w, half_w, -h, 0.0)
    if compensated:
        r = airy_root(h)
        fa += rect_gz(x, z_obs, RHO_C - RHO_M, -half_w, half_w, T_CRUST, T_CRUST + r)
    bg = fa - 2.0 * math.pi * G * RHO_C * e
    return fa, bg


def bouguer_slab(rho, thickness):
    return 2.0 * math.pi * G * rho * thickness


if __name__ == "__main__":
    rows = []
    for i in range(-300, 301):
        x = i * 1e3
        if abs(abs(i) - 100) == 0:
            # sample both sides of the edge
            for xx in (x - math.copysign(1.0, x), x + math.copysign(1.0, x)):
                fu, bu = anomalies(xx, False)
                fc, bc = anomalies(xx, True)
                rows.append((xx / 1e3, elevation(xx) / 1e3, fu / MGAL, bu / MGAL, fc / MGAL, bc / MGAL))
            continue
        fu, bu = anomalies(x, False)
        fc, bc = anomalies(x, True)
        rows.append((x / 1e3, elevation(x) / 1e3, fu / MGAL, bu / MGAL, fc / MGAL, bc / MGAL))
    write_table(__file__, ("x", "top", "fa_unc", "bg_unc", "fa_airy", "bg_airy"), rows,
                part="profiles", digits=6)
    fu0, bu0 = anomalies(0.0, False)
    fc0, bc0 = anomalies(0.0, True)
    vals = [("root_km", airy_root() / 1e3),
            ("slab_2piGrho_h_mGal", bouguer_slab(RHO_C, H) / MGAL),
            ("centre_fa_unc", fu0 / MGAL), ("centre_bg_unc", bu0 / MGAL),
            ("centre_fa_airy", fc0 / MGAL), ("centre_bg_airy", bc0 / MGAL),
            ("bouguer_constant_mGal_per_m_per_1000", bouguer_slab(1000.0, 1.0) / MGAL)]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

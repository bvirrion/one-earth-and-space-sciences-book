"""Ice flow (Year 3, glaciology): Glen's law in a parallel-sided slab, the plastic
(Nye) ice-sheet profile against a measured Greenland transect, and the invented
Arkel ice cap of the problem.

Glen's law (ledger pism:rheology): strain rate = A tau^n, n = 3, with the
Paterson-Budd softness A(T) = A0 exp(-Q/RT) (A0 = 3.61e-13 Pa^-3 s^-1,
Q = 60 kJ/mol below -10 degC; 1.73e3 and 139 kJ/mol above). In a slab of
thickness H on a slope alpha, tau(z) = rho g (H - z) sin(alpha) (z up from the
bed) and

    u(z) = u_b + 2A/(n+1) (rho g sin alpha)^n [H^(n+1) - (H - z)^(n+1)],
    q    = u_b H + 2A/(n+2) (rho g sin alpha)^n H^(n+2).

A perfectly plastic ice sheet on a flat bed has rho g h dh/dx = tau0, so
h^2 = 2 tau0 (x - x_m)/(rho g) from a margin at x_m (Nye). The Greenland
transect (ETOPO1 Ice Surface along 72.5 N, data/derived/bachelor-3-etopo-
greenland.csv, ledger data:b5-etopo-greenland) is fitted on each side of the
divide by a straight line through h^2 against distance, for surface heights
above 1000 m, the bed being taken at sea level.

  part slab     zeta u3 u1 u3b     u/u_s against height above the bed z/H:
                                   n = 3; n = 1; n = 3 with half the surface speed by sliding
  part gl       x h               the transect (km from 58 W along 72.5 N, m)
  part nye-w    x h               the plastic profile fitted to the western side
  part nye-e    x h               the same for the eastern side
  part cap      r h               the Arkel ice cap (km, m)
  part values   what value
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

RHO_I = 917.0        # kg/m3 (iapws:ice-density 916.7)
G = 9.81
R_GAS = 8.314462618  # J/mol/K (codata:R)
N = 3
SEC_YR = 3.156e7
LAT = 72.5
KM_PER_DEG_LON = 111.32 * math.cos(math.radians(LAT))
# the Arkel ice cap (invented): circular, radius 20 km, plastic with tau0 = 100 kPa,
# ice at -10 degC
CAP_R = 20e3
CAP_TAU0 = 1.0e5
CAP_T = 263.15


def softness(t_k):
    """Paterson-Budd A(T) in Pa^-3 s^-1."""
    if t_k < 263.15:
        a0, q = 3.61e-13, 6.0e4
    else:
        a0, q = 1.73e3, 1.39e5
    return a0 * math.exp(-q / (R_GAS * t_k))


def slab_velocity(z, h, alpha, a, ub=0.0):
    """Velocity (m/s if a in Pa^-3 s^-1) at height z above the bed of a slab."""
    k = RHO_I * G * math.sin(alpha)
    return ub + 2 * a / (N + 1) * k ** N * (h ** (N + 1) - (h - z) ** (N + 1))


def slab_flux(h, alpha, a, ub=0.0):
    k = RHO_I * G * math.sin(alpha)
    return ub * h + 2 * a / (N + 2) * k ** N * h ** (N + 2)


def nye(dist, tau0):
    """Plastic surface height (m) at a distance dist (m) from the margin."""
    return math.sqrt(max(2 * tau0 * dist / (RHO_I * G), 0.0))


def cap_volume(r_cap=CAP_R, tau0=CAP_TAU0):
    """Volume of a circular plastic cap: 2 pi sqrt(2 tau0/rho g) (4/15) R^(5/2)."""
    return 2 * math.pi * math.sqrt(2 * tau0 / (RHO_I * G)) * 4.0 / 15.0 * r_cap ** 2.5


def transect():
    rows = []
    with open(os.path.join(ROOT, "data", "derived", "bachelor-3-etopo-greenland.csv"),
              encoding="utf8") as f:
        for r in csv.DictReader(f):
            rows.append(((float(r["lon"]) + 58.0) * KM_PER_DEG_LON, float(r["elev_m"])))
    return rows


def fit_side(rows, side):
    """Fit h^2 = s (x - x_m) on one side of the divide (h > 1000 m)."""
    i_top = max(range(len(rows)), key=lambda i: rows[i][1])
    pts = rows[:i_top + 1] if side == "w" else rows[i_top:]
    pts = [(x, h) for x, h in pts if h > 1000.0]
    xs = np.array([p[0] for p in pts]) * 1e3
    h2 = np.array([p[1] ** 2 for p in pts])
    s, c = np.polyfit(xs, h2, 1)
    xm = -c / s
    tau0 = abs(s) * RHO_I * G / 2
    rms = float(np.sqrt(np.mean((np.sqrt(np.clip(s * xs + c, 0, None)) - np.sqrt(h2)) ** 2)))
    return tau0, xm / 1e3, rows[i_top], rms, len(pts)


def main():
    a10 = softness(263.15 - 1e-9)
    zs = np.linspace(0.0, 1.0, 101)
    alpha = 0.01
    us3 = slab_velocity(1.0, 1.0, alpha, 1.0)
    rows = []
    for z in zs:
        u3 = slab_velocity(z, 1.0, alpha, 1.0) / us3
        u1 = 1 - (1 - z) ** 2          # n = 1, normalised
        u3b = 0.5 + 0.5 * u3
        rows.append((z, u3, u1, u3b))
    write_table(__file__, ("zeta", "u3", "u1", "u3b"), rows, part="slab")

    gl = transect()
    write_table(__file__, ("x", "h"), gl, part="gl")
    tw, xmw, top, rmsw, nw = fit_side(gl, "w")
    te, xme, _, rmse, ne = fit_side(gl, "e")
    xtop = top[0]
    nyew = [(x, nye((x - xmw) * 1e3, tw)) for x in np.linspace(xmw, xtop, 200)]
    nyee = [(x, nye((xme - x) * 1e3, te)) for x in np.linspace(xtop, xme, 200)]
    write_table(__file__, ("x", "h"), nyew, part="nye-w")
    write_table(__file__, ("x", "h"), nyee, part="nye-e")

    cap =[(r / 1e3, nye(CAP_R - abs(r), CAP_TAU0)) for r in np.linspace(-CAP_R, CAP_R, 401)]
    write_table(__file__, ("r", "h"), cap, part="cap")

    vol = cap_volume()
    mass_gt = vol * RHO_I / 1e12
    h10 = nye(CAP_R - 10e3, CAP_TAU0)
    slope10 = h10 / (2 * (CAP_R - 10e3))
    a_cap = softness(CAP_T - 1e-9)
    us10 = slab_velocity(h10, h10, math.atan(slope10), a_cap) * SEC_YR
    q10 = slab_flux(h10, math.atan(slope10), a_cap) * SEC_YR
    vals = [["A_minus10_Pa3_s", a10], ["A_minus10_Pa3_yr", a10 * SEC_YR],
            ["A_0C_Pa3_yr", softness(273.15) * SEC_YR],
            ["gl_top_x_km", xtop], ["gl_top_h", top[1]],
            ["tau0_west_kPa", tw / 1e3], ["margin_west_km", xmw], ["rms_west_m", rmsw], ["n_west", nw],
            ["tau0_east_kPa", te / 1e3], ["margin_east_km", xme], ["rms_east_m", rmse], ["n_east", ne],
            ["cap_hmax", nye(CAP_R, CAP_TAU0)], ["cap_volume_km3", vol / 1e9],
            ["cap_mass_Gt", mass_gt], ["cap_sle_mm", mass_gt / 360.0],
            ["cap_mean_thickness", vol / (math.pi * CAP_R ** 2)],
            ["cap_h_10km", h10], ["cap_slope_10km", slope10],
            ["cap_us_10km_m_yr", us10], ["cap_q_10km_m2_yr", q10],
            ["cap_b_needed_m_yr", 2 * q10 / 10e3]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

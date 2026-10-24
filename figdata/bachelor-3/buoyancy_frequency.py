"""Buoyancy frequency of the atmosphere and of the ocean (Year 3, geophysical
fluid dynamics).

Atmosphere: the NASA Glenn standard-atmosphere model (nasa:grc-atmos),
T = 15.04 - 0.00649 h deg C to 11 km, -56.46 deg C from 11 to 25 km,
-131.21 + 0.00299 h above; N^2 = (g/T)(dT/dz + g/c_p), with c_p = gamma R /
(gamma - 1) from gamma = 1.4 (nasa:grc-gamma) and R = 286.9 J/(kg K).

Ocean: WOA23 annual temperature and salinity of the North Atlantic column at
40.5 N 30.5 W (shared derived tables grade-10-woa23-atlantic-{t,s}.csv,
ledger data:b2-woa23); potential temperature by UNESCO 44's THETA, density by
the one-atmosphere EOS-80 polynomial (ledger unesco44:eos80-b5), potential
density referred to the surface, N^2 = -(g/rho) d(sigma_theta)/dz on the
midpoints of the standard levels. Referring to the surface is adequate in
the upper two kilometres shown; deeper, a local reference would be needed.

Rossby radius NH/f: the troposphere with its mean N and H = 11 km at 45 N;
the upper ocean with the mean N of 0-1000 m and H = 1000 m at 40.5 N.

  part atm     z N              z in km, N in 1/s, 0-30 km
  part ocean   z N cph          z in m (positive down), N in 1/s and cycles per hour
  part values  what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
DERIVED = os.path.join(ROOT, "data", "derived")
STEM = "grade-10-woa23-atlantic"
LAT_OCEAN = 40.5
G = 9.81
R_AIR = 286.9
GAMMA = 1.4
CP = GAMMA * R_AIR / (GAMMA - 1)
OMEGA = 7.292115e-5
T68 = 1.00024
Z_OCEAN_MAX = 2000.0


# ------------------------------------------------------------------ atmosphere
def t_atm(h):
    """Standard-atmosphere temperature (K) at height h (m)."""
    if h <= 11000:
        tc = 15.04 - 0.00649 * h
    elif h <= 25000:
        tc = -56.46
    else:
        tc = -131.21 + 0.00299 * h
    return tc + 273.1


def n2_atm(h, dh=1.0):
    dtdz = (t_atm(h + dh) - t_atm(h - dh)) / (2 * dh)
    return G / t_atm(h) * (dtdz + G / CP)


# ------------------------------------------------------------------ ocean (UNESCO 44)
def rho0(s, t):
    """EOS-80 one-atmosphere density (kg/m3), t in deg C (IPTS-68)."""
    rw = ((((6.536332e-9 * t - 1.120083e-6) * t + 1.001685e-4) * t - 9.095290e-3) * t
          + 6.793952e-2) * t + 999.842594
    a = (((5.3875e-9 * t - 8.2467e-7) * t + 7.6438e-5) * t - 4.0899e-3) * t + 8.24493e-1
    b = (-1.6546e-6 * t + 1.0227e-4) * t - 5.72466e-3
    return rw + (a + b * math.sqrt(s) + 4.8314e-4 * s) * s


def atg(s, t, p):
    """Adiabatic lapse rate (deg C per dbar), Bryden (1973), as in UNESCO 44."""
    ds = s - 35.0
    return ((((-2.1687e-16 * t + 1.8676e-14) * t - 4.6206e-13) * p
             + ((2.7759e-12 * t - 1.1351e-10) * ds + ((-5.4481e-14 * t + 8.733e-12) * t
                                                       - 6.7795e-10) * t + 1.8741e-8)) * p
            + (-4.2393e-8 * t + 1.8932e-6) * ds
            + ((6.6228e-10 * t - 6.836e-8) * t + 8.5258e-6) * t + 3.5803e-5)


def theta(s, t0, p0, pr=0.0):
    """Potential temperature (UNESCO 44 THETA, fourth-order Runge-Kutta)."""
    p, t = p0, t0
    h = pr - p
    xk = h * atg(s, t, p)
    t = t + 0.5 * xk
    q = xk
    p = p + 0.5 * h
    xk = h * atg(s, t, p)
    t = t + 0.29289322 * (xk - q)
    q = 0.58578644 * xk + 0.121320344 * q
    xk = h * atg(s, t, p)
    t = t + 1.707106781 * (xk - q)
    q = 3.414213562 * xk - 4.121320344 * q
    p = p + 0.5 * h
    xk = h * atg(s, t, p)
    return t + (xk - 2.0 * q) / 6.0


def _column(var):
    with open(os.path.join(DERIVED, "%s-%s.csv" % (STEM, var)), encoding="utf8") as f:
        return {float(r["depth_m"]): float(r["value"]) for r in csv.DictReader(f)}


def ocean_profile():
    """[(depth m, sigma_theta)] with pressure taken as depth in dbar (the
    difference, under 1 % in the upper two kilometres, does not matter for
    theta)."""
    t, s = _column("t"), _column("s")
    out = []
    for z in sorted(t):
        if z in s and z <= Z_OCEAN_MAX:
            th = theta(s[z], T68 * t[z], z)
            out.append((z, rho0(s[z], th) - 1000.0))
    return out


def ocean_n2():
    prof = ocean_profile()
    out = []
    for (z1, s1), (z2, s2) in zip(prof, prof[1:]):
        n2 = G / (1000.0 + 0.5 * (s1 + s2)) * (s2 - s1) / (z2 - z1)
        out.append((0.5 * (z1 + z2), n2))
    return out


def coriolis(lat):
    return 2 * OMEGA * math.sin(math.radians(lat))


def mean_n(rows, zmax):
    """Depth-weighted mean N over 0-zmax from (z, N2) rows at midpoints."""
    num = den = 0.0
    prev = 0.0
    for z, n2 in rows:
        if z > zmax:
            break
        w = z - prev
        num += math.sqrt(max(n2, 0.0)) * w
        den += w
        prev = z
    return num / den


def main():
    atm = [(h / 1000, math.sqrt(n2_atm(h))) for h in range(250, 30001, 250)
           if h not in (11000, 25000)]
    write_table(__file__, ("z", "N"), atm, part="atm")
    oc = ocean_n2()
    write_table(__file__, ("z", "N", "cph"),
                [[z, math.sqrt(max(n2, 0.0)), math.sqrt(max(n2, 0.0)) * 3600 / (2 * math.pi)]
                 for z, n2 in oc], part="ocean")
    n_trop = sum(math.sqrt(n2_atm(h)) for h in range(500, 11000, 500)) / len(range(500, 11000, 500))
    n_strat = math.sqrt(n2_atm(18000))
    n_oc = mean_n(oc, 1000.0)
    lr_atm = n_trop * 11000 / coriolis(45.0)
    lr_oc = n_oc * 1000 / coriolis(LAT_OCEAN)
    nmax = max(oc, key=lambda r: r[1])
    write_table(__file__, ("what", "value"),
                [["cp", CP], ["dalr_K_per_km", G / CP * 1000], ["N_trop_mean", n_trop],
                 ["N_strat", n_strat], ["period_trop_min", 2 * math.pi / n_trop / 60],
                 ["N_ocean_0_1000", n_oc], ["Nmax_depth", nmax[0]], ["Nmax", math.sqrt(nmax[1])],
                 ["Nmax_cph", math.sqrt(nmax[1]) * 3600 / (2 * math.pi)],
                 ["LR_atm_km", lr_atm / 1000], ["LR_ocean_km", lr_oc / 1000]],
                part="values")


if __name__ == "__main__":
    main()

"""Convection scaling: Nusselt number and velocity scale against the Rayleigh
number, and the Rayleigh number of the mantle (Year 3, mantle convection).

Rayleigh number   Ra = rho g alpha dT d^3 / (kappa eta)
Critical value    Ra_c = 27 pi^4 / 4 (free-slip top and bottom; a mathematical
                  result: min over k of (pi^2 + k^2)^3 / k^2, at k = pi/sqrt 2)
Boundary layers   each boundary layer, across which the temperature drops by
                  dT/2, grows until its own Rayleigh number reaches Ra_c:
                  delta = d (2 Ra_c / Ra)^(1/3),  Nu = d / (2 delta),
                  u = kappa d / delta^2 = (kappa/d) (Ra / (2 Ra_c))^(2/3)

Mantle values: depth to the core 2891 km, mean density of the mantle and
gravity from PREM (data/derived/prem.csv, ledger data:prem, read only);
alpha = 3.1e-5 /K and dT = 1450 K (the plate model of ledger honda04:gdh1);
kappa = 1e-6 m2/s (ledger delaney86:properties, upper bound); viscosity
1e21 to 1e22 Pa s (ledgers mitrovica96:haskell, milne04:bifrost); k = 3.1
W/m/K. Plate speeds 10.6 to 74.6 mm/yr rms (ledger nnr56:rms).

  part conduction  ra nu u         Nu = 1 below Ra_c (u blank: no flow)
  part scaling     ra nu u         the boundary-layer law, 16 Ra_c (Nu = 1) to 1e10, u in cm/yr
                                   for d = 2891 km, kappa = 1e-6
  part band        ra y            the mantle's Ra range: two vertical lines, nan-separated
  part plates      ra u            slowest and fastest rms plate speeds (cm/yr), nan-separated
  part values      what value
"""
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
RAC = 27 * math.pi ** 4 / 4
G_NEWTON = 6.674e-11
R_EARTH = 6371e3
D_MANTLE = 2891e3
ALPHA = 3.1e-5
DT = 1450.0
KAPPA = 1e-6
K = 3.1
YR = 3.15576e7
ETAS = (1e21, 1e22)
PLATE_SLOW, PLATE_FAST = 1.06, 7.46   # cm/yr, South America and Cocos (nnr56:rms)


def critical_function(k):
    """Ra at marginal stability for horizontal wavenumber k (free-slip, d = 1)."""
    return (math.pi ** 2 + k * k) ** 3 / (k * k)


def rayleigh(rho, g, alpha, dt, d, kappa, eta):
    return rho * g * alpha * dt * d ** 3 / (kappa * eta)


def delta(ra, d=D_MANTLE):
    return d * (2 * RAC / np.asarray(ra, dtype=float)) ** (1 / 3)


def nusselt(ra):
    return 0.5 * (np.asarray(ra, dtype=float) / (2 * RAC)) ** (1 / 3)


def velocity(ra, d=D_MANTLE, kappa=KAPPA):
    """Velocity scale (m/s)."""
    return kappa / d * (np.asarray(ra, dtype=float) / (2 * RAC)) ** (2 / 3)


def read_prem():
    rows = []
    with open(os.path.join(ROOT, "data", "derived", "prem.csv"), newline="") as f:
        for r in csv.DictReader(f):
            rows.append((float(r["depth_km"]) * 1e3, float(r["rho_g_cm3"]) * 1e3,
                         float(r["vs_km_s"]) * 1e3, r["region"]))
    return rows


def prem_mass_profile():
    """Radius (m, increasing) and enclosed mass (kg), trapezoids in radius on the
    PREM layers (density linear between tabulated points)."""
    rows = read_prem()
    pts = sorted(((R_EARTH - z, rho) for z, rho, _, _ in rows), key=lambda p: (p[0], -p[1]))
    radii, masses = [0.0], [0.0]
    m = 0.0
    for (r1, rho1), (r2, rho2) in zip(pts[:-1], pts[1:]):
        if r2 <= r1:
            continue
        rr = np.linspace(r1, r2, 41)
        rho = rho1 + (rho2 - rho1) * (rr - r1) / (r2 - r1)
        m += np.trapezoid(4 * math.pi * rr * rr * rho, rr)
        radii.append(r2)
        masses.append(m)
    return np.array(radii), np.array(masses)


def gravity(depth):
    r, m = prem_mass_profile()
    rad = R_EARTH - depth
    return G_NEWTON * float(np.interp(rad, r, m)) / rad ** 2


def mantle_mean_density():
    r, m = prem_mass_profile()
    rc = R_EARTH - D_MANTLE
    rm = R_EARTH - 24.4e3
    mass = float(np.interp(rm, r, m) - np.interp(rc, r, m))
    return mass / (4 / 3 * math.pi * (rm ** 3 - rc ** 3))


def shear_modulus(depth):
    """mu = rho vs^2 from PREM at the first tabulated point at or below depth."""
    for z, rho, vs, region in read_prem():
        if z >= depth and region == "mantle":
            return rho * vs * vs
    raise ValueError(depth)


def mantle_rayleigh(eta, g=10.0):
    return rayleigh(mantle_mean_density(), g, ALPHA, DT, D_MANTLE, KAPPA, eta)


if __name__ == "__main__":
    write_table(__file__, ("ra", "nu"), [(10 ** e, 1.0) for e in np.linspace(2, math.log10(RAC), 12)],
                part="conduction")
    ras = np.logspace(math.log10(16 * RAC), 10, 60)   # from Nu = 1: the law holds far above Ra_c
    write_table(__file__, ("ra", "nu", "u"),
                [(ra, float(nusselt(ra)), float(velocity(ra)) * YR * 100) for ra in ras], part="scaling")
    lo, hi = mantle_rayleigh(ETAS[1]), mantle_rayleigh(ETAS[0])
    nan = float("nan")
    write_table(__file__, ("ra", "y"), [(lo, 1e-4), (lo, 1e4), (nan, nan), (hi, 1e-4), (hi, 1e4)], part="band")
    write_table(__file__, ("ra", "u"), [(1e2, PLATE_SLOW), (1e10, PLATE_SLOW), (nan, nan),
                                         (1e2, PLATE_FAST), (1e10, PLATE_FAST)], part="plates")
    vals = [
        ("Ra_c", RAC),
        ("mantle_mean_density", mantle_mean_density()),
        ("g_surface", gravity(0.0)),
        ("g_670", gravity(670e3)),
        ("g_cmb", gravity(D_MANTLE - 1.0)),
        ("Ra_eta1e21", hi),
        ("Ra_eta1e22", lo),
        ("Nu_eta1e21", float(nusselt(hi))),
        ("Nu_eta1e22", float(nusselt(lo))),
        ("u_cmyr_eta1e21", float(velocity(hi)) * YR * 100),
        ("u_cmyr_eta1e22", float(velocity(lo)) * YR * 100),
        ("delta_km_eta1e21", float(delta(hi)) / 1e3),
        ("q_mWm2_eta1e21", float(nusselt(hi)) * K * DT / D_MANTLE * 1e3),
        ("mu_300km", shear_modulus(300e3)),
        ("mu_1000km", shear_modulus(1000e3)),
    ]
    write_table(__file__, ("what", "value"), vals, part="values")

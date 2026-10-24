"""Cooling of the oceanic lithosphere: half-space and plate models against the
depth of the sea floor (Year 3, thermal models of the lithosphere).

Model parameters (the chapter's): surface 0 C, mantle Tm = 1450 C, plate
thickness L = 95 km, alpha = 3.1e-5 /K, conductivity k = 3.1 W/m/K (the plate
model of Stein and Stein 1992 as summarised by Honda and Yuen 2004, ledger
honda04:gdh1), diffusivity kappa = 0.8e-6 m2/s (within the range of ledger
delaney86:properties), mantle 3300 and sea water 1030 kg/m3, ridge depth
2500 m (ledger ps77:depth-age).

  half-space:  T = Tm erf(z / 2 sqrt(kappa t)),  q = k Tm / sqrt(pi kappa t),
               d = dr + 2 rho_m alpha Tm sqrt(kappa t / pi) / (rho_m - rho_w)
  plate:       T = Tm [ z/L + (2/pi) sum 1/n sin(n pi z/L) exp(-n^2 t/tau) ],
               tau = L^2 / (pi^2 kappa),
               q = (k Tm / L) [ 1 + 2 sum exp(-n^2 t/tau) ],
               d = dr + rho_m alpha Tm L / (2 (rho_m - rho_w))
                        [ 1 - (8/pi^2) sum_{n odd} exp(-n^2 t/tau) / n^2 ]

Data: one-degree cells where the sea floor has an age (Seton et al. 2020 grid,
data/derived/grade-11-seafloor-age.csv, ledger data:b2-seafloor-age, read
only) and ETOPO1 depth below 1000 m (data/derived/etopo-1deg.csv, ledger
data:etopo1); medians and quartiles of depth in 5-Myr age bins to 180 Myr,
with no correction for sediment, seamounts or swells.

  part isotherms t hs200..hs1400 pl200..pl1400   depth (km) of the 200-1400 C isotherms
                                against age (Myr), half-space and plate
  part depth     t hs pl pl1    depth (m) vs age: half-space, plate (100 terms),
                                plate with the first Fourier term only
  part heat      t hs pl        heat flow (mW/m2) vs age
  part bins      t med q1 q3 n  binned observed depths (m)
  part values    what value
"""
import csv
import math
import os
import sys

import numpy as np
from scipy.special import erfinv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
MYR = 3.15576e13
TM = 1450.0
L = 95e3
ALPHA = 3.1e-5
K = 3.1
KAPPA = 0.8e-6
RHO_M, RHO_W = 3300.0, 1030.0
DR = 2500.0


def erf(x):
    return np.vectorize(math.erf)(x)


def hs_temperature(z, t_myr, tm=TM, kappa=KAPPA):
    return tm * erf(np.asarray(z) / (2 * np.sqrt(kappa * t_myr * MYR)))


def hs_heat(t_myr, tm=TM, k=K, kappa=KAPPA):
    return k * tm / np.sqrt(np.pi * kappa * np.asarray(t_myr) * MYR)


def hs_depth(t_myr, tm=TM, kappa=KAPPA, alpha=ALPHA):
    return DR + 2 * RHO_M * alpha * tm / (RHO_M - RHO_W) * np.sqrt(kappa * np.asarray(t_myr) * MYR / np.pi)


def tau(l=L, kappa=KAPPA):
    return l * l / (np.pi ** 2 * kappa) / MYR


def plate_temperature(z, t_myr, l=L, tm=TM, kappa=KAPPA, nterms=100):
    z = np.asarray(z, dtype=float)
    s = z / l
    tt = tau(l, kappa)
    for n in range(1, nterms + 1):
        s = s + 2 / (np.pi * n) * np.sin(n * np.pi * z / l) * np.exp(-n * n * t_myr / tt)
    return tm * s


def plate_heat(t_myr, l=L, tm=TM, k=K, kappa=KAPPA, nterms=100):
    t = np.asarray(t_myr, dtype=float)
    tt = tau(l, kappa)
    s = 1.0 + 2 * sum(np.exp(-n * n * t / tt) for n in range(1, nterms + 1))
    return k * tm / l * s


def plate_depth(t_myr, l=L, tm=TM, kappa=KAPPA, alpha=ALPHA, nterms=100):
    t = np.asarray(t_myr, dtype=float)
    tt = tau(l, kappa)
    s = sum(np.exp(-n * n * t / tt) / n ** 2 for n in range(1, 2 * nterms, 2))
    return DR + RHO_M * alpha * tm * l / (2 * (RHO_M - RHO_W)) * (1 - 8 / np.pi ** 2 * s)


def plate_isotherm_depth(temp, t_myr, l=L):
    """Depth (m) of an isotherm in the plate model, by bisection (T rises with depth)."""
    lo, hi = 0.0, l
    for _ in range(80):
        mid = (lo + hi) / 2
        if float(plate_temperature(mid, t_myr, l)) < temp:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def read_bins(width=5.0, tmax=180.0):
    ages = {}
    with open(os.path.join(ROOT, "data", "derived", "grade-11-seafloor-age.csv"), newline="") as f:
        for r in csv.DictReader(f):
            ages[(float(r["lat"]), float(r["lon"]))] = float(r["age"])
    pairs = []
    with open(os.path.join(ROOT, "data", "derived", "etopo-1deg.csv"), newline="") as f:
        for r in csv.DictReader(f):
            key = (float(r["lat"]), float(r["lon"]))
            if key in ages and float(r["elev_m"]) < -1000.0:
                pairs.append((ages[key], -float(r["elev_m"])))
    pairs = np.array(pairs)
    rows = []
    for a in np.arange(0.0, tmax, width):
        sel = pairs[(pairs[:, 0] >= a) & (pairs[:, 0] < a + width), 1]
        if len(sel) >= 20:
            q1, med, q3 = np.percentile(sel, [25, 50, 75])
            rows.append((a + width / 2, med, q1, q3, len(sel)))
    return rows


if __name__ == "__main__":
    ts = np.concatenate([[0.05, 0.2, 0.5], np.arange(1.0, 180.01, 1.0)])
    levels = (200, 400, 600, 800, 1000, 1200, 1400)
    rows = []
    for t in np.concatenate([[0.1, 0.5], np.arange(1.0, 160.01, 1.0)]):
        row = [t]
        for lev in levels:
            row.append(2 * math.sqrt(KAPPA * t * MYR) * float(erfinv(lev / TM)) / 1e3)
        for lev in levels:
            row.append(plate_isotherm_depth(lev, t) / 1e3)
        rows.append(tuple(row))
    write_table(__file__, ("t",) + tuple("hs%d" % v for v in levels) + tuple("pl%d" % v for v in levels),
                rows, part="isotherms")
    write_table(__file__, ("t", "hs", "pl", "pl1"),
                [(t, hs_depth(t), plate_depth(t), plate_depth(t, nterms=1)) for t in ts], part="depth")
    write_table(__file__, ("t", "hs", "pl"),
                [(t, 1e3 * hs_heat(t), 1e3 * plate_heat(t)) for t in ts if t >= 1.0], part="heat")
    bins = read_bins()
    write_table(__file__, ("t", "med", "q1", "q3", "n"), bins, part="bins")
    sub = 2 * RHO_M * ALPHA * TM / (RHO_M - RHO_W) * math.sqrt(KAPPA * MYR / math.pi)
    vals = [("tau_Myr", tau()), ("hs_subsidence_m_per_sqrtMyr", sub),
            ("hs_heat_C_mW", 1e3 * K * TM / math.sqrt(math.pi * KAPPA * MYR)),
            ("plate_asymptote_m", DR + RHO_M * ALPHA * TM * L / (2 * (RHO_M - RHO_W))),
            ("plate_q_inf_mW", 1e3 * K * TM / L)]
    tgrid = np.arange(0.5, 180.0, 0.01)
    diff = hs_depth(tgrid) - plate_depth(tgrid)
    vals.append(("age_diff_100m", float(tgrid[np.argmax(diff >= 100.0)])))
    for b in bins:
        vals.append(("bin_%g" % b[0], b[1]))
    write_table(__file__, ("what", "value"), vals, part="values")

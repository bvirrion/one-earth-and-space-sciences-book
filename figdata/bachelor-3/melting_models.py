"""Trace-element melting models (Year 3, trace-element modelling).

Melt C_L and residue C_S relative to the source C_0, melt fraction F, bulk
partition coefficient D (constant, modal melting):

    batch                    C_L/C_0 = 1 / (D + F (1 - D))
    fractional, instant      C_L/C_0 = (1/D) (1 - F)^(1/D - 1)
    fractional, aggregated   C_L/C_0 = (1 - (1 - F)^(1/D)) / F
    non-modal batch          C_L/C_0 = 1 / (D0 + F (1 - P))
    dynamic (porosity phi)   fractional with D' = (1 - phi) D + phi

Partition coefficients: ledger budahn91:d-ree (cpx / garnet / olivine +
orthopyroxene + spinel lumped). Modes: spinel lherzolite white13:ex73
(58 ol, 27 opx, 12 cpx, 3 sp), garnet lherzolite rfr25:gkr-5gpa (54.1 ol,
9.8 opx, 19.5 cpx, 16.7 gt, as printed). Source: primitive mantle
ms95:pm-trace; normalisation: CI chondrite lodders:ci-table.

The two lavas A and B of the weekend problem are invented.

  part curves   f + batch/inst/agg for D = 0.01, 0.1, 1, 10   (C_L/C_0)
  part ree      z name sp01 sp05 sp20 gt01 gt05 gt20 pm      (chondrite-normalised)
  part traj     f la_sp lay_sp la_gt lay_gt                    (ppm; La/Yb)
  part ticks    f la_sp lay_sp la_gt lay_gt                    (F = 1, 2, 5, 10, 20 %)
  part lavas    name la layb
  part values   what value
"""
import math
import os
import sys

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

# budahn91:d-ree: cpx, garnet, olivine+opx+spinel
KD = {
    "La": (0.058, 0.001, 0.001),
    "Ce": (0.10, 0.0065, 0.0025),
    "Nd": (0.24, 0.035, 0.0075),
    "Sm": (0.40, 0.11, 0.016),
    "Eu": (0.48, 0.15, 0.022),
    "Gd": (0.52, 0.24, 0.030),
    "Tb": (0.59, 0.56, 0.057),
    "Yb": (0.58, 4.5, 0.16),
    "Lu": (0.53, 5.8, 0.18),
}
Z = {"La": 57, "Ce": 58, "Nd": 60, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Yb": 70, "Lu": 71}
# ms95:pm-trace (ppm) and lodders:ci-table (ppm)
PM = {"La": 0.648, "Ce": 1.675, "Nd": 1.25, "Sm": 0.406, "Eu": 0.154, "Gd": 0.544,
      "Tb": 0.099, "Yb": 0.441, "Lu": 0.0675}
CI = {"La": 0.232, "Ce": 0.621, "Nd": 0.457, "Sm": 0.145, "Eu": 0.0546, "Gd": 0.198,
      "Tb": 0.0356, "Yb": 0.163, "Lu": 0.0237}
# modes as mass fractions (cpx, garnet, ol+opx+sp)
MODE_SP = (0.12, 0.0, 0.58 + 0.27 + 0.03)
MODE_GT = (0.195, 0.167, 0.541 + 0.098)

# white13:ex73, for the non-modal exercise: ol, opx, cpx, sp
EX73_MODE = (0.58, 0.27, 0.12, 0.03)
EX73_MELT = (0.20, 0.25, 0.45, 0.10)
EX73_KD = {"La": (0.0003, 0.002, 0.053, 0.01), "Sm": (0.0013, 0.011, 0.36, 0.01)}

LAVA_A = (9.6, 1.7)    # La, Yb ppm (invented)
LAVA_B = (15.6, 0.45)


def bulk_d(element, mode):
    return sum(m * d for m, d in zip(mode, KD[element]))


def batch(f, d):
    return 1.0 / (d + f * (1.0 - d))


def batch_residue(f, d):
    return d * batch(f, d)


def fractional_instant(f, d):
    return (1.0 / d) * (1.0 - f) ** (1.0 / d - 1.0)


def fractional_residue(f, d):
    return (1.0 - f) ** (1.0 / d - 1.0)


def fractional_aggregate(f, d):
    if f == 0:
        return 1.0 / d
    return (1.0 - (1.0 - f) ** (1.0 / d)) / f


def nonmodal_batch(f, d0, p):
    return 1.0 / (d0 + f * (1.0 - p))


def nonmodal_residue_d(f, d0, p):
    return (d0 - p * f) / (1.0 - f)


def dynamic_effective_d(d, phi):
    return (1.0 - phi) * d + phi


def dynamic_instant(f, d, phi):
    return fractional_instant(f, dynamic_effective_d(d, phi))


def f_batch(c_ratio, d):
    """Melt fraction giving C_L/C_0 = c_ratio in batch melting."""
    return (1.0 / c_ratio - d) / (1.0 - d)


def f_aggregate(c_ratio, d):
    return brentq(lambda f: fractional_aggregate(f, d) - c_ratio, 1e-9, 1.0 - 1e-12)


def ratio_line(d_m, c0_h, c0_m):
    """Batch melting with D_H = 0: C_H/C_M = slope C_H + intercept."""
    return d_m / c0_m, c0_h * (1.0 - d_m) / c0_m


def ex73():
    d0 = {e: sum(m * k for m, k in zip(EX73_MODE, EX73_KD[e])) for e in EX73_KD}
    p = {e: sum(m * k for m, k in zip(EX73_MELT, EX73_KD[e])) for e in EX73_KD}
    return d0, p


def main():
    fs = np.concatenate([np.linspace(0.0, 0.02, 41)[1:], np.linspace(0.02, 0.3, 57)[1:]])
    ds = (0.01, 0.1, 1.0, 10.0)
    rows = []
    for f in fs:
        row = [f]
        for d in ds:
            row += [batch(f, d), fractional_instant(f, d), fractional_aggregate(f, d)]
        rows.append(row)
    header = ["f"]
    for tag in ("001", "01", "1", "10"):
        header += ["b" + tag, "i" + tag, "a" + tag]
    write_table(__file__, header, rows, part="curves")

    rows = []
    for el in KD:
        dsp, dgt = bulk_d(el, MODE_SP), bulk_d(el, MODE_GT)
        row = [Z[el], el]
        for d in (dsp,):
            row += [PM[el] * batch(f, d) / CI[el] for f in (0.01, 0.05, 0.20)]
        row += [PM[el] * batch(f, dgt) / CI[el] for f in (0.01, 0.05, 0.20)]
        row += [PM[el] / CI[el]]
        rows.append(row)
    write_table(__file__, ("z", "name", "sp01", "sp05", "sp20", "gt01", "gt05", "gt20", "pm"),
                rows, part="ree")

    dla_sp, dyb_sp = bulk_d("La", MODE_SP), bulk_d("Yb", MODE_SP)
    dla_gt, dyb_gt = bulk_d("La", MODE_GT), bulk_d("Yb", MODE_GT)

    def traj(f):
        la_sp, yb_sp = PM["La"] * batch(f, dla_sp), PM["Yb"] * batch(f, dyb_sp)
        la_gt, yb_gt = PM["La"] * batch(f, dla_gt), PM["Yb"] * batch(f, dyb_gt)
        return [f, la_sp, la_sp / yb_sp, la_gt, la_gt / yb_gt]

    fgrid = np.exp(np.linspace(math.log(0.004), math.log(0.3), 80))
    write_table(__file__, ("f", "la_sp", "lay_sp", "la_gt", "lay_gt"),
                [traj(f) for f in fgrid], part="traj")
    write_table(__file__, ("f", "la_sp", "lay_sp", "la_gt", "lay_gt"),
                [traj(f) for f in (0.01, 0.02, 0.05, 0.10, 0.20)], part="ticks")
    write_table(__file__, ("name", "la", "layb"),
                [["A", LAVA_A[0], LAVA_A[0] / LAVA_A[1]],
                 ["B", LAVA_B[0], LAVA_B[0] / LAVA_B[1]]], part="lavas")

    vals = [
        ["D_La_sp", dla_sp], ["D_Yb_sp", dyb_sp], ["D_La_gt", dla_gt], ["D_Yb_gt", dyb_gt],
        ["F_A_batch", f_batch(LAVA_A[0] / PM["La"], dla_sp)],
        ["F_A_aggregate", f_aggregate(LAVA_A[0] / PM["La"], dla_sp)],
        ["F_B_batch_gt", f_batch(LAVA_B[0] / PM["La"], dla_gt)],
        ["max_LaYb_sp", (PM["La"] / dla_sp) / (PM["Yb"] / dyb_sp)],
        ["max_LaYb_gt", (PM["La"] / dla_gt) / (PM["Yb"] / dyb_gt)],
    ]
    d0, p = ex73()
    vals += [["ex73_D0_La", d0["La"]], ["ex73_P_La", p["La"]],
             ["ex73_D0_Sm", d0["Sm"]], ["ex73_P_Sm", p["Sm"]]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

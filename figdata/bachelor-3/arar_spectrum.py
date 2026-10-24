"""A synthetic 40Ar/39Ar step-heating spectrum (Year 3, advanced geochronology).

Age equation t = ln(1 + J R) / lambda with R = 40Ar*/39Ar(K) and the total
40K decay constant lambda = 5.543e-10 /yr (ledger amherst:constants). J is
found from a monitor of known age, Fish Canyon sanidine 28.201 Ma (ledger
schaen20:monitors), irradiated beside the sample.

The biotite is invented: a plateau at 296 Ma (the cooling age of the Varden
granite biotite) with three low-temperature steps that lost argon, a staircase
rising to the plateau. Step values are printed in the weekend problem rounded
as R to 3 decimals and sigma(R) to 3 decimals.

  part steps    k f39 cum0 cum1 R sR age sage   (f39 in %, ages in Ma, 1 sigma)
  part boxes    cum age lo hi                    step outline and 2 sigma band
  part values   what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

LAMBDA = 5.543e-10
T_MONITOR = 28.201
R_MONITOR = 1.3129
F39 = (4, 6, 8, 12, 14, 15, 14, 12, 9, 6)
AGES = (150.0, 228.0, 279.0, 296.6, 295.3, 296.2, 297.1, 295.8, 296.9, 295.0)
REL_SR = 0.004
PLATEAU = range(3, 10)


def j_factor(t_ma=T_MONITOR, r=R_MONITOR):
    return math.expm1(LAMBDA * t_ma * 1e6) / r


def age(r, j):
    return math.log1p(j * r) / LAMBDA / 1e6


def ratio(t_ma, j):
    return math.expm1(LAMBDA * t_ma * 1e6) / j


def dage_dr(r, j):
    return j / (1 + j * r) / LAMBDA / 1e6


def weighted_mean(x, s):
    x, w = np.asarray(x, float), 1 / np.asarray(s, float) ** 2
    m = np.sum(w * x) / np.sum(w)
    mswd = np.sum(w * (x - m) ** 2) / (len(x) - 1)
    return m, 1 / math.sqrt(np.sum(w)), mswd


def steps():
    j = round(j_factor(), 5)
    rows, cum = [], 0.0
    for k, (f, t) in enumerate(zip(F39, AGES)):
        r = round(ratio(t, j), 3)
        sr = round(REL_SR * r, 3)
        a = age(r, j)
        rows.append([k + 1, f, cum, cum + f, r, sr, a, dage_dr(r, j) * sr])
        cum += f
    return j, rows


def main():
    j, rows = steps()
    write_table(__file__, ("k", "f39", "cum0", "cum1", "R", "sR", "age", "sage"), rows, part="steps")
    box = []
    for r in rows:
        for c in (r[2], r[3]):
            box.append([c, r[6], r[6] - 2 * r[7], r[6] + 2 * r[7]])
    write_table(__file__, ("cum", "age", "lo", "hi"), box, part="boxes")
    pl = [rows[i] for i in PLATEAU]
    m, sm, mswd = weighted_mean([r[6] for r in pl], [r[7] for r in pl])
    rtot = sum(r[1] * r[4] for r in rows) / 100.0
    write_table(__file__, ("what", "value"), [
        ["J", j], ["plateau", m], ["plateau_s", sm], ["plateau_mswd", mswd],
        ["plateau_f39", sum(r[1] for r in pl)], ["total_gas_R", rtot], ["total_gas_age", age(rtot, j)],
    ], part="values")


if __name__ == "__main__":
    main()

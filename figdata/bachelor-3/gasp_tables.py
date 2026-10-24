"""The GASP equilibrium 3 anorthite = grossular + 2 kyanite + quartz computed
from calorimetric tables and compared with the experimental line (Year 3,
thermodynamics of rocks).

Tables: Robie and Hemingway (1995), ledger rh95:gasp-298 (298.15 K, 1 bar)
and rh95:gasp-ht (Gibbs energies of formation at 800-1200 K). Experiment:
Koziol and Newton (1988), P0 = 22.80 T(C) - 1093 bar, ledger kn88:gasp
(Book 4). Thermometer of the problem: garnet-biotite exchange with Delta H =
52635 J, Delta S = 20.20 J/K (ideal fit of Ferry and Spear's brackets, ledger
h97:ideal, Book 4) and Delta V = 0.311 J/bar (h97:fs-reaction).

End-member line, constant Delta H, Delta S, Delta V (the 1 of P - 1 kept):
    P0 = 1 + (T Delta S - Delta H) / Delta V
from the tables (heat capacities included, Delta V constant):
    P0 = 1 - Delta G(T, 1 bar) / Delta V.
With ideal activities a_grs = X_Ca^3 (garnet), a_an = X_an (plagioclase),
    P = P0 - R T ln(X_Ca^3 / X_an^3) / Delta V
(Delta V = -6.210 J/bar with the experimental line, as in kn88:gasp).

  part lines    tc p_const p_kn88     end-member lines (kbar) vs T (C)
  part tables   tc p_table            from the high-temperature tables
  part values   what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

R = 8.314462618
# 298.15 K: (Delta_f H kJ/mol, S J/(mol K), V cm3/mol)
DATA = {"grs": (-6640.0, 260.1, 125.28), "an": (-4234.0, 199.3, 100.79),
        "ky": (-2593.8, 82.8, 44.15), "qz": (-910.7, 41.5, 22.69)}
# Delta_f G (kJ/mol) at 800 ... 1200 K
TABLE_T = (800.0, 900.0, 1000.0, 1100.0, 1200.0)
DFG = {"grs": (-5672.6, -5553.0, -5432.2, -5310.8, -5187.7),
       "an": (-3628.7, -3554.0, -3478.1, -3401.6, -3324.7),
       "ky": (-2189.7, -2139.9, -2088.8, -2037.1, -1985.6),
       "qz": (-765.3, -747.7, -730.2, -712.8, -695.4)}
NU = {"grs": 1, "ky": 2, "qz": 1, "an": -3}
KN_SLOPE, KN_INTERCEPT, KN_DV = 22.80, -1093.0, -6.210
GB_DH, GB_DS, GB_DV = 52635.0, 20.20, 0.311


def reaction_props():
    dh = sum(n * DATA[k][0] for k, n in NU.items()) * 1000.0
    ds = sum(n * DATA[k][1] for k, n in NU.items())
    dv = sum(n * DATA[k][2] for k, n in NU.items()) / 10.0      # J/bar
    return dh, ds, dv


def p_const(t_k):
    dh, ds, dv = reaction_props()
    return 1.0 + (t_k * ds - dh) / dv


def dg_table(i):
    return sum(n * DFG[k][i] for k, n in NU.items()) * 1000.0


def p_table(i):
    return 1.0 - dg_table(i) / reaction_props()[2]


def p_kn88(t_c):
    return KN_SLOPE * t_c + KN_INTERCEPT


def gasp_pressure(t_k, x_ca, x_an, p0=None):
    """Pressure (bar) of the GASP barometer at t_k (K). Default: the
    experimental end-member line with its own Delta V (-6.210 J/bar); with p0
    given (bar), the table Delta V."""
    if p0 is None:
        p0, dv = p_kn88(t_k - 273.15), KN_DV
    else:
        dv = reaction_props()[2]
    return p0 - R * t_k * math.log(x_ca ** 3 / x_an ** 3) / dv


def gb_temperature(p_bar, kd):
    return (GB_DH + GB_DV * p_bar) / (GB_DS - 3.0 * R * math.log(kd))


def intersect(kd, x_ca, x_an, p0_fn=None, p_start=8000.0, n=30):
    p = p_start
    for _ in range(n):
        t = gb_temperature(p, kd)
        p0 = None if p0_fn is None else p0_fn(t)
        p = gasp_pressure(t, x_ca, x_an, p0)
    return gb_temperature(p, kd), p


if __name__ == "__main__":
    tcs = np.arange(400.0, 1300.01, 10.0)
    write_table(__file__, ("tc", "p_const", "p_kn88"),
                [(t, p_const(t + 273.15) / 1000.0, p_kn88(t) / 1000.0) for t in tcs], part="lines")
    write_table(__file__, ("tc", "p_table"),
                [(t - 273.15, p_table(i) / 1000.0) for i, t in enumerate(TABLE_T)], part="tables")
    dh, ds, dv = reaction_props()
    vals = [("dH", dh), ("dS", ds), ("dV", dv), ("slope_const", ds / dv),
            ("p_const_900K", p_const(900.0)), ("p_table_900K", p_table(1)),
            ("p_kn88_900K", p_kn88(900.0 - 273.15)),
            ("p_const_1200K", p_const(1200.0)), ("p_table_1200K", p_table(4)),
            ("p_kn88_1200K", p_kn88(1200.0 - 273.15))]
    write_table(__file__, ("what", "value"), vals, part="values")

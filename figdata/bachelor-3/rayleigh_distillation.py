"""Rayleigh distillation of an air mass cooling towards an ice-sheet dome
(Year 3, stable isotopes).

Ice-vapour equilibrium fractionation factors (ledger gkinis14:alpha-ice):
  ln alpha18 = 11.839/T - 28.224e-3          (Majoube)
  ln alphaD  = 16288/T^2 - 9.34e-2            (Merlivat and Nief)
Saturation vapour pressure over ice from the IAPWS sublimation curve (ledger
iapws:melt-subl): ln(p/pt) = (1/theta) sum a_i theta^b_i, theta = T/273.16; only
ratios are used, so pt cancels.

The air mass cools isobarically from T0 = 0 degC; the fraction of vapour left
is f = e_i(T)/e_i(T0). The vapour obeys d ln R_v = (alpha(T) - 1) d ln f
(Rayleigh distillation with a temperature-dependent alpha), and the snow
formed at T is in equilibrium with it: R_s = alpha(T) R_v. The vapour at T0 is
invented (d18O = -20 permil, dD = -150 permil, on the line dD = 8 d18O + 10).

The traverse to "Dome Ilse" is invented: condensation temperatures -10 degC
(Coast), -20 degC (Midway), -30 degC (Dome Ilse).

  part curve     t f d18v d18s dDv dDs dex       (t in degC, every 0.5 degC, 0 to -55)
  part stations  name t f a18 aD d18s dDs dex
  part values    what value
"""
import math
import os
import sys

import numpy as np
from scipy.integrate import quad

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

TT = 273.16
SUB_A = (-21.2144006, 27.3203819, -6.10598130)
SUB_B = (0.00333333333, 1.20666667, 1.70333333)
T0_C = 0.0
D18_V0 = -20.0
DD_V0 = 8.0 * D18_V0 + 10.0
STATIONS = (("Coast", -10.0), ("Midway", -20.0), ("Dome Ilse", -30.0))


def kelvin(t_c):
    return t_c + 273.15


def ln_ei(t_c):
    """ln(e_i/pt) over ice, IAPWS R14-08."""
    th = kelvin(t_c) / TT
    return sum(a * th ** b for a, b in zip(SUB_A, SUB_B)) / th


def frac(t_c, t0_c=T0_C):
    return math.exp(ln_ei(t_c) - ln_ei(t0_c))


def alpha18(t_c):
    return math.exp(11.839 / kelvin(t_c) - 28.224e-3)


def alphad(t_c):
    return math.exp(16288.0 / kelvin(t_c) ** 2 - 9.34e-2)


def dlnf_dt(t_c, h=1e-4):
    return (ln_ei(t_c + h) - ln_ei(t_c - h)) / (2 * h)


def vapour(t_c, alpha, d0, t0_c=T0_C):
    """delta of the vapour at t_c: ln(R/R0) = int (alpha - 1) d ln f."""
    integral = quad(lambda t: (alpha(t) - 1.0) * dlnf_dt(t), t0_c, t_c, limit=200)[0]
    return (1000.0 + d0) * math.exp(integral) - 1000.0


def snow(t_c, alpha, d0, t0_c=T0_C):
    return alpha(t_c) * (1000.0 + vapour(t_c, alpha, d0, t0_c)) - 1000.0


def point(t_c):
    d18v = vapour(t_c, alpha18, D18_V0)
    ddv = vapour(t_c, alphad, DD_V0)
    d18s = alpha18(t_c) * (1000 + d18v) - 1000
    dds = alphad(t_c) * (1000 + ddv) - 1000
    return d18v, d18s, ddv, dds, dds - 8 * d18s


def stepwise(legs):
    """Hand method of the problem: constant alpha per leg, taken at the leg's mid temperature."""
    d = D18_V0
    out = []
    for t_a, t_b in legs:
        a = alpha18(0.5 * (t_a + t_b))
        d = (1000 + d) * (frac(t_b) / frac(t_a)) ** (a - 1) - 1000
        out.append((t_b, d, alpha18(t_b) * (1000 + d) - 1000))
    return out


def main():
    rows = []
    for t in np.arange(0.0, -55.01, -0.5):
        t = float(t)
        rows.append([t, frac(t)] + list(point(t)[:2]) + list(point(t)[2:]))
    write_table(__file__, ("t", "f", "d18v", "d18s", "dDv", "dDs", "dex"), rows, part="curve")
    st = []
    for name, t in STATIONS:
        d18v, d18s, ddv, dds, dex = point(t)
        st.append([name.replace(" ", "~"), t, frac(t), alpha18(t), alphad(t), d18s, dds, dex])
    write_table(__file__, ("name", "t", "f", "a18", "aD", "d18s", "dDs", "dex"), st,
                part="stations")
    s0 = point(-10.0)[1]
    s1 = point(-30.0)[1]
    legs = stepwise([(0.0, -10.0), (-10.0, -20.0), (-20.0, -30.0)])
    write_table(__file__, ("what", "value"), [
        ["slope_d18s_per_degC_coast_dome", (s0 - s1) / 20.0],
        ["d18s_dome_exact", s1],
        ["d18s_dome_stepwise", legs[-1][2]],
        ["f_dome", frac(-30.0)],
    ], part="values")


if __name__ == "__main__":
    main()

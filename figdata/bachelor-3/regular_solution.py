"""A symmetric regular solution: Gibbs energy of mixing, solvus, spinodal and
a one-dimensional section at fixed bulk composition (Year 3, thermodynamics
of rocks). Illustrative interaction parameter W (not a fitted mineral value).

    G_mix(x) = R T [x ln x + (1 - x) ln(1 - x)] + W x (1 - x)
Critical temperature Tc = W / (2 R). Below it, the solvus (binodal) is
symmetric: its limbs x and 1 - x satisfy dG_mix/dx = 0,
    R T ln(x / (1 - x)) + W (1 - 2 x) = 0,
the spinodal d2G_mix/dx2 = 0: x (1 - x) = R T / (2 W).
A rock of bulk composition X0 inside the solvus splits into the two limb
compositions; the fraction of the x-rich phase is (X0 - x1) / (x2 - x1).

  part gx       x g0900 g1203 g1500        G_mix (kJ/mol) at 900 K, Tc, 1500 K
  part solvus   x t_bin t_spin             solvus and spinodal (K)
  part section  t x1 x2 frac               the section at X0 (K; limb compositions; fraction)
  part values   what value
"""
import math
import os
import sys

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

R = 8.314462618
W = 20000.0
X0 = 0.3
NAN = float("nan")


def tc(w=W):
    return w / (2.0 * R)


def g_mix(x, t, w=W):
    x = np.asarray(x, dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        ideal = np.where((x > 0) & (x < 1), x * np.log(x) + (1 - x) * np.log(1 - x), 0.0)
    return R * t * ideal + w * x * (1 - x)


def binodal_t(x, w=W):
    """Temperature at which x lies on the solvus (x < 1/2)."""
    return w * (1.0 - 2.0 * x) / (R * math.log((1.0 - x) / x))


def spinodal_t(x, w=W):
    return 2.0 * w * x * (1.0 - x) / R


def limb(t, w=W):
    """Low-x limb of the solvus at t < Tc."""
    if t >= tc(w):
        return NAN
    f = lambda x: R * t * math.log(x / (1 - x)) + w * (1 - 2 * x)  # noqa: E731
    return brentq(f, 1e-12, 0.5 - 1e-12)


def common_tangent_ok(t, w=W):
    """Check that the tangent at the two limbs is the same line."""
    x1 = limb(t, w)
    x2 = 1.0 - x1
    g1, g2 = float(g_mix(x1, t, w)), float(g_mix(x2, t, w))
    return x1, x2, g1, g2


def section(t, x0=X0, w=W):
    x1 = limb(t, w)
    if x1 != x1 or x0 <= x1:
        return NAN, NAN, 0.0
    x2 = 1.0 - x1
    return x1, x2, (x0 - x1) / (x2 - x1)


if __name__ == "__main__":
    xs = np.linspace(0.0, 1.0, 201)
    write_table(__file__, ("x", "g0900", "g1203", "g1500"),
                [(x,) + tuple(float(g_mix(x, t)) / 1000.0 for t in (900.0, tc(), 1500.0)) for x in xs],
                part="gx")
    rows = []
    for x in np.linspace(0.005, 0.995, 199):
        tb = binodal_t(x) if abs(x - 0.5) > 1e-9 else tc()
        if x > 0.5:
            tb = binodal_t(1.0 - x)
        rows.append((x, tb, spinodal_t(x)))
    write_table(__file__, ("x", "t_bin", "t_spin"), rows, part="solvus")
    rows = []
    for t in np.arange(600.0, 1300.01, 5.0):
        x1, x2, fr = section(t)
        rows.append((t, x1, x2, fr))
    write_table(__file__, ("t", "x1", "x2", "frac"), rows, part="section")
    vals = [("Tc", tc()), ("T_enter_X0", binodal_t(X0)), ("T_spinodal_X0", spinodal_t(X0)),
            ("limb_900", limb(900.0)), ("frac_900", section(900.0)[2]), ("limb_1000", limb(1000.0))]
    write_table(__file__, ("what", "value"), vals, part="values")

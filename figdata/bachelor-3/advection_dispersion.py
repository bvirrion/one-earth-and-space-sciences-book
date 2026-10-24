"""Breakthrough curves of the one-dimensional advection--dispersion equation
(Year 3, hydrogeology). Invented values.

    R dC/dt = D d2C/dx2 - v dC/dx,   D = alpha v,
    C(0, t) = C0 for t > 0, C(x, 0) = 0, C bounded as x -> infinity,

has the solution (Ogata and Banks)

    C/C0 = 1/2 [erfc((x - v' t)/(2 sqrt(D' t))) + exp(v' x/D') erfc((x + v' t)/(2 sqrt(D' t)))]

with v' = v/R, D' = D/R. The second term is evaluated as
exp(a - b^2) erfcx(b) to avoid overflow. Seepage velocity v = 0.5 m/d, the
observation point 100 m down-gradient; dispersivities 1, 3 and 10 m (the last
one tenth of the distance, the rule of thumb of ledger epa:dispersivity); a
retarded solute with R = 3 and alpha = 3 m. Molecular diffusion is neglected.

  part btc      t c1 c3 c10 cR     C/C0 at x = 100 m against t (days)
  part profile  x c1 c3 c10        C/C0 against x after 150 days
  part values   what value
"""
import math
import os
import sys

import numpy as np
from scipy.special import erfc, erfcx

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

V = 0.5          # m/d
X_OBS = 100.0    # m
ALPHAS = (1.0, 3.0, 10.0)
R_SORB, ALPHA_SORB = 3.0, 3.0


def conc(x, t, alpha, v=V, r=1.0):
    """C/C0 of the Ogata--Banks solution."""
    if t <= 0:
        return 0.0
    vp = v / r
    dp = alpha * v / r
    s = 2.0 * math.sqrt(dp * t)
    a = (x - vp * t) / s
    b = (x + vp * t) / s
    second = math.exp(vp * x / dp - b * b) * erfcx(b)
    return 0.5 * (float(erfc(a)) + second)


def time_at(frac, alpha, r=1.0, x=X_OBS):
    """Time at which C/C0 reaches frac at x, by bisection."""
    lo, hi = 1e-6, 1e5
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if conc(x, mid, alpha, r=r) < frac:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    rows = []
    for t in np.arange(0.0, 1000.01, 2.5):
        rows.append([t] + [conc(X_OBS, t, a) for a in ALPHAS]
                    + [conc(X_OBS, t, ALPHA_SORB, r=R_SORB)])
    write_table(__file__, ("t", "c1", "c3", "c10", "cR"), rows, part="btc")
    prof = []
    for x in np.arange(0.0, 160.01, 0.5):
        prof.append([x] + [conc(x, 150.0, a) for a in ALPHAS])
    write_table(__file__, ("x", "c1", "c3", "c10"), prof, part="profile")
    vals = [["t_adv", X_OBS / V], ["t_adv_R", R_SORB * X_OBS / V]]
    for a in ALPHAS:
        vals += [["t16_a%g" % a, time_at(0.16, a)], ["t50_a%g" % a, time_at(0.5, a)],
                 ["t84_a%g" % a, time_at(0.84, a)]]
    vals += [["t50_R", time_at(0.5, ALPHA_SORB, r=R_SORB)],
             ["sigma_x_a3_200d", math.sqrt(2 * ALPHA_SORB * V * 200.0)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

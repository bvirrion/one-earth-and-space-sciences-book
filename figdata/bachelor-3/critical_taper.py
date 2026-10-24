"""The critical taper of a subaerial Coulomb wedge in the small-angle
approximation (Year 3, thrust belts and orogenic wedges).

A wedge of uniform density, cohesionless, internal friction mu = tan(phi),
pore-pressure ratio lambda inside, resting on a base of friction mu_b and
pore-pressure ratio lambda_b, with sigma_1 horizontal and every point at
failure (Coulomb, effective stresses):
    sigma'_xx = (1 + K) sigma'_zz,  K = 2 sin(phi) / (1 - sin(phi)),
and a horizontal force balance on a vertical slice gives
    alpha + beta = (beta + mu_b (1 - lambda_b)) / (1 + K (1 - lambda))
(radians, surface slope alpha, basal dip beta towards the hinterland).
Parameters of the plotted curves: western Taiwan, mu = 1.03, mu_b = 0.85
(ledger dsd83:taper), lambda = lambda_b = 0.4, 0.7, 0.9.

  part curves   beta a040 a070 a090      surface slope (deg) vs basal dip (deg)
  part bands    beta t3 t4 t12 t13       lines of constant taper 3, 4, 12, 13 deg (alpha = taper - beta;
                                         negative values clipped by the plot)
                                         (ledger deville21:jura)
  part values   what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

MU = 1.03
MU_B = 0.85
LAMBDAS = (0.4, 0.7, 0.9)


def k_factor(mu):
    s = math.sin(math.atan(mu))
    return 2.0 * s / (1.0 - s)


def taper(beta_deg, mu=MU, mu_b=MU_B, lam=0.4, lam_b=None):
    """Critical taper alpha + beta in degrees."""
    if lam_b is None:
        lam_b = lam
    b = math.radians(beta_deg)
    t = (b + mu_b * (1.0 - lam_b)) / (1.0 + k_factor(mu) * (1.0 - lam))
    return math.degrees(t)


def alpha(beta_deg, **kw):
    return taper(beta_deg, **kw) - beta_deg


def lambda_from_taper(alpha_deg, beta_deg, mu=MU, mu_b=MU_B):
    """Solve the critical-taper equation for lambda = lambda_b."""
    a, b = math.radians(alpha_deg), math.radians(beta_deg)
    k = k_factor(mu)
    # (a + b)(1 + k u) = b + mu_b u, u = 1 - lambda
    u = (b - (a + b)) / ((a + b) * k - mu_b)
    return 1.0 - u


def beta_flat(mu=MU, mu_b=MU_B, lam=0.4):
    """Basal dip at which the critical surface slope vanishes (degrees)."""
    return math.degrees(mu_b * (1.0 - lam) / (k_factor(mu) * (1.0 - lam)))


if __name__ == "__main__":
    betas = np.arange(0.0, 15.01, 0.25)
    write_table(__file__, ("beta", "a040", "a070", "a090"),
                [(b,) + tuple(alpha(b, lam=l) for l in LAMBDAS) for b in betas], part="curves")
    rows = [(b,) + tuple(t - b for t in (3.0, 4.0, 12.0, 13.0)) for b in betas]
    write_table(__file__, ("beta", "t3", "t4", "t12", "t13"), rows, part="bands")
    vals = [("K_taiwan", k_factor(MU)), ("K_mu060", k_factor(0.6)),
            ("alpha0_040", alpha(0.0, lam=0.4)), ("alpha0_070", alpha(0.0, lam=0.7)),
            ("alpha0_090", alpha(0.0, lam=0.9)),
            ("taper_beta6_040", taper(6.0, lam=0.4)), ("taper_beta6_090", taper(6.0, lam=0.9))]
    write_table(__file__, ("what", "value"), vals, part="values")

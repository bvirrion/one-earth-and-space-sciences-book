"""In situ 10Be in a steadily eroding rock surface (Year 3, advanced geochronology).

A grain now at the surface was at the depth eps (t - t') at the time t'; with
production P exp(-rho z / Lambda) and decay lambda,
    N(t) = P / (lambda + rho eps / Lambda) (1 - exp(-(lambda + rho eps / Lambda) t)).
Constants: 10Be half-life 1.388 Myr (ledger lugaro:slr-table), attenuation
length 160 g/cm2 and a sea-level high-latitude spallation production rate of
4.96 atoms/g/yr (ledger balco08:params), granite density 2.7 g/cm3 (ledger
zech04:exposure).

  part growth   t n0 n1 n10       (t in yr; N in atoms/g for 0, 1, 10 m/Myr)
  part values   what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

HALF_LIFE = 1.388e6
LAMBDA = math.log(2) / HALF_LIFE
ATT = 160.0        # g/cm2
P_SLHL = 4.96      # atoms/g/yr
RHO = 2.7          # g/cm3


def mu(eps_m_per_myr, rho=RHO, att=ATT):
    """rho eps / Lambda in 1/yr for eps in m/Myr."""
    return rho * eps_m_per_myr * 1e-4 / att


def concentration(t, eps_m_per_myr, p=P_SLHL):
    k = LAMBDA + mu(eps_m_per_myr)
    return p / k * (-np.expm1(-k * np.asarray(t, float)))


def concentration_ode(t, eps_m_per_myr, p=P_SLHL, n=20000):
    """Explicit integration along the grain's path (midpoint rule), for the test."""
    dt = t / n
    nn = 0.0
    for i in range(n):
        tp = (i + 0.5) * dt
        z = eps_m_per_myr * 1e-4 * (t - tp)          # cm
        nn += (p * math.exp(-RHO * z / ATT) - LAMBDA * nn) * dt
    return nn


def exposure_age(n, p=P_SLHL):
    return -math.log1p(-n * LAMBDA / p) / LAMBDA


def erosion_rate(n, p=P_SLHL, rho=RHO, att=ATT):
    """Steady-state erosion rate (m/Myr) from N, decay included."""
    return (p / n - LAMBDA) * att / rho * 1e4


def main():
    ts = np.exp(np.linspace(math.log(1e3), math.log(1e7), 81))
    write_table(__file__, ("t", "n0", "n1", "n10"),
                [[t, concentration(t, 0), concentration(t, 1), concentration(t, 10)] for t in ts],
                part="growth")
    write_table(__file__, ("what", "value"), [
        ["lambda", LAMBDA], ["nsat0", P_SLHL / LAMBDA], ["nsat1", P_SLHL / (LAMBDA + mu(1))],
        ["nsat10", P_SLHL / (LAMBDA + mu(10))],
    ], part="values")


if __name__ == "__main__":
    main()

"""Steady continental geotherms with exponentially decreasing heat production
(Year 3, thermal models of the lithosphere).

Heat production A(z) = A0 exp(-z/hr), conductivity k constant, surface
temperature 0 C, surface heat flow q0 = qm + A0 hr (qm the reduced heat flow):
    T(z) = qm z / k + (A0 hr^2 / k) (1 - exp(-z/hr)).
Model choices of the chapter (not data): k = 2.5 W/m/K (within ledger
delaney86:properties), hr = 10 km (the order of the Roy et al. depth scales,
ledger b2roy:provinces), and a crustal share A0 hr = 0.4 q0, for three surface
heat flows 40, 60 and 80 mW/m2. The 1300 C isotherm is taken as the base of
the thermal lithosphere.

  part geotherms  z T40 T60 T80   temperature (C) against depth (km), 0-200 km
  part values     what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

K = 2.5
HR = 10e3
SHARE = 0.4
Q0S = (40e-3, 60e-3, 80e-3)
T_BASE = 1300.0


def geotherm(z, q0, k=K, hr=HR, share=SHARE):
    a0hr = share * q0
    qm = q0 - a0hr
    a0 = a0hr / hr
    z = np.asarray(z, dtype=float)
    return qm * z / k + a0 * hr * hr / k * (1 - np.exp(-z / hr))


def depth_of(temp, q0, k=K, hr=HR, share=SHARE):
    """Depth (m) where the geotherm reaches temp, by bisection."""
    lo, hi = 0.0, 1e6
    for _ in range(200):
        mid = (lo + hi) / 2
        if geotherm(mid, q0, k, hr, share) < temp:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def heat_flow_at(z, q0, hr=HR, share=SHARE):
    """Heat flow (W/m2) at depth z: qm + A0 hr exp(-z/hr)."""
    return q0 * (1 - share) + share * q0 * math.exp(-z / hr)


if __name__ == "__main__":
    zs = np.arange(0.0, 200e3 + 1, 2e3)
    rows = [(z / 1e3,) + tuple(float(geotherm(z, q)) for q in Q0S) for z in zs]
    write_table(__file__, ("z", "T40", "T60", "T80"), rows, part="geotherms")
    vals = []
    for q in Q0S:
        tag = "%d" % round(q * 1e3)
        vals += [("zL_%s_km" % tag, depth_of(T_BASE, q) / 1e3),
                 ("T35_%s" % tag, float(geotherm(35e3, q))),
                 ("qm_%s_mW" % tag, 1e3 * q * (1 - SHARE))]
    write_table(__file__, ("what", "value"), vals, part="values")

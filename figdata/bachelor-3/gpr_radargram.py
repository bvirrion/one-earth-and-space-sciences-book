"""Travel times of a zero-offset ground-penetrating-radar profile (Year 3, field and lab
methods III).

Wave regime (sigma << omega epsilon): V = c / sqrt(eps_r) (ledger gpg:gpr). A buried pipe
at (x_p, d) returns at the two-way time t(x) = 2 sqrt((x - x_p)^2 + d^2) / V, a
hyperbola with apex t0 = 2 d / V; any second point (x, t) on it gives the velocity,
V = 2 |x - x_p| / sqrt(t^2 - t0^2). A flat reflector at depth h returns at 2 h / V.

The exercise profile (invented, on the Varden alluvial floor): dry alluvium with eps_r
EPS_DRY (dry sand 3-5 in ledger gpg:gpr), a drain pipe at X_PIPE, D_PIPE deep, and the
water table at H_WT, where the permittivity jumps to EPS_SAT (saturated sand 20-30).

  part pipe     x_m t_ns         the pipe hyperbola
  part table    x_m t_ns         the water-table reflection
  part values   what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

C = 0.299792458          # m/ns
EPS_DRY = 4.0
EPS_SAT = 25.0
X_PIPE = 4.0             # m
D_PIPE = 0.8             # m
H_WT = 1.5               # m (the water table of the resistivity sounding)


def velocity(eps_r):
    return C / math.sqrt(eps_r)


def pipe_time(x, xp, d, v):
    return 2.0 * np.sqrt((np.asarray(x, dtype=float) - xp) ** 2 + d * d) / v


def velocity_from_hyperbola(x, t, xp, t0):
    return 2.0 * abs(x - xp) / math.sqrt(t * t - t0 * t0)


def reflection_coefficient(eps1, eps2):
    """Normal-incidence amplitude reflection coefficient of the radar wave
    (non-magnetic media): (sqrt(eps1) - sqrt(eps2)) / (sqrt(eps1) + sqrt(eps2))."""
    a, b = math.sqrt(eps1), math.sqrt(eps2)
    return (a - b) / (a + b)


def skin_depth_wave(eps_r, sigma):
    """Skin depth in the wave regime, 2 / sigma * sqrt(eps / mu0) = 0.0053 sqrt(eps_r) /
    sigma (sigma in S/m)."""
    eps0, mu0 = 8.8541878128e-12, 4e-7 * math.pi
    return 2.0 / sigma * math.sqrt(eps0 * eps_r / mu0)


def main():
    v = velocity(EPS_DRY)
    xs = np.arange(0.0, 8.001, 0.05)
    tp = pipe_time(xs, X_PIPE, D_PIPE, v)
    write_table(__file__, ("x_m", "t_ns"), list(zip(xs, tp)), part="pipe")
    twt = 2.0 * H_WT / v
    write_table(__file__, ("x_m", "t_ns"), [(0.0, twt), (8.0, twt)], part="table")
    t0 = 2.0 * D_PIPE / v
    t2 = float(pipe_time(X_PIPE + 1.0, X_PIPE, D_PIPE, v))
    vals = [["V_dry_m_per_ns", v], ["V_sat_m_per_ns", velocity(EPS_SAT)], ["t0_ns", t0],
            ["t_at_1m_ns", t2], ["t_watertable_ns", twt],
            ["R_dry_sat", reflection_coefficient(EPS_DRY, EPS_SAT)],
            ["skin_limestone_m", skin_depth_wave(6.0, 1e-3)],
            ["skin_clay_m", skin_depth_wave(20.0, 0.1)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

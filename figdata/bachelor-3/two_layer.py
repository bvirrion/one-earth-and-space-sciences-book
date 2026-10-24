"""Two-layer energy-balance model of the climate response (Year 3, climate models).

    C   dT/dt   = F(t) - lam T - gam (T - Td)
    C_d dTd/dt  = gam (T - Td)

T the surface-layer and Td the deep-ocean temperature anomaly (deg C), F the
effective radiative forcing (W/m2). Parameters: the means of the calibration of
the AR6 two-layer emulator to 44 CMIP6 models, C = 8.1 and C_d = 110 W yr m-2 K-1,
gam = 0.62 W m-2 K-1, with the efficacy set to 1 (ledger ar6sm7:two-layer); the
feedback parameter lam = 1.33 W m-2 K-1, the mean of the emulator's sampling
distribution of alpha (same row); F_2x = 3.93 W/m2 (ipcc:erf-2xco2), F_4x = 2 F_2x
(logarithmic forcing, ipcc:log-co2).

The homogeneous system has two decay rates, the eigenvalues of
M = [[-(lam + gam)/C, gam/C], [gam/C_d, -gam/C_d]]; for an abrupt forcing F

    T(t) = (F/lam) [1 - a_f exp(-t/tau_f) - a_s exp(-t/tau_s)],  a_f + a_s = 1.

Integrated by the exact matrix exponential of the linear system (piecewise
constant forcing over steps of DT years).

  part abrupt  t T Td        abrupt 4xCO2, 0-500 yr
  part ramp    t T Td F      1 % per year CO2, F = F_2x t/70, 0-140 yr
  part values  what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

C, CD, GAM, LAM = 8.1, 110.0, 0.62, 1.33
F2X = 3.93
DT = 0.1


def matrix(lam=LAM, gam=GAM, c=C, cd=CD):
    return np.array([[-(lam + gam) / c, gam / c], [gam / cd, -gam / cd]])


def timescales(lam=LAM, gam=GAM, c=C, cd=CD):
    """(tau_fast, tau_slow) in years."""
    ev = np.linalg.eigvals(matrix(lam, gam, c, cd))
    ev = sorted(-ev.real, reverse=True)
    return 1 / ev[0], 1 / ev[1]


def amplitudes(lam=LAM, gam=GAM, c=C, cd=CD):
    """(a_fast, a_slow) of the surface response to an abrupt forcing."""
    m = matrix(lam, gam, c, cd)
    w, v = np.linalg.eig(m)
    order = np.argsort(-w.real)[::-1]       # fast first (most negative)
    w, v = w[order].real, v[:, order].real
    # T_eq = (F/lam)(1, 1); x(t) = T_eq + sum c_i v_i exp(w_i t), x(0) = 0
    coef = np.linalg.solve(v, -np.ones(2))
    a = -coef * v[0]                         # surface components, normalised by F/lam
    return float(a[0]), float(a[1])


def step_matrices(dt=DT, lam=LAM, gam=GAM, c=C, cd=CD):
    m = matrix(lam, gam, c, cd)
    w, v = np.linalg.eig(m)
    vi = np.linalg.inv(v)
    e = (v @ np.diag(np.exp(w * dt)) @ vi).real
    # forcing enters the surface equation as F/C; exact for F constant over the step
    g = (v @ np.diag((np.exp(w * dt) - 1) / w) @ vi).real @ np.array([1 / c, 0.0])
    return e, g


def integrate(forcing, years, dt=DT, **kw):
    e, g = step_matrices(dt, **kw)
    x = np.zeros(2)
    out = [(0.0, 0.0, 0.0)]
    n = int(round(years / dt))
    for i in range(n):
        t = (i + 0.5) * dt
        x = e @ x + g * forcing(t)
        out.append(((i + 1) * dt, x[0], x[1]))
    return out


def ecs(lam=LAM):
    return F2X / lam


def tcr_estimate(lam=LAM, gam=GAM):
    """TCR ~ F_2x/(lam + kappa), kappa = gam with efficacy 1."""
    return F2X / (lam + gam)


def main():
    ab = integrate(lambda t: 2 * F2X, 500.0)
    write_table(__file__, ("t", "T", "Td"), [r for r in ab if abs(r[0] * 2 - round(r[0] * 2)) < 1e-6],
                part="abrupt")
    rp = integrate(lambda t: F2X * t / 70.0, 140.0)
    write_table(__file__, ("t", "T", "Td", "F"),
                [(r[0], r[1], r[2], F2X * r[0] / 70.0) for r in rp
                 if abs(r[0] - round(r[0])) < 1e-6], part="ramp")
    tf, ts = timescales()
    af, as_ = amplitudes()
    tcr = [r for r in rp if abs(r[0] - 70.0) < 1e-6][0][1]
    t4_10 = [r for r in ab if abs(r[0] - 10.0) < 1e-6][0][1]
    t4_100 = [r for r in ab if abs(r[0] - 100.0) < 1e-6][0][1]
    vals = [["tau_fast", tf], ["tau_slow", ts], ["a_fast", af], ["a_slow", as_],
            ["ecs", ecs()], ["tcr_run", tcr], ["tcr_est", tcr_estimate()],
            ["tcr_ar6_kappa", F2X / (LAM + 0.84)], ["T4x_eq", 2 * F2X / LAM],
            ["T4x_10", t4_10], ["T4x_100", t4_100], ["T4x_500", ab[-1][1]],
            ["Td4x_500", ab[-1][2]]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

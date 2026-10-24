"""The bedrock river of the upland west of the Varden Hills (Year 3,
quantitative geomorphology). Invented: the upland, its river, its drainage
areas, its uplift rate and the base-level fall. The outlet elevation is the
region model's river at the west edge of the map, region.river_z(0).

Stream-power incision E = K A^m S^n with n = 1, m = THETA; distance d
downstream from the divide; drainage area A = C_HACK d^H_HACK. With rock
uplift U relative to the outlet, the steady state has S = (U/K) A^-THETA, so
ks = U/K is the channel steepness index and
  z(d) = Z_OUT + ks C^-THETA (L^p - d^p)/p,   p = 1 - H_HACK THETA.
The integral chi(d) = int_d^L (A0/A)^THETA dd' turns the profile into a
straight line z = Z_OUT + ks A0^-THETA chi.

Base-level fall: at t = 0 the outlet drops by DROP. For n = 1 the
incision equation dz/dt = U + K A^m dz/dd is a kinematic wave moving
upstream at speed K A^m; the step keeps its height and reaches the point
d after the time chi(d) / (K A0^m). profile_at(t) is that exact solution;
upwind() integrates the equation numerically and is checked against it.

  part steady  d z S A                 steady profile (after the fall)
  part sa      A S                     slope-area 'measurements' (noisy)
  part fit     A S                     the fitted power law
  part knick   d z0 z1 z2 z3           profiles at the times TIMES (yr)
  part values  what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

L = 12000.0            # m, divide to outlet
D_HEAD = 300.0         # m, channel head
C_HACK, H_HACK = 4.5, 1.7
THETA = 0.5            # m/n, n = 1
U = 4.3e-5             # m/yr, the Varden denudation rate (Year 1 volume)
K = 1.0e-6             # 1/yr (m^(1 - 2m) with m = 0.5)
A0 = 1.0e6             # m^2, reference area of chi
Z_OUT = region.river_z(0.0)
DROP = 25.0            # m
T_FALL = 900000.0      # yr, the age used for the figures
TIMES = (0.0, 300000.0, 600000.0, 900000.0)
P = 1.0 - H_HACK * THETA
SEED = 18


def area(d):
    return C_HACK * np.asarray(d, dtype=float) ** H_HACK


def ks():
    return U / K


def slope_ss(d):
    return ks() * area(d) ** -THETA


def z_ss(d, z_out=Z_OUT, l_out=L):
    d = np.asarray(d, dtype=float)
    return z_out + ks() * C_HACK ** -THETA * (l_out ** P - d ** P) / P


def chi(d, l_out=L, c=C_HACK):
    d = np.asarray(d, dtype=float)
    return A0 ** THETA * c ** -THETA * (l_out ** P - d ** P) / P


def celerity(d):
    return K * area(d) ** THETA


def travel_time(d):
    return chi(d) / (K * A0 ** THETA)


def knick_position(t):
    """Distance from the divide reached by the knickpoint after t years."""
    chi_target = K * A0 ** THETA * t
    x = L ** P - chi_target * P * C_HACK ** THETA / A0 ** THETA
    return x ** (1.0 / P)


def profile_at(d, t, drop=DROP):
    """Exact n = 1 solution: the old profile above the knickpoint, the new
    one below. t = 0 gives the profile before the fall."""
    d = np.asarray(d, dtype=float)
    new = z_ss(d)
    if t <= 0:
        return new + drop
    dk = knick_position(t)
    return np.where(d < dk, new + drop, new)


def upwind(t_end, dd=10.0, drop=DROP):
    """First-order upwind solution of dz/dt = U - K A^m S from the old
    steady state, outlet held at Z_OUT; returns (d, z)."""
    d = np.arange(D_HEAD, L + dd / 2, dd)
    z = z_ss(d) + drop
    z[-1] = Z_OUT
    c = celerity(d)
    dt = 0.8 * dd / c.max()
    n = int(math.ceil(t_end / dt))
    dt = t_end / n
    for _ in range(n):
        z[:-1] = z[:-1] + dt * (U - c[:-1] * (z[:-1] - z[1:]) / dd)
        z[-1] = Z_OUT
    return d, z


def slope_area_samples(n=12, reach=200.0, sigma=0.10, seed=SEED):
    """Slopes over reaches of the steady profile, with a multiplicative
    noise; the reaches are log-spaced along the river and none crosses the
    knickpoint (above and below it the profile has the same steepness)."""
    rng = np.random.default_rng(seed)
    dmid = np.geomspace(800.0, L - 300.0, n)
    dk = knick_position(T_FALL)
    dmid = np.where(np.abs(dmid - dk) < reach, dmid + 2 * reach, dmid)
    a = area(dmid)
    s = (z_ss(dmid - reach / 2) - z_ss(dmid + reach / 2)) / reach
    s = s * np.exp(rng.normal(0.0, sigma, n))
    return a, s


def fit_power(a, s):
    """Least squares on log S = log ks - theta log A; returns (ks, theta)."""
    slope, icpt = np.polyfit(np.log10(a), np.log10(s), 1)
    return 10 ** icpt, -slope


def main():
    d = np.arange(D_HEAD, L + 1e-9, 50.0)
    write_table(__file__, ("d", "z", "S", "A"),
                [[x / 1000, z, s, a / 1e6] for x, z, s, a in zip(d, z_ss(d), slope_ss(d), area(d))],
                part="steady")
    a, s = slope_area_samples()
    write_table(__file__, ("A", "S"), [[x / 1e6, y] for x, y in zip(a, s)], part="sa", digits=4)
    k_fit, th_fit = fit_power(a, s)
    af = np.array([0.5e6, 60e6])
    write_table(__file__, ("A", "S"), [[x / 1e6, k_fit * x ** -th_fit] for x in af], part="fit")
    cols = [profile_at(d, t) for t in TIMES]
    write_table(__file__, ("d", "z0", "z1", "z2", "z3"),
                [[x / 1000] + [c[i] for c in cols] for i, x in enumerate(d)], part="knick")
    vals = [["ks_m", ks()], ["z_out", Z_OUT], ["z_head", float(z_ss(D_HEAD))],
            ["A_out_km2", float(area(L)) / 1e6], ["S_out", float(slope_ss(L))],
            ["celerity_out_m_yr", float(celerity(L))], ["ks_fit", k_fit], ["theta_fit", th_fit],
            ["chi_head", float(chi(D_HEAD))]]
    for t in TIMES[1:]:
        vals.append(["knick_d_%d" % t, knick_position(t)])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

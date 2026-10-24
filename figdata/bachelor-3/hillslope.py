"""Hillslope diffusion (Year 3, quantitative geomorphology).

Linear transport q = -KAPPA dz/dx with mass conservation gives the diffusion
equation dz/dt = KAPPA d2z/dx2 (+ U for rock uplift relative to base level).

Part scarp: the degradation of a scarp of half-offset A_SCARP on a far-field
slope B_FAR, from a vertical step at t = 0. The analytic solution is
z = A erf(x / (2 sqrt(KAPPA t))) + B x; an explicit finite-difference solver
(scarp_fd) reproduces it and is checked by the tests.

Part hill: steady ridges of half-width L_HILL lowering at E (equal to U), for
which the transport-limited, linear-diffusion steady state is the parabola
z = -E x^2 / (2 KAPPA): hilltop curvature -E/KAPPA.

KAPPA is invented for the Varden Hills, inside the range measured on
fault and shoreline scarps (ledger whipple04:scarp-kappa).

  part scarp   x z0 z1 z2 z3           profiles at the ages AGES (yr)
  part hill    x z1 z2 z3              steady hills for the rates RATES (m/yr)
  part values  what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

KAPPA = 5e-3            # m^2/yr
A_SCARP = 2.5           # m, half the vertical offset
B_FAR = 0.05            # far-field slope
AGES = (0.0, 2000.0, 10000.0, 40000.0)
L_HILL = 150.0          # m, divide to channel
RATES = (2.15e-5, 4.3e-5, 8.6e-5)   # m/yr; the middle one is the Varden rate


def scarp(x, t, a=A_SCARP, b=B_FAR, kappa=KAPPA):
    x = np.asarray(x, dtype=float)
    if t <= 0:
        return a * np.sign(x) + b * x
    s = 2.0 * math.sqrt(kappa * t)
    return a * np.vectorize(math.erf)(x / s) + b * x


def scarp_fd(t_end, half_width=60.0, dx=0.25, kappa=KAPPA):
    """Explicit FTCS solution from the vertical step, with the far-field
    slope held at both ends; returns (x, z)."""
    x = np.arange(-half_width, half_width + dx / 2, dx)
    z = scarp(x, 0.0)
    z[np.abs(x) < 1e-9] = 0.0
    dt = 0.4 * dx * dx / kappa
    n = int(math.ceil(t_end / dt))
    dt = t_end / n
    r = kappa * dt / dx / dx
    for _ in range(n):
        z[1:-1] = z[1:-1] + r * (z[2:] - 2 * z[1:-1] + z[:-2])
        z[0] = z[1] - B_FAR * dx
        z[-1] = z[-2] + B_FAR * dx
    return x, z


def max_slope(t, a=A_SCARP, b=B_FAR, kappa=KAPPA):
    """Slope at the scarp midpoint: a / sqrt(pi kappa t) + b."""
    return a / math.sqrt(math.pi * kappa * t) + b


def kappa_t_from_slope(smax, a=A_SCARP, b=B_FAR):
    return (a / (smax - b)) ** 2 / math.pi


def hill(x, e, kappa=KAPPA):
    return -e * np.asarray(x, dtype=float) ** 2 / (2 * kappa)


def hill_relief(e, length=L_HILL, kappa=KAPPA):
    return e * length * length / (2 * kappa)


def hill_fd(e, length=L_HILL, dx=1.0, kappa=KAPPA, t_end=None):
    """Hillslope from a flat surface, uplift e relative to channels held at
    x = +-length, run to steady state; returns (x, z)."""
    x = np.arange(-length, length + dx / 2, dx)
    z = np.zeros_like(x)
    dt = 0.4 * dx * dx / kappa
    t_end = t_end or 3.0 * length * length / kappa
    r = kappa * dt / dx / dx
    for _ in range(int(t_end / dt)):
        z[1:-1] = z[1:-1] + r * (z[2:] - 2 * z[1:-1] + z[:-2]) + e * dt
        z[0] = z[-1] = 0.0
    return x, z


def main():
    xs = np.arange(-40.0, 40.0 + 1e-9, 0.25)
    cols = [scarp(xs, t) for t in AGES]
    write_table(__file__, ("x", "z0", "z1", "z2", "z3"),
                [[x] + [c[i] for c in cols] for i, x in enumerate(xs)], part="scarp")
    xh = np.arange(-L_HILL, L_HILL + 1e-9, 2.0)
    cols = [hill(xh, e) + hill_relief(e) for e in RATES]
    write_table(__file__, ("x", "z1", "z2", "z3"),
                [[x] + [c[i] for c in cols] for i, x in enumerate(xh)], part="hill")
    vals = [["kappa_m2_yr", KAPPA]]
    for t in AGES[1:]:
        vals.append(["max_slope_%d" % t, max_slope(t)])
    for e in RATES:
        vals.append(["relief_%g" % e, hill_relief(e)])
        vals.append(["curv_%g" % e, -e / KAPPA])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

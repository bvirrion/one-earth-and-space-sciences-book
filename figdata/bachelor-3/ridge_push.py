"""Ridge-push force against the age of the sea floor (Year 3, mantle
convection), from the cooling models of the thermal-models chapter.

The force per unit length of ridge is the difference of the depth-integrated
lithostatic pressures of the column at the ridge (water to dr, then mantle at
Tm) and of the column of age t (water to dr + w, then the cooled plate, whose
density is rho_m (1 + alpha (Tm - T))), integrated from the sea surface to a
depth below which both pressures agree (isostasy):
    F = integral (P_ridge - P_t) dy.
For the half-space it is, in closed form,
    F = g rho_m alpha (Tm - T0) kappa t [1 + 2 rho_m alpha (Tm - T0) / (pi (rho_m - rho_w))].
Parameters: those of figdata/bachelor-3/plate_cooling.py (ledger honda04:gdh1),
g = 9.8 m/s2. Slab pull, for comparison: an excess density rho_m alpha Tm / 2
over a slab 95 km thick reaching 670 km (PREM discontinuity, ledger data:prem).

  part force  t hs pl    ridge push (1e12 N/m) vs age (Myr): half-space, plate
  part values what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _table import write_table  # noqa: E402
import plate_cooling as pc  # noqa: E402

G = 9.8
SLAB_DEPTH = 670e3


def hs_force(t_myr, tm=pc.TM, kappa=pc.KAPPA, alpha=pc.ALPHA):
    t = np.asarray(t_myr, dtype=float) * pc.MYR
    return G * pc.RHO_M * alpha * tm * kappa * t * (
        1 + 2 * pc.RHO_M * alpha * tm / (math.pi * (pc.RHO_M - pc.RHO_W)))


def numeric_force(temperature, zmax, n=40001):
    """Ridge push (N/m) for a column whose plate temperature is temperature(z),
    z below the sea floor, and which is isostatically compensated at depth."""
    z = np.linspace(0.0, zmax, n)
    deficit = np.trapezoid(pc.TM - temperature(z), z)
    w = pc.RHO_M * pc.ALPHA * deficit / (pc.RHO_M - pc.RHO_W)
    # depth y below the ridge's sea floor; the old column has water down to w
    # (a grid node sits exactly on the old sea floor, y = w, where the density jumps)
    yw = np.linspace(0.0, w, 201)
    rho_p = pc.RHO_M * (1 + pc.ALPHA * (pc.TM - temperature(z)))
    p_w = G * pc.RHO_W * yw
    p_p = p_w[-1] + G * np.concatenate([[0.0], np.cumsum((rho_p[1:] + rho_p[:-1]) / 2 * np.diff(z))])
    y = np.concatenate([yw, w + z[1:]])
    p_old = np.concatenate([p_w, p_p[1:]])
    p_ridge = G * pc.RHO_M * y
    return float(np.trapezoid(p_ridge - p_old, y)), float(p_ridge[-1] - p_old[-1])


def plate_force(t_myr):
    return numeric_force(lambda z: pc.plate_temperature(np.minimum(z, pc.L), t_myr), pc.L)[0]


def slab_pull(h=pc.L, depth=SLAB_DEPTH):
    return pc.RHO_M * pc.ALPHA * pc.TM / 2 * G * h * depth


if __name__ == "__main__":
    ts = np.concatenate([[0.5], np.arange(2.0, 160.01, 2.0)])
    write_table(__file__, ("t", "hs", "pl"),
                [(t, float(hs_force(t)) / 1e12, plate_force(t) / 1e12) for t in ts], part="force")
    vals = [("hs_50", float(hs_force(50.0))), ("hs_100", float(hs_force(100.0))),
            ("pl_100", plate_force(100.0)), ("pl_160", plate_force(160.0)),
            ("slab_pull", slab_pull()), ("ratio_slab_hs100", slab_pull() / float(hs_force(100.0)))]
    write_table(__file__, ("what", "value"), vals, part="values")

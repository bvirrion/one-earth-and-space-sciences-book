"""Glacial isostatic adjustment of a uniform viscous half-space (Year 3,
mantle convection).

A surface depression w = w_m cos(2 pi x / lambda), left by a melted load on a
half-space of viscosity eta and density rho, decays as exp(-t / tau) with
    tau = 4 pi eta / (rho g lambda).
The flow (z down, v downward velocity) is
    v = C (1 + kz) exp(-kz) cos kx,   u = C k z exp(-kz) sin kx,
    p = 2 eta C k exp(-kz) cos kx,    C = -rho g w_m / (2 eta k),  k = 2 pi / lambda.

Model choices of the chapter: rho = 3300 kg/m3, g = 9.8 m/s2; viscosities
1e20, 1e21, 1e22 Pa s spanning the ledger estimates (mitrovica96:haskell,
milne04:bifrost, zhao12:fenno); lambda = 3000 km for the decay curves.

  part decay   t f20 f21 f22   remaining fraction w/w_m against time (kyr)
  part tau     lam t20 t21 t22 relaxation time (kyr) against wavelength (km)
  part values  what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

RHO = 3300.0
G = 9.8
YR = 3.15576e7
ETAS = (1e20, 1e21, 1e22)
LAMBDA = 3000e3


def tau(eta, lam, rho=RHO, g=G):
    """Relaxation time (s)."""
    return 4 * math.pi * eta / (rho * g * lam)


def viscosity(tau_s, lam, rho=RHO, g=G):
    return tau_s * rho * g * lam / (4 * math.pi)


def flow(x, z, wm, eta, lam, rho=RHO, g=G):
    """Velocity (u, v) and pressure perturbation p of the relaxing half-space."""
    k = 2 * math.pi / lam
    c = -rho * g * wm / (2 * eta * k)
    e = np.exp(-k * z)
    u = c * k * z * e * np.sin(k * x)
    v = c * (1 + k * z) * e * np.cos(k * x)
    p = 2 * eta * c * k * e * np.cos(k * x)
    return u, v, p


def remaining(t_s, eta, lam, rho=RHO, g=G):
    return np.exp(-np.asarray(t_s, dtype=float) / tau(eta, lam, rho, g))


if __name__ == "__main__":
    ts = np.linspace(0.0, 20.0, 201)
    write_table(__file__, ("t", "f20", "f21", "f22"),
                [(t,) + tuple(float(remaining(t * 1e3 * YR, eta, LAMBDA)) for eta in ETAS) for t in ts],
                part="decay")
    lams = np.logspace(2, 4, 41)
    write_table(__file__, ("lam", "t20", "t21", "t22"),
                [(lam,) + tuple(tau(eta, lam * 1e3) / YR / 1e3 for eta in ETAS) for lam in lams],
                part="tau")
    vals = [("tau_kyr_eta%d_3000km" % round(math.log10(eta)), tau(eta, LAMBDA) / YR / 1e3) for eta in ETAS]
    vals += [("tau_kyr_eta21_1000km", tau(1e21, 1000e3) / YR / 1e3)]
    write_table(__file__, ("what", "value"), vals, part="values")

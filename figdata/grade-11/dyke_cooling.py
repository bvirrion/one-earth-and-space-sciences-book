"""Conductive cooling of a sheet of basaltic magma (a dyke or a sill), grade 11, igneous rocks.

Model (Delaney 1986, USGS Open-File Report 86-444; ledger delaney86:*): a sheet of
thickness b of basaltic magma intruded at 1150 degC into host rock at 50 degC; heat
leaves only by conduction, perpendicular to the sheet; the heat of crystallization,
900 MJ/m3, is released evenly between 1150 degC and the solidus, 950 degC. Constant
properties: heat capacity per unit volume 2.5 MJ/m3/K (Delaney: 2-3), diffusivity
1e-6 m2/s (England et al. 2007 Table 1; Delaney: 0.5-1e-6 for most rocks). The
equation dH/dt = k d2T/dx2 is solved with an explicit finite-difference scheme on the
enthalpy H(T), over half the sheet (the centre is a plane of symmetry) and a host
twenty half-thicknesses deep.

The sheet has solidified when its centre falls below the solidus. With constant
properties the problem has no length scale but b: the time grows as b squared.

  part times     b t_yr t0_yr        solidification time (years) with / without heat of crystallization
  part profiles  x T1 T2 T3 T4       temperature across a 20 m sheet at four times (x from the centre, m)
  part front     x t_day             time (days) at which each point of a 20 m sheet reaches the solidus
  part numbers   key value
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

T_MAGMA = 1150.0      # degC, intrusion temperature (Delaney's example)
T_SOLIDUS = 950.0     # degC
T_HOST = 50.0         # degC
RHO_C = 2.5e6         # J/m3/K
RHO_H = 900e6         # J/m3, heat of crystallization
KAPPA = 1.0e-6        # m2/s
YEAR = 3.156e7        # s
N_HALF = 40           # cells across half the sheet
HOST_FACTOR = 20      # host depth in half-thicknesses


def enthalpy(T, magma, latent=True):
    """Heat content per unit volume (J/m3), counted from 0 degC."""
    H = RHO_C * T
    if latent:
        frac = np.clip((T - T_SOLIDUS) / (T_MAGMA - T_SOLIDUS), 0.0, 1.0)
        H = H + np.where(magma, RHO_H * frac, 0.0)
    return H


def temperature(H, magma, latent=True):
    """Inverse of enthalpy()."""
    T = H / RHO_C
    if not latent:
        return T
    c_eff = RHO_C + RHO_H / (T_MAGMA - T_SOLIDUS)        # J/m3/K inside the melting interval
    H_s = RHO_C * T_SOLIDUS
    H_m = RHO_C * T_MAGMA + RHO_H
    mush = magma & (H > H_s) & (H <= H_m)
    hot = magma & (H > H_m)
    T = np.where(mush, T_SOLIDUS + (H - H_s) / c_eff, T)
    T = np.where(hot, (H - RHO_H) / RHO_C, T)
    return T


def cool(b, latent=True, snapshots=(), n_half=N_HALF, t_max_factor=3.0):
    """Cool a sheet of thickness b (m). Returns (t_solid_s, front, snaps).

    front: list of (x, t) at which each magma cell first falls to the solidus;
    snaps: {t_s: (x, T)} temperatures at the requested times (s)."""
    h = b / 2.0
    dx = h / n_half
    n = n_half * (1 + HOST_FACTOR)
    x = (np.arange(n) + 0.5) * dx
    magma = x < h
    T = np.where(magma, T_MAGMA, T_HOST)
    H = enthalpy(T, magma, latent)
    k = KAPPA * RHO_C
    dt = 0.4 * dx * dx / KAPPA
    t = 0.0
    t_front = np.full(n_half, np.nan)
    snaps = {}
    pending = sorted(snapshots)
    t_solid = None
    t_stop = t_max_factor * h * h / KAPPA * 10
    while t < t_stop:
        Tp = np.concatenate(([T[0]], T, [T_HOST]))          # symmetry at the centre, fixed far field
        H = H + dt * k * (Tp[2:] - 2 * T + Tp[:-2]) / (dx * dx)
        t += dt
        T = temperature(H, magma, latent)
        newly = np.isnan(t_front) & (T[:n_half] <= T_SOLIDUS)
        t_front[newly] = t
        while pending and t >= pending[0]:
            snaps[pending.pop(0)] = (x.copy(), T.copy())
        if t_solid is None and T[0] <= T_SOLIDUS:
            t_solid = t
        if t_solid is not None and not pending:
            break
    front = list(zip(x[:n_half], t_front))
    return t_solid, front, snaps


THICKNESSES = (1, 2, 5, 10, 20, 50, 100)
SNAP_DAYS = (30, 180, 365, 730)


def numbers():
    n = {}
    t20, front, _ = cool(20.0)
    t20_0, _, _ = cool(20.0, latent=False)
    n["t20_yr"] = t20 / YEAR
    n["t20_nolatent_yr"] = t20_0 / YEAR
    n["latent_factor"] = t20 / t20_0
    n["t2_day"] = cool(2.0)[0] / 86400
    n["t100_yr"] = cool(100.0)[0] / YEAR
    n["margin_day_20m"] = front[-1][1] / 86400            # outermost cell (dx/2 from the contact)
    n["quarter_day_20m"] = [t for x, t in front if x >= 5.0][0] / 86400
    n["c_eff"] = RHO_C + RHO_H / (T_MAGMA - T_SOLIDUS)
    return n


if __name__ == "__main__":
    rows = []
    for b in THICKNESSES:
        rows.append((b, cool(b)[0] / YEAR, cool(b, latent=False)[0] / YEAR))
    write_table(__file__, ("b", "t_yr", "t0_yr"), rows, part="times", digits=4)
    t20, front, snaps = cool(20.0, snapshots=[d * 86400 for d in SNAP_DAYS])
    keys = sorted(snaps)
    x = snaps[keys[0]][0]
    sel = x <= 30.0
    prof = [(-xi, *(snaps[k][1][i] for k in keys)) for i, xi in reversed(list(enumerate(x))) if sel[i]]
    prof += [(xi, *(snaps[k][1][i] for k in keys)) for i, xi in enumerate(x) if sel[i]]
    write_table(__file__, ("x", "T1", "T2", "T3", "T4"), prof, part="profiles", digits=5)
    write_table(__file__, ("x", "t_day"), [(xi, ti / 86400) for xi, ti in front], part="front", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)

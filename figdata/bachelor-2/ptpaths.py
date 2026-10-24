"""Thermobarometry and P-T-t paths (Year 2, pt-paths).

  gb        garnet-biotite Fe-Mg exchange thermometer, ideal mixing:
                3RT ln K_D = -(dH + P dV) + T dS          (Holdaway et al. 1997, eq. 2)
            K_D = (X_Mg/X_Fe)grt / (X_Mg/X_Fe)bt; dH, dS refitted here from the twelve
            Ferry and Spear (1978) brackets at 2070 bar listed in Holdaway et al. (1997),
            Table 1 (ledger h97:fs-data), dV = 0.311 J/bar (Berman 1988, ledger h97:dv).
            The fit gives dH = 52633 J, dS = 20.19 J/K (Holdaway et al. 1997, Table 2,
            ideal row: 52635, 20.20); the book prints and uses 52630 J and 20.19 J/K.
  gasp      3 anorthite = grossular + 2 kyanite + quartz, Koziol and Newton (1988):
            end-member line P0 = 22.80 T(C) - 1093 bar, dV = -6.210 J/bar (ledger kn88:gasp);
            with ideal activities a_grs = X_grs^3, a_an = X_an:
                P = P0 + R T ln(X_grs^3 / X_an^3) / 6.210.
  thick     one-dimensional conduction after instantaneous doubling of a 35-km crust by
            stacking (England and Thompson 1984, told; ledger et84:abstract), followed by
            erosion of 35 km. Material coordinates: the grid moves with the rock; erosion
            moves the surface (T = 0 C) down through the grid. Parameters (ledger
            delaney:conductivity, roy:granitic-k, vila:heat-production, prem:moho-average):
            k = 2.5 W/m/K, kappa = 1e-6 m2/s, crustal heat production 1.0 microW/m3,
            basal heat flow 25 mW/m2 at 200 km, initial steady geotherm; erosion starts
            30 Myr after thickening and removes 35 km in 70 Myr (0.5 mm/yr).
  series    three geothermal gradients drawn over the Al2SiO5 diagram (rho = 2800 kg/m3).

  part fs       T_C, lnKD of the Ferry-Spear brackets
  part gb       T_C for P = 0..12 kbar along isopleths of lnKD (columns per K_D)
  part gasp     P (kbar) against T for X_grs/X_an ratios
  part geo      depth (km), T at 0, 10, 30, 60 Myr after thickening
  part path     t (Myr), T_C, P_kbar, depth of the rock that starts at 35 km
  part series   T_C, P_kbar along 10, 25 and 60 C/km
  part values   what value
"""
import os
import sys

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

R = 8.31441
K = 273.15
G = 9.81
RHO = 2800.0

# Holdaway et al. (1997), Table 1: Ferry and Spear (1978) brackets at 2.07 kbar (T C, ln K_D)
FS78 = [(799, -1.157), (799, -1.255), (738, -1.265), (749, -1.330), (698, -1.341),
        (698, -1.355), (651, -1.464), (651, -1.493), (599, -1.624), (599, -1.734),
        (550, -1.738), (550, -1.826)]
FS_P = 2070.0
GB_DV = 0.311
GB_DH = 52630.0          # printed values (rounded fit)
GB_DS = 20.19
GASP_A, GASP_B, GASP_DV = 22.80, 1093.0, 6.210


def fs_fit():
    """least-squares fit 3R ln KD = -(dH + P dV)/T + dS; returns dH (J), dS (J/K)."""
    t = np.array([a + K for a, _ in FS78])
    y = np.array([b for _, b in FS78])
    s, i = np.polyfit(1.0 / t, y, 1)
    return -s * 3 * R - FS_P * GB_DV, i * 3 * R


def gb_t(lnkd, p_bar, dh=GB_DH, ds=GB_DS):
    """garnet-biotite temperature (K)."""
    return (dh + p_bar * GB_DV) / (ds - 3 * R * lnkd)


def gb_lnkd(t, p_bar, dh=GB_DH, ds=GB_DS):
    return (-(dh + p_bar * GB_DV) / t + ds) / (3 * R)


def gasp_p0(tc):
    return GASP_A * tc - GASP_B


def gasp_p(tc, xgrs, xan):
    """GASP pressure (bar) at T (C) with ideal activities."""
    return gasp_p0(tc) + R * (tc + K) * 3 * np.log(xgrs / xan) / GASP_DV


def intersect(lnkd, xgrs, xan):
    """T (C), P (bar) where the thermometer and the barometer agree."""
    tc = brentq(lambda tc: gb_t(lnkd, gasp_p(tc, xgrs, xan)) - K - tc, 200, 1200)
    return tc, gasp_p(tc, xgrs, xan)


# ---------------------------------------------------------------- thickening model
KCOND = 2.5
KAPPA = 1.0e-6
A_CRUST = 1.0e-6
Q_BASE = 0.025
H_CRUST = 35e3
ZMAX = 200e3
MYR = 3.15576e13


def steady(z):
    """initial steady geotherm (C) with uniform crustal heat production and basal flux."""
    q0 = Q_BASE + A_CRUST * H_CRUST
    zc = np.minimum(z, H_CRUST)
    t = q0 * zc / KCOND - A_CRUST * zc ** 2 / (2 * KCOND)
    return t + np.where(z > H_CRUST, Q_BASE * (z - H_CRUST) / KCOND, 0.0)


def thicken(dz=250.0):
    """material grid (depth after thickening) and its temperature and heat production:
    the crust 0-35 km is stacked on a copy of itself; the mantle moves 35 km down."""
    z = np.arange(0.0, ZMAX + dz / 2, dz)
    zorig = np.where(z < H_CRUST, z, np.where(z < 2 * H_CRUST, z - H_CRUST, z - H_CRUST))
    t = steady(zorig)
    a = np.where(z < 2 * H_CRUST, A_CRUST, 0.0)
    return z, t, a


def run(delay=30.0, duration=70.0, t_end=110.0, dt=0.05, dz=250.0, keep=(0, 10, 30, 60),
        rock=35e3):
    """erosion of 35 km at a constant rate from `delay` for `duration` Myr. Returns the
    material grid, geotherms at the `keep` times (on present depth), and the rock path."""
    from scipy.linalg import solve_banded
    z, t, a = thicken(dz)
    n = len(z)
    rate = H_CRUST / duration                    # m per Myr
    r = KAPPA * dt * MYR / dz ** 2
    src = a / (KCOND / KAPPA) * dt * MYR
    ir = int(round(rock / dz))
    geo, path = {}, []
    steps = int(round(t_end / dt))
    for k in range(steps + 1):
        time = k * dt
        e = min(max(time - delay, 0.0), duration) * rate
        top = int(np.ceil(e / dz - 1e-9))
        if any(abs(time - g) < dt / 2 for g in keep):
            geo[int(round(time))] = (z[top:] - top * dz, t[top:].copy())
        depth = z[ir] - top * dz
        path.append((time, t[ir], RHO * G * depth / 1e8, depth / 1e3))
        if k == steps:
            break
        # backward Euler on nodes top..n-1, T = 0 at top, flux at the base
        m = n - top
        ab = np.zeros((3, m))
        ab[0, 1:] = -r
        ab[1, :] = 1 + 2 * r
        ab[2, :-1] = -r
        rhs = t[top:] + src[top:]
        ab[1, 0], ab[0, 1] = 1.0, 0.0
        rhs[0] = 0.0
        ab[2, -2] = -2 * r                       # ghost node: dT/dz = Q_BASE / k
        rhs[-1] += 2 * r * dz * Q_BASE / KCOND
        t[top:] = solve_banded((1, 1), ab, rhs)
        t[:top] = 0.0
    return geo, np.array(path)


def path_summary(path):
    i_t = int(np.argmax(path[:, 1]))
    i_p = int(np.argmax(path[:, 2]))
    return dict(t_peakT=path[i_t, 0], peakT=path[i_t, 1], p_at_peakT=path[i_t, 2],
                peakP=path[i_p, 2], t_at_peakP=path[i_p, 1])


if __name__ == "__main__":
    write_table(__file__, ("T_C", "lnKD"), FS78, part="fs")
    kds = (0.12, 0.15, 0.18, 0.21, 0.24)
    rows = []
    for p in np.arange(0.0, 12.01, 0.5):
        rows.append((p,) + tuple(gb_t(np.log(kd), p * 1e3) - K for kd in kds))
    write_table(__file__, ("P_kbar",) + tuple("kd%d" % round(100 * kd) for kd in kds), rows,
                part="gb")
    ratios = (0.15, 0.20, 0.25, 0.30)
    rows = [(tc,) + tuple(gasp_p(tc, rr, 1.0) / 1e3 for rr in ratios)
            for tc in np.arange(400.0, 801.0, 10.0)]
    write_table(__file__, ("T_C",) + tuple("r%d" % round(100 * rr) for rr in ratios), rows,
                part="gasp")
    geo, path = run()
    rows = []
    zs = np.arange(0.0, 80.01, 1.0)
    for zk in zs:
        row = [zk]
        for g in (0, 10, 30, 60):
            d, tt = geo[g]
            row.append(round(float(np.interp(zk * 1e3, d, tt)), 2) + 0.0)
        rows.append(tuple(row))
    write_table(__file__, ("z_km", "t0", "t10", "t30", "t60"), rows, part="geo")
    sel = path[::20]
    write_table(__file__, ("t_Myr", "T_C", "P_kbar", "z_km"),
                [tuple(round(float(x), 3) + 0.0 for x in r) for r in sel],
                part="path")
    rows = []
    for tc in np.arange(0.0, 901.0, 10.0):
        rows.append((tc,) + tuple(RHO * G * (tc - 10) / g / 1e5 if tc >= 10 else 0.0
                                  for g in (10.0, 25.0, 60.0)))
    write_table(__file__, ("T_C", "g10", "g25", "g60"), rows, part="series")
    dh, ds = fs_fit()
    s = path_summary(path)
    vals = [("fit_dH", dh), ("fit_dS", ds)] + [(k, v) for k, v in s.items()]
    write_table(__file__, ("what", "value"), vals, part="values")

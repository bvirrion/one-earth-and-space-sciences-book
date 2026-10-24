"""A model continental geotherm and the peridotite solidus (grade 11,
lithosphere-asthenosphere).

Lithosphere: steady heat conduction with a constant conductivity K and a heat
production that decreases exponentially with depth in the crust,
A(z) = A0 exp(-z/B), on top of a heat flow QM from below (the "reduced" heat flow):

    T(z) = T0 + QM z / K + A0 B^2 / K (1 - exp(-z/B)),
    surface gradient dT/dz(0) = (QM + A0 B) / K = Q0 / K.

Values (ledger): Q0 = 70.9 mW/m2, the mean continental heat flow (dd10:split);
QM = 0.8 HFU = 33.5 mW/m2 and B = 7.5 km, the eastern United States (roy:provinces);
K = 6.5 mcal/(cm s degC) = 2.72 W/(m K), the conductivity of the upper-crust layer
of the same models (roy:conductivity); T0 = 15 degC (planet:Earth.Tmean).
Asthenosphere: the mantle adiabat T = TP + G_AD z with TP = 1300 degC (the
'1300 degC adiabat' of porter:lab) and G_AD = 0.45 K/km (katsura10:adiabat, 0.4-0.5).
The base of the (thermal) lithosphere is where the conductive geotherm meets the
adiabat; below it the geotherm follows the adiabat.
Solidus: dry peridotite, T = a P^2 + b P + c with P in GPa (hirschmann:solidus),
valid 0-10 GPa; the pressure at a depth is the weight of the rock above it, with
the PREM densities (data:prem) and g = 9.82 m/s2 (earth:gmean).

  part geotherm  depth_km t_cond t_adiabat t_geotherm t_solidus   0-300 km
  part numbers   key value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

import prem_profiles  # noqa: E402

T0 = 15.0                     # degC
Q0 = 70.9e-3                  # W/m2
QM = 0.8 * 41.84e-3           # W/m2 (1 HFU = 1e-6 cal/cm2/s = 41.84 mW/m2)
B_KM = 7.5                    # km
K = 6.5e-3 * 4.184 * 100      # W/(m K) from 6.5 mcal/(cm s degC)
TP, G_AD = 1300.0, 0.45       # degC, K/km
SOL = (-5.104, 132.899, 1120.661)
G = 9.82


def a0():
    """Surface heat production (W/m3) that makes the surface heat flow Q0."""
    return (Q0 - QM) / (B_KM * 1e3)


def t_cond(z_km):
    z, b = z_km * 1e3, B_KM * 1e3
    return T0 + QM * z / K + a0() * b * b / K * (1 - math.exp(-z / b))


def surface_gradient():
    """degC per km at the surface, by finite difference."""
    return (t_cond(0.001) - t_cond(0.0)) / 0.001


def t_adiabat(z_km):
    return TP + G_AD * z_km


def lab_depth():
    """Depth (km) where the conductive geotherm meets the adiabat (bisection)."""
    lo, hi = 1.0, 400.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if t_cond(mid) < t_adiabat(mid):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def t_geotherm(z_km):
    return t_cond(z_km) if z_km <= lab_depth() else t_adiabat(z_km)


def pressure_gpa(z_km, rows=None):
    """Weight of the rock above, per unit area, with the PREM densities."""
    rows = rows or prem_profiles.prem()
    p, n = 0.0, 200
    for k in range(n):
        zm = (k + 0.5) * z_km / n
        p += prem_profiles.value_at(zm, 3, rows) * 1e3 * G * (z_km * 1e3 / n)
    return p / 1e9


def t_solidus(p_gpa):
    a, b, c = SOL
    return a * p_gpa * p_gpa + b * p_gpa + c


def closest_approach(rows=None):
    """(depth, solidus - geotherm) where the geotherm comes closest to melting, 0-300 km."""
    rows = rows or prem_profiles.prem()
    best = None
    for z in range(5, 301, 5):
        gap = t_solidus(pressure_gpa(z, rows)) - t_geotherm(float(z))
        if best is None or gap < best[1]:
            best = (z, gap)
    return best


def numbers():
    rows = prem_profiles.prem()
    lab = lab_depth()
    zc, gap = closest_approach(rows)
    return {"k_w_mk": K, "a0_uw_m3": a0() * 1e6, "qm_mw_m2": QM * 1e3,
            "surface_gradient_c_km": surface_gradient(), "q0_over_k_c_km": Q0 / K * 1e3,
            "t_moho40_c": t_cond(40.0), "lab_km": lab, "t_lab_c": t_cond(lab),
            "p100_gpa": pressure_gpa(100.0, rows), "solidus100_c": t_solidus(pressure_gpa(100.0, rows)),
            "solidus0_c": t_solidus(0.0), "closest_depth_km": zc, "closest_gap_c": gap,
            "t200_c": t_geotherm(200.0), "p300_gpa": pressure_gpa(300.0, rows)}


if __name__ == "__main__":
    rows = prem_profiles.prem()
    out = []
    for z in range(0, 301, 2):
        zf = float(z)
        out.append((zf, t_cond(zf), t_adiabat(zf), t_geotherm(zf), t_solidus(pressure_gpa(zf, rows))))
    write_table(__file__, ("depth_km", "t_cond", "t_adiabat", "t_geotherm", "t_solidus"), out,
                part="geotherm", digits=6)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

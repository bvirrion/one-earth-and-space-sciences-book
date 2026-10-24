"""Flow laws of quartz and olivine, the olivine deformation-mechanism map and
the quartz piezometer (Year 3, deformation mechanisms and shear zones).

General law:  strain rate = A sigma^n d^-m exp(-(E + P V) / (R T)),
sigma in MPa, grain size d in micrometres, A in s^-1 MPa^-n um^m.

  wet quartzite, dislocation creep (Gleason and Tullis 1995): n 4, E 223 kJ/mol,
      A 1.1e-4 (ledger lopez:flow-laws, Book 3)
  dry olivine, dislocation creep (Hirth and Kohlstedt 2003): n 3.5, E 530 kJ/mol,
      V 14 cm3/mol, A 1.1e5 (ledger azuma17:olivine)
  dry olivine, diffusion creep (same): n 1, m 3, E 375 kJ/mol, V 5 cm3/mol,
      A 10^9.2 (ledger azuma17:olivine)
  quartz piezometer (Stipp and Tullis 2003): D = 10^3.56 sigma^-1.26, D in um,
      sigma in MPa (ledger st03:piezometer)
  R = 8.314462618 J/mol/K (ledger codata:R, Book 3).

Model choices of the chapter: olivine at P = 1 GPa for the strain-rate
curves, and at T = 1100 C, P = 2 GPa for the map.

  part quartz     s r400 r500 r600        log10 strain rate vs stress (MPa), wet quartzite
  part olivine    s r900 r1100 r1300      the same, dry olivine dislocation creep, 1 GPa
  part mapcont    d s16 s14 s12 s10       stress (MPa) giving total strain rates 1e-16..1e-10
                                          /s against grain size (um), dry olivine, map T and P
  part mapbound   d s                     the boundary where both creep rates are equal
  part values     what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

R = 8.314462618
QTZ = dict(A=1.1e-4, n=4.0, m=0.0, E=223e3, V=0.0)
OL_DIS = dict(A=1.1e5, n=3.5, m=0.0, E=530e3, V=14e-6)
OL_DIF = dict(A=10 ** 9.2, n=1.0, m=3.0, E=375e3, V=5e-6)
PIEZO_K, PIEZO_P = 10 ** 3.56, 1.26
MAP_T, MAP_P = 1100.0 + 273.15, 2e9
CURVE_P = 1e9


def rate(law, sigma, t_k, p=0.0, d=1.0):
    """Strain rate (1/s) for stress sigma (MPa), temperature t_k (K), pressure p (Pa),
    grain size d (um)."""
    return (law["A"] * np.asarray(sigma, dtype=float) ** law["n"] * np.asarray(d, dtype=float) ** (-law["m"])
            * np.exp(-(law["E"] + p * law["V"]) / (R * t_k)))


def stress(law, edot, t_k, p=0.0, d=1.0):
    """Stress (MPa) for a strain rate edot (1/s)."""
    return (edot / (law["A"] * d ** (-law["m"]) * math.exp(-(law["E"] + p * law["V"]) / (R * t_k)))) ** (1 / law["n"])


def total_rate(sigma, d, t_k=MAP_T, p=MAP_P):
    return rate(OL_DIS, sigma, t_k, p) + rate(OL_DIF, sigma, t_k, p, d)


def stress_for_total(edot, d, t_k=MAP_T, p=MAP_P):
    lo, hi = -6.0, 6.0          # log10 MPa
    for _ in range(200):
        mid = (lo + hi) / 2
        if total_rate(10 ** mid, d, t_k, p) < edot:
            lo = mid
        else:
            hi = mid
    return 10 ** ((lo + hi) / 2)


def boundary_stress(d, t_k=MAP_T, p=MAP_P):
    """Stress at which dislocation and diffusion creep of dry olivine run equally fast."""
    a = OL_DIF["A"] * d ** (-OL_DIF["m"]) * math.exp(-(OL_DIF["E"] + p * OL_DIF["V"]) / (R * t_k))
    b = OL_DIS["A"] * math.exp(-(OL_DIS["E"] + p * OL_DIS["V"]) / (R * t_k))
    return (a / b) ** (1 / (OL_DIS["n"] - OL_DIF["n"]))


def piezometer_grain_size(sigma):
    return PIEZO_K * sigma ** (-PIEZO_P)


def piezometer_stress(d):
    return (PIEZO_K / d) ** (1 / PIEZO_P)


if __name__ == "__main__":
    s = np.logspace(0, 3, 61)
    write_table(__file__, ("s", "r400", "r500", "r600"),
                [(x,) + tuple(float(np.log10(rate(QTZ, x, tc + 273.15))) for tc in (400, 500, 600)) for x in s],
                part="quartz")
    write_table(__file__, ("s", "r900", "r1100", "r1300"),
                [(x,) + tuple(float(np.log10(rate(OL_DIS, x, tc + 273.15, CURVE_P))) for tc in (900, 1100, 1300))
                 for x in s], part="olivine")
    ds = np.logspace(1, 4, 61)
    write_table(__file__, ("d", "s16", "s14", "s12", "s10"),
                [(d,) + tuple(stress_for_total(10.0 ** -e, d) for e in (16, 14, 12, 10)) for d in ds],
                part="mapcont")
    write_table(__file__, ("d", "s"), [(d, boundary_stress(d)) for d in ds], part="mapbound")
    vals = [("qtz_stress_1e-14_400C", stress(QTZ, 1e-14, 673.15)),
            ("qtz_stress_1e-14_500C", stress(QTZ, 1e-14, 773.15)),
            ("ol_stress_1e-14_1100C_1GPa", stress(OL_DIS, 1e-14, 1373.15, CURVE_P)),
            ("map_boundary_1mm", boundary_stress(1000.0)),
            ("map_boundary_100um", boundary_stress(100.0)),
            ("piezo_D_at_50MPa", piezometer_grain_size(50.0)),
            ("piezo_sigma_at_20um", piezometer_stress(20.0))]
    write_table(__file__, ("what", "value"), vals, part="values")

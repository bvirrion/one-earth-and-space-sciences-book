"""Aluminium-26 (Year 2, planet-formation-meteorites): relative ages from 26Al/27Al and the
heating of a planetesimal by 26Al decay, neglecting heat loss (the centre of a body large
enough for conduction to be slow).

  ratio       R(t) = R0 exp(-t/tau),    R0 = 5.23e-5, tau = 1.035 Myr   (ledger lugaro:al26)
  rel. age    dt = tau ln(R0/R)
  heating     H(t) = H0 exp(-t/tau),    H0 = 1.9e-7 W/kg                (ledger gail:params)
  body accreted at t_a, adiabatic:  T(t) = T0 + (H0 tau / c) (exp(-t_a/tau) - exp(-t/tau))
  peak        T_peak(t_a) = T0 + (H0 tau / c) exp(-t_a/tau),  c = 837 J/(kg K), T0 = 250 K
  critical    t_a* = tau ln(H0 tau / (c (T_crit - T0)))      T_crit 750, 1200, 1700 K (gail:temps)
  diffusion   R* = sqrt(kappa tau), kappa = k / (rho c), k = 2.1 W/(m K), rho = 3300 kg/m3

  part ta<x>   t_Myr  T_K        (x = 15, 20, 25, 30: accretion at 1.5, 2, 2.5, 3 Myr)
  part peak    ta_Myr Tpeak_K
  part values  what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

YR = 3.15576e7            # s, Julian year
MYR = 1e6 * YR
TAU = 1.035 * MYR         # lugaro:al26 (mean life)
R0 = 5.23e-5              # lugaro:al26
H0 = 1.9e-7               # W/kg, gail:params
C = 837.0                 # J/(kg K), gail:params
T0 = 250.0                # K, gail:params
K_COND = 2.1              # W/(m K), gail:params
RHO = 3300.0              # kg/m3, gail:params
T_SINTER, T_FEFES, T_LIQ = 750.0, 1200.0, 1700.0   # gail:temps


def ratio(t):
    return R0 * math.exp(-t / TAU)


def relative_age(R):
    return TAU * math.log(R0 / R)


def energy_left(t_a):
    """J/kg still to be released by 26Al after t_a"""
    return H0 * TAU * math.exp(-t_a / TAU)


def temperature(t, t_a):
    if t < t_a:
        return float("nan")
    return T0 + H0 * TAU / C * (math.exp(-t_a / TAU) - math.exp(-t / TAU))


def peak(t_a):
    return T0 + energy_left(t_a) / C


def critical_time(T_crit):
    return TAU * math.log(H0 * TAU / (C * (T_crit - T0)))


def diffusion_radius():
    kappa = K_COND / (RHO * C)
    return math.sqrt(kappa * TAU)


if __name__ == "__main__":
    ts = [8.0 * i / 160 for i in range(161)]
    for ta in (1.5, 2.0, 2.5, 3.0):
        rows = [(t, temperature(t * MYR, ta * MYR)) for t in ts if t >= ta]
        write_table(__file__, ("t_Myr", "T_K"), rows, part="ta%02d" % int(round(ta * 10)))
    tas = [4.0 * i / 80 for i in range(81)]
    write_table(__file__, ("ta_Myr", "Tpeak_K"), [(t, peak(t * MYR)) for t in tas], part="peak")
    vals = [
        ("energy_per_kg_t0", energy_left(0)),
        ("dT_max_t0_K", energy_left(0) / C),
        ("t_sinter_Myr", critical_time(T_SINTER) / MYR),
        ("t_fefes_Myr", critical_time(T_FEFES) / MYR),
        ("t_liquidus_Myr", critical_time(T_LIQ) / MYR),
        ("peak_2.4Myr_K", peak(2.4 * MYR)),
        ("peak_0.8Myr_K", peak(0.8 * MYR)),
        ("peak_1.5Myr_K", peak(1.5 * MYR)),
        ("peak_2.5Myr_K", peak(2.5 * MYR)),
        ("peak_3.0Myr_K", peak(3.0 * MYR)),
        ("relage_1e-5_Myr", relative_age(1e-5) / MYR),
        ("diffusion_radius_km", diffusion_radius() / 1e3),
    ]
    write_table(__file__, ("what", "value"), vals, part="values")

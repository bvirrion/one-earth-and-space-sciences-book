"""Star formation (Year 2, ism-star-formation): Jeans mass and length, free-fall time,
sound speed and protostellar accretion rate, Kelvin--Helmholtz time, the temperature of a
dust grain in starlight, the phases of the interstellar medium, and the disc fractions of
young clusters with an exponential fit.

  Jeans mass    M_J = (5 k T / (G mu m_u))^(3/2) (3 / (4 pi rho))^(1/2)   (energy criterion,
                uniform sphere: 3 M k T / (mu m_u) < 3 G M^2 / (5 R))
  Jeans radius  R_J = (15 k T / (4 pi G mu m_u rho))^(1/2)
  free fall     t_ff = (3 pi / (32 G rho))^(1/2)
  accretion     Mdot = c_s^3 / G,  c_s = (k T / (mu m_u))^(1/2)
  KH time       t_KH = G M^2 / (R L)
  grain         T = (L / (16 pi sigma r^2))^(1/4)
  rho = mu m_u n, n the number density of free particles, mu = 2.33 (ledger kauffmann:mu).

  part jeans    n  MJ10 MJ20 MJ50        (n in cm-3, masses in solar masses)
  part tff      n  tff_Myr
  part phases   name Tlo Thi nlo nhi     (ISM phases, ledger ferriere:*)
  part discs    age frac err             (Haisch et al. 2001, ledger haisch:disc-fractions)
  part discfit  age frac                 (least-squares straight line through the first five)
  part values   what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

K_B = 1.380649e-23        # J/K, const:kB
G = 6.67430e-11           # const:G
M_U = 1.66053906892e-27   # kg, nist:u
SIGMA = 5.670374419e-8    # const:sigma
M_SUN = 1.9884e30         # kg, sun:mass
R_SUN = 6.957e8           # m, sun:R
L_SUN = 3.828e26          # W, sun:L
AU = 149597870700.0       # m, const:au
PC = 3.085677581e16       # m, iau:parsec
YR = 3.15576e7            # s, Julian year
MYR = 1e6 * YR
MU = 2.33                 # kauffmann:mu

# ISM phases (ferriere:molecular, cold-atomic, warm-atomic, warm-ionized, hot-ionized);
# single values given as "about" are drawn as a factor-of-two box around them.
PHASES = [
    ("molecular", 10.0, 20.0, 1e2, 1e6),
    ("cold-atomic", 50.0, 100.0, 20.0, 50.0),
    ("warm-atomic", 6000.0, 10000.0, 0.2, 0.5),
    ("warm-ionized", 8000.0 / 1.4, 8000.0 * 1.4, 0.2, 0.5),
    ("hot-ionized", 1e6 / 1.4, 1e6 * 1.4, 0.0065 / 1.4, 0.0065 * 1.4),
]

# Haisch, Lada & Lada (2001) Table 1: (age Myr, fraction, error)
DISCS = [(0.3, 0.85, 0.08), (1.5, 0.80, 0.05), (2.3, 0.65, 0.08),
         (3.2, 0.52, 0.10), (5.0, 0.12, 0.04), (30.0, 0.03, 0.03)]


def density(n_cm3, mu=MU):
    """Mass density (kg/m3) of n free particles per cm3."""
    return mu * M_U * n_cm3 * 1e6


def jeans_mass(T, n_cm3, mu=MU):
    rho = density(n_cm3, mu)
    return (5.0 * K_B * T / (G * mu * M_U)) ** 1.5 * (3.0 / (4.0 * math.pi * rho)) ** 0.5


def jeans_radius(T, n_cm3, mu=MU):
    rho = density(n_cm3, mu)
    return math.sqrt(15.0 * K_B * T / (4.0 * math.pi * G * mu * M_U * rho))


def free_fall(n_cm3, mu=MU):
    return math.sqrt(3.0 * math.pi / (32.0 * G * density(n_cm3, mu)))


def sound_speed(T, mu=MU):
    return math.sqrt(K_B * T / (mu * M_U))


def accretion_rate(T, mu=MU):
    """kg/s"""
    return sound_speed(T, mu) ** 3 / G


def kh_time(M, R, L):
    return G * M * M / (R * L)


def grain_temperature(r, L=L_SUN):
    return (L / (16.0 * math.pi * SIGMA * r * r)) ** 0.25


def snow_line(T_snow, L=L_SUN):
    """Radius where the grain temperature equals T_snow."""
    return math.sqrt(L / (16.0 * math.pi * SIGMA)) / T_snow ** 2


def centrifugal_radius(j, M):
    return j * j / (G * M)


def disc_fit(points=DISCS[:5]):
    """Least-squares straight line f = f0 - b t through the first five clusters (the
    form Haisch et al. fitted). Returns (f0, b, t0) with t0 = f0 / b the age at which the
    line reaches zero."""
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    slope = sxy / sxx
    f0 = my - slope * mx
    return f0, -slope, f0 / -slope


def logspace(a, b, k):
    return [10 ** (a + (b - a) * i / (k - 1)) for i in range(k)]


if __name__ == "__main__":
    ns = logspace(1, 7, 61)
    write_table(__file__, ("n", "MJ10", "MJ20", "MJ50"),
                [(n, jeans_mass(10, n) / M_SUN, jeans_mass(20, n) / M_SUN, jeans_mass(50, n) / M_SUN)
                 for n in ns], part="jeans")
    write_table(__file__, ("n", "tff_Myr"), [(n, free_fall(n) / MYR) for n in ns], part="tff")
    write_table(__file__, ("name", "Tlo", "Thi", "nlo", "nhi"), PHASES, part="phases")
    write_table(__file__, ("age", "frac", "err"), DISCS, part="discs")
    f0, b, t0 = disc_fit()
    write_table(__file__, ("age", "frac"), [(0.0, f0), (t0, 0.0)], part="discfit")
    vals = [
        ("MJ_10K_1e4_Msun", jeans_mass(10, 1e4) / M_SUN),
        ("MJ_10K_1e5_Msun", jeans_mass(10, 1e5) / M_SUN),
        ("RJ_10K_1e4_pc", jeans_radius(10, 1e4) / PC),
        ("tff_1e4_Myr", free_fall(1e4) / MYR),
        ("tff_1e5_Myr", free_fall(1e5) / MYR),
        ("cs_10K_kms", sound_speed(10) / 1e3),
        ("Mdot_10K_Msun_per_yr", accretion_rate(10) * YR / M_SUN),
        ("tKH_sun_Myr", kh_time(M_SUN, R_SUN, L_SUN) / MYR),
        ("Tgrain_1au", grain_temperature(AU)),
        ("snow_170K_au", snow_line(170.0) / AU),
        ("disc_f0", f0),
        ("disc_slope_per_Myr", b),
        ("disc_zero_Myr", t0),
        ("disc_half_Myr", (f0 - 0.5) / b),
    ]
    write_table(__file__, ("what", "value"), vals, part="values")

"""The solar nebula (Year 2, planet-formation-meteorites): minimum-mass solar nebula,
midplane temperature of a passive disc, temperature of grains in direct starlight, disc
mass inside a radius, snow-line radii, isolation mass of a planetary embryo.

  MMSN (ledger cy10:mmsn)      Sigma_g = 2200 (r/au)^-3/2 g/cm2,
                               Sigma_p = 33 Zrel (r/au)^-3/2 g/cm2, Zrel 0.33 / 0.78 / 1
  passive midplane (cy10:passive)  T = 120 (r/au)^-3/7 K
  grain in starlight (ch. 1)   T = (L / (16 pi sigma r^2))^(1/4)
  disc mass inside R           M(R) = 4 pi Sigma_1 r_1^2 (R/r_1)^(1/2)
  isolation mass (cy10:isolation)  M_iso = (2 pi b r^2 Sigma_p)^(3/2) / (3 M_star)^(1/2), b = 5

  part temp    r_au  T_mid  T_grain        (r from 0.1 to 100 au)
  part values  what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

G = 6.67430e-11           # const:G
SIGMA = 5.670374419e-8    # const:sigma
AU = 149597870700.0       # const:au
M_SUN = 1.9884e30         # sun:mass
L_SUN = 3.828e26          # sun:L
M_EARTH = 5.9722e24       # earth:mass
SIGMA_G1 = 2200.0         # g/cm2 at 1 au, cy10:mmsn
SIGMA_P1 = 33.0           # g/cm2 at 1 au for Zrel = 1
T1_PASSIVE = 120.0        # K at 1 au, cy10:passive
B_ISO = 5.0               # annulus width in Hill radii, cy10:isolation
T_WATER = 182.0           # K, lodders:phases (water ice)
T_METHANE = 41.0          # K, cy10:mmsn (methane ice sublimates above about 41 K)


def sigma_gas(r_au):
    """kg/m2"""
    return SIGMA_G1 * 10.0 * r_au ** -1.5


def sigma_solid(r_au, zrel):
    """kg/m2"""
    return SIGMA_P1 * zrel * 10.0 * r_au ** -1.5


def t_passive(r_au):
    return T1_PASSIVE * r_au ** (-3.0 / 7.0)


def r_passive(T):
    """radius (au) where the passive midplane reaches T"""
    return (T1_PASSIVE / T) ** (7.0 / 3.0)


def t_grain(r_au, L=L_SUN):
    return (L / (16.0 * math.pi * SIGMA * (r_au * AU) ** 2)) ** 0.25


def r_grain(T, L=L_SUN):
    return math.sqrt(L / (16.0 * math.pi * SIGMA)) / T ** 2 / AU


def disc_mass(R_au):
    """gas mass (kg) of the MMSN inside R (au), Sigma ~ r^-3/2"""
    return 4.0 * math.pi * sigma_gas(1.0) * AU ** 2 * math.sqrt(R_au)


def isolation_mass(r_au, zrel, m_star=M_SUN, b=B_ISO, factor=1.0):
    """kg; factor multiplies the MMSN solids"""
    r = r_au * AU
    s = factor * sigma_solid(r_au, zrel)
    return (2.0 * math.pi * b * r * r * s) ** 1.5 / math.sqrt(3.0 * m_star)


def logspace(a, b, k):
    return [10 ** (a + (b - a) * i / (k - 1)) for i in range(k)]


if __name__ == "__main__":
    rs = logspace(-1, 2, 61)
    write_table(__file__, ("r_au", "T_mid", "T_grain"),
                [(r, t_passive(r), t_grain(r)) for r in rs], part="temp")
    vals = [
        ("sigma_gas_1au_gcm2", sigma_gas(1) / 10),
        ("sigma_gas_5.2au_gcm2", sigma_gas(5.2) / 10),
        ("disc_mass_30au_Msun", disc_mass(30) / M_SUN),
        ("disc_mass_100au_Msun", disc_mass(100) / M_SUN),
        ("r_water_passive_au", r_passive(T_WATER)),
        ("r_methane_passive_au", r_passive(T_METHANE)),
        ("r_water_grain_au", r_grain(T_WATER)),
        ("Miso_1au_Mearth", isolation_mass(1, 0.33) / M_EARTH),
        ("Miso_2.5au_Mearth", isolation_mass(2.5, 0.33) / M_EARTH),
        ("Miso_5.2au_Mearth", isolation_mass(5.2, 1.0) / M_EARTH),
        ("Miso_5.2au_x3.5_Mearth", isolation_mass(5.2, 1.0, factor=3.5) / M_EARTH),
    ]
    write_table(__file__, ("what", "value"), vals, part="values")

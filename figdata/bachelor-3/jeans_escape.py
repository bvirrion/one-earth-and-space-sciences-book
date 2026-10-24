"""Jeans escape from the exobases of Venus, the Earth, Mars and Titan (Year 3,
planetary atmospheres).

At the exobase, radius r and temperature T, a gas of particles of mass m has the
thermal speed u = sqrt(2kT/m) and the escape parameter

    lambda = G M m / (k T r) = (v_esc / u)^2,

the ratio of the gravitational binding energy to kT. The Jeans flux of escaping
particles (number per unit area and time, exobase density n) is

    Phi = n u / (2 sqrt(pi)) (1 + lambda) exp(-lambda),

so that the fraction of the 'thermal' flux n u / (2 sqrt(pi)) that escapes is
(1 + lambda) exp(-lambda).

Data: masses and radii of the NASA fact sheets (nasa:venus, planet:Earth.mass,
nasa:mars, nasa:titan); exobase temperatures and altitudes of Gronoff et al. (2020,
gronoff:jeans-table, gronoff:exobases): Venus 290 K at 200 km, the Earth 800-1600 K
at 500 km (1000 K used), Mars 240-300 K at 200 km (270 K used), Titan 180 K at
about 1500 km. Constants CODATA 2022 (const:G, const:kB), atomic masses in u.

  part lambda   A Venus Earth Mars Titan EarthLo EarthHi   (mass number, -)
  part factor   lam f                                        escaping fraction
  part species  name A lambdaEarth fEarth                    H, D, He, O at the Earth
  part values   what value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

G = 6.67430e-11
KB = 1.380649e-23
U = 1.66053906892e-27  # atomic mass constant, kg

# name: (mass kg, radius km, exobase altitude km, exobase temperature K)
BODIES = {
    "Venus": (4.8673e24, 6051.8, 200.0, 290.0),
    "Earth": (5.97e24, 6378.1, 500.0, 1000.0),
    "Mars": (0.64169e24, 3389.5, 200.0, 270.0),
    "Titan": (1345.5e20, 2575.0, 1500.0, 180.0),
}
EARTH_T = (800.0, 1600.0)
SPECIES = (("H", 1.008), ("D", 2.014), ("He", 4.0026), ("O", 15.999))


def escape_parameter(mass, r_m, t, m_u):
    """lambda = G M m / (k T r), r in metres, m in u."""
    return G * mass * m_u * U / (KB * t * r_m)


def thermal_speed(t, m_u):
    return math.sqrt(2.0 * KB * t / (m_u * U))


def escape_velocity(mass, r_m):
    return math.sqrt(2.0 * G * mass / r_m)


def escaping_fraction(lam):
    """(1 + lambda) exp(-lambda): the Jeans flux over n u / (2 sqrt(pi))."""
    return (1.0 + lam) * math.exp(-lam)


def jeans_flux(n, t, m_u, lam):
    """Number of particles escaping per m2 and per second at the exobase."""
    return n * thermal_speed(t, m_u) / (2.0 * math.sqrt(math.pi)) * escaping_fraction(lam)


def body_lambda(name, m_u, t=None):
    mass, r, z, te = BODIES[name]
    return escape_parameter(mass, (r + z) * 1e3, te if t is None else t, m_u)


def main():
    masses = [0.5 + 0.25 * i for i in range(0, 199)]  # 0.5 ... 50 u
    rows = []
    for a in masses:
        rows.append((a, *[body_lambda(b, a) for b in BODIES],
                     body_lambda("Earth", a, EARTH_T[0]), body_lambda("Earth", a, EARTH_T[1])))
    write_table(__file__, ("A", *BODIES, "EarthLo", "EarthHi"), rows, part="lambda")
    lams = [0.1 * i for i in range(1, 401)]
    write_table(__file__, ("lam", "f"), [(x, escaping_fraction(x)) for x in lams], part="factor")
    sp = []
    for name, a in SPECIES:
        lam = body_lambda("Earth", a)
        sp.append((name, a, lam, escaping_fraction(lam)))
    write_table(__file__, ("name", "A", "lambdaEarth", "fEarth"), sp, part="species")
    vals = []
    for b, (mass, r, z, te) in BODIES.items():
        rm = (r + z) * 1e3
        vals += [[b + "_lamH", body_lambda(b, 1.008)],
                 [b + "_lamH2", body_lambda(b, 2.016)],
                 [b + "_lamO", body_lambda(b, 15.999)],
                 [b + "_vesc_exo", escape_velocity(mass, rm)],
                 [b + "_uH", thermal_speed(te, 1.008)],
                 [b + "_lamH_surface_r", escape_parameter(mass, r * 1e3, te, 1.008)]]
    vals += [["Titan_lamCH4", body_lambda("Titan", 16.043)],
             ["Titan_lamN2", body_lambda("Titan", 28.014)],
             ["Earth_lamH_800", body_lambda("Earth", 1.008, 800.0)],
             ["Earth_lamH_1600", body_lambda("Earth", 1.008, 1600.0)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

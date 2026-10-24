"""Steady conductive geotherms with radiogenic heat production (Year 1, heat-budget):
three continental geotherms, an oceanic one, and the mantle adiabat they merge into.

Continental model (the chapter's theorem): heat production A(z) = A0 exp(-z/D) in a
medium of uniform conductivity k, surface temperature T0, heat flow q_m from below:
  q(z) = q_m + A0 D exp(-z/D)                      (upward heat flow)
  T(z) = T0 + q_m z / k + (A0 D^2 / k) (1 - exp(-z/D))
  q0 = q_m + A0 D                                  (the linear heat-flow relation)
with k = 2.5 W/m/K (within 1.5-3 for most rocks, ledger delaney:conductivity), D = 10 km (ledger
roy:provinces), A0 = 2.5 microW/m3 (granite median, ledger vila:heat-production), and
q_m = 15, 30, 45 mW/m2, i.e. q0 = 40, 55, 70 mW/m2. A uniform k down to 250 km is the
textbook simplification; the conductive branch is followed down to where it meets the
adiabat (the base of the thermal lithosphere), then the adiabat.

Adiabat (ledger katsura:adiabat): 1646 K at 50 km with a gradient of 0.54 K/km,
decreasing linearly to 0.36 K/km at 410 km; above 50 km the 0.54 K/km gradient,
which extrapolates to the potential temperature (1350 degC at the surface).

Oceanic geotherm (told): half-space cooling of 60-Myr-old lithosphere, with the
adiabat as the interior temperature: T = T0 + (T_ad(z) - T0) erf(z / (2 sqrt(kappa t))),
kappa = 1e-6 m2/s (ledger england:kelvin, Table 1).

  part continental  depth T15 T30 T45 Tc15 Tc30 Tc45   T: conductive then adiabat;
                                                       Tc: conductive branch only
                                                       (nan beyond 250 km)
  part oceanic      depth T
  part adiabat      depth T
  part isotherms    age z400 z800 z1200     depth (km) of the 400, 800 and 1200 degC
                                           isotherms of a half-space cooled from
                                           T_M = 1350 degC, against age (Myr)
  part values       what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

T0 = 10.0            # degC, surface temperature
K = 2.5              # W/m/K
D = 10e3             # m
A0 = 2.5e-6          # W/m3
QMS = (15e-3, 30e-3, 45e-3)   # W/m2, heat flow from below
KAPPA = 1e-6         # m2/s
YEAR = 3.15576e7     # s (Julian year)
OCEAN_AGE = 60.0     # Myr
Z_MAX = 250e3        # m

# adiabat (Katsura 2022)
T50 = 1646.0 - 273.15     # degC at 50 km
G50, G410 = 0.54e-3, 0.36e-3   # K/m


def surface_heat_flow(qm, a0=A0, d=D):
    return qm + a0 * d


def heat_flow(z, qm, a0=A0, d=D):
    return qm + a0 * d * math.exp(-z / d)


def t_conductive(z, qm, a0=A0, d=D, k=K, t0=T0):
    return t0 + qm * z / k + a0 * d * d / k * (1.0 - math.exp(-z / d))


def t_uniform_layer(z, q0, a, h, k=K, t0=T0):
    """Uniform production a in 0 < z < h, none below (the chapter's proposition)."""
    if z <= h:
        return t0 + q0 * z / k - a * z * z / (2.0 * k)
    th = t0 + q0 * h / k - a * h * h / (2.0 * k)
    return th + (q0 - a * h) * (z - h) / k


def adiabat_gradient(z):
    if z <= 50e3:
        return G50
    if z >= 410e3:
        return G410
    return G50 + (G410 - G50) * (z - 50e3) / 360e3


def t_adiabat(z):
    """Integral of the gradient from 50 km (closed form for the linear part)."""
    if z <= 50e3:
        return T50 - G50 * (50e3 - z)
    zz = min(z, 410e3)
    s = (G410 - G50) / 360e3
    dz = zz - 50e3
    t = T50 + G50 * dz + 0.5 * s * dz * dz
    if z > 410e3:
        t += G410 * (z - 410e3)
    return t


def potential_temperature():
    return t_adiabat(0.0)


def lithosphere_base(qm, a0=A0, d=D):
    """Depth (m) where the conductive geotherm meets the adiabat (bisection)."""
    f = lambda z: t_conductive(z, qm, a0, d) - t_adiabat(z)
    a, b = 1e3, 600e3
    for _ in range(200):
        c = 0.5 * (a + b)
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return 0.5 * (a + b)


def t_continental(z, qm):
    return t_conductive(z, qm) if z <= lithosphere_base(qm) else t_adiabat(z)


def t_oceanic(z, age_myr=OCEAN_AGE):
    t = age_myr * 1e6 * YEAR
    return T0 + (t_adiabat(z) - T0) * math.erf(z / (2.0 * math.sqrt(KAPPA * t)))


def halfspace_surface_flux(dt, age_myr, k=3.0, kappa=KAPPA):
    """k dT / sqrt(pi kappa t), W/m2 (Kelvin's and the ocean floor's formula)."""
    return k * dt / math.sqrt(math.pi * kappa * age_myr * 1e6 * YEAR)


T_M = 1350.0         # degC, interior temperature of the cooling half-space (isotherms)


def erfinv(y):
    """Inverse error function on [0, 1) by bisection."""
    a, b = 0.0, 6.0
    for _ in range(200):
        c = 0.5 * (a + b)
        if math.erf(c) < y:
            a = c
        else:
            b = c
    return 0.5 * (a + b)


def isotherm_depth(temp, age_myr, tm=T_M, t0=T0, kappa=KAPPA):
    """Depth (m) of an isotherm in a half-space cooled from tm for age_myr."""
    t = age_myr * 1e6 * YEAR
    return 2.0 * math.sqrt(kappa * t) * erfinv((temp - t0) / (tm - t0))


def numeric_geotherm(qm, a0=A0, d=D, k=K, n=2000, zmax=100e3):
    """Integrate dT/dz = q/k, dq/dz = -A(z) from the surface (q upward, z downward)
    with fourth-order Runge-Kutta, independently of the closed form; returns
    (T, q) at zmax, for the test."""
    a = lambda z: a0 * math.exp(-z / d)
    f = lambda z, t, q: (q / k, -a(z))
    h = zmax / n
    z, t, q = 0.0, T0, surface_heat_flow(qm, a0, d)
    for _ in range(n):
        k1 = f(z, t, q)
        k2 = f(z + h / 2, t + h / 2 * k1[0], q + h / 2 * k1[1])
        k3 = f(z + h / 2, t + h / 2 * k2[0], q + h / 2 * k2[1])
        k4 = f(z + h, t + h * k3[0], q + h * k3[1])
        t += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        q += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        z += h
    return t, q


def kelvin_age(gradient, t0, kappa):
    """Age (s) of a half-space cooled from t0 with present surface gradient."""
    return t0 * t0 / (math.pi * kappa * gradient * gradient)


def perry_time_constant(lid, radius=6.4e6, kappa=KAPPA):
    """R L / (3 kappa): Perry's well-stirred interior under a conducting lid (s)."""
    return radius * lid / (3.0 * kappa)


if __name__ == "__main__":
    zs = [i * 1e3 for i in range(0, int(Z_MAX / 1e3) + 1)]
    rows = []
    for z in zs:
        row = [z / 1e3]
        row += [t_continental(z, qm) for qm in QMS]
        row += [t_conductive(z, qm) for qm in QMS]
        rows.append(tuple(row))
    write_table(__file__, ("depth", "T15", "T30", "T45", "Tc15", "Tc30", "Tc45"), rows,
                part="continental", digits=6)
    write_table(__file__, ("depth", "T"), [(z / 1e3, t_oceanic(z)) for z in zs],
                part="oceanic", digits=6)
    write_table(__file__, ("depth", "T"), [(z / 1e3, t_adiabat(z)) for z in zs],
                part="adiabat", digits=6)
    ages = [0.25 * i for i in range(0, 401)]
    write_table(__file__, ("age", "z400", "z800", "z1200"),
                [(a,) + tuple(isotherm_depth(tt, a) / 1e3 for tt in (400.0, 800.0, 1200.0))
                 for a in ages], part="isotherms", digits=6)
    vals = [("potential_temperature", potential_temperature())]
    for qm in QMS:
        tag = "%d" % round(qm * 1e3)
        vals += [("q0_" + tag, surface_heat_flow(qm) * 1e3),
                 ("T35_" + tag, t_conductive(35e3, qm)),
                 ("base_" + tag, lithosphere_base(qm) / 1e3),
                 ("Tbase_" + tag, t_adiabat(lithosphere_base(qm)))]
    vals += [("ocean_flux_60", halfspace_surface_flux(t_adiabat(0.0) - T0, OCEAN_AGE) * 1e3),
             ("kelvin_age_Ma", kelvin_age(0.02 * 5 / 9 / 0.3048, 3900.0, 1.2e-6) / YEAR / 1e6),
             ("z1200_100Myr", isotherm_depth(1200.0, 100.0) / 1e3),
             ("perry_tau_100_Gyr", perry_time_constant(100e3) / YEAR / 1e9)]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

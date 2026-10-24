"""Steady-state exhumation, the closure isotherm under topography and the
age--elevation relationship (Year 3, thrust belts and orogenic wedges).

1-D: rock rises at the speed v through a layer of thickness L, T = TS at the
mean surface (z = 0, depth z positive downward), T = TL at z = L; steady
state of dT/dt - v dT/dz = kappa d2T/dz2 gives
    T0(z) = TS + (TL - TS) (1 - exp(-Pe z / L)) / (1 - exp(-Pe)),  Pe = v L / kappa.
2-D, linearised: topography h(x) = H0 cos(k x) about the mean surface, surface
temperature TS - GAMMA h (lapse rate GAMMA). The perturbation
    theta = (G0 - GAMMA) H0 cos(k x) exp(-m z),  m = v/(2 kappa) + sqrt((v/(2 kappa))^2 + k^2),
with G0 = T0'(0), solves the steady equation and makes T = TS - GAMMA h on the
surface to first order. The closure isotherm (TC) lies at the elevation
    e(x) = -z_c + f h(x),   f = (G0 - GAMMA) exp(-m z_c) / T0'(z_c),
and a surface sample (vertical path, speed v) has the age (h - e) / v, so the
age--elevation slope is v / (1 - f), not v.

Parameters: L = 30 km, TS = 10 C, TL set for 30 C/km without erosion (ledger
earle:settings, Book 2), kappa = 1e-6 m2/s (england:kelvin, Book 3), lapse
rate 6.5 C/km (ussa76:layers, Book 1), TC = 65 C (apatite (U-Th)/He, middle of
50-80 C, ledger sueoka19:closure), wavelength 20 km, H0 = 1 km.

  part geotherm  z t03 t10 t30           1-D geotherms for v = 0.3, 1, 3 mm/yr
  part ages      h a03 a10 a30           elevation (km above mean) vs age (Myr)
  part iso       x h e03 e10 e30         topography and closure-isotherm elevation (km)
  part values    what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

SEC_PER_MYR = 3.15576e13
L = 30.0
TS = 10.0
GRAD = 30.0
TL = TS + GRAD * L
KAPPA = 1e-6 * SEC_PER_MYR / 1e6       # km^2 / Myr
GAMMA = 6.5
TC = 65.0
WAVELENGTH = 20.0
H0 = 1.0
RATES = (0.3, 1.0, 3.0)                # mm/yr = km/Myr


def peclet(v, l=L, kappa=KAPPA):
    return v * l / kappa


def geotherm(z, v, l=L, ts=TS, tl=TL, kappa=KAPPA):
    pe = peclet(v, l, kappa)
    if pe < 1e-9:
        return ts + (tl - ts) * np.asarray(z, dtype=float) / l
    return ts + (tl - ts) * (1.0 - np.exp(-pe * np.asarray(z, dtype=float) / l)) / (1.0 - math.exp(-pe))


def gradient(z, v, l=L, ts=TS, tl=TL, kappa=KAPPA):
    pe = peclet(v, l, kappa)
    if pe < 1e-9:
        return (tl - ts) / l
    return (tl - ts) * pe / l * math.exp(-pe * z / l) / (1.0 - math.exp(-pe))


def closure_depth(v, tc=TC, l=L, ts=TS, tl=TL, kappa=KAPPA):
    pe = peclet(v, l, kappa)
    frac = (tc - ts) / (tl - ts)
    if pe < 1e-9:
        return frac * l
    return -l / pe * math.log(1.0 - frac * (1.0 - math.exp(-pe)))


def decay(v, wavelength=WAVELENGTH, kappa=KAPPA):
    k = 2.0 * math.pi / wavelength
    a = v / (2.0 * kappa)
    return a + math.sqrt(a * a + k * k)


def deflection(v, wavelength=WAVELENGTH, gamma=GAMMA, tc=TC):
    zc = closure_depth(v, tc)
    return (gradient(0.0, v) - gamma) * math.exp(-decay(v, wavelength) * zc) / gradient(zc, v)


def perturbation(x, z, v, h0=H0, wavelength=WAVELENGTH, gamma=GAMMA):
    k = 2.0 * math.pi / wavelength
    return (gradient(0.0, v) - gamma) * h0 * np.cos(k * x) * np.exp(-decay(v, wavelength) * z)


def isotherm_elevation(h, v, **kw):
    return -closure_depth(v) + deflection(v, **kw) * np.asarray(h, dtype=float)


def age(h, v, **kw):
    h = np.asarray(h, dtype=float)
    return (h - isotherm_elevation(h, v, **kw)) / v


def apparent_rate(v, **kw):
    return v / (1.0 - deflection(v, **kw))


if __name__ == "__main__":
    zs = np.linspace(0.0, 10.0, 201)
    write_table(__file__, ("z", "t03", "t10", "t30"),
                [(z,) + tuple(float(geotherm(z, v)) for v in RATES) for z in zs], part="geotherm")
    hs = np.linspace(-H0, H0, 41)
    write_table(__file__, ("h", "a03", "a10", "a30"),
                [(h,) + tuple(float(age(h, v)) for v in RATES) for h in hs], part="ages")
    xs = np.linspace(0.0, 2.0 * WAVELENGTH, 161)
    k = 2.0 * math.pi / WAVELENGTH
    rows = []
    for x in xs:
        h = H0 * math.cos(k * x)
        rows.append((x, h) + tuple(float(isotherm_elevation(h, v)) for v in RATES))
    write_table(__file__, ("x", "h", "e03", "e10", "e30"), rows, part="iso")
    vals = []
    for v in RATES:
        tag = f"{int(round(v * 10)):02d}"
        vals += [("Pe_" + tag, peclet(v)), ("G0_" + tag, gradient(0.0, v)),
                 ("zc_" + tag, closure_depth(v)), ("f_" + tag, deflection(v)),
                 ("vapp_" + tag, apparent_rate(v))]
    write_table(__file__, ("what", "value"), vals, part="values")

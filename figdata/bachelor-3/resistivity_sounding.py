"""Vertical electrical sounding over a layered ground (Year 3, field and lab methods III).

A point current source I on the surface of horizontal layers (resistivities rho_1..rho_n,
thicknesses h_1..h_(n-1), the last a half-space) gives the surface potential
V(r) = (I / 2 pi) * integral_0^inf T(lam) J0(lam r) dlam, with the resistivity transform
T from the bottom up (Pekeris recursion):
    T_n = rho_n,  T_i = (T_(i+1) + rho_i tanh(lam h_i)) / (1 + T_(i+1) tanh(lam h_i) / rho_i).
For a Schlumberger array with half-spacing s = AB/2 and a short MN, the apparent
resistivity is rho_a(s) = s^2 * integral_0^inf T(lam) lam J1(lam s) dlam, computed as
rho_1 + s^2 * integral (T - rho_1) lam J1(lam s) dlam: the difference decays like
exp(-2 lam h_1), so a plain quadrature on a fine grid converges. Tested against the
two-layer image series rho_a / rho_1 = 1 + 2 sum k^n (1 + (2 n h / s)^2)^(-3/2),
k = (rho_2 - rho_1) / (rho_2 + rho_1), and the Wenner series
rho_a / rho_1 = 1 + 4 sum k^n [(1 + (2nh/a)^2)^(-1/2) - (4 + (2nh/a)^2)^(-1/2)].

The Varden sounding (exercise model, not a measurement): on the alluvial floor of the
river over the granite (region.py: alluvium 6 m thick there), dry alluvium over the water
table, saturated alluvium, granite. Resistivities inside the published ranges (ledger
gpg:resistivity): dry gravel and sand RHO_DRY, unweathered igneous rock RHO_GRANITE;
the saturated layer from Archie's law (ledger keys:archie) with water RHO_W, porosity
PHI, a = 1, m = M_ARCHIE. The "field" values are the model at the stations multiplied
by a fixed pseudo-random factor (seeded; standard deviation NOISE), the way readings
scatter.

  part curves   s_over_h  k_m09 k_m06 k_m03 k_0 k_03 k_06 k_09    two-layer master curves
  part varden   s_m rho_model                                    the model curve
  part field    s_m rho_obs                                      the Varden readings
  part values   what value
"""
import math
import os
import sys

import numpy as np
from scipy.special import j1

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

RHO_DRY = 600.0          # ohm m, dry alluvial gravel and sand
H_DRY = 1.5              # m, depth of the water table below the floor
RHO_W = 20.0             # ohm m, the groundwater
PHI = 0.30               # porosity of the alluvium
M_ARCHIE = 2.0           # cementation exponent (a = 1)
H_ALLUVIUM = 6.0         # m, region.py
RHO_GRANITE = 20000.0    # ohm m
NOISE = 0.03             # relative scatter of the readings
SEED = 31
STATIONS = [1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 10.0, 15.0, 20.0, 30.0, 40.0, 60.0, 80.0, 100.0]


def archie(rho_w, phi, m=M_ARCHIE, a=1.0):
    """Archie's law: rho = a rho_w phi^-m (clean rock, fully saturated)."""
    return a * rho_w * phi ** (-m)


def archie_porosity(rho, rho_w, m=M_ARCHIE, a=1.0):
    return (a * rho_w / rho) ** (1.0 / m)


def varden_model():
    rho_sat = archie(RHO_W, PHI)
    return [RHO_DRY, rho_sat, RHO_GRANITE], [H_DRY, H_ALLUVIUM - H_DRY]


def transform(lam, rhos, hs):
    """Pekeris resistivity transform T(lambda)."""
    t = np.full_like(lam, rhos[-1], dtype=float)
    for rho, h in zip(reversed(rhos[:-1]), reversed(hs)):
        th = np.tanh(lam * h)
        t = (t + rho * th) / (1.0 + t * th / rho)
    return t


def schlumberger(s, rhos, hs, n=400000):
    """Apparent resistivity of a Schlumberger array of half-spacing s (short MN)."""
    lam_max = 40.0 / hs[0]                       # exp(-80): negligible beyond
    lam = np.linspace(0.0, lam_max, n + 1)[1:]
    dl = lam[1] - lam[0]
    f = (transform(lam, rhos, hs) - rhos[0]) * lam * j1(lam * s)
    integral = (f.sum() - 0.5 * f[-1]) * dl      # trapezoid; the integrand is 0 at lam = 0
    return rhos[0] + s * s * integral


def two_layer_schlumberger(s, rho1, rho2, h, nterms=4000):
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, nterms + 1)
    return rho1 * (1.0 + 2.0 * np.sum(k ** n * (1.0 + (2.0 * n * h / s) ** 2) ** -1.5))


def two_layer_wenner(a, rho1, rho2, h, nterms=4000):
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, nterms + 1)
    u = (2.0 * n * h / a) ** 2
    return rho1 * (1.0 + 4.0 * np.sum(k ** n * ((1.0 + u) ** -0.5 - (4.0 + u) ** -0.5)))


def k_wenner(a):
    return 2.0 * math.pi * a


def k_schlumberger(s, l):
    """Geometric factor of a Schlumberger array: AB/2 = s, MN/2 = l."""
    return math.pi * (s * s - l * l) / (2.0 * l)


def field_readings():
    rhos, hs = varden_model()
    rng = np.random.default_rng(SEED)
    f = 1.0 + NOISE * rng.standard_normal(len(STATIONS))
    return [(s, schlumberger(s, rhos, hs) * e) for s, e in zip(STATIONS, f)]


def main():
    ratios = np.logspace(-1, 2, 61)
    ks = (-0.9, -0.6, -0.3, 0.0, 0.3, 0.6, 0.9)
    rows = []
    for r in ratios:
        row = [r]
        for k in ks:
            rho2 = (1 + k) / (1 - k)
            row.append(two_layer_schlumberger(r, 1.0, rho2, 1.0))
        rows.append(row)
    write_table(__file__, ("s_over_h", "k_m09", "k_m06", "k_m03", "k_0", "k_03", "k_06", "k_09"),
                rows, part="curves")
    rhos, hs = varden_model()
    ss = np.logspace(0, 2, 41)
    write_table(__file__, ("s_m", "rho_model"), [(s, schlumberger(s, rhos, hs)) for s in ss],
                part="varden")
    obs = field_readings()
    write_table(__file__, ("s_m", "rho_obs"), obs, part="field", digits=4)
    vals = [["rho_dry", RHO_DRY], ["h_dry", H_DRY], ["rho_w", RHO_W], ["phi", PHI],
            ["m", M_ARCHIE], ["rho_sat", rhos[1]], ["h_sat", hs[1]], ["rho_granite", RHO_GRANITE],
            ["min_model", min(schlumberger(s, rhos, hs) for s in ss)],
            ["S_conductance", hs[0] / rhos[0] + hs[1] / rhos[1]]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

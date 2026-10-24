"""Equilibrium temperatures, the phase diagram of water and the habitable zone
(grade 10, habitable-planet).

Sources (ledger): solar irradiance and Bond albedo from the NASA fact sheets
(nasa:bond-albedos, earth:TSI, earth:albedo); mean temperatures and surface
pressures from the planetary fact sheet (planet:*.Tmean, planet:*.psurf,
nasa:mars-psurf); water phase boundaries from IAPWS SR1-86(1992) (vapour
pressure) and IAPWS R14-08(2011) (melting of ice Ih, sublimation)
(iapws:triple-critical, iapws:vapour-pressure, iapws:melt-subl); habitable
zone 0.99-1.70 au (kopparapu:hz-sun); Proxima Cen b (nea:proxima-b).

  part planets  name S_Wm2 albedo Teq_K Tmean_K greenhouse_K
  part vap      T_K p_bar           liquid-vapour curve, triple to critical point
  part subl     T_K p_bar           ice-vapour curve, 150 K to the triple point
  part melt     T_K p_bar           ice Ih-liquid curve, triple point to 2000 bar
  part points   name T_K p_bar      surface conditions of Venus, Earth, Mars
  part numbers  key value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

SIGMA = 5.670374419e-8          # const:sigma

# name: (solar irradiance W/m2, Bond albedo, mean surface temperature degC)
PLANETS = {
    "Mercury": (9082.7, 0.068, 167),
    "Venus": (2601.3, 0.77, 464),
    "Earth": (1361.0, 0.294, 15),
    "Moon": (1361.0, 0.11, -20),
    "Mars": (586.2, 0.250, -65),
}
SURFACE = {"Venus": (737.0, 92.0), "Earth": (288.0, 1.014), "Mars": (210.0, 0.00636)}

TT, PT = 273.16, 611.657            # triple point, K and Pa
TC, PC = 647.096, 22.064e6          # critical point, K and Pa
A_VAP = (-7.85951783, 1.84408259, -11.7866497, 22.6807411, -15.9618719, 1.80122502)
E_VAP = (1.0, 1.5, 3.0, 3.5, 4.0, 7.5)
A_MELT = (0.119539337e7, 0.808183159e5, 0.333826860e4)
B_MELT = (0.300000e1, 0.257500e2, 0.103750e3)
A_SUB = (-0.212144006e2, 0.273203819e2, -0.610598130e1)
B_SUB = (0.333333333e-2, 0.120666667e1, 0.170333333e1)

HZ_SUN = (0.99, 1.70)               # au: water loss, maximum greenhouse
PROXIMA_A = 0.04848                 # au
PROXIMA_LOGL = -2.82                # log10(L/Lsun)


def t_eq(S, albedo):
    """Equilibrium temperature (K) of a fast-rotating body: sigma T^4 = S(1-A)/4."""
    return (S * (1.0 - albedo) / (4.0 * SIGMA)) ** 0.25


def p_vap(T):
    """Liquid-vapour saturation pressure (Pa), IAPWS SR1-86(1992)."""
    tau = 1.0 - T / TC
    s = sum(a * tau ** e for a, e in zip(A_VAP, E_VAP))
    return PC * math.exp(TC / T * s)


def p_sub(T):
    """Ice Ih-vapour sublimation pressure (Pa), IAPWS R14-08(2011) Eq. (6)."""
    th = T / TT
    return PT * math.exp(sum(a * th ** b for a, b in zip(A_SUB, B_SUB)) / th)


def p_melt(T):
    """Ice Ih-liquid melting pressure (Pa), IAPWS R14-08(2011) Eq. (1), 251.165-273.16 K."""
    th = T / TT
    return PT * (1.0 + sum(a * (1.0 - th ** b) for a, b in zip(A_MELT, B_MELT)))


def boiling_T(p):
    """Temperature (K) at which the saturation pressure equals p (bisection)."""
    lo, hi = TT, TC
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if p_vap(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def planets():
    rows = []
    for name, (S, A, tc) in PLANETS.items():
        te = t_eq(S, A)
        rows.append((name, S, A, te, tc + 273.0, tc + 273.0 - te))
    return rows


def hz(lum):
    f = math.sqrt(lum)
    return HZ_SUN[0] * f, HZ_SUN[1] * f


def numbers():
    n = {r[0] + "_Teq": r[3] for r in planets()}
    n.update({r[0] + "_greenhouse": r[5] for r in planets()})
    L = 10 ** PROXIMA_LOGL
    n["proxima_L"] = L
    n["proxima_flux"] = L / PROXIMA_A ** 2
    n["proxima_Teq"] = t_eq(1361.0 * L / PROXIMA_A ** 2, 0.294)
    n["proxima_hz_in"], n["proxima_hz_out"] = hz(L)
    n["boil_1atm_C"] = boiling_T(101325.0) - 273.15
    n["boil_mars_C"] = boiling_T(636.0) - 273.15
    n["p_vap_20C"] = p_vap(293.15)
    n["p_sub_230K"] = p_sub(230.0)
    n["p_melt_260K"] = p_melt(260.0)
    n["earth_inverse_square_1au"] = 1361.0
    return n


if __name__ == "__main__":
    write_table(__file__, ("name", "S_Wm2", "albedo", "Teq_K", "Tmean_K", "greenhouse_K"), planets(), part="planets")
    vap = [(T, p_vap(T) / 1e5) for T in [TT + i * (TC - TT) / 120 for i in range(121)]]
    write_table(__file__, ("T_K", "p_bar"), vap, part="vap")
    sub = [(T, p_sub(T) / 1e5) for T in [150 + i * (TT - 150) / 80 for i in range(81)]]
    write_table(__file__, ("T_K", "p_bar"), sub, part="subl")
    melt = [(T, p_melt(T) / 1e5) for T in [TT - i * (TT - 251.165) / 60 for i in range(61)] if p_melt(T) / 1e5 <= 2000]
    write_table(__file__, ("T_K", "p_bar"), melt, part="melt")
    write_table(__file__, ("name", "T_K", "p_bar"), [(k, v[0], v[1]) for k, v in SURFACE.items()], part="points")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=7)

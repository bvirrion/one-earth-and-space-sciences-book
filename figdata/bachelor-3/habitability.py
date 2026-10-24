"""Habitable-zone limits and the surface phase diagram of water and methane (Year 3,
planetary atmospheres).

1. Habitable-zone limits of Kopparapu et al. (2013, arXiv:1301.6674v2, Table 3,
   kopparapu13:hz-fit): the stellar flux at the top of the atmosphere, relative to
   the Earth's today, at which an Earth-like planet reaches each limit,

       S_eff = S_eff_sun + a T* + b T*^2 + c T*^3 + d T*^4,   T* = T_eff - 5780 K,

   valid for 2600 <= T_eff <= 7200 K; the orbital distance of a limit is
   d = (L/L_sun / S_eff)^(1/2) au.

2. Phase boundaries: water (IAPWS vapour pressure above the triple point,
   iapws:vapour-pressure; sublimation of ice Ih below, iapws4:sublimation; triple and
   critical points, iapws:triple-critical) and methane (Antoine equation of Prydz and
   Goodwin 1972 fitted by NIST, 90.99-189.99 K, log10 p/bar = A - B/(T + C); triple
   and critical points of the NIST WebBook, nist:methane-phase).

3. Mean surface temperature and pressure of Venus, the Earth, Mars and Titan
   (planet:*.Tmean, planet:*.psurf, nasa:venus-atm, nasa:mars-atm, nasa:titan-surface).

  part hz       Teff rv rg mg maxg em            S_eff of the five limits
  part water    T p_bar                          liquid-vapour, triple -> critical
  part ice      T p_bar                          sublimation, 180 K -> triple
  part methane  T p_bar                          liquid-vapour, triple -> critical
  part bodies   name T p_bar
  part values   what value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

# Kopparapu et al. 2013, Table 3: S_eff_sun, a, b, c, d
HZ = {
    "rv": (1.7753, 1.4316e-4, 2.9875e-9, -7.5702e-12, -1.1635e-15),   # recent Venus
    "rg": (1.0512, 1.3242e-4, 1.5418e-8, -7.9895e-12, -1.8328e-15),   # runaway greenhouse
    "mg": (1.0140, 8.1774e-5, 1.7063e-9, -4.3241e-12, -6.6462e-16),   # moist greenhouse
    "maxg": (0.3438, 5.8942e-5, 1.6558e-9, -3.0045e-12, -5.2983e-16),  # maximum greenhouse
    "em": (0.3179, 5.4513e-5, 1.5313e-9, -2.7786e-12, -4.8997e-16),   # early Mars
}
T_SUN = 5780.0

TC, PC = 647.096, 22.064e6
A_VP = (-7.85951783, 1.84408259, -11.7866497, 22.6807411, -15.9618719, 1.80122502)
TT, PT = 273.16, 611.657
A_SUB = (-0.212144006e2, 0.273203819e2, -0.610598130e1)
B_SUB = (0.333333333e-2, 0.120666667e1, 0.170333333e1)

CH4_ANTOINE = (3.9895, 443.028, -0.49)  # bar, K; 90.99-189.99 K
CH4_TRIPLE = (90.67, 0.1169)   # K, bar
CH4_CRIT = (190.6, 46.1)       # K, bar

# mean surface temperature (K) and pressure (bar)
BODIES = (("Venus", 737.0, 92.0), ("Earth", 288.15, 1.0),
          ("Mars", 214.0, 0.00636), ("Titan", 94.15, 1.6))


def s_eff(limit, teff):
    s0, a, b, c, d = HZ[limit]
    t = teff - T_SUN
    return s0 + a * t + b * t ** 2 + c * t ** 3 + d * t ** 4


def hz_distance(limit, teff, lum):
    """Orbital distance (au) of a limit around a star of luminosity lum (L_sun)."""
    return math.sqrt(lum / s_eff(limit, teff))


def p_water(t):
    """Saturation pressure of water (Pa): over liquid above the triple point, over ice below."""
    if t >= TT:
        tau = 1.0 - t / TC
        a = A_VP
        s = (a[0] * tau + a[1] * tau ** 1.5 + a[2] * tau ** 3 + a[3] * tau ** 3.5
             + a[4] * tau ** 4 + a[5] * tau ** 7.5)
        return PC * math.exp(TC / t * s)
    th = t / TT
    return PT * math.exp(sum(a * th ** b for a, b in zip(A_SUB, B_SUB)) / th)


def p_methane(t):
    """Vapour pressure of liquid methane (bar), NIST Antoine fit."""
    a, b, c = CH4_ANTOINE
    return 10 ** (a - b / (t + c))


def main():
    teffs = [2600.0 + 50.0 * i for i in range(0, 93)]  # 2600 ... 7200 K
    write_table(__file__, ("Teff", *HZ),
                [(t, *[s_eff(k, t) for k in HZ]) for t in teffs], part="hz")
    tw = [TT + (TC - TT) * i / 200 for i in range(201)]
    write_table(__file__, ("T", "p_bar"), [(t, p_water(t) / 1e5) for t in tw], part="water")
    ti = [180.0 + (TT - 180.0) * i / 60 for i in range(61)]
    write_table(__file__, ("T", "p_bar"), [(t, p_water(t) / 1e5) for t in ti], part="ice")
    tm = [91.0 + (189.99 - 91.0) * i / 100 for i in range(101)]
    write_table(__file__, ("T", "p_bar"), [(t, p_methane(t)) for t in tm], part="methane")
    write_table(__file__, ("name", "T", "p_bar"), BODIES, part="bodies")
    vals = [[k + "_sun", s_eff(k, T_SUN)] for k in HZ]
    vals += [[k + "_dsun", hz_distance(k, T_SUN, 1.0)] for k in HZ]
    vals += [["ch4_94K", p_methane(94.15)], ["ch4_at_triple", p_methane(CH4_TRIPLE[0] + 0.32)],
             ["ch4_at_crit", p_methane(CH4_CRIT[0] - 0.61)],
             ["water_288", p_water(288.15)], ["water_214", p_water(214.0)],
             ["water_373", p_water(373.15)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

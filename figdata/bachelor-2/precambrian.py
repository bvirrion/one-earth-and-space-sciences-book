"""The Precambrian Earth (Year 2, precambrian-earth): radiogenic heat back in time, the
komatiite thermometer, a zero-dimensional energy-balance model with an ice--albedo feedback
(faint young Sun and snowball Earth), and the carbon dioxide build-up that ends a snowball.

  heat        bulk silicate Earth U 0.0203, Th 0.0795, K 240 ppm (ms95:pm-trace); heat per kg
              of isotope U-238 95.13, U-235 568.47, Th-232 26.28, K-40 28.47 microW/kg
              (Book 3 row dye:isotope-heat); half-lives and atom abundances (Book 3 row
              iaea:isotopes). Atom fractions become mass fractions with the mass numbers
              (U-238 against U-235, K-40 against the atomic weight 39.098 of K).
  komatiite   1-atm liquidus 1616 degC at 32.2 wt% MgO (Barberton 49J) and 1450 degC at
              23 wt% (Munro 422/95), so.16:liquidus; the line through them.
  ebm         C dT/dt = S/4 (1 - a(T)) - eps sigma T^4. Albedo a = 0.6 for a frozen planet
              (the snowball setting of hoffman17:models, within the 0.5-0.9 of ice and snow,
              nsidc:albedo-ice) below T1 = 263 K, today's 0.294 (earth:albedo) above
              T2 = 283 K, linear between (a MODEL CHOICE, said so in the text). The effective
              emissivity eps is set so that today's Earth (S0 = 1361 W/m2, earth:TSI) sits at
              288 K (earth:Tsurf). sigma from const:sigma.
  sun         Gough's law L/L0 = 1 / (1 + 0.4 (1 - t/t_sun)), t_sun = 4.567 Gyr (Book 2 rows
              gough81:luminosity, connelly12:cai).
  co2         mass of CO2 for a volume mixing ratio x added to today's air:
              x/(1-x) M_CO2/M_air M_atm (M_atm 5.1e18 kg, M_air 28.97 g/mol: earth:Matm,
              earth:Mmol; M_CO2 from ciaaw:abridged-2024); volcanic release 0.26 Gt/yr
              (usgs:volcanic-co2).

  part heat     t_Ga U238 U235 Th232 K40 total     (pW per kg of bulk silicate Earth)
  part ebm      T_K emit absS0 absP4               (W/m2: emitted; absorbed today, 4 Ga ago)
  part branch   s Tsnow Tmid Twarm                 (equilibria against S/S0, nan if absent)
  part kom      MgO T                              (the liquidus line)
  part numbers  key value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

# --- radiogenic heat ------------------------------------------------------------------
PPM = 1e-6
U, TH, K = 0.0203 * PPM, 0.0795 * PPM, 240.0 * PPM     # kg per kg of bulk silicate Earth
ISO = {  # name: (mass fraction of the element, heat W/kg of isotope, half-life Gyr)
    "U238": (0.992742 * 238 / (0.992742 * 238 + 0.007204 * 235), 95.13e-6, 4.468),
    "U235": (0.007204 * 235 / (0.992742 * 238 + 0.007204 * 235), 568.47e-6, 0.704),
    "Th232": (1.0, 26.28e-6, 14.0),
    "K40": (0.000117 * 40 / 39.098, 28.47e-6, 1.248),
}
ELEM = {"U238": U, "U235": U, "Th232": TH, "K40": K}


def lam(name):
    """Decay constant (1/Gyr)."""
    return math.log(2.0) / ISO[name][2]


def heat(name, t_ga=0.0):
    """Heat production of one isotope, W per kg of bulk silicate Earth, t_ga Gyr ago."""
    f, h, _ = ISO[name]
    return ELEM[name] * f * h * math.exp(lam(name) * t_ga)


def heat_total(t_ga=0.0):
    return sum(heat(n, t_ga) for n in ISO)


# --- komatiite thermometer -------------------------------------------------------------
K1, K2 = (32.2, 1616.0), (23.0, 1450.0)
SLOPE = (K1[1] - K2[1]) / (K1[0] - K2[0])          # degC per wt% MgO


def liquidus(mgo):
    return K1[1] + SLOPE * (mgo - K1[0])


# --- energy balance --------------------------------------------------------------------
SIGMA = 5.670374419e-8
S0, A_WARM, A_ICE, T_TODAY = 1361.0, 0.294, 0.6, 288.0
T1, T2 = 263.0, 283.0
EPS = S0 / 4 * (1 - A_WARM) / (SIGMA * T_TODAY ** 4)


def albedo(T):
    if T <= T1:
        return A_ICE
    if T >= T2:
        return A_WARM
    return A_ICE + (A_WARM - A_ICE) * (T - T1) / (T2 - T1)


def absorbed(T, s=1.0):
    return s * S0 / 4 * (1 - albedo(T))


def emitted(T, eps=EPS):
    return eps * SIGMA * T ** 4


def equilibria(s, eps=EPS):
    """Equilibrium temperatures (K) for sunlight s S0: (snowball, middle, warm), None if absent."""
    t_snow = (s * S0 * (1 - A_ICE) / (4 * eps * SIGMA)) ** 0.25
    t_warm = (s * S0 * (1 - A_WARM) / (4 * eps * SIGMA)) ** 0.25
    snow = t_snow if t_snow <= T1 else None
    warm = t_warm if t_warm >= T2 else None
    # the middle one, in the ramp: bisection on absorbed - emitted
    f = lambda T: absorbed(T, s) - emitted(T, eps)
    mid = None
    if f(T1) * f(T2) < 0:
        lo, hi = T1, T2
        for _ in range(80):
            m = 0.5 * (lo + hi)
            if f(lo) * f(m) <= 0:
                hi = m
            else:
                lo = m
        mid = 0.5 * (lo + hi)
    return snow, mid, warm


def s_freeze(eps=EPS):
    """Lowest sunlight (fraction of S0) at which the warm climate exists."""
    return 4 * eps * SIGMA * T2 ** 4 / (1 - A_WARM) / S0


def s_melt(eps=EPS):
    """Highest sunlight (fraction of S0) at which the snowball exists."""
    return 4 * eps * SIGMA * T1 ** 4 / (1 - A_ICE) / S0


def eps_to_melt(s):
    """Effective emissivity at which a snowball under sunlight s S0 reaches T1 and melts."""
    return s * S0 * (1 - A_ICE) / (4 * SIGMA * T1 ** 4)


def eps_for(T, s, a=A_WARM):
    return s * S0 * (1 - a) / (4 * SIGMA * T ** 4)


# --- faint young Sun -------------------------------------------------------------------
T_SUN = 4.567


def lum(ago):
    """Luminosity / today's, `ago` Gyr before present (Gough 1981)."""
    return 1.0 / (1.0 + 0.4 * (ago / T_SUN))


def ago_for_lum(l):
    return T_SUN * (1.0 / l - 1.0) / 0.4


# --- snowball CO2 ----------------------------------------------------------------------
M_ATM, M_AIR, M_CO2 = 5.1e18, 28.97, 12.011 + 2 * 15.999
F_VOLC = 0.26e12                                    # kg CO2 per year
G, R_EARTH = 9.820, 6371.0e3


def co2_mass(x):
    """Mass of CO2 (kg) that brings today's air to a volume mixing ratio x."""
    return x / (1 - x) * M_CO2 / M_AIR * M_ATM


def co2_time(x, flux=F_VOLC):
    """Years of volcanic release, with no sink, to reach the mixing ratio x."""
    return co2_mass(x) / flux


def one_bar_time(flux=F_VOLC):
    """Years to pile up a column of CO2 weighing 1 bar over the whole Earth."""
    return 1e5 * 4 * math.pi * R_EARTH ** 2 / G / flux


def numbers():
    h0, h3 = heat_total(0.0), heat_total(3.0)
    snow, mid, warm = equilibria(1.0)
    s4 = lum(4.0)
    d = {"eps": round(EPS, 4), "s_freeze": round(s_freeze(), 4), "s_melt": round(s_melt(), 4),
         "S_freeze": round(s_freeze() * S0, 1), "S_melt": round(s_melt() * S0, 1),
         "T_snow_today": round(snow, 1), "T_mid_today": round(mid, 1), "T_warm_today": round(warm, 1),
         "lum_4": round(s4, 4), "T_snow_4": round(equilibria(s4)[0], 1),
         "eps_warm_4": round(eps_for(T_TODAY, s4), 4),
         "ago_freeze": round(ago_for_lum(s_freeze()), 3),
         "eps_melt_094": round(eps_to_melt(0.94), 4),
         "forcing_melt_094": round(SIGMA * T1 ** 4 * (EPS - eps_to_melt(0.94)), 1),
         "H0_pW": round(h0 * 1e12, 3), "H3_pW": round(h3 * 1e12, 3), "H3_ratio": round(h3 / h0, 3),
         "H4_ratio": round(heat_total(4.0) / h0, 3),
         "slope": round(SLOPE, 3), "T_morb12": round(liquidus(12.0), 1),
         "dT_kom_morb": round(liquidus(32.2) - liquidus(12.0), 1),
         "co2_t001_Myr": round(co2_time(0.01) / 1e6, 3), "co2_t01_Myr": round(co2_time(0.1) / 1e6, 3),
         "one_bar_Myr": round(one_bar_time() / 1e6, 2), "M_CO2": round(M_CO2, 3)}
    for n in ISO:
        d["H0_%s" % n] = round(heat(n) * 1e12, 4)
        d["H3_%s" % n] = round(heat(n, 3.0) * 1e12, 4)
        d["frac_%s" % n] = float("%.5g" % ISO[n][0])
    return d


if __name__ == "__main__":
    ts = [0.05 * i for i in range(0, 92)]
    write_table(__file__, ("t_Ga", "U238", "U235", "Th232", "K40", "total"),
                [(round(t, 2),) + tuple(round(heat(n, t) * 1e12, 4) for n in ISO)
                 + (round(heat_total(t) * 1e12, 4),) for t in ts], part="heat")
    Ts = [215.0 + 0.5 * i for i in range(0, 181)]
    write_table(__file__, ("T_K", "emit", "absS0", "absP4"),
                [(T, round(emitted(T), 2), round(absorbed(T), 2), round(absorbed(T, lum(4.0)), 2))
                 for T in Ts], part="ebm")
    rows = []
    for i in range(0, 141):
        s = 0.70 + 0.005 * i
        e = equilibria(s)
        rows.append((round(s, 3),) + tuple(round(v, 2) if v is not None else "nan" for v in e))
    # the two tipping points, where two branches meet
    sf, sm = s_freeze(), s_melt()
    t_snow = lambda s: (s * S0 * (1 - A_ICE) / (4 * EPS * SIGMA)) ** 0.25
    t_warm = lambda s: (s * S0 * (1 - A_WARM) / (4 * EPS * SIGMA)) ** 0.25
    rows += [(round(sf, 4), round(t_snow(sf), 2), T2, T2), (round(sm, 4), T1, T1, round(t_warm(sm), 2))]
    rows.sort(key=lambda r: r[0])
    write_table(__file__, ("s", "Tsnow", "Tmid", "Twarm"), rows, part="branch")
    write_table(__file__, ("MgO", "T"), [(m, round(liquidus(m), 1)) for m in range(8, 35)],
                part="kom")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

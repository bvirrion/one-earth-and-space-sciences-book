"""Anthropogenic climate change (Year 2, anthropogenic-climate-change): the historical
effective radiative forcing, the energy-budget estimates of the climate response, the
warming per unit of cumulative CO2 emissions and the remaining carbon budget.

  erf       data/derived/bachelor-2-ar6-erf.csv (data:b4-ar6-erf, AR6 WG1 Annex III Table
            A3.3): W/m2 relative to 1750 for CO2, the other greenhouse gases (CH4, N2O,
            halogenated, ozone, stratospheric water vapour), aerosols, total anthropogenic
            with its 5-95 % range, and natural (volcanic + solar).
  tcre      warming above 1850-1900 against cumulative CO2 emissions since 1850 (GtCO2) for
            the AR6 TCRE, 0.45 degC per 1000 GtCO2, likely 0.27 to 0.63 (SPM D.1.1), drawn
            through the origin; the 2019 point, 2390 GtCO2 and 1.07 degC (SPM Table SPM.2).
  budget    the remaining carbon budget from the start of 2020 (GtCO2):
              B = (T_lim - T_hist - T_nonCO2) / TCRE - E_since - ESF (T_lim - T_hist)
            with T_hist = 1.07 degC (2010-2019 above 1850-1900), E_since = 210 GtCO2
            emitted 2015-2019 (the budget from T_hist starts at the middle of 2010-2019),
            ESF = 26 GtCO2 per degC of further warming for the Earth-system feedbacks not
            in the models (AR6 ch5 5.5.2.2.3-5 and 5.5.2.3).
  energy    the energy-budget estimate: lambda = (dN - dF) / dT, effective ECS = -F2x/lambda,
            TCR = F2x dT/dF with dN = 0.59, dF = 2.20 W/m2, dT = 1.03 degC between 1850-1900
            and 2006-2019, F2x = 3.93 W/m2 (AR6 ch7 7.5.2.1).
  planck    the Planck response (g - 1) 4 sigma T^3 of an Earth that emits (1 - g) sigma T^4
            to space, g the normalised greenhouse effect: 0.4 in AR6 (G = 159 W/m2 over the
            398 W/m2 emitted by the surface, ch7 7.4.2.1), T = 288 K.

  part erf      year co2 other_ghg aerosol anthro lo hi natural
  part tcre     E_GtCO2 dT_mid dT_lo dT_hi
  part numbers  key value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")

SIGMA = 5.670374419e-8       # W m-2 K-4 (const:sigma)
F2X = 3.93                   # W/m2, ERF of doubled CO2 (ipcc:erf-2xco2)
TCRE = 0.45                  # degC per 1000 GtCO2 (SPM D.1.1)
TCRE_LO, TCRE_HI = 0.27, 0.63
T_HIST = 1.07                # degC, 1850-1900 to 2010-2019
E_HIST = 2390.0              # GtCO2, 1850-2019
E_SINCE = 210.0              # GtCO2, 2015-2019
ESF = 26.0                   # GtCO2 per degC
M_C, M_CO2 = 12.011, 12.011 + 2 * 15.999   # g/mol (ciaaw:abridged-2024)


def read_erf():
    with open(os.path.join(DERIVED, "bachelor-2-ar6-erf.csv"), encoding="utf8") as f:
        return [{k: float(v) for k, v in r.items()} for r in csv.DictReader(f)]


def lambda_energy(dn, df, dt):
    """Net feedback parameter (W m-2 degC-1) from the energy balance dN = dF + lambda dT."""
    return (dn - df) / dt


def ecs(lam, f2x=F2X):
    return -f2x / lam


def tcr_energy(dt, df, f2x=F2X):
    return f2x * dt / df


def planck(g=0.4, t=288.0):
    """Planck response (W m-2 degC-1): d/dT of the outgoing (1 - g) sigma T^4."""
    return (g - 1.0) * 4.0 * SIGMA * t ** 3


def co2_forcing(c, c0=278.0, f2x=F2X):
    return f2x * math.log(c / c0, 2.0)


def budget(t_lim, t_nonco2, tcre=TCRE, t_hist=T_HIST, e_since=E_SINCE, esf=ESF):
    """Remaining carbon budget from the start of 2020 (GtCO2)."""
    dt = t_lim - t_hist
    return (dt - t_nonco2) / tcre * 1000.0 - e_since - esf * dt


def per_pgc(x_per_1000_gtco2):
    """degC per 1000 GtCO2 -> degC per 1000 PgC (1 PgC = M_CO2/M_C GtCO2)."""
    return x_per_1000_gtco2 * M_CO2 / M_C


def main():
    erf = read_erf()
    rows = [(int(r["year"]), r["co2"], r["other_ghg"], r["aerosol"], r["anthro"],
             r["anthro_p05"], r["anthro_p95"], r["volcanic"] + r["solar"]) for r in erf]
    write_table(__file__, ("year", "co2", "other_ghg", "aerosol", "anthro", "lo", "hi",
                           "natural"), rows, part="erf")

    rows = [(e, TCRE * e / 1000.0, TCRE_LO * e / 1000.0, TCRE_HI * e / 1000.0)
            for e in range(0, 4001, 250)]
    write_table(__file__, ("E_GtCO2", "dT_mid", "dT_lo", "dT_hi"), rows, part="tcre")

    last = erf[-1]
    lam = lambda_energy(0.59, 2.20, 1.03)
    nums = [
        ("erf2019_anthro", last["anthro"]), ("erf2019_p05", last["anthro_p05"]),
        ("erf2019_p95", last["anthro_p95"]), ("erf2019_co2", last["co2"]),
        ("erf2019_aerosol", last["aerosol"]), ("erf2019_other_ghg", last["other_ghg"]),
        ("erf_min_volcanic", min(r["volcanic"] for r in erf)),
        ("year_min_volcanic", min(erf, key=lambda r: r["volcanic"])["year"]),
        ("lambda_energy", lam), ("ecs_energy", ecs(lam)), ("tcr_energy", tcr_energy(1.03, 2.20)),
        ("ecs_process", ecs(-1.16)), ("planck", planck()),
        ("co2_forcing_2019", co2_forcing(410.0)),
        ("tcre_per_pgc", per_pgc(TCRE)), ("tcre_lo_pgc", per_pgc(TCRE_LO)),
        ("tcre_hi_pgc", per_pgc(TCRE_HI)),
        ("co2_warming_hist", TCRE * E_HIST / 1000.0),
        ("budget15_nonco2_01", budget(1.5, 0.1)), ("budget15_nonco2_02", budget(1.5, 0.2)),
        ("budget20_nonco2_01", budget(2.0, 0.1)), ("budget20_nonco2_02", budget(2.0, 0.2)),
    ]
    write_table(__file__, ("key", "value"), nums, part="numbers")


if __name__ == "__main__":
    main()

"""Calcite, water and carbon dioxide: open and closed systems, and a karst
spring degassing (Year 3, water-rock interaction).

Equilibrium constants: the analytical expressions of the USGS PHREEQC
database phreeqc.dat (ledger phreeqc:carbonate),
    log K = A1 + A2 T + A3/T + A4 log10 T + A5/T^2 + A6 T^2   (T in K),
for CaCO3 = Ca+2 + CO3-2 (Plummer and Busenberg 1982), CO3-2 + H+ = HCO3-,
CO3-2 + 2H+ = CO2 + H2O, CO2(g) = CO2 and H2O = OH- + H+. Hence
    K1 = [HCO3][H]/[CO2] = 10^(logK(HCO3) - logK(CO2)),  K2 = 10^-logK(HCO3).

Activity coefficients: the extended Debye-Hueckel equation of Hem (1985),
    -log gamma = A z^2 sqrt(I) / (1 + B a sqrt(I)),
A = 0.5085, B = 0.3281 (water at 25 C) and the ion sizes a of Hem's table 5
(ledger hem85:debye-huckel). A and B are kept at their 25 C values at every
temperature: Hem gives A from 0.4883 at 0 C to 0.5085 at 25 C, an effect he
calls relatively minor. Ion pairs (CaHCO3+, CaCO3 aq, CaSO4 aq) are
neglected, as in the chapter.

Open system: calcite and water at a fixed P_CO2. Closed system: water first
equilibrated with a gas at P_CO2 (no calcite), then sealed from the gas and
left to dissolve calcite; each Ca dissolved adds one carbon.

The spring of the weekend problem (invented, 10 C) is degassed at fixed Ca
and alkalinity (no precipitation) from its own P_CO2 to the air's
(427 ppm, the 2025 Mauna Loa annual mean, ledger data:co2-mlo, rounded to
log P = -3.37); the travertine is the calcite that must then precipitate to
bring the water back to saturation.

  part solubility  logp ca_open10 ca_open25 ca_closed10 ca_closed25   (mmol/L)
  part degassing   logp si ph                                          the spring at 10 C
  part ends        logp si                                             outlet and air end points
  part values      what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

ANALYTIC = {
    "calcite": (-67.87, -5.1813e-2, 0.0, 30.25746, 0.0, 0.0),
    "hco3": (107.8871, 0.03252849, -5151.79, -38.92561, 563713.9, 0.0),
    "co2aq": (464.1965, 0.09344813, -26986.16, -165.75951, 2248628.9, 0.0),
    "co2g": (10.5624, -2.3547e-2, -3972.8, 0.0, 5.8746e5, 1.9194e-5),
    "water": (293.29227, 0.1360833, -10576.913, -123.73158, 0.0, -6.996455e-5),
}
LOGK25 = {"calcite": -8.45, "hco3": 10.329, "co2aq": 16.681, "co2g": -1.468, "water": -14.0}

A_DH, B_DH = 0.5085, 0.3281
ION = {  # charge, ion size (angstrom), molar mass g/mol
    "Ca": (2, 6.0, 40.078), "Mg": (2, 8.0, 24.305), "Na": (1, 4.0, 22.990),
    "K": (1, 3.0, 39.098), "HCO3": (-1, 4.0, 61.017), "CO3": (-2, 5.0, 60.009),
    "Cl": (-1, 3.0, 35.453), "SO4": (-2, 4.0, 96.06), "NO3": (-1, 3.0, 62.004),
    "H": (1, 9.0, 1.008), "OH": (-1, 3.0, 17.007),
}
M_CACO3 = 100.09
LOGP_AIR = -3.37
CO2_PPM_2025 = 427.35

# the spring below the Varden limestone (invented; printed values, mg/L)
SPRING_T = 10.0
SPRING = {"Ca": 112.0, "Mg": 4.0, "Na": 7.0, "K": 1.2, "HCO3": 340.0, "Cl": 11.0,
          "SO4": 14.0, "NO3": 9.0}
SPRING_PH = 7.20


def log_k(name, t_c):
    a = ANALYTIC[name]
    T = t_c + 273.15
    return a[0] + a[1] * T + a[2] / T + a[3] * math.log10(T) + a[4] / T ** 2 + a[5] * T ** 2


def constants(t_c):
    """log10 of Kcal, K1, K2, KH, Kw at t_c."""
    lk_hco3 = log_k("hco3", t_c)
    return {
        "cal": log_k("calcite", t_c),
        "k1": lk_hco3 - log_k("co2aq", t_c),
        "k2": -lk_hco3,
        "kh": log_k("co2g", t_c),
        "kw": log_k("water", t_c),
    }


def gamma(ion, ionic_strength):
    z, a, _ = ION[ion]
    s = math.sqrt(ionic_strength)
    return 10 ** (-A_DH * z * z * s / (1 + B_DH * a * s))


def ionic_strength(molal):
    return 0.5 * sum(m * ION[i][0] ** 2 for i, m in molal.items())


def _bisect(f, lo, hi, n=200):
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


def open_system(logp, t_c, iters=30):
    """Calcite + water at fixed P_CO2: returns (Ca mol/L, pH)."""
    k = constants(t_c)
    a_co2 = 10 ** (k["kh"] + logp)
    I = 1e-3
    for _ in range(iters):
        g = {i: gamma(i, I) for i in ("Ca", "HCO3", "CO3", "H", "OH")}

        def balance(ph):
            ah = 10 ** -ph
            hco3 = 10 ** k["k1"] * a_co2 / ah / g["HCO3"]
            co3 = 10 ** k["k2"] * hco3 * g["HCO3"] / ah / g["CO3"]
            ca = 10 ** k["cal"] / (co3 * g["CO3"]) / g["Ca"]
            oh = 10 ** k["kw"] / ah / g["OH"]
            return 2 * ca + ah / g["H"] - hco3 - 2 * co3 - oh

        ph = _bisect(balance, 4.0, 12.0)
        ah = 10 ** -ph
        hco3 = 10 ** k["k1"] * a_co2 / ah / g["HCO3"]
        co3 = 10 ** k["k2"] * hco3 * g["HCO3"] / ah / g["CO3"]
        ca = 10 ** k["cal"] / (co3 * g["CO3"]) / g["Ca"]
        I = ionic_strength({"Ca": ca, "HCO3": hco3, "CO3": co3})
    return ca, ph


def open_cubic(logp, t_c, g_ca=1.0, g_hco3=1.0):
    """The closed form of the theorem: m_Ca = (K P / (4 g_Ca g_HCO3^2))^(1/3)."""
    k = constants(t_c)
    big_k = 10 ** (k["cal"] + k["k1"] + k["kh"] - k["k2"])
    return (big_k * 10 ** logp / (4 * g_ca * g_hco3 ** 2)) ** (1.0 / 3.0)


def initial_carbon(logp, t_c):
    """Carbon of pure water equilibrated with the gas (mol/L)."""
    k = constants(t_c)
    a_co2 = 10 ** (k["kh"] + logp)
    # pure water: H = HCO3 (+ OH); ionic strength tiny, gammas ~ 1
    ah = math.sqrt(10 ** k["k1"] * a_co2 + 10 ** k["kw"])
    return a_co2 + 10 ** k["k1"] * a_co2 / ah


def closed_system(logp, t_c, iters=30):
    """Water equilibrated with P_CO2, sealed, then calcite: returns (Ca, pH, log P_final)."""
    k = constants(t_c)
    c0 = initial_carbon(logp, t_c)
    I = 1e-3
    for _ in range(iters):
        g = {i: gamma(i, I) for i in ("Ca", "HCO3", "CO3", "H", "OH")}

        def state(ph):
            ah = 10 ** -ph
            # carbon fractions in terms of activities of CO2 (gamma 1)
            r1 = 10 ** k["k1"] / ah / g["HCO3"]          # HCO3/CO2 (molar)
            r2 = r1 * 10 ** k["k2"] * g["HCO3"] / ah / g["CO3"]  # CO3/CO2
            return ah, r1, r2

        def balance(ph):
            ah, r1, r2 = state(ph)
            # Ca from calcite saturation needs CO3; carbon conservation: C = c0 + Ca
            # unknowns: co2, ca. co3 = r2 co2; ca = Kcal/(g_ca g_co3 co3)
            # carbon: co2 (1 + r1 + r2) = c0 + ca  -> solve for co2 by inner bisection
            def cbal(lco2):
                co2 = 10 ** lco2
                ca = 10 ** k["cal"] / (g["Ca"] * g["CO3"] * r2 * co2)
                return co2 * (1 + r1 + r2) - c0 - ca
            co2 = 10 ** _bisect(cbal, -12.0, 0.0, 120)
            ca = 10 ** k["cal"] / (g["Ca"] * g["CO3"] * r2 * co2)
            oh = 10 ** k["kw"] / ah / g["OH"]
            return 2 * ca + ah / g["H"] - r1 * co2 - 2 * r2 * co2 - oh

        ph = _bisect(balance, 4.0, 12.0)
        ah, r1, r2 = state(ph)

        def cbal(lco2):
            co2 = 10 ** lco2
            ca = 10 ** k["cal"] / (g["Ca"] * g["CO3"] * r2 * co2)
            return co2 * (1 + r1 + r2) - c0 - ca
        co2 = 10 ** _bisect(cbal, -12.0, 0.0, 120)
        ca = 10 ** k["cal"] / (g["Ca"] * g["CO3"] * r2 * co2)
        I = ionic_strength({"Ca": ca, "HCO3": r1 * co2, "CO3": r2 * co2})
    return ca, ph, math.log10(co2) - k["kh"]


def molal(analysis_mgl):
    return {i: v / 1000.0 / ION[i][2] for i, v in analysis_mgl.items()}


def charge_balance(analysis_mgl):
    """(cations meq/L, anions meq/L, error %)."""
    m = molal(analysis_mgl)
    cat = sum(1000 * v * ION[i][0] for i, v in m.items() if ION[i][0] > 0)
    an = -sum(1000 * v * ION[i][0] for i, v in m.items() if ION[i][0] < 0)
    return cat, an, 100 * (cat - an) / (cat + an)


def spring_state(analysis=SPRING, ph=SPRING_PH, t_c=SPRING_T):
    """Ionic strength, gammas, DIC species, P_CO2 and SI of an analysed water."""
    k = constants(t_c)
    m = molal(analysis)
    I = ionic_strength(m)
    g = {i: gamma(i, I) for i in ION}
    ah = 10 ** -ph
    a_hco3 = m["HCO3"] * g["HCO3"]
    a_co2 = ah * a_hco3 / 10 ** k["k1"]
    a_co3 = 10 ** k["k2"] * a_hco3 / ah
    logp = math.log10(a_co2) - k["kh"]
    si = math.log10(m["Ca"] * g["Ca"] * a_co3) - k["cal"]
    return {"I": I, "g": g, "co2": a_co2, "co3": a_co3 / g["CO3"], "logp": logp, "si": si,
            "k": k}


def degas(logp, analysis=SPRING, ph0=SPRING_PH, t_c=SPRING_T, ca_loss=0.0):
    """Water of fixed Ca and alkalinity (less 2 x ca_loss mol/L of calcite
    precipitated) at P_CO2 = 10^logp: returns (SI, pH)."""
    k = constants(t_c)
    s0 = spring_state(analysis, ph0, t_c)
    m = molal(analysis)
    g = s0["g"]
    alk = m["HCO3"] + 2 * s0["co3"] - 2 * ca_loss
    ca = m["Ca"] - ca_loss
    a_co2 = 10 ** (k["kh"] + logp)

    def balance(ph):
        ah = 10 ** -ph
        hco3 = 10 ** k["k1"] * a_co2 / ah / g["HCO3"]
        co3 = 10 ** k["k2"] * hco3 * g["HCO3"] / ah / g["CO3"]
        oh = 10 ** k["kw"] / ah / g["OH"]
        return hco3 + 2 * co3 + oh - ah / g["H"] - alk

    ph = _bisect(balance, 3.0, 12.0)
    ah = 10 ** -ph
    hco3 = 10 ** k["k1"] * a_co2 / ah / g["HCO3"]
    co3 = 10 ** k["k2"] * hco3 * g["HCO3"] / ah / g["CO3"]
    si = math.log10(ca * g["Ca"] * co3 * g["CO3"]) - k["cal"]
    return si, ph


def travertine(logp=LOGP_AIR):
    """Calcite (mol/L) the degassed spring must precipitate to return to SI = 0."""
    return _bisect(lambda x: degas(logp, ca_loss=x)[0], 0.0, molal(SPRING)["Ca"] * 0.999)


def main():
    rows = []
    for lp in np.arange(-3.5, -0.99, 0.05):
        lp = round(float(lp), 2)
        rows.append([lp] + [1000 * f(lp, t)[0] for f in (open_system, closed_system)
                            for t in (10.0, 25.0)])
    # reorder columns: open10 open25 closed10 closed25
    write_table(__file__, ("logp", "ca_open10", "ca_open25", "ca_closed10", "ca_closed25"),
                rows, part="solubility")
    s = spring_state()
    rows = []
    for lp in np.arange(LOGP_AIR, s["logp"] + 1e-9, (s["logp"] - LOGP_AIR) / 60):
        si, ph = degas(float(lp))
        rows.append([float(lp), si, ph])
    write_table(__file__, ("logp", "si", "ph"), rows, part="degassing")
    write_table(__file__, ("logp", "si"), [[s["logp"], s["si"]], [LOGP_AIR, degas(LOGP_AIR)[0]]],
                part="ends")
    k10, k25 = constants(10.0), constants(25.0)
    cat, an, err = charge_balance(SPRING)
    x = travertine()
    vals = [["logKcal10", k10["cal"]], ["logKcal25", k25["cal"]],
            ["logK1_10", k10["k1"]], ["logK1_25", k25["k1"]],
            ["logK2_10", k10["k2"]], ["logK2_25", k25["k2"]],
            ["logKH10", k10["kh"]], ["logKH25", k25["kh"]],
            ["spring_I", s["I"]], ["spring_logp", s["logp"]], ["spring_si", s["si"]],
            ["cations_meq", cat], ["anions_meq", an], ["balance_pct", err],
            ["si_air", degas(LOGP_AIR)[0]], ["ph_air", degas(LOGP_AIR)[1]],
            ["travertine_mg", 1000 * M_CACO3 * x]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

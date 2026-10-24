"""Outgoing long-wave radiation of a moist grey atmosphere against surface
temperature: the plateau of the runaway greenhouse (Year 3, planetary atmospheres).

ILLUSTRATIVE MODEL, not a line-by-line calculation. An Earth-like planet (g = 9.81
m/s2) carries 1 bar of nitrogen and an ocean; its air is saturated with water vapour
at every level.

* Troposphere: the saturated (pseudo-)adiabat of nitrogen and water vapour, integrated
  upwards in the nitrogen partial pressure p_a,

      dlnT/dln p_a = (R_a/c_pa) (1 + L r/(R_a T)) /
                     (1 + (c_pv/c_pa + (L/(R_v T) - 1) L/(c_pa T)) r),

  r = (R_a/R_v) p_sat(T)/p_a the mass mixing ratio of vapour, until the temperature
  falls to T_STRAT; above, an isothermal stratosphere at T_STRAT whose vapour mixing
  ratio stays at its tropopause value.
* p_sat(T): the IAPWS vapour-pressure equation (iapws:vapour-pressure) above the
  triple point, the IAPWS sublimation equation of ice (iapws4:sublimation) below;
  L(T) = R_v T^2 dln p_sat/dT (Clausius-Clapeyron, ideal vapour), so that the profile
  is consistent with the saturation curve.
* Heat capacities of ideal gases by equipartition: c_p = (7/2) R/M for nitrogen,
  4 R/M for water vapour (const:R; molar masses 28.014 and 18.015 g/mol).
* Radiation: water vapour is the only absorber, grey, with a mass absorption
  coefficient that grows with pressure as collisions broaden the lines,
  kappa = KAPPA0 (p/P0)^(1/2), P0 = 1 bar; two-stream with the diffusivity factor
  D = 1.66:
  OLR = sigma Ts^4 exp(-tau_s) + int_0^tau_s sigma T^4 exp(-tau) dtau.

Once the surface is hot, the level where tau = 1 sits at a fixed vapour pressure on
the saturation curve, so its temperature, and the OLR, stop growing: the radiation
limit (Simpson, Komabayashi, Ingersoll, Nakajima). KAPPA0 is chosen so that the
plateau lies near the line-by-line limit of Kopparapu et al. (2013), 291 W/m2
(kopparapu13:runaway); a grey model can only mimic that number, not predict it.

  part olr     Ts olr                       K, W/m2
  part values  what value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

R = 8.314462618
SIGMA = 5.670374419e-8
M_A, M_V = 28.014e-3, 18.015e-3
R_A, R_V = R / M_A, R / M_V
CP_A, CP_V = 3.5 * R_A, 4.0 * R_V
G = 9.81
P_A_SURF = 1.0e5
T_STRAT = 200.0
KAPPA0 = 0.24  # m2/kg at P0, grey, illustrative
P0 = 1.0e5
DIFFUSIVITY = 1.66

# IAPWS vapour pressure over liquid water (Wagner and Pruss)
TC, PC = 647.096, 22.064e6
A_VP = (-7.85951783, 1.84408259, -11.7866497, 22.6807411, -15.9618719, 1.80122502)
# IAPWS sublimation pressure of ice Ih
TT, PT = 273.16, 611.657
A_SUB = (-0.212144006e2, 0.273203819e2, -0.610598130e1)
B_SUB = (0.333333333e-2, 0.120666667e1, 0.170333333e1)


def p_sat(t):
    if t >= TT:
        tau = 1.0 - t / TC
        a = A_VP
        s = (a[0] * tau + a[1] * tau ** 1.5 + a[2] * tau ** 3 + a[3] * tau ** 3.5
             + a[4] * tau ** 4 + a[5] * tau ** 7.5)
        return PC * math.exp(TC / t * s)
    th = t / TT
    return PT * math.exp(sum(a * th ** b for a, b in zip(A_SUB, B_SUB)) / th)


def latent_heat(t):
    """L = R_v T^2 dln p_sat/dT by a centred difference."""
    h = 1e-3 * t
    return R_V * t * t * (math.log(p_sat(t + h)) - math.log(p_sat(t - h))) / (2 * h)


def lapse(t, p_a):
    """dlnT/dln p_a on the saturated adiabat."""
    lh = latent_heat(t)
    r = (R_A / R_V) * p_sat(t) / p_a
    num = (R_A / CP_A) * (1.0 + lh * r / (R_A * t))
    den = 1.0 + (CP_V / CP_A + (lh / (R_V * t) - 1.0) * lh / (CP_A * t)) * r
    return num / den


def profile(ts, dlnp=0.004, p_a_top=1e-2):
    """Levels from the surface up: (p_total, T, q) with q the vapour mass fraction."""
    levels = []
    lnp = math.log(P_A_SURF)
    t = ts
    r_strat = None
    while lnp > math.log(p_a_top):
        p_a = math.exp(lnp)
        if r_strat is None:
            pv = p_sat(t)
            r = (R_A / R_V) * pv / p_a
        else:
            r = r_strat
            pv = r * p_a * R_V / R_A
        levels.append((p_a + pv, t, r / (1.0 + r)))
        if r_strat is None:
            # midpoint step in ln p_a (downwards)
            k1 = lapse(t, p_a)
            tm = t * math.exp(-0.5 * dlnp * k1)
            k2 = lapse(tm, p_a * math.exp(-0.5 * dlnp))
            t = t * math.exp(-dlnp * k2)
            if t <= T_STRAT:
                t = T_STRAT
                r_strat = (R_A / R_V) * p_sat(T_STRAT) / (p_a * math.exp(-dlnp))
        lnp -= dlnp
    return levels


def olr(ts, kappa0=KAPPA0):
    lev = profile(ts)
    # optical depth from the top down
    n = len(lev)
    tau = [0.0] * n
    for i in range(n - 2, -1, -1):
        p1, _, q1 = lev[i + 1]
        p0, _, q0 = lev[i]
        kappa = kappa0 * math.sqrt(0.5 * (p0 + p1) / P0)
        tau[i] = tau[i + 1] + DIFFUSIVITY * kappa * 0.5 * (q0 + q1) * (p0 - p1) / G
    out = SIGMA * ts ** 4 * math.exp(-tau[0])
    for i in range(n - 1):
        tm = 0.5 * (lev[i][1] + lev[i + 1][1])
        out += SIGMA * tm ** 4 * (math.exp(-tau[i + 1]) - math.exp(-tau[i]))
    return out


def main():
    ts_grid = [250.0 + 5.0 * i for i in range(0, 71)]  # 250 ... 600 K
    rows = [(ts, olr(ts)) for ts in ts_grid]
    write_table(__file__, ("Ts", "olr"), rows, part="olr")
    vals = [["olr_288", olr(288.0)], ["olr_350", olr(350.0)], ["olr_450", olr(450.0)],
            ["olr_600", olr(600.0)], ["olr_max", max(o for _, o in rows)],
            ["olr_250", olr(250.0)], ["olr_300", olr(300.0)], ["olr_400", olr(400.0)],
            ["L_280", latent_heat(280.0)], ["L_373", latent_heat(373.15)],
            ["psat_373", p_sat(373.15)], ["cp_a", CP_A], ["cp_v", CP_V]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

"""Saturation, the rising parcel, the condensation level and the warm dry wind
in the lee of a mountain (grade 10, why-clouds-form).

Sources (ledger): saturation pressure over water and over ice from IAPWS
SR1-86 and R14-08 (iapws:vapour-pressure, iapws:melt-subl; the functions are
imported from planet_temperatures.py); latent heat of vaporization at 0 and
15 degC (nist:water-latent), interpolated linearly in between and beyond;
molar gas constant (const:R), standard gravity (const:gn), mean molecular
weight of air (earth:Mmol), atomic weights of H and O (ciaaw:abridged-2024);
the standard-atmosphere lapse 6.49 degC/km (nasa:grc-atmosphere).

Physics used (admitted in the text): dry air as an ideal diatomic gas,
c_p = (7/2) R/M_d, so the dry adiabatic rate is g/c_p; a rising parcel keeps
its mixing ratio until saturation; above it, the pseudo-adiabatic rate
g (1 + L w_s/(R_d T)) / (c_p + L^2 w_s eps/(R_d T^2)).

The soundings are invented examples for the chapter (not measurements).

  part sat       T_C ws_gkg rho_gm3      saturation content at 1013.25 hPa
  part parcel    z_km T_C Td_C           the afternoon parcel (28 degC, dew point 16 degC)
  part dew       z_km Td_C               its dew point, ground to condensation level
  part envA      z_km T_C                afternoon sounding (unstable above the cloud base)
  part envB      z_km T_C                a stable sounding
  part numbers   key value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _table import write_table  # noqa: E402
from planet_temperatures import p_vap, p_sub  # noqa: E402

R = 8.314462618             # const:R
G = 9.80665                 # const:gn
M_D = 28.97e-3              # earth:Mmol, kg/mol
M_W = (2 * 1.0080 + 15.999) * 1e-3   # ciaaw:abridged-2024, kg/mol
RD, RV = R / M_D, R / M_W
EPS = RD / RV
CP = 3.5 * RD               # ideal diatomic gas
GAMMA_D = G / CP * 1000     # K/km
P0 = 101325.0
L0, L15 = 2500.9e3, 2465.5e3  # nist:water-latent at 273.16 K and 288.12 K
STD_LAPSE = 6.49            # nasa:grc-atmosphere, K/km


def latent(T):
    return L0 + (L15 - L0) * (T - 273.16) / (288.12 - 273.16)


def e_sat(T):
    """Saturation vapour pressure (Pa): over water at and above 0 degC, over ice below."""
    return p_vap(T) if T >= 273.15 else p_sub(T)


def e_sat_water(T):
    return p_vap(T)


def mixing_ratio(e, p):
    return EPS * e / (p - e)


def ws(T, p=P0):
    """Saturation mixing ratio (kg/kg) over water (the cloud droplets stay liquid well below 0 degC)."""
    return mixing_ratio(e_sat_water(T), p)


def dew_point(w, p):
    """Temperature (K) at which the mixing ratio w is saturating over water at pressure p (bisection)."""
    e = w * p / (EPS + w)
    lo, hi = 200.0, 330.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if e_sat_water(mid) > e:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def moist_rate(T, p):
    """Pseudo-adiabatic lapse rate (K/km)."""
    w = ws(T, p)
    L = latent(T)
    return G * (1 + L * w / (RD * T)) / (CP + L * L * w * EPS / (RD * T * T)) * 1000


def parcel(T0_C, Td0_C, z_top=8.0, dz=0.01, z0=0.0, p0=P0):
    """Lift a parcel from height z0 (km). Returns rows (z, T_C, Td_C, p) and the condensation level (km)."""
    T, p, z = T0_C + 273.15, p0, z0
    w = mixing_ratio(e_sat_water(Td0_C + 273.15), p0)
    rows, lcl = [], None
    while z <= z_top + 1e-9:
        if lcl is None:
            Td = dew_point(w, p)
            if T <= Td:
                lcl = z
        else:
            Td = T
        rows.append((z, T - 273.15, Td - 273.15, p))
        rate = GAMMA_D if lcl is None else moist_rate(T, p)
        T_new = T - rate * dz
        p = p * math.exp(-G * dz * 1000 / (RD * 0.5 * (T + T_new)))     # hydrostatic, dry-air constant
        T, z = T_new, z + dz
    return rows, lcl


def descend(T_top_K, w, p_top, dz_km, dz=0.01):
    """Dry descent by dz_km from a saturated summit: returns (T_K, Td_K, p) at the bottom."""
    T, p = T_top_K, p_top
    n = int(round(dz_km / dz))
    for _ in range(n):
        T_new = T + GAMMA_D * dz
        p = p * math.exp(G * dz * 1000 / (RD * 0.5 * (T + T_new)))
        T = T_new
    return T, dew_point(w, p), p


# invented example soundings: (height km, temperature degC) corners, linear in between
ENV_A = [(0.0, 28.0), (1.5, 28.0 - 1.5 * 9.76), (3.6, 28.0 - 1.5 * 9.76 - 2.1 * 6.5), (4.0, 28.0 - 1.5 * 9.76 - 2.1 * 6.5 + 1.5), (8.0, 28.0 - 1.5 * 9.76 - 2.1 * 6.5 + 1.5 - 4.0 * 4.5)]
# above the warm layer the sounding cools at only 4.5 degC/km (stable for a saturated parcel),
# so the parcel stays colder than A all the way up and the cumulus stops near 4 km
ENV_B = [(0.0, 28.0), (0.4, 29.5), (8.0, 29.5 - 7.6 * 4.5)]


def env(profile, z):
    for (z1, t1), (z2, t2) in zip(profile, profile[1:]):
        if z1 <= z <= z2:
            return t1 + (t2 - t1) * (z - z1) / (z2 - z1)
    return profile[-1][1]


def cloud_top(rows, lcl, profile):
    """First height above the condensation level where the parcel becomes colder than the sounding."""
    for z, T, Td, p in rows:
        if z > lcl + 0.05 and T < env(profile, z):
            return z
    return None


def numbers():
    n = {"gamma_d": GAMMA_D, "cp": CP, "Rd": RD, "eps": EPS}
    for t in (-10, 0, 10, 20, 30, 40):
        n["ws_%d" % t] = ws(t + 273.15) * 1000
    n["ws_ratio_10K_at_20"] = ws(303.15) / ws(293.15)
    rows, lcl = parcel(28.0, 16.0)
    n["lcl_afternoon_km"] = lcl
    n["lcl_rule_km"] = 0.125 * (28 - 16)
    # dew-point lapse below the condensation level
    n["dewpoint_rate"] = (rows[0][2] - [r for r in rows if r[0] >= 1.0 - 1e-9][0][2]) / 1.0
    n["T_lcl"] = [r for r in rows if abs(r[0] - lcl) < 1e-6][0][1]
    n["moist_rate_lcl"] = moist_rate(n["T_lcl"] + 273.15, [r for r in rows if abs(r[0] - lcl) < 1e-6][0][3])
    n["moist_rate_15C_1000"] = moist_rate(288.15, 100000.0)
    n["moist_rate_0C_700"] = moist_rate(273.15, 70000.0)
    n["moist_rate_m20C_500"] = moist_rate(253.15, 50000.0)
    n["cloud_top_A_km"] = cloud_top(rows, lcl, ENV_A)
    n["parcel_warmer_than_A_above_top"] = any(z > n["cloud_top_A_km"] and T > env(ENV_A, z) for z, T, Td, p in rows)
    n["parcel_minus_env_B_at_1km"] = [r for r in rows if r[0] >= 1.0 - 1e-9][0][1] - env(ENV_B, 1.0)
    # morning: relative humidity of the 16 degC dew point at 20 degC; evening dew at 16 degC
    n["rh_morning_20C"] = ws(289.15) / ws(293.15) * 100
    n["rh_afternoon_28C"] = ws(289.15) / ws(301.15) * 100
    n["ws_16"] = ws(289.15) * 1000
    n["ws_28"] = ws(301.15) * 1000
    # the mountain: air at sea level 20 degC, dew point 12 degC, over a 2500 m ridge
    up, lcl_m = parcel(20.0, 12.0, z_top=2.5)
    top = up[-1]
    n["mtn_lcl_km"] = lcl_m
    n["mtn_T_lcl"] = [r for r in up if abs(r[0] - lcl_m) < 1e-6][0][1]
    n["mtn_T_top"] = top[1]
    w_top = ws(top[1] + 273.15, top[3])
    n["mtn_w_start_gkg"] = mixing_ratio(e_sat_water(285.15), P0) * 1000
    n["mtn_w_top_gkg"] = w_top * 1000
    Tb, Tdb, pb = descend(top[1] + 273.15, w_top, top[3], 2.5)
    n["mtn_T_lee"] = Tb - 273.15
    n["mtn_Td_lee"] = Tdb - 273.15
    n["mtn_rh_lee"] = ws(Tdb, pb) / ws(Tb, pb) * 100
    n["droplets_per_raindrop"] = (2.0 / 0.02) ** 3
    for t in (-5, -10, -20):
        n["e_water_%d" % t] = p_vap(273.15 + t)
        n["e_ice_%d" % t] = p_sub(273.15 + t)
        n["water_over_ice_%d" % t] = p_vap(273.15 + t) / p_sub(273.15 + t)
    n["std_lapse"] = STD_LAPSE
    return n


if __name__ == "__main__":
    write_table(__file__, ("T_C", "ws_gkg", "rho_gm3"),
                [(t, ws(t + 273.15) * 1000, e_sat_water(t + 273.15) / (RV * (t + 273.15)) * 1000)
                 for t in range(-10, 41)], part="sat", digits=5)
    rows, lcl = parcel(28.0, 16.0)
    write_table(__file__, ("z_km", "T_C", "Td_C"), [(z, T, Td) for z, T, Td, p in rows[::5]], part="parcel", digits=5)
    write_table(__file__, ("z_km", "Td_C"), [(z, Td) for z, T, Td, p in rows if z <= lcl + 1e-9], part="dew", digits=5)
    write_table(__file__, ("z_km", "T_C"), ENV_A, part="envA", digits=5)
    write_table(__file__, ("z_km", "T_C"), ENV_B, part="envB", digits=5)
    up, lcl_m = parcel(20.0, 12.0, z_top=2.5)
    write_table(__file__, ("z_km", "T_C", "Td_C"), [(z, T, Td) for z, T, Td, p in up[::5]], part="mountain", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=7)

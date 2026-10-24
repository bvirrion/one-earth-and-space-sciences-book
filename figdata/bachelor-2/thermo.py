"""Atmospheric thermodynamics (Year 2, atmospheric-thermodynamics): saturation vapour pressure,
the moist adiabat, a real morning sounding on a skew-T diagram with its parcel, CAPE and CIN,
and Koehler curves.

  constants    R = 8.314462618 J/(mol K) (const:R); molar mass of dry air 28.97 g/mol
               (earth:Mmol) and of water 18.0153 g/mol (nist4:water-mw); R_d = R/M_d,
               R_v = R/M_w, eps = M_w/M_d; c_p = gamma/(gamma - 1) R_d with gamma = 1.4 for air
               (nasa:grc-gamma, as in the Year 1 volume); g = 9.80665 m/s2 (const:gn).
               Latent heat of vaporization at the triple point L = 2500.9 kJ/kg, the enthalpy
               difference of the saturated vapour and liquid at 0.01 degC (nist4:water-sat),
               held constant.
  es           saturation vapour pressure over liquid water: integrated Clausius--Clapeyron
               with constant L from the triple point (611.657 Pa, 273.16 K; iapws4:sublimation);
               the empirical formula e = 611.2 exp(17.67 t/(t + 243.5)) Pa, t in degC
               (su26:svp); NIST values from IAPWS-95 at 0.01 to 40 degC (nist4:water-sat).
               Over ice: the IAPWS R14-08 sublimation equation (iapws4:sublimation).
  sounding     Norman, Oklahoma, 16 April 2026 12 UTC (IGRA2, data:b4-sounding): every level
               with a temperature down to 100 hPa. Heights: the reported geopotential heights
               where given, otherwise integrated from the surface with the hypsometric
               equation on the virtual temperature (Year 1 volume).
  parcel       the surface parcel: dry adiabat (constant mixing ratio) to the lifting
               condensation level (found by bisection), then the pseudo-adiabat
               dT/dp = (R_d T + L r_s)/(p (c_p + L^2 r_s/(R_v T^2))), r_s = eps e_s/(p - e_s),
               by fourth-order Runge--Kutta in steps of at most 1 hPa.
  cape         on a 1-hPa grid, environment interpolated linearly in ln p:
               CAPE = R_d * integral of (T_parcel - T_env) d ln p where positive, from the LFC
               (lowest level above the LCL where the parcel becomes warmer and stays warmer
               for at least 50 hPa) to the EL (top of the positive area); CIN the negative
               area below the LFC. Both with T (as in the chapter) and with the virtual
               temperature.
  skewt        x = T(degC) + SKEW ln(1000/p), SKEW = 30 K, p in hPa on a reversed log axis.
  kohler       kappa-Koehler (Petters and Kreidenweis 2007, pk07:kohler, pk07:kappa):
               S = (D^3 - Dd^3)/(D^3 - Dd^3 (1 - kappa)) exp(A/D), A = 4 sigma M_w/(R T rho_w),
               sigma = 0.072 J/m2, T = 298.15 K, rho_w = 997.0 kg/m3 (NIST at 25 degC,
               nist4:water-sat); ammonium sulfate, kappa = 0.61.

  part es        T_C cc emp ice wi    (hPa; ice and the ratio emp/ice only up to 0 degC)
  part nist      T_C es_hPa
  part iso       x p T        (isotherms every 10 degC, two points each, blank line between)
  part dry       x p theta    (dry adiabats, every 10 K of potential temperature)
  part moist     x p thw      (pseudo-adiabats, labelled by their temperature at 1000 hPa)
  part mix       x p r        (saturation mixing-ratio lines, g/kg, 1000 to 600 hPa)
  part env       x p T        (the sounding's temperature)
  part dew       x p Td       (its dew point)
  part parcel    x p T        (the surface parcel)
  part cape      x p          (closed polygon of the positive area, parcel up then env down)
  part cin       x p          (closed polygon of the negative area below the LFC)
  part marks     name x p     (LCL, LFC and EL on the parcel curve)
  part kohler    D_um s30 s50 s100     (supersaturation in per cent, dry diameters in nm)
  part table     p z T Td Tp           (the levels printed in the chapter's problem)
  part numbers   key value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")

R = 8.314462618
MD, MW = 28.97e-3, 18.0153e-3
RD, RV = R / MD, R / MW
EPS = MW / MD
GAMMA = 1.4
CP = GAMMA / (GAMMA - 1.0) * RD
G = 9.80665
L = 2500.9e3
TT, PT = 273.16, 611.657                   # triple point (K, Pa)
SKEW = 30.0

# NIST Chemistry WebBook (IAPWS-95), saturated water: degC, Pa
NIST = ((0.01, 611.65), (5.0, 872.58), (10.0, 1228.2), (15.0, 1705.8), (20.0, 2339.3),
        (25.0, 3169.9), (30.0, 4247.0), (35.0, 5629.0), (40.0, 7384.9))
RHO_W25 = 997.0
SIGMA, T_K = 0.072, 298.15
KAPPA_AS = 0.61


# --- saturation -------------------------------------------------------------------------
def es(T):
    """Saturation vapour pressure over liquid water (Pa), Clausius--Clapeyron, constant L."""
    return PT * math.exp(L / RV * (1.0 / TT - 1.0 / T))


def es_emp(T):
    t = T - 273.15
    return 611.2 * math.exp(17.67 * t / (t + 243.5))


def es_ice(T):
    """IAPWS R14-08 sublimation pressure (Pa), valid 50-273.16 K."""
    a = (-0.212144006e2, 0.273203819e2, -0.610598130e1)
    b = (0.333333333e-2, 0.120666667e1, 0.170333333e1)
    th = T / TT
    return PT * math.exp(sum(ai * th ** bi for ai, bi in zip(a, b)) / th)


def dew_point(e):
    """Inverse of es: the temperature at which e is the saturation pressure."""
    return 1.0 / (1.0 / TT - RV / L * math.log(e / PT))


def mixing_ratio(e, p):
    return EPS * e / (p - e)


def rs(T, p):
    return mixing_ratio(es(T), p)


def tv(T, r):
    return T * (1.0 + r / EPS) / (1.0 + r)


def theta(T, p):
    return T * (1.0e5 / p) ** (RD / CP)


def gamma_s(T, p):
    """Saturated adiabatic lapse rate (K/m) at T, p."""
    r = rs(T, p)
    return G * (1.0 + L * r / (RD * T)) / (CP + L * L * r / (RV * T * T))


def dTdp_moist(T, p):
    r = rs(T, p)
    return (RD * T + L * r) / (p * (CP + L * L * r / (RV * T * T)))


def moist(T, p, p_end, dp=100.0):
    """Follow the pseudo-adiabat from (T, p) to p_end (Pa) by RK4."""
    n = max(1, int(math.ceil(abs(p_end - p) / dp)))
    h = (p_end - p) / n
    for _ in range(n):
        k1 = dTdp_moist(T, p)
        k2 = dTdp_moist(T + 0.5 * h * k1, p + 0.5 * h)
        k3 = dTdp_moist(T + 0.5 * h * k2, p + 0.5 * h)
        k4 = dTdp_moist(T + h * k3, p + h)
        T += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        p += h
    return T


def lcl(T, Td, p):
    """Pressure and temperature of the lifting condensation level of a parcel (T, Td, p)."""
    r = mixing_ratio(es(Td), p)
    th = theta(T, p)
    lo, hi = 1.0e4, p
    for _ in range(200):
        pm = 0.5 * (lo + hi)
        Tm = th * (pm / 1.0e5) ** (RD / CP)
        if pm * r / (EPS + r) < es(Tm):
            hi = pm
        else:
            lo = pm
    pm = 0.5 * (lo + hi)
    return pm, th * (pm / 1.0e5) ** (RD / CP)


def lcl_height_rule(T, Td):
    """Height of the LCL by the linearised rule z = (T - Td)/(Gamma_d - Gamma_dew)."""
    gd = G / CP
    gdew = G * RV * Td * Td / (L * RD * T)
    return (T - Td) / (gd - gdew)


# --- the sounding -----------------------------------------------------------------------
def read_sounding():
    with open(os.path.join(DERIVED, "bachelor-2-sounding.csv"), encoding="utf8") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        p = float(r["p_hPa"]) * 100.0
        T = float(r["T_C"]) + 273.15
        Td = float(r["Td_C"]) + 273.15 if r["Td_C"] else None
        z = float(r["z_m"]) if r["z_m"] else None
        out.append([p, z, T, Td])
    out.sort(key=lambda x: -x[0])
    # dew points missing aloft: take the last reported depression (only for the virtual
    # temperature, where they matter little)
    last = None
    for row in out:
        if row[3] is None:
            row[3] = row[2] - last if last is not None else row[2] - 30.0
        else:
            last = row[2] - row[3]
    return out


def interp_env(snd, p):
    """T and Td of the environment at p (Pa), linear in ln p."""
    for a, b in zip(snd, snd[1:]):
        if a[0] >= p >= b[0]:
            f = math.log(a[0] / p) / math.log(a[0] / b[0])
            return a[2] + f * (b[2] - a[2]), a[3] + f * (b[3] - a[3])
    raise ValueError(p)


def grid(snd, dp=100.0):
    p0, p1 = snd[0][0], snd[-1][0]
    n = int((p0 - p1) // dp)
    return [p0 - i * dp for i in range(n + 1)]


def heights(snd, ps):
    """Heights above sea level of the pressures ps (descending), hypsometric on T_v."""
    z0 = snd[0][1]
    zs, z = [z0], z0
    for a, b in zip(ps, ps[1:]):
        Ta, Tda = interp_env(snd, a)
        Tb, Tdb = interp_env(snd, b)
        tva = tv(Ta, mixing_ratio(es(Tda), a))
        tvb = tv(Tb, mixing_ratio(es(Tdb), b))
        z += RD * 0.5 * (tva + tvb) / G * math.log(a / b)
        zs.append(z)
    return zs


def parcel_profile(T0, Td0, p0, ps):
    plcl, Tlcl = lcl(T0, Td0, p0)
    r0 = mixing_ratio(es(Td0), p0)
    th = theta(T0, p0)
    out, Tc, pc = [], Tlcl, plcl
    for p in ps:
        if p >= plcl:
            out.append((th * (p / 1.0e5) ** (RD / CP), r0))
        else:
            Tc = moist(Tc, pc, p)
            pc = p
            out.append((Tc, rs(Tc, p)))
    return plcl, Tlcl, out


def buoyancy(snd, virtual=False):
    ps = grid(snd)
    p0, _, T0, Td0 = snd[0]
    plcl, Tlcl, par = parcel_profile(T0, Td0, p0, ps)
    b = []
    for p, (Tp, rp) in zip(ps, par):
        Te, Tde = interp_env(snd, p)
        if virtual:
            b.append(tv(Tp, rp) - tv(Te, mixing_ratio(es(Tde), p)))
        else:
            b.append(Tp - Te)
    return ps, par, b, plcl, Tlcl


def cape_cin(snd, virtual=False):
    ps, par, b, plcl, Tlcl = buoyancy(snd, virtual)
    i_lfc = None
    for i, p in enumerate(ps):
        if p > plcl or b[i] <= 0:
            continue
        j = i
        while j < len(ps) and b[j] > 0:
            j += 1
        if ps[i] - ps[min(j, len(ps) - 1)] >= 5000.0:
            i_lfc = i
            break
    i_el = i_lfc
    while i_el + 1 < len(ps) and b[i_el + 1] > 0:
        i_el += 1
    cape = sum(RD * 0.5 * (b[k] + b[k + 1]) * math.log(ps[k] / ps[k + 1])
               for k in range(i_lfc, i_el))
    cin = sum(RD * 0.5 * (min(b[k], 0) + min(b[k + 1], 0)) * math.log(ps[k] / ps[k + 1])
              for k in range(0, i_lfc))
    # interpolate the zero crossings
    def cross(k):
        return ps[k] + (ps[k + 1] - ps[k]) * b[k] / (b[k] - b[k + 1])
    p_lfc = cross(i_lfc - 1) if i_lfc > 0 and b[i_lfc - 1] <= 0 else ps[i_lfc]
    p_el = cross(i_el) if i_el + 1 < len(ps) else ps[i_el]
    return dict(cape=cape, cin=cin, p_lfc=p_lfc, p_el=p_el, plcl=plcl, Tlcl=Tlcl,
                i_lfc=i_lfc, i_el=i_el, ps=ps, par=par, b=b)


# --- Koehler ----------------------------------------------------------------------------
def kohler_A(T=T_K):
    return 4.0 * SIGMA * MW / (R * T * RHO_W25)


def kohler_S(D, Dd, kappa=KAPPA_AS, T=T_K):
    return (D ** 3 - Dd ** 3) / (D ** 3 - Dd ** 3 * (1.0 - kappa)) * math.exp(kohler_A(T) / D)


def kohler_critical(Dd, kappa=KAPPA_AS, T=T_K):
    """Exact maximum of the kappa-Koehler curve (golden-section search in ln D)."""
    lo, hi = math.log(Dd * 1.01), math.log(Dd * 200.0)
    f = lambda x: -kohler_S(math.exp(x), Dd, kappa, T)
    gr = (math.sqrt(5) - 1) / 2
    c, d = hi - gr * (hi - lo), lo + gr * (hi - lo)
    for _ in range(200):
        if f(c) < f(d):
            hi = d
        else:
            lo = c
        c, d = hi - gr * (hi - lo), lo + gr * (hi - lo)
    x = 0.5 * (lo + hi)
    return math.exp(x), kohler_S(math.exp(x), Dd, kappa, T) - 1.0


def kohler_critical_approx(Dd, kappa=KAPPA_AS, T=T_K):
    """S - 1 ~ A/D - B/D^3 with B = kappa Dd^3: D_c = sqrt(3B/A), s_c = sqrt(4A^3/(27B))."""
    A, B = kohler_A(T), kappa * Dd ** 3
    return math.sqrt(3 * B / A), math.sqrt(4 * A ** 3 / (27 * B))


# --- the chapter's numbers ---------------------------------------------------------------
TABLE_P = (971.09, 925.0, 907.72, 889.14, 850.0, 700.0, 500.0, 400.0, 300.0, 250.0, 200.0)


def numbers():
    d = {}
    snd = read_sounding()
    p0, z0, T0, Td0 = snd[0]
    d["sfc_p"], d["sfc_z"], d["sfc_T"], d["sfc_Td"] = p0 / 100, z0, T0 - 273.15, Td0 - 273.15
    e0 = es(Td0)
    d["sfc_e"] = e0 / 100
    d["sfc_r_gkg"] = mixing_ratio(e0, p0) * 1000
    d["sfc_q_gkg"] = d["sfc_r_gkg"] / (1 + d["sfc_r_gkg"] / 1000)
    d["sfc_Tv_minus_T"] = tv(T0, mixing_ratio(e0, p0)) - T0
    c = cape_cin(snd)
    cv = cape_cin(snd, virtual=True)
    zs = heights(snd, c["ps"])
    zp = dict(zip(c["ps"], zs))

    def z_at(p):
        ps = c["ps"]
        for a, b in zip(ps, ps[1:]):
            if a >= p >= b:
                f = math.log(a / p) / math.log(a / b)
                return zp[a] + f * (zp[b] - zp[a])
        return zs[-1]
    d["lcl_p"], d["lcl_T"] = c["plcl"] / 100, c["Tlcl"] - 273.15
    d["lcl_z_agl"] = z_at(c["plcl"]) - z0
    d["lcl_rule_agl"] = lcl_height_rule(T0, Td0)
    d["lfc_p"], d["lfc_z_agl"] = c["p_lfc"] / 100, z_at(c["p_lfc"]) - z0
    d["el_p"], d["el_z"] = c["p_el"] / 100, z_at(c["p_el"])
    d["cape"], d["cin"] = c["cape"], c["cin"]
    d["cape_v"], d["cin_v"] = cv["cape"], cv["cin"]
    d["w_max"] = math.sqrt(2 * c["cape"])
    d["w_max_v"] = math.sqrt(2 * cv["cape"])
    d["Tp500"] = moist(c["Tlcl"], c["plcl"], 50000.0) - 273.15
    d["Te500"] = interp_env(snd, 50000.0)[0] - 273.15
    d["lifted_index"] = d["Te500"] - d["Tp500"]
    d["Gamma_d_Kkm"] = G / CP * 1000
    d["cp"], d["Rd"], d["Rv"], d["eps"] = CP, RD, RV, EPS
    d["L_over_Rv"] = L / RV
    for t in (0.0, 10.0, 20.0, 30.0):
        T = t + 273.15
        d["es_cc_%d" % t] = es(T) / 100
        d["es_emp_%d" % t] = es_emp(T) / 100
        d["slope_pct_%d" % t] = 100 * L / (RV * T * T)
        d["gamma_s_1000_%d" % t] = gamma_s(T, 1.0e5) * 1000
        d["gamma_s_500_%d" % t] = gamma_s(T, 5.0e4) * 1000
    for tn, pn in NIST:
        d["nist_ratio_%g" % tn] = es(tn + 273.15) / pn
    d["gamma_s_200_m60"] = gamma_s(213.15, 2.0e4) * 1000
    d["sfc_theta"] = theta(T0, p0)
    d["sfc_thetae"] = theta(T0, p0) * math.exp(L * mixing_ratio(e0, p0) / (CP * c["Tlcl"]))
    d["ice_ratio_m10"] = es_emp(263.15) / es_ice(263.15)
    d["ice_ratio_m20"] = es_emp(253.15) / es_ice(253.15)
    d["kohler_A_nm"] = kohler_A() * 1e9
    for dd in (30, 50, 100):
        Dc, sc = kohler_critical(dd * 1e-9)
        Dca, sca = kohler_critical_approx(dd * 1e-9)
        d["kc_D_%d" % dd], d["kc_s_%d" % dd] = Dc * 1e6, sc * 100
        d["kca_D_%d" % dd], d["kca_s_%d" % dd] = Dca * 1e6, sca * 100
    # problem table: parcel temperature at the table levels
    for p in TABLE_P:
        Tp = parcel_profile(T0, Td0, p0, [p * 100])[2][0][0]
        d["tab_Tp_%g" % p] = Tp - 273.15
    return d


def problem_table():
    snd = read_sounding()
    p0, z0, T0, Td0 = snd[0]
    c = cape_cin(snd)
    zs = dict(zip(c["ps"], heights(snd, c["ps"])))
    rows = []
    for p in TABLE_P:
        pp = p * 100
        Te, Tde = interp_env(snd, pp)
        exact = [s for s in snd if abs(s[0] - pp) < 1.0]
        near = min(zs, key=lambda q: abs(q - pp))
        z = zs[near]
        if exact:
            Te, Tde = exact[0][2], exact[0][3]
            z = exact[0][1] if exact[0][1] is not None else z      # reported height
        Tp = parcel_profile(T0, Td0, p0, [pp])[2][0][0]
        rows.append((p, round(z), round(Te - 273.15, 1), round(Tde - 273.15, 1),
                     round(Tp - 273.15, 1)))
    return rows


def skewx(T, p):
    return T - 273.15 + SKEW * math.log(1.0e5 / p)


if __name__ == "__main__":
    rows = []
    for t in range(-40, 41):
        T = t + 273.15
        rows.append((t, round(es(T) / 100, 4), round(es_emp(T) / 100, 4),
                     round(es_ice(T) / 100, 4) if t <= 0 else "nan",
                     round(es_emp(T) / es_ice(T), 4) if t <= 0 else "nan"))
    write_table(__file__, ("T_C", "cc", "emp", "ice", "wi"), rows, part="es")
    write_table(__file__, ("T_C", "es_hPa"), [(t, round(e / 100, 3)) for t, e in NIST],
                part="nist")
    plev = [105000 - 1000 * i for i in range(96)]          # 1050 .. 100 hPa
    iso, dry, mst, mix = [], [], [], []
    for t in range(-100, 51, 10):
        for p in (105000.0, 10000.0):
            iso.append((round(skewx(t + 273.15, p), 3), p / 100, t))
        iso.append(())
    for th_ in range(250, 461, 10):
        for p in plev[::5]:
            T = th_ * (p / 1.0e5) ** (RD / CP)
            dry.append((round(skewx(T, p), 3), p / 100, th_))
        dry.append(())
    for tw in range(-10, 41, 5):
        T = tw + 273.15
        pts = []
        for p in [100000 + 1000 * i for i in range(6)][::-1]:          # 1050 .. 1000
            pts.append((skewx(moist(T, 1.0e5, p), p), p))
        Tc, pc = T, 1.0e5
        for p in [100000 - 2500 * i for i in range(1, 37)]:            # down to 10000
            Tc = moist(Tc, pc, p)
            pc = p
            pts.append((skewx(Tc, p), p))
        mst += [(round(x, 3), p / 100, tw) for x, p in pts] + [()]
    for r in (1, 2, 4, 8, 12, 16, 20, 28):
        for p in (105000.0, 60000.0):
            # temperature at which the saturation mixing ratio is r g/kg at p
            e = p * (r / 1000) / (EPS + r / 1000)
            mix.append((round(skewx(dew_point(e), p), 3), p / 100, r))
        mix.append(())
    write_table(__file__, ("x", "p", "T"), iso, part="iso")
    write_table(__file__, ("x", "p", "theta"), dry, part="dry")
    write_table(__file__, ("x", "p", "thw"), mst, part="moist")
    write_table(__file__, ("x", "p", "r"), mix, part="mix")
    snd = read_sounding()
    write_table(__file__, ("x", "p", "T"),
                [(round(skewx(s[2], s[0]), 3), s[0] / 100, round(s[2] - 273.15, 1)) for s in snd],
                part="env")
    raw = []
    with open(os.path.join(DERIVED, "bachelor-2-sounding.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            if r["Td_C"]:
                p = float(r["p_hPa"]) * 100
                raw.append((round(skewx(float(r["Td_C"]) + 273.15, p), 3), p / 100,
                            float(r["Td_C"])))
    write_table(__file__, ("x", "p", "Td"), raw, part="dew")
    c = cape_cin(snd)
    ps, par, b = c["ps"], c["par"], c["b"]
    write_table(__file__, ("x", "p", "T"),
                [(round(skewx(Tp, p), 3), p / 100, round(Tp - 273.15, 2))
                 for p, (Tp, _) in list(zip(ps, par))[::10] if p >= 15000], part="parcel")
    i0, i1 = c["i_lfc"], c["i_el"]
    up = [(round(skewx(par[k][0], ps[k]), 3), ps[k] / 100) for k in range(i0, i1 + 1, 5)]
    down = [(round(skewx(interp_env(snd, ps[k])[0], ps[k]), 3), ps[k] / 100)
            for k in range(i1, i0 - 1, -5)]
    write_table(__file__, ("x", "p"), up + down + [up[0]], part="cape")
    up = [(round(skewx(par[k][0], ps[k]), 3), ps[k] / 100) for k in range(0, i0 + 1)]
    down = [(round(skewx(interp_env(snd, ps[k])[0], ps[k]), 3), ps[k] / 100)
            for k in range(i0, -1, -1)]
    write_table(__file__, ("x", "p"), up + down + [up[0]], part="cin")
    marks = []
    for name, pm in (("LCL", c["plcl"]), ("LFC", c["p_lfc"]), ("EL", c["p_el"])):
        k = min(range(len(ps)), key=lambda i: abs(ps[i] - pm))
        marks.append((name, round(skewx(par[k][0], ps[k]), 3), round(pm / 100, 1)))
    write_table(__file__, ("name", "x", "p"), marks, part="marks")
    krows = []
    for i in range(0, 241):
        D = 10 ** (-1.7 + i * 0.0125)                        # 0.02 .. 20 um
        row = [round(D, 5)]
        for dd in (30, 50, 100):
            Dd = dd * 1e-9
            row.append(round(100 * (kohler_S(D * 1e-6, Dd) - 1.0), 5) if D * 1e-6 > Dd * 1.02
                       else "nan")
        krows.append(tuple(row))
    write_table(__file__, ("D_um", "s30", "s50", "s100"), krows, part="kohler")
    write_table(__file__, ("p", "z", "T", "Td", "Tp"), problem_table(), part="table")
    write_table(__file__, ("key", "value"),
                [(k, round(v, 4)) for k, v in sorted(numbers().items())], part="numbers")

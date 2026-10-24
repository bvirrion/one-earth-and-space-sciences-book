"""Magmatic differentiation (Year 2, magmatic-differentiation): the plagioclase loop, the laws
of fractional and equilibrium crystallisation for a trace element, the lavas of Paricutin
(1943-1952) and their mass balance, assimilation with fractional crystallisation, and the
whole-rock record of the Skaergaard intrusion.

  plag       Bowen (1913), Am. J. Sci. (4) 35, 577-599, "Summary of melting intervals"
             (ledger bowen13:plagioclase): solidus and liquidus of the plagioclase
             feldspars, compositions as molecular ratios Ab:An converted to mol % An.
             The curves between the data points are monotone cubic (PCHIP) interpolants
             through the data; at the albite end both curves are taken to meet at 1100 C, the
             beginning of melting of Ab98An2, "practically" the melting point of albite.
  zoning     Crystallisation of a plagioclase liquid of 50 mol % An on that loop.  Equilibrium:
             the crystals stay in equilibrium with the liquid and end at the bulk composition.
             Fractional: each increment of crystal is removed as it forms (no reaction), so
             d(m X_L) = X_S dm, i.e. dX_L/d(ln m) = X_S(T(X_L)) - X_L, integrated with RK4 in
             ln m; the layer formed when a fraction x has crystallised has X_S.
  rayleigh   C_L/C_0 = F^(D-1) (fractional) and 1/(D + F(1 - D)) (equilibrium) for a trace
             element of bulk partition coefficient D, F the mass fraction of liquid left.
  paricutin  Wilcox (1954), USGS Bulletin 965-C, Table 2 (ledger wilcox54:table2): bulk
             analyses of 22 lavas, Feb. 1943 to Feb. 1952, wt %; FeO_t = FeO + 0.8998 Fe2O3.
             Calculated groundmass of nos. 1 and 19 (wilcox54:groundmass) and the four
             xenoliths of Table 3 (wilcox54:xenoliths), whose mean is the "average xenolith".
  massbal    The three-oxide mass balance of Wilcox (SiO2, Al2O3, MgO as controls): 100 g of
             groundmass 1 + a g of average xenolith - b g of olivine Fo80 - c g of plagioclase
             An70 has the composition of groundmass 19.  Each oxide k gives
                 100 g1_k + a X_k - b O_k - c P_k = (100 + a - b - c) g19_k,
             a 3x3 linear system (or least squares over seven oxides).  Fo80 and An70 are
             computed from their formulae.  Wilcox's graphical answer: a = 25.4, b = 2.9,
             c = 9.6 (wilcox54:mass-balance).
  afc        Assimilation with fractional crystallisation (the closed form of DePaolo 1981,
             re-derived): crystallisation rate dMc, assimilation rate dMa = r dMc, magma mass
             M with F = M/M0; for a trace element with bulk D and assimilant concentration Ca,
                 C/C0 = F^(-z) + (r/(r - 1 + D)) (Ca/C0) (1 - F^(-z)),  z = (r + D - 1)/(r - 1),
             and the isotope ratio of the element is the concentration-weighted mean of the
             initial magma's and the assimilant's.  The magma and wall-rock values in the
             figure are illustrative assumptions, not measurements.
  skaergaard data/derived/bachelor-2-skaergaard.csv (Tegner et al. 2023, CC BY 4.0, ledger
             data:b4-skaergaard): cumulates of the reference profile, stratigraphic height,
             the authors' fraction of melt remaining F, Ni and Zr (XRF) and FeO_t.  The
             authors' fit F = 1.091e-7 H^2 - 5.9064e-4 H + 0.7678 (H in m, tegner23:skaergaard).

  part plag-data   an T_sol T_liq          (nan where not measured)
  part plag-curve  an T_sol T_liq
  part zoning      x an_frac an_eq an_liq_frac
  part rayleigh    F d0.01 d0.1 d0.5 d2 d5 d10 e0.01 e0.1 e2 e10
  part paricutin   n year SiO2 Al2O3 FeOt MgO CaO Na2O K2O
  part afc         F srC_r0 srC_r02 srC_r05 iso_r0 iso_r02 iso_r05
  part skg         H F Ni Zr FeOt
  part skg-fit     H F
  part values      what value
"""
import math
import os
import sys

import numpy as np
from scipy.interpolate import PchipInterpolator

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SKG_CSV = os.path.join(HERE, "..", "..", "data", "derived", "bachelor-2-skaergaard.csv")

# --- plagioclase, Bowen 1913 (mol % An, solidus, liquidus; None = not measured) ------------
BOWEN_PLAG = [(100.0, 1550, 1550), (100 * 5 / 6, 1465, 1521), (100 * 2 / 3, 1372, 1490),
              (50.0, 1287, 1450), (100 / 3, 1205, 1394), (25.0, 1175, 1362),
              (22.5, 1158, None), (20.0, None, 1334), (100 / 9, None, 1265), (2.0, 1100, None)]
ALBITE_END = 1100.0   # both curves meet here (beginning of melting of Ab98An2)


def _curve(index):
    pts = sorted([(a, r[index]) for r in BOWEN_PLAG for a in [r[0]] if r[index] is not None])
    if index == 2:                      # the liquidus has no point at the albite end
        pts = [(0.0, ALBITE_END)] + pts
    else:
        pts = [(0.0, ALBITE_END)] + [p for p in pts if p[0] > 2.0]
    x, y = zip(*pts)
    return PchipInterpolator(x, y)


T_SOL = _curve(1)
T_LIQ = _curve(2)


def _invert(f, t, lo=0.0, hi=100.0):
    """An (mol %) at which the increasing curve f reaches temperature t (bisection)."""
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(mid) < t:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def an_solid(t):
    return _invert(T_SOL, t)


def an_liquid(t):
    return _invert(T_LIQ, t)


def equilibrium_path(x0, n=200):
    """(T, An_liquid, An_solid, fraction crystallised) from the liquidus to the solidus of a
    bulk composition x0 (mol % An), lever rule in mol fractions."""
    t1, t2 = float(T_LIQ(x0)), float(T_SOL(x0))
    out = []
    for i in range(n + 1):
        t = t1 + (t2 - t1) * i / n
        xl, xs = an_liquid(t), an_solid(t)
        frac = 0.0 if xs == xl else (x0 - xl) / (xs - xl)
        out.append((t, xl, xs, min(max(frac, 0.0), 1.0)))
    return out


def fractional_path(x0, m_end=1e-3, n=600):
    """(fraction crystallised, An of the layer forming, An of the liquid) for perfect
    fractional crystallisation of a plagioclase liquid x0; RK4 in u = ln m."""
    def rhs(xl):
        return an_solid(float(T_LIQ(xl))) - xl
    u_end = math.log(m_end)
    h = u_end / n
    xl, out = x0, []
    for i in range(n + 1):
        u = i * h
        out.append((1 - math.exp(u), an_solid(float(T_LIQ(xl))), xl))
        k1 = rhs(xl)
        k2 = rhs(max(xl + 0.5 * h * k1, 0.0))
        k3 = rhs(max(xl + 0.5 * h * k2, 0.0))
        k4 = rhs(max(xl + h * k3, 0.0))
        xl = max(xl + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6, 0.0)
    return out


# --- trace element laws ------------------------------------------------------------------
def rayleigh(f, d):
    return f ** (d - 1)


def equilibrium(f, d):
    return 1.0 / (d + f * (1 - d))


# --- Paricutin, Wilcox 1954 -----------------------------------------------------------------
# number, date as decimal year (month middle where only the month is given), then wt %:
# SiO2 Al2O3 Fe2O3 FeO MgO CaO Na2O K2O
PARICUTIN = [
    (1, 1943.14, 55.04, 18.82, 1.92, 5.69, 5.68, 7.17, 3.88, 0.85),
    (2, 1943.21, 54.88, 18.38, 1.31, 5.97, 5.57, 7.40, 3.88, 0.86),
    (3, 1943.87, 55.51, 18.19, 1.63, 5.38, 5.31, 7.19, 3.92, 1.10),
    (4, 1944.29, 55.21, 17.94, 1.60, 5.96, 5.37, 6.98, 3.87, 1.26),
    (5, 1944.87, 55.59, 17.72, 1.33, 5.99, 5.60, 6.99, 4.00, 1.13),
    (6, 1945.87, 56.41, 17.67, 1.39, 5.40, 5.66, 6.89, 3.87, 1.19),
    (7, 1945.89, 56.15, 17.57, 1.80, 5.08, 5.68, 6.95, 3.85, 1.18),
    (8, 1945.96, 56.48, 17.57, 1.63, 5.18, 5.56, 6.95, 3.70, 1.34),
    (9, 1945.96, 56.41, 17.60, 1.67, 5.18, 5.62, 6.90, 3.81, 1.20),
    (10, 1945.96, 56.61, 17.61, 1.45, 5.35, 5.64, 6.89, 3.84, 1.21),
    (11, 1946.71, 56.13, 17.34, 1.74, 5.42, 5.58, 6.99, 3.79, 1.30),
    (12, 1947.27, 57.05, 17.27, 1.42, 5.21, 5.64, 6.94, 3.71, 1.23),
    (13, 1947.44, 57.63, 17.50, 1.38, 5.12, 5.16, 6.77, 3.71, 1.38),
    (14, 1947.68, 58.13, 17.59, 1.27, 5.20, 4.55, 6.72, 3.79, 1.41),
    (15, 1947.87, 58.39, 17.78, 1.87, 4.51, 4.03, 6.75, 3.86, 1.30),
    (16, 1948.62, 59.09, 17.55, 2.04, 4.27, 4.03, 6.46, 3.92, 1.50),
    (17, 1949.38, 59.41, 17.30, 1.57, 4.78, 3.81, 6.36, 3.71, 1.67),
    (18, 1949.95, 59.77, 17.29, 1.21, 4.95, 3.72, 6.28, 3.74, 1.67),
    (19, 1950.67, 59.93, 17.31, 1.23, 4.95, 3.55, 6.21, 3.73, 1.72),
    (20, 1951.37, 60.24, 17.30, 1.19, 4.59, 3.55, 6.14, 4.01, 1.66),
    (21, 1951.87, 60.38, 17.27, 1.10, 4.66, 3.59, 6.16, 3.89, 1.69),
    (22, 1952.15, 60.07, 17.28, 1.37, 4.39, 3.73, 6.16, 4.00, 1.67),
]
FE2O3_TO_FEO = 2 * 71.844 / 159.688        # 0.8998

OXIDES = ("SiO2", "Al2O3", "FeO", "MgO", "CaO", "Na2O", "K2O")
GROUNDMASS_1 = dict(SiO2=55.53, Al2O3=19.22, FeO=7.15, MgO=4.66, CaO=7.29, Na2O=4.00, K2O=0.88)
GROUNDMASS_19 = dict(SiO2=60.16, Al2O3=17.60, FeO=5.93, MgO=3.19, CaO=6.32, Na2O=3.79, K2O=1.75)
# Table 3, X-1 to X-4: SiO2 Al2O3 Fe2O3 FeO MgO CaO Na2O K2O
XENOLITHS = [(70.88, 14.27, 1.52, 1.53, 1.17, 1.65, 4.18, 3.64),
             (71.99, 15.95, 0.68, 1.22, 0.71, 2.49, 4.03, 2.43),
             (71.10, 14.31, 1.43, 1.63, 1.14, 2.88, 3.20, 3.76),
             (75.95, 13.51, 0.25, 0.27, 0.05, 1.05, 3.90, 4.74)]
WILCOX_ABC = (25.4, 2.9, 9.6)

MOLAR = dict(SiO2=60.084, Al2O3=101.961, FeO=71.844, MgO=40.304, CaO=56.077, Na2O=61.979,
             K2O=94.196)


def paricutin_rows():
    out = []
    for n, yr, si, al, fe3, fe2, mg, ca, na, k in PARICUTIN:
        out.append((n, yr, si, al, fe2 + FE2O3_TO_FEO * fe3, mg, ca, na, k))
    return out


def olivine(fo):
    """wt % oxides of olivine (Mg_fo Fe_1-fo)2 SiO4."""
    m = dict(MgO=2 * fo * MOLAR["MgO"], FeO=2 * (1 - fo) * MOLAR["FeO"], SiO2=MOLAR["SiO2"])
    t = sum(m.values())
    return {k: 100 * v / t for k, v in m.items()}


def plagioclase(an):
    """wt % oxides of plagioclase, an mole fraction of CaAl2Si2O8 (rest NaAlSi3O8)."""
    m = dict(CaO=an * MOLAR["CaO"], Na2O=(1 - an) * 0.5 * MOLAR["Na2O"],
             Al2O3=(an + 0.5 * (1 - an)) * MOLAR["Al2O3"],
             SiO2=(2 * an + 3 * (1 - an)) * MOLAR["SiO2"])
    t = sum(m.values())
    return {k: 100 * v / t for k, v in m.items()}


def average_xenolith():
    cols = list(zip(*XENOLITHS))
    mean = [sum(c) / len(c) for c in cols]
    si, al, fe3, fe2, mg, ca, na, k = mean
    return dict(SiO2=si, Al2O3=al, FeO=fe2 + FE2O3_TO_FEO * fe3, MgO=mg, CaO=ca, Na2O=na, K2O=k)


def mass_balance(controls=("SiO2", "Al2O3", "MgO")):
    """(a, b, c, total, residuals) of the Wilcox mass balance; exact for three controls,
    least squares for more."""
    x, o, p = average_xenolith(), olivine(0.80), plagioclase(0.70)
    g1, g19 = GROUNDMASS_1, GROUNDMASS_19
    a_mat = np.array([[x[k] - g19[k], -(o.get(k, 0.0) - g19[k]), -(p.get(k, 0.0) - g19[k])]
                      for k in controls])
    rhs = np.array([100 * (g19[k] - g1[k]) for k in controls])
    a, b, c = np.linalg.lstsq(a_mat, rhs, rcond=None)[0]
    total = 100 + a - b - c
    res = {k: (100 * g1[k] + a * x[k] - b * o.get(k, 0.0) - c * p.get(k, 0.0)) / total - g19[k]
           for k in OXIDES}
    return a, b, c, total, res


# --- AFC ----------------------------------------------------------------------------------
def afc_conc(f, d, r, ca_c0):
    z = (r + d - 1) / (r - 1)
    return f ** (-z) + (r / (r - 1 + d)) * ca_c0 * (1 - f ** (-z))


def afc_ratio(f, d, r, ca_c0, iso_m, iso_a):
    """Isotope ratio of the magma: mass of the element from the initial magma, C0 F^(1-z)...
    computed as the concentration-weighted mean of the two sources."""
    z = (r + d - 1) / (r - 1)
    from_magma = f ** (-z)                      # C/C0 carried by the original magma's atoms
    from_wall = (r / (r - 1 + d)) * ca_c0 * (1 - f ** (-z))
    return (from_magma * iso_m + from_wall * iso_a) / (from_magma + from_wall)


def afc_numeric(f_end, d, r, ca_c0, iso_m, iso_a, n=20000):
    """Euler-free check: integrate the mass balances in steps of crystallised mass.
    State: magma mass M, element mass from magma Em, from wall Ew (C0 = 1, M0 = 1)."""
    m, em, ew = 1.0, 1.0, 0.0
    dmc = (1.0 - f_end) / (1.0 - r) / n
    for _ in range(n):
        c = (em + ew) / m
        out_m = d * c * dmc * em / (em + ew)
        out_w = d * c * dmc * ew / (em + ew)
        em -= out_m
        ew += r * dmc * ca_c0 - out_w
        m += (r - 1) * dmc
    c = (em + ew) / m
    return m, c, (em * iso_m + ew * iso_a) / (em + ew)


AFC_D, AFC_CA_C0, AFC_ISO_M, AFC_ISO_A = 1.5, 0.5, 0.7035, 0.7200   # illustrative


# --- Skaergaard ---------------------------------------------------------------------------
SKG_A, SKG_B, SKG_C = 1.091e-7, -5.9064e-4, 0.7678


def skg_f(h):
    return SKG_A * h * h + SKG_B * h + SKG_C


def skg_rows():
    import csv
    with open(SKG_CSV, encoding="utf8") as fh:
        return [r for r in csv.DictReader(fh)]


def skg_ni_slope(fmin=0.23):
    """least-squares slope of ln Ni against ln F for the cumulates with F >= fmin (the
    Lower and Middle Zones): ln Ni = const + (D - 1) ln F if the cumulates hold D times the
    liquid's Ni and the liquid follows the Rayleigh law with a constant D."""
    pts = [(math.log(float(r["F"])), math.log(float(r["Ni"]))) for r in skg_rows()
           if r["Ni"] and float(r["F"]) >= fmin]
    x, y = np.array(pts).T
    slope, icept = np.polyfit(x, y, 1)
    return slope, icept, len(pts)


if __name__ == "__main__":
    write_table(__file__, ("an", "T_sol", "T_liq"),
                [(a, s if s is not None else float("nan"), lq if lq is not None else float("nan"))
                 for a, s, lq in BOWEN_PLAG], part="plag-data")
    write_table(__file__, ("an", "T_sol", "T_liq"),
                [(a, float(T_SOL(a)), float(T_LIQ(a))) for a in np.linspace(0, 100, 101)],
                part="plag-curve")

    frac = fractional_path(50.0)
    eq = equilibrium_path(50.0)
    fx, fs_, fl = (np.array(c) for c in zip(*frac))
    ex, es = np.array([r[3] for r in eq]), np.array([r[2] for r in eq])
    rows = []
    for x in np.linspace(0, 0.99, 100):
        # layer forming at crystallised fraction x (fractional); crystals when a fraction x
        # has crystallised (equilibrium); both interpolated in their computed paths
        rows.append((x, float(np.interp(x, fx, fs_)), float(np.interp(x, ex, es)),
                     float(np.interp(x, fx, fl))))
    write_table(__file__, ("x", "an_frac", "an_eq", "an_liq_frac"), rows, part="zoning")

    fs = [i / 200 for i in range(1, 201)]
    write_table(__file__, ("F", "d0.01", "d0.1", "d0.5", "d2", "d5", "d10",
                           "e0.01", "e0.1", "e2", "e10"),
                [(f, rayleigh(f, 0.01), rayleigh(f, 0.1), rayleigh(f, 0.5), rayleigh(f, 2),
                  rayleigh(f, 5), rayleigh(f, 10), equilibrium(f, 0.01), equilibrium(f, 0.1),
                  equilibrium(f, 2), equilibrium(f, 10)) for f in fs], part="rayleigh")

    write_table(__file__, ("n", "year", "SiO2", "Al2O3", "FeOt", "MgO", "CaO", "Na2O", "K2O"),
                paricutin_rows(), part="paricutin")

    fa = [1 - i / 100 for i in range(0, 71)]
    write_table(__file__, ("F", "srC_r0", "srC_r02", "srC_r05", "iso_r0", "iso_r02", "iso_r05"),
                [(f, rayleigh(f, AFC_D), afc_conc(f, AFC_D, 0.2, AFC_CA_C0),
                  afc_conc(f, AFC_D, 0.5, AFC_CA_C0), AFC_ISO_M,
                  afc_ratio(f, AFC_D, 0.2, AFC_CA_C0, AFC_ISO_M, AFC_ISO_A),
                  afc_ratio(f, AFC_D, 0.5, AFC_CA_C0, AFC_ISO_M, AFC_ISO_A)) for f in fa],
                part="afc")

    write_table(__file__, ("H", "F", "Ni", "Zr", "FeOt"),
                [(float(r["height_m"]), float(r["F"]), float(r["Ni"]) if r["Ni"] else float("nan"),
                  float(r["Zr"]) if r["Zr"] else float("nan"), float(r["FeOt"]))
                 for r in skg_rows()], part="skg")
    write_table(__file__, ("H", "F"), [(h, skg_f(h)) for h in range(0, 2201, 50)], part="skg-fit")

    a, b, c, tot, res = mass_balance()
    a7, b7, c7, tot7, res7 = mass_balance(OXIDES)
    xa, o80, p70 = average_xenolith(), olivine(0.80), plagioclase(0.70)
    slope, icept, npts = skg_ni_slope()
    h0 = (-SKG_B - math.sqrt(SKG_B ** 2 - 4 * SKG_A * SKG_C)) / (2 * SKG_A)
    vals = [("mb3_a", a), ("mb3_b", b), ("mb3_c", c), ("mb3_total", tot)]
    vals += [("mb3_res_" + k, v) for k, v in res.items()]
    vals += [("mb7_a", a7), ("mb7_b", b7), ("mb7_c", c7), ("mb7_total", tot7)]
    vals += [("xen_" + k, v) for k, v in xa.items()]
    vals += [("fo80_" + k, v) for k, v in o80.items()]
    vals += [("an70_" + k, v) for k, v in p70.items()]
    vals += [("frac_core_an", frac[0][1]), ("frac_an_at_x0.5", float(np.interp(0.5, fx, fs_))),
             ("frac_an_at_x0.7", float(np.interp(0.7, fx, fs_))),
             ("frac_x_liquid_an1", float(np.interp(-1.0, -fl, fx))),
             ("eq_start_T", eq[0][0]), ("eq_end_T", eq[-1][0]), ("eq_first_solid", eq[0][2]),
             ("eq_last_liquid", eq[-1][1]),
             ("skg_ni_slope", slope), ("skg_ni_D", slope + 1), ("skg_ni_npts", npts),
             ("skg_H_at_F0", h0), ("skg_F_H1000", skg_f(1000))]
    write_table(__file__, ("what", "value"), vals, part="values")

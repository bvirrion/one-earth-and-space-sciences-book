"""Melting the mantle (Year 2, mantle-melting): two binary phase diagrams of rock-forming
minerals from the original quenching experiments, and the decompression melting of
peridotite with the parameterisation of Katz, Spiegelman and Langmuir (2003).

  di-an      Diopside-anorthite, Bowen (1915), Am. J. Sci. (4) 40, Table I and text (ledger
             bowen15:di-an): an ordinary eutectic system, eutectic 1270 C at 42 wt %
             anorthite; diopside melts at 1391.5 C and anorthite at 1550 C (the calibration
             points of the paper).  Liquidus temperatures are the midpoints of the quenching
             brackets (glass + crystals / glass only).  The liquidus between the data points
             is drawn as a straight line in each bracket of composition.
  fo-sio2    Forsterite-silica, Bowen and Andersen (1914), Am. J. Sci. (4) 37, 487-500 (ledger
             bowen14:mgo-sio2): forsterite melts at 1890 +- 20 C; MgSiO3 (clino-enstatite)
             melts incongruently at 1557 C to forsterite and a liquid of 97.5 % MgSiO3 +
             2.5 % SiO2; eutectic clino-enstatite + cristobalite at 1543 C, liquid 87.5 %
             MgSiO3 + 12.5 % SiO2; forsterite liquidus at 1577 C for the MgSiO3 composition and
             just above 1625 C for 88.3 % MgSiO3 + 11.7 % Mg2SiO4.  Compositions converted to
             wt % SiO2 with the molar masses below.  The forsterite liquidus between 1890 C
             (pure Mg2SiO4) and 1625 C is not measured and is drawn straight (dashed).
  katz       Anhydrous melting of peridotite, Katz et al. (2003), Table 2 (ledger katz03:*):
               solidus             Ts = 1085.7 + 132.9 P - 5.1 P^2      (C, P in GPa)
               lherzolite liquidus Tl = 1475.0 + 80.0 P - 3.2 P^2
               liquidus            Tq = 1780.0 + 45.0 P - 2.0 P^2
               F = T'^beta1 with T' = (T - Ts)/(Tl - Ts) until cpx is exhausted at
               F_cpxout = M_cpx/(r1 + r2 P); beyond, F = F_co + (1 - F_co)((T - T_co)/(Tq - T_co))^beta2
               r1 = 0.50, r2 = 0.08, beta1 = beta2 = 1.5; cp 1000 J/(kg K), alpha_s 40e-6 /K,
               rho_s 3300 kg/m3, Delta S 300 J/(kg K); M_cpx = 0.15 (their Figure 2).
             Isentropic upwelling (Katz eqs 20-23 in integrated form): the specific entropy
               s = cp ln T - (alpha/rho) P + Delta S F
             is conserved; below the solidus T = Tp exp(alpha P/(rho cp)); above it F is found at
             each pressure on the melting surface T(P, F) by bisection.  The melt column runs
             from the onset pressure to the surface; crustal thickness of a triangular melting
             region h = integral of F dz along the axis (z = P/(rho g)), mantle and crust taken
             of equal density.
             Hydrous solidus: Ts - Delta T(X), Delta T = K X^gamma, K = 43 C/wt%^gamma,
             gamma = 0.75; water saturation X_sat = chi1 P^lambda + chi2 P, chi1 = 12,
             chi2 = 1 wt%, lambda = 0.6.

  part di-an-liq      x_an T             (liquidus, wt % anorthite)
  part di-an-data     x_an T
  part fo-sio2-liq    x_sio2 T           (measured part of the liquidus)
  part fo-sio2-fo     x_sio2 T           (unmeasured forsterite liquidus, straight)
  part pt             P_GPa z_km Ts Tl Tq ad1300 ad1350 ad1450 wet5 wetsat
  part onset          Tp P0 z0 T0
  part column         z_km F1300 F1350 F1450
  part crust          Tp h_km
  part values         what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# --- molar masses (g/mol) for converting Bowen and Andersen's compositions -------------------
M_MGO, M_SIO2 = 40.304, 60.084
M_FO = 2 * M_MGO + M_SIO2          # Mg2SiO4
M_EN = M_MGO + M_SIO2              # MgSiO3
SIO2_FO = 100 * M_SIO2 / M_FO      # 42.7 wt % SiO2
SIO2_EN = 100 * M_SIO2 / M_EN      # 59.9 wt % SiO2


def sio2_of(en, sio2=0.0, fo=0.0):
    """wt % SiO2 of a mixture of MgSiO3, SiO2 and Mg2SiO4 given in wt % of each."""
    return (en * SIO2_EN + 100.0 * sio2 + fo * SIO2_FO) / (en + sio2 + fo)


# --- diopside-anorthite, Bowen 1915 ------------------------------------------------------------
DI_MELT, AN_MELT = 1391.5, 1550.0
DI_AN_EUTECTIC = (42.0, 1270.0)
# (wt % An, lower bracket with crystals, upper bracket glass only)
DI_AN_BRACKETS = [(20, 1348, 1352), (40, 1275, 1280), (50, 1326, 1330), (60, 1388, 1392),
                  (80, 1483, 1487)]


def di_an_points():
    pts = [(0.0, DI_MELT)] + [(x, (lo + hi) / 2) for x, lo, hi in DI_AN_BRACKETS]
    pts.append((100.0, AN_MELT))
    pts.append(DI_AN_EUTECTIC)
    return sorted(pts)


def di_an_liquidus(x):
    """Piecewise-linear liquidus through the data and the eutectic."""
    pts = di_an_points()
    for (x1, t1), (x2, t2) in zip(pts, pts[1:]):
        if x1 <= x <= x2:
            return t1 + (t2 - t1) * (x - x1) / (x2 - x1)
    raise ValueError(x)


def lever(bulk, a, b):
    """Fraction of phase b in a mixture of a and b of bulk composition (one coordinate)."""
    return (bulk - a) / (b - a)


# --- forsterite-silica, Bowen and Andersen 1914 ------------------------------------------------
FO_MELT = 1890.0
PERITECTIC = (sio2_of(97.5, 2.5), 1557.0)
EUTECTIC_EN_CR = (sio2_of(87.5, 12.5), 1543.0)
FO_LIQ_EN = (SIO2_EN, 1577.0)
FO_LIQ_117 = (sio2_of(88.3, 0.0, 11.7), 1625.0)


def peritectic_forsterite_fraction():
    """Mass fraction of forsterite when MgSiO3 melts incongruently at the peritectic."""
    return lever(SIO2_EN, PERITECTIC[0], SIO2_FO)


# --- Katz et al. 2003 ---------------------------------------------------------------------------
A = (1085.7, 132.9, -5.1)
B = (1475.0, 80.0, -3.2)
C = (1780.0, 45.0, -2.0)
R1, R2, BETA1, BETA2 = 0.50, 0.08, 1.5, 1.5
CP, ALPHA, RHO, DS, G = 1000.0, 40e-6, 3300.0, 300.0, 9.81
K_H2O, GAMMA_H2O, CHI1, CHI2, LAMBDA = 43.0, 0.75, 12.0, 1.0, 0.6
M_CPX = 0.15
KM_PER_GPA = 1e9 / (RHO * G) / 1e3       # 30.9 km per GPa


def quad(c, p):
    return c[0] + c[1] * p + c[2] * p * p


def dquad(c, p):
    return c[1] + 2 * c[2] * p


def t_solidus(p):
    return quad(A, p)


def t_lherz(p):
    return quad(B, p)


def t_liquidus(p):
    return quad(C, p)


def t_melt(p, f, m_cpx=M_CPX, beta=BETA1):
    """Temperature (C) on the melting surface at pressure p (GPa) and melt fraction f."""
    ts, tl, tq = t_solidus(p), t_lherz(p), t_liquidus(p)
    fco = m_cpx / (R1 + R2 * p)
    if f <= fco:
        return ts + f ** (1 / beta) * (tl - ts)
    tco = ts + fco ** (1 / beta) * (tl - ts)
    return tco + ((f - fco) / (1 - fco)) ** (1 / BETA2) * (tq - tco)


def adiabat(tp, p):
    """Solid adiabat (C): T = Tp exp(alpha P / (rho cp)), Tp in C, P in GPa."""
    return (tp + 273.15) * math.exp(ALPHA * p * 1e9 / (RHO * CP)) - 273.15


def adiabat_gradient(tp):
    """dT/dP of the solid adiabat at the surface, K per GPa."""
    return ALPHA * (tp + 273.15) / (RHO * CP) * 1e9


def onset_pressure(tp):
    """Pressure (GPa) where the solid adiabat meets the dry solidus."""
    lo, hi = 0.0, 10.0
    for _ in range(80):
        m = (lo + hi) / 2
        if adiabat(tp, m) > t_solidus(m):
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def onset_linear(tp, grad):
    """Onset pressure with a straight adiabat T = Tp + grad P (the quadratic of the text)."""
    a, b, c = -A[2], grad - A[1], tp - A[0]
    return (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)


def entropy(p, t, f):
    return CP * math.log(t + 273.15) - ALPHA / RHO * p * 1e9 + DS * f


def melt_fraction(tp, p, m_cpx=M_CPX, beta=BETA1):
    """Melt fraction at pressure p along the isentrope of potential temperature tp."""
    s0 = CP * math.log(tp + 273.15)
    if entropy(p, t_solidus(p), 0.0) >= s0:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(50):
        m = (lo + hi) / 2
        if entropy(p, t_melt(p, m, m_cpx, beta), m) < s0:
            lo = m
        else:
            hi = m
    return (lo + hi) / 2


def productivity(p, f, beta=1.0):
    """-dF/dP (per GPa) on the melting surface of the T' model (no cpx exhaustion):
    [cp/T (dT/dP)_F - alpha/rho] / [Delta S + cp/T (dT/dF)_P]."""
    ts, tl = t_solidus(p), t_lherz(p)
    t = ts + f ** (1 / beta) * (tl - ts)
    tk = t + 273.15
    dtdp = dquad(A, p) + f ** (1 / beta) * (dquad(B, p) - dquad(A, p))
    dtdf = (1 / beta) * f ** (1 / beta - 1) * (tl - ts)
    num = CP / tk * dtdp - ALPHA / RHO * 1e9
    den = DS + CP / tk * dtdf
    return num / den


def column(tp, n=1500, m_cpx=M_CPX, beta=BETA1):
    """(P, F) from the onset to the surface and the crustal thickness h = int F dz (km)."""
    p0 = onset_pressure(tp)
    ps = [p0 * (1 - i / n) for i in range(n + 1)]
    fs = [melt_fraction(tp, p, m_cpx, beta) for p in ps]
    h = sum((fs[i] + fs[i + 1]) / 2 for i in range(n)) * (p0 / n) * KM_PER_GPA
    return p0, ps, fs, h


def delta_t_water(x):
    """Solidus lowering (C) by x wt % water dissolved in the melt."""
    return K_H2O * x ** GAMMA_H2O


def x_saturation(p):
    return CHI1 * p ** LAMBDA + CHI2 * p


def triangle_crust(f_max, height):
    """Crust of a triangular melting region with F rising linearly to f_max over height."""
    return f_max * height / 2


if __name__ == "__main__":
    write_table(__file__, ("x_an", "T"), [(x, di_an_liquidus(x)) for x in
                                          [0, 20, 40, 42, 50, 60, 80, 100]], part="di-an-liq")
    write_table(__file__, ("x_an", "T"), [(x, (lo + hi) / 2) for x, lo, hi in DI_AN_BRACKETS],
                part="di-an-data")
    write_table(__file__, ("x_sio2", "T"),
                [FO_LIQ_117, FO_LIQ_EN, PERITECTIC, EUTECTIC_EN_CR], part="fo-sio2-liq")
    write_table(__file__, ("x_sio2", "T"), [(SIO2_FO, FO_MELT), FO_LIQ_117], part="fo-sio2-fo")

    rows = []
    for i in range(0, 61):
        p = i / 10
        wsat = t_solidus(p) - delta_t_water(x_saturation(p))
        rows.append((p, p * KM_PER_GPA, t_solidus(p), t_lherz(p), t_liquidus(p),
                     adiabat(1300, p), adiabat(1350, p), adiabat(1450, p),
                     t_solidus(p) - delta_t_water(5.0), wsat))
    write_table(__file__, ("P_GPa", "z_km", "Ts", "Tl", "Tq", "ad1300", "ad1350", "ad1450",
                           "wet5", "wetsat"), rows, part="pt")

    onsets = []
    for tp in (1300, 1350, 1450):
        p0 = onset_pressure(tp)
        onsets.append((tp, p0, p0 * KM_PER_GPA, adiabat(tp, p0)))
    write_table(__file__, ("Tp", "P0", "z0", "T0"), onsets, part="onset")

    zs = [i for i in range(0, 131)]
    cols = {tp: [melt_fraction(tp, z / KM_PER_GPA) for z in zs] for tp in (1300, 1350, 1450)}
    write_table(__file__, ("z_km", "F1300", "F1350", "F1450"),
                [(z, cols[1300][i], cols[1350][i], cols[1450][i]) for i, z in enumerate(zs)],
                part="column")

    crust = []
    for tp in range(1250, 1560, 10):
        crust.append((tp, column(tp, n=600)[3]))
    write_table(__file__, ("Tp", "h_km"), crust, part="crust")

    p0, ps, fs, h1350 = column(1350)
    _, _, fs1450, h1450 = column(1450)
    _, _, fs1300, h1300 = column(1300)
    vals = [("sio2_fo", SIO2_FO), ("sio2_en", SIO2_EN), ("peritectic_sio2", PERITECTIC[0]),
            ("eutectic_en_cr_sio2", EUTECTIC_EN_CR[0]), ("fo_liq_117_sio2", FO_LIQ_117[0]),
            ("peritectic_fo_fraction", peritectic_forsterite_fraction()),
            ("grad_1350_K_per_GPa", adiabat_gradient(1350)), ("km_per_GPa", KM_PER_GPA),
            ("onset_1350", p0), ("onset_1350_linear20", onset_linear(1350, 20.0)),
            ("onset_1300", onset_pressure(1300)), ("onset_1450", onset_pressure(1450)),
            ("Fmax_1350", fs[-1]), ("Fmax_1300", fs1300[-1]), ("Fmax_1450", fs1450[-1]),
            ("h_1300", h1300), ("h_1350", h1350), ("h_1450", h1450),
            ("mean_prod_1350", fs[-1] / p0),
            ("prod_lin_1.5GPa_F0.1", productivity(1.5, 0.1)),
            ("prod_lin_2GPa_F0.1", productivity(2.0, 0.1)),
            ("cpxout_P0_DMM", 0.13 / R1), ("cpxout_P0_15", M_CPX / R1),
            ("dT_water_1", delta_t_water(1)), ("dT_water_5", delta_t_water(5)),
            ("xsat_1", x_saturation(1)), ("xsat_2", x_saturation(2)),
            ("dT_sat_1", delta_t_water(x_saturation(1))),
            ("dT_sat_2", delta_t_water(x_saturation(2)))]
    write_table(__file__, ("what", "value"), vals, part="values")

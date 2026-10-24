"""Metamorphic reactions (Year 2, metamorphic-facies): the Al2SiO5 phase diagram computed
from thermodynamic data, compared with the experimental diagram, and three other reactions.

  data       Robie and Hemingway (1995), USGS Bulletin 2131 (ledger rh95:al2sio5,
             rh95:al2sio5-ht): for kyanite, andalusite and sillimanite the enthalpy of
             formation at 298.15 K, the molar volume (J/bar) and, at 298.15-1200 K, the
             entropy S_T and (H_T - H_298)/T.
  method A   constant reaction properties: for a reaction a -> b,
                 dG(T, P) = dH - T dS + dV (P - 1)     (dH, dS at 298.15 K, dV constant),
             so the equilibrium line is P = 1 + (T dS - dH)/dV, a straight line of slope
             dS/dV (the Clapeyron slope).
  method B   temperature-dependent dH(T) = dH_298 + d(H_T - H_298) and dS(T) from the tables
             (linear interpolation between the tabulated temperatures), dV still constant
             (thermal expansion and compressibility neglected).
  triple     the intersection of the kyanite = andalusite and kyanite = sillimanite lines (the
             andalusite = sillimanite line passes through it identically, since
             dG(ky->sil) = dG(ky->and) + dG(and->sil)).
  hm93       Holdaway and Mukhopadhyay (1993), Table 11 (Book 2 ledger hm93:table11) and the
             triple point 504 C, 3.75 kbar (hm93:triple): the experimental diagram.
  day73      Day (1973) (ledger day73:ms-qz): muscovite + quartz = sanidine + sillimanite +
             water, 603, 637 and 662 C at 1, 2 and 3 kbar.
  cc-ar      calcite = aragonite, ab-jd     albite = jadeite + quartz, method A with the
             298.15 K data of rh95:cc-ar and rh95:ab-jd-qz (exercise values).

  part lines     T_C, P (kbar) of the three reactions by method A and B (full lines)
  part stable-*  the stable half of each line by method B, ending at the triple point
  part meta-*    its metastable extension
  part hm93-*    the experimental lines (T_C, P_kbar)
  part dg6       T_C, G(and) - G(ky), G(sil) - G(ky) in kJ/mol at 6 kbar (method B)
  part day73     T_C, P_kbar
  part values    what value
"""
import os
import sys

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

TT = np.array([298.15, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200])
PHASES = {
    "ky": dict(H=-2593.8e3, V=4.415,
               S=[82.80, 122.81, 157.97, 189.10, 216.84, 241.77, 264.37, 285.02, 304.02, 321.61],
               h=[0.0, 34.84, 59.44, 78.02, 92.59, 104.36, 114.09, 122.29, 129.30, 135.37]),
    "and": dict(H=-2589.9e3, V=5.152,
                S=[91.39, 131.57, 166.71, 197.79, 225.45, 250.30, 272.83, 293.41, 312.35, 329.88],
                h=[0.0, 34.98, 59.54, 78.05, 92.55, 104.25, 113.92, 122.07, 129.04, 135.07]),
    "sil": dict(H=-2586.1e3, V=4.986,
                S=[95.40, 135.63, 170.58, 201.44, 228.91, 253.59, 275.97, 296.44, 315.27, 332.71],
                h=[0.0, 35.01, 59.40, 77.73, 92.09, 103.70, 113.29, 121.39, 128.32, 134.33]),
}
REACTIONS = (("ky", "and"), ("ky", "sil"), ("and", "sil"))
K = 273.15

# experimental diagram, Holdaway and Mukhopadhyay (1993), Table 11 (C, kbar)
HM93 = {
    ("ky", "and"): [(200, 0.16), (300, 1.36), (400, 2.54), (500, 3.71), (600, 4.86),
                    (700, 6.00), (800, 7.13), (900, 8.24), (1000, 9.33)],
    ("ky", "sil"): [(500, 3.67), (600, 5.77), (700, 7.86), (800, 9.95), (900, 12.05),
                    (1000, 14.16)],
    ("and", "sil"): [(500, 3.82), (600, 2.30), (700, 0.95)],
}
HM93_TRIPLE = (504.0, 3.75)
DAY73 = [(603.0, 1.0), (637.0, 2.0), (662.0, 3.0)]

# 298.15 K data (S J/mol/K, V J/bar, dfH J/mol) for the exercise reactions
CC = dict(S=91.7, V=3.693, H=-1207.4e3, G=-1128.5e3)
AR = dict(S=88.0, V=3.415, H=-1207.4e3, G=-1127.4e3)
AB = dict(S=207.4, V=10.007, H=-3935.0e3, G=-3711.6e3)
JD = dict(S=133.5, V=6.040, H=-3029.3e3, G=-2850.6e3)
QZ = dict(S=41.5, V=2.269, H=-910.7e3, G=-856.3e3)


def g_phase(name, t, p, method="B"):
    """Gibbs energy relative to the elements' convention at 298.15 K (J/mol), T in K, P in
    bar: H_298 + (H_T - H_298) - T S_T + V (P - 1); method A freezes H and S at 298.15 K."""
    m = PHASES[name]
    if method == "A":
        return m["H"] - t * m["S"][0] + m["V"] * (p - 1)
    s = np.interp(t, TT, m["S"])
    h = np.interp(t, TT, np.array(m["h"]) * TT)
    return m["H"] + h - t * s + m["V"] * (p - 1)


def delta(a, b, key):
    """reaction a -> b property at 298.15 K: H (J), S (J/K), V (J/bar)."""
    if key == "S":
        return PHASES[b]["S"][0] - PHASES[a]["S"][0]
    return PHASES[b][key] - PHASES[a][key]


def clapeyron_slope(a, b):
    """dP/dT = dS/dV in bar/K (method A)."""
    return delta(a, b, "S") / delta(a, b, "V")


def line_p(a, b, t, method="B"):
    """equilibrium pressure (bar) of a = b at T (K)."""
    if method == "A":
        return 1 + (t * delta(a, b, "S") - delta(a, b, "H")) / delta(a, b, "V")
    return brentq(lambda p: g_phase(b, t, p, "B") - g_phase(a, t, p, "B"), -1e5, 1e5)


def triple_point(method="B"):
    t = brentq(lambda t: line_p("ky", "and", t, method) - line_p("ky", "sil", t, method), 500, 1100)
    return t, line_p("ky", "and", t, method)


def stable_phase(t, p, method="B"):
    g = {n: g_phase(n, t, p, method) for n in PHASES}
    return min(g, key=g.get)


def simple_line(r, p_):
    """method A line for products p_ and reactants r (lists of 298 K dicts): P(T) in bar."""
    dh = sum(x["H"] for x in p_) - sum(x["H"] for x in r)
    ds = sum(x["S"] for x in p_) - sum(x["S"] for x in r)
    dv = sum(x["V"] for x in p_) - sum(x["V"] for x in r)
    dg = sum(x["G"] for x in p_) - sum(x["G"] for x in r)
    return dh, ds, dv, dg, (lambda t: 1 + (t * ds - dh) / dv)


def cc_ar():
    return simple_line([CC], [AR])


def ab_jd_qz():
    return simple_line([AB], [JD, QZ])


def sensitivity(dh_kj=1.0, which=("ky", "and")):
    """shift of the method-A triple point when dfH of the product of `which` rises by dh_kj."""
    t0, p0 = triple_point("A")
    old = PHASES[which[1]]["H"]
    PHASES[which[1]]["H"] = old + dh_kj * 1e3
    try:
        t1, p1 = triple_point("A")
    finally:
        PHASES[which[1]]["H"] = old
    return t1 - t0, p1 - p0


if __name__ == "__main__":
    ts = np.arange(200.0, 901.0, 10.0)
    rows = []
    for tc in ts:
        t = tc + K
        rows.append((tc,) + tuple(line_p(a, b, t, m) / 1e3 for m in ("A", "B") for a, b in REACTIONS))
    write_table(__file__, ("T_C", "kyand_A", "kysil_A", "andsil_A", "kyand_B", "kysil_B",
                           "andsil_B"), rows, part="lines")
    tB, pB = triple_point("B")
    tcB = tB - K
    for a, b in REACTIONS:
        lo = ts[ts < tcB] if (a, b) == ("ky", "and") else ts[ts > tcB]
        hi = ts[ts > tcB] if (a, b) == ("ky", "and") else ts[ts < tcB]
        st = [(tc, line_p(a, b, tc + K) / 1e3) for tc in lo] + [(tcB, pB / 1e3)]
        mt = [(tcB, pB / 1e3)] + [(tc, line_p(a, b, tc + K) / 1e3) for tc in hi]
        st.sort()
        mt.sort()
        st = [r for r in st if r[1] >= 0]
        mt = [r for r in mt if r[1] >= 0]
        write_table(__file__, ("T_C", "P_kbar"), st, part="stable-%s%s" % (a, b))
        write_table(__file__, ("T_C", "P_kbar"), mt, part="meta-%s%s" % (a, b))
        write_table(__file__, ("T_C", "P_kbar"), HM93[(a, b)], part="hm93-%s%s" % (a, b))
    write_table(__file__, ("T_C", "P_kbar"), [HM93_TRIPLE], part="hm93-triple")
    write_table(__file__, ("T_C", "P_kbar"), [(tcB, pB / 1e3)], part="triple-B")
    write_table(__file__, ("T_C", "P_kbar"), DAY73, part="day73")
    dg = []
    for tc in np.arange(300.0, 901.0, 10.0):
        t = tc + K
        gk = g_phase("ky", t, 6000.0)
        dg.append((tc, (g_phase("and", t, 6000.0) - gk) / 1e3, (g_phase("sil", t, 6000.0) - gk) / 1e3))
    write_table(__file__, ("T_C", "dG_and", "dG_sil"), dg, part="dg6")
    tA, pA = triple_point("A")
    vals = [("triple_A_C", tA - K), ("triple_A_kbar", pA / 1e3),
            ("triple_B_C", tcB), ("triple_B_kbar", pB / 1e3)]
    for a, b in REACTIONS:
        vals += [("dH_%s%s_kJ" % (a, b), delta(a, b, "H") / 1e3),
                 ("dS_%s%s" % (a, b), delta(a, b, "S")),
                 ("dV_%s%s_Jbar" % (a, b), delta(a, b, "V")),
                 ("slope_%s%s_barK" % (a, b), clapeyron_slope(a, b))]
    for nm, f in (("ccar", cc_ar), ("abjd", ab_jd_qz)):
        dh, ds, dv, dgr, ln = f()
        vals += [("%s_dH" % nm, dh / 1e3), ("%s_dS" % nm, ds), ("%s_dV" % nm, dv),
                 ("%s_dG298" % nm, dgr / 1e3), ("%s_P25C_kbar" % nm, ln(298.15) / 1e3),
                 ("%s_P500C_kbar" % nm, ln(773.15) / 1e3)]
    for w in (("ky", "and"), ("ky", "sil"), ("and", "sil")):
        dt, dp = sensitivity(1.0, w)
        vals += [("sens_%s%s_dT" % w, dt), ("sens_%s%s_dP_bar" % w, dp)]
    write_table(__file__, ("what", "value"), vals, part="values")

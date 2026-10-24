"""Energy-balance climate models: the zero-dimensional model with an ice-albedo
ramp, and Budyko's latitudinal model with its ice line (Year 3, climate models).

Outgoing longwave radiation is linear in the surface temperature T (deg C),
OLR = A + B T. A and B are fitted, area-weighted, to the zonal annual means of
the NCEP-NCAR Reanalysis 1 (1991-2020): OLR at the top of the atmosphere
(data/derived/bachelor-1-ncep-ulwrf-toa.csv, Book 3 block, ledger data:b3-ncep)
against the air temperature at sigma 0.995 (data/derived/bachelor-3-ncep-air-sfc.csv,
ledger data:b5-ncep-air). Budyko (1969) found A = 14.0 - 3.0 n and B = 0.14 - 0.10 n
kcal cm-2 month-1 (n = 0.5 cloudiness), about 199 W/m2 and 1.43 W m-2 K-1
(ledger budyko69:olr); the conversion takes a month as a twelfth of a year.

Mean insolation Q0 = S0/4 with S0 = 1360 W/m2 (nasa:solar-mean). Albedos: ice
0.62 and ice edge 0.50 from Budyko (budyko69:albedo); ice-free 0.30, the Bond
albedo 0.294 rounded (earth:albedo).

Zero-dimensional model (parts asr, olr, eq):
    C dT/dt = Q (1 - alpha(T)) - (A + B T),
alpha(T) = 0.62 below T_ICE = -10 C, 0.30 above T_FREE = +10 C, linear between
(the ramp is a model choice of this chapter).

Budyko's latitudinal model (parts iceline, profile, obs): x = sin(latitude),
symmetric hemispheres, s(x) the annual-mean insolation of each latitude divided
by its global mean, taken from the NCEP top-of-atmosphere downward solar flux
(data/derived/bachelor-1-ncep-dswrf-toa.csv). Transport relaxes each latitude
towards the global mean, F = beta (T - Tbar), beta = 0.235 kcal cm-2 month-1 K-1
(budyko69:transport). In equilibrium

    B Tbar = Q (1 - abar) - A,
    T(x)   = [Q s(x)(1 - alpha(x)) - A + beta Tbar] / (B + beta),

ice where T < T_c. The ice line x_s satisfies T(x_s) = T_c with the edge albedo
0.50, which gives Q as an explicit function of x_s. T_c is fixed, as Budyko did,
so that today's insolation puts the ice line at 72 deg.

  part asr      T asr              absorbed solar Q(1 - alpha(T)) today
  part olr      T olr              A + B T
  part eqcold   S T                stable snowball branch of the 0-D model
  part eqmid    S T                unstable middle branch (on the albedo ramp)
  part eqwarm   S T                stable warm branch
  part icestable   lat q           Q/Q0 needed for an ice line at lat, stable
  part iceunstable lat q           the same, unstable branch (below the minimum)
  part profile  lat tmodel         Budyko model temperature today (ice line 72)
  part obs      lat tobs           NCEP annual zonal mean, NH and SH averaged
  part values   what value
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
DER = os.path.join(ROOT, "data", "derived")
S0 = 1360.0
Q0 = S0 / 4
ALB_ICE, ALB_EDGE, ALB_FREE = 0.62, 0.50, 0.30
T_ICE, T_FREE = -10.0, 10.0
KCAL_MONTH = 4184.0 * 1e4 / (365.25 * 86400.0 / 12)   # kcal cm-2 month-1 -> W m-2
BETA = 0.235 * KCAL_MONTH
LAT_ICE_TODAY = 72.0
DAYS = (31, 28.25, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def _read(name):
    with open(os.path.join(DER, name), newline="") as f:
        return list(csv.DictReader(f))


def annual_air():
    acc = {}
    for r in _read("bachelor-3-ncep-air-sfc.csv"):
        la = float(r["lat"])
        acc[la] = acc.get(la, 0.0) + DAYS[int(r["month"]) - 1] * float(r["value"])
    return {la: v / sum(DAYS) for la, v in acc.items()}


def zonal(name):
    return {float(r["lat"]): float(r["value"]) for r in _read(name)}


def fit_olr():
    """Area-weighted least squares OLR = A + B T over the 2.5-degree latitudes."""
    t = annual_air()
    olr = zonal("bachelor-1-ncep-ulwrf-toa.csv")
    lk = sorted(olr)
    lats = np.array(sorted(t))
    tv = np.array([t[la] for la in lats])
    ov = np.interp(lats, lk, [olr[k] for k in lk])
    w = np.cos(np.radians(lats))
    W = np.sum(w)
    tm, om = np.sum(w * tv) / W, np.sum(w * ov) / W
    b = np.sum(w * (tv - tm) * (ov - om)) / np.sum(w * (tv - tm) ** 2)
    return float(om - b * tm), float(b)


A, B = fit_olr()


def albedo_0d(t):
    if t <= T_ICE:
        return ALB_ICE
    if t >= T_FREE:
        return ALB_FREE
    return ALB_ICE + (ALB_FREE - ALB_ICE) * (t - T_ICE) / (T_FREE - T_ICE)


def net_0d(t, q=Q0):
    return q * (1 - albedo_0d(t)) - (A + B * t)


def equilibria_0d(q=Q0):
    """All roots of net_0d, with their stability (d net/dT < 0)."""
    out = []
    # snowball and warm branches: linear in T
    ts = (q * (1 - ALB_ICE) - A) / B
    if ts <= T_ICE:
        out.append((ts, True))
    # ramp: q(1 - a0 - a1 T) - A - B T = 0, alpha = ALB_ICE + k (T - T_ICE)
    k = (ALB_FREE - ALB_ICE) / (T_FREE - T_ICE)
    num = q * (1 - ALB_ICE + k * T_ICE) - A
    den = B + q * k
    if den != 0:
        tm = num / den
        if T_ICE < tm < T_FREE:
            out.append((tm, -q * k - B < 0))
    tw = (q * (1 - ALB_FREE) - A) / B
    if tw >= T_FREE:
        out.append((tw, True))
    return sorted(out)


def q_threshold_warm():
    """Q at which the warm equilibrium reaches the top of the ramp (saddle-node)."""
    return (A + B * T_FREE) / (1 - ALB_FREE)


def q_threshold_snowball():
    return (A + B * T_ICE) / (1 - ALB_ICE)


def insolation_shape():
    """s(x) on a grid of x = sin(lat), NCEP dswrf normalised, hemispheres averaged."""
    d = zonal("bachelor-1-ncep-dswrf-toa.csv")
    lk = np.array(sorted(d))
    vk = np.array([d[k] for k in lk])
    lat = np.degrees(np.arcsin(np.linspace(0.0, 1.0, 2001)))
    s = 0.5 * (np.interp(lat, lk, vk) + np.interp(-lat, lk, vk))
    x = np.sin(np.radians(lat))
    s = s / np.trapezoid(s, x)
    return x, s


X, SX = insolation_shape()


def s_of(x):
    return float(np.interp(x, X, SX))


CUM = np.concatenate(([0.0], np.cumsum(0.5 * (SX[1:] + SX[:-1]) * np.diff(X))))


def sun_fraction(xs):
    """Fraction of the planet's sunlight that falls equatorward of x_s."""
    return float(np.interp(xs, X, CUM))


def mean_albedo(xs):
    f = sun_fraction(xs)
    return ALB_FREE * f + ALB_ICE * (1.0 - f)


def q_for_iceline(xs, tc):
    abar = mean_albedo(xs)
    rhs = (B + BETA) * tc + A + BETA * A / B
    return rhs / (s_of(xs) * (1 - ALB_EDGE) + (BETA / B) * (1 - abar))


def t_mean(q, xs):
    return (q * (1 - mean_albedo(xs)) - A) / B


def t_profile(q, xs):
    tb = t_mean(q, xs)
    alb = np.where(X < xs, ALB_FREE, ALB_ICE)
    return (q * SX * (1 - alb) - A + BETA * tb) / (B + BETA)


def t_critical():
    """T_c such that Q0 puts the ice line at LAT_ICE_TODAY."""
    xs = math.sin(math.radians(LAT_ICE_TODAY))
    tb = t_mean(Q0, xs)
    return (Q0 * s_of(xs) * (1 - ALB_EDGE) - A + BETA * tb) / (B + BETA)


TC = t_critical()


def iceline_curve(step=0.25):
    rows = []
    lat = 0.0
    while lat <= 90.0 + 1e-9:
        rows.append((lat, q_for_iceline(math.sin(math.radians(lat)), TC) / Q0))
        lat += step
    return rows


def glaciation_threshold():
    rows = iceline_curve(0.05)
    lat, q = min(rows, key=lambda r: r[1])
    return lat, q


def main():
    ts = np.arange(-60.0, 40.01, 0.5)
    write_table(__file__, ("T", "asr"), [(t, Q0 * (1 - albedo_0d(t))) for t in ts], part="asr")
    write_table(__file__, ("T", "olr"), [(t, A + B * t) for t in ts], part="olr")
    branches = {"eqcold": [], "eqmid": [], "eqwarm": []}
    for s in np.arange(1000.0, 2400.01, 5.0):
        for t, st in equilibria_0d(s / 4):
            key = "eqmid" if not st else ("eqcold" if t <= T_ICE else "eqwarm")
            branches[key].append((s, t))
    # close each branch exactly at its saddle-node, where it meets the middle one
    branches["eqwarm"].insert(0, (4 * q_threshold_warm(), T_FREE))
    branches["eqcold"].append((4 * q_threshold_snowball(), T_ICE))
    branches["eqmid"] = ([(4 * q_threshold_warm(), T_FREE)] + branches["eqmid"]
                         + [(4 * q_threshold_snowball(), T_ICE)])
    for key, rows in branches.items():
        write_table(__file__, ("S", "T"), sorted(rows), part=key)
    glat, _ = glaciation_threshold()
    curve = iceline_curve()
    gpt = (glat, q_for_iceline(math.sin(math.radians(glat)), TC) / Q0)
    write_table(__file__, ("lat", "q"), sorted([r for r in curve if r[0] > glat] + [gpt]),
                part="icestable")
    write_table(__file__, ("lat", "q"), sorted([r for r in curve if r[0] < glat] + [gpt]),
                part="iceunstable")
    xs_today = math.sin(math.radians(LAT_ICE_TODAY))
    prof = t_profile(Q0, xs_today)
    lat = np.degrees(np.arcsin(X))
    rows = [(float(la), float(t)) for la, t in zip(lat[::20], prof[::20])]
    write_table(__file__, ("lat", "tmodel"), rows, part="profile")
    air = annual_air()
    obs = [(la, 0.5 * (air[la] + air[-la])) for la in sorted(air) if la >= 0]
    write_table(__file__, ("lat", "tobs"), obs, part="obs")
    roots = equilibria_0d(Q0)
    glat, gq = glaciation_threshold()
    vals = [["A", A], ["B", B], ["beta", BETA], ["Q0", Q0],
            ["budyko_A", (14.0 - 3.0 * 0.5) * KCAL_MONTH], ["budyko_B", (0.14 - 0.10 * 0.5) * KCAL_MONTH]]
    for i, (t, st) in enumerate(roots):
        vals.append(["eq%d_T" % i, t])
        vals.append(["eq%d_stable" % i, 1 if st else 0])
    vals += [["S_warm_lost", 4 * q_threshold_warm()],
             ["drop_warm_lost_pct", 100 * (1 - q_threshold_warm() / Q0)],
             ["S_snowball_lost", 4 * q_threshold_snowball()],
             ["rise_snowball_lost_pct", 100 * (q_threshold_snowball() / Q0 - 1)],
             ["Tc", TC], ["Tbar_today", t_mean(Q0, xs_today)],
             ["abar_today", mean_albedo(xs_today)],
             ["tobs_72", float(np.interp(72.0, [o[0] for o in obs], [o[1] for o in obs]))],
             ["glac_lat", glat], ["glac_q", gq], ["glac_drop_pct", 100 * (1 - gq)],
             ["s_equator", s_of(0.0)], ["s_pole", s_of(1.0)],
             ["resp_time_yr_C8.1", 8.1 / B]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

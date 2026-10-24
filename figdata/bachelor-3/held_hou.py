"""The Held-Hou model of the Hadley cell (Year 3, atmospheric dynamics).

Small-angle model: the upper branch keeps the angular momentum it had at rest
at the equator, u_M = Omega a phi^2; thermal-wind balance over the depth H then
fixes the mean potential temperature,

    theta_M / theta0 = A - K phi^4,     K = Omega^2 a^2 / (2 g H),

which must meet the radiative-equilibrium profile

    theta_E / theta0 = 1 + Delta/3 - Delta phi^2

at the cell edge phi_H, with equal integrals over the cell (no net heating):

    phi_H = sqrt(5 g H Delta / (3 Omega^2 a^2)),

A following from the continuity of theta at phi_H (theta_m below).

H and Delta are model parameters, chosen for illustration (H_ILL, DELTAS).

Observed: the mean meridional mass streamfunction at 500 hPa,
psi = (2 pi a cos(phi)/g) * integral_0^p [v] dp, from the zonal-mean meridional
wind of the NCEP-NCAR Reanalysis 1, long-term monthly means 1991-2020 (shared
derived table data/derived/bachelor-1-ncep-vwnd-p.csv, ledger
data:b5-ncep-vwnd), the 100 hPa value carried up to the top as in the Year 1
volume's script; the Hadley edge is where psi(500) changes sign poleward of its
extremum.

  part theta-<d>   phi thE thM    (theta/theta0 - 1) x 100, phi in degrees, for Delta = 1/d
  part psi         lat ann djf jja    psi(500 hPa) in 1e10 kg/s
  part values      what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
VWND = os.path.join(ROOT, "data", "derived", "bachelor-1-ncep-vwnd-p.csv")
OMEGA = 7.292115e-5
A_EARTH = 6371.0e3
G = 9.81
H_ILL = 15000.0
DELTAS = (3, 6)          # Delta = 1/3 and 1/6
SEASONS = {"ann": range(1, 13), "djf": (12, 1, 2), "jja": (6, 7, 8)}


def k_coef(h=H_ILL):
    return OMEGA ** 2 * A_EARTH ** 2 / (2 * G * h)


def phi_h(delta, h=H_ILL):
    return math.sqrt(5 * G * h * delta / (3 * OMEGA ** 2 * A_EARTH ** 2))


def theta_e(phi, delta):
    return 1 + delta / 3 - delta * phi ** 2


def theta_m(phi, delta, h=H_ILL):
    """Angular-momentum-conserving profile matching theta_E at phi_H."""
    ph = phi_h(delta, h)
    k = k_coef(h)
    a = theta_e(ph, delta) + k * ph ** 4
    return a - k * phi ** 4


def u_m(phi):
    return OMEGA * A_EARTH * phi ** 2


def load_v():
    d = {}
    with open(VWND, encoding="utf8") as f:
        for r in csv.DictReader(f):
            d[(int(r["month"]), int(r["level"]), float(r["lat"]))] = float(r["value"])
    return d


def psi500(d, months):
    lats = sorted({k[2] for k in d})
    levels = sorted({k[1] for k in d})           # 100 ... 1000 hPa
    out = {}
    for lat in lats:
        v = {p: sum(d[(m, p, lat)] for m in months) / len(months) for p in levels}
        integ = v[levels[0]] * levels[0] * 100.0  # top: 0 to 100 hPa
        for p1, p2 in zip(levels, levels[1:]):
            if p2 > 500:
                break
            integ += 0.5 * (v[p1] + v[p2]) * (p2 - p1) * 100.0
        out[lat] = 2 * math.pi * A_EARTH * math.cos(math.radians(lat)) / G * integ
    return out


def hadley_edge(psi, hemisphere):
    """Latitude where psi changes sign poleward of its extremum (linear interpolation)."""
    lats = sorted(psi)
    if hemisphere > 0:
        cand = [la for la in lats if 0 < la < 60]
        lat_ext = max(cand, key=lambda la: psi[la])
        seq = [la for la in cand if la >= lat_ext]
    else:
        cand = [la for la in lats if -60 < la < 0]
        lat_ext = min(cand, key=lambda la: psi[la])
        seq = sorted([la for la in cand if la <= lat_ext], reverse=True)
    for a, b in zip(seq, seq[1:]):
        if psi[a] * psi[b] <= 0:
            return a + (b - a) * psi[a] / (psi[a] - psi[b])
    return float("nan")


def main():
    for dd in DELTAS:
        delta = 1 / dd
        ph = phi_h(delta)
        rows = []
        for i in range(0, 61):
            phi = math.radians(i)
            rows.append([i, (theta_e(phi, delta) - 1) * 100,
                         (theta_m(phi, delta) - 1) * 100 if phi <= ph else float("nan")])
        write_table(__file__, ("phi", "thE", "thM"), rows, part="theta-%d" % dd)
    d = load_v()
    ps = {s: psi500(d, m) for s, m in SEASONS.items()}
    lats = sorted(ps["ann"])
    write_table(__file__, ("lat", "ann", "djf", "jja"),
                [[la, ps["ann"][la] / 1e10, ps["djf"][la] / 1e10, ps["jja"][la] / 1e10]
                 for la in lats], part="psi")
    vals = []
    for dd in DELTAS:
        ph = phi_h(1 / dd)
        vals += [["phiH_deg_1over%d" % dd, math.degrees(ph)], ["uM_at_phiH_1over%d" % dd, u_m(ph)]]
    for s in SEASONS:
        vals += [["edgeN_" + s, hadley_edge(ps[s], 1)], ["edgeS_" + s, hadley_edge(ps[s], -1)],
                 ["psimaxN_" + s, max(ps[s][la] for la in lats if 0 < la < 40) / 1e10],
                 ["psiminS_" + s, min(ps[s][la] for la in lats if -40 < la < 0) / 1e10]]
    vals.append(["K", k_coef()])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

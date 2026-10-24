"""Sea ice (Year 3, glaciology): the Arctic extent in March and September since
1979, and the growth of sea ice by conduction (Stefan's law).

Extents: NSIDC Sea Ice Index G02135 v4, monthly means (data/derived/bachelor-3-
nsidc-{mar,sep}-extent.csv, ledger data:b5-nsidc-extent); least-squares trends
over 1979-2026 (September 2026 is the last month in the files at writing), and
in percent of the 1981-2010 mean.

Growth: a slab of ice of thickness h under air at a constant temperature T_a
below the freezing point T_f of sea water; the heat of freezing at the base is
conducted through the ice (k_i = 2.03 W/m/K) and an optional snow cover
(k_s = 0.30 W/m/K, ledger cice:constants):

    rho_i L dh/dt = (T_f - T_a) / (h/k_i + h_s/k_s),

whose solution without snow is Stefan's law h^2 = 2 k_i (T_f - T_a) t/(rho_i L).
L = Lsub - Lvap = 2.835e6 - 2.501e6 = 3.34e5 J/kg (cice:constants), rho_i =
917 kg/m3 (iapws:ice-density). The surface is taken at the air temperature (no
surface boundary layer) and the ocean heat flux is neglected.

  part extent   year mar sep          million km2
  part trend    year mar sep          the fitted lines
  part stefan   day h0 hs              thickness (m): no snow; 0.2 m of snow
  part values   what value
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

K_ICE, K_SNOW = 2.03, 0.30
L_FUS = 2.835e6 - 2.501e6
RHO_I = 917.0
DT = 20.0            # K, T_f - T_a (invented winter)
H_SNOW = 0.2         # m
DAYS = 200


def read(month):
    path = os.path.join(ROOT, "data", "derived", "bachelor-3-nsidc-%s-extent.csv" % month)
    with open(path, encoding="utf8") as f:
        return {int(r["year"]): float(r["extent_Mkm2"]) for r in csv.DictReader(f)}


def trend(series, y0=1979, y1=2026):
    ys = np.array([y for y in sorted(series) if y0 <= y <= y1], float)
    vs = np.array([series[int(y)] for y in ys])
    b, a = np.polyfit(ys, vs, 1)
    return b, a


def stefan(t_s, dt=DT):
    return math.sqrt(2 * K_ICE * dt * t_s / (RHO_I * L_FUS))


def grow(days=DAYS, hs=0.0, dt=DT, h0=0.0, steps_per_day=48):
    """Integrate the growth law (explicit, exact for hs = 0 in the limit)."""
    out = [(0.0, h0)]
    h = h0
    step = 86400.0 / steps_per_day
    for i in range(1, days * steps_per_day + 1):
        # midpoint (RK2) on dh/dt = dt / (rho L (h/k_i + hs/k_s))
        f = lambda hh: dt / (RHO_I * L_FUS * (hh / K_ICE + hs / K_SNOW) + 1e-30)  # noqa: E731
        if h == 0.0 and hs == 0.0:
            h = stefan(step, dt)
        else:
            k1 = f(h)
            h = h + step * f(h + 0.5 * step * k1)
        if i % steps_per_day == 0:
            out.append((i / steps_per_day, h))
    return out


def main():
    mar, sep = read("mar"), read("sep")
    years = sorted(set(mar) & set(sep))
    write_table(__file__, ("year", "mar", "sep"), [(y, mar[y], sep[y]) for y in years], part="extent")
    bm, am = trend(mar)
    bs, as_ = trend(sep)
    write_table(__file__, ("year", "mar", "sep"),
                [(y, am + bm * y, as_ + bs * y) for y in (1979, 2026)], part="trend")
    ref_m = np.mean([mar[y] for y in range(1981, 2011)])
    ref_s = np.mean([sep[y] for y in range(1981, 2011)])
    g0 = grow()
    gs = grow(hs=H_SNOW)
    write_table(__file__, ("day", "h0", "hs"), [(a[0], a[1], b[1]) for a, b in zip(g0, gs)],
                part="stefan")
    vals = [["mar_trend_Mkm2_dec", 10 * bm], ["sep_trend_Mkm2_dec", 10 * bs],
            ["mar_ref_1981_2010", ref_m], ["sep_ref_1981_2010", ref_s],
            ["mar_trend_pct_dec", 1000 * bm / ref_m], ["sep_trend_pct_dec", 1000 * bs / ref_s],
            ["mar_1979", mar[1979]], ["sep_1979", sep[1979]], ["sep_min", min(sep.values())],
            ["sep_min_year", min(sep, key=sep.get)], ["mar_last", mar[max(mar)]],
            ["sep_last", sep[max(sep)]], ["last_year", max(sep)],
            ["L_fus", L_FUS], ["stefan_200d", stefan(DAYS * 86400.0)],
            ["stefan_100d", stefan(100 * 86400.0)], ["snow_200d", gs[-1][1]],
            ["snow_100d", gs[100][1]]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

"""Thermal wind read from observed zonal-mean winds (Year 3, geophysical fluid
dynamics).

Zonal-mean zonal wind of the NCEP-NCAR Reanalysis 1, long-term monthly means
1991-2020 (shared derived table data/derived/bachelor-1-ncep-uwnd-p.csv,
ledger data:b5-ncep-uwnd), January and July. In pressure coordinates the
thermal wind relation for the zonal wind is

    d u_g / d ln p = (R / f) (dT/dy)_p ,

so the shear between two levels gives the meridional gradient of the mean
temperature of the layer between them:

    <dT/dy> = - f (u(p_top) - u(p_bot)) / (R ln(p_bot / p_top)).

R is the gas constant of dry air of the NASA standard-atmosphere model
(nasa:grc-atmos, 0.2869 kJ/(kg K)); f = 2 Omega sin(lat) (geod5:grs80-defining).
The zonal-mean wind is close to geostrophic away from the tropics; latitudes
equatorward of LAT_MIN are left out.

  part prof-<lat>   p u          January profiles at 30, 45, 60 N (hPa, m/s)
  part grad-<mon>   lat dTdy drop  layer-mean dT/dy 850-250 hPa, K per 1000 km, by
                    latitude, and the poleward drop (dT/dy northward in the
                    north, -dT/dy in the south), K per 1000 km
  part jet          lat u200jan u200jul u850jan u850jul
  part values       what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
UWND = os.path.join(ROOT, "data", "derived", "bachelor-1-ncep-uwnd-p.csv")
OMEGA = 7.292115e-5
R_AIR = 286.9
P_BOT, P_TOP = 850, 250
LAT_MIN = 25.0
PROFILE_LATS = (30.0, 45.0, 60.0)


def load():
    d = {}
    with open(UWND, encoding="utf8") as f:
        for r in csv.DictReader(f):
            d[(int(r["month"]), int(r["level"]), float(r["lat"]))] = float(r["value"])
    return d


def coriolis(lat):
    return 2 * OMEGA * math.sin(math.radians(lat))


def layer_gradient(u_top, u_bot, lat, p_top=P_TOP, p_bot=P_BOT):
    """Layer-mean dT/dy (K/m) from the shear of the geostrophic zonal wind."""
    return -coriolis(lat) * (u_top - u_bot) / (R_AIR * math.log(p_bot / p_top))


def shear_from_gradient(dtdy, lat, p_top=P_TOP, p_bot=P_BOT):
    """Inverse: the wind difference u(p_top) - u(p_bot) for a uniform dT/dy."""
    return -R_AIR * dtdy * math.log(p_bot / p_top) / coriolis(lat)


def main():
    d = load()
    levels = sorted({k[1] for k in d}, reverse=True)
    lats = sorted({k[2] for k in d})
    for lat in PROFILE_LATS:
        write_table(__file__, ("p", "u"), [[p, d[(1, p, lat)]] for p in levels],
                    part="prof-%d" % lat)
    for mon, name in ((1, "jan"), (7, "jul")):
        rows = []
        for lat in lats:
            if abs(lat) < LAT_MIN or abs(lat) > 80:
                continue
            g = layer_gradient(d[(mon, P_TOP, lat)], d[(mon, P_BOT, lat)], lat)
            rows.append([lat, g * 1e6, -g * 1e6 if lat > 0 else g * 1e6])
        write_table(__file__, ("lat", "dTdy", "drop"), rows, part="grad-" + name)
    write_table(__file__, ("lat", "u200jan", "u200jul", "u850jan", "u850jul"),
                [[lat, d[(1, 200, lat)], d[(7, 200, lat)], d[(1, 850, lat)], d[(7, 850, lat)]]
                 for lat in lats], part="jet")
    jan_nh = max((d[(1, 200, lat)], lat) for lat in lats if lat > 0)
    jul_sh = max((d[(7, 200, lat)], lat) for lat in lats if lat < 0)
    g30 = layer_gradient(d[(1, P_TOP, 30.0)], d[(1, P_BOT, 30.0)], 30.0)
    g45 = layer_gradient(d[(1, P_TOP, 45.0)], d[(1, P_BOT, 45.0)], 45.0)
    write_table(__file__, ("what", "value"),
                [["jan_nh_u200_max", jan_nh[0]], ["jan_nh_u200_lat", jan_nh[1]],
                 ["jul_sh_u200_max", jul_sh[0]], ["jul_sh_u200_lat", jul_sh[1]],
                 ["dTdy_jan_30N_K_per_1000km", g30 * 1e6], ["dTdy_jan_45N_K_per_1000km", g45 * 1e6],
                 ["u250_jan_30", d[(1, 250, 30.0)]], ["u850_jan_30", d[(1, 850, 30.0)]],
                 ["u250_jan_45", d[(1, 250, 45.0)]], ["u850_jan_45", d[(1, 850, 45.0)]]],
                part="values")


if __name__ == "__main__":
    main()

"""Temperature, salinity and density with depth from the World Ocean Atlas 2023, and
the density of seawater from the international one-atmosphere equation of state
(grade 10, layered-ocean).

Sources (ledger): WOA23 annual and monthly climatologies, one 1-degree column per
site (data:b2-woa23; derived tables data/derived/grade-10-woa23-*.csv written by
tools/fetch_data.py); the one-atmosphere equation of state EOS-80 as printed in
UNESCO Technical Paper 44 (unesco:eos80), pure water after Bigg (1967); ocean area
and mean depth (charette:ocean-volume).

Densities are computed at the pressure of the surface (one atmosphere), as
oceanographers do to compare water masses; the in-situ compression is left aside.

  part site-<name>  depth t s rho     annual profile, 0-2000 m (or to the sea floor)
  part season       depth t_feb t_aug mid-latitude North Atlantic, 0-300 m
  part eos          t rho_s30 rho_s35 rho_s38   density against temperature
  part numbers      key value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DERIVED = os.path.join(ROOT, "data", "derived")
SITES = ("warmpool", "atlantic", "arctic", "peru", "gyre")
OCEAN_AREA_KM2, OCEAN_DEPTH_M = 361.84e6, 3682.2      # charette:ocean-volume
SIGMA_40_40_10000, Z_10000_KM = 59.82037, 9.712653    # unesco:eos80-checks (in situ, 10000 dbar)


def rho(s, t):
    """Density (kg/m3) of seawater of practical salinity s at temperature t (deg C) and
    one atmosphere: EOS-80 one-atmosphere equation, coefficients of UNESCO 44."""
    rw = ((((6.536332e-9 * t - 1.120083e-6) * t + 1.001685e-4) * t - 9.095290e-3) * t
          + 6.793952e-2) * t + 999.842594
    a = (((5.3875e-9 * t - 8.2467e-7) * t + 7.6438e-5) * t - 4.0899e-3) * t + 8.24493e-1
    b = (-1.6546e-6 * t + 1.0227e-4) * t - 5.72466e-3
    c = 4.8314e-4
    return rw + (a + b * math.sqrt(s) + c * s) * s


def column(name):
    with open(os.path.join(DERIVED, "grade-10-woa23-%s.csv" % name), encoding="utf8") as f:
        return [(float(r["depth_m"]), float(r["value"])) for r in csv.DictReader(f)]


def profile(site, zmax=2000.0):
    t, s = dict(column(site + "-t")), dict(column(site + "-s"))
    return [(z, t[z], s[z], rho(s[z], t[z])) for z in sorted(t) if z in s and z <= zmax]


def at(prof, z):
    for row in prof:
        if row[0] == z:
            return row
    raise KeyError(z)


def mixed_layer_depth(col, dt=0.5):
    """Depth where the temperature first falls dt below its surface value (a simple
    threshold; linear interpolation between standard levels)."""
    t0 = col[0][1]
    for (z1, t1), (z2, t2) in zip(col, col[1:]):
        if t2 < t0 - dt:
            return z1 + (t1 - (t0 - dt)) / (t1 - t2) * (z2 - z1)
    return col[-1][0]


def numbers():
    n = {}
    for site in SITES:
        p = profile(site, zmax=6000)
        n["%s_t0" % site], n["%s_s0" % site], n["%s_rho0" % site] = p[0][1], p[0][2], p[0][3]
        for z in (200, 1000):
            try:
                row = at(p, z)
                n["%s_t%d" % (site, z)], n["%s_s%d" % (site, z)], n["%s_rho%d" % (site, z)] = row[1:]
            except KeyError:
                pass
        n["%s_bottom" % site] = p[-1][0]
        n["%s_tmin" % site] = min(r[1] for r in p)
        n["%s_tmax" % site] = max(r[1] for r in p)
    n["warmpool_dt_0_1000"] = n["warmpool_t0"] - n["warmpool_t1000"]
    n["gyre_drho_0_200"] = n["gyre_rho200"] - n["gyre_rho0"]
    n["peru_drho_0_200"] = n["peru_rho200"] - n["peru_rho0"]
    n["arctic_drho_0_200"] = n["arctic_rho200"] - n["arctic_rho0"]
    feb, aug = column("atlantic-t02"), column("atlantic-t08")
    n["mld_feb"], n["mld_aug"] = mixed_layer_depth(feb), mixed_layer_depth(aug)
    n["feb_t0"], n["aug_t0"] = feb[0][1], aug[0][1]
    n["feb_t300"], n["aug_t300"] = dict(feb)[300.0], dict(aug)[300.0]
    n["rho_35_0"] = rho(35, 0)
    n["rho_35_25"] = rho(35, 25)
    n["rho_0_4"] = rho(0, 4)
    n["rho_35_4"] = rho(35, 4)
    n["drho_per_psu_at10"] = rho(36, 10) - rho(35, 10)
    n["drho_per_degC_at10"] = rho(35, 11) - rho(35, 10)
    n["drho_per_degC_at25"] = rho(35, 26) - rho(35, 25)
    n["drho_per_degC_at0"] = rho(35, 1) - rho(35, 0)
    n["compression_kgm3_per_km"] = (1000.0 + SIGMA_40_40_10000 - rho(40, 40)) / Z_10000_KM
    n["ocean_volume_km3"] = OCEAN_AREA_KM2 * OCEAN_DEPTH_M / 1000.0
    return n


if __name__ == "__main__":
    for site in SITES:
        write_table(__file__, ("depth", "t", "s", "rho"), profile(site), part="site-" + site, digits=6)
    feb, aug = dict(column("atlantic-t02")), dict(column("atlantic-t08"))
    write_table(__file__, ("depth", "t_feb", "t_aug"),
                [(z, feb[z], aug[z]) for z in sorted(feb) if z in aug and z <= 300], part="season", digits=5)
    write_table(__file__, ("t", "rho_s30", "rho_s35", "rho_s38"),
                [(t / 2.0, rho(30, t / 2.0), rho(35, t / 2.0), rho(38, t / 2.0)) for t in range(-4, 61)],
                part="eos", digits=7)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=6)

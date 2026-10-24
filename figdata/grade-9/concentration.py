"""Concentration factors of some metals, time scales of resources, and the
weekend problem of grade 9, chapter 3 (resources from the Earth).

Concentration factor = minimum economic ore grade / average abundance in the
crust (both in percent by mass).

  * Al, Fe, Cu, Zn, Sn, Cr: Perkins and others, Mineralogy, LibreTexts
    section 9.1.04 (ledger perkins:ore-grades).
  * Au: S. Earle, Environmental Geology, Table 8.1 (ledger earle:ore-grades),
    0.003 ppm in average rock, 6 ppm in ore.

Time scales (years), each from the ledger:
  * a swamp keeps its dead plants under water for centuries to millennia to
    build a thick layer (earle:coal);
  * bituminous coal of the United States is 100 to 300 million years old
    (eia:coal);
  * the Chuquicamata open pit has been worked for over 100 years
    (earle:chuquicamata);
  * world copper reserves divided by the 2024 mine production (usgs:mcs-copper).

The problem ("Concrete for a new town") is exercise data.

  main table   : metal crust_pct ore_pct factor x   (x = bar position)
  part times   : item lo_yr hi_yr y
  part problem : item value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

PPM = 1e-4   # 1 ppm = 0.0001 percent by mass

# metal: (crust %, minimum ore grade %)
METALS = [
    ("aluminium", 8.2, 30.0),
    ("iron", 5.6, 20.0),
    ("copper", 0.006, 0.5),
    ("zinc", 0.007, 4.0),
    ("gold", 0.003 * PPM, 6 * PPM),
    ("tin", 0.0002, 0.5),
    ("chromium", 0.01, 30.0),
]

COPPER_RESERVES_2024 = 980e6       # t of copper (usgs:mcs-copper)
COPPER_MINE_2024 = 23.0e6          # t of copper mined in 2024 (usgs:mcs-copper)
COPPER_RESERVES_1970 = 280e6       # t (usgs:mcs-reserves)
COPPER_PRODUCED_SINCE_1970 = 697e6  # t (usgs:mcs-reserves)

TIMES = [  # item, lo, hi (years)
    ("a swamp builds a thick layer of dead plants", 1e2, 1e3),
    ("age of the bituminous coal of the United States", 1e8, 3e8),
    ("Chuquicamata worked so far", 1e2, 1e2),
    ("world copper reserves at the 2024 rate", None, None),
]

# weekend problem: concrete for a new town (exercise data)
HOMES = 2000
AGG_PER_HOME_T = 300.0       # t of aggregates per home, with its share of streets and schools
BUILD_YEARS = 10
SAND_SHARE = 0.40
PIT = dict(length_m=1200.0, width_m=500.0, thickness_m=5.0, extractable=2.0 / 3.0,
           density_t_m3=1.6, other_users_t_yr=1.36e5)
RIVER_SUPPLY_T_YR = 2.0e3
RECYCLED_SHARE = 0.25


def factor(crust, ore):
    return ore / crust


def factors():
    return [(m, c, o, factor(c, o)) for m, c, o in METALS]


def reserve_years(reserve, rate):
    return reserve / rate


def copper_years():
    return reserve_years(COPPER_RESERVES_2024, COPPER_MINE_2024)


def problem():
    p = {}
    p["agg_per_home_kg"] = 100.0 * 1000
    p["agg_total_t"] = HOMES * AGG_PER_HOME_T
    p["agg_per_year_t"] = p["agg_total_t"] / BUILD_YEARS
    p["sand_per_year_t"] = p["agg_per_year_t"] * SAND_SHARE
    p["deposit_m3"] = PIT["length_m"] * PIT["width_m"] * PIT["thickness_m"]
    p["reserve_m3"] = p["deposit_m3"] * PIT["extractable"]
    p["reserve_t"] = p["reserve_m3"] * PIT["density_t_m3"]
    p["extraction_t_yr"] = p["sand_per_year_t"] + PIT["other_users_t_yr"]
    p["river_ratio"] = p["extraction_t_yr"] / RIVER_SUPPLY_T_YR
    p["recycling_saving_t_yr"] = p["sand_per_year_t"] * RECYCLED_SHARE
    p["years"] = reserve_years(p["reserve_t"], p["extraction_t_yr"])
    return p


if __name__ == "__main__":
    rows = [(m, c, o, round(f, 1), i + 1) for i, (m, c, o, f) in enumerate(factors())]
    write_table(__file__, ("metal", "crust_pct", "ore_pct", "factor", "x"), rows)
    cy = copper_years()
    times = []
    for i, (item, lo, hi) in enumerate(TIMES):
        if lo is None:
            lo = hi = round(cy, 1)
        times.append((item.replace(" ", "_"), lo, hi, len(TIMES) - i))
    write_table(__file__, ("item", "lo_yr", "hi_yr", "y"), times, part="times")
    p = problem()
    write_table(__file__, ("item", "value"), [(k, round(v, 3)) for k, v in p.items()], part="problem")
    for m, c, o, f in factors():
        print("%-10s %10.6g %8.4g  x%.1f  (log10 %.2f)" % (m, c, o, f, math.log10(f)))
    print("copper years %.1f" % cy)
    for k, v in p.items():
        print(k, v)

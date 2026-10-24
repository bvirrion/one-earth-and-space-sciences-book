"""India's journey north (grade 12, mountain building).

Past positions of two present-day points, one in central India (78 E, 20 N) and Lhasa
(91.1 E, 29.65 N, north of the suture), in two published plate reconstructions in a
mantle reference frame, MULLER2022 and MULLER2019, from the GPlates Web Service
(tools/fetch_data.py, Book 2 block; data/derived/grade-12-gws-india.csv; ledger
data:b2-gws-india). A change of latitude of one degree is a northward displacement of
2 pi R / 360 = 111.2 km (R = 6371 km, shared ledger earth:Rmean), and 1 km per million
years is 1 mm per year.

Today's convergence of India with Eurasia across the Himalaya comes from the rotation
poles of grade 11 (figdata/grade-11/plate_velocities.py, NNR-MORVEL56), at 85 E 28 N.

  part lat      age m22_india m22_lhasa m19_india m19_lhasa     latitudes (degrees)
  part speed    age_lo age_hi m22 m19                          India's northward speed (mm/yr) in each 5-Myr step
  part steps    age m22 m19                                    the same as a staircase line (two points per step)
  part numbers  key value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "grade-11"))
from _table import write_table  # noqa: E402
import plate_velocities as pv  # noqa: E402

DATA = os.path.join(HERE, "..", "..", "data", "derived", "grade-12-gws-india.csv")
R_KM = 6371.0
KM_PER_DEG = 2 * math.pi * R_KM / 360.0
MODELS = ("MULLER2022", "MULLER2019")
END_CRETACEOUS = 66.0


def load():
    """{model: {age: (india_lat, lhasa_lat)}}"""
    out = {m: {} for m in MODELS}
    with open(DATA, encoding="utf8") as f:
        for r in csv.DictReader(f):
            out[r["model"]][int(r["age_Ma"])] = (float(r["india_lat"]), float(r["lhasa_lat"]))
    return out


def lat(series, age, which=0):
    return series[age][which]


def north_km(series, old, young, which=0):
    """Distance moved north (km) between two ages (Ma), old > young."""
    return (lat(series, young, which) - lat(series, old, which)) * KM_PER_DEG


def mean_speed(series, old, young, which=0):
    """Mean northward speed (mm/yr = km/Myr) between two ages."""
    return north_km(series, old, young, which) / (old - young)


def steps(series, step=5):
    ages = sorted(a for a in series if a % step == 0)
    return [(a, b, mean_speed(series, b, a)) for a, b in zip(ages, ages[1:])]


def numbers():
    d = load()
    s = d["MULLER2022"]
    n = {}
    n["india_lat_66"] = lat(s, 66)
    n["india_lat_80"] = lat(s, 80)
    n["north_since_66_km"] = north_km(s, 66, 0)
    n["north_since_66_km_m19"] = north_km(d["MULLER2019"], 66, 0)
    n["speed_65_50"] = mean_speed(s, 65, 50)
    n["speed_40_0"] = mean_speed(s, 40, 0)
    n["slowdown_ratio"] = n["speed_40_0"] / n["speed_65_50"]
    sp = steps(s)
    fastest = max(sp, key=lambda r: r[2])
    n["fastest_step_lo"], n["fastest_step_hi"], n["fastest_speed"] = fastest
    n["lhasa_north_since_50_km"] = north_km(s, 50, 0, which=1)
    n["india_north_since_50_km"] = north_km(s, 50, 0)
    n["converge_since_50_km"] = n["india_north_since_50_km"] - n["lhasa_north_since_50_km"]
    n["gap_66_km"] = (lat(s, 66, 1) - lat(s, 66, 0)) * KM_PER_DEG
    n["gap_0_km"] = (lat(s, 0, 1) - lat(s, 0, 0)) * KM_PER_DEG
    n["india_lhasa_last5_mm"] = mean_speed(s, 5, 0) - mean_speed(s, 5, 0, which=1)
    ve, vn = pv.relative("in", "eu", 85.0, 28.0)
    n["today_in_eu_speed"] = math.hypot(ve, vn)
    n["today_in_eu_north"] = vn
    n["km_per_deg"] = KM_PER_DEG
    return n


if __name__ == "__main__":
    d = load()
    ages = sorted(d["MULLER2022"])
    write_table(__file__, ("age", "m22_india", "m22_lhasa", "m19_india", "m19_lhasa"),
                [(a, *d["MULLER2022"][a], *d["MULLER2019"][a]) for a in ages], part="lat", digits=6)
    s22, s19 = steps(d["MULLER2022"]), steps(d["MULLER2019"])
    write_table(__file__, ("age_lo", "age_hi", "m22", "m19"),
                [(a, b, v, w) for (a, b, v), (_, _, w) in zip(s22, s19)], part="speed", digits=5)
    write_table(__file__, ("age", "m22", "m19"),
                [r for (a, b, v), (_, _, w) in zip(s22, s19) for r in ((a, v, w), (b, v, w))],
                part="steps", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)

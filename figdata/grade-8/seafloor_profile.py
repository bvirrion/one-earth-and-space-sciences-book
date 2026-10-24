"""Two real seafloor profiles for grade 8, chapter 4 (the oceans).

Source: ETOPO1 relief sampled every degree (shared dataset, ledger
data:etopo1, data/derived/etopo-1deg.csv). Each profile follows one row of
the grid (a parallel), so its points are 1 degree of longitude apart;
narrow features (a trench, the crest of a ridge) are smoothed or missed.

  * South Atlantic along 30.5 S, from Uruguay (59.5 W) to South Africa
    (19.5 E): shelf, slope, abyssal plains, the Mid-Atlantic Ridge.
  * South-east Pacific along 20.5 S, from 89.5 W to 60.5 W: abyssal plain,
    the Peru--Chile trench, the Andes.

Distances are measured along the parallel: 1 degree of longitude is
2 pi R cos(lat) / 360 km (R from the shared ledger, earth:Rmean).

  part atlantic : km elev_m
  part pacific  : km elev_m
  parts atlantic-rock, pacific-rock : the same, closed down to the panel floor
  main table    : item value   (vertical exaggeration of the printed panels,
                                the deepest points, the ridge crest)
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R_EARTH = 6371.0                  # km, ledger earth:Rmean
ATLANTIC = (-30.5, -59.5, 19.5)   # lat, lon west end, lon east end
PACIFIC = (-20.5, -89.5, -60.5)
# printed panel size (cm), used for the vertical exaggeration
ATL_W_CM, ATL_H_CM, ATL_ZMIN, ATL_ZMAX = 14.0, 3.6, -6000.0, 1500.0
PAC_W_CM, PAC_H_CM, PAC_ZMIN, PAC_ZMAX = 7.0, 3.6, -6000.0, 4500.0


def km_per_degree(lat, r=R_EARTH):
    return 2 * math.pi * r * math.cos(math.radians(lat)) / 360.0


def row(lat, lon0, lon1):
    """(lon, elev) along one parallel of the 1-degree grid, west to east."""
    out = []
    with open(os.path.join(ROOT, "data", "derived", "etopo-1deg.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            la, lo = float(r["lat"]), float(r["lon"])
            if abs(la - lat) < 1e-6 and lon0 - 1e-6 <= lo <= lon1 + 1e-6:
                out.append((lo, float(r["elev_m"])))
    return sorted(out)


def profile(spec):
    lat, lon0, lon1 = spec
    k = km_per_degree(lat)
    return [((lo - lon0) * k, z) for lo, z in row(lat, lon0, lon1)]


def vertical_exaggeration(length_km, w_cm, zmin, zmax, h_cm):
    """How many times the heights are stretched compared with the lengths."""
    horiz = length_km * 1000.0 / w_cm      # metres per cm across
    vert = (zmax - zmin) / h_cm            # metres per cm up
    return horiz / vert


if __name__ == "__main__":
    atl, pac = profile(ATLANTIC), profile(PACIFIC)
    write_table(__file__, ("km", "elev_m"), [(round(x, 1), z) for x, z in atl], part="atlantic")
    write_table(__file__, ("km", "elev_m"), [(round(x, 1), z) for x, z in pac], part="pacific")
    # closed polygons of the rock (profile, then down to the panel floor) for filling
    write_table(__file__, ("km", "elev_m"), [(round(x, 1), z) for x, z in atl]
                + [(round(atl[-1][0], 1), ATL_ZMIN), (0.0, ATL_ZMIN)], part="atlantic-rock")
    write_table(__file__, ("km", "elev_m"), [(round(x, 1), z) for x, z in pac]
                + [(round(pac[-1][0], 1), PAC_ZMIN), (0.0, PAC_ZMIN)], part="pacific-rock")
    ve_a = vertical_exaggeration(atl[-1][0], ATL_W_CM, ATL_ZMIN, ATL_ZMAX, ATL_H_CM)
    ve_p = vertical_exaggeration(pac[-1][0], PAC_W_CM, PAC_ZMIN, PAC_ZMAX, PAC_H_CM)
    sea_a = [z for _, z in atl if z < 0]
    ridge = max((z, x) for x, z in atl if 4000 < x < 6500)
    write_table(__file__, ("item", "value"), [
        ("atlantic_length_km", round(atl[-1][0])), ("pacific_length_km", round(pac[-1][0])),
        ("km_per_degree_30.5S", round(km_per_degree(-30.5), 1)),
        ("ve_atlantic", round(ve_a)), ("ve_pacific", round(ve_p)),
        ("atlantic_deepest_m", min(sea_a)), ("ridge_crest_m", ridge[0]), ("ridge_crest_km", round(ridge[1])),
        ("pacific_deepest_m", min(z for _, z in pac)), ("andes_highest_m", max(z for _, z in pac)),
    ])
    print("VE atl %.0f pac %.0f; ridge %s" % (ve_a, ve_p, ridge))

"""The Alpine-Himalayan belt (grade 12, mountain building): high ground and earthquakes.

A regional window from the Atlantic to the east of Tibet. High ground: the cells of
the shared 1-degree ETOPO1 table (data/derived/etopo-1deg.csv; ledger data:etopo1)
higher than 1500 m and than 3500 m (the value of the cell's centre, not a mean, so
single cells are noisy). Earthquakes: the shared USGS catalogue of magnitude 6 or more,
1976-2025 (data/derived/usgs-m6.csv; ledger data:usgs-comcat), shallower than 70 km.

  part high     lon lat                 cells from 1500 to 3500 m
  part higher   lon lat                 cells above 3500 m
  part quakes   lon lat mag             shallow earthquakes in the window
  part numbers  key value
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")
WINDOW = (-12.0, 105.0, 18.0, 52.0)       # lon min, lon max, lat min, lat max
H1, H2 = 1500.0, 3500.0
SHALLOW = 70.0


def inside(lon, lat, w=WINDOW):
    return w[0] <= lon <= w[1] and w[2] <= lat <= w[3]


def cells():
    with open(os.path.join(DERIVED, "etopo-1deg.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            lon, lat, z = float(r["lon"]), float(r["lat"]), float(r["elev_m"])
            if inside(lon, lat):
                yield lon, lat, z


def quakes():
    with open(os.path.join(DERIVED, "usgs-m6.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            lon, lat, d = float(r["lon"]), float(r["lat"]), float(r["depth_km"])
            if inside(lon, lat) and d < SHALLOW:
                yield lon, lat, float(r["mag"])


def numbers():
    cs = list(cells())
    qs = list(quakes())
    tib = [z for lon, lat, z in cs if 80 <= lon <= 95 and 30 <= lat <= 36]   # a box on the Tibetan Plateau
    return {"n_quakes": len(qs), "n_high": sum(1 for *_, z in cs if z >= H1),
            "n_higher": sum(1 for *_, z in cs if z >= H2),
            "tibet_box_mean_m": sum(tib) / len(tib), "tibet_box_n": len(tib)}


if __name__ == "__main__":
    cs = list(cells())
    write_table(__file__, ("lon", "lat"), [(lo, la) for lo, la, z in cs if H1 <= z < H2], part="high")
    write_table(__file__, ("lon", "lat"), [(lo, la) for lo, la, z in cs if z >= H2], part="higher")
    write_table(__file__, ("lon", "lat", "mag"), list(quakes()), part="quakes")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)

"""A dozen cities on a world map with a 30-degree grid (grade 6).

Coordinates from Natural Earth 1:110m populated places
(data/derived/grade-6-ne-places.csv; ledger data:b1-ne-places). The exercises
read the coordinates rounded to the nearest whole degree, and the ideal time
zone from figdata/grade-6/time_zones.py.

  part map  : lon lat name anchor   (~ for spaces in names)
  main table: name lat_deg NS lon_deg EW zone
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from _table import write_table  # noqa: E402
import time_zones  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(HERE))
# name -> label anchor on the map (chosen so that labels do not overlap)
CITIES = {
    "Reykjavík": "south", "London": "south", "New York": "west", "Los Angeles": "east",
    "Quito": "east", "Rio de Janeiro": "west", "Cape Town": "north",
    "Nairobi": "west", "Cairo": "south", "Mumbai": "north", "Tokyo": "west",
    "Sydney": "south", "Auckland": "north east",
}


def load():
    out = {}
    with open(os.path.join(ROOT, "data", "derived", "grade-6-ne-places.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            if r["name"] in CITIES:
                out[r["name"]] = (float(r["lon"]), float(r["lat"]))
    assert set(out) == set(CITIES), set(CITIES) - set(out)
    return out


def rounded(name, pts=None):
    """(|lat| rounded, 'N'/'S', |lon| rounded, 'E'/'W')."""
    lon, lat = (pts or load())[name]
    return (round(abs(lat)), "N" if lat >= 0 else "S", round(abs(lon)), "E" if lon >= 0 else "W")


if __name__ == "__main__":
    pts = load()
    write_table(__file__, ("lon", "lat", "name", "anchor"),
                [(round(pts[n][0], 3), round(pts[n][1], 3), n.replace(" ", "~"), "{%s}" % a if " " in a else a)
                 for n, a in CITIES.items()],
                part="map")
    rows = []
    for n in CITIES:
        la, ns, lo, ew = rounded(n, pts)
        rows.append((n.replace(" ", "~"), la, ns, lo, ew, time_zones.offset(pts[n][0])))
        print(rows[-1])
    write_table(__file__, ("name", "lat_deg", "NS", "lon_deg", "EW", "zone"), rows)

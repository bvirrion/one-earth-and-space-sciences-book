"""How many earthquakes, how deep, and how fast a tsunami crosses the ocean
(grade 7, earthquakes).

Counts come from the shared USGS catalogue of M >= 6 earthquakes, 1976-2025
(data/derived/usgs-m6.csv, ledger data:usgs-comcat). The classes are by
whole magnitude: "6" means 6.0 to 6.9, ..., "9" means 9.0 or more.

The tsunami times use the NOAA deep-ocean speed of about 800 km/h (ledger
nws:tsunami-speed, "over 500 mph") over the great-circle distance from the
2004 epicentre (ledger usgs:largest; the catalogue's own position) to two
capitals of Book 1's Natural Earth places table (data/derived/grade-6-ne-places.csv).
They are ideal times for an exercise: a real wave slows down in shallow water.

  main table   : cls label n per_year           (one row per magnitude class)
  part depth   : n_total n_shallow pct_shallow shallow_km n_deep300 deepest_km
  part tsunami : place dist_km hours minutes
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
YEARS = 50                      # 1976-2025 inclusive
R_KM = 6371.0                   # earth:Rmean
TSUNAMI_KMH = 800.0             # nws:tsunami-speed (over 500 mph)
SHALLOW_KM = 70.0               # "shallow" focus in this chapter's exercise
PLACES = ("Colombo", "Malé")


def _read(name):
    with open(os.path.join(ROOT, "data", "derived", name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def quakes():
    return _read("usgs-m6")


def magnitude_class(mag):
    return min(int(math.floor(float(mag) + 1e-9)), 9)


def counts(data=None):
    """[(cls, n)] for classes 6, 7, 8, 9."""
    data = data or quakes()
    n = {c: 0 for c in (6, 7, 8, 9)}
    for q in data:
        n[magnitude_class(q["mag"])] += 1
    return sorted(n.items())


def per_year(n, years=YEARS):
    return n / years


def shallow_share(data=None, limit_km=SHALLOW_KM):
    data = data or quakes()
    k = sum(1 for q in data if float(q["depth_km"]) <= limit_km)
    return len(data), k, 100.0 * k / len(data)


def deep(data=None, limit_km=300.0):
    """(number of foci deeper than limit_km, deepest focus in km)."""
    data = data or quakes()
    d = [float(q["depth_km"]) for q in data]
    return sum(1 for x in d if x > limit_km), max(d)


def great_circle_km(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dl = math.radians(lon2 - lon1)
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R_KM * math.asin(math.sqrt(h))


def sumatra_2004(data=None):
    data = data or quakes()
    q = [e for e in data if e["date"] == "2004-12-26" and float(e["mag"]) >= 9.0]
    assert len(q) == 1
    return float(q[0]["lat"]), float(q[0]["lon"])


def tsunami_times(data=None):
    lat0, lon0 = sumatra_2004(data)
    places = {p["name"]: p for p in _read("grade-6-ne-places")}
    out = []
    for name in PLACES:
        p = places[name]
        d = great_circle_km(lat0, lon0, float(p["lat"]), float(p["lon"]))
        out.append((name, d, d / TSUNAMI_KMH))
    return out


if __name__ == "__main__":
    data = quakes()
    write_table(__file__, ("cls", "label", "n", "per_year"),
                [(c, "{%d to %d.9}" % (c, c) if c < 9 else "{9 or more}", n, round(per_year(n), 2))
                 for c, n in counts(data)])
    n, k, p = shallow_share(data)
    nd, dmax = deep(data)
    write_table(__file__, ("n_total", "n_shallow", "pct_shallow", "shallow_km", "n_deep300", "deepest_km"),
                [(n, k, round(p, 1), SHALLOW_KM, nd, dmax)], part="depth")
    write_table(__file__, ("place", "dist_km", "hours", "minutes"),
                [("{%s}" % name.replace("é", "\\'e"), round(d), round(h, 2), round(60 * h)) for name, d, h in tsunami_times(data)],
                part="tsunami")

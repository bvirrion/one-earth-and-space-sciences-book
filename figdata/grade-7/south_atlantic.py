"""The width and the age of the South Atlantic (grade 7, plate-tectonics, problem).

Where the parallel LAT crosses the east coast of South America and the west
coast of Africa (Natural Earth 1:110m land, ledger data:ne-land), the length of
one degree of longitude on that parallel (from earth:Rmean), the width of the
ocean along the parallel, the full spreading rate of the Mid-Atlantic Ridge
between South America and Africa near that latitude (mean of the PB2002 steps,
data:pb2002), and the time the ocean would need to open at that speed.

  table: lat lon_america lon_africa km_per_degree width_km rate_cm_a age_Myr
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R_KM = 6371.0            # ledger earth:Rmean
LAT = -23.0              # just north of the tropic, a clean coast crossing on both sides


def _read(name):
    with open(os.path.join(ROOT, "data", "derived", name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def crossings(lat):
    """Longitudes where land outlines cross the parallel `lat`."""
    rings = {}
    for r in _read("ne-land-110m"):
        rings.setdefault(r["ring"], []).append((float(r["lon"]), float(r["lat"])))
    out = []
    for pts in rings.values():
        for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
            if (y0 - lat) * (y1 - lat) < 0:
                out.append(x0 + (lat - y0) * (x1 - x0) / (y1 - y0))
    return out


def coasts(lat=LAT):
    xs = crossings(lat)
    america = max(x for x in xs if -60 < x < -30)       # east coast of South America
    africa = min(x for x in xs if 5 < x < 25)           # west coast of Africa
    return america, africa


def km_per_degree(lat=LAT):
    return 2 * math.pi * R_KM * math.cos(math.radians(lat)) / 360.0


def ridge_rate_cm_a(lat=LAT, half_window=8.0):
    v = [float(s["vel_mm_a"]) for s in _read("pb2002-steps")
         if s["name"] == "AF-SA" and s["class"] == "OSR" and abs(float(s["lat"]) - lat) <= half_window]
    return sum(v) / len(v) / 10.0


def summary():
    am, af = coasts()
    kpd = km_per_degree()
    width = (af - am) * kpd
    rate = ridge_rate_cm_a()
    return am, af, kpd, width, rate, width / (rate * 10.0)      # 1 cm/a = 10 km per million years


if __name__ == "__main__":
    am, af, kpd, width, rate, age = summary()
    write_table(__file__, ("lat", "lon_america", "lon_africa", "km_per_degree", "width_km", "rate_cm_a", "age_Myr"),
                [(LAT, round(am, 2), round(af, 2), round(kpd, 1), round(width), round(rate, 2), round(age))])

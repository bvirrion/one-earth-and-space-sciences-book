"""How fast plates move: relative speeds at six boundaries (grade 7, plate-tectonics).

Each speed is the mean of the PB2002 boundary steps (Bird 2003; ledger
data:pb2002) of one boundary inside a latitude/longitude window: the speed of
one plate relative to the other, in mm per year, printed in the book in cm per
year to one decimal.

  table: rank (slowest first), label (no spaces), speed_cm_a
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# label, PB2002 boundary name, step class, (lat min, lat max, lon min, lon max)
BOUNDARIES = [
    ("North-Atlantic-ridge", "NA-EU", "OSR", (40, 70, -60, 0)),
    ("South-Atlantic-ridge", "AF-SA", "OSR", (-50, 0, -40, 20)),
    ("Himalaya", "EU-IN", "CCB", (25, 35, 70, 100)),
    ("San-Andreas", "NA-PA", "CTF", (33, 40, -125, -114)),
    ("Peru-Chile-trench", "NZ\\SA", "SUB", (-45, -3, -90, -60)),
    ("East-Pacific-Rise", "NZ-PA", "OSR", (-31, 1, -120, -100)),
]


def steps():
    with open(os.path.join(ROOT, "data", "derived", "pb2002-steps.csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def mean_speed_mm_a(name, cls, box, rows=None):
    lat0, lat1, lon0, lon1 = box
    v = [float(r["vel_mm_a"]) for r in (rows or steps())
         if r["name"] == name and r["class"] == cls
         and lat0 <= float(r["lat"]) <= lat1 and lon0 <= float(r["lon"]) <= lon1]
    assert v, (name, cls)
    return sum(v) / len(v), len(v)


def speeds_cm_a():
    rows = steps()
    return [(label, round(mean_speed_mm_a(n, c, b, rows)[0] / 10, 1)) for label, n, c, b in BOUNDARIES]


if __name__ == "__main__":
    write_table(__file__, ("rank", "label", "speed_cm_a"),
                [(i + 1, label, s) for i, (label, s) in
                 enumerate(sorted(speeds_cm_a(), key=lambda t: t[1]))])

"""East and north positions of two satellite-positioning stations against time
(grade 11, plate-motions).

Daily positions from the Nevada Geodetic Laboratory (IGS20 frame, Blewitt, Hammond and
Kreemer 2018; ledger data:b2-ngl-gnss), reduced by tools/fetch_data.py to monthly means
from the first month (data/derived/grade-11-gnss-<site>.csv). The rate of each component
is the slope of the least-squares straight line through the monthly means.

  MKEA  Mauna Kea, Hawaii, Pacific plate, 1996-2026
  WTZR  Wettzell, Germany, Eurasian plate, 1995-2026

  part <site>    year east north   monthly means, in centimetres (every month)
  part numbers   key value          rates (mm/yr), speeds, azimuths, scatter
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITES = ("mkea", "wtzr")


def series(site):
    """[(year, east_mm, north_mm)] monthly means."""
    path = os.path.join(ROOT, "data", "derived", "grade-11-gnss-%s.csv" % site)
    with open(path, encoding="utf8") as f:
        return [(float(r["year"]), float(r["east_mm"]), float(r["north_mm"])) for r in csv.DictReader(f)]


def fit(ts, ys):
    """Least-squares line y = a + b t: (a, b)."""
    n = len(ts)
    mt, my = sum(ts) / n, sum(ys) / n
    b = sum((t - mt) * (y - my) for t, y in zip(ts, ys)) / sum((t - mt) ** 2 for t in ts)
    return my - b * mt, b


def rates(site):
    """(east rate, north rate) in mm/yr, and the RMS scatter about the lines (mm)."""
    s = series(site)
    t = [r[0] for r in s]
    ae, be = fit(t, [r[1] for r in s])
    an, bn = fit(t, [r[2] for r in s])
    res = [(r[1] - ae - be * r[0]) ** 2 + (r[2] - an - bn * r[0]) ** 2 for r in s]
    return be, bn, math.sqrt(sum(res) / (2 * len(s)))


def numbers():
    n = {}
    for site in SITES:
        be, bn, sc = rates(site)
        s = series(site)
        n[site + "_ve"], n[site + "_vn"], n[site + "_scatter"] = be, bn, sc
        n[site + "_speed"] = math.hypot(be, bn)
        n[site + "_az"] = math.degrees(math.atan2(be, bn)) % 360
        n[site + "_t0"], n[site + "_t1"], n[site + "_months"] = s[0][0], s[-1][0], len(s)
        n[site + "_east_total"], n[site + "_north_total"] = s[-1][1], s[-1][2]
    return n


if __name__ == "__main__":
    for site in SITES:
        s = series(site)
        write_table(__file__, ("year", "east", "north"), [(t, e / 10, nn / 10) for t, e, nn in s],
                    part=site, digits=6)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

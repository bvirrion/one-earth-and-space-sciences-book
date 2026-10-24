"""Four climate charts from the NOAA 1991-2020 monthly normals (grade 5).

Reads data/derived/grade-5-normals-<station>.csv (ledger data:b1-noaa-normals;
written by tools/fetch_data.py, Book 1 block: deg F and inches converted to
deg C and mm). One table per station for the charts, and a summary table the
text and the exercises quote.

  part <station> : month (1-12), letter (J F M ...), tavg_C, prcp_mm
  main table     : station, mean_C, coldest_C, warmest_C, range_C, total_mm,
                   wettest_mm, driest_mm, wettest_month, driest_month
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATIONS = ("phoenix", "hilo", "seattle", "utqiagvik")
LETTERS = "JFMAMJJASOND"


def load(station):
    path = os.path.join(ROOT, "data", "derived", "grade-5-normals-%s.csv" % station)
    rows = []
    for r in csv.DictReader(open(path, encoding="utf8")):
        rows.append((int(r["month"]), float(r["tavg_C"]), float(r["prcp_mm"])))
    assert [m for m, _, _ in rows] == list(range(1, 13))
    return rows


def summary(station):
    rows = load(station)
    t = [r[1] for r in rows]
    p = [r[2] for r in rows]
    wet = max(range(12), key=lambda i: p[i])
    dry = min(range(12), key=lambda i: p[i])
    return dict(station=station, mean_C=sum(t) / 12, coldest_C=min(t), warmest_C=max(t),
                range_C=max(t) - min(t), total_mm=sum(p), wettest_mm=p[wet],
                driest_mm=p[dry], wettest_month=wet + 1, driest_month=dry + 1)


if __name__ == "__main__":
    out = []
    for s in STATIONS:
        write_table(__file__, ("month", "letter", "tavg_C", "prcp_mm"),
                    [(m, LETTERS[m - 1], "%.1f" % t, "%.1f" % p) for m, t, p in load(s)],
                    part=s)
        d = summary(s)
        out.append((s, "%.1f" % d["mean_C"], "%.1f" % d["coldest_C"], "%.1f" % d["warmest_C"],
                    "%.1f" % d["range_C"], "%.0f" % d["total_mm"], "%.1f" % d["wettest_mm"],
                    "%.1f" % d["driest_mm"], d["wettest_month"], d["driest_month"]))
        print(out[-1])
    write_table(__file__, ("station", "mean_C", "coldest_C", "warmest_C", "range_C", "total_mm",
                           "wettest_mm", "driest_mm", "wettest_month", "driest_month"), out)

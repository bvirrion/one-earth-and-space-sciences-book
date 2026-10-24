"""Annual flood peaks, return periods and a flood hydrograph of the Potomac River
near Washington DC (grade 10, drainage-basins).

Sources (ledger): USGS station 01646500, annual peak discharges 1931-2025 and daily
mean discharges of January-February 1996 (data:b2-usgs-potomac; derived tables
data/derived/grade-10-usgs-potomac-*.csv written by tools/fetch_data.py).

Return periods by the ranking method: the n annual peaks are sorted from the
largest (rank m = 1) down, and the peak of rank m is given T = (n + 1)/m years.
Equal peaks keep the order of their years.

  part record      year peak                 annual peaks against time (m3/s)
  part ranked      m year peak T             ranked peaks with their return periods
  part hydrograph  day q                     daily mean discharge, day 0 = 1996-01-05
  part chance      n p10 p50 p100            chance of at least one T-year flood in n years
  part numbers     key value
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DERIVED = os.path.join(ROOT, "data", "derived")
MI2_KM2 = 1.609344 ** 2
DRAINAGE_MI2 = 11560.0                      # data:b2-usgs-potomac


def peaks():
    with open(os.path.join(DERIVED, "grade-10-usgs-potomac-peaks.csv"), encoding="utf8") as f:
        return [(int(r["water_year"]), r["date"], float(r["peak_m3s"])) for r in csv.DictReader(f)]


def hydrograph():
    with open(os.path.join(DERIVED, "grade-10-usgs-potomac-dv.csv"), encoding="utf8") as f:
        return [(int(r["day"]), r["date"], float(r["q_m3s"])) for r in csv.DictReader(f)]


def ranked(rows):
    """[(m, year, date, peak, T)] from the largest peak down, T = (n + 1)/m."""
    n = len(rows)
    order = sorted(rows, key=lambda r: (-r[2], r[0]))
    return [(m, y, d, q, (n + 1) / m) for m, (y, d, q) in enumerate(order, start=1)]


def chance(T, n):
    """Probability of at least one flood of return period T in n years."""
    return 1.0 - (1.0 - 1.0 / T) ** n


def numbers():
    p, h = peaks(), hydrograph()
    r = ranked(p)
    qs = sorted(q for _, _, q in p)
    n = len(p)
    out = {"n_years": n, "first_year": p[0][0], "last_year": p[-1][0],
           "T_largest": r[0][4], "largest_year": r[0][1], "largest_m3s": r[0][3],
           "median_peak": qs[n // 2] if n % 2 else 0.5 * (qs[n // 2 - 1] + qs[n // 2]),
           "smallest_peak": qs[0],
           "count_over_9500": sum(1 for q in qs if q > 9500),
           "drainage_km2": DRAINAGE_MI2 * MI2_KM2,
           "chance_100_30": chance(100, 30), "chance_100_100": chance(100, 100),
           "chance_10_10": chance(10, 10), "chance_50_30": chance(50, 30)}
    for m, y, _, q, T in r[:6]:
        out["rank%d_year" % m], out["rank%d_m3s" % m], out["rank%d_T" % m] = y, q, T
    day_max = max(h, key=lambda x: x[2])
    out["hydro_peak_m3s"], out["hydro_peak_day"] = day_max[2], day_max[0]
    out["hydro_before_mean"] = sum(q for d, _, q in h if 5 <= d <= 13) / 9.0
    out["hydro_peak_mm_per_day"] = day_max[2] * 86400.0 / (out["drainage_km2"] * 1e6) * 1000.0
    return out


if __name__ == "__main__":
    p = peaks()
    write_table(__file__, ("year", "peak"), [(y, q) for y, _, q in p], part="record")
    write_table(__file__, ("m", "year", "peak", "T"), [(m, y, q, T) for m, y, _, q, T in ranked(p)],
                part="ranked")
    write_table(__file__, ("day", "q"), [(d, q) for d, _, q in hydrograph()], part="hydrograph")
    write_table(__file__, ("n", "p10", "p50", "p100"),
                [(n, chance(10, n), chance(50, n), chance(100, n)) for n in range(0, 101)], part="chance")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

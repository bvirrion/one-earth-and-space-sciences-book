"""Arctic sea ice in September, 1979--2025, for grade 8, chapter 5 (ice on Earth).

Source: NSIDC Sea Ice Index G02135 v4, September monthly mean extent of the
Arctic (dataset grade-8-nsidc-sep-extent, ledger data:b1-nsidc-sea-ice,
data/derived/grade-8-nsidc-sep-extent.csv). The book stops at 2025, the last
complete year when the chapter was written (the 2026 value is recent and
may be revised).

The straight line is the least-squares fit (school name: "the trend line");
its slope is given per decade.

  part extent : year extent_Mkm2
  part trend  : year extent_Mkm2 (the fitted line, 1979 and 2025)
  main table  : item value
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FIRST, LAST = 1979, 2025


def series(first=FIRST, last=LAST):
    """[(year, extent in million km2)], September means, missing years skipped."""
    out = []
    with open(os.path.join(ROOT, "data", "derived", "grade-8-nsidc-sep-extent.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            y = int(r["year"])
            if first <= y <= last:
                out.append((y, float(r["extent_Mkm2"])))
    return out


def fit(points):
    """Least-squares line: (slope per year, intercept)."""
    n = len(points)
    mx = sum(x for x, _ in points) / n
    my = sum(y for _, y in points) / n
    sxy = sum((x - mx) * (y - my) for x, y in points)
    sxx = sum((x - mx) ** 2 for x, _ in points)
    a = sxy / sxx
    return a, my - a * mx


def decade_mean(points, y0):
    vals = [v for y, v in points if y0 <= y < y0 + 10]
    return sum(vals) / len(vals)


if __name__ == "__main__":
    s = series()
    a, b = fit(s)
    write_table(__file__, ("year", "extent_Mkm2"), s, part="extent")
    write_table(__file__, ("year", "extent_Mkm2"), [(FIRST, round(a * FIRST + b, 3)), (LAST, round(a * LAST + b, 3))],
                part="trend")
    low = min(s, key=lambda p: p[1])
    rows = [("n_years", len(s)), ("first_year", s[0][0]), ("first_value", s[0][1]),
            ("last_year", s[-1][0]), ("last_value", s[-1][1]),
            ("lowest_year", low[0]), ("lowest_value", low[1]),
            ("trend_Mkm2_per_decade", round(10 * a, 3)),
            ("trend_1979", round(a * FIRST + b, 2)), ("trend_2025", round(a * LAST + b, 2)),
            ("mean_1980s", round(decade_mean(s, 1980), 2)), ("mean_2010s", round(decade_mean(s, 2010), 2))]
    write_table(__file__, ("item", "value"), rows)
    for r in rows:
        print(r)

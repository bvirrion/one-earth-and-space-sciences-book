"""The Gutenberg--Richter law read from the world catalogue (Year 1, earthquake-source).

Data: the shared USGS ComCat extract of the earthquakes of magnitude 6 or more,
1976--2025 (data/derived/usgs-m6.csv, ledger data:usgs-comcat). Its magnitudes are
the catalogue's preferred ones, mostly moment magnitudes (mww, mw, mwc, mwb) with
some older surface-wave and body-wave magnitudes.

The cumulative count N(M) of the events of magnitude >= M, for M = 6.0, 6.1, ...,
is divided by the 50 years of the catalogue to give a yearly rate. The b-value is
minus the slope of the least-squares line through log10 N against M, over
FIT_RANGE (where every count is 200 or more, so that its Poisson scatter is under
about 7 per cent).

The moment of each event is M0 = 10**(1.5 M + 9.1) N m (the inverse of the moment
magnitude); the second table gives the share of the total moment released by the
events of magnitude >= M.

  part counts  M N rate              cumulative counts and yearly rates
  part fit     M rate                the fitted line over the plotted range
  part moment  M share               share of the moment released by events >= M
  part values  what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "..", "..", "data", "derived", "usgs-m6.csv")
YEARS = 50.0               # 1976-2025 inclusive
FIT_RANGE = (6.0, 7.5)
STEP = 0.1


def load_magnitudes(path=CSV):
    with open(path, encoding="utf8") as f:
        return [float(r["mag"]) for r in csv.DictReader(f)]


def magnitude_grid(lo, hi, step=STEP):
    n = int(round((hi - lo) / step))
    return [round(lo + i * step, 1) for i in range(n + 1)]


def cumulative_counts(mags, grid):
    """N(M): the number of events of magnitude >= M (magnitudes are given to 0.1)."""
    return [sum(1 for m in mags if m >= M - 1e-9) for M in grid]


def least_squares(xs, ys):
    """Slope and intercept of the least-squares line y = a + s x."""
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    s = sxy / sxx
    return s, my - s * mx


def b_value(mags, lo, hi, years=1.0):
    """Least-squares (a, b) of log10 N = a - b M over lo <= M <= hi, N per `years`."""
    grid = magnitude_grid(lo, hi)
    counts = cumulative_counts(mags, grid)
    s, a = least_squares(grid, [math.log10(c / years) for c in counts])
    return a, -s


def seismic_moment(mw):
    """M0 in N m from the moment magnitude: Mw = (log10 M0 - 9.1) / 1.5."""
    return 10.0 ** (1.5 * mw + 9.1)


def moment_shares(mags, grid):
    total = sum(seismic_moment(m) for m in mags)
    return [sum(seismic_moment(m) for m in mags if m >= M - 1e-9) / total for M in grid]


def main():
    mags = load_magnitudes()
    grid = magnitude_grid(6.0, max(mags))
    counts = cumulative_counts(mags, grid)
    write_table(__file__, ("M", "N", "rate"),
                [(M, c, c / YEARS) for M, c in zip(grid, counts)], part="counts")
    a, b = b_value(mags, *FIT_RANGE, years=YEARS)
    write_table(__file__, ("M", "rate"),
                [(M, 10 ** (a - b * M)) for M in (5.8, 9.3)], part="fit")
    shares = moment_shares(mags, grid)
    write_table(__file__, ("M", "share"), list(zip(grid, shares)), part="moment")
    total = sum(seismic_moment(m) for m in mags)
    top2 = sorted((seismic_moment(m) for m in mags), reverse=True)[:2]
    values = [
        ("events", len(mags)),
        ("a_per_year", a),
        ("b", b),
        ("rate_ge_7", 10 ** (a - 7 * b)),
        ("rate_ge_8", 10 ** (a - 8 * b)),
        ("total_moment_Nm", total),
        ("moment_per_year_Nm", total / YEARS),
        ("share_ge_8", shares[grid.index(8.0)]),
        ("count_ge_8", counts[grid.index(8.0)]),
        ("share_top2", sum(top2) / total),
    ]
    write_table(__file__, ("what", "value"), values, part="values")


if __name__ == "__main__":
    main()

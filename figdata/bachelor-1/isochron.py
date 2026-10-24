"""A rubidium-strontium whole-rock isochron fitted by least squares (Year 1,
radiometric-methods).

Exercise data: six whole-rock samples of an invented rhyolite lava series,
made from an age of 425 Ma and an initial 87Sr/86Sr of 0.70610 with small
scatter added (fixed offsets, so that the table never changes).
The decay constant of 87Rb is the ledger's (villa22:rb87). The least-squares
line, its standard errors and the age follow the method of the chapter.

  part points   x y               (87Rb/86Sr, 87Sr/86Sr of each sample)
  part line     x y               (fitted line, x 0-30)
  part initial  x y               (the initial ratio, a horizontal line)
  part values   what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

LAMBDA_RB = 1.3972e-11      # per year (villa22:rb87)

AGE_MA = 425.0              # synthetic age of the exercise rhyolite
INITIAL = 0.70610           # synthetic initial 87Sr/86Sr
X = (1.85, 4.62, 9.30, 14.75, 21.20, 27.60)
SCATTER = (2.0e-4, -3.0e-4, 1.5e-4, 2.5e-4, -1.0e-4, -2.0e-4)   # fixed scatter


def slope_for(age_ma, lam=LAMBDA_RB):
    """Isochron slope e^(lambda t) - 1 for an age in Ma."""
    return math.expm1(lam * age_ma * 1e6)


def age_from_slope(m, lam=LAMBDA_RB):
    """Age in Ma from an isochron slope: t = ln(1 + m)/lambda."""
    return math.log1p(m) / lam / 1e6


def synthetic(xs, age_ma, initial, scatter=None):
    m = slope_for(age_ma)
    scatter = scatter or (0.0,) * len(xs)
    return [initial + m * x + e for x, e in zip(xs, scatter)]


def lsq(xs, ys):
    """Least-squares line y = b + m x: (m, b, s, sigma_m, sigma_b).

    s is the standard deviation of the residuals with n - 2 degrees of freedom."""
    n = len(xs)
    xm, ym = sum(xs) / n, sum(ys) / n
    sxx = sum((x - xm) ** 2 for x in xs)
    sxy = sum((x - xm) * (y - ym) for x, y in zip(xs, ys))
    m = sxy / sxx
    b = ym - m * xm
    res = [y - (b + m * x) for x, y in zip(xs, ys)]
    s = math.sqrt(sum(r * r for r in res) / (n - 2))
    return m, b, s, s / math.sqrt(sxx), s * math.sqrt(1.0 / n + xm * xm / sxx)


def age_sigma(m, sigma_m, lam=LAMBDA_RB):
    """Standard uncertainty of the age (Ma) from that of the slope."""
    return sigma_m / (lam * (1.0 + m)) / 1e6


def data():
    """The printed table: ratios rounded to five decimals, as measured."""
    return list(X), [round(y, 5) for y in synthetic(X, AGE_MA, INITIAL, SCATTER)]


if __name__ == "__main__":
    xs, ys = data()
    m, b, s, sm, sb = lsq(xs, ys)
    write_table(__file__, ("x", "y"), list(zip(xs, ys)), part="points", digits=7)
    write_table(__file__, ("x", "y"), [(0.0, b), (30.0, b + 30.0 * m)], part="line", digits=7)
    write_table(__file__, ("x", "y"), [(0.0, b), (30.0, b)], part="initial", digits=7)
    vals = [("slope", m), ("intercept", b), ("s_residuals", s), ("sigma_slope", sm),
            ("sigma_intercept", sb), ("age_Ma", age_from_slope(m)),
            ("sigma_age_Ma", age_sigma(m, sm)), ("xmean", sum(xs) / len(xs)),
            ("ymean", sum(ys) / len(ys))]
    write_table(__file__, ("what", "value"), vals, part="values", digits=7)

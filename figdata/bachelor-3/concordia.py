"""U-Pb concordia and discordia (Year 3, advanced geochronology).

Decay constants and the present 235U/238U from the ledger row
amherst:constants (lambda238 = 1.55125e-10 /yr, lambda235 = 9.8485e-10 /yr,
235U/238U = 0.0072567, i.e. 238U/235U = 137.8).

Wetherill concordia: x = 207Pb*/235U = exp(l235 t) - 1, y = 206Pb*/238U =
exp(l238 t) - 1. Tera-Wasserburg: X = 238U/206Pb* = 1/y,
Y = 207Pb*/206Pb* = x / (137.8 y).

A crystal of age t1 that lost a fraction f of its radiogenic lead at t2 plots
at (1 - f) C(t1) + f C(t2): the discordia is the chord. The five zircons of
the Varden granite are invented (t1 = 310 Ma, t2 = 95 Ma) with a fixed
scatter, rounded as printed in the weekend problem; the line is fitted with
the errors of y only (x treated as exact), as the problem does.

  part curve    t xw yw xtw ytw          (t in Ma; t >= 30 Ma for the TW part)
  part ticks    t xw yw xtw ytw          every 50 Ma from 50 to 400
  part zircons  name x y sy xtw ytw      (printed values)
  part ellipses one closed curve per zircon: e x y (2 sigma, rho = 0.85)
  part line     x y                      the fitted discordia, extended
  part twline   xtw ytw                  the same line in Tera-Wasserburg coordinates
  part values   what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

L238 = 1.55125e-10
L235 = 9.8485e-10
U85 = 137.8
T1, T2 = 310.0, 95.0
FRACTIONS = (0.04, 0.12, 0.21, 0.30, 0.40)
NOISE = (0.6, -0.9, 0.4, -0.3, 0.5)   # in units of sigma_y
REL_SY = 0.002                         # 1 sigma, relative, on y
REL_SX = 0.0025
RHO = 0.85


def concordia(t_ma):
    t = np.asarray(t_ma, dtype=float) * 1e6
    return np.expm1(L235 * t), np.expm1(L238 * t)


def tera_wasserburg(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    return 1.0 / y, x / (U85 * y)


def age206(y):
    return math.log1p(y) / L238 / 1e6


def age207(x):
    return math.log1p(x) / L235 / 1e6


def lead_loss_point(t1, t2, f):
    x1, y1 = concordia(t1)
    x2, y2 = concordia(t2)
    return (1 - f) * x1 + f * x2, (1 - f) * y1 + f * y2


def lead_loss_explicit(t1, t2, f):
    """Same point from the history: growth, loss of f at t2, growth again."""
    out = []
    for lam in (L235, L238):
        grown = math.exp(lam * (t1 - t2) * 1e6) - 1.0       # Pb/U at t2, per U then
        kept = (1 - f) * grown * math.exp(lam * t2 * 1e6)     # per U now
        out.append(kept + math.expm1(lam * t2 * 1e6))
    return tuple(out)


def zircons():
    rows = []
    for k, (f, e) in enumerate(zip(FRACTIONS, NOISE)):
        x, y = lead_loss_point(T1, T2, f)
        sy = REL_SY * y
        y = y + e * sy
        rows.append(("Z%d" % (k + 1), round(float(x), 4), round(float(y), 5),
                     round(float(sy), 5)))
    return rows


def fit_line(xs, ys, sys_):
    """Weighted least squares of y on x: y = a + b x; returns a, b, s_b, x_bar, y_bar, mswd."""
    xs, ys, w = np.asarray(xs), np.asarray(ys), 1.0 / np.asarray(sys_) ** 2
    xb = np.sum(w * xs) / np.sum(w)
    yb = np.sum(w * ys) / np.sum(w)
    sxx = np.sum(w * (xs - xb) ** 2)
    b = np.sum(w * (xs - xb) * (ys - yb)) / sxx
    a = yb - b * xb
    r = ys - a - b * xs
    mswd = np.sum(w * r ** 2) / (len(xs) - 2)
    return a, b, 1.0 / math.sqrt(sxx), xb, yb, mswd


def intercepts(a, b, guess_hi=400.0, guess_lo=50.0):
    """Ages where y = a + b x meets the concordia (Newton on t)."""
    def g(t):
        x, y = concordia(t)
        return float(y - a - b * x)

    def dg(t):
        return float(L238 * 1e6 * math.exp(L238 * t * 1e6) - b * L235 * 1e6 * math.exp(L235 * t * 1e6))

    out = []
    for t in (guess_hi, guess_lo):
        for _ in range(60):
            t = t - g(t) / dg(t)
        out.append(t)
    return tuple(out)


def pivot_intercepts(a, b, s_b, xb, yb, k=2.0):
    """Upper intercepts for the line pivoted about its weighted centroid by +-k s_b."""
    res = []
    for bb in (b - k * s_b, b + k * s_b):
        aa = yb - bb * xb
        res.append(intercepts(aa, bb)[0])
    return tuple(sorted(res))


def ellipse(x, y, sx, sy, rho, k=2.0, n=60):
    cov = np.array([[sx * sx, rho * sx * sy], [rho * sx * sy, sy * sy]])
    vals, vecs = np.linalg.eigh(cov)
    th = np.linspace(0, 2 * math.pi, n + 1)
    pts = (vecs @ (np.sqrt(vals)[:, None] * k * np.vstack([np.cos(th), np.sin(th)])))
    return x + pts[0], y + pts[1]


def main():
    ts = np.concatenate([np.linspace(0, 450, 91)])
    xw, yw = concordia(ts)
    rows = []
    for t, x, y in zip(ts, xw, yw):
        if t >= 30:
            xt, yt = tera_wasserburg(x, y)
        else:
            xt, yt = float("nan"), float("nan")
        rows.append([t, x, y, xt, yt])
    write_table(__file__, ("t", "xw", "yw", "xtw", "ytw"), rows, part="curve")
    tt = np.arange(50, 401, 50)
    xw, yw = concordia(tt)
    xt, yt = tera_wasserburg(xw, yw)
    write_table(__file__, ("t", "xw", "yw", "xtw", "ytw"),
                [list(r) for r in zip(tt, xw, yw, xt, yt)], part="ticks")

    zs = zircons()
    rows = []
    for name, x, y, sy in zs:
        xt, yt = tera_wasserburg(x, y)
        rows.append([name, x, y, sy, float(xt), float(yt)])
    write_table(__file__, ("name", "x", "y", "sy", "xtw", "ytw"), rows, part="zircons")
    rows = []
    for k, (name, x, y, sy) in enumerate(zs):
        ex, ey = ellipse(x, y, REL_SX * x, sy, RHO)
        rows += [[k + 1, a, b] for a, b in zip(ex, ey)]
        rows.append(["nan", "nan", "nan"])
    write_table(__file__, ("e", "x", "y"), rows, part="ellipses")

    a, b, s_b, xb, yb, mswd = fit_line([z[1] for z in zs], [z[2] for z in zs], [z[3] for z in zs])
    up, lo = intercepts(a, b)
    xl = np.array([0.06, 0.42])
    write_table(__file__, ("x", "y"), [[x, a + b * x] for x in xl], part="line")
    # the same line in Tera-Wasserburg coordinates: Y = (1 - a X) / (137.8 b)
    xt = np.array([18.0, 75.0])
    write_table(__file__, ("xtw", "ytw"), [[x, (1 - a * x) / (U85 * b)] for x in xt],
                part="twline")
    lo_up, hi_up = pivot_intercepts(a, b, s_b, xb, yb)
    write_table(__file__, ("what", "value"), [
        ["a", a], ["b", b], ["s_b", s_b], ["x_bar", xb], ["y_bar", yb], ["mswd", mswd],
        ["upper", up], ["lower", lo], ["upper_minus_2s", lo_up], ["upper_plus_2s", hi_up],
    ], part="values")


if __name__ == "__main__":
    main()

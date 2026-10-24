"""Pumping tests: the Theis well function, the Cooper--Jacob line, the cone of
depression and the interference of two wells (Year 3, hydrogeology).

    s(r, t) = Q W(u) / (4 pi T),   u = r^2 S / (4 T t),   W(u) = E1(u)

(ledger heath:theis). The Cooper--Jacob form, valid once u <= 0.05
(heath:jacob), is s = (2.3 Q / 4 pi T) log10(2.25 T t / (r^2 S)).

The invented well Varden-3 is drilled at (4500, 5000) on the grid of the Varden
Hills (figdata/shared/region.py, read only): ground at 363 m, the Jurassic shale
from the surface to 80 m, the Jurassic limestone below it, 180 m thick, a
confined aquifer. The test parameters are invented: T = 450 m2/d (K = 2.5 m/d,
inside the carbonate range of heath:k-chart), S = 2e-4 (heath:storage), Q = 2160
m3/d (25 L/s), an observation well at r = 60 m. The 'measured' drawdowns are
the Theis values plus a deterministic error of a few millimetres (a fixed
pseudo-random sequence) and rounded to the centimetre.

  part wu       u W invu           the well function and the Cooper--Jacob line
  part cj       invu Wcj           -0.5772 - ln u, for u <= 1
  part cone-<d> r s                drawdown against distance after d days
  part interf   x s1 s2 stot       two wells 400 m apart, 10 days, along their line
  part test     tmin s             the Varden-3 observation-well record
  part values   what value
"""
import math
import os
import sys

import numpy as np
from scipy.special import exp1

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

EULER = 0.5772156649015329
T_TRUE = 450.0         # m2/d
S_TRUE = 2.0e-4
Q = 2160.0             # m3/d
R_OBS = 60.0           # m
WELL_XY = (4500.0, 5000.0)
TEST_MIN = [1, 2, 3, 5, 7, 10, 15, 20, 30, 45, 60, 90, 120, 180, 240, 360, 480,
            720, 960, 1440, 2160, 2880]


def well_function(u):
    return exp1(u)


def drawdown(r, t, T=T_TRUE, S=S_TRUE, q=Q):
    """Theis drawdown (m) at distance r (m) after t days."""
    u = r * r * S / (4.0 * T * t)
    return q * well_function(u) / (4.0 * math.pi * T)


def jacob(r, t, T=T_TRUE, S=S_TRUE, q=Q):
    return 2.3 * q / (4.0 * math.pi * T) * math.log10(2.25 * T * t / (r * r * S))


def site():
    """Elevations at Varden-3: ground, top and base of the limestone."""
    x, y = WELL_XY
    g = region.topo(x, y)
    top = region.contact_elevation("shale", x, y)
    base = region.contact_elevation("limestone", x, y)
    return g, top, base


def test_record():
    """Synthetic record: Theis + deterministic small errors, rounded to 1 cm."""
    rng = np.random.default_rng(23)
    errs = rng.normal(0.0, 0.004, len(TEST_MIN))
    rows = []
    for m, e in zip(TEST_MIN, errs):
        s = drawdown(R_OBS, m / 1440.0) + e
        rows.append((m, round(s, 2)))
    return rows


def fit_jacob(rows, umax=0.05, S_guess=S_TRUE, T_guess=T_TRUE):
    """Least-squares line s = a + b log10 t through the late points (u <= umax)."""
    pts = [(math.log10(m / 1440.0), s) for m, s in rows
           if R_OBS ** 2 * S_guess / (4 * T_guess * m / 1440.0) <= umax]
    xs = np.array([p[0] for p in pts])
    ys = np.array([p[1] for p in pts])
    b, a = np.polyfit(xs, ys, 1)
    T = 2.3 * Q / (4 * math.pi * b)
    t0 = 10 ** (-a / b)
    S = 2.25 * T * t0 / R_OBS ** 2
    return T, S, b, t0, len(pts)


def radius_of_influence(t, T=T_TRUE, S=S_TRUE):
    """Jacob's r0, where the distance-drawdown line meets zero drawdown."""
    return math.sqrt(2.25 * T * t / S)


def main():
    us = np.logspace(-4, 1, 101)
    write_table(__file__, ("u", "W", "invu"), [(u, well_function(u), 1 / u) for u in us], part="wu")
    uc = np.logspace(-4, 0, 41)
    write_table(__file__, ("invu", "Wcj"), [(1 / u, -EULER - math.log(u)) for u in uc], part="cj")
    rs = np.logspace(0, math.log10(5000.0), 121)
    for d in (1, 10, 100):
        write_table(__file__, ("r", "s"), [(r, drawdown(r, d)) for r in rs], part="cone-%d" % d)
    rows = []
    for x in np.linspace(-1500.0, 1900.0, 341):
        r1 = max(abs(x), 0.15)
        r2 = max(abs(x - 400.0), 0.15)
        s1, s2 = drawdown(r1, 10.0), drawdown(r2, 10.0)
        rows.append((x, s1, s2, s1 + s2))
    write_table(__file__, ("x", "s1", "s2", "stot"), rows, part="interf")
    rec = test_record()
    write_table(__file__, ("tmin", "s"), rec, part="test")
    T, S, b, t0, n = fit_jacob(rec)
    g, top, base = site()
    vals = [["ground", g], ["top_limestone", top], ["base_limestone", base],
            ["shale_thickness", g - top], ["b", top - base],
            ["K", T_TRUE / (top - base)], ["Q_over_4piT", Q / (4 * math.pi * T_TRUE)],
            ["fit_T", T], ["fit_S", S], ["fit_slope", b], ["fit_t0_min", t0 * 1440], ["fit_n", n],
            ["tc_min", 1440 * R_OBS ** 2 * S_TRUE / (4 * T_TRUE * 0.05)],
            ["s_60m_2d_theis", drawdown(R_OBS, 2.0)], ["s_60m_2d_jacob", jacob(R_OBS, 2.0)],
            ["r0_30d", radius_of_influence(30.0)], ["s_1km_30d", drawdown(1000.0, 30.0)],
            ["s_1km_30d_u", 1e6 * S_TRUE / (4 * T_TRUE * 30)],
            ["interf_mid_10d", 2 * drawdown(200.0, 10.0)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

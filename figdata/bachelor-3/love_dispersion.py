"""Dispersion of fundamental-mode Love waves in a layer over a half-space (Year 3,
seismology-imaging).

Model (a model crust over a model mantle, rounded values chosen for the chapter,
not a measurement): layer of thickness H = 35 km, S velocity b1 = 3.5 km/s,
density 2.7 g/cm3; half-space b2 = 4.5 km/s, density 3.3 g/cm3; rigidities
mu = rho b^2. The chapter's theorem gives, for the phase velocity c
(b1 < c < b2) at the angular frequency w,
    tan(w H s1) = mu2 s2 / (mu1 s1),   s1 = sqrt(1/b1^2 - 1/c^2),
                                       s2 = sqrt(1/c^2 - 1/b2^2);
the fundamental mode is the root with w H s1 in (0, pi/2). It is found by
bisection; the group velocity U = dw/dk (k = w / c) by centred differences on
a fine grid of periods.

  part curve     period c U          (s, km/s, km/s), periods 3-150 s
  part values    what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

H = 35.0
B1, RHO1 = 3.5, 2.7
B2, RHO2 = 4.5, 3.3


def residual(c, w, h=H, b1=B1, b2=B2, r1=RHO1, r2=RHO2):
    s1 = math.sqrt(1.0 / b1 ** 2 - 1.0 / c ** 2)
    s2 = math.sqrt(1.0 / c ** 2 - 1.0 / b2 ** 2)
    return math.tan(w * h * s1) - (r2 * b2 ** 2 * s2) / (r1 * b1 ** 2 * s1)


def phase_velocity(period, h=H, b1=B1, b2=B2, r1=RHO1, r2=RHO2):
    w = 2.0 * math.pi / period
    # w h s1 must stay below pi/2: largest admissible c
    smax = min(math.sqrt(1.0 / b1 ** 2 - 1.0 / b2 ** 2), (math.pi / 2) / (w * h) * (1 - 1e-12))
    c_hi = 1.0 / math.sqrt(1.0 / b1 ** 2 - smax ** 2)
    c_hi = min(c_hi, b2 * (1 - 1e-12))
    lo, hi = b1 * (1 + 1e-12), c_hi
    f = lambda c: residual(c, w, h, b1, b2, r1, r2)  # noqa: E731
    # f(lo) -> -inf (s1 -> 0), f(hi) > 0 if the root lies inside
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def group_velocity(period, dp=1e-3, **kw):
    w0 = 2 * math.pi / period
    w1, w2 = w0 * (1 - dp), w0 * (1 + dp)
    k1 = w1 / phase_velocity(2 * math.pi / w1, **kw)
    k2 = w2 / phase_velocity(2 * math.pi / w2, **kw)
    return (w2 - w1) / (k2 - k1)


def curve(periods):
    return [(t, phase_velocity(t), group_velocity(t)) for t in periods]


PERIODS = [3.0 * (150.0 / 3.0) ** (j / 120.0) for j in range(121)]

if __name__ == "__main__":
    rows = curve(PERIODS)
    write_table(__file__, ("period", "c", "U"), rows, part="curve")
    umin = min(rows, key=lambda r: r[2])
    vals = [("Umin", round(umin[2], 3)), ("T_Umin", round(umin[0], 1))]
    for t in (10, 20, 30, 50, 100):
        vals += [("c%d" % t, round(phase_velocity(t), 3)), ("U%d" % t, round(group_velocity(t), 3))]
    write_table(__file__, ("what", "value"), vals, part="values")

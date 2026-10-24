"""Seismic refraction over a two-layer Earth (Year 1, layered-earth): travel times of the
direct, reflected and head waves from a surface source over a layer of thickness h and
speed v1 resting on a half-space of speed v2 > v1.

  direct      t = x / v1
  reflected   t = sqrt(x^2 + 4 h^2) / v1
  head wave   t = x / v2 + 2 h cos(ic) / v1,  sin(ic) = v1 / v2,  for x >= x_crit
  crossover   x_c = 2 h sqrt((v2 + v1) / (v2 - v1))

The model is a generic continental crust (h = 35 km, v1 = 6.0 km/s) over the mantle
(v2 = 8.0 km/s): round numbers of the order of PREM's (5.8--6.8 and 8.11 km/s) and of
the 35-km average continental Moho depth (ledger prem:moho-average), chosen for the exercises.

  part times   x t_direct t_reflected t_head   (t_head = nan before the critical distance)
  part rays    x z                             ray paths of the figure: direct, reflected at
                                               the critical distance, and one head-wave ray
                                               to x = 250 km (separated by nan rows)
  part values  what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

H = 35.0       # km
V1 = 6.0       # km/s
V2 = 8.0       # km/s
X_MAX = 400.0  # km


def critical_angle(v1=V1, v2=V2):
    return math.asin(v1 / v2)


def t_direct(x, v1=V1):
    return x / v1


def t_reflected(x, h=H, v1=V1):
    return math.hypot(x, 2.0 * h) / v1


def critical_distance(h=H, v1=V1, v2=V2):
    return 2.0 * h * math.tan(critical_angle(v1, v2))


def intercept(h=H, v1=V1, v2=V2):
    return 2.0 * h * math.cos(critical_angle(v1, v2)) / v1


def t_head(x, h=H, v1=V1, v2=V2):
    if x < critical_distance(h, v1, v2) - 1e-12:
        return float("nan")
    return x / v2 + intercept(h, v1, v2)


def crossover(h=H, v1=V1, v2=V2):
    """Distance at which the head wave overtakes the direct wave (the theorem)."""
    return 2.0 * h * math.sqrt((v2 + v1) / (v2 - v1))


def depth_from_crossover(xc, v1=V1, v2=V2):
    return 0.5 * xc * math.sqrt((v2 - v1) / (v2 + v1))


def depth_from_intercept(ti, v1=V1, v2=V2):
    return ti * v1 / (2.0 * math.cos(critical_angle(v1, v2)))


def crossover_numeric(h=H, v1=V1, v2=V2, lo=None, hi=X_MAX):
    """Bisection on t_direct - t_head, for the test."""
    lo = critical_distance(h, v1, v2) if lo is None else lo
    f = lambda x: t_direct(x, v1) - t_head(x, h, v1, v2)
    a, b = lo, hi
    for _ in range(200):
        c = 0.5 * (a + b)
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c
    return 0.5 * (a + b)


def rays(x_far=250.0):
    ic = critical_angle()
    xc = critical_distance()
    leg = H * math.tan(ic)
    out = [(0.0, 0.0), (x_far, 0.0), ("nan", "nan"),
           (0.0, 0.0), (xc / 2.0, -H), (xc, 0.0), ("nan", "nan"),
           (0.0, 0.0), (leg, -H), (x_far - leg, -H), (x_far, 0.0)]
    return out


if __name__ == "__main__":
    xs = [i * 2.0 for i in range(int(X_MAX / 2) + 1)]
    xcrit = critical_distance()
    if xcrit not in xs:
        xs = sorted(xs + [xcrit])
    rows = [(x, t_direct(x), t_reflected(x), t_head(x)) for x in xs]
    rows = [(x, a, b, "nan" if math.isnan(c) else c) for x, a, b, c in rows]
    write_table(__file__, ("x", "t_direct", "t_reflected", "t_head"), rows, part="times", digits=6)
    write_table(__file__, ("x", "z"), rays(), part="rays", digits=6)
    vals = [("critical_angle_deg", math.degrees(critical_angle())), ("critical_distance", xcrit),
            ("intercept_s", intercept()), ("crossover", crossover()),
            ("crossover_time_s", t_direct(crossover()))]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

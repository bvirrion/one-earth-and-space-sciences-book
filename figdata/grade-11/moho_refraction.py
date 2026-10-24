"""Direct and refracted waves over a crust of thickness h on a faster mantle
(grade 11, seismic-structure).

A source at the surface; a crust of speed v1 and thickness h over a mantle of speed
v2 > v1. The direct wave reaches a station at distance x after x/v1. The head wave
goes down at the critical angle ic (sin ic = v1/v2), runs along the top of the mantle
at v2 and comes back up at ic:

    t(x) = x/v2 + 2 h cos(ic) / v1          (for x beyond the critical distance
                                             2 h tan ic)

It overtakes the direct wave beyond the crossover distance
x_c = 2 h sqrt((v2 + v1)/(v2 - v1)).

The weekend problem's region is invented: its arrival times are computed from the
model below, with a reading error of up to +-0.1 s (fixed pseudo-random sequence),
rounded to 0.1 s.

  part model     x tdirect thead       the two lines, 0-300 km
  part stations  x pg pn               the problem's readings ('nan' where absent)
  part numbers   key value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

V1, V2, H = 6.2, 8.1, 30.0          # km/s, km/s, km: the invented region (chosen)
STATIONS = list(range(20, 301, 20))


def critical_angle(v1=V1, v2=V2):
    return math.asin(v1 / v2)


def t_direct(x, v1=V1):
    return x / v1


def intercept(v1=V1, v2=V2, h=H):
    return 2 * h * math.cos(critical_angle(v1, v2)) / v1


def t_head(x, v1=V1, v2=V2, h=H):
    return x / v2 + intercept(v1, v2, h)


def t_head_geometric(x, v1=V1, v2=V2, h=H):
    """The same time from the path itself: two slanted legs in the crust and the leg
    along the interface."""
    ic = critical_angle(v1, v2)
    leg = h / math.cos(ic)
    along = x - 2 * h * math.tan(ic)
    return 2 * leg / v1 + along / v2


def critical_distance(v1=V1, v2=V2, h=H):
    return 2 * h * math.tan(critical_angle(v1, v2))


def crossover(v1=V1, v2=V2, h=H):
    return 2 * h * math.sqrt((v2 + v1) / (v2 - v1))


def depth_from(t_i, v1, v2):
    """Crust thickness from the intercept time and the two speeds."""
    return t_i * v1 * v2 / (2 * math.sqrt(v2 * v2 - v1 * v1))


def readings():
    """(x, Pg, Pn) as a seismologist would read them: model time + error, 0.1 s."""
    seq = [0.07, -0.04, 0.02, -0.08, 0.05, 0.0, -0.06, 0.09, -0.02, 0.04, -0.09, 0.06,
           -0.03, 0.08, -0.05, 0.01, -0.07, 0.03, 0.06, -0.01, 0.05, -0.08, 0.02, -0.04,
           0.07, -0.06, 0.04, -0.02, 0.09, -0.05]
    out = []
    for k, x in enumerate(STATIONS):
        pg = round(t_direct(x) + seq[2 * k], 1) if x <= 200 else float("nan")
        pn = round(t_head(x) + seq[2 * k + 1], 1) if x >= 80 else float("nan")
        out.append((x, pg, pn))
    return out


def fit_line(pts):
    """Least-squares line t = a + b x: (a, b)."""
    n = len(pts)
    mx = sum(x for x, _ in pts) / n
    mt = sum(t for _, t in pts) / n
    b = sum((x - mx) * (t - mt) for x, t in pts) / sum((x - mx) ** 2 for x, _ in pts)
    return mt - b * mx, b


def numbers():
    r = readings()
    a1, b1 = fit_line([(x, pg) for x, pg, _ in r if pg == pg])
    a2, b2 = fit_line([(x, pn) for x, _, pn in r if pn == pn])
    v1, v2 = 1 / b1, 1 / b2
    return {"ic_deg": math.degrees(critical_angle()), "intercept_s": intercept(),
            "critical_km": critical_distance(), "crossover_km": crossover(),
            "fit_v1": v1, "fit_v2": v2, "fit_intercept_s": a2, "fit_direct_t0": a1,
            "fit_depth_km": depth_from(a2, v1, v2),
            "fit_crossover_km": (a2 - a1) / (b1 - b2)}


if __name__ == "__main__":
    write_table(__file__, ("x", "tdirect", "thead"),
                [(x, t_direct(x), t_head(x)) for x in range(0, 301, 5)], part="model", digits=5)
    write_table(__file__, ("x", "pg", "pn"), readings(), part="stations", digits=4)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

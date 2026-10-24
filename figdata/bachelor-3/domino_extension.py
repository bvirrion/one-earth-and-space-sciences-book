"""Domino faulting and the frictional lock-up of normal faults (Year 3,
extensional and strike-slip tectonics).

Rigid dominoes: parallel planar faults, dip theta0 at the start, perpendicular
spacing d kept by the rigid blocks; the horizontal spacing is d / sin(theta),
so the extension factor is
    beta = sin(theta0) / sin(theta)
when the faults have rotated to the dip theta (the bedding then dips
theta0 - theta the other way).

Frictional reactivation (cohesionless fault, friction coefficient mu, effective
principal stresses, sigma1 vertical): a plane at the angle t from sigma1 (fault
dip = 90 - t) slips when
    R = sigma1 / sigma3 = (1 + mu cot t) / (1 - mu tan t),
which is least at tan 2t = 1/mu, R_min = (sqrt(1 + mu^2) + mu)^2, and infinite
(lock-up) at tan t = 1/mu, i.e. at the fault dip arctan(mu). Byerlee's mu:
0.6 and 0.85 (ledger byerlee:1975, Book 3).

  part beta      dip b45 b60 b70     extension factor vs present fault dip (nan above theta0)
  part lockup    dip r060 r085       stress ratio needed for slip vs fault dip (nan beyond lock-up)
  part values    what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

NAN = float("nan")
THETA0 = (45.0, 60.0, 70.0)
MUS = (0.6, 0.85)
R_CAP = 40.0


def beta(theta0, theta):
    if theta > theta0 or theta <= 0:
        return NAN
    return math.sin(math.radians(theta0)) / math.sin(math.radians(theta))


def domino_width(theta0, theta, d=1.0, h=1.0):
    """Horizontal width of one rigid block, built explicitly: a parallelogram
    whose fault sides are d apart, rotated so that the faults dip theta; the
    width is measured between the faults along a horizontal line."""
    t = math.radians(theta)
    # unit vectors along the fault (down-dip) and across it
    along = np.array([math.cos(t), -math.sin(t)])
    across = np.array([math.sin(t), math.cos(t)])
    p0 = np.zeros(2)
    p1 = p0 + d * across
    # where does the horizontal line y = 0 meet the second fault (p1 + s along)?
    s = -p1[1] / along[1]
    return (p1 + s * along)[0] - p0[0]


def stress_ratio(dip, mu):
    t = math.radians(90.0 - dip)
    den = 1.0 - mu * math.tan(t)
    if den <= 0 or t <= 0:
        return NAN
    return (1.0 + mu / math.tan(t)) / den


def lockup_dip(mu):
    return math.degrees(math.atan(mu))


def optimal_dip(mu):
    return 90.0 - 0.5 * math.degrees(math.atan(1.0 / mu))


def min_ratio(mu):
    return (math.sqrt(1.0 + mu * mu) + mu) ** 2


if __name__ == "__main__":
    dips = np.arange(10.0, 70.01, 0.5)
    write_table(__file__, ("dip", "b45", "b60", "b70"),
                [(x,) + tuple(beta(t0, x) for t0 in THETA0) for x in dips], part="beta")
    rows = []
    for x in np.arange(20.0, 89.51, 0.25):
        r = [stress_ratio(x, mu) for mu in MUS]
        rows.append((x,) + tuple(v if v == v and v <= R_CAP else NAN for v in r))
    write_table(__file__, ("dip", "r060", "r085"), rows, part="lockup")
    vals = [("beta_60_to_30", beta(60.0, 30.0)), ("beta_45_to_20", beta(45.0, 20.0)),
            ("lockup_dip_060", lockup_dip(0.6)), ("lockup_dip_085", lockup_dip(0.85)),
            ("optimal_dip_060", optimal_dip(0.6)), ("optimal_dip_085", optimal_dip(0.85)),
            ("min_ratio_060", min_ratio(0.6)), ("min_ratio_085", min_ratio(0.85)),
            ("ratio_060_at_45", stress_ratio(45.0, 0.6)), ("ratio_060_at_35", stress_ratio(35.0, 0.6))]
    write_table(__file__, ("what", "value"), vals, part="values")

"""Repeated compass readings of the bedding of the Varden east limb (Year 1,
field-lab-methods-1). The true attitude is the model's (region.limb_attitude,
about 080.7/12.2); 25 readings are simulated with independent Gaussian errors
of 3 degrees on the dip direction and on the dip, then rounded to whole degrees
as a compass is read. Nothing here is a real-world measurement.

  part readings  i dipdir dip                 the 25 rounded readings
  part hist-dd   value count                  readings per whole degree of dip direction
  part hist-dip  value count                  readings per whole degree of dip
  part normals   i dipdir dip nE nN nU        unit upward normals of the first 12 (the problem)
  part values    what value                   means, sds, vector means, resultant lengths
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
import region as R  # noqa: E402

SEED = 83
N_READINGS = 25
SIGMA = 3.0
TRUE = R.limb_attitude(4300.0)          # (dip direction, dip) of the east limb


def readings(n=N_READINGS, sigma=SIGMA, seed=SEED):
    rng = np.random.default_rng(seed)
    a0, d0 = TRUE
    out = []
    for _ in range(n):
        a = a0 + rng.normal(0.0, sigma)
        d = d0 + rng.normal(0.0, sigma)
        out.append((int(round(a)) % 360, int(round(d))))
    return out


def normal(dipdir, dip):
    """Upward unit normal (east, north, up) of a plane of given dip direction and dip."""
    a, d = math.radians(dipdir), math.radians(dip)
    return (math.sin(d) * math.sin(a), math.sin(d) * math.cos(a), math.cos(d))


def vector_mean(rs):
    """(dip direction, dip, mean resultant length) of the vector mean of the normals."""
    ns = [normal(a, d) for a, d in rs]
    sx, sy, sz = (sum(c) for c in zip(*ns))
    r = math.sqrt(sx * sx + sy * sy + sz * sz)
    a = math.degrees(math.atan2(sx, sy)) % 360.0
    d = math.degrees(math.acos(sz / r))
    return a, d, r / len(rs)


def mean_sd(xs):
    m = sum(xs) / len(xs)
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))
    return m, sd


def angles_to(rs, a, d):
    """Angles (degrees) between each reading's normal and the normal of (a, d)."""
    m = normal(a, d)
    return [math.degrees(math.acos(min(1.0, sum(p * q for p, q in zip(normal(*r), m))))) for r in rs]


def counts(xs, lo, hi):
    """Number of readings at each whole-degree value from lo to hi."""
    return [(v, sum(1 for x in xs if x == v)) for v in range(lo, hi + 1)]


if __name__ == "__main__":
    rs = readings()
    write_table(__file__, ("i", "dipdir", "dip"), [(i + 1, a, d) for i, (a, d) in enumerate(rs)], part="readings")
    write_table(__file__, ("value", "count"), counts([a for a, _ in rs], 70, 90), part="hist-dd")
    write_table(__file__, ("value", "count"), counts([d for _, d in rs], 4, 20), part="hist-dip")
    rows = []
    for i, (a, d) in enumerate(rs[:12]):
        rows.append((i + 1, a, d) + tuple(round(c, 4) for c in normal(a, d)))
    write_table(__file__, ("i", "dipdir", "dip", "nE", "nN", "nU"), rows, part="normals")
    vals = []
    for tag, sub in (("all", rs), ("p12", rs[:12])):
        ma, sa = mean_sd([a for a, _ in sub])
        md, sd = mean_sd([d for _, d in sub])
        va, vd, rb = vector_mean(sub)
        th = angles_to(sub, va, vd)
        vals += [(tag + "_mean_dd", ma), (tag + "_sd_dd", sa), (tag + "_mean_dip", md), (tag + "_sd_dip", sd),
                 (tag + "_vec_dd", va), (tag + "_vec_dip", vd), (tag + "_Rbar", rb),
                 (tag + "_theta_rms", math.sqrt(sum(t * t for t in th) / len(th)))]
    vals += [("true_dd", TRUE[0]), ("true_dip", TRUE[1])]
    write_table(__file__, ("what", "value"), vals, part="values", digits=7)

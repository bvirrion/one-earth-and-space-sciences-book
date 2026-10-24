"""The Fry method on an invented population of grain centres (Year 3,
structural analysis).

Grain centres are placed by random sequential addition (fixed seed): a random
point of a BOX x BOX square is kept if it lies at least 1 from every centre
already kept, until N_TRY points have been tried; no two centres are then
closer than 1, the grains' diameter, and the directions are random: the
undeformed rock. The
population is then deformed by a pure strain of ratio R_TRUE = X/Z, long axis
at THETA_TRUE degrees anticlockwise from the x axis, area preserved. The Fry
plot is the set of all differences between pairs of centres; its empty
centre is an ellipse of the shape of the strain ellipse. The void boundary is
read as the shortest difference in each of 36 sectors and fitted by least
squares with 1/r^2 = a cos^2 t + b sin t cos t + c sin^2 t.

  part points     x y        deformed centres (the thin section)
  part fry        x y        Fry plot, differences shorter than FRY_CUT
  part void       x y        the sector minima (void boundary)
  part fit        x y        the fitted ellipse
  part values     what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

R_TRUE = 2.0
THETA_TRUE = 30.0
BOX = 14.0
N_TRY = 20000
SEED = 8
FRY_CUT = 2.6


def undeformed(box=BOX, n_try=N_TRY, seed=SEED):
    rng = np.random.default_rng(seed)
    cand = rng.uniform(0.0, box, (n_try, 2))
    kept = np.empty((0, 2))
    for c in cand:
        if len(kept) == 0 or np.min(np.hypot(*(kept - c).T)) >= 1.0:
            kept = np.vstack([kept, c])
    return kept - box / 2


def strain_matrix(r=R_TRUE, theta=THETA_TRUE):
    t = math.radians(theta)
    rot = np.array([[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]])
    d = np.diag([math.sqrt(r), 1.0 / math.sqrt(r)])
    return rot @ d @ rot.T


def deformed(r=R_TRUE, theta=THETA_TRUE):
    return undeformed() @ strain_matrix(r, theta).T


def fry_points(p, cut=FRY_CUT):
    d = (p[:, None, :] - p[None, :, :]).reshape(-1, 2)
    r = np.hypot(d[:, 0], d[:, 1])
    return d[(r > 0) & (r < cut)]


def void_boundary(fry, sectors=36):
    ang = np.mod(np.arctan2(fry[:, 1], fry[:, 0]), 2 * math.pi)
    r = np.hypot(fry[:, 0], fry[:, 1])
    out = []
    for k in range(sectors):
        sel = (ang >= 2 * math.pi * k / sectors) & (ang < 2 * math.pi * (k + 1) / sectors)
        i = np.argmin(np.where(sel, r, np.inf))
        out.append(fry[i])
    return np.array(out)


def fit_ellipse(b):
    """Centred ellipse through the boundary points: returns (ratio, long-axis
    angle in degrees from x, in [0, 180), sqrt(area/pi))."""
    x, y = b[:, 0], b[:, 1]
    m = np.column_stack([x * x, x * y, y * y])
    a, bb, c = np.linalg.lstsq(m, np.ones_like(x), rcond=None)[0]
    q = np.array([[a, bb / 2], [bb / 2, c]])
    w, e = np.linalg.eigh(q)                 # w[0] < w[1]: long axis has the smaller w
    long_axis = e[:, 0]
    theta = math.degrees(math.atan2(long_axis[1], long_axis[0])) % 180.0
    return math.sqrt(w[1] / w[0]), theta, (w[0] * w[1]) ** -0.25


def ellipse(ratio, theta, size, n=181):
    t = math.radians(theta)
    a, b = size * math.sqrt(ratio), size / math.sqrt(ratio)
    out = []
    for u in np.linspace(0, 2 * math.pi, n):
        x, y = a * math.cos(u), b * math.sin(u)
        out.append((x * math.cos(t) - y * math.sin(t), x * math.sin(t) + y * math.cos(t)))
    return out


if __name__ == "__main__":
    p = deformed()
    write_table(__file__, ("x", "y"), [tuple(v) for v in p], part="points")
    f = fry_points(p)
    write_table(__file__, ("x", "y"), [tuple(v) for v in f], part="fry")
    b = void_boundary(f)
    write_table(__file__, ("x", "y"), [tuple(v) for v in b], part="void")
    ratio, theta, size = fit_ellipse(b)
    write_table(__file__, ("x", "y"), ellipse(ratio, theta, size), part="fit")
    write_table(__file__, ("what", "value"),
                [("n_points", len(p)), ("n_fry", len(f)), ("fit_ratio", ratio),
                 ("fit_theta", theta), ("fit_size", size)], part="values")

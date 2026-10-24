"""A Schreinemakers bundle computed by Gibbs energy minimisation (Year 3,
thermodynamics of rocks). Invented phases, for the method only.

Binary system, four phases of fixed composition x: A (0), B (1/3), C (2/3),
D (1). Only the Gibbs energies of B and C measured from the straight line
between A and D matter:
    dB = -SB (T - T0) + VB (P - P0),  dC = -SC (T - T0) + VC (P - P0)
(J/mol, T in K, P in bar). The four reactions, each named after the absent
phase:
    (D)  A + C = 2 B        dG = 2 dB - dC
    (A)  B + D = 2 C        dG = 2 dC - dB
    (C)  2 A + D = 3 B      dG = 3 dB
    (B)  A + 2 D = 3 C      dG = 3 dC
all meet at the invariant point (T0, P0). At any (T, P) the stable
assemblages are the edges of the lower convex hull of the points (x, G); a
reaction is stable where its three phases lie on the hull.

  part ray_<X>_s   t p     stable half of the (X)-absent line
  part ray_<X>_m   t p     metastable extension
  part values      what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

T0, P0 = 873.15, 5000.0
SB, VB = 10.0, -0.20          # J/(mol K), J/bar
SC, VC = 10.0, 0.20
X = {"A": 0.0, "B": 1.0 / 3.0, "C": 2.0 / 3.0, "D": 1.0}
REACTIONS = {"D": {"A": -1, "C": -1, "B": 2}, "A": {"B": -1, "D": -1, "C": 2},
             "C": {"A": -2, "D": -1, "B": 3}, "B": {"A": -1, "D": -2, "C": 3}}
RAY_LENGTH = 200.0             # length of each ray, in K (pressure scaled by SCALE)
SCALE = 20.0                   # bar per K in the plotted frame


def g_values(t, p):
    db = -SB * (t - T0) + VB * (p - P0)
    dc = -SC * (t - T0) + VC * (p - P0)
    return {"A": 0.0, "B": db, "C": dc, "D": 0.0}


def hull_phases(t, p, tol=1e-6):
    """Phases on the lower convex hull of (x, G)."""
    g = g_values(t, p)
    on = []
    for k in "ABCD":
        others = [m for m in "ABCD" if m != k]
        above = False
        for i, m1 in enumerate(others):
            for m2 in others[i + 1:]:
                x1, x2 = X[m1], X[m2]
                if not (min(x1, x2) < X[k] < max(x1, x2)):
                    continue
                gl = g[m1] + (g[m2] - g[m1]) * (X[k] - x1) / (x2 - x1)
                if g[k] > gl + tol:
                    above = True
        if not above:
            on.append(k)
    return on


def reaction_dg(absent, t, p):
    g = g_values(t, p)
    return sum(n * g[k] for k, n in REACTIONS[absent].items())


def direction(absent):
    """Unit direction (dT, dP/SCALE) of the line dG = 0 through the point."""
    nu = REACTIONS[absent]
    s = sum(n * {"B": SB, "C": SC}.get(k, 0.0) for k, n in nu.items())
    v = sum(n * {"B": VB, "C": VC}.get(k, 0.0) for k, n in nu.items())
    # -s dT + v dP = 0 -> (dT, dP) proportional to (v, s)
    return v, s


def stable_sign(absent, step=1.0):
    """+1 if the half-line along +direction is stable, -1 otherwise."""
    v, s = direction(absent)
    norm = math.hypot(v, s / SCALE)
    for sign in (1, -1):
        t = T0 + sign * step * v / norm * 50.0
        p = P0 + sign * step * s / norm * 50.0
        phases = hull_phases(t, p, tol=1e-6)
        if all(k in phases for k in REACTIONS[absent]):
            return sign
    raise RuntimeError("no stable half-line for (" + absent + ")")


def ray(absent, sign, n=21):
    v, s = direction(absent)
    norm = math.hypot(v, s / SCALE)
    d = np.linspace(0.0, 1.0, n) * sign
    return [(T0 + u * v / norm * RAY_LENGTH - 273.15, (P0 + u * s / norm * RAY_LENGTH) / 1000.0) for u in d]


if __name__ == "__main__":
    vals = []
    for absent in "ABCD":
        sg = stable_sign(absent)
        write_table(__file__, ("t", "p"), ray(absent, sg), part=f"ray_{absent}_s")
        write_table(__file__, ("t", "p"), ray(absent, -sg), part=f"ray_{absent}_m")
        v, s = direction(absent)
        vals.append((f"slope_{absent}", s / v))
    write_table(__file__, ("what", "value"), vals, part="values")

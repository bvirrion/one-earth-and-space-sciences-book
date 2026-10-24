"""A two-dimensional forward model of a shelf through a sea-level cycle
(Year 3, sequence stratigraphy). Invented basin (the Varden basin of the
weekend problem); nothing here is a measured quantity.

Geometry (x in km basinward, elevations in m): an initial ramp
h0(x) = H0 - G x; subsidence increasing basinward, sigma(x) = S0 + S1 x / L
(m/kyr); eustatic sea level E(t) = -A cos(2 pi t / P), starting at a
lowstand, after a spin-up of SPIN kyr at E = -A that builds a first wedge
(not recorded). Each step:
  1. the basin subsides by sigma(x) dt;
  2. the sediment supplied in the step, Q dt (m2 per metre of coast), fills
     the depositional profile: a flat topset at sea level landward of the
     shoreline x_s (only where the old surface is below sea level: exposed
     land receives nothing and is not eroded) and a foreset of slope
     tan(theta) seaward of it; x_s is found by bisection so that the volume
     added is exactly Q dt.
The shoreline trajectory follows: with the relative sea-level rise rate at
the shoreline A_s = dE/dt + sigma(x_s), the topset width W and the foreset
height D (water depth at the toe of the foreset),
    dx_s/dt = (Q - A_s W) / D           (A_s >= 0, topset aggrading),
    dx_s/dt = Q / D - A_s / tan(theta)   (A_s < 0, forced regression),
for a topset that aggrades uniformly; the model's topset does not (its
subsidence varies with x), so the test checks only the falling-stage form,
which needs no topset.

Systems tracts from the shoreline trajectory: falling stage (A_s < 0),
lowstand (A_s >= 0, regression, before the maximum landward position),
transgressive (transgression), highstand (A_s >= 0, regression, after it).

  part surfaces   x z_<t>...      stratal surfaces every 20 kyr, buried by later subsidence
  part shore      t xs es zfinal tract   shoreline position, elevation then, elevation now
  part series     t sea rate xs   eustasy, relative rise rate at the shoreline, shoreline
  part tracts     t0 t1 tract     intervals
  part poly<k>    x z             the deposit of the k-th interval, a closed
                                  polygon in its final (buried) position
  part values     what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

L_KM = 120.0
NX = 1201
H0, G = 10.0, 1.5            # m, m per km
S0, S1 = 0.02, 0.10          # m/kyr at x = 0, increment at x = L
A_SEA, P_SEA = 30.0, 400.0   # m, kyr
Q = 6000.0                   # m2/kyr per metre of coast
TAN = 0.012                  # foreset slope
DT = 0.5                     # kyr
T_END = 600.0
SPIN = 100.0                 # kyr of still-stand before t = 0
SURF_EVERY = 20.0

X = np.linspace(0.0, L_KM, NX)
DX_M = (X[1] - X[0]) * 1000.0


def sea(t):
    if t < 0:
        return -A_SEA
    return -A_SEA * math.cos(2 * math.pi * t / P_SEA)


def dsea(t):
    if t < 0:
        return 0.0
    return A_SEA * 2 * math.pi / P_SEA * math.sin(2 * math.pi * t / P_SEA)


def sigma(x):
    return S0 + S1 * np.asarray(x) / L_KM


def profile(xs, e):
    """Depositional profile for a shoreline at xs (km) and sea level e."""
    return np.where(X <= xs, e, e - TAN * (X - xs) * 1000.0)


def fill(h, e, vol):
    """Add vol (m2) of sediment; return the new surface and the shoreline."""
    def added(xs):
        p = profile(xs, e)
        return float(np.sum(np.clip(p - h, 0.0, None)) * DX_M)

    lo, hi = 0.0, L_KM
    if not added(lo) <= vol <= added(hi):
        raise ValueError("supply does not fit the grid")
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if added(mid) < vol:
            lo = mid
        else:
            hi = mid
    xs = 0.5 * (lo + hi)
    p = profile(xs, e)
    return np.maximum(h, p), xs


def run():
    """Spin-up, then the recorded run; returns the final surface, the
    shoreline record (t, x_s, E) and the surfaces every SURF_EVERY kyr."""
    h = H0 - G * X
    sig = sigma(X)
    t = -SPIN
    shore = []
    surfaces = {}
    steps = [(0.0, h.copy())]
    while t < T_END - 1e-9:
        t1 = t + DT
        h = h - sig * DT
        e = sea(t1)
        h, xs = fill(h, e, Q * DT)
        if t1 > 1e-9:
            shore.append((t1, xs, e))
            steps.append((t1, h.copy()))
        elif abs(t1) < 1e-9:
            steps[0] = (0.0, h.copy())
        if t1 > -1e-9 and abs(t1 / SURF_EVERY - round(t1 / SURF_EVERY)) < 1e-9:
            surfaces[round(t1, 6)] = h.copy()
        t = t1
    return h, shore, surfaces, steps


def classify(shore, window=10, min_run=8):
    """Tract label per step: F, L, T, H. The shoreline move is a centred
    difference over +-window steps; runs shorter than min_run steps take the
    label of the run before them (the shoreline dithers at a turnaround)."""
    n = len(shore)
    rates = [dsea(t) + float(sigma(xs)) for t, xs, _ in shore]
    labels = []
    for i in range(n):
        a, b = max(0, i - window), min(n - 1, i + window)
        dx = shore[b][1] - shore[a][1]
        if rates[i] < 0:
            labels.append("F")
        elif dx < 0:
            labels.append("T")
        else:
            labels.append(None)
    # regression under rising relative sea level: lowstand after a falling
    # stage (the run starts at a lowstand), highstand after a transgression
    last = "F"
    for i in range(n):
        if labels[i] is None:
            labels[i] = "L" if last in ("F", "L") else "H"
        last = labels[i]
    runs = []
    for i, lab in enumerate(labels):
        if runs and runs[-1][0] == lab:
            runs[-1][2] = i
        else:
            runs.append([lab, i, i])
    for k in range(1, len(runs)):
        if runs[k][2] - runs[k][1] + 1 < min_run:
            runs[k][0] = runs[k - 1][0]
    out = [None] * n
    for lab, i0, i1 in runs:
        for i in range(i0, i1 + 1):
            out[i] = lab
    return out, rates


def basinward_shift(shore, tracts):
    """Largest basinward move of the shoreline from the start of a falling
    stage to the end of the lowstand regression that follows (km)."""
    best = 0.0
    i, n = 0, len(shore)
    while i < n:
        if tracts[i] == "F" and (i == 0 or tracts[i - 1] != "F"):
            x0 = shore[i - 1][1] if i > 0 else shore[i][1]
            j = i
            xmax = x0
            while j < n and tracts[j] in ("F", "L"):
                xmax = max(xmax, shore[j][1])
                j += 1
            best = max(best, xmax - x0)
            i = j
        else:
            i += 1
    return best


def main():
    h, shore, surfaces, steps = run()
    tracts, rates = classify(shore)
    times = sorted(surfaces)
    # bury each surface by the subsidence after its time
    sig = sigma(X)
    cols = []
    for tt in times:
        cols.append(surfaces[tt] - sig * (T_END - tt))
    step = 10
    rows = [[float(X[k])] + [float(c[k]) for c in cols] for k in range(0, NX, step)]
    write_table(__file__, ["x"] + ["z%d" % int(round(tt)) for tt in times], rows,
                part="surfaces")
    code = {"F": 1, "L": 2, "T": 3, "H": 4}
    rows = []
    for (t, xs, e), tr in zip(shore, tracts):
        if abs(t - round(t)) < 1e-9 and int(round(t)) % 2 == 0:
            rows.append([t, xs, e, e - float(sigma(xs)) * (T_END - t), code[tr]])
    write_table(__file__, ("t", "xs", "es", "zfinal", "tract"), rows, part="shore")
    rows = [[t, e, r, xs] for (t, xs, e), r in zip(shore, rates)
            if abs(t - round(t)) < 1e-9 and int(round(t)) % 2 == 0]
    write_table(__file__, ("t", "sea", "rate", "xs"), rows, part="series")
    iv = []
    start = 0
    for i in range(1, len(tracts) + 1):
        if i == len(tracts) or tracts[i] != tracts[start]:
            iv.append([shore[start][0] - DT, shore[i - 1][0], code[tracts[start]]])
            start = i
    write_table(__file__, ("t0", "t1", "tract"), iv, part="tracts")
    by_t = {round(tt, 6): hh for tt, hh in steps}
    for k, (t0, t1, _) in enumerate(iv, start=1):
        top = by_t[round(t1, 6)] - sig * (T_END - t1)
        bot = by_t[round(t0, 6)] - sig * (T_END - t0)
        idx = list(range(0, NX, 5))
        rows = [[float(X[i]), float(top[i])] for i in idx]
        rows += [[float(X[i]), float(bot[i])] for i in reversed(idx)]
        write_table(__file__, ("x", "z"), rows, part="poly%d" % k)
    shift = basinward_shift(shore, tracts)
    xs_all = [s[1] for s in shore]
    vals = [["basinward_shift_km", shift], ["xs_min", min(xs_all)], ["xs_max", max(xs_all)],
            ["n_intervals", len(iv)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

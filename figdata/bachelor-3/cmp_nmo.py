"""A synthetic CMP gather beneath CMP S of the Varden line, its normal-moveout
correction, the RMS and Dix interval velocities (Year 3, exploration-seismology).

Model: seismic_model.column(S_SYNCLINE), flat layers (near the syncline axis
the limbs dip 12 degrees, neglected here). Exact reflection times by two-point
ray tracing in flat layers: for a ray parameter p,
    x(p) = 2 sum h_i p v_i / sqrt(1 - p^2 v_i^2),
    t(p) = 2 sum h_i / (v_i sqrt(1 - p^2 v_i^2)),
solved for p at each offset by bisection. The stacking (NMO) velocity of each
reflector is the least-squares slope of t^2 against x^2 over the near offsets
0-600 m (OFFSETS_FIT; the gather itself spans 0-2000 m);
V_rms from its definition; interval velocities from the Dix equation applied to
the stacking velocities. Traces: Ricker wavelet (synthetic_seismogram.ricker),
amplitude = normal-incidence reflection coefficient (no spreading, no
transmission loss), 2 ms sampling.

  part gather-raw, gather-nmo   x t        wiggle traces, x = offset + gain*amp,
                                           traces separated by nan rows
  part curves     k x t                    exact reflection times (k = reflector)
  part vel        t0 vrms vstack vint vdix  per reflector
  part values     what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402
import seismic_model as M  # noqa: E402
from synthetic_seismogram import ricker, F_PEAK  # noqa: E402

OFFSETS = np.arange(0.0, 2001.0, 100.0)
OFFSETS_FIT = np.arange(0.0, 601.0, 100.0)   # the near offsets used for velocity analysis
DT = 0.002
T_MAX = 1.0
GAIN = 220.0   # metres of plot per unit amplitude


def layers(col):
    return np.array([h for n, h, v, r in col[:-1]]), np.array([v for n, h, v, r in col[:-1]])


def x_t(p, h, v):
    c = np.sqrt(1.0 - (p * v) ** 2)
    return 2.0 * np.sum(h * p * v / c), 2.0 * np.sum(h / (v * c))


def reflection_time(x, h, v):
    """Two-way time (s) of the reflection off the base of the stack h, v at offset x."""
    if x == 0.0:
        return 2.0 * np.sum(h / v)
    lo, hi = 0.0, (1.0 - 1e-12) / v.max()
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if x_t(mid, h, v)[0] < x:
            lo = mid
        else:
            hi = mid
    return x_t(0.5 * (lo + hi), h, v)[1]


def stacking_velocity(xs, ts):
    """Least-squares fit of t^2 = t0^2 + x^2 / V^2: returns (t0, V)."""
    a = np.vstack([np.ones_like(xs), xs ** 2]).T
    c, *_ = np.linalg.lstsq(a, ts ** 2, rcond=None)
    return math.sqrt(c[0]), 1.0 / math.sqrt(c[1])


def vrms(h, v):
    t = 2.0 * h / v
    return np.sqrt(np.cumsum(v ** 2 * t) / np.cumsum(t))


def dix(t0, vst):
    out = []
    for k in range(len(t0)):
        if k == 0:
            out.append(vst[0])
        else:
            out.append(math.sqrt((vst[k] ** 2 * t0[k] - vst[k - 1] ** 2 * t0[k - 1]) / (t0[k] - t0[k - 1])))
    return out


def gather(col, nmo_v=None):
    h, v = layers(col)
    rc = M.reflection_coefficients(col)
    tt = np.arange(0.0, T_MAX + DT / 2, DT)
    traces = []
    for x in OFFSETS:
        tr = np.zeros_like(tt)
        for k in range(len(h)):
            t = reflection_time(x, h[:k + 1], v[:k + 1])
            tr += rc[k] * ricker(tt - t)
        if nmo_v is not None:
            t0v, vv = nmo_v
            vel = np.interp(tt, t0v, vv)
            tin = np.sqrt(tt ** 2 + (x / vel) ** 2)
            tr = np.interp(tin, tt, tr, right=0.0)
        traces.append(tr)
    return tt, traces


def wiggle_rows(tt, traces):
    rows = []
    for x, tr in zip(OFFSETS, traces):
        rows += [(x + GAIN * a, t) for a, t in zip(tr, tt)]
        rows.append(("nan", "nan"))
    return rows[:-1]


if __name__ == "__main__":
    col, ground = M.column()
    h, v = layers(col)
    t0 = [2.0 * np.sum(h[:k + 1] / v[:k + 1]) for k in range(len(h))]
    curves, vst = [], []
    for k in range(len(h)):
        ts = np.array([reflection_time(x, h[:k + 1], v[:k + 1]) for x in OFFSETS])
        curves += [(k + 1, x, t) for x, t in zip(OFFSETS, ts)]
        tf = np.array([reflection_time(x, h[:k + 1], v[:k + 1]) for x in OFFSETS_FIT])
        vst.append(stacking_velocity(OFFSETS_FIT, tf)[1])
    vr = vrms(h, v)
    vd = dix(t0, vst)
    write_table(__file__, ("k", "x", "t"), curves, part="curves")
    write_table(__file__, ("t0", "vrms", "vstack", "vint", "vdix"),
                list(zip(t0, vr, vst, v, vd)), part="vel")
    tt, raw = gather(col)
    write_table(__file__, ("x", "t"), wiggle_rows(tt, raw), part="gather-raw", digits=5)
    tt, cor = gather(col, nmo_v=([0.0] + t0, [vst[0]] + vst))
    write_table(__file__, ("x", "t"), wiggle_rows(tt, cor), part="gather-nmo", digits=5)
    vals = [("ground_m", round(ground, 1)), ("depth_basement_m", round(float(np.sum(h)), 1)),
            ("f_peak_hz", F_PEAK)]
    for k in range(len(h)):
        t600 = reflection_time(600.0, h[:k + 1], v[:k + 1])
        vals += [("t0_%d" % (k + 1), round(t0[k], 4)), ("t600_%d" % (k + 1), round(t600, 4)),
                 ("vst_%d" % (k + 1), round(vst[k], 1)), ("vrms_%d" % (k + 1), round(vr[k], 1)),
                 ("vdix_%d" % (k + 1), round(vd[k], 1))]
    write_table(__file__, ("what", "value"), vals, part="values")

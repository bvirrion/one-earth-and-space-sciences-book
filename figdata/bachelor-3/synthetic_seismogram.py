"""Synthetic seismogram and wedge (tuning) model (Year 3, exploration-seismology).

Convolutional model s(t) = (w * r)(t): the reflectivity series r of the Varden
column beneath CMP S (seismic_model.py; normal-incidence coefficients at the
two-way times of the interfaces) convolved with a zero-phase Ricker wavelet of
peak frequency F_PEAK,
    w(t) = (1 - 2 pi^2 f^2 t^2) exp(-pi^2 f^2 t^2).
Wedge model: a layer of thickness b and speed V_WEDGE between two half-spaces
whose reflection coefficients are +R and -R (the classic thin bed); the peak
amplitude of the composite trace against b shows tuning, the maximum near
b = lambda / 4.

  part log        t z imp            impedance against two-way time (step log)
  part refl       t r                reflectivity spikes (stem plot data)
  part trace      t s                synthetic trace
  part wavelet    t w                the wavelet
  part wedge      b amp tsep         thickness (m), peak amplitude, apparent
                                     peak-to-trough separation (ms)
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

F_PEAK = 30.0       # Hz
DT = 0.0005         # s
V_WEDGE = 3000.0    # m/s, the wedge layer
R_WEDGE = 0.2


def ricker(t, f=F_PEAK):
    a = (math.pi * f * t) ** 2
    return (1.0 - 2.0 * a) * np.exp(-a)


def trace_from_spikes(times, coefs, tt):
    s = np.zeros_like(tt)
    for t, r in zip(times, coefs):
        s += r * ricker(tt - t)
    return s


def wedge_amplitude(b, v=V_WEDGE, r=R_WEDGE):
    """Peak absolute amplitude of top (+r) and base (-r) reflections of a bed b thick."""
    dt = 2.0 * b / v
    tt = np.arange(-0.1, 0.1 + dt, DT / 4)
    s = r * ricker(tt) - r * ricker(tt - dt)
    return float(np.max(np.abs(s))), tt, s


def peak_trough_ms(tt, s):
    return 1000.0 * abs(tt[np.argmax(s)] - tt[np.argmin(s)])


def tuning_thickness(v=V_WEDGE):
    bs = np.arange(0.5, 80.0, 0.25)
    amps = [wedge_amplitude(b, v)[0] for b in bs]
    return float(bs[int(np.argmax(amps))])


if __name__ == "__main__":
    col, ground = M.column()
    t0 = M.t0s(col)
    rc = M.reflection_coefficients(col)
    imp = M.impedances(col)
    tt = np.arange(0.0, 0.9 + DT / 2, DT)
    # step impedance log against time, with the depth of each step
    depth, log = 0.0, []
    tb = [0.0] + t0
    zb = [0.0]
    for name, h, v, rho in col[:-1]:
        depth += h
        zb.append(depth)
    for k in range(len(imp) - 1):
        log += [(tb[k], zb[k], imp[k] / 1000.0), (tb[k + 1], zb[k + 1], imp[k] / 1000.0)]
    log += [(t0[-1], zb[-1], imp[-1] / 1000.0), (0.9, zb[-1] + (0.9 - t0[-1]) * 2500.0, imp[-1] / 1000.0)]
    write_table(__file__, ("t", "z", "imp"), log, part="log")
    write_table(__file__, ("t", "r"), list(zip(t0, rc)), part="refl")
    s = trace_from_spikes(t0, rc, tt)
    write_table(__file__, ("t", "s"), list(zip(tt, s)), part="trace")
    tw = np.arange(-0.06, 0.06 + DT / 2, DT)
    write_table(__file__, ("t", "w"), list(zip(tw, ricker(tw))), part="wavelet")
    rows = []
    for b in np.arange(0.0, 80.01, 1.0):
        amp, ts, ss = wedge_amplitude(b)
        rows.append((b, amp / (2 * R_WEDGE), peak_trough_ms(ts, ss) if b > 0 else 0.0))
    write_table(__file__, ("b", "amp", "tsep"), rows, part="wedge")
    lam = V_WEDGE / F_PEAK
    vals = [("lambda_m", round(lam, 1)), ("lambda_over_4_m", round(lam / 4, 1)),
            ("tuning_m", tuning_thickness()),
            ("amp_max_rel", round(max(r[1] for r in rows), 3))]
    for k, (t, r) in enumerate(zip(t0, rc)):
        vals += [("t0_%d" % (k + 1), round(t, 4)), ("r_%d" % (k + 1), round(r, 4))]
    write_table(__file__, ("what", "value"), vals, part="values")

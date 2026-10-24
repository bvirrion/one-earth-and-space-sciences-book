"""Tests for the exploration-seismology figdata (Year 3)."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import cmp_nmo as C  # noqa: E402
import refraction_dip as RD  # noqa: E402
import seismic_model as M  # noqa: E402
import synthetic_seismogram as S  # noqa: E402

# ledger mavko:velocities ranges (m/s, g/cm3); schist taken in the gneiss range
RANGES = {"chalk": ((2300, 2600), (1.8, 3.1)), "shale": ((1100, 2500), (2.0, 2.4)),
          "limestone": ((3500, 6000), (2.4, 2.7)), "sandstone": ((2000, 3500), (2.1, 2.4)),
          "schist": ((4400, 5200), (2.5, 2.7))}


def test_model_properties_inside_ledger_ranges():
    for name, (v, rho) in M.PROPS.items():
        (v1, v2), (r1, r2) = RANGES[name]
        assert v1 <= v <= v2 and r1 <= rho <= r2


def test_column_matches_region_thicknesses():
    col, ground = M.column()
    th = [h for n, h, v, r in col[:-1]]
    assert all(h > 0 for h in th)
    assert th[1] == 100.0 and th[2] == 180.0 and th[3] == 120.0   # region.THICK
    assert 900.0 < sum(th) < 1100.0


def test_ricker_peak_and_zero_mean():
    t = np.arange(-0.2, 0.2, 1e-4)
    w = S.ricker(t)
    assert abs(w.max() - 1.0) < 1e-9 and abs(t[np.argmax(w)]) < 1e-9
    assert abs(np.sum(w) * 1e-4) < 1e-6
    spec = np.abs(np.fft.rfft(w, 2 ** 16))
    f = np.fft.rfftfreq(2 ** 16, 1e-4)
    assert abs(f[np.argmax(spec)] - S.F_PEAK) < 0.5


def test_tuning_below_quarter_wavelength_for_ricker():
    lam = S.V_WEDGE / S.F_PEAK
    b = S.tuning_thickness()
    # Ricker tuning: two-way time about 1 / (2.6 f), i.e. b = v / (5.2 f)
    assert abs(b - S.V_WEDGE / (5.2 * S.F_PEAK)) < 1.0
    assert 0.15 * lam < b < 0.26 * lam


def test_single_layer_reflection_is_an_exact_hyperbola():
    h, v = np.array([800.0]), np.array([2000.0])
    for x in (0.0, 300.0, 1500.0):
        t = C.reflection_time(x, h, v)
        assert abs(t - math.sqrt(0.8 ** 2 + (x / 2000.0) ** 2)) < 1e-9
    xs = np.arange(0.0, 2001.0, 100.0)
    ts = np.array([C.reflection_time(x, h, v) for x in xs])
    assert abs(C.stacking_velocity(xs, ts)[1] - 2000.0) < 1e-6


def test_dix_on_rms_velocities_recovers_interval_velocities():
    h, v = np.array([500.0, 300.0, 200.0]), np.array([2000.0, 3500.0, 2500.0])
    t0 = np.cumsum(2 * h / v)
    vr = C.vrms(h, v)
    assert np.allclose(C.dix(t0, vr), v)


def test_reciprocal_times_and_apparent_velocities():
    length, theta, hw, he = RD.geometry()
    ic = math.asin(RD.V1 / RD.V2)
    tw = RD.head_time(length, hw, ic, -1.0, theta)
    te = RD.head_time(length, he, ic, +1.0, theta)
    assert abs(tw - te) < 1e-9          # reciprocity
    v_up = RD.V1 / math.sin(ic - theta)
    v_down = RD.V1 / math.sin(ic + theta)
    assert v_down < RD.V2 < v_up
    # the harmonic-mean rule recovers V2 to within the dip correction
    assert abs(2.0 / (1 / v_up + 1 / v_down) * math.cos(theta) - RD.V2) / RD.V2 < 0.01


def test_flat_refractor_critical_distance():
    ic = math.asin(0.5)
    assert abs(RD.critical_distance(100.0, ic, 1.0, 0.0) - 200.0 * math.tan(ic)) < 1e-9

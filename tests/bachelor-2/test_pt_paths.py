"""Tests for thermobarometry and the thickening model (figdata/bachelor-2/ptpaths.py)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import ptpaths as pt  # noqa: E402

K = 273.15


def test_fit_reproduces_the_published_ideal_calibration():
    dh, ds = pt.fs_fit()
    assert dh == pytest.approx(52635, abs=10)          # Holdaway et al. 1997, Table 2
    assert ds == pytest.approx(20.20, abs=0.02)
    assert pt.GB_DH == pytest.approx(dh, abs=5) and pt.GB_DS == pytest.approx(ds, abs=0.005)


def test_thermometer_inverts_and_reproduces_the_experiments():
    for tc, lnkd in pt.FS78:
        t = pt.gb_t(lnkd, pt.FS_P)
        assert pt.gb_lnkd(t, pt.FS_P) == pytest.approx(lnkd, abs=1e-12)
        assert t - K == pytest.approx(tc, abs=40)
    # weak pressure dependence: 1 kbar moves T by about 4-5 K at 600 C
    l = pt.gb_lnkd(873.15, 5000)
    assert 3 < pt.gb_t(l, 6000) - pt.gb_t(l, 5000) < 6


def test_gasp_end_member_and_activity_term():
    assert pt.gasp_p(650, 1.0, 1.0) == pytest.approx(22.80 * 650 - 1093)
    # dilution of grossular lowers the pressure; anorthite-poor plagioclase raises it
    assert pt.gasp_p(600, 0.05, 0.3) < pt.gasp_p(600, 0.10, 0.3) < pt.gasp_p(600, 0.10, 0.2)


def test_intersection_is_self_consistent():
    l = math.log((0.120 / 0.720) / (0.46 / 0.53))
    tc, p = pt.intersect(l, 0.060, 0.28)
    assert pt.gb_t(l, p) - K == pytest.approx(tc, abs=1e-6)
    assert tc == pytest.approx(623.1, abs=0.2) and p == pytest.approx(7568, abs=10)


def test_initial_geotherm_is_steady_and_continuous():
    z = np.linspace(0, 200e3, 4001)
    t = pt.steady(z)
    q_top = pt.KCOND * (t[1] - t[0]) / (z[1] - z[0])
    assert q_top == pytest.approx(pt.Q_BASE + pt.A_CRUST * pt.H_CRUST, rel=1e-3)
    assert np.all(np.diff(t) > 0)


def test_thickening_conserves_the_sawtooth_and_relaxes():
    z, t, a = pt.thicken()
    i = int(round(pt.H_CRUST / (z[1] - z[0])))
    assert t[i] == 0.0 and t[i - 1] > 500                  # cold former surface under a hot base
    geo, path = pt.run()
    d60, t60 = geo[60]
    assert np.interp(35e3, d60, t60) > np.interp(35e3, *geo[10])
    s = pt.path_summary(path)
    # clockwise path: peak pressure first, peak temperature during decompression
    assert s["t_at_peakP"] == 0 and s["p_at_peakT"] < s["peakP"]
    frac = (s["t_peakT"] - 30.0) / 70.0
    assert 0.1 < frac < 0.4


def test_numerical_conduction_matches_steady_state_without_thickening():
    # without thickening and erosion, the steady geotherm must not drift
    z = np.arange(0.0, pt.ZMAX + 125, 250.0)
    t0 = pt.steady(z)
    from scipy.linalg import solve_banded
    n, dz, dt = len(z), 250.0, 0.05
    r = pt.KAPPA * dt * pt.MYR / dz ** 2
    a = np.where(z < pt.H_CRUST, pt.A_CRUST, 0.0)
    src = a / (pt.KCOND / pt.KAPPA) * dt * pt.MYR
    t = t0.copy()
    for _ in range(200):
        ab = np.zeros((3, n))
        ab[0, 1:], ab[1, :], ab[2, :-1] = -r, 1 + 2 * r, -r
        rhs = t + src
        ab[1, 0], ab[0, 1], rhs[0] = 1.0, 0.0, 0.0
        ab[2, -2] = -2 * r
        rhs[-1] += 2 * r * dz * pt.Q_BASE / pt.KCOND
        t = solve_banded((1, 1), ab, rhs)
    assert np.max(np.abs(t - t0)[z <= 100e3]) < 1.0

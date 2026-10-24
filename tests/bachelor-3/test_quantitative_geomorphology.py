"""Tests for the hillslope and river-profile scripts (Year 3, ch. 18)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import hillslope as hs  # noqa: E402
import stream_profile as sp  # noqa: E402
import varden_river as vr  # noqa: E402


def test_scarp_numerical_solution_matches_error_function():
    x, z = hs.scarp_fd(10000.0)
    assert np.max(np.abs(z - hs.scarp(x, 10000.0))) < 0.01


def test_scarp_midpoint_slope_formula():
    t, h = 10000.0, 1e-3
    num = (hs.scarp(h, t) - hs.scarp(-h, t)) / (2 * h)
    assert float(num) == pytest.approx(hs.max_slope(t), rel=1e-6)
    assert hs.kappa_t_from_slope(hs.max_slope(t)) == pytest.approx(hs.KAPPA * t)


def test_hill_reaches_the_parabolic_steady_state():
    e = hs.RATES[1]
    x, z = hs.hill_fd(e)
    assert z.max() == pytest.approx(hs.hill_relief(e), rel=0.005)
    i = len(x) // 2
    curv = (z[i + 1] - 2 * z[i] + z[i - 1]) / (x[1] - x[0]) ** 2
    assert curv == pytest.approx(-e / hs.KAPPA, rel=0.01)


def test_steady_profile_balances_uplift():
    d = np.linspace(1000.0, sp.L - 100.0, 7)
    h = 0.5
    s = (sp.z_ss(d - h) - sp.z_ss(d + h)) / (2 * h)
    assert np.allclose(sp.K * sp.area(d) ** sp.THETA * s, sp.U, rtol=1e-5)
    assert float(sp.z_ss(sp.L)) == pytest.approx(sp.Z_OUT)
    assert sp.Z_OUT == pytest.approx(sp.region.river_z(0.0))


def test_chi_makes_the_profile_a_straight_line():
    d = np.linspace(sp.D_HEAD, sp.L, 50)
    slope = (sp.z_ss(d) - sp.Z_OUT) / np.where(sp.chi(d) > 0, sp.chi(d), np.nan)
    assert np.allclose(slope[:-1], sp.ks() * sp.A0 ** -sp.THETA)


def test_knick_position_inverts_travel_time():
    for t in sp.TIMES[1:]:
        assert sp.travel_time(sp.knick_position(t)) == pytest.approx(t)


@pytest.mark.parametrize("t", [300000.0, 600000.0])
def test_upwind_solution_moves_the_step_at_the_kinematic_speed(t):
    d, z = sp.upwind(t)
    mid = sp.z_ss(d) + sp.DROP / 2
    i = np.where((z[:-1] - mid[:-1]) * (z[1:] - mid[1:]) < 0)[0]
    assert len(i) == 1
    assert d[i[0]] == pytest.approx(sp.knick_position(t), abs=50.0)
    far = d < sp.knick_position(t) - 500
    # first-order upwind: a truncation error of a few decimetres, no more
    assert np.allclose(z[far], sp.z_ss(d[far]) + sp.DROP, atol=0.5)


def test_slope_area_fit_recovers_the_concavity():
    k_fit, th_fit = sp.fit_power(*sp.slope_area_samples())
    assert abs(th_fit - sp.THETA) < 0.08
    a, s = sp.slope_area_samples()
    ksn = math.exp(np.mean(np.log(s * a ** sp.THETA)))
    assert ksn == pytest.approx(sp.ks(), rel=0.1)


def test_all_knickpoints_share_one_chi():
    t = sp.T_FALL
    ck = vr.chi_knick(t)
    assert sp.chi(sp.knick_position(t)) == pytest.approx(ck)
    reached = 0
    for j in range(len(vr.TRIBS)):
        sk = vr.trib_knick(j, t)
        if sk is None:
            assert sp.chi(vr.TRIBS[j][0]) >= ck
        else:
            reached += 1
            assert float(vr.trib_chi(j, sk)) == pytest.approx(ck)
    assert reached == 1


def test_tributaries_are_smaller_than_the_trunk_at_their_junctions():
    for dj, lt in vr.TRIBS:
        assert float(vr.trib_area(lt)) < float(sp.area(dj))
        assert dj < sp.L

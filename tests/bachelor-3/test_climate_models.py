"""Tests for the energy-balance and two-layer scripts (Year 3, ch. 22)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import budyko_sellers as bs  # noqa: E402
import two_layer as tl  # noqa: E402


def test_olr_fit_is_physical():
    assert 190 < bs.A < 230 and 1.5 < bs.B < 2.2
    # Budyko's 1969 coefficients converted: about 199 W/m2 and 1.43 W m-2 K-1
    assert (14.0 - 1.5) * bs.KCAL_MONTH == pytest.approx(199, abs=1)
    assert bs.BETA == pytest.approx(3.74, abs=0.01)


def test_zero_dimensional_equilibria():
    roots = bs.equilibria_0d(bs.Q0)
    assert [st for _, st in roots] == [True, False, True]
    for t, _ in roots:
        assert bs.net_0d(t) == pytest.approx(0.0, abs=1e-9)
    # stability: net decreases through a stable root, increases through the unstable one
    for t, st in roots:
        d = (bs.net_0d(t + 1e-4) - bs.net_0d(t - 1e-4)) / 2e-4
        assert (d < 0) == st
    # saddle-node: just below the threshold the warm root is gone
    qw = bs.q_threshold_warm()
    assert max(t for t, _ in bs.equilibria_0d(qw * 1.001)) >= bs.T_FREE
    assert max(t for t, _ in bs.equilibria_0d(qw * 0.999)) < bs.T_ICE


def test_budyko_model_balances():
    xs = math.sin(math.radians(60.0))
    q = bs.q_for_iceline(xs, bs.TC)
    tb = bs.t_mean(q, xs)
    prof = bs.t_profile(q, xs)
    # the transport integrates to zero: the area mean of T is Tbar (the profile's
    # albedo step falls between grid points, hence the tolerance)
    assert np.trapezoid(prof, bs.X) == pytest.approx(tb, abs=1e-2)
    assert bs.mean_albedo(1.0) == pytest.approx(bs.ALB_FREE)
    assert bs.mean_albedo(0.0) == pytest.approx(bs.ALB_ICE)
    # the ice-line condition, with the edge albedo
    te = (q * bs.s_of(xs) * (1 - bs.ALB_EDGE) - bs.A + bs.BETA * tb) / (bs.B + bs.BETA)
    assert te == pytest.approx(bs.TC, abs=1e-9)
    # today's ice line sits at 72 degrees by construction, and s(x) has mean 1
    assert bs.q_for_iceline(math.sin(math.radians(72.0)), bs.TC) == pytest.approx(bs.Q0)
    assert np.trapezoid(bs.SX, bs.X) == pytest.approx(1.0, abs=1e-12)
    lat, qmin = bs.glaciation_threshold()
    assert 35 < lat < 60 and 0.95 < qmin < 1.0


def test_two_layer_time_scales_and_equilibrium():
    tf, ts = tl.timescales()
    lam, gam, c, cd = tl.LAM, tl.GAM, tl.C, tl.CD
    assert tf == pytest.approx(c / (lam + gam), rel=0.02)
    assert ts == pytest.approx(cd * (lam + gam) / (lam * gam), rel=0.02)
    af, as_ = tl.amplitudes()
    assert af + as_ == pytest.approx(1.0)
    assert af == pytest.approx(lam / (lam + gam), rel=0.02)
    run = tl.integrate(lambda t: 2 * tl.F2X, 3000.0, dt=1.0)
    assert run[-1][1] == pytest.approx(2 * tl.F2X / lam, rel=1e-4)
    # the two-exponential solution matches the integration
    t = 25.0
    num = [r for r in tl.integrate(lambda t: 2 * tl.F2X, 30.0) if abs(r[0] - t) < 1e-6][0][1]
    ana = 2 * tl.F2X / lam * (1 - af * math.exp(-t / tf) - as_ * math.exp(-t / ts))
    assert num == pytest.approx(ana, rel=1e-6)

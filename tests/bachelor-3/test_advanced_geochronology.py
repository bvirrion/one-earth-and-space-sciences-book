"""Tests for the concordia, Ar-Ar, model-age and cosmogenic figdata scripts
(Year 3, ch. 13)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import arar_spectrum as ar  # noqa: E402
import concordia as cc  # noqa: E402
import cosmogenic as cg  # noqa: E402
import model_ages as ma  # noqa: E402


def test_concordia_points_give_equal_ages():
    for t in (10.0, 310.0, 2500.0):
        x, y = cc.concordia(t)
        assert cc.age206(float(y)) == pytest.approx(t, rel=1e-12)
        assert cc.age207(float(x)) == pytest.approx(t, rel=1e-12)


@pytest.mark.parametrize("f", [0.0, 0.1, 0.5, 0.9])
def test_episodic_lead_loss_lies_on_the_chord(f):
    a = cc.lead_loss_point(310.0, 95.0, f)
    b = cc.lead_loss_explicit(310.0, 95.0, f)
    assert float(a[0]) == pytest.approx(b[0], rel=1e-12)
    assert float(a[1]) == pytest.approx(b[1], rel=1e-12)


def test_exact_chord_returns_both_ages_and_tw_is_straight():
    x1, y1 = cc.concordia(310.0)
    x2, y2 = cc.concordia(95.0)
    b = float((y1 - y2) / (x1 - x2))
    a = float(y1 - b * x1)
    up, lo = cc.intercepts(a, b)
    assert up == pytest.approx(310.0, abs=1e-6)
    assert lo == pytest.approx(95.0, abs=1e-6)
    pts = [cc.lead_loss_point(310.0, 95.0, f) for f in (0.1, 0.4, 0.8)]
    tw = [cc.tera_wasserburg(*p) for p in pts]
    s1 = (tw[1][1] - tw[0][1]) / (tw[1][0] - tw[0][0])
    s2 = (tw[2][1] - tw[1][1]) / (tw[2][0] - tw[1][0])
    assert float(s1) == pytest.approx(float(s2), rel=1e-9)


def test_zircon_fit_recovers_the_varden_granite():
    zs = cc.zircons()
    a, b, s_b, xb, yb, mswd = cc.fit_line([z[1] for z in zs], [z[2] for z in zs], [z[3] for z in zs])
    up, lo = cc.intercepts(a, b)
    assert abs(up - 310.0) < 5.0
    assert abs(lo - 95.0) < 10.0
    lo_up, hi_up = cc.pivot_intercepts(a, b, s_b, xb, yb)
    assert lo_up < 310.0 < hi_up
    assert 0.1 < mswd < 3.0


def test_ar_age_equation_and_j():
    j = ar.j_factor()
    assert ar.age(ar.R_MONITOR, j) == pytest.approx(ar.T_MONITOR, rel=1e-12)
    j, rows = ar.steps()
    for r in rows:
        assert ar.age(r[4], j) == pytest.approx(r[6])
    plateau = [rows[i] for i in ar.PLATEAU]
    assert len(plateau) >= 5 and sum(r[1] for r in plateau) > 50
    m, s, mswd = ar.weighted_mean([r[6] for r in plateau], [r[7] for r in plateau])
    assert abs(m - 296.0) < 1.0 and mswd < 2.0


def test_weighted_mean_mswd_has_expectation_one():
    rng = np.random.default_rng(3)
    s = np.array([1.0, 2.0, 0.5, 1.5, 1.0])
    vals = []
    for _ in range(20000):
        x = rng.normal(0.0, s)
        vals.append(ar.weighted_mean(x, s)[2])
    assert np.mean(vals) == pytest.approx(1.0, abs=0.03)


def test_model_ages():
    # the sample meets CHUR at T_CHUR and the depleted mantle at T_DM
    t = ma.model_age(ma.SAMPLE, ma.CHUR)
    assert ma.ratio_at(ma.SAMPLE, t) == pytest.approx(ma.ratio_at(ma.CHUR, t), abs=1e-12)
    t = ma.model_age(ma.SAMPLE, ma.DM)
    assert ma.ratio_at(ma.SAMPLE, t) == pytest.approx(ma.ratio_at(ma.DM, t), abs=1e-12)
    assert ma.model_age(ma.SAMPLE, ma.DM) > ma.model_age(ma.SAMPLE, ma.CHUR)
    # the depleted mantle line starts from CHUR about 4.55 Ga ago
    assert abs(ma.eps(ma.DM, 4.55)) < 0.2


@pytest.mark.parametrize("eps", [0.0, 1.0, 10.0])
def test_cosmogenic_closed_form_matches_path_integration(eps):
    t = 2e5
    assert cg.concentration(t, eps) == pytest.approx(cg.concentration_ode(t, eps), rel=1e-3)


def test_cosmogenic_limits():
    # no erosion, short exposure: N = P t; exposure age inverts it
    assert cg.concentration(1000.0, 0.0) == pytest.approx(cg.P_SLHL * 1000.0, rel=1e-3)
    n = float(cg.concentration(5e5, 0.0))
    assert cg.exposure_age(n) == pytest.approx(5e5, rel=1e-9)
    # steady state recovers the erosion rate, and without decay Book 3's formula
    n = cg.P_SLHL / (cg.LAMBDA + cg.mu(10.0))
    assert cg.erosion_rate(n) == pytest.approx(10.0, rel=1e-9)
    no_decay = cg.P_SLHL * cg.ATT / (cg.RHO * 10.0 * 1e-4)
    assert n == pytest.approx(no_decay, rel=0.04)


def test_tw_line_is_the_wetherill_line_transformed():
    zs = cc.zircons()
    a, b = cc.fit_line([z[1] for z in zs], [z[2] for z in zs], [z[3] for z in zs])[:2]
    for x in (0.1, 0.25, 0.4):
        y = a + b * x
        xt, yt = cc.tera_wasserburg(x, y)
        assert float(yt) == pytest.approx((1 - a * float(xt)) / (cc.U85 * b), rel=1e-12)

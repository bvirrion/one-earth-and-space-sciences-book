"""Tests for the Rayleigh distillation, carbon mass balance and LR04 scripts
(Year 3, ch. 14)."""
import math
import os
import sys

import numpy as np
import pytest
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import carbon_mass_balance as cm  # noqa: E402
import lr04_d18o as lr  # noqa: E402
import rayleigh_distillation as rd  # noqa: E402


def test_iapws_sublimation_check_value():
    # IAPWS R14-08 check value: 8.94735e-6 MPa at 230 K, with pt = 611.657 Pa
    p = 611.657 * math.exp(rd.ln_ei(230.0 - 273.15))
    assert p == pytest.approx(8.94735, rel=1e-5)


def test_alpha_ice_vapour_matches_the_product_at_zero():
    # alpha(ice-vapour) = alpha(ice-water) alpha(water-vapour) at 0 degC: 1.0035 x 1.0117
    assert rd.alpha18(0.0) == pytest.approx(1.0035 * 1.0117, abs=2e-4)


def test_constant_alpha_reduces_to_the_rayleigh_law():
    t = -20.0
    a = 1.01
    d = rd.vapour(t, lambda _t: a, -20.0)
    assert (1000 + d) / 980.0 == pytest.approx(rd.frac(t) ** (a - 1), rel=1e-10)


def test_vapour_against_ode_and_mass_balance_of_isotopes():
    # integrate the heavy-isotope budget directly: d(R f)/df = alpha R
    def rhs(t, y):
        r = y[0]
        return [(rd.alpha18(t) - 1.0) * r * rd.dlnf_dt(t)]
    sol = solve_ivp(rhs, (0.0, -30.0), [0.98], rtol=1e-11, atol=1e-14)
    d_ode = sol.y[0, -1] * 1000.0 - 1000.0
    assert d_ode == pytest.approx(rd.vapour(-30.0, rd.alpha18, -20.0), abs=1e-6)


def test_snow_gets_lighter_and_stepwise_is_close():
    pts = [rd.point(t)[1] for t in (-10.0, -20.0, -30.0)]
    assert pts[0] > pts[1] > pts[2]
    legs = rd.stepwise([(0.0, -10.0), (-10.0, -20.0), (-20.0, -30.0)])
    assert legs[-1][2] == pytest.approx(pts[2], abs=0.2)


def test_carbon_mass_balance_roundtrip_and_published_pairs():
    for f in (0.1, 0.2, 0.3):
        assert cm.f_org(cm.d_carb(f, -25.0), -25.0) == pytest.approx(f)
    assert cm.d_carb(0.2, -25.0) == pytest.approx(0.0)
    for d, s, m in cm.PUBLISHED:
        res = cm.implied_reservoir(d, s, m)
        assert 4e4 < res < 7e4
        assert cm.mass_added(d, s, res) == pytest.approx(m)
        # the mixture has the shifted composition
        assert (res * 0.0 + m * s) / (res + m) == pytest.approx(d)


def test_lr04_stack_and_lgm():
    s = lr.stack()
    assert np.all(np.diff(s[:, 0]) > 0)
    hol, lgm, amp = lr.lgm_amplitude(s)
    assert 3.0 < hol < 3.5 and 4.7 < lgm < 5.2
    assert 1.4 < amp < 2.0

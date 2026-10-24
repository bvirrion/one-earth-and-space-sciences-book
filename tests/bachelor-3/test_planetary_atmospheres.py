"""Tests for the planetary atmospheres scripts (Year 3, ch. 27)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import habitability as hb  # noqa: E402
import jeans_escape as je  # noqa: E402
import runaway_greenhouse as rg  # noqa: E402


def test_escape_parameter_is_velocity_ratio_squared():
    for name, (mass, r, z, t) in je.BODIES.items():
        rm = (r + z) * 1e3
        lam = je.escape_parameter(mass, rm, t, 1.008)
        assert lam == pytest.approx((je.escape_velocity(mass, rm) / je.thermal_speed(t, 1.008)) ** 2)
    # lambda is proportional to the mass of the particle
    assert je.body_lambda("Earth", 16.0) == pytest.approx(16.0 * je.body_lambda("Earth", 1.0))


def test_gronoff_table_values_at_the_planetary_radius():
    # Gronoff et al. (2020) Table 2 quotes lambda for H with the radius of the planet
    lam = lambda b: je.escape_parameter(je.BODIES[b][0], je.BODIES[b][1] * 1e3, je.BODIES[b][3], 1.008)
    assert lam("Venus") == pytest.approx(22.3, abs=0.3)
    assert lam("Titan") == pytest.approx(2.3, abs=0.1)
    assert je.escape_parameter(5.97e24, 6378.1e3, 800.0, 1.008) == pytest.approx(9.4, abs=0.1)


def test_jeans_flux_by_numerical_integration():
    # integrate the upward flux of a Maxwellian above v_esc and compare
    t, m_u, n = 1000.0, 1.008, 1.0
    u = je.thermal_speed(t, m_u)
    lam = 3.0
    vesc = u * math.sqrt(lam)
    # flux = n / (u^3 pi^1.5) * int_vesc^inf v^3 exp(-v^2/u^2) dv * pi  (angle integral = pi)
    steps = 20000
    vmax = vesc + 12 * u
    h = (vmax - vesc) / steps
    s = 0.0
    for i in range(steps + 1):
        v = vesc + i * h
        w = 1 if i in (0, steps) else (4 if i % 2 else 2)
        s += w * v ** 3 * math.exp(-(v / u) ** 2)
    s *= h / 3
    flux = n / (u ** 3 * math.pi ** 1.5) * math.pi * s
    assert flux == pytest.approx(je.jeans_flux(n, t, m_u, lam), rel=1e-6)


def test_saturation_and_latent_heat():
    assert rg.p_sat(373.124) == pytest.approx(101325, rel=2e-4)
    assert rg.p_sat(273.16) == pytest.approx(611.657, rel=1e-5)
    # ideal-vapour Clausius-Clapeyron gives the latent heat within a few per cent
    assert rg.latent_heat(300.0) == pytest.approx(2.44e6, rel=0.02)
    # the moist adiabat is shallower than the dry one and tends to it when dry
    assert rg.lapse(300.0, 1e5) < rg.R_A / rg.CP_A
    assert rg.lapse(200.0, 1e5) == pytest.approx(rg.R_A / rg.CP_A, rel=1e-3)


def test_olr_plateau():
    assert rg.olr(250.0, 0.0) == pytest.approx(rg.SIGMA * 250.0 ** 4, rel=1e-9)
    hot = [rg.olr(t) for t in (500.0, 550.0, 600.0)]
    assert max(hot) - min(hot) < 2.0
    assert hot[-1] == pytest.approx(291.0, abs=5.0)
    assert rg.olr(288.0) < rg.olr(350.0) < rg.olr(450.0)


def test_habitable_zone_fit():
    assert hb.hz_distance("mg", 5780.0, 1.0) == pytest.approx(0.99, abs=0.01)
    assert hb.hz_distance("maxg", 5780.0, 1.0) == pytest.approx(1.70, abs=0.01)
    assert hb.hz_distance("rv", 5780.0, 1.0) == pytest.approx(0.75, abs=0.01)
    # a cooler star: the same limits at lower fluxes
    assert hb.s_eff("maxg", 3500.0) < hb.s_eff("maxg", 5780.0)


def test_phase_curves():
    assert hb.p_methane(111.6) == pytest.approx(1.013, rel=0.03)  # normal boiling point near 111 K
    assert hb.p_water(273.16) == pytest.approx(611.657, rel=1e-6)
    assert hb.p_water(647.096) == pytest.approx(22.064e6, rel=1e-6)

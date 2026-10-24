"""Tests for the Rossby-wave, Eady and Held-Hou scripts (Year 3, ch. 20)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import eady  # noqa: E402
import held_hou as hh  # noqa: E402
import rossby_waves as rw  # noqa: E402


def test_rossby_dispersion_phase_and_group():
    k, l, u = rw.k_of_n(5), 1e-6, 15.0
    assert rw.omega(k, l, u) == pytest.approx(k * rw.phase_speed(k, l, u))
    dk = k * 1e-6
    cg = (rw.omega(k + dk, l, u) - rw.omega(k - dk, l, u)) / (2 * dk)
    assert rw.group_velocity(k, l, u) == pytest.approx(cg, rel=1e-6)
    # l = 0: group velocity exceeds phase speed by 2 beta / k^2
    assert rw.group_velocity(k, 0, u) - rw.phase_speed(k, 0, u) == pytest.approx(2 * rw.beta(45) / k ** 2)
    assert rw.phase_speed(k, 0, 0.0) < 0                     # westward without a current


def test_stationary_wave():
    n = rw.stationary_n(15.0, 45.0)
    assert rw.phase_speed(rw.k_of_n(n), 0, 15.0) == pytest.approx(0.0, abs=1e-9)
    circ = 2 * math.pi * rw.A_EARTH * math.cos(math.radians(45.0))
    assert circ / rw.stationary_wavelength(15.0, 45.0) == pytest.approx(n)
    assert rw.stationary_n(20.0, 45.0) < n < rw.stationary_n(10.0, 45.0)


def test_eady_classic_numbers():
    mu, s = eady.argmax_growth()
    assert mu == pytest.approx(1.6061, abs=2e-4)
    assert s == pytest.approx(0.3098, abs=2e-4)
    assert eady.critical_mu() == pytest.approx(2.3994, abs=2e-4)
    assert eady.growth(2.5) == 0.0 and eady.growth(1.0) > 0


def test_standard_atmosphere_heights():
    assert eady.height_of_p(101.29) == pytest.approx(0.0, abs=10.0)   # the model mixes 288.08 and 288.14 K
    assert 8000 < eady.height_of_p(25.0) - eady.height_of_p(85.0) < 10000
    lam, _ = eady.observed_shear()
    assert 1e-3 < lam < 4e-3                                   # s^-1


def test_held_hou_construction():
    for dd in hh.DELTAS:
        delta = 1 / dd
        ph = hh.phi_h(delta)
        assert hh.theta_m(ph, delta) == pytest.approx(hh.theta_e(ph, delta))
        n = 2000
        dphi = ph / n
        ie = sum(hh.theta_e((i + 0.5) * dphi, delta) for i in range(n)) * dphi
        im = sum(hh.theta_m((i + 0.5) * dphi, delta) for i in range(n)) * dphi
        assert im == pytest.approx(ie, rel=1e-7)               # equal areas
    # thermal wind: 2 Omega phi u_M / H = -(g / a) d(theta_M/theta0)/dphi
    phi, delta, d = 0.3, 1 / 3, 1e-6
    dth = (hh.theta_m(phi + d, delta) - hh.theta_m(phi - d, delta)) / (2 * d)
    assert 2 * hh.OMEGA * phi * hh.u_m(phi) / hh.H_ILL == pytest.approx(-hh.G / hh.A_EARTH * dth, rel=1e-6)


def test_observed_hadley_edges():
    d = hh.load_v()
    psi = hh.psi500(d, range(1, 13))
    assert 25 < hh.hadley_edge(psi, 1) < 40
    assert -40 < hh.hadley_edge(psi, -1) < -25

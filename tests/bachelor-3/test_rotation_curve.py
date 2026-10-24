"""Tests for the Milky Way rotation-curve model (Year 3, ch. 29)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import rotation_curve as rc  # noqa: E402


def test_gravitational_constant_in_galactic_units():
    # G = 4.30e-6 kpc (km/s)^2 per solar mass
    assert rc.G == pytest.approx(4.3009e-6, rel=1e-4)


def test_components_tend_to_keplerian_and_vanish_at_centre():
    for v in (rc.v_plummer(1e-9, *rc.BULGE), rc.v_miyamoto_nagai(1e-9, *rc.THIN)):
        assert v < 1e-3
    # far away every component behaves as a point mass
    r = 1e4
    m = rc.BULGE[0] * rc.MASS_UNIT
    assert rc.v_plummer(r, *rc.BULGE) == pytest.approx(math.sqrt(rc.G * m / r), rel=1e-6)
    m = rc.THIN[0] * rc.MASS_UNIT
    assert rc.v_miyamoto_nagai(r, *rc.THIN) == pytest.approx(math.sqrt(rc.G * m / r),
                                                            rel=1e-5)
    # the stellar discs of Model I add up to 7.9e10 solar masses (7.8e10 in the paper)
    assert (rc.THIN[0] + rc.THICK[0]) * rc.MASS_UNIT == pytest.approx(7.888e10)


def test_nfw_mass_and_velocity():
    rho0, rs = 1e7, 15.0
    # mass by direct integration of the density
    n, r_max = 20000, 20.0
    h = r_max / n
    m = 0.0
    for i in range(n):
        r = (i + 0.5) * h
        x = r / rs
        m += 4 * math.pi * r * r * rho0 / (x * (1 + x) ** 2) * h
    assert rc.nfw_mass(r_max, rho0, rs) == pytest.approx(m, rel=1e-5)
    assert rc.v_nfw(r_max, rho0, rs) == pytest.approx(math.sqrt(rc.G * m / r_max), rel=1e-5)


def test_fit_recovers_known_halo_from_synthetic_data():
    true = (8.0e6, 18.0)
    radii = [5 + 0.5 * i for i in range(40)]
    data = [(r, rc.v_total(r, *true), 2.0) for r in radii]
    rho0, rs, chi2 = rc.fit_nfw(data, start=(1.5e7, 10.0))
    assert rho0 == pytest.approx(true[0], rel=1e-5)
    assert rs == pytest.approx(true[1], rel=1e-5)
    assert chi2 < 1e-8


def test_fit_to_eilers_matches_their_halo():
    rho0, rs, chi2 = rc.fit_nfw(rc.eilers_rows())
    # Eilers et al. 2019: Rs = 14.8 +- 0.4 kpc, rho0 = (1.06 +- 0.09) e7 Msun/kpc^3
    assert rs == pytest.approx(14.8, abs=0.4)
    assert rho0 == pytest.approx(1.06e7, abs=0.09e7)
    # the circular velocity at the Sun, 229.0 km/s in the paper
    assert rc.v_total(rc.R0, rho0, rs) == pytest.approx(229.0, abs=1.0)
    # beyond about 14 kpc the halo dominates (Eilers et al.)
    assert rc.v_nfw(13.0, rho0, rs) < rc.v_baryons(13.0)[3]
    assert rc.v_nfw(15.0, rho0, rs) > rc.v_baryons(15.0)[3]


def test_enclosed_mass_and_slope():
    # a flat curve at 200 km/s gives M = R v^2 / G, about 1.86e11 Msun within 20 kpc
    assert rc.enclosed_mass(20.0, 200.0) == pytest.approx(20 * 4e4 / rc.G)
    assert rc.enclosed_mass(20.0, 200.0) == pytest.approx(1.86e11, rel=0.01)
    k, c = rc.linear_slope([(r, 230.0 - 1.7 * r) for r in (5, 10, 15, 20)])
    assert k == pytest.approx(-1.7) and c == pytest.approx(230.0)
    assert len(rc.EILERS) == 38

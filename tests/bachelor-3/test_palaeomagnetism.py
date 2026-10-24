"""Tests for the geomagnetism and palaeomagnetism figdata scripts (Year 3, ch. 4)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import igrf_field as ig  # noqa: E402
import magnetostratigraphy as ms  # noqa: E402
import palaeomag_stats as pm  # noqa: E402


def test_schmidt_low_degrees():
    th = np.radians(np.array([10.0, 47.0, 123.0]))
    c, s = np.cos(th), np.sin(th)
    p = ig.schmidt(3, th)
    assert np.allclose(p[2, 0], 1.5 * c ** 2 - 0.5)
    assert np.allclose(p[2, 1], math.sqrt(3) * c * s)
    assert np.allclose(p[2, 2], math.sqrt(3) / 2 * s ** 2)
    assert np.allclose(p[3, 0], 0.5 * (5 * c ** 3 - 3 * c))
    assert np.allclose(p[3, 3], math.sqrt(10) / 4 * s ** 3)


def test_axial_dipole_gives_the_dipole_formula():
    g = {(1, 0): -30000.0, (1, 1): 0.0}
    h = {(1, 1): 0.0}
    for lat in (-60.0, -20.0, 10.0, 35.0, 70.0):
        x, y, z = ig.field(lat, 25.0, coeffs=(g, h))
        inc, f, hh, dec = ig.elements(x, y, z)
        assert math.tan(math.radians(inc)) == pytest.approx(2 * math.tan(math.radians(lat)), rel=1e-6)
        assert f == pytest.approx(30000.0 * math.sqrt(1 + 3 * math.sin(math.radians(lat)) ** 2), rel=1e-6)
        assert dec == pytest.approx(0.0, abs=1e-9)


def test_dipole_moment_and_pole_2025():
    b0, m, plat, plon = ig.dipole(*ig.read_coeffs("e2025"))
    assert 7.5e22 < m < 7.9e22
    assert 79.0 < plat < 82.0 and -75.0 < plon < -70.0


def test_fisher_known_cases():
    # four directions 10 deg from (0, 50) on a symmetric cross: mean exact, R = 4 cos 10
    dirs = [pm.to_di(math.cos(math.radians(10.0)) * pm.to_xyz(0.0, 50.0)
                     + math.sin(math.radians(10.0)) * e)
            for e in (pm.to_xyz(0.0, -40.0), -pm.to_xyz(0.0, -40.0), np.array([0.0, 1.0, 0.0]),
                      np.array([0.0, -1.0, 0.0]))]
    d, i, n, r, k, a95 = pm.fisher_mean(dirs)
    assert i == pytest.approx(50.0) and r == pytest.approx(4 * math.cos(math.radians(10.0)))
    assert k == pytest.approx(3 / (4 - r))
    # two directions 20 deg either side of the mean: R = 2 cos 20
    d, i, n, r, k, a95 = pm.fisher_mean([(0.0, 20.0), (0.0, 60.0)])
    assert i == pytest.approx(40.0) and r == pytest.approx(2 * math.cos(math.radians(20.0)))


def test_fisher_alpha95_shrinks_like_root_n():
    rng = np.random.default_rng(5)
    a_small = np.mean([pm.fisher_mean(pm.fisher_draw(0, 50, 50, 10, rng))[5] for _ in range(300)])
    a_big = np.mean([pm.fisher_mean(pm.fisher_draw(0, 50, 50, 40, rng))[5] for _ in range(300)])
    assert a_small / a_big == pytest.approx(2.0, rel=0.12)


def test_vgp_round_trip():
    for d, i in ((34.0, 37.0), (300.0, 60.0), (170.0, -45.0), (5.0, 70.0)):
        plat, plon = pm.vgp(d, i)
        d2, i2, lat = pm.expected_direction(plat, plon)
        assert d2 == pytest.approx(d, abs=1e-6) and i2 == pytest.approx(i, abs=1e-6)


def test_present_axial_pole_gives_axial_field():
    d, i, lat = pm.expected_direction(90.0, 0.0)
    assert min(d, 360.0 - d) == pytest.approx(0.0, abs=1e-6)
    assert math.tan(math.radians(i)) == pytest.approx(2 * math.tan(math.radians(pm.SITE[0])))
    assert lat == pytest.approx(pm.SITE[0])


def test_zijderveld_endpoints():
    rows = pm.zijderveld()
    first, after300, last = rows[0], [r for r in rows if r[0] == 300][0], rows[-1]
    v = np.array(after300[1:4])
    assert np.allclose(v, 40.0 * pm.to_xyz(35.0, 38.0))
    assert np.allclose(last[1:4], 0.0)
    assert np.linalg.norm(first[1:4]) > 40.0


def test_magnetostratigraphy_rates():
    ties = ms.ties()
    assert [t for t, h in ties] == sorted([t for t, h in ties], reverse=True)
    assert ms.fit_rate([x for x in ties if x[0] >= 3.2]) == pytest.approx(40.0, rel=0.01)
    assert ms.fit_rate([x for x in ties if x[0] <= 3.207]) == pytest.approx(55.0, rel=0.01)
    assert ms.polarity(3.0) == 1 and ms.polarity(3.1) == 0

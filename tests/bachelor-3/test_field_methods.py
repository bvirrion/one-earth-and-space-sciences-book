"""Tests for the field-geophysics models of Year 3, ch. 31 (field and lab methods III):
the granite gravity anomaly, the magnetic dyke, the resistivity sounding, the radar
hyperbola."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "shared"))
import gpr_radargram as gpr  # noqa: E402
import gravity_granite as gg  # noqa: E402
import magnetic_dyke as md  # noqa: E402
import region  # noqa: E402
import resistivity_sounding as rs  # noqa: E402


# --- gravity -----------------------------------------------------------------------------
def test_prism_far_away_is_a_point_mass():
    a = 100.0
    dg = gg.prism_gz(-a / 2, a / 2, -a / 2, a / 2, -1050.0, -950.0, 300.0, 0.0, 0.0, 1000.0)
    m = 1000.0 * a ** 3
    assert dg == pytest.approx(gg.point_gz(m, 300.0, 1000.0), rel=2e-3)


def test_wide_thin_prism_is_a_bouguer_slab():
    dg = gg.prism_gz(-1e6, 1e6, -1e6, 1e6, -110.0, -100.0, 0.0, 0.0, 0.0, 1000.0)
    assert dg == pytest.approx(2 * math.pi * gg.G * 1000.0 * 10.0, rel=1e-4)


def test_square_column_on_axis_close_to_the_cylinder():
    """A column of square section a x a against the cylinder of equal area."""
    a, top, bot = 200.0, 100.0, 900.0
    dg = gg.prism_gz(-a / 2, a / 2, -a / 2, a / 2, -bot, -top, 0.0, 0.0, 0.0, 1000.0)
    cyl = gg.vcyl_axis(a / math.sqrt(math.pi), top, bot, 1000.0)
    assert dg == pytest.approx(cyl, rel=0.01)


def test_sphere_half_width_rule():
    z = 500.0
    xs = np.linspace(-3000, 3000, 6001)
    xh, _, _ = gg.half_width(xs, gg.point_gz(1e10, xs, z))
    assert z / xh == pytest.approx(1.305, abs=0.002)
    zs, m = gg.sphere_from_halfwidth(gg.point_gz(1e10, 0.0, z), xh)
    assert zs == pytest.approx(z, rel=1e-3) and m == pytest.approx(1e10, rel=2e-3)


def test_varden_granite_anomaly():
    prisms = gg.granite_prisms()
    vol, mass, zc = gg.body_stats(prisms)
    assert vol / 1e9 == pytest.approx(1.34, abs=0.01)
    px = np.arange(2000.0, 5001.0, 50.0)
    pz = np.array([region.topo(x, gg.Y_LINE) for x in px])
    g = gg.anomaly(prisms, px, np.full_like(px, gg.Y_LINE), pz) * gg.SI_TO_MGAL
    assert g.min() == pytest.approx(-2.29, abs=0.01)
    assert px[int(np.argmin(g))] == pytest.approx(3500.0, abs=50)
    # the sphere of the half-width rule sits above the true centre of mass
    xh, _, pk = gg.half_width(px, g)
    zs, _ = gg.sphere_from_halfwidth(pk, xh)
    assert zs < region.topo(3500.0, gg.Y_LINE) - zc


# --- magnetics ---------------------------------------------------------------------------
def test_thin_dyke_limit_and_half_width():
    xs = np.arange(-1500.0, 1500.1, 2.0)
    thick = md.prism_dT(-0.5, 0.5, 200.0, 1e7, 0.02, 50000.0, 70.0, 90.0, xs)
    thin = md.thin_dyke_dT(xs, 200.0, 1.0, 0.02, 50000.0, 70.0)
    assert np.max(np.abs(thick - thin)) < 1e-3 * thin.max()
    xh, x0, _ = md.half_width(xs, thick)
    assert xh == pytest.approx(200.0, rel=2e-3) and x0 == pytest.approx(0.0)


def test_dyke_symmetry_and_pole_reduction():
    xs = np.arange(-800.0, 800.1, 10.0)
    ns = md.prism_dT(-10, 10, 100, 2e4, 0.01, 50000, 60, 90, xs)
    assert np.allclose(ns, ns[::-1], atol=1e-9)              # N-S strike: symmetric
    ew = md.prism_dT(-10, 10, 100, 2e4, 0.01, 50000, 60, 0, xs)
    assert ew.min() < -0.1 * ew.max()                          # E-W strike: a negative lobe
    pole = md.prism_dT(-10, 10, 100, 2e4, 0.01, 50000, 90, 0, xs)
    assert np.allclose(pole, pole[::-1], atol=1e-9) and pole.min() > -0.05


def test_varden_dyke_depth_from_half_width():
    top, ground, depth = md.varden_dyke()
    assert top < region.base_cover(md.DYKE_X, md.PROFILE_Y) + 1e-9   # below the unconformity
    xs = np.arange(1200.0, 3200.1, 10.0)
    xh, xpk, pk = md.half_width(xs, md.varden_profile(xs))
    assert xpk == pytest.approx(md.DYKE_X, abs=10)
    assert xh == pytest.approx(depth, rel=0.03)
    assert pk == pytest.approx(21.0, abs=0.5)


# --- resistivity -------------------------------------------------------------------------
@pytest.mark.parametrize("rho2", [10.0, 1000.0])
def test_hankel_against_image_series(rho2):
    for s in (1.0, 5.0, 20.0, 100.0):
        assert rs.schlumberger(s, [100.0, rho2], [5.0]) == pytest.approx(
            rs.two_layer_schlumberger(s, 100.0, rho2, 5.0), rel=1e-6)


def test_limits_and_geometric_factors():
    assert rs.two_layer_wenner(0.01, 100.0, 1000.0, 5.0) == pytest.approx(100.0, rel=1e-4)
    assert rs.two_layer_wenner(1e4, 100.0, 1000.0, 5.0) == pytest.approx(1000.0, rel=0.01)
    assert rs.k_wenner(10.0) == pytest.approx(62.83, abs=0.01)
    # Schlumberger with l -> s/3 is the Wenner array of spacing a = 2l
    assert rs.k_schlumberger(15.0, 5.0) == pytest.approx(rs.k_wenner(10.0))


def test_conductive_layer_over_insulator_45_degree_branch():
    rhos, hs = [600.0, 222.2, 1e8], [1.5, 4.5]
    S = 1.5 / 600.0 + 4.5 / 222.2
    assert rs.schlumberger(100.0, rhos, hs) == pytest.approx(100.0 / S, rel=2e-3)


def test_archie_round_trip():
    rho = rs.archie(20.0, 0.30)
    assert rho == pytest.approx(222.2, abs=0.1)
    assert rs.archie_porosity(rho, 20.0) == pytest.approx(0.30)


# --- radar -------------------------------------------------------------------------------
def test_radar_velocity_and_hyperbola():
    v = gpr.velocity(4.0)
    assert v == pytest.approx(0.15, abs=0.001)
    t0 = 2 * 0.8 / v
    t = float(gpr.pipe_time(5.5, 4.0, 0.8, v))
    assert gpr.velocity_from_hyperbola(5.5, t, 4.0, t0) == pytest.approx(v)
    assert gpr.skin_depth_wave(1.0, 1.0) == pytest.approx(0.0053, abs=1e-4)

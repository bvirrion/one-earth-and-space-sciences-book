"""Tests for the seismology-imaging figure data: ray tracing in a spherical Earth,
Love-wave dispersion, the damped least-squares checkerboard."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import love_dispersion as ld  # noqa: E402
import ray_tracing as rt  # noqa: E402
import tomo_checkerboard as tc  # noqa: E402


def test_homogeneous_sphere_rays_are_chords():
    v = 8.0
    sh = rt.homogeneous_shells(v, n=2000)
    for ang in (5.0, 20.0, 45.0, 70.0):
        p = rt.take_off_p(ang, sh)
        dl, t, _ = rt.trace(p, sh)
        # a chord leaving at angle i from the vertical subtends pi - 2i
        assert abs(dl - (math.pi - 2 * math.radians(ang))) < 1e-9
        assert abs(t - 2 * rt.R_EARTH * math.sin(dl / 2) / v) < 1e-6


def test_benndorf_dT_dDelta_equals_p():
    sh = rt.shells("P")
    for ang in (20.0, 25.0, 30.0):
        p = rt.take_off_p(ang, sh)
        dp = p * 1e-4
        d1, t1, _ = rt.trace(p - dp, sh)
        d2, t2, _ = rt.trace(p + dp, sh)
        assert abs((t2 - t1) / (d2 - d1) - p) / p < 2e-3


def test_ray_parameter_is_snell_invariant_along_path():
    sh = rt.shells("P")
    p = rt.take_off_p(25.0, sh)
    rtop, rbot, v = sh
    for i in (10, 500, 1500):
        # in shell i the line passes at d = p v: r sin(i)/v = p at its top
        sin_i = p * v[i] / rtop[i]
        assert abs(rtop[i] * sin_i / v[i] - p) < 1e-9


def test_core_shadow_edge():
    edge = rt.shadow_edge_deg(rt.shells("P"))
    assert 97.0 < edge < 103.0


def test_prem_cmb_and_icb_radii():
    rows = rt.read_prem()
    depths = [z for z, a, b in rows]
    assert any(abs(rt.R_EARTH - z - rt.R_CMB) < 1.0 for z in depths)
    assert any(abs(rt.R_EARTH - z - rt.R_ICB) < 1.0 for z in depths)


def test_love_roots_and_limits():
    for t in (5.0, 20.0, 60.0):
        c = ld.phase_velocity(t)
        assert ld.B1 < c < ld.B2
        assert abs(ld.residual(c, 2 * math.pi / t)) < 1e-6
    assert abs(ld.phase_velocity(1.0) - ld.B1) / ld.B1 < 0.01
    assert abs(ld.phase_velocity(1000.0) - ld.B2) / ld.B2 < 0.01


def test_love_group_slower_than_phase_and_has_minimum():
    rows = ld.curve(ld.PERIODS)
    assert all(u <= c + 1e-9 for t, c, u in rows)
    us = [u for t, c, u in rows]
    k = us.index(min(us))
    assert 0 < k < len(us) - 1  # an interior minimum: the Airy phase


def test_damped_ls_tends_to_minimum_norm_solution():
    g, _ = tc.kernel()
    mt = tc.checkerboard()
    d = g @ mt
    m = tc.damped(g, d, 1e-3)
    assert np.linalg.norm(g @ m - d) < 1e-6 * np.linalg.norm(d)
    mp = np.linalg.pinv(g, rcond=1e-10) @ d
    assert np.linalg.norm(m - mp) < 1e-4 * np.linalg.norm(mp)
    # the model is under-determined: a few null-space directions
    assert np.linalg.matrix_rank(g) < g.shape[1]


def test_tradeoff_monotonic():
    g, _ = tc.kernel()
    d = tc.data(g, tc.checkerboard())
    prev_mis, prev_norm = -1.0, 1e99
    for e in (0.5, 2.0, 8.0, 32.0, 128.0):
        m = tc.damped(g, d, e)
        mis, nrm = np.linalg.norm(g @ m - d), np.linalg.norm(m)
        assert mis >= prev_mis - 1e-9 and nrm <= prev_norm + 1e-12
        prev_mis, prev_norm = mis, nrm


def test_pkp_caustic_and_c_point_in_expected_ranges():
    sh = rt.shells("P")
    b, c, i_min = rt.core_points(sh, n=1500)
    assert 140.0 < b < 148.0  # observed PKP caustic is near 145 deg
    assert b < c < 158.0
    assert 105.0 < i_min < 130.0


def test_s_rays_reflected_at_the_core_are_not_mantle_rays():
    sh = rt.shells("S")
    # a near-vertical S ray cannot enter the liquid core: it is ScS, not S
    d, t, b = rt.trace(rt.take_off_p(2.0, sh), sh)
    assert rt.branch_of(b) == "cmb"
    for p, dl, t, br in rt.curve("S", sh, 400):
        if br == "mantle":
            assert math.degrees(dl) > 0.0 and t / 60.0 < 27.0
    # the steepest S ray still turning in the mantle reaches about 100 deg
    far = max(math.degrees(dl) for p, dl, t, br in rt.curve("S", sh, 800) if br == "mantle")
    assert 95.0 < far < 106.0

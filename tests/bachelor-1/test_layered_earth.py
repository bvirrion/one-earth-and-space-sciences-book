"""Tests for the layered-earth figure data: PREM profiles and functionals, and the
two-layer refraction travel times."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import prem_profiles as pp  # noqa: E402
import refraction as rf  # noqa: E402

EARTH_MASS = 5.9722e24      # ledger earth:mass
EARTH_MOI = 0.3308          # ledger earth:MoI
PREM_P_CENTRE = 363.8524    # GPa, PREM Table II (3638.524 kbar), ledger prem:table2
PREM_P_CMB = 135.751        # GPa (1357.510 kbar)
PREM_G_CMB = 10.6823        # m/s2 (1068.23 cm/s2)


def test_discontinuities():
    t = pp.table()
    # the core-mantle boundary at 2891 km depth: vS drops to zero below it
    assert abs(pp.R_EARTH - pp.R_CMB - 2891.0) < 1e-9
    assert pp.vs(pp.R_CMB, below=True) == 0.0 and pp.vs(pp.R_CMB) > 7.0
    # the outer core is liquid throughout, the inner core solid
    assert all(r[2] == 0.0 for r in t if r[4] == "outer-core")
    assert all(r[2] > 3.0 for r in t if r[4] == "inner-core")
    # inner-core boundary at 5149.5 km depth
    assert abs(pp.R_EARTH - pp.R_ICB - 5149.5) < 1e-9
    assert pp.vs(pp.R_ICB, below=True) > 3.0 and pp.vs(pp.R_ICB) == 0.0


def test_mass_and_moment():
    assert abs(pp.total_mass() / EARTH_MASS - 1.0) < 0.005
    assert abs(pp.moment_factor() - EARTH_MOI) < 0.002


def test_pressure_and_gravity():
    assert abs(pp.pressure(0.0) / 1e9 / PREM_P_CENTRE - 1.0) < 0.01
    assert abs(pp.pressure(pp.R_CMB) / 1e9 / PREM_P_CMB - 1.0) < 0.01
    assert abs(pp.gravity(pp.R_CMB) / PREM_G_CMB - 1.0) < 0.01
    # gravity peaks near the core-mantle boundary, not at the surface
    assert pp.gravity(pp.R_CMB) > pp.gravity(pp.R_EARTH)


def test_core_fraction_and_shells():
    assert abs(pp.mass_within(pp.R_CMB) / pp.total_mass() - 0.325) < 0.002
    total = sum(pp.shell(r1, r2)[1] for _, r1, r2 in pp.SHELLS)
    assert abs(total / pp.total_mass() - 1.0) < 1e-9


def test_adams_williamson():
    # self-compression explains PREM's density increase within 1 % in the lower mantle
    # and the outer core
    for top, bot in ((pp.R_LM_TOP, pp.R_CMB), (pp.R_CMB, pp.R_ICB)):
        for r, d_prem, d_aw in pp.adams_williamson(top, bot):
            assert abs(d_aw / d_prem - 1.0) < 0.01


def test_two_layer():
    # a uniform sphere has I/MR^2 = 0.4
    m, k = pp.two_layer(5000.0, 5000.0)
    assert abs(k - 0.4) < 1e-12


def test_crossover_equals_theorem():
    assert abs(rf.crossover_numeric() - rf.crossover()) < 1e-6
    for h, v1, v2 in ((10.0, 5.0, 7.0), (35.0, 6.0, 8.0), (50.0, 6.5, 8.2)):
        assert abs(rf.crossover_numeric(h, v1, v2) - rf.crossover(h, v1, v2)) < 1e-6
        assert abs(rf.depth_from_crossover(rf.crossover(h, v1, v2), v1, v2) - h) < 1e-9
        ti = rf.intercept(h, v1, v2)
        assert abs(rf.depth_from_intercept(ti, v1, v2) - h) < 1e-9


def test_reflection_tangent_to_head_wave():
    xc = rf.critical_distance()
    assert abs(rf.t_reflected(xc) - rf.t_head(xc)) < 1e-9
    # beyond it the head wave arrives first
    assert rf.t_head(xc + 50) < rf.t_reflected(xc + 50)
    assert math.isnan(rf.t_head(xc - 1))

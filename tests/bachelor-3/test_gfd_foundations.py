"""Tests for the inertial-oscillation, thermal-wind and buoyancy-frequency
scripts (Year 3, ch. 19)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import buoyancy_frequency as bf  # noqa: E402
import inertial_oscillation as io  # noqa: E402
import thermal_wind as tw  # noqa: E402


def test_inertial_circle_matches_closed_form():
    a = io.integrate()
    x, y = io.exact(a[:, 0])
    assert np.max(np.hypot(a[:, 1] - x, a[:, 2] - y)) < 1.0      # metres
    speed = np.hypot(a[:, 3], a[:, 4])
    assert np.allclose(speed, io.U_START, rtol=1e-6)


def test_inertial_radius_and_period():
    f = io.coriolis(45.0)
    assert io.radius() == pytest.approx(io.U_START / f)
    assert io.period_hours(io.coriolis(30.0)) == pytest.approx(2 * math.pi / io.OMEGA / 3600, rel=1e-9)
    # turns clockwise in the northern hemisphere: v becomes negative first
    a = io.integrate(t_end=600.0)
    assert a[-1, 4] < 0


def test_friction_shrinks_the_circles_and_the_current_drifts_them():
    s = io.integrate(r=io.R_FRIC)
    speed = np.hypot(s[:, 3], s[:, 4])
    assert speed[-1] == pytest.approx(io.U_START * math.exp(-io.R_FRIC * io.T_END), rel=1e-6)
    lo = io.integrate(r=io.R_FRIC, u0=io.U0)
    assert lo[-1, 1] - s[-1, 1] == pytest.approx(io.U0 * io.T_END, rel=1e-6)


def test_beta_plane_is_the_tangent_of_f():
    assert io.f_beta_plane(io.LAT) == pytest.approx(io.coriolis())
    d = 0.01
    slope = (io.coriolis(io.LAT + d) - io.coriolis(io.LAT - d)) / (2 * io.A_EARTH * math.radians(d))
    assert io.beta() == pytest.approx(slope, rel=1e-6)
    assert io.f_beta_plane(0.0) > io.coriolis(0.0)          # the tangent lies above the sine


def test_thermal_wind_inverse_pair():
    for lat in (30.0, 45.0, 60.0):
        du = tw.shear_from_gradient(-5e-6, lat)
        assert du > 0                                     # colder poleward: westerly shear
        assert tw.layer_gradient(du, 0.0, lat) == pytest.approx(-5e-6)


def test_observed_jets_and_gradients():
    d = tw.load()
    jan = max((d[(1, 200, lat)], lat) for lat in {k[2] for k in d} if lat > 0)
    assert 35 < jan[0] < 55 and 25 <= jan[1] <= 40          # subtropical jet near 30 N
    g = tw.layer_gradient(d[(1, 250, 45.0)], d[(1, 850, 45.0)], 45.0)
    assert -1e-5 < g < -1e-6                              # K/m, colder toward the pole


def test_eos80_and_theta_check_values():
    assert bf.rho0(35.0, 0.0) == pytest.approx(1028.1063, abs=1e-4)
    assert bf.theta(40.0, 40.0, 10000.0) == pytest.approx(36.89073, abs=1e-5)


def test_atmosphere_buoyancy_frequency():
    # troposphere: N^2 = g/T (Gamma_d - 0.00649); stratosphere isothermal: N^2 = g^2/(c_p T)
    h = 5000.0
    expect = bf.G / bf.t_atm(h) * (bf.G / bf.CP - 0.00649)
    assert bf.n2_atm(h) == pytest.approx(expect, rel=1e-6)
    assert bf.n2_atm(18000.0) == pytest.approx(bf.G ** 2 / (bf.CP * bf.t_atm(18000.0)), rel=1e-6)
    assert bf.G / bf.CP * 1000 == pytest.approx(9.8, abs=0.05)       # nws:dalr


def test_ocean_is_stably_stratified_with_a_seasonal_pycnocline():
    rows = bf.ocean_n2()
    assert sum(1 for _, n2 in rows if n2 < 0) <= 1
    zmax, n2max = max(rows, key=lambda r: r[1])
    assert zmax < 200
    # a few cycles per hour at most
    assert 1 < math.sqrt(n2max) * 3600 / (2 * math.pi) < 15

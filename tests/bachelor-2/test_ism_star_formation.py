"""Tests for the star-formation figure data (jeans.py)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import jeans as j  # noqa: E402


def test_jeans_scalings():
    m0 = j.jeans_mass(10.0, 1e4)
    assert abs(j.jeans_mass(40.0, 1e4) / m0 - 8.0) < 1e-12      # T^(3/2)
    assert abs(j.jeans_mass(10.0, 4e4) / m0 - 0.5) < 1e-12      # n^(-1/2)
    # the Jeans mass is the mass of a sphere of the Jeans radius at that density
    r = j.jeans_radius(10.0, 1e4)
    m_sphere = 4.0 / 3.0 * math.pi * r ** 3 * j.density(1e4)
    assert abs(m_sphere / m0 - 1.0) < 1e-12


def test_energy_criterion_at_jeans_mass():
    # at M = M_J and R = R_J, thermal energy 3MkT/(2 mu m_u) is half the gravitational 3GM^2/(5R)
    T, n = 10.0, 1e4
    M, R = j.jeans_mass(T, n), j.jeans_radius(T, n)
    thermal = 1.5 * M * j.K_B * T / (j.MU * j.M_U)
    grav = 0.6 * j.G * M * M / R
    assert abs(2.0 * thermal / grav - 1.0) < 1e-12


def test_free_fall_against_bergin_rule():
    # Bergin & Tafalla: t_ff ~ 4e7 / sqrt(n_H) yr; with rho = 1.4 m_H n_H (cosmic He)
    n_h = 2e4
    rho = 1.4 * j.M_U * 1.008 * n_h * 1e6
    t = math.sqrt(3.0 * math.pi / (32.0 * j.G * rho)) / j.YR
    assert abs(t / (4e7 / math.sqrt(n_h)) - 1.0) < 0.1


def test_values():
    assert abs(j.jeans_mass(10, 1e4) / j.M_SUN - 5.46) < 0.01
    assert abs(j.free_fall(1e4) / j.MYR - 0.338) < 0.002
    assert abs(j.grain_temperature(j.AU) - 278.3) < 0.1
    assert abs(j.grain_temperature(j.snow_line(170.0)) - 170.0) < 1e-9
    # the Sun's Kelvin-Helmholtz time is about 30 Myr
    assert 25 < j.kh_time(j.M_SUN, j.R_SUN, j.L_SUN) / j.MYR < 35


def test_disc_fit():
    f0, b, t0 = j.disc_fit()
    assert 0.9 < f0 < 1.05
    assert abs(t0 - 6.0) < 0.5          # Haisch et al.: overall lifetime ~6 Myr
    assert abs((f0 - 0.5) / b - 3.0) < 0.3

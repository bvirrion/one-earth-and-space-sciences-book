"""Tests for the heat-budget figure data: conductive geotherms with exponential heat
production, the adiabat, the oceanic geotherm, Kelvin's age and Perry's lid."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import geotherms as gt  # noqa: E402


def test_surface_gradient_is_q0_over_k():
    for qm in gt.QMS:
        h = 1.0
        grad = (gt.t_conductive(h, qm) - gt.t_conductive(0.0, qm)) / h
        assert abs(grad - gt.surface_heat_flow(qm) / gt.K) < 1e-6


def test_closed_form_equals_numerical_integration():
    for qm in gt.QMS:
        t, q = gt.numeric_geotherm(qm, zmax=100e3)
        assert abs(t - gt.t_conductive(100e3, qm)) < 1e-6
        assert abs(q - gt.heat_flow(100e3, qm)) < 1e-12


def test_linear_heat_flow_relation():
    # q0 - q_m = A0 D, whatever A0
    for a0 in (0.5e-6, 2.5e-6, 6e-6):
        assert abs(gt.surface_heat_flow(30e-3, a0) - 30e-3 - a0 * gt.D) < 1e-15
    # erosion by e keeps the line: A0 -> A0 exp(-e/D), same q_m, same slope D
    e = 3e3
    a0 = 3e-6
    a_new = a0 * math.exp(-e / gt.D)
    q_new = gt.heat_flow(e, 30e-3, a0)          # heat flow at the new surface
    assert abs(q_new - (30e-3 + a_new * gt.D)) < 1e-15


def test_uniform_layer_continuity():
    q0, a, h = 60e-3, 2e-6, 10e3
    eps = 1e-3
    assert abs(gt.t_uniform_layer(h - eps, q0, a, h) - gt.t_uniform_layer(h + eps, q0, a, h)) < 1e-4
    # below the layer the gradient is (q0 - a h) / k
    g = (gt.t_uniform_layer(30e3, q0, a, h) - gt.t_uniform_layer(20e3, q0, a, h)) / 10e3
    assert abs(g - (q0 - a * h) / gt.K) < 1e-12


def test_adiabat_matches_katsura():
    assert abs(gt.t_adiabat(50e3) + 273.15 - 1646.0) < 1e-9
    # extrapolated to the surface: the potential temperature, 1619 K
    assert abs(gt.potential_temperature() + 273.15 - 1619.0) < 1.0
    # at 410 km within 15 K of Katsura's 1799 K just above the discontinuity
    assert abs(gt.t_adiabat(410e3) + 273.15 - 1799.0) < 15.0


def test_lithosphere_base_is_where_geotherm_meets_adiabat():
    bases = [gt.lithosphere_base(qm) for qm in gt.QMS]
    assert bases[0] > bases[1] > bases[2]
    for qm, zb in zip(gt.QMS, bases):
        assert abs(gt.t_conductive(zb, qm) - gt.t_adiabat(zb)) < 1e-6
        assert 60e3 < zb < 250e3          # the observed range (ledger fischer:lithosphere)


def test_oceanic_geotherm_and_halfspace_flux():
    assert abs(gt.t_oceanic(0.0) - gt.T0) < 1e-12
    assert abs(gt.t_oceanic(250e3) - gt.t_adiabat(250e3)) < 1.0
    # surface flux of the half-space: numerical gradient vs k dT / sqrt(pi kappa t)
    t = 60e6 * gt.YEAR
    dt = 1300.0
    h = 1.0
    tz = lambda z: dt * math.erf(z / (2 * math.sqrt(gt.KAPPA * t)))
    assert abs(3.0 * (tz(h) - tz(0.0)) / h - gt.halfspace_surface_flux(dt, 60.0)) < 1e-6


def test_kelvin_age_and_perry():
    g = 0.02 * 5.0 / 9.0 / 0.3048          # 1/50 degF per foot in K/m
    age = gt.kelvin_age(g, 3900.0, 1.2e-6) / gt.YEAR / 1e6
    assert abs(age - 96.0) < 1.0             # England et al. (2007): 96 Ma
    # Perry: 6 (3) Ga for a 100 (50) km lid
    assert abs(gt.perry_time_constant(100e3) / gt.YEAR / 1e9 - 6.0) < 1.0
    assert abs(gt.perry_time_constant(50e3) / gt.YEAR / 1e9 - 3.0) < 0.5
    # Perry's ODE dTi/dt = -3 kappa Ti / (R L), integrated, decays with that constant
    tau = gt.perry_time_constant(100e3)
    ti, n, dt = 1.0, 10000, tau / 10000
    for _ in range(n):
        ti -= dt * ti / tau * (1 - 0.5 * dt / tau)   # second-order step
    assert abs(ti - math.exp(-1.0)) < 1e-4


def test_isotherms_deepen_as_root_age():
    # the half-space solution evaluated at the isotherm depth returns the isotherm
    for temp in (400.0, 800.0, 1200.0):
        for age in (1.0, 25.0, 100.0):
            z = gt.isotherm_depth(temp, age)
            t = age * 1e6 * gt.YEAR
            val = gt.T0 + (gt.T_M - gt.T0) * math.erf(z / (2 * math.sqrt(gt.KAPPA * t)))
            assert abs(val - temp) < 1e-6
        # depth proportional to the square root of age
        assert abs(gt.isotherm_depth(temp, 100.0) / gt.isotherm_depth(temp, 25.0) - 2.0) < 1e-9

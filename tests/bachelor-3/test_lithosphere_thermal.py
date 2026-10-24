"""Tests for the lithosphere thermal-model figdata scripts (Year 3, ch. 5)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import continental_geotherm as cg  # noqa: E402
import plate_cooling as pc  # noqa: E402


def test_half_space_solves_the_diffusion_equation():
    z = np.linspace(1e3, 80e3, 400)
    t, dt = 20.0, 1e-3
    tz = pc.hs_temperature(z, t)
    dTdt = (pc.hs_temperature(z, t + dt) - pc.hs_temperature(z, t - dt)) / (2 * dt * pc.MYR)
    d2 = np.gradient(np.gradient(tz, z), z)
    assert np.allclose(dTdt[5:-5], pc.KAPPA * d2[5:-5], rtol=2e-3, atol=1e-18)


def test_surface_heat_flow_is_the_gradient():
    for t in (5.0, 40.0):
        h = 1.0
        grad = (pc.hs_temperature(h, t) - pc.hs_temperature(0.0, t)) / h
        assert pc.K * grad == pytest.approx(pc.hs_heat(t), rel=1e-4)
        grad = (pc.plate_temperature(h, t) - pc.plate_temperature(0.0, t)) / h
        assert pc.K * grad == pytest.approx(pc.plate_heat(t), rel=1e-3)


def test_subsidence_is_the_isostatic_integral():
    z = np.linspace(0.0, 400e3, 40001)
    for t in (10.0, 40.0):
        deficit = np.trapezoid(pc.TM - pc.hs_temperature(z, t), z)
        w = pc.RHO_M * pc.ALPHA * deficit / (pc.RHO_M - pc.RHO_W)
        assert pc.DR + w == pytest.approx(float(pc.hs_depth(t)), rel=1e-4)
        zp = np.linspace(0.0, pc.L, 20001)
        deficit = np.trapezoid(pc.TM - pc.plate_temperature(zp, t), zp)
        w = pc.RHO_M * pc.ALPHA * deficit / (pc.RHO_M - pc.RHO_W)
        assert pc.DR + w == pytest.approx(float(pc.plate_depth(t)), rel=1e-3)


def test_plate_tends_to_half_space_young_and_to_steady_state_old():
    assert float(pc.plate_depth(2.0)) == pytest.approx(float(pc.hs_depth(2.0)), abs=1.0)
    z = np.linspace(0.0, pc.L, 50)
    assert np.allclose(pc.plate_temperature(z, 2000.0), pc.TM * z / pc.L, atol=1e-6)
    asym = pc.DR + pc.RHO_M * pc.ALPHA * pc.TM * pc.L / (2 * (pc.RHO_M - pc.RHO_W))
    assert float(pc.plate_depth(2000.0)) == pytest.approx(asym, rel=1e-9)


def test_binned_depths_deepen_with_young_age():
    bins = pc.read_bins()
    med = [b[1] for b in bins if b[0] < 45]
    assert all(b > a for a, b in zip(med[:-1], med[1:]))
    assert all(b[4] >= 20 for b in bins)


def test_continental_geotherm_balance():
    for q0 in cg.Q0S:
        h = 1.0
        assert cg.K * (cg.geotherm(h, q0) - cg.geotherm(0.0, q0)) / h == pytest.approx(q0, rel=1e-4)
        z = 50e3
        d2 = (cg.geotherm(z + 100, q0) - 2 * cg.geotherm(z, q0) + cg.geotherm(z - 100, q0)) / 100 ** 2
        a = cg.SHARE * q0 / cg.HR * np.exp(-z / cg.HR)
        assert cg.K * d2 == pytest.approx(-a, rel=1e-3)
        assert cg.heat_flow_at(1e6, q0) == pytest.approx(q0 * (1 - cg.SHARE))

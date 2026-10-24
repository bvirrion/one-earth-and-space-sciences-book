"""Tests for the mantle-convection figdata scripts (Year 3, ch. 6)."""
import math
import os
import sys

import numpy as np
import pytest
from scipy.optimize import minimize_scalar

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import convection_scaling as cs  # noqa: E402
import gia_relaxation as gr  # noqa: E402
import plate_cooling as pc  # noqa: E402
import ridge_push as rp  # noqa: E402


def test_critical_rayleigh_number_is_the_minimum_of_the_marginal_curve():
    res = minimize_scalar(cs.critical_function, bounds=(0.5, 6.0), method="bounded",
                          options={"xatol": 1e-10})
    assert res.fun == pytest.approx(cs.RAC, rel=1e-9)
    assert res.x == pytest.approx(math.pi / math.sqrt(2), rel=1e-5)
    assert cs.RAC == pytest.approx(657.511, abs=1e-3)


def test_boundary_layer_is_marginally_stable_and_carries_the_heat():
    for ra in (1e5, 1e7, 1e9):
        d = cs.D_MANTLE
        dl = float(cs.delta(ra))
        # local Rayleigh number of the layer, with dT/2 across a thickness delta
        assert ra * (dl / d) ** 3 / 2 == pytest.approx(cs.RAC, rel=1e-12)
        # conductive flux through the layer, in units of the conductive k dT / d
        assert (0.5 / dl) * d == pytest.approx(float(cs.nusselt(ra)), rel=1e-12)
        # velocity scale: the time to cross the cell equals the growth time of the layer
        u = float(cs.velocity(ra))
        assert d / u == pytest.approx(dl ** 2 / cs.KAPPA, rel=1e-12)


def test_prem_integration_gives_the_surface_gravity_and_mantle_values():
    assert cs.gravity(0.0) == pytest.approx(9.82, abs=0.02)
    assert 9.9 < cs.gravity(1500e3) < 10.4
    assert 4.3e3 < cs.mantle_mean_density() < 4.6e3
    assert cs.mantle_rayleigh(1e21) == pytest.approx(10 * cs.mantle_rayleigh(1e22))


def test_relaxing_half_space_satisfies_stokes_and_the_surface_conditions():
    eta, lam, wm = 1e21, 1000e3, 100.0
    h = 50.0
    x = np.linspace(0.0, lam, 7)[1:-1]
    for z in (h, 100e3, 400e3):
        u, v, p = gr.flow(x, z, wm, eta, lam)
        ux = (gr.flow(x + h, z, wm, eta, lam)[0] - gr.flow(x - h, z, wm, eta, lam)[0]) / (2 * h)
        vz = (gr.flow(x, z + h, wm, eta, lam)[1] - gr.flow(x, z - h, wm, eta, lam)[1]) / (2 * h)
        assert np.allclose(ux + vz, 0.0, atol=1e-6 * np.max(np.abs(v)) / lam)

        def lap(i):
            f0 = gr.flow(x, z, wm, eta, lam)[i]
            return ((gr.flow(x + h, z, wm, eta, lam)[i] - 2 * f0 + gr.flow(x - h, z, wm, eta, lam)[i])
                    + (gr.flow(x, z + h, wm, eta, lam)[i] - 2 * f0 + gr.flow(x, z - h, wm, eta, lam)[i])) / h ** 2
        px = (gr.flow(x + h, z, wm, eta, lam)[2] - gr.flow(x - h, z, wm, eta, lam)[2]) / (2 * h)
        pz = (gr.flow(x, z + h, wm, eta, lam)[2] - gr.flow(x, z - h, wm, eta, lam)[2]) / (2 * h)
        assert np.allclose(px, eta * lap(0), rtol=1e-4, atol=1e-6 * np.max(np.abs(px)))
        assert np.allclose(pz, eta * lap(1), rtol=1e-4, atol=1e-6 * np.max(np.abs(pz)))
    # surface: no shear stress, and the pressure perturbation is -rho g w
    x = np.linspace(0.0, lam, 9)
    uz = (gr.flow(x, h, wm, eta, lam)[0] - gr.flow(x, 0.0, wm, eta, lam)[0]) / h
    vx = (gr.flow(x + h, 0.0, wm, eta, lam)[1] - gr.flow(x - h, 0.0, wm, eta, lam)[1]) / (2 * h)
    assert np.allclose(uz + vx, 0.0, atol=1e-3 * np.max(np.abs(vx)))
    w = wm * np.cos(2 * math.pi * x / lam)
    assert np.allclose(gr.flow(x, 0.0, wm, eta, lam)[2], -gr.RHO * gr.G * w)
    # and the surface velocity is -w / tau: exponential relaxation
    assert np.allclose(gr.flow(x, 0.0, wm, eta, lam)[1], -w / gr.tau(eta, lam))
    assert gr.viscosity(gr.tau(eta, lam), lam) == pytest.approx(eta)


def test_ridge_push_integral_matches_the_closed_form_and_saturates():
    for t in (10.0, 100.0):
        f, dp = rp.numeric_force(lambda z: pc.hs_temperature(z, t), 1500e3, 200001)
        assert f == pytest.approx(float(rp.hs_force(t)), rel=1e-6)
        assert abs(dp) < 1.0
    # young plate = half-space; old plate levels off
    assert rp.plate_force(5.0) == pytest.approx(float(rp.hs_force(5.0)), rel=1e-4)
    assert rp.plate_force(160.0) - rp.plate_force(120.0) < 0.05 * rp.plate_force(160.0)
    assert 3e12 < float(rp.hs_force(100.0)) < 4.5e12

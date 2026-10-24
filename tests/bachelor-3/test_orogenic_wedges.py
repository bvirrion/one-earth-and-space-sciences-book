"""Tests for the critical-taper and age--elevation figdata scripts (Year 3, ch. 10)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import age_elevation as ae  # noqa: E402
import critical_taper as ct  # noqa: E402


def test_k_factor_is_the_coulomb_stress_ratio():
    for mu in (0.6, 0.85, 1.03):
        r = 1.0 + ct.k_factor(mu)              # sigma1' / sigma3'
        # on the plane at 45 - phi/2 from sigma1 (sigma3' = 1), tau = mu sigma_n exactly
        phi = math.atan(mu)
        t = math.pi / 4.0 - phi / 2.0
        sn = r * math.sin(t) ** 2 + math.cos(t) ** 2
        tau = (r - 1.0) * math.sin(t) * math.cos(t)
        assert tau == pytest.approx(mu * sn)


def test_taper_satisfies_the_slice_force_balance():
    # (1 + K (1 - lam)) (alpha + beta) = beta + mu_b (1 - lam_b), radians
    for lam in ct.LAMBDAS:
        for b in (0.0, 4.0, 10.0):
            t = math.radians(ct.taper(b, lam=lam))
            lhs = (1.0 + ct.k_factor(ct.MU) * (1.0 - lam)) * t
            assert lhs == pytest.approx(math.radians(b) + ct.MU_B * (1.0 - lam))
    # more fluid pressure, smaller taper; the dry-sand limit
    a = [ct.alpha(5.0, lam=l) for l in (0.0, 0.4, 0.7, 0.9)]
    assert all(np.diff(a) < 0)
    assert ct.taper(0.0, mu=0.6, mu_b=0.3, lam=0.0) == pytest.approx(
        math.degrees(0.3 * (1 - math.sin(math.atan(0.6))) / (1 + math.sin(math.atan(0.6)))))


def test_lambda_inversion_and_flat_surface():
    for lam in (0.3, 0.6, 0.85):
        for b in (2.0, 6.0):
            assert ct.lambda_from_taper(ct.alpha(b, lam=lam), b) == pytest.approx(lam)
    for lam in ct.LAMBDAS:
        assert ct.alpha(ct.beta_flat(lam=lam), lam=lam) == pytest.approx(0.0, abs=1e-9)


def test_steady_geotherm_solves_advection_diffusion():
    for v in ae.RATES:
        dz = 1e-3
        for z in (0.5, 3.0, 12.0):
            t2 = (ae.geotherm(z + dz, v) - 2 * ae.geotherm(z, v) + ae.geotherm(z - dz, v)) / dz ** 2
            t1 = (ae.geotherm(z + dz, v) - ae.geotherm(z - dz, v)) / (2 * dz)
            assert ae.KAPPA * t2 == pytest.approx(-v * t1, rel=1e-4)   # -v dT/dz = kappa T''
        assert float(ae.geotherm(0.0, v)) == pytest.approx(ae.TS)
        assert float(ae.geotherm(ae.L, v)) == pytest.approx(ae.TL)
        assert float(ae.geotherm(ae.closure_depth(v), v)) == pytest.approx(ae.TC)
        slope = float((ae.geotherm(1.001, v) - ae.geotherm(0.999, v)) / 0.002)
        assert ae.gradient(1.0, v) == pytest.approx(slope, rel=1e-5)
    # without erosion the geotherm is the 30 C/km line
    assert ae.closure_depth(0.0) == pytest.approx((ae.TC - ae.TS) / ae.GRAD)


def test_perturbation_solves_the_2d_equation_and_surface_condition():
    v = 1.0
    x, z, d = 3.7, 0.8, 1e-3
    f = lambda xx, zz: float(ae.perturbation(xx, zz, v))  # noqa: E731
    lap = ((f(x + d, z) - 2 * f(x, z) + f(x - d, z)) + (f(x, z + d) - 2 * f(x, z) + f(x, z - d))) / d ** 2
    dz = (f(x, z + d) - f(x, z - d)) / (2 * d)
    assert ae.KAPPA * lap == pytest.approx(-v * dz, rel=1e-4)
    # first-order surface condition: T0(-h) + theta(x, 0) = TS - GAMMA h
    for xx in (0.0, 4.0, 10.0):
        h = ae.H0 * math.cos(2 * math.pi * xx / ae.WAVELENGTH)
        t_surf = ae.TS - ae.gradient(0.0, v) * h + f(xx, 0.0)
        assert t_surf == pytest.approx(ae.TS - ae.GAMMA * h)


def test_age_elevation_slope_and_limits():
    for v in ae.RATES:
        a = ae.age(np.array([-0.5, 0.5]), v)
        assert 1.0 / (a[1] - a[0]) == pytest.approx(ae.apparent_rate(v))
        assert ae.apparent_rate(v) > v
        assert np.all(ae.age(np.linspace(-ae.H0, ae.H0, 21), v) > 0)
    # short wavelengths: flat isotherm, the slope is the true rate
    assert ae.deflection(1.0, wavelength=0.5) < 1e-6
    # long wavelengths, slow erosion: the isotherm follows the topography
    assert ae.deflection(1e-6, wavelength=1e5) == pytest.approx(1.0 - ae.GAMMA / ae.GRAD, rel=1e-3)


def test_fault_bend_fold_conserves_area_and_thickness():
    import fault_bend as fb
    # every point moves the slip distance, along the fault where it lies on it
    q = fb.advect((1.0, 0.0), 6.0)
    assert q[1] == pytest.approx(fb.RAMP_H, abs=1e-6)
    # a bed above the upper flat: excess area above its regional = slip x ramp height,
    # the same for every such bed (the slip carries material on out along the upper flat)
    for y0 in (1.3, 1.6):
        pts = np.array(fb.bed_after(y0, n=1201))
        area = float(np.sum(0.5 * (pts[1:, 1] + pts[:-1, 1] - 2 * y0) * np.diff(pts[:, 0])))
        assert area == pytest.approx(fb.SLIP * fb.RAMP_H, rel=5e-3)
        assert pts[:, 1].max() - y0 == pytest.approx(fb.RAMP_H, abs=1e-6)
    # back limb parallel to the ramp, bed thickness kept
    t = math.radians(fb.THETA)
    a = fb.advect((2.0, 1.3), 2.5)
    b = fb.advect((2.0, 1.6), 2.5)
    ramp = np.array([math.cos(t), math.sin(t)])
    normal = np.array([-math.sin(t), math.cos(t)])
    assert fb.domain(a) == 1 and fb.domain(b) == 1
    assert float(np.dot(b - a, normal)) == pytest.approx(0.3, abs=1e-3)   # step 0.002

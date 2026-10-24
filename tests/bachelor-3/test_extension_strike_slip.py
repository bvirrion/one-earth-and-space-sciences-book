"""Tests for the domino-extension and lock-up figdata script (Year 3, ch. 9)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import domino_extension as de  # noqa: E402
import rollover as ro  # noqa: E402


def test_beta_matches_explicit_rigid_blocks():
    for t0 in de.THETA0:
        w0 = de.domino_width(t0, t0)
        for t in (t0 - 5.0, 30.0, 15.0):
            assert de.domino_width(t0, t) / w0 == pytest.approx(de.beta(t0, t))
    assert math.isnan(de.beta(45.0, 50.0))
    assert de.beta(60.0, 60.0) == pytest.approx(1.0)


def test_stress_ratio_is_the_coulomb_friction_condition():
    for mu in de.MUS:
        for dip in (40.0, 55.0, 70.0, 80.0):
            r = de.stress_ratio(dip, mu)
            if math.isnan(r):
                continue
            t = math.radians(90.0 - dip)        # angle between the plane and sigma1
            s1, s3 = r, 1.0
            sn = s1 * math.sin(t) ** 2 + s3 * math.cos(t) ** 2
            tau = (s1 - s3) * math.sin(t) * math.cos(t)
            assert tau == pytest.approx(mu * sn)


def test_optimum_and_lockup():
    for mu in de.MUS:
        dips = np.arange(de.lockup_dip(mu) + 0.01, 89.99, 0.01)
        r = np.array([de.stress_ratio(x, mu) for x in dips])
        i = int(np.nanargmin(r))
        assert dips[i] == pytest.approx(de.optimal_dip(mu), abs=0.02)
        assert r[i] == pytest.approx(de.min_ratio(mu), rel=1e-6)
        # just above the lock-up dip the ratio diverges; at or below it, no slip
        assert de.stress_ratio(de.lockup_dip(mu) + 0.01, mu) > 1e3
        assert math.isnan(de.stress_ratio(de.lockup_dip(mu) - 0.5, mu))
    # Anderson's 60 deg normal fault is near optimal for mu = 0.6
    assert de.optimal_dip(0.6) == pytest.approx(60.5, abs=0.1)


def test_listric_fault_and_depth_to_detachment():
    # the fault dips DIP0 at the surface and flattens at D
    eps = 1e-6
    assert (ro.fault(eps) - ro.fault(0.0)) / eps == pytest.approx(math.tan(math.radians(ro.DIP0)), rel=1e-4)
    assert float(ro.fault(200.0)) == pytest.approx(ro.D)
    assert ro.fault_x(2.0) == pytest.approx(float(np.interp(2.0, ro.fault(np.linspace(0, 30, 300001)),
                                                            np.linspace(0, 30, 300001))), abs=1e-4)
    # area balance: sag below a bed's original level = heave x height above the detachment
    for h in (1.0, 2.0, 3.2):
        for z0 in (0.0, 1.0, 2.5):
            assert ro.sag_area(z0, h) == pytest.approx(h * (ro.D - z0), rel=2e-3)
    # the rollover: the displaced top dips towards the fault (subsidence decreases away from it)
    xs = np.linspace(ro.H, 20.0, 200)
    s = ro.displaced_bed(xs, 0.0)
    assert np.all(np.diff(s) < 0)

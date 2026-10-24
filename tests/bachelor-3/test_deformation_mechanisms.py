"""Tests for the flow-law figdata script (Year 3, ch. 7)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import flow_laws as fl  # noqa: E402


def test_stress_inverts_the_rate():
    for law, t, p, d in ((fl.QTZ, 723.15, 0.0, 1.0), (fl.OL_DIS, 1373.15, 1e9, 1.0), (fl.OL_DIF, 1473.15, 2e9, 300.0)):
        s = fl.stress(law, 1e-14, t, p, d)
        assert float(fl.rate(law, s, t, p, d)) == pytest.approx(1e-14, rel=1e-10)


def test_log_log_slope_is_the_stress_exponent():
    for law in (fl.QTZ, fl.OL_DIS, fl.OL_DIF):
        r1, r2 = fl.rate(law, 10.0, 1200.0, 0.0, 100.0), fl.rate(law, 100.0, 1200.0, 0.0, 100.0)
        assert math.log10(r2 / r1) == pytest.approx(law["n"])
    # and the grain-size exponent of diffusion creep
    r1, r2 = fl.rate(fl.OL_DIF, 1.0, 1400.0, 0.0, 10.0), fl.rate(fl.OL_DIF, 1.0, 1400.0, 0.0, 100.0)
    assert math.log10(r1 / r2) == pytest.approx(3.0)


def test_mechanism_boundary_and_contours():
    for d in (30.0, 300.0, 3000.0):
        s = fl.boundary_stress(d)
        assert float(fl.rate(fl.OL_DIS, s, fl.MAP_T, fl.MAP_P)) == pytest.approx(
            float(fl.rate(fl.OL_DIF, s, fl.MAP_T, fl.MAP_P, d)), rel=1e-9)
        for e in (1e-16, 1e-12):
            assert float(fl.total_rate(fl.stress_for_total(e, d), d)) == pytest.approx(e, rel=1e-9)
    # the boundary falls with grain size as d^(-m/(n_dis - n_dif)) = d^(-1.2)
    assert math.log10(fl.boundary_stress(10.0) / fl.boundary_stress(1000.0)) == pytest.approx(2 * 3 / 2.5)


def test_piezometer_round_trip_and_calibration_range():
    for s in (34.0, 100.0, 268.0):
        assert fl.piezometer_stress(fl.piezometer_grain_size(s)) == pytest.approx(s)
    # the calibration's end points: about 46 um at 34 MPa and 3.2 um at 268 MPa
    assert fl.piezometer_grain_size(34.0) == pytest.approx(46, rel=0.15)
    assert fl.piezometer_grain_size(268.0) == pytest.approx(3.2, rel=0.15)


def test_quartz_weakens_steeply_with_temperature():
    s = [fl.stress(fl.QTZ, 1e-14, t + 273.15) for t in (300, 400, 500, 600)]
    assert all(a > 2 * b for a, b in zip(s[:-1], s[1:]))
    assert np.isclose(s[1], 65.4, rtol=1e-3)

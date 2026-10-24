"""Tests for the deep-time climate figure data (figdata/bachelor-2/deeptime.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import deeptime as dt  # noqa: E402


def test_steady_state_and_its_warming():
    # no excess: weathering equals the base flux and there is no warming
    assert dt.warming(0.0) == 0.0
    assert dt.weathering(0.0) == pytest.approx(dt.W0)
    # the steady warming depends on the outgassing and k only, not on S or f
    for s in (2.0, 3.0, 8.0):
        m = dt.steady_excess(1.2, s=s)
        assert dt.weathering(m, s=s) == pytest.approx(1.2 * dt.W0, rel=1e-12)
        assert dt.warming(m, s=s) == pytest.approx(math.log(1.2) / dt.KT, rel=1e-12)
    assert dt.steady_warming(1.2) == pytest.approx(2.026, abs=0.001)


def test_linearised_time_matches_the_slope_of_the_weathering():
    h = 1e-3
    slope = (dt.weathering(h) - dt.weathering(-h)) / (2 * h)
    assert dt.tau() == pytest.approx(1.0 / slope, rel=1e-6)
    assert dt.tau() / 1e3 == pytest.approx(137.3, abs=0.1)
    assert dt.tau(k=dt.K_RUN) / 1e3 == pytest.approx(103.6, abs=0.1)
    # about a new steady state the slope is that of the full model there
    m = dt.steady_excess(1.2)
    slope = (dt.weathering(m + h) - dt.weathering(m - h)) / (2 * h)
    c = 1 + dt.F_AIR * m / dt.A0
    assert dt.tau(c_ratio=c, w=1.2 * dt.W0) == pytest.approx(1.0 / slope, rel=1e-6)


def test_small_pulse_decays_like_the_linear_model():
    m0 = 1.0
    t1 = dt.tau()
    out = dt.integrate(m0, 1.0, t1, dt=100.0)
    assert out[-1][1] == pytest.approx(m0 / math.e, rel=1e-3)


def test_big_pulse_is_removed_more_slowly_than_the_linear_model():
    t_nl = dt.time_to_fraction(dt.PULSE, 0.1)
    t_lin = dt.tau() * math.log(10.0)
    assert t_nl > t_lin
    assert t_nl / 1e3 == pytest.approx(339.9, abs=0.5)
    # the integration conserves the mass balance: rate integrated equals the change
    out = dt.integrate(dt.PULSE, 1.0, 2.0e4, dt=50.0)
    removed = sum((dt.weathering(m) - dt.W0) * 50.0 for _, m in out[:-1])
    assert dt.PULSE - out[-1][1] == pytest.approx(removed, rel=5e-3)


def test_data_tables_have_the_known_values():
    ceno = dt.read_csv("bachelor-2-cenogrid.csv")
    d = {round(r["age_Ma"], 2): r for r in ceno}
    assert d[0.05]["d18O"] == pytest.approx(4.619)
    assert d[50.05]["d18O"] == pytest.approx(-0.471)
    petm = dt.read_csv("bachelor-2-cenogrid-petm.csv")
    low = min(petm, key=lambda r: r["d13C"])
    assert low["age_Ma"] == pytest.approx(55.835)
    co2 = dt.read_csv("bachelor-2-foster2017.csv")
    assert co2[0]["co2"] == pytest.approx(276.0)
    assert max(r["co2"] for r in co2) == pytest.approx(2165.3)
    assert all(r["lo68"] > 0 for r in co2)

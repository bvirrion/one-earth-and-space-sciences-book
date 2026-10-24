import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import oil_window as ow  # noqa: E402


def test_source_rock_enters_the_window_when_it_passes_60_degC():
    t, sense = ow.crossings(ow.OIL_TOP)[0]
    assert sense == 1
    assert ow.source_temperature(t) == pytest.approx(60.0, abs=1e-9)
    assert ow.source_temperature(t + 0.5) < 60.0 < ow.source_temperature(t - 0.5)


def test_source_rock_leaves_the_oil_window_into_the_gas_window():
    t, sense = ow.crossings(ow.OIL_BASE)[0]
    assert sense == 1 and t < ow.crossings(ow.OIL_TOP)[0][0]
    assert ow.source_temperature(t) == pytest.approx(120.0, abs=1e-9)
    assert ow.source_temperature(0.0) > 120.0          # still in the gas window today


def test_window_depth_is_linear_in_the_inverse_geotherm():
    for g in (20.0, 30.0, 40.0):
        top, base = ow.window_depths(g)
        assert top * g == pytest.approx(40.0) and base * g == pytest.approx(100.0)
    assert ow.window_depths(30.0) == pytest.approx((4 / 3, 10 / 3))


def test_depth_today_is_the_sum_of_the_episodes():
    assert ow.depth(ow.SOURCE_AGE, 0.0) == pytest.approx(sum(h for _, _, h in ow.EPISODES) / 1000)
    assert ow.depth(ow.SOURCE_AGE, ow.SOURCE_AGE) == 0.0
    assert ow.depth(95.0, 100.0) is None


def test_horizons_stay_in_order_and_erosion_lifts_them():
    for t in range(0, 95):
        zs = [ow.depth(h, t) for h in ow.HORIZONS if h >= t]
        assert zs == sorted(zs, reverse=True)
    assert ow.depth(ow.SOURCE_AGE, 0.0) < ow.depth(ow.SOURCE_AGE, 20.0)
    for h in ow.HORIZONS:                               # erosion never reaches a plotted horizon
        assert min(ow.depth(h, t / 2) for t in range(0, int(2 * h) + 1)) >= 0.0


def test_named_numbers():
    n = ow.numbers()
    assert n["enter_oil_Ma"] == pytest.approx(117.0, abs=0.05)
    assert n["leave_oil_Ma"] == pytest.approx(51.24, abs=0.05)
    assert n["T_max"] == pytest.approx(140.0)


def test_a_hotter_basin_makes_oil_earlier_and_before_the_trap():
    n = ow.numbers()
    assert n["enter_oil_G40_Ma"] > n["enter_oil_Ma"]
    assert n["leave_oil_G40_Ma"] > ow.TRAP_AGE > n["leave_oil_Ma"]
    assert ow.source_temperature(n["enter_oil_G40_Ma"], g=40.0) == pytest.approx(60.0)

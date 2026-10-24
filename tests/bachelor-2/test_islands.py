"""Tests for the oceanic-islands figure data (figdata/bachelor-2/islands.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import islands  # noqa: E402


def test_depth_age_law_is_continuous_and_matches_its_sources():
    # Parsons and Sclater: 2500 m at the ridge, 350 t^1/2 below it
    assert islands.depth(0.0) == pytest.approx(2500.0)
    assert islands.depth(16.0) == pytest.approx(2500.0 + 350.0 * 4.0)
    # the switch lies where the two branches meet, so the floor never jumps
    t = islands.T_SW
    assert 20.0 < t < 30.0
    assert islands.depth_root(t) == pytest.approx(islands.depth_exp(t), abs=1e-6)
    for a, b in ((t - 1e-6, t + 1e-6), (t - 0.5, t + 0.5)):
        assert abs(islands.depth(b) - islands.depth(a)) < 50.0
    # the floor deepens with age everywhere
    ds = [islands.depth(0.5 * i) for i in range(1, 400)]
    assert all(y > x for x, y in zip(ds, ds[1:]))


def test_rate_is_the_derivative_of_depth():
    for t in (2.0, 10.0, 25.0, 40.0, 100.0, 150.0):
        h = 1e-4
        num = (islands.depth(t + h) - islands.depth(t - h)) / (2 * h)
        assert islands.rate(t) == pytest.approx(num, rel=1e-5)
    # the rate along an old ridge is about 0.01 m/kyr (Clague and Sherrod) on a plate ~100 Myr old
    assert islands.rate(100.0) == pytest.approx(10.37, abs=0.01)
    assert islands.age_for_rate(10.0) == pytest.approx(102.3, abs=0.1)
    assert islands.rate(islands.age_for_rate(10.0)) == pytest.approx(10.0)


def test_sinking_is_fastest_on_a_young_plate():
    for dt in (5.0, 20.0, 60.0):
        s = [islands.sink(t0, dt) for t0 in (2.0, 10.0, 30.0, 60.0)]
        assert all(b < a for a, b in zip(s, s[1:]))
    assert islands.sink_root(0.0, 25.0) == pytest.approx(1750.0)


def test_the_invented_island_and_the_drilled_atolls():
    n = islands.numbers()
    assert n["petrel_floor"] == pytest.approx(3606.8, abs=0.05)
    assert n["petrel_sink"] + n["petrel_erosion"] == pytest.approx(1000.0, abs=0.1)
    # the summit reaches sea level when stated, and the reef cap then equals the sinking
    assert islands.petrel_summit(islands.PETREL_GONE) == pytest.approx(0.0, abs=1e-9)
    assert -islands.petrel_summit(70.0) == pytest.approx(n["petrel_cap"], abs=0.05)
    assert n["petrel_cap"] == pytest.approx(350.0 * (math.sqrt(70) - math.sqrt(22)), abs=0.05)
    assert n["petrel_guyot_sink"] > 0
    # feet to metres; E-1 met basalt at 4,158 ft, F-1 hard basement at 4,610 ft
    assert n["basalt_E_1"] == pytest.approx(1267.4, abs=0.05)
    assert n["basalt_F_1"] - n["basalt_E_1"] == pytest.approx(452 * 0.3048, abs=0.1)

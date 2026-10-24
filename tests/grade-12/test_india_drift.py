import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import india_drift as idr  # noqa: E402


def test_both_reconstructions_start_from_today():
    d = idr.load()
    for m in idr.MODELS:
        assert d[m][0] == pytest.approx((20.0, 29.65), abs=1e-6)
        assert len(d[m]) == 22


def test_india_moved_north_fast_before_the_collision_and_slowly_after():
    n = idr.numbers()
    assert 110 < n["speed_65_50"] < 150          # mm/yr, more than 10 cm a year
    assert 35 < n["speed_40_0"] < 45
    assert n["slowdown_ratio"] < 0.5             # less than half
    for m in idr.MODELS:
        sp = idr.steps(idr.load()[m])
        before = [v for a, b, v in sp if 50 <= a < 65]
        after = [v for a, b, v in sp if b <= 40]
        assert min(before) > 2 * max(after)


def test_distance_north_since_the_end_of_the_cretaceous():
    n = idr.numbers()
    assert n["north_since_66_km"] == pytest.approx(4379, abs=1)
    assert abs(n["north_since_66_km"] - n["north_since_66_km_m19"]) < 200    # the two models agree within 200 km
    assert n["north_since_66_km"] == pytest.approx((20.0 - n["india_lat_66"]) * 111.195, rel=1e-4)


def test_convergence_with_lhasa_and_today():
    n = idr.numbers()
    assert n["converge_since_50_km"] == pytest.approx(n["india_north_since_50_km"] - n["lhasa_north_since_50_km"])
    assert 1300 < n["converge_since_50_km"] < 1400
    assert n["today_in_eu_speed"] == pytest.approx(45.0, abs=0.1)        # grade 11, plate-motions
    assert n["india_lhasa_last5_mm"] < n["today_in_eu_north"]

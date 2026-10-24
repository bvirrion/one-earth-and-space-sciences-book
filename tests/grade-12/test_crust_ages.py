import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import crust_ages as ca  # noqa: E402


def test_histogram_sums_to_one_and_stops_before_200_myr():
    h = ca.histogram()
    assert sum(s for _, _, s in h) == pytest.approx(1.0)
    assert h[-1][2] < 0.001                    # almost nothing in 190-200 Myr
    assert ca.numbers()["oldest_open_myr"] < 200.0


def test_agrees_with_grade_11():
    import seafloor_age as sa
    n = sa.numbers()
    assert ca.numbers()["oldest_open_myr"] == pytest.approx(n["oldest_open_myr"])
    assert ca.share_younger(100.0) == pytest.approx(n["share_younger_100"], abs=0.01)


def test_young_floor_dominates():
    h = ca.histogram()
    first_half = sum(s for lo, _, s in h if lo < 100)
    assert first_half > 0.7
    assert ca.numbers()["rock_over_floor"] > 20

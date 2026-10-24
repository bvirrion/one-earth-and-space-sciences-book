"""figdata/grade-11/hypsometry.py: two levels on the Earth's surface."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import hypsometry as hy  # noqa: E402

N = hy.numbers()


def test_land_fraction_near_29_percent():
    assert 0.27 < N["land_fraction"] < 0.31


def test_two_modes_one_on_land_one_on_the_deep_sea_floor():
    (lm, ls), (sm, ss) = hy.modes()
    assert 0 < lm < 1000
    assert -5500 < sm < -3500
    # the bins between them are much lower than either peak
    mid = [h for h in hy.histogram() if -2500 <= h[2] <= -1000]
    assert all(h[3] < 0.3 * min(ls, ss) for h in mid)


def test_bins_add_up_to_the_whole_surface():
    assert abs(sum(h[3] for h in hy.histogram()) - 100.0) < 1e-6


def test_tibet_box_stands_about_five_km_high():
    assert 4700 < N["tibet_mean_m"] < 5300


def test_curve_is_decreasing_from_the_highest_to_the_deepest():
    c = hy.curve()
    assert all(b[1] <= a[1] for a, b in zip(c[:-1], c[1:]))
    assert abs(c[-1][0] - 100.0) < 1e-6

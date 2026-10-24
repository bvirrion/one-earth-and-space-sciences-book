import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import alpine_belt as ab  # noqa: E402


def test_only_shallow_earthquakes_inside_the_window():
    qs = list(ab.quakes())
    assert len(qs) > 100
    assert all(ab.inside(lo, la) and m >= 6.0 for lo, la, m in qs)


def test_the_tibetan_plateau_box_stands_high():
    n = ab.numbers()
    assert n["tibet_box_mean_m"] > 4000
    assert n["n_higher"] < n["n_high"] + n["n_higher"]

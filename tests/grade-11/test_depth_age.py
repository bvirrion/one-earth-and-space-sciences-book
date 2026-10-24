"""figdata/grade-11/depth_age.py: ocean depth against age, ETOPO1 and the age grid."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import depth_age as da  # noqa: E402


def test_published_law_values():
    assert da.ps_sqrt(0) == 2500 and abs(da.ps_sqrt(64) - 5300) < 1e-9
    assert abs(da.ps_exp(64) - 5245) < 1
    # the two forms agree within about 100 m where both hold (20-70 Myr)
    for t in (30, 50, 70):
        assert abs(da.ps_sqrt(t) - da.ps_exp(t)) < 150


def test_fit_recovers_a_square_root_law():
    bs = [(t, 2500 + 350 * math.sqrt(t), 0, 0, 100) for t in (1, 4, 9, 25, 49)]
    a, b = da.fit_sqrt(bs)
    assert abs(a - 2500) < 1e-6 and abs(b - 350) < 1e-6


def test_floor_deepens_with_age_while_young():
    bs = da.bins()
    young = [d for t, d, _, _, _ in bs if t < 50]
    assert all(b > a for a, b in zip(young, young[1:]))


def test_young_floor_matches_the_law_old_floor_is_shallower():
    bs = da.bins()
    for t, d, _, _, _ in bs:
        if t < 10:
            assert abs(d - da.ps_sqrt(t)) < 150
        if 40 < t < 70:
            assert d < da.ps_sqrt(t) - 200            # sediments and volcanoes: shallower


def test_square_root_fit_of_the_data():
    a, b = da.fit_sqrt(da.bins())
    assert 2500 < a < 2900 and 200 < b < 350

"""figdata/grade-6/granite_mosaic.py: the drawn granite used by exercise 7."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-6"))
import granite_mosaic as gm  # noqa: E402


def test_mosaic_tiles_the_box():
    s, tot = gm.summary()
    assert abs(tot - gm.W * gm.H) < 1e-9


def test_counts_quoted_in_exercise_7():
    s, _ = gm.summary()
    n = {m: k for m, k, _ in s}
    assert n == {"feldspar": 33, "quartz": 21, "mica": 6}
    assert round(100 * n["quartz"] / gm.N) == 35

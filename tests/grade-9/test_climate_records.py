"""Tests for figdata/grade-9/climate_records.py (grade 9, chapter 1)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-9"))
import climate_records as cr  # noqa: E402


def test_greenhouse_temperatures():
    assert math.isclose(cr.kelvin_to_celsius(cr.T_BB_K), -19.15)
    assert round(cr.kelvin_to_celsius(cr.T_SURF_K)) == 15
    assert cr.T_SURF_K - cr.T_BB_K == 34


def test_gistemp_is_complete_and_decades_warm():
    t = cr.gistemp()
    assert sorted(t) == list(range(1880, cr.LAST + 1))
    d = cr.decades()
    assert len(d) == 15 and d[0][0] == "1880s" and d[-1][1] == 2020
    # the last five decades each warmer than the one before
    means = [m for _l, _s, m in d]
    assert all(b > a for a, b in zip(means[-6:], means[-5:]))
    assert max(t, key=t.get) == 2024


def test_problem_warming():
    w = cr.warming(1880, 1899, 2015, 2024)
    assert math.isclose(w, 1.21, abs_tol=0.01)
    # the same function on two equal periods gives zero
    assert cr.warming(1950, 1959, 1950, 1959) == 0


def test_co2_records():
    c = cr.co2()
    assert c[1959] < 320 and c[2025] > 425
    assert all(c[y + 1] > c[y] for y in range(1959, 2025))     # it rose every year
    lo, hi = cr.preindustrial_co2_range()
    assert 170 < lo < 180 and 295 < hi < 300
    assert c[2025] > hi + 100                                   # far above 800 000 years of ice


def test_icecore_binning():
    ice = cr.icecore_co2()
    assert ice[0][0] == 1.0 and 790 < ice[-1][0] < 800
    assert all(b[0] - a[0] >= 1.99 for a, b in zip(ice, ice[1:]))
    rows = [{"x": "100", "y": "1"}, {"x": "1500", "y": "3"}, {"x": "2500", "y": "10"}]
    assert cr.binned(rows, "x", "y") == [(1.0, 2.0), (3.0, 10.0)]


def test_sea_level_rate():
    a, _b = cr.sea_level_rate()
    assert 2.8 < a < 3.6                                        # mm per year
    sl = cr.sea_level_yearly()
    assert sl[0][0] == 1993 and sl[-1][0] == 2024

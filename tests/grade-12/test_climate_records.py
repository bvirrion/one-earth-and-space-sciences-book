"""figdata/grade-12/climate_records.py: the records say what the chapter says."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import climate_records as cr  # noqa: E402


def test_keeling_curve():
    n = cr.numbers()
    assert n["season_max_month"] == 5 and n["season_min_month"] in (9, 10)   # May peak, autumn low
    assert 5 < n["season_amplitude"] < 8
    assert n["rate_2015_2025"] > 2 * n["rate_1960s"]                         # the rise is accelerating
    assert n["co2_last_year"] == 2025 and 420 < n["co2_last"] < 435


def test_ice_cores_bracket_today():
    lo, hi = cr.icecore_range()
    assert 170 < lo < 180 and 290 < hi < 305
    assert cr.numbers()["co2_last"] > hi + 100


def test_temperature_and_sea_level():
    n = cr.numbers()
    assert n["warmest_year"] >= 2023
    assert 0.95 < n["warming_2011_2020_vs_1880_1900"] < 1.3                 # cf. AR6 1.09 vs 1850-1900
    assert 2.8 < n["sea_trend_mm_a"] < 3.6
    rm = cr.running_mean([1.0] * 20)
    assert math.isnan(rm[0]) and rm[10] == 1.0

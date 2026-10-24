"""Tests for figdata/grade-9/concentration.py (grade 9, chapter 3)."""
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "grade-9"))
import concentration as cn  # noqa: E402


def test_factors_match_the_published_tables():
    f = {m: x for m, _c, _o, x in cn.factors()}
    assert 3.5 < f["aluminium"] < 4.5 and 3.5 < f["iron"] < 4.5      # "4" in the table
    assert 80 <= f["copper"] <= 85                                    # "80"
    assert 560 < f["zinc"] < 580                                      # "570"
    assert abs(f["tin"] - 2500) < 1 and abs(f["gold"] - 2000) < 1e-6
    assert 2900 < f["chromium"] <= 3000                               # "2,940"


def test_rare_metals_need_more_concentration():
    f = {m: (c, x) for m, c, _o, x in cn.factors()}
    assert f["copper"][1] > 10 * f["iron"][1]
    assert f["gold"][0] < f["copper"][0] and f["gold"][1] > f["copper"][1]


def test_copper_reserve_years_and_growth():
    assert 42 < cn.copper_years() < 43.5
    assert cn.COPPER_RESERVES_2024 / cn.COPPER_RESERVES_1970 == 3.5
    assert cn.COPPER_PRODUCED_SINCE_1970 > cn.COPPER_RESERVES_1970


def test_problem_chain():
    p = cn.problem()
    assert p["agg_total_t"] == 6e5 and p["sand_per_year_t"] == 2.4e4
    assert p["deposit_m3"] == 3e6 and abs(p["reserve_t"] - 3.2e6) < 1e-6
    assert abs(p["extraction_t_yr"] - 1.6e5) < 1e-6
    assert abs(p["river_ratio"] - 80) < 1e-9 and p["recycling_saving_t_yr"] == 6000
    assert abs(p["years"] - 20) < 1e-9

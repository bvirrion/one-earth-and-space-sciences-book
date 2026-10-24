"""Tests for figdata/grade-9/cliff_retreat.py (grade 9, chapter 4)."""
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "grade-9"))
import cliff_retreat as cr  # noqa: E402


def test_the_edge_only_retreats():
    d = [x for _y, x in cr.SURVEY]
    assert all(a > b for a, b in zip(d, d[1:]))
    assert all(r > 0 for *_s, r in cr.intervals())


def test_average_rate_and_fastest_interval():
    p = cr.problem()
    assert abs(p["total_retreat_m"] - 15.6) < 1e-9 and p["span_yr"] == 20
    assert abs(p["rate_m_yr"] - 0.78) < 1e-9
    # the storm interval is the fastest, about three times the average
    assert (p["fast_start"], p["fast_end"]) == (2012, 2014)
    assert abs(p["fast_rate_m_yr"] - 2.4) < 1e-9
    assert 3.0 <= p["fast_ratio"] < 3.1
    # the rate stays within "up to about one metre a year" (sdnp:birling)
    assert p["rate_m_yr"] < 1.0


def test_forecast_years_printed_in_the_solution():
    p = cr.problem()
    assert round(p["road_years"]) == 39 and round(p["road_year"]) == 2063
    assert round(p["margin_year"]) == 2050
    assert 19 < p["storm_years"] < 20 and 2043 < p["storm_year"] < 2044
    assert round(p["lighthouse_years"]) == 22


def test_tibet_net_rise():
    assert abs(cr.tibet_rate_mm_yr() - 0.46) < 1e-12

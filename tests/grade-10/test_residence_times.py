"""figdata/grade-10/residence_times.py: stock / flux for the reservoirs of the water cycle."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import residence_times as rt  # noqa: E402


def test_ocean_residence_time_is_near_3000_years():
    t = dict(rt.times())
    assert 3000 < t["ocean"] < 3500          # 1,335,040 / 413 = 3233 years


def test_atmosphere_is_renewed_in_about_ten_days():
    t = dict(rt.times())
    assert 8 < t["atmosphere"] * rt.DAYS_PER_YEAR < 11


def test_global_budget_closes():
    for k, v in rt.balances().items():
        assert abs(v) < 1e-9, k


def test_order_of_the_chart():
    ys = [y for _, y in rt.times()]
    assert ys == sorted(ys)
    assert rt.NUBIAN_YEARS[0] > 50 * dict(rt.times())["ocean"]

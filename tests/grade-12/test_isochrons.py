import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "shared"))
import isochrons as iso  # noqa: E402
import region  # noqa: E402


def test_ages_agree_with_the_varden_region_model():
    ages = {u[1]: u[4] for u in region.UNITS}
    assert iso.GRANITE_AGE_MA == ages["granite"]
    assert iso.SCHIST_AGE_MA == ages["schist"]


def test_granite_isochron_slope_gives_310_ma_from_rounded_ratios():
    n = iso.numbers()
    assert n["granite_age_Ma"] == pytest.approx(310.0, abs=0.5)
    assert n["granite_intercept"] == pytest.approx(iso.GRANITE_SR0, abs=1e-5)
    assert n["schist_age_Ma"] == pytest.approx(480.0, abs=0.5)
    # minerals listed in the order of rising Rb/Sr, so their 87Sr/86Sr rises too
    ys = [s[2] for s in iso.granite_samples()]
    assert ys == sorted(ys)


def test_age_from_slope_inverts_the_isochron_equation():
    for t in (10.0, 310.0, 4567.0):
        assert iso.age_from_slope_ma(iso.growth(t)) == pytest.approx(t, rel=1e-12)
    assert iso.numbers()["rb_half_life_Ga"] == pytest.approx(49.61, abs=0.01)


def test_patterson_meteorites_give_4_55_ga_within_his_error():
    n = iso.numbers()
    assert abs(n["pb_age_Ga"] - 4.55) < 0.07
    # the slope at 4.55 Ga with his constants, and the inverse
    assert iso.pb_age_ga(iso.pb_slope(4.55)) == pytest.approx(4.55, abs=1e-6)
    # the modern sediment lies close to the meteorite line (within 3 % of its 207/204)
    assert abs(n["sediment_residual"]) < 0.03 * iso.SEDIMENT[1]


def test_history_is_in_order_and_ends_at_today():
    years = [h[1] for h in iso.HISTORY]
    assert years == sorted(years)
    assert iso.HISTORY[-1][2] < 4.54e9 < iso.HISTORY[-1][3]

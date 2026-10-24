import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import ice_age_records as iar  # noqa: E402


def test_temperature_and_co2_vary_together():
    r = iar.correlation()
    assert r > 0.8
    a, b = iar.fit()
    # a warmer Antarctica goes with more CO2, a few ppm per degree
    assert 5.0 < b < 11.0
    # the line passes close to the pre-industrial value at today's temperature
    assert 255.0 < a < 280.0


def test_glacial_interglacial_amplitudes():
    n = iar.numbers()
    assert -11.0 < n["edc_min_C"] < -9.0
    assert 3.0 < n["edc_max_C"] < 6.0
    assert 170.0 < n["co2_min_ppm"] < 180.0
    assert 295.0 < n["co2_max_ppm"] < 305.0
    # the last deglaciation: about 9 degC at Dome C, about 75 ppm
    assert 8.0 < n["edc_rise_C"] < 10.0
    assert 65.0 < n["co2_rise_ppm"] < 85.0
    # the coldest point lies in or near the LGM
    assert 18.0 < n["edc_min_age_kyr"] < 30.0


def test_hundred_thousand_year_rhythm():
    n = iar.numbers()
    assert 80.0 < n["edc_period_kyr"] < 125.0
    assert 80.0 < n["lr04_period_0_700"] < 125.0
    assert 38.0 < n["lr04_period_1300_2600"] < 44.0


def test_lr04_is_the_stack_only_and_later_mean_is_heavier():
    lr = iar.lr04()
    ages = lr[:, 0]
    assert ages[0] == 0.0 and ages[-1] == pytest.approx(5.32)
    assert all(b > a for a, b in zip(ages, ages[1:]))
    n = iar.numbers()
    assert n["lr04_mean_0_1Ma"] > n["lr04_mean_3_5Ma"] + 0.5
    # the LGM is heavier than today
    assert n["lr04_lgm"] > n["lr04_today"] + 1.0


def test_lowered_sea_level_adds_land():
    n = iar.numbers()
    assert n["sunda_land_lgm_km2"] > n["sunda_land_now_km2"]
    assert 1.5e6 < n["sunda_gain_km2"] < 5e6
    assert n["world_land_lgm_frac"] > n["world_land_now_frac"]
    # land is about 29 % of the surface today (Antarctic ice counted as land)
    assert 0.27 < n["world_land_now_frac"] < 0.31


def test_today_is_about_twenty_times_faster():
    n = iar.numbers()
    assert n["ldt_mean_rate_C_per_kyr"] == pytest.approx(6.0 / 7.0)
    assert 0.17 < n["rate_1970_2025_C_per_decade"] < 0.23
    assert 18.0 < n["ratio_today_ldt_mean"] < 28.0
    assert n["ratio_today_ldt_fast_lo"] > 10.0


def test_pollen_rows_sum_to_100():
    for row in iar.pollen_rows():
        assert sum(row[2:]) == 100
    ages = [r[1] for r in iar.pollen_rows()]
    assert ages[0] == 14.0 and ages[-1] == 6.0


def test_deep_periods_are_ordered():
    assert [d[0] for d in iar.DEEP] == ["PETM", "EECO", "MPWP", "LIG", "LGM", "MH"]
    for nm, age, t, c, s in iar.DEEP:
        assert t[0] < t[1] and c[0] <= c[1]


def test_borneo_joins_asia_before_sumatra_and_java_need_less():
    n = iar.numbers()
    # Borneo needs a fall of a few tens of metres; Sumatra and Java join sooner
    assert -45.0 < n["borneo_link_m"] < -25.0
    assert n["sumatra_link_m"] > n["borneo_link_m"]
    assert n["java_link_m"] > n["borneo_link_m"]
    # all are joined at the lowstand
    assert n["borneo_link_m"] > -iar.LOWSTAND_M


def test_link_level_on_a_toy_grid():
    z = np.array([[5.0, -10.0, 5.0], [5.0, -50.0, 5.0], [5.0, -80.0, 5.0]])
    lats = np.array([2.0, 1.0, 0.0])
    lons = np.array([0.0, 1.0, 2.0])
    assert iar.link_level(lats, lons, z, (1.0, 0.0), (1.0, 2.0)) == -10.0

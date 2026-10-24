"""figdata/grade-10/clouds.py: lapse rates, the condensation-level rule and the lee wind."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import clouds as cl  # noqa: E402


def test_rates():
    assert abs(cl.GAMMA_D - 9.8) < 0.1                       # g/c_p
    n = cl.numbers()
    assert 1.6 < n["dewpoint_rate"] < 1.9                     # dew point falls about 1.8 K/km
    assert 4.0 < n["moist_rate_15C_1000"] < 5.5 < n["moist_rate_0C_700"] < 6.5 < n["moist_rate_m20C_500"]
    assert abs(cl.ws(293.15) * 1000 - 14.7) < 0.2            # about 14.7 g/kg at 20 degC, 1013 hPa


def test_condensation_level_rule():
    for t, td in ((28, 16), (20, 12), (15, 13), (32, 10)):
        rows, lcl = cl.parcel(t, td, z_top=4.0)
        rule = 0.125 * (t - td)
        assert abs(lcl - rule) <= max(0.06 * rule, 0.03), (t, td, lcl, rule)


def test_lee_wind_is_warmer_and_drier():
    n = cl.numbers()
    assert n["mtn_T_lee"] > 20 + 5 and n["mtn_Td_lee"] < 12 - 4
    assert n["mtn_w_top_gkg"] < n["mtn_w_start_gkg"]
    assert 3.5 < n["cloud_top_A_km"] < 4.1 and n["parcel_minus_env_B_at_1km"] < 0
    assert not n["parcel_warmer_than_A_above_top"]

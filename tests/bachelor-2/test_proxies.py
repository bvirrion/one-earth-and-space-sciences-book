"""Tests for figdata/bachelor-2/proxies.py (ch. 24 climate-proxies)."""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "bachelor-2"))
import proxies as px  # noqa: E402


def test_ice_volume_mass_balance_conserves_oxygen_18():
    h, d_ice, H = 130.0, -40.0, px.H_OCEAN
    d_ocean = px.ice_volume_shift(h, d_ice)
    # (ocean left) * d_ocean + (ice) * d_ice = (whole ocean today) * 0
    assert abs((H - h) * d_ocean + h * d_ice) < 1e-9
    assert abs(d_ocean - 1.464) < 0.001
    # about 0.011 permil per metre of sea level, as the textbook rule
    assert abs(px.ice_volume_shift(1.0, -40.0) - 0.011) < 0.0005


def test_benthic_calibration_slope_and_inverse():
    assert abs(px.benthic_temperature(3.0, 0.0) - px.benthic_temperature(3.21, 0.0) - 1.0) < 0.001
    for T in (-1.0, 2.0, 10.0):
        assert abs(px.benthic_temperature(px.benthic_offset(T), 0.0) - T) < 1e-9


def test_mgca_is_nine_percent_per_degree():
    assert abs(px.mgca(11.0) / px.mgca(10.0) - math.exp(0.09)) < 1e-12
    assert abs(px.mgca_temperature(px.mgca(17.3)) - 17.3) < 1e-9
    assert abs(px.mgca_temperature(2.0) - 17.88) < 0.01


def test_lr04_and_edc_windows():
    n = px.numbers()
    assert n["lr04_today"] == 3.23 and abs(n["lr04_lgm"] - 4.92) < 1e-9
    assert abs(n["edc_lgm_C"] + 9.389) < 0.001
    assert abs(n["cool_porewater"] - 4.76 * 0.69) < 1e-9


def test_gicc05_table_is_monotonic_and_errors_grow():
    a = px.GICC05
    assert all(b[1] > x[1] and b[2] >= x[2] and b[3] > x[3] for x, b in zip(a, a[1:]))
    assert px.uncertain_layers(1287) == 2574
    assert abs(px.random_error(1287) - 25.37) < 0.01


def test_co2_windows():
    n = px.numbers()
    assert 185 < n["co2_lgm"] < 195 and 275 < n["co2_preind"] < 285

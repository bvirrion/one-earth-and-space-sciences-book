"""Tests for the rifts-ridges-margins figure data: the depth--age law and the binned
depths of the ocean floor."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import depth_age as da  # noqa: E402


def test_halfspace_law_values():
    assert da.halfspace(0.0) == 2500.0
    assert abs(da.halfspace(25.0) - 4250.0) < 1e-9
    assert abs(da.halfspace(100.0) - 6000.0) < 1e-9


def test_plate_law_starts_at_3200_and_tends_to_6400():
    assert abs(da.plate(0.0) - 3200.0) < 1e-9
    assert abs(da.plate(1000.0) - 6400.0) < 1e-3
    # older floor deepens more slowly than the half-space predicts
    assert da.plate(150.0) < da.halfspace(150.0)


def test_erfc_integral_is_one_over_root_pi():
    n, top = 200000, 8.0
    h = top / n
    s = sum(math.erfc((k + 0.5) * h) for k in range(n)) * h
    assert abs(s - 1.0 / math.sqrt(math.pi)) < 1e-6


def test_physical_coefficient_is_close_to_the_fitted_one():
    # the book's values (ledger parsons:plate-model: alpha 3.2e-5, 1350 degC; kappa 1e-6)
    # give 393 m per sqrt(Myr), against the 350 fitted to the North Pacific and Atlantic
    c = da.halfspace_coefficient(3.2e-5, 3300.0, 1000.0, 1350.0, 1e-6)
    assert abs(c - 393.0) < 1.0
    assert abs(c / 350.0 - 1.0) < 0.15


def test_quantile():
    v = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert da.quantile(v, 0.5) == 3.0
    assert da.quantile(v, 0.25) == 2.0
    assert abs(da.quantile([0.0, 10.0], 0.75) - 7.5) < 1e-12


def test_ocean_floor_deepens_with_age_then_flattens():
    rows = da.bins()
    med = {round(t): m for t, n, q1, m, q3 in rows}
    assert sum(n for _, n, _, _, _ in rows) > 25000
    young_rise = med[41] - med[1]
    old_rise = med[161] - med[61]
    assert young_rise > 1000.0
    assert old_rise < young_rise / 2.0
    # the ridge-axis bin lies within 600 m of the law's ridge depth
    assert abs(med[1] - 2500.0) < 600.0


import ridge_budget as rb  # noqa: E402


def test_arc_length():
    assert abs(rb.arc_km(0.0, 0.0, 0.0, 1.0) - 6371.0 * math.pi / 180.0) < 1e-9
    assert abs(rb.arc_km(10.0, 20.0, 10.0, 20.0)) < 1e-3


def test_ridge_production_is_a_few_km2_per_year():
    length, area = rb.ridge_production()
    assert 55000.0 < length < 80000.0
    assert 2.5 < area < 3.5
    # converging or zero-rate steps add nothing
    fake = [{"class": "OSR", "lat0": "0", "lon0": "0", "lat1": "0", "lon1": "1", "div_mm_a": "-5"},
            {"class": "OTF", "lat0": "0", "lon0": "0", "lat1": "0", "lon1": "1", "div_mm_a": "50"}]
    ell, a = rb.ridge_production(fake)
    assert abs(ell - 6371.0 * math.pi / 180.0) < 1e-9 and a == 0.0


def test_charlie_gibbs_offset_is_about_350_km():
    off, n = rb.charlie_gibbs_offset()
    assert n >= 2
    assert 320.0 < off < 380.0


def test_azores_junction_is_ridge_ridge_ridge():
    (lat, lon), classes = rb.azores_junction()
    assert abs(lat - 39.4) < 0.1 and abs(lon + 29.8) < 0.1
    assert set(classes.values()) == {"OSR"}


def test_subduction_consumes_about_what_the_ridges_make():
    sub_len, sub_area = rb.subduction_consumption()
    _, made = rb.ridge_production()
    assert 40000.0 < sub_len < 70000.0
    assert abs(sub_area / made - 1.0) < 0.35


def test_backarc_rates():
    mariana, lau = rb.backarc_rates()
    assert 25.0 < mariana < 40.0
    assert lau > 100.0


def test_the_plates_destroy_as_much_area_as_they_make():
    made, lost = rb.area_balance()
    assert 3.4 < made < 3.6
    assert abs(made - lost) / made < 0.01
    # the subduction steps take most, not all, of what the ridges make
    assert rb.subduction_consumption()[1] < rb.ridge_production()[1] < made

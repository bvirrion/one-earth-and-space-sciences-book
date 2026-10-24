import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import arc_magmatism as am  # noqa: E402


def test_slab_lies_about_100_km_below_the_volcanic_front():
    n = am.numbers()
    assert 140.5 < n["jp_front_lon"] < 141.5            # Iwate, the easternmost volcano
    assert 80 < n["jp_slab_depth_front"] < 130          # the brief's 80-130 km
    assert n["jp_fit_n"] > 100


def test_fitted_slab_reaches_the_surface_near_the_trench():
    a, b, k = am.slab_fit()
    x0 = -a / b                                          # depth 0
    lon0 = am.LON0 + x0 / am.KM_PER_DEG_LON
    assert 143.5 < lon0 < 145.0                          # the Japan Trench is near 144 E
    assert 10 < am.numbers()["jp_dip_deg"] < 35


def test_water_lowers_the_solidus_by_hundreds_of_degrees():
    n = am.numbers()
    assert n["dry_minus_wet_3gpa"] > 400
    assert n["dry_minus_wet_5gpa"] > 500
    assert 90 < n["z_3gpa_km"] < 100


def test_most_volcanoes_sit_above_subduction_zones():
    n = am.numbers()
    assert 0.6 < n["frac_subduction"] < 0.8


def test_planar_slab_geometry_gives_the_same_depth():
    n = am.numbers()
    assert 250 < n["jp_front_trench_km"] < 290
    assert abs(n["jp_H_geom"] - n["bin_141_median"]) < 15     # d tan(dip) against the measured median

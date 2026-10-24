"""figdata/grade-10/meridian_degree.py: the ellipsoid gives the textbook lengths."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import meridian_degree as md  # noqa: E402


def test_degree_lengths():
    n = md.numbers()
    assert abs(n["deg_equator_exact_km"] - 110.574) < 0.001     # 1 deg of latitude at the equator
    assert abs(n["deg_pole_km"] - 111.694) < 0.001              # ... at the pole
    assert n["deg_pole_km"] > n["deg_66_km"] > n["deg_45_km"] > n["deg_equator_km"]
    assert abs(n["par_equator_km"] - 111.320) < 0.001           # 1 deg of longitude at the equator
    assert abs(n["par_60_km"] - 55.8) < 0.1


def test_quarter_meridian_and_metre():
    n = md.numbers()
    assert abs(n["quarter_meridian_km"] - 10001.966) < 0.001
    assert abs(n["a_minus_b_km"] - 21.385) < 0.001
    assert 0.19 < n["metre_short_by_mm"] < 0.20                  # the 1799 metre is ~0.2 mm short


def test_eratosthenes_modern():
    n = md.numbers()
    assert abs(n["syene_alexandria_dlat_deg"] - 7.111) < 0.001
    assert 780 < n["syene_alexandria_arc_km"] < 795
    assert abs(n["eratosthenes_modern_km"] - 4 * n["quarter_meridian_km"]) < 150   # 0.3 %: local curvature

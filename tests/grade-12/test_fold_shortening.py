import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import fold_shortening as fs  # noqa: E402


def test_chevron_formula_matches_the_measured_polyline():
    for theta in (12.0, 30.0, 60.0):
        t = math.tan(math.radians(theta))
        zigzag = [(0.0, 0.0), (1.0, t), (2.0, 0.0), (3.0, t)]
        assert fs.shortening(zigzag) == pytest.approx(fs.chevron_shortening(theta), rel=1e-12)
    assert fs.chevron_shortening(60.0) == pytest.approx(0.5)
    assert fs.chevron_shortening(0.0) == 0.0


def test_a_straight_layer_is_not_shortened_and_folding_only_adds_length():
    assert fs.shortening([(0.0, 0.0), (5.0, 0.0)]) == 0.0
    es = [fs.shortening(fs.sine_profile(r / 20)) for r in range(0, 11)]
    assert es[0] == pytest.approx(0.0, abs=1e-12)
    assert all(b > a for a, b in zip(es, es[1:]))


def test_sine_fold_arc_length_against_the_elliptic_integral():
    # arc length of one wavelength of A sin(2 pi x / lam), lam = 1: 4 a E(k) with a = sqrt(1 + (2 pi A)^2)
    from scipy.special import ellipe
    A = 0.25
    m = (2 * math.pi * A) ** 2
    exact = 4 * math.sqrt(1 + m) * ellipe(m / (1 + m)) / (2 * math.pi)
    assert fs.length_along(fs.sine_profile(A, n=4000)) == pytest.approx(exact, rel=1e-6)


def test_the_varden_profile_gives_the_chevron_value():
    n = fs.numbers()
    assert n["varden_profile_e_pct"] == pytest.approx(n["varden_e_pct"], rel=1e-6)
    assert n["varden_e_pct"] == pytest.approx(2.185, abs=0.001)


def test_section_axes_sit_on_the_hinges_of_the_section():
    """The axis lines of section A-B pass through the lowest point (syncline, hanging
    wall) and highest point (anticline, footwall) of the base of the chalk on the grid."""
    n = fs.numbers()
    (ax, ay), (bx, by) = fs.region.SECTION_AB
    L = math.hypot(bx - ax, by - ay)

    def base_chalk(s_km):
        x, y = ax + (bx - ax) * s_km * 1000 / L, ay + (by - ay) * s_km * 1000 / L
        z = 650.0
        while z > -1500 and fs.region.unit(x, y, z, with_alluvium=False) not in (0, fs.region.UNIT["chalk"]):
            z += 1.0
        while z > -1500 and fs.region.unit(x, y, z, with_alluvium=False) in (0, fs.region.UNIT["chalk"]):
            z -= 1.0
        return z

    ss = [7.0 + 0.01 * k for k in range(101)]
    low = min(ss, key=base_chalk)
    assert abs(low - n["section_syncline_km"]) < 0.02
    assert n["section_anticline_km"] == pytest.approx(3.162, abs=0.001)
    assert n["section_syncline_km"] == pytest.approx(7.484, abs=0.001)

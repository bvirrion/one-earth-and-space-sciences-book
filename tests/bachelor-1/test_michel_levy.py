"""Tests for figdata/bachelor-1/michel_levy.py (optical-mineralogy)."""
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "bachelor-1"))
import michel_levy as M  # noqa: E402


def test_zero_retardation_is_black():
    assert M.colour(0.0) == [0.0, 0.0, 0.0]


def test_d65_white_maps_to_srgb_white():
    rgb = [M.gamma(v) for v in M.linear_rgb(M.xyz(lambda lam: 1.0))]
    assert all(abs(v - 1.0) < 1e-3 for v in rgb)


def test_first_order_red_near_550_nm():
    mins = M.green_minima()
    assert 530 <= mins[0] <= 560
    # the next two tints follow at about twice and three times the first
    assert abs(mins[1] / mins[0] - 2.0) < 0.06 and abs(mins[2] / mins[0] - 3.0) < 0.09


def test_colours_fade_with_order():
    mins = M.green_minima()
    s = [M.saturation(m) for m in mins[:3]]
    assert s[0] > s[1] > s[2]
    assert M.saturation(5000.0) < 0.01          # high-order white


def test_lines_stay_inside_chart():
    for d, x1, y1 in M.lines():
        assert 0 < x1 <= M.D_MAX + 1e-9 and 0 < y1 <= M.T_MAX + 1e-9
        assert abs(x1 - d * 1000.0 * y1) < 1e-9


def test_four_extinctions_per_turn():
    for th in (0, 90, 180, 270, 360):
        assert M.intensity(th, 270.0) < 1e-20
    peaks = [th for th in range(0, 360) if all(M.intensity(th, 270.0) >= M.intensity(th + d, 270.0) for d in (-1, 1))]
    assert peaks == [45, 135, 225, 315]
    # a half-wave plate passes everything at 45 degrees
    assert abs(M.intensity(45, 275.0) - 1.0) < 1e-12

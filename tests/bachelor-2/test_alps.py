"""Tests for the Alps figure data (figdata/bachelor-2/alps.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import alps  # noqa: E402

PROBLEM = [(8.0, 0), (3.0, 35), (3.0, 35), (5.0, 0), (2.5, 50), (2.5, 50), (6.0, 10),
           (4.0, 40), (4.0, 40), (10.0, 5)]


def test_line_length_balance_of_the_problem_section():
    assert alps.bed_length([(5.0, 0)]) == pytest.approx(5.0)
    assert sum(dx for dx, _ in PROBLEM) == pytest.approx(48.0)
    l0 = alps.bed_length(PROBLEM) + 6.0          # the stretch repeated under the thrust
    assert l0 == pytest.approx(60.68, abs=0.01)
    assert alps.shortening(48.0, 60.7) == pytest.approx(0.209, abs=5e-4)


def test_area_balance_and_decollement_depth():
    # a strip of cover keeps its area: restored length = area / thickness
    assert alps.restored_length_area(146.0, 2.4) == pytest.approx(60.83, abs=0.01)
    # excess area = S d: a decollement 2 km below the marker, 17 km of shortening
    assert alps.decollement_depth(34.0, 17.0) == pytest.approx(2.0)
    l0, l, t = 59.0, 42.0, 2.0
    assert alps.decollement_depth(l0 * t - l * t, l0 - l) == pytest.approx(t)


def test_chevron_keeps_its_length_and_shortens_by_one_minus_cos():
    pts, x = alps.chevron(l0=30.0, dip=40.0, n=6)
    length = sum(math.dist(a, b) for a, b in zip(pts, pts[1:]))
    assert length == pytest.approx(30.0)
    assert x == pytest.approx(30.0 * math.cos(math.radians(40.0)))
    assert alps.shortening(x, 30.0) == pytest.approx(1 - math.cos(math.radians(40.0)))


def test_airy_root_uses_the_year1_densities():
    assert alps.airy_root(1000.0) == pytest.approx(4.5)
    assert alps.airy_root(-200.0) == 0.0


def test_swath_profile_and_moho_picks():
    sw = alps.swath()
    assert len(sw) == 55 and sw[0][0] == pytest.approx(45.3) and sw[-1][0] == pytest.approx(48.0)
    assert all(m <= x for _, _, m, x in sw)
    top = max(sw, key=lambda r: r[2])
    assert top[0] == pytest.approx(46.5) and 2700 < top[2] < 2800
    mp = alps.moho_profile()
    assert len(mp) == 16
    deep = max(mp, key=lambda r: r[2])
    assert deep[0] == pytest.approx(45.545, abs=1e-3) and deep[2] == pytest.approx(61.18)
    # the root lies south of the highest ground, and is larger than local Airy predicts
    assert deep[0] < top[0]
    obs, airy = alps.root_areas()
    assert obs > airy > 0


def test_contours_stay_in_the_window():
    for lev in (0, 2000):
        lines = alps.contours(lev)
        assert lines
        for line in lines:
            for lon, lat in line:
                assert 5.0 <= lon <= 14.0 and 43.5 <= lat <= 48.5
    # the coastline lies in the south (Ligurian Sea, Adriatic)
    assert all(lat < 46.0 for line in alps.contours(0) for _, lat in line)

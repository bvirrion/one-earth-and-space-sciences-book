"""Tests for the Leavitt-law fit and the distance-ladder rungs (Year 3, ch. 29)."""
import math
import os
import random
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import distance_ladder as dl  # noqa: E402


def test_wesenheit_and_distance_modulus():
    assert dl.wesenheit(15.0, 16.0) == pytest.approx(15.0 - 1.55)
    assert dl.distance_kpc(18.477) == pytest.approx(49.59, abs=0.01)
    assert dl.distance_kpc(10.0) == pytest.approx(1.0)


def test_clipped_fit_on_synthetic_data():
    rng = random.Random(7)
    xy = [(x, -3.3 * x + 15.9 + rng.gauss(0, 0.08)) for x in [i / 500 for i in range(750)]]
    xy += [(0.5, 25.0), (1.0, 5.0)]         # two wild points
    a, b, s, kept, removed = dl.clipped_fit(xy)
    assert (0.5, 25.0) in removed and (1.0, 5.0) in removed
    assert a == pytest.approx(-3.3, abs=0.03) and b == pytest.approx(15.9, abs=0.02)
    assert s == pytest.approx(0.08, rel=0.1)


def test_ogle_fit_reproduces_the_published_relation():
    stars = dl.load_fundamental()
    assert len(stars) > 2000
    a, b, s, kept, removed = dl.clipped_fit([(x, w) for x, w, _, _ in stars])
    # Soszynski et al. 2015, Table 2, LMC F: -3.314 +- 0.008, 15.888 +- 0.005, sigma 0.077
    assert a == pytest.approx(-3.314, abs=0.008)
    assert b == pytest.approx(15.888, abs=0.005)
    assert s == pytest.approx(0.077, abs=0.005)
    assert len(removed) < 0.1 * len(stars)


def test_ladder_rungs_overlap_where_they_must():
    rungs = {name: (lo, hi) for _, name, lo, hi in dl.ladder()}
    # cz/H0 at z = 0.011 with H0 = 73.04 is 45 Mpc
    assert rungs["cepheids"][1] == pytest.approx(299792.458 * 0.011 / 73.04 * 1000)
    assert rungs["parallax"][1] == pytest.approx(4.0)
    # the supernova Hubble-flow sample starts beyond the calibrators
    assert rungs["snia"][0] > rungs["cepheids"][1]
    assert math.isclose(rungs["trgb"][0], rungs["cepheids"][0])

"""Tests for the Wilson-cycle figure data (figdata/bachelor-2/wilson.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import wilson  # noqa: E402


def test_model_ocean_opens_then_closes():
    assert wilson.ocean_width(600) == 0.0
    assert wilson.ocean_width(wilson.T_OPEN) == 0.0
    assert wilson.max_width() == pytest.approx(30 * 80)
    assert wilson.ocean_width(wilson.T_SUB) == pytest.approx(2400)
    # narrows at V_C - V_S = 30 km/Myr and closes 80 Myr later
    assert wilson.closure_age() == pytest.approx(410)
    assert wilson.ocean_width(450) == pytest.approx(2400 - 30 * 40)
    assert wilson.ocean_width(400) == 0.0
    # the width never exceeds its value at the start of subduction
    assert max(wilson.ocean_width(t) for t in range(360, 601)) == pytest.approx(2400)


def test_problem_model_values():
    # the weekend-problem ocean: spreading from 580 Ma at 36, subduction from 500 Ma at 64
    assert wilson.max_width(580, 500, 36) == pytest.approx(2880)
    assert wilson.closure_age(580, 500, 36, 64) == pytest.approx(500 - 2880 / 28)


def test_ridge_reaches_the_trench():
    # the ridge moves at V_C - V_S/2 relative to the upper plate
    assert wilson.ridge_arrival(1200, 36, 64) == pytest.approx(1200 / 46)


def test_relief_decay_with_rebound():
    assert wilson.K_EROSION * 11 == pytest.approx(math.log(10))
    assert wilson.F_REBOUND == pytest.approx(600 / 3300)
    tau = wilson.decay_tau()
    assert tau == pytest.approx(26.275, abs=0.001)
    assert wilson.time_to_height(1000, 100) == pytest.approx(tau * math.log(10))


def test_supercontinents_and_spacings():
    rows = wilson.supercontinent_rows()
    assert [r[0] for r in rows][-1] == "Pangaea"
    assert all(r[2] >= r[3] for r in rows)
    sp = wilson.mid_spacings()
    assert sum(sp) == pytest.approx(3000 - 262.5)
    assert sp == pytest.approx([400, 1100, 625, 275, 337.5])

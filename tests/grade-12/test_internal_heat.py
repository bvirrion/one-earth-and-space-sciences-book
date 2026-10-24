import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import internal_heat as ih  # noqa: E402


def test_present_heat_matches_the_geoneutrino_scale():
    p = ih.present_tw()
    assert p["Th232"] + p["U238"] == pytest.approx(20.0)
    assert p["K40"] == pytest.approx(4.0)
    # U-235 carries 0.72 % of the atoms of uranium but six times the heat per kg of U-238
    assert p["U235"] / p["U238"] == pytest.approx(0.007204 * 568.47 / (0.992796 * 95.13))
    # with Th/U = 3.9, thorium gives a little more heat than uranium-238
    assert 1.0 < p["Th232"] / p["U238"] < 1.2
    assert 22 < ih.total_tw() < 26
    assert 0.45 < ih.numbers()["share_radiogenic"] < 0.55        # about half


def test_past_heat_follows_the_decay_law():
    for k, (half, _) in ih.ISOTOPES.items():
        # one half-life ago, twice the heat
        assert ih.heat_tw(half)[k] == pytest.approx(2 * ih.present_tw()[k])
    # U-235 and K-40 dominate the early Earth
    assert ih.numbers()["share_U235_K40_4.5Ga"] > 0.6
    assert ih.total_tw(4.5) > 4 * ih.total_tw(0.0)


def test_ocean_floor_cools_as_one_over_root_age():
    assert ih.halfspace_q(1.0) == pytest.approx(490.0)
    assert ih.halfspace_q(4.0) == pytest.approx(245.0)
    # the floor reaches the continental mean near 48 Myr
    t = ih.numbers()["age_where_q_equals_cont_Myr"]
    assert ih.halfspace_q(t) == pytest.approx(ih.CONT_MEAN)


def test_conduction_is_far_too_slow():
    assert ih.numbers()["conduction_time_Gyr"] > 50 * 4.5   # over fifty times the age of the Earth
    assert ih.numbers()["borehole_q_mW"] == pytest.approx(2.72 * 29)

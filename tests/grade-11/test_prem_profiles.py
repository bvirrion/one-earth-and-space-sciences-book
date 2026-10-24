"""figdata/grade-11/prem_profiles.py: the PREM boundaries and the mean density."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import prem_profiles as pp  # noqa: E402


def test_boundaries_are_the_published_depths():
    n = pp.numbers()
    assert n["cmb_km"] == 2891.0
    assert n["icb_km"] == 5149.5
    assert abs(n["core_radius_km"] - 3480.0) < 1e-9
    assert abs(n["inner_core_radius_km"] - 1221.5) < 1e-9


def test_no_s_waves_in_the_outer_core():
    assert pp.numbers()["vs_outer_core_max"] == 0.0


def test_p_speed_drops_at_the_core_mantle_boundary():
    n = pp.numbers()
    assert n["vp_above_cmb"] > 13.0 and n["vp_below_cmb"] < 8.5


def test_mean_density_is_the_earths():
    # the Earth's mass over its volume: 5.97e24 kg / 1.083e21 m3 = 5.51 g/cm3
    assert abs(pp.mean_density() - 5.51) < 0.03


def test_mean_density_of_a_uniform_model():
    rows = [(0.0, 1, 1, 2.0, "a"), (6371.0, 1, 1, 2.0, "a")]
    assert abs(pp.mean_density(rows) - 2.0) < 1e-3     # midpoint rule, 50 steps


def test_low_velocity_zone_between_80_and_220_km():
    rows = pp.prem()
    up = [(d, vs) for d, vp, vs, rho, reg in rows if 80.0 <= d <= 220.0 and reg == "mantle"]
    # S speed decreases with depth through the zone, then jumps up at 220 km
    assert all(b[1] < a[1] for a, b in zip(up[:-1], up[1:]) if b[0] > a[0])
    assert pp.value_at(220.0, 2, rows) > pp.value_at(220.0, 2, rows, below=False) + 0.1

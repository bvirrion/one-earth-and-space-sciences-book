"""figdata/grade-10/ocean_profiles.py: WOA23 profiles and the equation of state."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import ocean_profiles as op  # noqa: E402


def test_equation_of_state_check_values():
    assert abs(op.rho(35, 0) - 1028.1063) < 0.001      # UNESCO 44 reference density
    assert abs(op.rho(0, 4) - 999.975) < 0.01           # pure water near its maximum density
    assert op.rho(36, 10) > op.rho(35, 10)              # saltier is denser
    assert op.rho(35, 20) < op.rho(35, 10)              # warmer is lighter


def test_profiles_layered():
    n = op.numbers()
    assert n["warmpool_dt_0_1000"] > 20                 # tropical surface >20 degC warmer than 1000 m
    assert n["arctic_tmax"] - n["arctic_tmin"] < 3      # polar column within a few degrees
    assert n["arctic_s200"] - n["arctic_s0"] > 4        # Arctic halocline
    for site in op.SITES:                               # stable: density grows downwards
        p = op.profile(site)
        assert p[-1][3] > p[0][3]


def test_season_and_upwelling():
    n = op.numbers()
    assert n["mld_feb"] > 5 * n["mld_aug"]              # winter mixed layer far deeper
    assert n["peru_t0"] < n["gyre_t0"] - 4              # cold water off Peru
    assert abs(n["ocean_volume_km3"] - 1.3324e9) < 0.001e9

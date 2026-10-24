"""figdata/grade-11/seafloor_age.py: oldest floor, ages growing away from the ridge."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import seafloor_age as sa  # noqa: E402


def test_oldest_open_ocean_floor_is_below_200_myr():
    n = sa.numbers()
    assert 180 < n["oldest_open_myr"] < 200
    assert n["oldest_mediterranean_myr"] > n["oldest_open_myr"]


def test_mean_age_close_to_published():
    # Seton et al. (2020): mean age of the oceanic crust 64.2 Myr (whole grid)
    assert abs(sa.numbers()["mean_age_myr"] - 64.2) < 3.0


def test_ages_grow_away_from_the_ridge_at_30s():
    prof, ridge = sa.profile_30s()
    assert -20 < ridge < -10                     # Mid-Atlantic Ridge near 14 W
    for side in (1, -1):
        pts = [(abs(d), a) for _, d, a in prof if d * side > 0]
        n = len(pts)
        mx = sum(d for d, _ in pts) / n
        my = sum(a for _, a in pts) / n
        sxy = sum((d - mx) * (a - my) for d, a in pts)
        sxx = sum((d - mx) ** 2 for d, _ in pts)
        syy = sum((a - my) ** 2 for _, a in pts)
        assert sxy > 0 and sxy / (sxx * syy) ** 0.5 > 0.95

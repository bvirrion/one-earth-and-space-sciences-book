"""figdata/grade-2: ocean fraction and the 100 buckets of water."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-2"))
import ocean_fraction as of  # noqa: E402
import water_shares as ws  # noqa: E402


def test_ocean_fraction_matches_usgs():
    f = of.ocean_fraction()
    assert 0.69 < f < 0.73          # USGS: "about 71 percent" (usgs-wss:ocean-cover)
    assert round(100 * f) == 71


def test_area_weighting():
    # one cell at the equator and one at 60 degrees: the polar cell counts half
    f = of.ocean_fraction([(0.0, 0.0, -10.0), (60.0, 0.0, 10.0)])
    assert abs(f - 1 / 1.5) < 1e-9


def test_grid_has_the_right_number_of_blue_squares():
    g = of.grid(71)
    assert len(g) == 100 and sum(b for _, _, b in g) == 71


def test_buckets_sum_to_100_and_follow_largest_remainder():
    b = ws.buckets()
    assert sum(b.values()) == 100
    assert b == {"ocean": 96, "ice": 2, "groundwater": 2}
    assert sum(ws.SMALL.values()) < 0.5   # everything else is under half a bucket

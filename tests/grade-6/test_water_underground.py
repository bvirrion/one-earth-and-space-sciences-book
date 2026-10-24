"""figdata/grade-6/water_table.py: the spring, the water table and the wells."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-6"))
import water_table as wt  # noqa: E402
import region as R  # noqa: E402  (put on the path by water_table)


def test_spring_is_at_the_base_of_the_chalk():
    y = wt.spring_y()
    assert abs(wt.ground(y) - wt.chalk_base(y)) < 0.01
    assert R.unit(wt.X, y + 50, wt.ground(y + 50) - 1) == R.UNIT["chalk"]
    assert R.unit(wt.X, y - 50, wt.ground(y - 50) - 1) == R.UNIT["shale"]


def test_water_table_lies_in_the_chalk_and_below_the_ground():
    for y in range(int(wt.spring_y()) + 20, int(wt.Y1), 100):
        for k in (wt.K_WET, wt.K_DRY):
            z = wt.water_table(y, k)
            assert wt.chalk_base(y) < z < wt.ground(y)
        assert wt.water_table(y, wt.K_DRY) < wt.water_table(y, wt.K_WET)


def test_spring_above_the_river():
    assert wt.ground(wt.spring_y()) > R.river_z(wt.X)


def test_wells():
    assert wt.well_state("A") == "always"
    assert wt.well_state("B") == "wet season only"


def test_problem_numbers():
    assert wt.stored_days(100, 50, 2, 18, 18) == 100.0      # the named final number
    assert wt.volume_of_water(10000, 20) == 2000.0           # water in the pores
    assert wt.volume_of_water(10000, 18) == 1800.0           # water that drains out


def test_fresh_water_shares():
    rows = dict(wt.fresh_shares())
    assert rows["groundwater"] == 30.1 and rows["ice and permanent snow"] == 68.7
    assert round(sum(rows.values()), 6) == 100.0
    assert round(rows["groundwater"] / rows["lakes"]) == 116

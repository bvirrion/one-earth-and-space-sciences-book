"""figdata/grade-2: the simple map of the Varden Hills."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "grade-2"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "shared"))
import region  # noqa: E402
import varden_plan as vp  # noqa: E402


def test_road_crosses_the_river_once_at_the_bridge():
    b = vp.bridge()
    assert len(b) == 1
    x, y = b[0]
    assert abs(y - region.river_y(x)) < 5.0


def test_farm_village_wood_are_on_dry_ground_inside_the_map():
    for x, y in (vp.FARM, vp.VILLAGE):
        assert 0 < x < region.WIDTH and 0 < y < region.HEIGHT
        assert not vp.on_floor(x, y)
        assert region.topo(x, y) < vp.HILL_Z     # in the lowland, not on a hilltop
    for x, y in vp.wood():
        assert 0 < x < region.WIDTH and 0 < y < region.HEIGHT and not vp.on_floor(x, y)


def test_directions_used_in_the_exercises():
    # the river is north of the farm; the village is north-east of the farm
    fx, fy = vp.FARM
    assert region.river_y(fx) > fy
    vx, vy = vp.VILLAGE
    assert vx > fx and vy > fy
    assert (vx - fx, vy - fy) == (5000.0, 2000.0)   # 5 squares east, 2 north
    # the wood is east of the farm, south of the river
    assert vp.WOOD[0] > fx and vp.WOOD[1] < region.river_y(vp.WOOD[0])

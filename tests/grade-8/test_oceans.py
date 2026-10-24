"""Tests for figdata/grade-8/seafloor_profile.py and ocean_currents.py (grade 8, chapter 4)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-8"))
import ocean_currents as oc  # noqa: E402
import seafloor_profile as sp  # noqa: E402


def test_atlantic_profile_has_shelf_plains_and_ridge():
    prof = sp.profile(sp.ATLANTIC)
    assert len(prof) == 80                        # 59.5 W to 19.5 E, one point per degree
    assert prof[0][1] > 0 and prof[-1][1] > 0     # land at both ends
    plains = [z for x, z in prof if 1500 < x < 3500 or 5500 < x < 7000]
    ridge = max(z for x, z in prof if 4000 < x < 5000)
    assert min(plains) < -4500
    assert ridge > -2600                          # the ridge rises well above the plains
    assert math.isclose(sp.km_per_degree(-30.5), 95.8, abs_tol=0.1)


def test_pacific_profile_has_trench_next_to_the_andes():
    prof = sp.profile(sp.PACIFIC)
    deepest = min(prof, key=lambda p: p[1])
    highest = max(prof, key=lambda p: p[1])
    assert deepest[1] < -5000 and highest[1] > 3000
    assert 0 < highest[0] - deepest[0] < 600      # trench and mountains side by side


def test_vertical_exaggeration():
    # 1000 km over 10 cm across, 1000 m over 1 cm up: 100 km/cm against 1 km/cm
    assert math.isclose(sp.vertical_exaggeration(1000, 10, 0, 1000, 1), 100.0)


def test_gyres_turn_clockwise_north_and_anticlockwise_south():
    for g in oc.GYRES:
        sides = oc.SIDES_N if g[5] == "N" else oc.SIDES_S
        loop = []
        for _name, t0, t1 in sides:
            loop += oc.side_points(g, t0, t1, n=10)
        # put the sides in flow order: west, pole, east, equator for N; west, pole, east, equator for S
        area = oc.turning(loop)
        if g[5] == "N":
            assert area < 0, g[0]
        else:
            assert area > 0, g[0]


def test_western_side_flows_poleward_and_is_warm():
    for gname, side, warm, pts in oc.gyre_sides():
        dlat = pts[-1][1] - pts[0][1]
        north = [g for g in oc.GYRES if g[0] == gname][0][5] == "N"
        if side == "west":
            assert warm
            assert (dlat > 0) == north            # towards the pole
        if side == "east":
            assert not warm
            assert (dlat < 0) == north            # towards the equator


def test_wrapping_cuts_at_the_dateline():
    pieces = oc.split_wrapped([(170.0, 0.0), (179.0, 0.0), (181.0, 0.0), (190.0, 0.0)])
    assert len(pieces) == 2 and pieces[1][0][0] == -179.0


def test_buoy_journey():
    legs = oc.rounded_legs()
    assert [k for k, *_ in legs] == ["A", "B", "C", "D"]
    assert 40 <= legs[0][3] <= 120                # Gulf Stream leg inside the sourced range
    days = sum(d for *_r, d in legs)
    assert math.isclose(days, 603.0)
    assert round(days / 30.0, 1) == 20.1
    route_start = oc.BUOY_LEGS[0][3][0]
    route_end = oc.BUOY_LEGS[-1][3][-1]
    assert route_start == route_end               # a closed loop

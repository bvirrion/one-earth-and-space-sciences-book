"""Tests for figdata/grade-9/projections.py, varden_topo.py and
trilateration.py (grade 9, chapter 5)."""
import math
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "grade-9"))
import projections as pj  # noqa: E402
import trilateration as tl  # noqa: E402
import varden_topo as vt  # noqa: E402


# ----------------------------------------------------------------- projections
def test_areas_of_greenland_and_africa():
    p = pj.areas()
    assert 2.0 < p["greenland_Mkm2"] < 2.3          # about 2.1 million km2
    assert 29.0 < p["africa_Mkm2"] < 30.5           # the mainland, about 29 million km2
    assert 13 < p["true_ratio"] < 15                # "about 14 times"
    # on the Mercator map the two look about the same size
    assert 0.8 < p["mercator_ratio"] < 1.2
    # an equal-area map keeps the true ratio
    assert abs(p["mollweide_ratio"] - p["true_ratio"]) < 0.05 * p["true_ratio"]


def test_africa_is_cut_at_suez_and_reaches_the_cape():
    a = pj.africa()
    lats = [q[1] for q in a]
    lons = [q[0] for q in a]
    assert min(lats) < -34.5 and max(lats) < 38
    assert max(lons) < 52 and min(lons) > -18


def test_mercator_area_factor():
    assert abs(pj.mercator_area_factor(0) - 1) < 1e-12
    assert abs(pj.mercator_area_factor(60) - 4) < 1e-9
    # the drawn circles at 60 degrees are about 4 times the area of those at the equator
    eq = pj.plane_area([pj.mercator(*q) for q in pj.small_circle(0, 0, 3)])
    hi = pj.plane_area([pj.mercator(*q) for q in pj.small_circle(0, 60, 3)])
    assert 3.8 < hi / eq < 4.3


def test_mollweide_keeps_the_circles_equal():
    eq = pj.plane_area([pj.mollweide(*q) for q in pj.small_circle(0, 0, 7)])
    hi = pj.plane_area([pj.mollweide(*q) for q in pj.small_circle(60, 60, 7)])
    assert abs(hi / eq - 1) < 0.02


# ----------------------------------------------------------------- the map
def test_footpath_legs_only_climb_or_descend():
    pts = [p for _n, p in vt.path_points()]
    for a, b in zip(pts, pts[1:]):
        assert vt.leg_is_monotonic(a, b)


def test_footpath_numbers_printed_in_the_problem():
    p = vt.problem()
    assert round(p["z_S"]) == 296 and round(p["z_B"]) == 143
    assert round(p["z_W"]) == 335 and round(p["z_T"]) == 544
    assert round(p["leg_SB_cm"], 1) == 3.6 and round(p["leg_BW_cm"], 1) == 2.5
    assert round(p["leg_WT_cm"], 2) == 2.35
    assert round(p["length_km"], 1) == 4.2
    assert p["climb_m"] == 401 and p["descent_m"] == 153


def test_the_bridge_is_on_the_river_floor():
    (_n, (x, y)) = vt.path_points()[1]
    assert abs(vt.z(x, y) - (170 - 0.007 * x * 1000)) < 1e-6


def test_profile_crossings_agree_with_the_ground():
    for s, lv in vt.crossings():
        x, y = vt.C[0], vt.C[1] + s
        assert abs(vt.z(x, y) - lv) < 2.0


def test_contour_labels_sit_on_their_contour():
    for x, y, lv in vt.contour_labels():
        assert abs(vt.z(x, y) - lv) < 2.0


# ----------------------------------------------------------------- positioning
def test_three_distances_fix_the_position():
    r = tl.distances()
    assert (r["A"], r["B"], r["C"]) == (5.0, 10.0, 5.0)
    pos, false = tl.locate()
    assert math.hypot(pos[0] - 4, pos[1] - 3) < 1e-9
    # the false point is on circles A and B but far off circle C
    assert abs(tl.dist(false, tl.BEACONS["A"]) - 5) < 1e-9
    assert abs(tl.dist(false, tl.BEACONS["B"]) - 10) < 1e-9
    assert abs(tl.dist(false, tl.BEACONS["C"]) - 5) > 3


def test_travel_time_from_a_gps_satellite():
    assert 0.067 < tl.travel_time_s() < 0.068

"""Tests for the atmospheric-circulation figures: the angular-momentum wind, the
invented weather map with its geostrophic winds, and the zonal-mean circulation of the
reanalysis."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import angular_momentum_wind as amw  # noqa: E402
import weather_map as wm  # noqa: E402
import general_circulation as gc  # noqa: E402


# ------------------------------------------------------------ angular momentum
def test_angular_momentum_wind():
    assert amw.u_closed(0.0) == 0.0
    assert round(amw.u_closed(30.0)) == 134
    assert abs(amw.OMEGA - 7.2921e-5) < 1e-8
    # the closed form equals the conservation law applied directly
    for lat in (5.0, 15.0, 30.0, 40.0):
        assert abs(amw.u_ring(lat) - amw.u_closed(lat)) < 1e-9
    # a ring starting at 10 deg with no wind reaches less at 30 deg
    assert amw.u_ring(30.0, lat0=10.0) < amw.u_closed(30.0)


# ------------------------------------------------------------ weather map
def test_geostrophic_wind_is_along_the_isobars():
    for x, y in ((-1200.0, 200.0), (0.0, -200.0), (800.0, 600.0)):
        u, v = wm.geostrophic(x, y)
        gx, gy = wm.gradient(x, y)
        assert abs(u * gx + v * gy) < 1e-9 * (abs(gx) + abs(gy) + 1)


def test_low_pressure_on_the_left_in_the_north():
    """Northern Hemisphere: looking downwind, the pressure falls to the left."""
    for x, y in ((-1200.0, 200.0), (0.0, -200.0), (400.0, 600.0), (1200.0, -1000.0)):
        u, v = wm.geostrophic(x, y)
        s = math.hypot(u, v)
        lx, ly = -v / s, u / s                       # unit vector to the left of the wind
        assert wm.pressure(x + 20 * lx, y + 20 * ly) < wm.pressure(x - 20 * lx, y - 20 * ly)


def test_cyclone_turns_anticlockwise_and_speed_formula():
    xl, yl = wm.LOW[:2]
    u, v = wm.geostrophic(xl + 300.0, yl)            # east of the low: wind from the south
    assert v > 0 and abs(u) < abs(v)
    gx, gy = wm.gradient(xl + 300.0, yl)
    f = wm.coriolis(wm.latitude(yl))
    assert abs(math.hypot(u, v) - math.hypot(gx, gy) / (wm.RHO * f)) < 1e-9
    assert abs(wm.RHO - 1.225) < 0.001


def test_barb_direction_convention():
    # a wind blowing towards the north comes FROM the south (180 deg)
    assert abs(wm.from_azimuth(0.0, 5.0) - 180.0) < 1e-9
    assert abs(wm.from_azimuth(5.0, 0.0) - 270.0) < 1e-9


# ------------------------------------------------------------ reanalysis circulation
def test_hadley_cells_and_edges():
    v = dict(gc.values())
    assert 5 < v["hadleyN_ann"] < 15 and -15 < v["hadleyS_ann"] < -5
    edges = [x for k, x in gc.values() if k.startswith("edges500_ann_")]
    near = [e for e in edges if 25 < abs(e) < 40]
    assert len(near) == 2                            # the poleward edges of the two Hadley cells
    # the winter cell is the stronger
    assert v["hadley_main_djf"] > 2 * v["hadleyN_ann"]


def test_jets_and_surface_winds():
    v = dict(gc.values())
    assert v["jetN_djf"] > v["jetN_jja"] and v["jetS_jja"] > v["jetS_djf"]
    assert v["usfc_ann_15"] < 0 and v["usfc_ann_-15"] < 0          # trade winds (easterly)
    assert v["usfc_ann_45"] > 0 and v["usfc_ann_-45"] > 0          # westerlies
    assert 25 < v["slp_maxN_lat"] < 45 and -45 < v["slp_maxS_lat"] < -25


def test_itcz_migrates_north_in_boreal_summer():
    it = dict(gc.itcz())
    assert it[8] > 5 and it[2] < 0

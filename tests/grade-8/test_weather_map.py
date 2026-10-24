"""Tests for figdata/grade-8/weather_map.py (grade 8, chapter 3)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-8"))
import weather_map as wm  # noqa: E402


def test_centres_are_a_low_and_a_high():
    lo, hi = wm.centre_values()
    assert 978 < lo < 982          # a deep-ish low, below 980--1000 "moderate"
    assert hi > 1020               # a typical high is around 1020 hPa or more
    for dx, dy in ((150, 0), (0, 150), (-150, 0), (0, -150)):
        assert float(wm.pressure(wm.LOW[0] + dx, wm.LOW[1] + dy)) > lo
        assert float(wm.pressure(wm.HIGH[0] + dx, wm.HIGH[1] + dy)) < hi


def test_isobars_every_4_hpa():
    xs, ys, field = wm.grid(40.0)
    levs = wm.levels(field)
    assert all(abs(b - a - 4.0) < 1e-9 for a, b in zip(levs, levs[1:]))
    assert all(lv % 4 == 0 for lv in levs)


def test_winds_turn_anticlockwise_around_the_low():
    # north of the low the wind blows towards the west, east of it towards the north
    u, v = wm.wind(wm.LOW[0], wm.LOW[1] + 300)
    assert u < 0
    u, v = wm.wind(wm.LOW[0] - 300, wm.LOW[1])
    assert v < 0                    # west of the low: towards the south
    # clockwise around the high: north of it towards the east
    u, v = wm.wind(wm.HIGH[0], wm.HIGH[1] + 300)
    assert u > 0


def test_wind_turned_towards_the_low():
    x, y = wm.LOW[0], wm.LOW[1] + 300
    u, v = wm.wind(x, y)
    # component towards the low (southwards) is positive
    assert v < 0


def test_cold_front_symbols_point_east():
    line = wm.cold_front()
    (x0, y0), (x1, y1) = line[10], line[11]
    left = (-(y1 - y0), x1 - x0)    # the style draws symbols on the left
    assert left[0] > 0              # towards the east, the way the front moves


def test_warm_front_symbols_point_north_east():
    line = wm.warm_front()
    (x0, y0), (x1, y1) = line[10], line[11]
    left = (-(y1 - y0), x1 - x0)
    assert left[0] > 0 and left[1] > 0


def test_town_in_warm_sector_and_arrival():
    tx, ty = wm.town()
    assert tx > wm.front_x_at(ty)                       # east of the cold front
    # south of the warm front at the town's x
    w = wm.warm_front(400)
    yw = min(w, key=lambda p: abs(p[0] - tx))[1]
    assert ty < yw
    assert wm.hhmm(wm.arrival_hour()) == "13:30"
    assert math.isclose(wm.front_x_at(ty) - wm.front_x_at(ty, -3 * wm.SPEED_KMH), 120.0, abs_tol=1e-6)


def test_wind_at_town_from_south_west():
    u, v = wm.wind(*wm.town())
    frm = math.degrees(math.atan2(-u, -v)) % 360
    assert 200 < frm < 250

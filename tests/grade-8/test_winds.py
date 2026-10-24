"""Tests for figdata/grade-8/trade_route.py and sunlight_spread.py (chapter g8.2)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-8"))
import sunlight_spread as L  # noqa: E402
import trade_route as T  # noqa: E402


def test_spread():
    assert L.spread(0) == 1.0
    assert abs(L.spread(60) - 2.0) < 1e-12
    assert round(L.share(60)) == 50 and round(L.share(30)) == 87


def test_ports_from_natural_earth():
    pl = T.places()
    a, b = pl[T.FROM], pl[T.TO]
    assert 14 < a[1] < 16 and -24 < a[0] < -23          # Praia
    assert 13 < b[1] < 14 and -60 < b[0] < -59          # Bridgetown


def test_great_circle_known_cases():
    # a quarter of a meridian, and one degree along the equator
    assert abs(T.great_circle((0, 0), (0, 90)) - math.pi * T.R_EARTH / 2) < 1e-6
    assert abs(T.great_circle((0, 0), (1, 0)) - T.km_per_degree_lat()) < 1e-6
    assert abs(T.km_per_degree_lon(60) - T.km_per_degree_lat() / 2) < 1e-9


def test_route_and_estimate():
    pl = T.places()
    a, b = pl[T.FROM], pl[T.TO]
    gc = T.great_circle(a, b)
    assert 3850 < gc < 3950
    # the school estimate along the parallel is a little longer, never shorter
    assert gc <= T.along_parallel(a, b) < gc * 1.01
    pts = T.route_points(a, b)
    assert abs(pts[0][0] - a[0]) < 1e-9 and abs(pts[0][1] - a[1]) < 1e-9
    assert abs(pts[-1][0] - b[0]) < 1e-9 and abs(pts[-1][1] - b[1]) < 1e-9
    # the pieces of the route add up to the great circle
    tot = sum(T.great_circle(p, q) for p, q in zip(pts, pts[1:]))
    assert abs(tot - gc) < 1e-6


def test_days_and_arrows():
    assert T.SPEED_KMH * 24 == 168
    pl = T.places()
    d = T.days(T.great_circle(pl[T.FROM], pl[T.TO]))
    assert 23 < d < 23.5
    rings = T.land_rings()
    arrows = T.trade_arrows()
    assert len(arrows) > 15
    for lon, lat, dx, dy in arrows:
        assert dx < 0 and dy < 0                       # towards the south-west
        assert not T.on_land((lon, lat), rings)

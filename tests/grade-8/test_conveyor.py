"""Tests for figdata/grade-8/conveyor.py (chapter g8.4: the ocean conveyor belt)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-8"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "shared"))
import conveyor as C  # noqa: E402
import geo  # noqa: E402


def test_the_loop_stays_at_sea():
    rings = geo.land_rings()
    for pts in (C.SURFACE, C.DEEP):
        for p in C.spline(pts):
            assert C.in_island_box(p) or not C.on_land(p, rings), p
    assert not C.on_land(C.SINK, rings) and not C.on_land(C.RISE, rings)


def test_route_order_follows_the_ledger():
    # warm water goes north in the Atlantic and sinks in the far north;
    # the deep water starts there and goes south to the Southern Ocean
    assert C.SURFACE[-1][1] > 55 and C.DEEP[0][1] > 55
    assert min(lat for _l, lat in C.DEEP) < -50
    # the surface branch passes south of Africa (Cape of Good Hope, 34.4 S)
    assert any(10 < lon < 25 and lat < -35 for lon, lat in C.SURFACE)


def test_numbers_printed_in_the_example():
    n = C.numbers()
    assert 67500 < n["loop_km"] < 75000           # "roughly 70 000 km"
    assert 180 < n["deep_m_per_day"] < 210        # "about 200 m a day"
    assert round(n["gulf_km_per_day"]) == 154     # "about 150 km in a day"
    hours = n["deep_km_per_year"] / C.GULF_KM_H
    assert 10.5 < hours < 11.7                    # "in about 11 hours"

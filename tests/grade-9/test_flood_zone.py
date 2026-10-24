"""Tests for figdata/grade-9/flood_zone.py (grade 9, chapter 2)."""
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "grade-9"))
import flood_zone as fz  # noqa: E402
import region as rg  # noqa: E402


def test_the_floor_is_flooded_and_the_zone_grows_with_the_flood():
    for x in (3600.0, 5000.0, 6800.0):
        assert fz.in_zone(x, rg.river_y(x))
        assert fz.edge(x, +1) >= rg.FLOOR_HALF and fz.edge(x, -1) >= rg.FLOOR_HALF
        assert fz.edge(x, +1, h=10.0) > fz.edge(x, +1, h=5.0) > fz.edge(x, +1, h=2.0)


def test_zone_edge_is_at_the_flood_height():
    x = 5000.0
    for side in (+1, -1):
        y = rg.river_y(x) + side * fz.edge(x, side)
        assert abs(fz.height_above_river(x, y) - fz.H_FLOOD) < 0.01


def test_zone_polygon_is_closed_and_contains_the_river():
    poly = fz.zone_polygon()
    assert poly[0] == poly[-1]
    n = (len(poly) - 1) // 2
    for (x, yn), (_x2, ys) in zip(poly[:n], reversed(poly[n:-1])):
        assert ys < rg.river_y(x) < yn


def test_house_count():
    assert len(fz.HOUSES) == 28
    assert len(fz.houses_in_zone()) == 17
    for (x, d) in fz.HOUSES:                     # no house sits on the edge of the zone
        e = fz.edge(x, 1 if d > 0 else -1)
        assert abs(abs(d) - e) >= 60.0


def test_school_sites():
    st = {s[0]: s for s in fz.site_table()}
    assert st["A"][6] and not st["B"][6] and not st["C"][6]          # only A in the flood zone
    assert st["B"][5] < 100 and st["B"][4] > 30                      # B: on the fault, steep
    assert st["C"][5] > 1000 and st["C"][4] < 12 and st["C"][3] > 50  # C: far, gentle, high


def test_fault_trace_is_read():
    tr = fz.fault_trace()
    assert len(tr) > 10
    assert fz.distance_to_fault(*tr[5]) < 1.0

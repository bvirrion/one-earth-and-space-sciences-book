"""Tests for figdata/grade-8/sea_ice.py and glacier_retreat.py (grade 8, chapter 5)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-8"))
import glacier_retreat as gr  # noqa: E402
import sea_ice as si  # noqa: E402


def test_sea_ice_series_is_complete_and_shrinking():
    s = si.series()
    assert [y for y, _ in s] == list(range(1979, 2026))      # 47 Septembers, none missing
    assert all(2.5 < v < 8.5 for _, v in s)                   # million km2
    assert min(s, key=lambda p: p[1])[0] == 2012              # the record low
    assert si.decade_mean(s, 2010) < si.decade_mean(s, 1980) - 2


def test_sea_ice_trend():
    a, b = si.fit(si.series())
    assert math.isclose(10 * a, -0.76, abs_tol=0.01)          # million km2 per decade
    # the fit on an exact line returns that line
    a2, b2 = si.fit([(x, 3 - 0.5 * x) for x in range(10)])
    assert math.isclose(a2, -0.5) and math.isclose(b2, 3)


def test_glacier_positions_retreat_every_decade():
    years = [y for y, _ in gr.POSITIONS]
    assert years == list(range(1960, 2021, 10))
    assert all(r > 0 for _, r in gr.retreat_per_decade())
    assert sum(r for _, r in gr.retreat_per_decade()) == 1080


def test_glacier_rate_and_year_at_hut():
    assert gr.average_rate() == 18.0
    assert gr.year_at_hut() == 2070.0


def test_glacier_tongue_bulges_down_the_valley():
    pts = gr.arc(500)
    middle = min(pts, key=lambda p: abs(p[0]))
    assert middle[1] == 500 and pts[0][1] > middle[1] and pts[-1][1] > middle[1]
    # the walls stay outside the ice and the valley widens downwards
    for side in (-1, 1):
        w = gr.wall(side)
        assert all(abs(x) > gr.HALF_WIDTH for x, _ in w)
        assert abs(w[0][0]) > abs(w[-1][0])


def test_ice_polygon_starts_at_the_last_front():
    poly = gr.ice(1080)
    assert min(y for _, y in poly) == 1080
    assert len(gr.floor()) == 2 * len(gr.wall(1))

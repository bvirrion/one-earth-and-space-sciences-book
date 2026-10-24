"""figdata/grade-11/gnss_series.py: rates fitted to two station time series."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import gnss_series as gs  # noqa: E402


def test_fit_recovers_a_line():
    t = [2000 + 0.1 * k for k in range(50)]
    a, b = gs.fit(t, [3.0 + 7.0 * x for x in t])
    assert abs(b - 7.0) < 1e-9


def test_mauna_kea_moves_about_seven_cm_toward_the_north_west():
    be, bn, sc = gs.rates("mkea")
    assert -66 < be < -60 and 31 < bn < 38
    assert sc < 10


def test_wettzell_moves_about_two_and_a_half_cm_toward_the_north_east():
    be, bn, sc = gs.rates("wtzr")
    assert 18 < be < 23 and 13 < bn < 18
    assert sc < 5


def test_series_are_long_and_monthly():
    for site in gs.SITES:
        s = gs.series(site)
        assert len(s) > 300 and s[-1][0] - s[0][0] > 29
        assert s[0][1] == 0 and s[0][2] == 0

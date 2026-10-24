"""Tests for figdata/grade-8/rain_by_belt.py (chapter g8.2: four towns, four belts)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-8"))
import rain_by_belt as R  # noqa: E402


def test_each_town_in_the_belt_the_text_gives():
    belts = {n: b for _lat, _t, n, b in R.stations()}
    assert belts == {"Hilo": "trade winds", "Phoenix": "westerlies",
                     "Seattle": "westerlies", "Utqiagvik": "polar easterlies"}


def test_yearly_totals_printed_in_the_example():
    tot = {n: t for _lat, t, n, _b in R.stations()}
    assert 3000 < tot["Hilo"] < 3100          # "about 3 000 mm"
    assert tot["Phoenix"] < 200               # "under 200 mm"
    assert 950 < tot["Seattle"] < 1050        # "about 1 000 mm"
    assert tot["Utqiagvik"] < 150             # "less than 150 mm"
    assert tot["Hilo"] > 15 * tot["Phoenix"]

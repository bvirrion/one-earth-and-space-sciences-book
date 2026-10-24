"""Tests for figdata/grade-8/barogram.py (chapter g8.3: a barometer's record)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-8"))
import barogram as B  # noqa: E402


def test_story_of_the_record():
    s = B.summary()
    assert 6 <= s["max_hour"] <= 10 and 1029 < s["max_hPa"] < 1033      # the anticyclone, about 1031 hPa
    assert s["warm_hour"] < s["cold_hour"]                              # the warm front passes first
    assert abs(s["min_hour"] - s["cold_hour"]) < 1.5                    # lowest at the cold front
    assert 984 < s["min_hPa"] < 988                                     # about 986 hPa
    assert 43 < s["fall_hPa"] < 48                                      # "about 45 hPa"
    assert s["end_hPa"] > s["min_hPa"] + 20                             # rises behind the front


def test_pressure_falls_all_the_way_from_the_high_to_the_cold_front():
    s = B.summary()
    tr = [p for h, p in B.trace() if s["max_hour"] <= h <= s["min_hour"]]
    assert all(b <= a + 0.05 for a, b in zip(tr, tr[1:]))


def test_fastest_fall_before_the_warm_front_slower_behind_it():
    s = B.summary()
    tr = B.trace()
    slopes = [((h0 + h1) / 2, (p1 - p0) / (h1 - h0)) for (h0, p0), (h1, p1) in zip(tr, tr[1:])]
    h_fast = min(slopes, key=lambda r: r[1])[0]
    assert s["warm_hour"] - 8 < h_fast < s["warm_hour"]              # "a few hours before"
    before = (B.p_at(s["warm_hour"]) - B.p_at(s["warm_hour"] - 10)) / 10
    after = (B.p_at(s["warm_hour"] + 10) - B.p_at(s["warm_hour"])) / 10
    assert after > before                                            # falls more slowly behind it

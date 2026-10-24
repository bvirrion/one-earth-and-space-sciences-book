"""Tests for figdata/bachelor-2/climvar.py (ch. 23 climate-variability)."""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "bachelor-2"))
import climvar as cv  # noqa: E402


def test_episode_rule_counts_five_seasons_and_flags_a_running_one():
    s = [("X", 2000, v) for v in (0.0, 0.5, 0.6, 0.7, 0.8, 0.5, 0.4, 0.5, 0.6, 0.7, 0.8, 0.0,
                                  -0.5, -0.6, -0.7, -0.8, -0.9)]
    en = cv.episodes(s, 1)
    assert [e["n"] for e in en] == [5]
    assert en[0]["peak"][2] == 0.8 and not en[0]["running"]
    ln = cv.episodes(s, -1)
    assert [e["n"] for e in ln] == [5] and ln[0]["running"]
    assert cv.episodes(s[:5], 1) == []


def test_season_time_is_the_middle_month():
    assert abs(cv.season_time("DJF", 1997) - (1997 + 0.5 / 12)) < 1e-12
    assert abs(cv.season_time("NDJ", 1997) - (1997 + 11.5 / 12)) < 1e-12


def test_table_is_the_text_file_rounded_to_one_decimal():
    a, b = cv.table(), cv.read_index("bachelor-2-oni")
    assert len(a) == len(b) and all(x[:2] == y[:2] for x, y in zip(a, b))
    assert max(abs(x[2] - y[2]) for x, y in zip(a, b)) <= 0.0501


def test_oni_is_the_three_month_mean_of_the_monthly_nino34_anomaly():
    m = {}
    with open(os.path.join(cv.DERIVED, "bachelor-2-nino34.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            m[(int(r["year"]), int(r["month"]))] = float(r["anom_C"])
    worst = 0.0
    for s, y, a in cv.read_index("bachelor-2-oni"):
        k = cv.SEASONS.index(s) + 1
        mon = []
        for off in (-1, 0, 1):
            mm, yy = k + off, y
            if mm < 1:
                mm, yy = mm + 12, yy - 1
            if mm > 12:
                mm, yy = mm - 12, yy + 1
            mon.append((yy, mm))
        worst = max(worst, abs(sum(m[x] for x in mon) / 3 - a))
    assert worst < 0.015


def test_strong_el_ninos_and_their_mean_interval():
    en = cv.episodes(cv.table(), 1)
    starts, gaps = cv.strong_intervals(en)
    assert len(starts) == 11
    assert abs(sum(gaps) / len(gaps) - 6.9) < 1e-9
    peaks = sorted(e["peak"][2] for e in en)
    assert peaks[-1] == 2.6


def test_damping_time_and_red_noise_memory():
    tau = cv.tau_seconds(50.0) / cv.DAY
    assert abs(tau - 147.07) < 0.05
    x = cv.red_noise(int(500 * 365.25), tau, seed=7)
    assert abs(float(x.std()) - 0.5) < 0.03
    r = cv.acf(x, [int(round(cv.MONTH)), int(round(3 * cv.MONTH))])
    assert abs(r[0] - math.exp(-cv.MONTH / tau)) < 0.03
    assert abs(r[1] - math.exp(-3 * cv.MONTH / tau)) < 0.05


def test_nao_winter_is_the_dec_jan_feb_mean():
    w = cv.nao_winters()
    assert 1951 in w and 1950 not in w
    assert abs(w[2010] - (-1.673)) < 0.001
    assert min(w.values()) == w[2010]

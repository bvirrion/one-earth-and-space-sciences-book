import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import flood_frequency as ff  # noqa: E402


def test_largest_peak_has_return_period_n_plus_one():
    p = ff.peaks()
    r = ff.ranked(p)
    n = len(p)
    assert r[0][4] == n + 1
    assert r[0][3] == max(q for _, _, q in p)
    assert r[-1][4] == (n + 1) / n
    assert [x[0] for x in r] == list(range(1, n + 1))
    assert all(a[3] >= b[3] for a, b in zip(r, r[1:]))


def test_record_is_continuous_and_matches_ledger():
    p = ff.peaks()
    years = [y for y, _, _ in p]
    assert years == list(range(1931, 2026))
    # 484000 cfs on 1936-03-19 (data:b2-usgs-potomac)
    big = max(p, key=lambda r: r[2])
    assert big[1] == "1936-03-19" and abs(big[2] - 484000 * 0.3048 ** 3) < 1


def test_chance_of_at_least_one():
    assert abs(ff.chance(100, 30) - 0.2603) < 1e-4
    assert abs(ff.chance(100, 1) - 0.01) < 1e-12
    assert ff.chance(10, 0) == 0.0

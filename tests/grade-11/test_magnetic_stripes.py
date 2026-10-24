"""figdata/grade-11/magnetic_stripes.py: symmetric profiles, boundaries at half rate x age."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import magnetic_stripes as ms  # noqa: E402


def test_profiles_are_symmetric():
    for name in ms.RATES:
        p = ms.profile(name)
        for (x1, a1), (x2, a2) in zip(p, reversed(p)):
            assert abs(x1 + x2) < 1e-9 and abs(a1 - a2) < 1e-6


def test_boundaries_at_half_rate_times_age():
    for u in ms.RATES.values():
        edges = {round(abs(e), 6) for x1, x2, _ in ms.blocks(u) for e in (x1, x2)}
        for a, b in ms.NORMAL:
            for t in (a, b):
                if 0 < t < ms.T_MAX:
                    assert round(10.0 * u * t, 6) in edges
        assert ms.polarity(0.1) == 1 and ms.polarity(0.9) == -1 and ms.polarity(1.0) == 1  # Jaramillo


def test_anomaly_sign_follows_polarity_over_wide_blocks():
    # positive above normal blocks, negative above reversed ones, where a block is
    # wider than about three times its depth
    for name, u in ms.RATES.items():
        bl = ms.blocks(u)
        for x1, x2, s in bl:
            if x2 - x1 > 10.0 and abs(x1) < 10 * u * ms.SPAN_MA:
                assert ms.anomaly(0.5 * (x1 + x2), bl) * s > 0
    # an infinite uniform sheet has no anomaly
    assert abs(ms.anomaly(0.0, [(-1e7, 1e7, 1)])) < 1e-3

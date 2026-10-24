"""figdata/grade-11/seismic_rays.py: shadow zone and travel times against observation."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import seismic_rays as sr  # noqa: E402

N = sr.numbers()


def test_p_shadow_zone_close_to_gutenbergs():
    # observed (ledger kayal:shadow): about 105 to 143 degrees
    assert 97.0 < N["shadow_start_deg"] < 106.0
    assert 141.0 < N["shadow_end_pkp_deg"] < 146.0


def test_s_waves_never_cross_the_core():
    assert all(not b[4] for b in sr.branches("S", 600))
    assert N["s_direct_max_deg"] < 106.0


def test_travel_times_close_to_the_empirical_ak135_times():
    # ledger auspass:surftim: P 608.2 s and S 1101.3 s at 60 degrees, P 370.3 s at 30
    assert abs(N["p_60_s"] / 608.2 - 1) < 0.02
    assert abs(N["s_60_s"] / 1101.3 - 1) < 0.02
    assert abs(N["p_30_s"] / 370.3 - 1) < 0.02


def test_ray_parameter_is_the_slope_of_the_travel_time_curve():
    # dT/d(delta) = p (s per radian) on the direct branch
    import math
    p = sr.p_for_delta(50.0)
    d1, t1 = sr.trace(p * 1.0005)[:2]
    d2, t2 = sr.trace(p * 0.9995)[:2]
    slope = (t2 - t1) / math.radians(d2 - d1)
    assert abs(slope / p - 1) < 0.01


def test_vertical_ray_time_is_the_sum_of_shell_times():
    r = sr.trace(0.0)
    assert abs(r[0] - 180.0) < 1e-9             # straight through the centre to the antipode
    t = sum((a - b) / v for a, b, v in sr.SHELLS["P"])
    assert abs(r[1] - 2 * t) < 1e-6


def test_observed_table_matches_the_ledger_row():
    import re
    led = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "ledger", "book2.md")
    with open(led, encoding="utf8") as f:
        line = next(l for l in f if l.startswith("| auspass:surftim |"))
    for d, (p, s) in sr.OBSERVED.items():
        m = re.search(r"\b%d(?: deg)? P ([\d.]+)(?: S ([\d.]+))?" % d, line)
        assert m, d
        assert float(m.group(1)) == p
        assert (float(m.group(2)) if m.group(2) else None) == s


def test_model_follows_every_observed_time():
    for d, (p, s) in sr.OBSERVED.items():
        assert abs(sr.time_at(float(d), "P") / p - 1) < 0.02
        if s:
            assert abs(sr.time_at(float(d), "S") / s - 1) < 0.02

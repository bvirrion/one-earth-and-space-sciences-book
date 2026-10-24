"""Tests for figdata/grade-7/quake_counts.py and epicentre.py (chapter g7.3)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-7"))
import epicentre as E  # noqa: E402
import quake_counts as Q  # noqa: E402


def test_counts_add_up_and_printed_values():
    c = dict(Q.counts())
    assert sum(c.values()) == 7031
    assert c == {6: 6335, 7: 656, 8: 38, 9: 2}
    assert round(Q.per_year(c[6])) == 127 and round(Q.per_year(c[7])) == 13


def test_about_ten_times_fewer_per_step():
    c = dict(Q.counts())
    for a, b in ((6, 7), (7, 8)):
        assert 8 <= c[a] / c[b] <= 18


def test_magnitude_class_edges():
    assert Q.magnitude_class("6.0") == 6 and Q.magnitude_class("6.99") == 6
    assert Q.magnitude_class("9.5") == 9 and Q.magnitude_class("7.0") == 7


def test_most_foci_are_shallow():
    n, k, p = Q.shallow_share()
    assert (n, k) == (7031, 5561) and round(p) == 79
    assert Q.deep() == (483, 688.0)


def test_tsunami_2004_times():
    t = {name: (d, h) for name, d, h in Q.tsunami_times()}
    assert round(t["Colombo"][0], -1) == 1830
    assert 2.2 < t["Colombo"][1] < 2.4
    assert t["Malé"][1] > t["Colombo"][1]


def test_crust_rule_brackets_eight():
    k = [r[3] for r in E.crust_rule()]
    assert len(k) == 2 and k[0] < E.KM_PER_S < k[1]
    assert round(k[0], 1) == 7.1 and round(k[1], 1) == 9.1


def test_method_example_is_exact():
    for n, x, y, d, t in E.stations(E.M_EPI, E.M_STATIONS):
        assert d == int(d)
    lx, ly = E.locate([(x, y, d) for n, x, y, d, t in E.stations(E.M_EPI, E.M_STATIONS)])
    assert abs(lx) < 1e-6 and abs(ly) < 1e-6


def test_problem_delays_are_whole_seconds_and_locate_back():
    st = E.stations(E.P_EPI, E.P_STATIONS)
    assert [round(t, 6) for *_, t in st] == [20.0, 13.0, 15.0]
    lx, ly = E.locate([(x, y, d) for n, x, y, d, t in st])
    assert abs(lx - 120) < 1e-6 and abs(ly - 90) < 1e-6


def test_stations_on_land_epicentre_at_sea():
    rings = E.coasts()
    land = lambda p: any(E.on_land(p, r) for r in rings)  # noqa: E731
    for n, x, y in E.P_STATIONS:
        assert land((x, y)), n
    assert not land(E.P_EPI)
    # the town stands on the island's shore: within 2 km of its ring
    island = rings[2]
    assert min(E.dist((E.P_TOWN[1], E.P_TOWN[2]), p) for p in island) < 2.0


def test_problem_final_number():
    assert E.dist(E.P_EPI, (E.P_TOWN[1], E.P_TOWN[2])) == 240.0
    assert E.tsunami_minutes() == 18.0
    assert E.minutes_left() == 13.0


def test_trace_is_reproducible_and_s_arrives_later():
    t1, v1 = E.trace(10.0)
    t2, v2 = E.trace(10.0)
    assert (v1 == v2).all()
    quiet = abs(v1[t1 < 9.5]).max()
    p_part = abs(v1[(t1 > 10) & (t1 < 19.5)]).max()
    s_part = abs(v1[(t1 > 20) & (t1 < 25)]).max()
    assert quiet < p_part < s_part

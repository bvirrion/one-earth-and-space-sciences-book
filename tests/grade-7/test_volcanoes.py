"""Tests for figdata/grade-7/volcano_settings.py (chapter g7.2, volcanoes)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-7"))
import volcano_settings as V  # noqa: E402


def test_every_volcano_has_one_setting():
    data = V.rows()
    c = V.counts(data)
    assert sum(n for _, _, n, _ in c) == len(data)
    assert abs(sum(p for _, _, _, p in c) - 100.0) < 1e-9


def test_printed_counts():
    c = {k: (n, round(p)) for k, _, n, p in V.counts()}
    assert c["sub"] == (838, 69)
    assert c["rift"] == (221, 18)
    assert c["intra"] == (149, 12)
    assert c["unknown"][0] == 6


def test_sinking_plates_hold_most_volcanoes():
    c = {k: n for k, _, n, _ in V.counts()}
    assert c["sub"] > c["rift"] + c["intra"]


def test_steep_cones_sit_above_sinking_plates():
    n, ns, p = V.strato_share()
    assert (n, ns) == (660, 564)
    assert round(p) == 85


def test_types_add_up():
    t = V.types_by_setting()
    c = {k: n for k, _, n, _ in V.counts()}
    for k in c:
        assert sum(t[k].values()) == c[k]


def test_hawaii_is_intraplate():
    hawaii = [r for r in V.rows() if r["name"] in ("Kilauea", "Mauna Loa")]
    assert len(hawaii) == 2
    assert all(V.setting_key(r) == "intra" for r in hawaii)


def test_mount_st_helens_and_pinatubo_above_sinking_plates():
    rows = {r["name"]: r for r in V.rows()}
    for name in ("St. Helens", "Pinatubo"):
        assert V.setting_key(rows[name]) == "sub"
        assert V.shape(rows[name]) == "strato"


def test_problem_height_lost():
    """The problem's named number: 2950 m before, 2549 m after (ledger
    usgs:msh-heights, from 9,677 ft and 8,363 ft)."""
    before, after = round(9677 * 0.3048), round(8363 * 0.3048)
    assert (before, after) == (2950, 2549)
    assert before - after == 401

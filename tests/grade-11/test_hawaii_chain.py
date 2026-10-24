"""figdata/grade-11/hawaii_chain.py: the age progression of the Hawaiian-Emperor chain."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import hawaii_chain as hc  # noqa: E402

LEDGER = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "ledger", "book2.md")


def test_speed_formula_on_exact_data():
    rows = [("x", d, d / 90.0, 0) for d in (100, 500, 2000)]
    assert abs(hc.speed_through_origin(rows) - 90.0) < 1e-9


def test_hawaiian_segment_about_nine_cm_per_year():
    assert 85 < hc.numbers()["v_hawaiian"] < 95


def test_ages_grow_with_distance_on_the_whole():
    h = hc.segment(True)
    first, last = h[: len(h) // 3], h[-len(h) // 3:]
    assert max(r[2] for r in first) < min(r[2] for r in last)


def test_table_matches_the_ledger():
    text = open(LEDGER, encoding="utf8").read()
    row = [l for l in text.splitlines() if l.startswith("| cd87:ages ")][0]
    for name, d, a, e in hc.TABLE:
        if name not in hc.EXCLUDED:
            assert "%s %d km %s+-%s" % (name, d, a, e) in row, name


def test_bend_is_between_abbott_and_daikakuji():
    assert max(r[1] for r in hc.segment(True)) < hc.BEND_KM < min(r[1] for r in hc.segment(False))

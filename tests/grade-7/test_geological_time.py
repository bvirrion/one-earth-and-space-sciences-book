"""Tests for figdata/grade-7/time_scale.py, earth_calendar.py and
varden_history.py (chapter g7.5)."""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-7"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "shared"))
import earth_calendar as C  # noqa: E402
import region as R  # noqa: E402
import time_scale as T  # noqa: E402
import varden_history as H  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")


# ---------------------------------------------------------------- time scale

def test_time_scale_reads_the_ledger():
    base, colour = T.ledger()
    text = open(os.path.join(ROOT, "sources", "data_ledger.md"), encoding="utf8").read()
    for name in T.LONG + T.ERAS + T.PERIODS:
        m = re.search(r"\|\s*ics:base\.%s\s*\|[^|]*\|\s*([0-9.]+)" % name, text)
        assert m and float(m.group(1)) == base[name]
        assert re.search(r"ics:colour\.%s\s*\|[^|]*\|\s*#%s" % (name, colour[name]), text, re.I)
    assert base["Cenozoic"] == base["Paleogene"] == 66.0
    assert base["Paleozoic"] == base["Cambrian"] == base["Phanerozoic"]


def test_spans_are_consecutive_and_end_today():
    for names in (T.LONG, T.ERAS, T.PERIODS):
        sp = T.spans(names)
        for (_, _, end), (_, start, _) in zip(sp, sp[1:]):
            assert end == start
        assert sp[-1][2] == 0.0
        assert all(s > e for _, s, e in sp)
    # the eras fill the Phanerozoic, the periods fill the eras
    assert T.spans(T.ERAS)[0][1] == T.spans(T.PERIODS)[0][1] == T.ledger()[0]["Phanerozoic"]


def test_time_scale_numbers():
    base, _ = T.ledger()
    assert T.AGE_EARTH_MA == C.AGE_EARTH_MA
    assert round(T.share(base["Hadean"], base["Paleozoic"]), 1) == 88.1
    assert round(T.share(base["Cenozoic"], 0.0), 2) == 1.45
    assert round(T.share(base["Mesozoic"], base["Cenozoic"]), 1) == 4.1
    assert round(base["Mesozoic"] - base["Cenozoic"], 1) == 185.9


# ------------------------------------------------------------------ calendar

def test_calendar_ends_and_starts():
    assert C.calendar(C.AGE_EARTH_MA) == ("January", 1, 0, 0)
    assert C.elapsed_days(0.0) == 365.0
    assert sum(C.MONTH_DAYS) == C.DAYS


def test_calendar_dates():
    assert C.calendar(4030.0) == ("February", 11, 0, 3)
    assert C.calendar(3500.0) == ("March", 25, 14, 42)
    assert C.calendar(538.8) == ("November", 18, 16, 23)
    assert C.calendar(66.0) == ("December", 26, 16, 39)


def test_one_day_and_our_species():
    assert round(C.myr_per_day(), 2) == 12.44
    m = C.minutes_before_midnight(C.HOMO_SAPIENS_MA)
    assert round(m, 1) == 34.7
    # 31 December, 24:00 minus 35 minutes = 23:25
    assert C.calendar(C.HOMO_SAPIENS_MA) == ("December", 31, 23, 25)


# ------------------------------------------------------- the region's history

def test_section_crosses_granite_fault_and_cover():
    ss, zs, codes, ground = H.section()
    present = H.units_present(codes)
    for name in ("schist", "granite", "sandstone", "limestone", "shale", "chalk"):
        assert name in present
    (s0, z0), (s1, z1) = H.fault_line()
    assert 0 < s0 < R.WIDTH and 0 < s1 < R.WIDTH
    assert z0 == H.ZMIN and abs(z1 - R.topo(s1, H.Y)) < 0.01     # it stops at the ground
    assert s1 < s0          # the fault dips to the east: lower down, further east
    # each point of the drawn trace is on the fault plane
    ux, uy = R._fault_u()
    import math
    fx, fy, fz = R.FAULT_POINT
    for s, z in ((s0, z0), (s1, z1)):
        assert abs((s - fx) * ux + (H.Y - fy) * uy + (z - fz) / math.tan(math.radians(R.FAULT_DIP))) < 1e-6


def test_unconformity_lies_on_schist_or_granite():
    lines = H.base_line()
    assert lines
    for ln in lines:
        for s, z in ln[1:-1:5]:
            assert R.unit(s, H.Y, z - 3.0, with_alluvium=False) in (R.UNIT["schist"], R.UNIT["granite"])
            assert R.unit(s, H.Y, z + 3.0) == R.UNIT["sandstone"]


def test_events_follow_the_region_ages():
    ages = {u[1]: u[4] for u in R.UNITS}
    order = [k for k, *_ in H.EVENTS]
    assert order[:2] == ["schist", "granite"] and ages["schist"] > ages["granite"]
    assert ages["granite"] > ages["sandstone"] > ages["limestone"] > ages["shale"] > ages["chalk"]
    assert order.index("erosion") < order.index("cover") < order.index("folding") < order.index("fault")


def test_bars_and_labels():
    base, _ = T.ledger()
    r = T.ring(base["Jurassic"], base["Cretaceous"])
    assert r[0] == r[-1] and len(r) == 5
    assert {a for a, _ in r} == {base["Jurassic"], base["Cretaceous"]}
    assert T.middle(201.4, 143.1) == (201.4 + 143.1) / 2


def test_calendar_tags():
    assert C.tag("{oldest rocks found}", 4030.0) == "{11 February: oldest rocks found}"
    assert C.tag("{the dinosaurs are gone}", 66.0) == "{26 December: the dinosaurs are gone}"

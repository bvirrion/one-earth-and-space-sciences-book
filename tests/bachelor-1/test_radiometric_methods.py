"""Tests for the radiometric-methods figures: the decay curves, the least-squares
isochron and the IntCal20 calibration curve."""
import csv
import math
import os
import random
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import decay_curves as dc  # noqa: E402
import isochron as iso  # noqa: E402
import radiocarbon as rc  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")


def test_parent_plus_daughter_is_conserved():
    for i in range(0, 101):
        n = i / 20.0
        assert abs(dc.parent(n) + dc.daughter(n) - 1.0) < 1e-12
    assert [dc.ratio(n) for n in range(4)] == [0.0, 1.0, 3.0, 7.0]


def test_decay_law_matches_the_growth_equation():
    # D*/P = e^(lambda t) - 1 with lambda = ln 2 / T
    for n in (0.5, 1.0, 2.7):
        assert abs(dc.ratio(n) - math.expm1(math.log(2.0) * n)) < 1e-12


def test_rb_constant_is_the_ledger_value():
    led = open(os.path.join(ROOT, "sources", "ledger", "book2.md"), encoding="utf8").read()
    led += open(os.path.join(ROOT, "sources", "ledger", "book3.md"), encoding="utf8").read()
    assert re.search(r"\| villa22:rb87 \|[^|]*1\.3972e-11", led)
    assert iso.LAMBDA_RB == 1.3972e-11


def test_slope_and_age_are_inverse():
    for age in (1.0, 310.0, 425.0, 4400.0):
        assert abs(iso.age_from_slope(iso.slope_for(age)) - age) < 1e-9
    # Book 2's Varden granite: slope 0.004341 gives 310 Ma
    assert round(iso.age_from_slope(0.004341)) == 310


def test_fit_recovers_a_synthetic_age_exactly_without_scatter():
    xs = [0.5, 3.0, 7.5, 12.0, 30.0]
    ys = iso.synthetic(xs, 1234.0, 0.7031)
    m, b, s, sm, sb = iso.lsq(xs, ys)
    assert abs(iso.age_from_slope(m) - 1234.0) < 1e-6 and abs(b - 0.7031) < 1e-12
    assert s < 1e-12


def test_fit_recovers_the_age_within_its_uncertainty():
    rng = random.Random(7)
    xs = [1.0 + 2.5 * i for i in range(10)]
    ys = [y + rng.gauss(0.0, 1e-4) for y in iso.synthetic(xs, 500.0, 0.7050)]
    m, b, s, sm, sb = iso.lsq(xs, ys)
    assert abs(iso.age_from_slope(m) - 500.0) < 4 * iso.age_sigma(m, sm)
    assert abs(b - 0.7050) < 4 * sb


def test_printed_isochron_values():
    xs, ys = iso.data()
    m, b, s, sm, sb = iso.lsq(xs, ys)
    assert round(iso.age_from_slope(m), 1) == 424.5
    assert round(iso.age_sigma(m, sm), 1) == 0.8
    assert round(b, 4) == 0.7062 and round(sb, 5) == 0.00018
    assert round(m, 6) == 0.005948
    # the least-squares line passes through the centroid
    xm, ym = sum(xs) / len(xs), sum(ys) / len(ys)
    assert abs(b + m * xm - ym) < 1e-12


def test_intcal_values_equal_the_dataset():
    cur = rc.read()
    with open(rc.DATA, encoding="utf8") as f:
        raw = {int(r["cal_bp"]): r for r in csv.DictReader(f)}
    for c in (0, 2000, 2500, 8000, 12000, 55000):
        assert cur[c] == (int(raw[c]["c14_age"]), int(raw[c]["c14_sigma"]))
    assert len(cur) == 9501 and max(cur) == 55000
    assert cur[2000] == (2070, 14) and cur[12000][0] == 10306


def test_intcal_is_monotonic_overall_but_not_everywhere():
    cur = rc.read()
    thousands = [cur[c][0] for c in range(0, 50001, 1000)]   # to 50 cal kBP
    assert all(a < b for a, b in zip(thousands, thousands[1:]))
    zoom = [cur[c][0] for c in range(2500, 2701)]
    assert any(a > b for a, b in zip(zoom, zoom[1:]))       # wiggles: not monotonic in detail


def test_plateau_range():
    cur = rc.read()
    old, young, n = rc.calendar_range(cur, 2480, 15, 2000, 3000)
    assert (old, young) == (2699, 2495) and n > 30


def test_radiocarbon_younger_than_calendar_at_12_kyr():
    cur = rc.read()
    assert 12000 - cur[12000][0] == 1694
    assert round(rc.MODERN / rc.LIBBY, 4) == 1.0237

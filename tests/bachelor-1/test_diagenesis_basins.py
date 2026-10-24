"""Tests for compaction and decompaction (Athy's law) and for the sea-level stack."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import compaction as c  # noqa: E402
import sea_level as sl  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
LEDGER = os.path.join(ROOT, "sources", "ledger", "book3.md")


def ledger_row(row_id):
    with open(LEDGER, encoding="utf8") as f:
        for line in f:
            if line.startswith("| %s |" % row_id):
                return line
    raise KeyError(row_id)


def test_parameters_match_the_ledger():
    row = ledger_row("pybacktrack:compaction")
    for lith, key in (("shale", "shale"), ("sandstone", "sand"), ("chalk", "chalk"),
                      ("shaly sandstone", "shaly sand")):
        phi0, lam, rho = c.LITHOLOGIES[lith]
        assert "%s %d kg/m3 / %.2f / %d m" % (key, rho, phi0, lam) in row or \
            "%s %d / %.2f / %d m" % (key, rho, phi0, lam) in row


def test_surface_porosity_and_decay():
    for lith, (phi0, lam, _) in c.LITHOLOGIES.items():
        assert c.porosity(0.0, lith) == phi0
        assert abs(c.porosity(lam, lith) - phi0 / math.e) < 1e-12


def test_solid_thickness_is_the_integral_of_one_minus_porosity():
    n = 20000
    z1, z2 = 1200.0, 2100.0
    h = (z2 - z1) / n
    num = sum(1.0 - c.porosity(z1 + (k + 0.5) * h, "shale") for k in range(n)) * h
    assert abs(num - c.solid_thickness(z1, z2, "shale")) < 1e-4


def test_moving_a_layer_keeps_its_solid():
    for lith in c.LITHOLOGIES:
        b = c.move_layer(3000.0, 3500.0, lith, 0.0)
        assert abs(c.solid_thickness(0.0, b, lith) - c.solid_thickness(3000.0, 3500.0, lith)) < 1e-6
        assert b > 500.0                         # a layer thickens as it is unburied
        back = c.move_layer(0.0, b, lith, 3000.0)
        assert abs(back - 3500.0) < 1e-6         # and burying it again restores it


def test_printed_demo():
    lith, z1, z2 = c.DEMO
    assert round(c.solid_thickness(z1, z2, lith)) == 440
    assert round(c.decompacted_thickness(z1, z2, lith)) == 891
    assert round(c.porosity(3000.0, "shale"), 2) == 0.14
    assert round(c.loading_factor(3300.0, 1030.0, 2300.0), 2) == 2.27
    assert round(c.loading_factor(3300.0, 0.0, 2300.0), 1) == 3.3


def test_stack_last_glacial_minimum_agrees_with_lambeck():
    rows = sl.read()
    assert len(rows) == 799 and rows[0][0] == 0 and rows[-1][0] == 798
    age, v, sig = sl.extreme(rows, "short", 0, 40)
    assert (age, v) == (24, -130.0)
    assert "-130.0 m at 24 ka" in ledger_row("data:b3-sealevel-stack")
    assert "-134 m" in ledger_row("lambeck:lgm")
    # within the stack's own one-sigma error, and well within its 9-12 m mean uncertainty
    assert abs(v - sl.LAMBECK_LGM) < sig


def test_stack_series_and_rate():
    rows = sl.read()
    long_ = sl.series(rows, "long")
    short = sl.series(rows, "short", 140)
    assert long_[-1][0] == 798 and short[-1][0] == 140
    assert all(lo <= s <= hi for _, s, lo, hi in long_)
    assert round(sl.mean_rate(rows, "short", 8, 16), 1) == 11.1


def test_five_fast_rises_of_more_than_100_m():
    rises = sl.fast_rises(sl.read())
    assert [a for a, _ in rises] == [24, 138, 342, 429, 627]
    long_ = [s for _, s, _, _ in sl.series(sl.read(), "long")]
    assert max(long_) - min(long_) < 150.0          # "a range of about 150 m"

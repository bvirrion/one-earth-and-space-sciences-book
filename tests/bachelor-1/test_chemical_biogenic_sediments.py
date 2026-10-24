"""Tests for the evaporation of seawater: the reference composition, the onsets
of the evaporation sequence, and the masses laid down by complete evaporation."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import evaporation as e  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
LEDGER = os.path.join(ROOT, "sources", "ledger", "book3.md")


def ledger_row(row_id):
    with open(LEDGER, encoding="utf8") as f:
        for line in f:
            if line.startswith("| %s |" % row_id):
                return line
    raise KeyError(row_id)


def test_reference_composition_sums_and_is_neutral():
    assert abs(sum(w for _, _, w in e.COMPOSITION.values()) - 1.0) < 1e-6
    # the table's mole fractions balance exactly; the rounded mass fractions to 1e-6 mol/kg
    assert abs(e.charge_balance()) < 1e-6
    assert abs(e.bittern_charge()) < 1e-6


def test_composition_matches_the_ledger():
    row = ledger_row("teos10:reference-composition")
    for ion in ("Na", "Mg", "Ca", "K", "Cl", "SO4"):
        assert ("%.7f" % e.COMPOSITION[ion][2]) in row
    assert "35.16504" in ledger_row("teos10:reference-salinity")


def test_onsets_match_the_ledger_and_increase():
    row = ledger_row("mccaffrey:thresholds")
    for _, cf in e.ONSETS:
        assert ("%g" % cf) in row
    cfs = [cf for _, cf in e.ONSETS]
    assert cfs == sorted(cfs)
    assert round(e.remaining_fraction(10.6), 3) == 0.094


def test_precipitate_never_exceeds_the_salt():
    seq = e.sequence()
    assert e.anhydrous_total(seq) <= e.S_R
    # the only mass lost is the CO2 and water released by the carbonate step
    lost = e.S_R - e.anhydrous_total(seq)
    n_hco3 = e.moles("HCO3")
    assert abs(lost - n_hco3 / 2 * (44.0095 + 18.01528)) < 1e-9


def test_printed_masses():
    seq = e.sequence()
    assert round(seq["caco3"], 2) == 0.11
    assert round(seq["gypsum"], 2) == 1.58
    assert round(seq["halite"], 1) == 27.4
    assert round(seq["bittern"], 1) == 6.3
    assert round(seq["halite"] / e.anhydrous_total(seq), 2) == 0.78


def test_layer_thicknesses_from_a_column():
    seq = e.sequence()
    h = e.layer_thickness(seq["halite"], 1000.0, 1030.0, 2170.0)
    assert round(h, 1) == 13.0
    assert round(e.layer_thickness(seq["gypsum"], 1000.0, 1030.0, 2300.0), 2) == 0.71
    assert math.ceil(1500.0 / h) == 116


import ccd_flank as cf  # noqa: E402


def test_flank_uses_the_depth_age_law_of_chapter_13():
    assert cf.crossing_age(2500.0) == 0.0
    assert abs(cf.crossing_age(4250.0) - 25.0) < 1e-9   # the example of ch. 13
    t = cf.crossing_age(4500.0)
    assert round(t, 1) == 32.7 and abs(cf.halfspace(t) - 4500.0) < 1e-9
    assert round(cf.distance_km(t)) == 816
    assert round(cf.crossing_age(5100.0), 1) == 55.2
    prof = cf.profile()
    assert prof[0] == (0.0, 0.0, 2500.0) and prof[-1][0] == 70.0
    assert all(b[2] > a[2] for a, b in zip(prof, prof[1:]))

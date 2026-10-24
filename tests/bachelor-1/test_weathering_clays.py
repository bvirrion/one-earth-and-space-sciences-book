"""Tests for the weathering-clays figure data: the ionic-potential diagram (radii
equal the ledger, the classic ions fall in their fields) and the balanced
hydrolysis reactions (every element and the charge balance; the exported fractions
of the three degrees)."""
import os
import re
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import hydrolysis as hy  # noqa: E402
import ionic_potential as ip  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
LEDGER = os.path.join(ROOT, "sources", "ledger", "book3.md")


def ledger_row(row_id):
    with open(LEDGER, encoding="utf8") as f:
        for line in f:
            if line.startswith("| %s |" % row_id):
                return line
    raise KeyError(row_id)


# --- ionic potential -------------------------------------------------------------

def test_radii_equal_the_ledger():
    row = ledger_row("shannon:radii-b19")
    pairs = re.findall(r"([A-Z][a-z]?)(\d?)\+ (\d\.\d+)", row)
    found = {}
    for sym, charge, r in pairs:
        found[(sym, int(charge or 1))] = float(r)
    assert len(found) == len(ip.IONS)
    for s, z, r in ip.IONS:
        base = re.match(r"[A-Z][a-z]?", s).group(0)
        assert found[(base, z)] == r, s


def test_classic_ions_fall_in_their_fields():
    assert ip.field(*ip.ion("Na")) == 0
    assert ip.field(*ip.ion("K")) == 0
    assert ip.field(*ip.ion("Ca")) == 0
    assert ip.field(*ip.ion("Fe2")) == 0
    assert ip.field(*ip.ion("Al")) == 1
    assert ip.field(*ip.ion("Fe3")) == 1
    assert ip.field(*ip.ion("Ti")) == 1
    assert ip.field(*ip.ion("P")) == 2
    assert ip.field(*ip.ion("S")) == 2
    assert ip.field(*ip.ion("Si")) == -1               # on the boundary z/r = 10
    assert abs(ip.ionic_potential(*ip.ion("Si")) - 10.0) < 1e-9


def test_oxidation_moves_iron_and_manganese_across_the_boundary():
    assert ip.ionic_potential(*ip.ion("Fe2")) < ip.LOW < ip.ionic_potential(*ip.ion("Fe3"))
    assert ip.ionic_potential(*ip.ion("Mn2")) < ip.LOW < ip.ionic_potential(*ip.ion("Mn4"))


# --- hydrolysis ------------------------------------------------------------------

PAIRS = [("albite", "beidellite"), ("albite", "kaolinite"), ("albite", "gibbsite"),
         ("anorthite", "kaolinite"), ("anorthite", "gibbsite"), ("orthoclase", "kaolinite"),
         ("orthoclase", "gibbsite")]


def test_every_reaction_balances():
    for mineral, product in PAIRS:
        left, right, ql, qr = hy.check(mineral, product)
        keys = set(left) | set(right)
        for e in keys:
            assert left.get(e, 0) == right.get(e, 0), (mineral, product, e)
        assert ql == qr
        c = hy.balance(mineral, product)
        assert all(v >= 0 for v in c.values())


def test_textbook_orthoclase_equation():
    c = hy.balance("orthoclase", "kaolinite")       # 2 Or + 2 H+ + 9 H2O -> Kln + 2 K+ + 4 H4SiO4
    assert (c["mineral"], c["H+"], c["H2O"], c["K"], c["H4SiO4"]) == (2, 2, 9, 2, 4)


def test_exported_fractions_of_the_three_degrees():
    assert hy.exported("albite", "beidellite") == {"Na": F(4, 5), "Si": F(8, 15), "Al": 0}
    assert hy.exported("albite", "kaolinite") == {"Na": 1, "Si": F(2, 3), "Al": 0}
    assert hy.exported("albite", "gibbsite") == {"Na": 1, "Si": 1, "Al": 0}
    assert hy.exported("anorthite", "kaolinite")["Si"] == 0      # Si/Al = 1 already


def test_molar_masses_match_the_mineral_database():
    # webmineral: kaolinite 258.16, gibbsite 78.00 g/mol (ledger webmineral:clays-b19)
    assert abs(hy.molar_mass(hy.MINERALS["kaolinite"]) - 258.16) < 0.01
    assert abs(hy.molar_mass(hy.MINERALS["gibbsite"]) - 78.00) < 0.01


def test_mass_is_conserved_per_tonne():
    t = hy.per_tonne("albite", "kaolinite")
    m = hy.molar_mass
    c = hy.balance("albite", "kaolinite")
    k = t["mol"] / float(c["mineral"])
    left = 1e6 + k * (float(c["H+"]) * hy.ATOMIC_WEIGHT["H"] + float(c["H2O"]) * m(hy.WATER))
    right = (k * m(hy.MINERALS["kaolinite"]) + k * float(c["Na"]) * hy.ATOMIC_WEIGHT["Na"]
             + k * float(c["H4SiO4"]) * m(hy.SILICIC_ACID))
    assert abs(left - right) < 1e-6 * left

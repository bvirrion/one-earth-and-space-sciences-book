"""Tests for the Phanerozoic chart read from the shared ledger, and for the
interpolation of ages between dated ash beds used in the chapter."""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import ics_chart as ic  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")


def raw_rows(kind):
    """{unit: first number of the value column} straight from the ledger text."""
    out = {}
    for line in open(os.path.join(ROOT, "sources", "data_ledger.md"), encoding="utf8"):
        cells = [c.strip() for c in line.split("|")]
        if len(cells) > 3 and cells[1].startswith("ics:%s." % kind):
            out[cells[1].split(".", 1)[1]] = cells[3].split()[0]
    return out


def test_every_unit_is_in_the_ledger():
    base, colour = ic.ledger()
    for n in ic.ERAS + ic.PERIODS + ("Phanerozoic",):
        assert n in base and n in colour


def test_bases_equal_the_ledger():
    base, _ = ic.ledger()
    raw = raw_rows("base")
    for n in ic.ERAS + ic.PERIODS:
        assert base[n] == raw[n]


def test_bases_decrease_and_eras_match_periods():
    base, _ = ic.ledger()
    ages = [float(base[n]) for n in ic.PERIODS]
    assert all(a > b for a, b in zip(ages, ages[1:]))
    assert base["Paleozoic"] == base["Cambrian"] == base["Phanerozoic"]
    assert base["Mesozoic"] == base["Triassic"]
    assert base["Cenozoic"] == base["Paleogene"]


def test_spans_tile_the_phanerozoic():
    base, _ = ic.ledger()
    sp = ic.spans(ic.PERIODS, base)
    assert sp[0][1] == float(base["Phanerozoic"]) and sp[-1][2] == 0.0
    assert all(a[2] == b[1] for a, b in zip(sp, sp[1:]))
    assert abs(sum(ic.durations(base).values()) - float(base["Phanerozoic"])) < 1e-9


def test_colours_equal_the_ledger_and_the_style_file():
    _, colour = ic.ledger()
    raw = raw_rows("colour")
    sty = ic.sty_colours()
    for n in ic.ERAS + ic.PERIODS:
        assert colour[n] == raw[n].lstrip("#").upper()
        assert sty[n] == colour[n]


def test_printed_values():
    base, _ = ic.ledger()
    d = ic.durations(base)
    assert max(d, key=d.get) == "Cretaceous" and round(d["Cretaceous"], 1) == 77.1
    pre_q = {k: v for k, v in d.items() if k != "Quaternary"}
    assert min(pre_q, key=pre_q.get) == "Neogene" and round(d["Neogene"], 2) == 20.46
    assert round(sum(d.values()) / len(d), 1) == 44.9


def test_extinction_horizons_are_ledger_boundaries():
    ledger3 = open(os.path.join(ROOT, "sources", "ledger", "book3.md"), encoding="utf8").read()
    base, _ = ic.ledger()
    assert re.search(r"\| gssp:induan \|[^|]*251\.902", ledger3) and base["Mesozoic"] == "251.902"
    assert re.search(r"\| gssp:danian \|[^|]*66\.00", ledger3) and base["Cenozoic"] == "66.00"
    # the end-Permian extinction interval of Burgess et al. brackets the boundary age
    assert 251.880 < float(base["Mesozoic"]) < 251.941

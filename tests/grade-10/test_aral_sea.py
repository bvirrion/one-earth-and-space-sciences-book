"""figdata/grade-10/aral_sea.py: the Aral Sea table against its ledger row, and the budget."""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import aral_sea as aral  # noqa: E402

LEDGER = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "ledger", "book2.md")


def ledger_rows():
    with open(LEDGER, encoding="utf8") as f:
        line = next(l for l in f if l.startswith("| gaybullaev:aral-table |"))
    out = {}
    for m in re.finditer(r"(\d{4}) (?:river runoff )?([\d.]+)(?: \(Amu Darya [\d.]+, Syr Darya [\d.]+\))?,"
                         r" (?:evaporation )?([\d.]+), (?:volume )?([\d.]+), (?:precipitation )?([\d.]+),"
                         r" (?:salinity )?([\d.]+)", line):
        out[int(m.group(1))] = tuple(float(m.group(k)) for k in range(2, 7))
    return out


def test_table_matches_the_ledger_row():
    rows = ledger_rows()
    assert set(rows) == set(aral.TABLE)
    for y, v in aral.TABLE.items():
        assert rows[y] == v, y


def test_budget_numbers():
    n = aral.numbers()
    assert abs(n["e_1960_m"] - 1.046) < 0.001
    assert abs(n["mean_depth_1960_m"] - 16.1) < 0.1
    assert -1.0 < n["level_change_1987_m"] < -0.7
    assert abs(n["net_1987"] - (-29.6)) < 1e-9
    assert 0.5 < n["area_1987_share"] < 0.55


def test_volume_falls_overall():
    years = sorted(aral.TABLE)
    assert aral.TABLE[years[-1]][2] < 0.1 * aral.TABLE[years[0]][2]

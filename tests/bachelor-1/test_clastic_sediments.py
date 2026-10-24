"""Tests for the clastic-sediments figure data and calculations: the phi scale,
Folk's graphic measures, the method of moments, the sorting scale, and the plane
vector mean of palaeocurrents."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import grain_size as g  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
LEDGER = os.path.join(ROOT, "sources", "ledger", "book3.md")


def ledger_row(row_id):
    with open(LEDGER, encoding="utf8") as f:
        for line in f:
            if line.startswith("| %s |" % row_id):
                return line
    raise KeyError(row_id)


def test_phi_scale():
    assert g.phi_of(1.0) == 0.0
    assert g.phi_of(0.25) == 2.0
    assert g.phi_of(2.0) == -1.0
    assert abs(g.d_of(4.0) - 0.0625) < 1e-12
    assert abs(g.phi_of(0.18) - 2.47) < 0.005


def test_samples_sum_to_100_and_classes_are_contiguous():
    for s in (g.BEACH, g.TILL):
        assert abs(sum(w for _, _, w in s) - 100.0) < 1e-9
        for (lo0, hi0, _), (lo1, _, _) in zip(s, s[1:]):
            assert hi0 == lo1
    cum = g.cumulative(g.BEACH)
    assert cum[0][1] == 0.0 and abs(cum[-1][1] - 100.0) < 1e-9


def test_printed_measures_of_the_figure():
    (mz, si), _ = g.folk_measures(g.BEACH)
    assert round(mz, 2) == 2.25 and round(si, 2) == 0.36
    assert g.sorting_class(si) == "well sorted"
    assert abs(g.d_of(mz) - 0.21) < 0.005
    (mz, si), _ = g.folk_measures(g.TILL)
    assert round(mz, 2) == 1.83 and round(si, 2) == 3.84
    assert g.sorting_class(si) == "very poorly sorted"
    m, sd = g.moments(g.TILL)
    assert round(m, 2) == 1.89 and round(sd, 2) == 3.64


def test_folk_constants_and_scale_match_the_ledger():
    row = ledger_row("folk:graphic-measures")
    assert "/6.6" in row and "3.30" in row
    row = ledger_row("folk:sorting-classes")
    for lim, _ in g.SORTING[:-1]:
        assert ("%g" % lim) in row
    assert g.sorting_class(0.70) == "moderately well sorted"
    assert g.sorting_class(1.04) == "poorly sorted"


def test_graphic_measures_of_a_normal_distribution():
    mz, si = g.normal_quantile_check(2.0, 0.5)
    assert abs(mz - 2.0) < 1e-12
    assert round(si / 0.5, 3) == 0.996


def test_exercise_ten_moments_and_graphic_measures():
    s = [(-1, 0, 2.0), (0, 1, 8.0), (1, 2, 30.0), (2, 3, 40.0), (3, 4, 15.0), (4, 5, 5.0)]
    m, sd = g.moments(s)
    assert abs(m - 2.23) < 1e-9 and round(sd, 2) == 1.04
    (mz, si), ps = g.folk_measures(s)
    assert [round(p, 3) for p in ps] == [0.375, 1.2, 2.25, 3.267, 4.0]
    assert round(mz, 2) == 2.24 and round(si, 2) == 1.07


def test_vector_mean_handles_north():
    a, r = g.vector_mean([350, 10])
    assert min(a, 360 - a) < 1e-9 and abs(r - math.cos(math.radians(10))) < 1e-12
    a, r = g.vector_mean([352, 10, 25, 4, 338, 17, 31, 359, 12, 46, 6, 344])
    assert round(a, 1) == 8.6 and round(r, 3) == 0.948
    a, r = g.vector_mean([350, 20, 5, 340, 15, 30])
    assert round(a, 1) == 6.7 and round(r, 3) == 0.955


def test_problem_units():
    beds = {1: (4.2, 5.0, 6.6, 8.4, 9.6), 2: (1.9, 2.4, 3.4, 4.6, 5.5),
            3: (0.9, 1.25, 1.8, 2.35, 2.7), 4: (-1.8, -0.8, 0.9, 2.1, 2.9)}
    want = {1: (6.67, 1.67, "poorly sorted"), 2: (3.47, 1.10, "poorly sorted"),
            3: (1.80, 0.55, "moderately well sorted"), 4: (0.73, 1.44, "poorly sorted")}
    for k, v in beds.items():
        mz, si = g.folk(*v)
        assert round(mz, 2) == want[k][0] and round(si, 2) == want[k][1]
        assert g.sorting_class(si) == want[k][2]


def test_step_table_keeps_the_last_class():
    for smp in (g.BEACH, g.TILL):
        st = g.step(smp)
        assert len(st) == len(smp) + 1
        assert st[-1] == (smp[-1][1], smp[-1][2]) and st[-2] == (smp[-1][0], smp[-1][2])

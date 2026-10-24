"""Tests for the Al2SiO5 and other reaction lines (figdata/bachelor-2/facies.py)."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import facies as fa  # noqa: E402

K = 273.15
DFG = {"ky": -2443.1e3, "and": -2441.8e3, "sil": -2439.1e3}   # rh95:al2sio5


def test_tabulated_gibbs_energies_match_h_minus_ts():
    # dG = dH - T dS at 298.15 K reproduces the tabulated free energies of reaction
    for a, b in fa.REACTIONS:
        dg = fa.delta(a, b, "H") - 298.15 * fa.delta(a, b, "S")
        assert dg == pytest.approx(DFG[b] - DFG[a], abs=150)


def test_methods_agree_at_298_and_clapeyron_slope():
    for a, b in fa.REACTIONS:
        assert fa.line_p(a, b, 298.15, "B") == pytest.approx(fa.line_p(a, b, 298.15, "A"), abs=1)
        h = 1.0
        num = (fa.line_p(a, b, 600 + h, "A") - fa.line_p(a, b, 600 - h, "A")) / (2 * h)
        assert num == pytest.approx(fa.clapeyron_slope(a, b), rel=1e-9)


def test_three_lines_meet_at_the_triple_point():
    for m in ("A", "B"):
        t, p = fa.triple_point(m)
        assert fa.line_p("and", "sil", t, m) == pytest.approx(p, abs=1e-3)
    t, p = fa.triple_point("A")
    assert t - K == pytest.approx(513.8, abs=0.1) and p == pytest.approx(3882, abs=1)


def test_fields_hold_the_right_polymorph():
    assert fa.stable_phase(400 + K, 1000) == "and"
    assert fa.stable_phase(400 + K, 6000) == "ky"
    assert fa.stable_phase(750 + K, 3000) == "sil"
    assert fa.stable_phase(750 + K, 9000) == "ky"


def test_method_b_is_close_to_the_experimental_diagram():
    for tc, pk in fa.HM93[("ky", "and")][2:7]:
        assert fa.line_p("ky", "and", tc + K) / 1e3 == pytest.approx(pk, abs=0.3)
    for tc, pk in fa.HM93[("ky", "sil")][:3]:
        assert fa.line_p("ky", "sil", tc + K) / 1e3 == pytest.approx(pk, abs=0.6)
    t, p = fa.triple_point("B")
    assert abs(t - K - fa.HM93_TRIPLE[0]) < 40 and abs(p / 1e3 - fa.HM93_TRIPLE[1]) < 0.5


def test_other_reactions_and_dehydration_curvature():
    dh, ds, dv, dg, ln = fa.cc_ar()
    assert ln(298.15) == pytest.approx(1 + dg / -dv, rel=0.01)
    dh, ds, dv, dg, ln = fa.ab_jd_qz()
    assert ln(298.15) == pytest.approx(1 + dg / -dv, rel=0.02)
    (t1, p1), (t2, p2), (t3, p3) = fa.DAY73
    assert (p2 - p1) / (t2 - t1) < (p3 - p2) / (t3 - t2)       # the curve steepens


def test_triple_point_sensitivity_matches_the_line_shift():
    dt, dp = fa.sensitivity(1.0, ("ky", "and"))
    shift = -1000 / fa.delta("ky", "and", "V")
    assert dt == pytest.approx(shift / (fa.clapeyron_slope("ky", "sil") - fa.clapeyron_slope("ky", "and")),
                               rel=1e-6)

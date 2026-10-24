"""Tests for the isotope-geochemistry figure data (isotopes.py)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import isotopes as iso  # noqa: E402


def test_chur_and_epsilon():
    assert iso.eps_nd(iso.R_CHUR) == 0
    # CHUR 4.567 Ga ago: the isochron equation run backwards
    assert abs(iso.r_chur(4.567e9) - 0.506692) < 2e-6
    # epsilon of CHUR at any time is zero by definition
    assert abs(iso.eps_nd(iso.r_chur(2e9), 2e9)) < 1e-12
    assert abs(iso.eps_nd(iso.MORB_ND) - 8.505) < 0.002


def test_linear_growth_matches_exact_to_first_order():
    q = iso.q_factor()
    assert abs(q - 25.02) < 0.01
    # the depleted mantle starts at CHUR at T_EARTH and reaches MORB today
    assert abs(iso.eps_nd(iso.r_dm(iso.T_EARTH), iso.T_EARTH)) < 1e-9
    assert abs(iso.r_dm(0) - iso.MORB_ND) < 1e-15
    f = iso.dm_smnd() / iso.SMND_CHUR - 1
    lin = q * f * iso.T_EARTH / 1e9
    exact = iso.eps_nd(iso.MORB_ND)
    # neglected terms of relative size about lambda T / 2 (1.5 per cent)
    assert abs(exact / lin - 1) < 0.03


def test_crust_curve():
    # crust starts on the depleted-mantle curve at 2.7 Ga and ends strongly negative
    t = iso.T_CRUST
    assert abs(iso.r_crust(t) - iso.r_dm(t)) < 1e-15
    assert -28 < iso.eps_nd(iso.r_crust(0)) < -26.5
    assert abs(iso.f_smnd(iso.SMND_UCC) + 0.4514) < 1e-3


def test_mixing():
    # f = 0 and 1 give the end-members; ratio * concentration linear in f
    c, r = iso.mix(0.0, 200, 0.72, 10, 0.70282)
    assert (c, r) == (10, 0.70282)
    c, r = iso.mix(1.0, 200, 0.72, 10, 0.70282)
    assert abs(r - 0.72) < 1e-15
    # R is linear in 1/C along the mixing line
    pts = [iso.mix(f, 200, 0.72, 10, 0.70282) for f in (0.01, 0.05, 0.2)]
    (c1, r1), (c2, r2), (c3, r3) = pts
    s12 = (r2 - r1) / (1 / c2 - 1 / c1)
    s13 = (r3 - r1) / (1 / c3 - 1 / c1)
    assert abs(s12 - s13) < 1e-12
    # normalised hyperbola: straight when K = 1, above the diagonal when K > 1
    assert iso.mix_normalised(0.3, 1.0) == (0.3, 0.3)
    assert iso.mix_normalised(0.3, 5.0)[1] > 0.3 > iso.mix_normalised(0.3, 0.2)[1]


def test_water_vapour_and_standards():
    d18, dd = iso.vapour(20)
    assert abs(d18 + 9.705) < 0.001 and abs(dd + 77.49) < 0.01
    assert 7.5 < dd / d18 < 9.0   # close to the slope 8 of the meteoric water line
    assert abs((2.0672e-3 / 2.0052e-3 - 1) * 1000 - 30.92) < 0.01


def test_oib_dataset():
    himu, em1 = iso.oib("HIMU"), iso.oib("EM1")
    assert len(himu) == 36 and len(em1) == 53
    # HIMU islands: MORB-like strontium, epsilon between CHUR and MORB
    assert all(0.7027 < s < 0.7032 and 3.5 < e < 6 for s, e in himu)
    # EM1 islands: enriched side of CHUR
    assert all(s > 0.7048 and e < 0 for s, e in em1)
    assert not any(math.isnan(e) for _, e in himu + em1)

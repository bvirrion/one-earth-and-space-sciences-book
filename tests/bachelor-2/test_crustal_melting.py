"""Tests for the crustal-melting figure data (figdata/bachelor-2/anatexis.py)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import anatexis as an  # noqa: E402


def test_wet_solidus_passes_through_the_published_points_and_falls_with_pressure():
    for p, t in an.WET:
        assert an.wet_solidus(p) == pytest.approx(t)
    assert an.wet_solidus(6.0) == pytest.approx(650.0)
    assert np.isnan(an.wet_solidus(1.0)) and np.isnan(an.wet_solidus(20.0))
    ps = np.linspace(2.0, 15.3, 50)
    assert np.all(np.diff(an.wet_solidus(ps)) < 0)


def test_feldspars_have_unit_saturation_index():
    # one Al2O3 per K2O, Na2O or CaO in every feldspar, whatever the mixture
    m = an.M
    for k, n, c in ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0), (0.3, 0.5, 0.2)):
        ox = {"Al2O3": (k + n + c) * m["Al2O3"], "K2O": k * m["K2O"],
              "Na2O": n * m["Na2O"], "CaO": c * m["CaO"]}
        assert an.acnk(ox) == pytest.approx(1.0)


def test_classification_of_the_reference_materials():
    assert an.classify(an.ROCKS["BHVO-2"]) == "metaluminous"
    assert an.classify(an.ROCKS["AGV-2"]) == "metaluminous"
    assert an.classify(an.ROCKS["S-leuco"]) == "peraluminous"
    assert an.classify(an.ROCKS["peralk"]) == "peralkaline"
    assert an.acnk(an.ROCKS["SRM-278"]) == pytest.approx(0.993, abs=0.001)
    for ox in an.ROCKS.values():          # A/CNK can never exceed A/NK
        assert an.acnk(ox) < an.ank(ox)


def test_water_budget_of_micas():
    w_ms = an.water_fraction(an.M_MUSCOVITE)
    assert w_ms == pytest.approx(0.0452, abs=1e-4)
    assert an.water_fraction(an.M_PHLOGOPITE) == pytest.approx(0.0432, abs=1e-4)
    f = an.melt_fraction(0.20, w_ms, 0.060)
    assert f == pytest.approx(0.151, abs=1e-3)
    # a saturated melt holds more water, so it makes less melt from the same mica
    assert an.melt_fraction(0.20, w_ms, 0.1254) < f


def test_solubility_line_matches_the_quoted_slope():
    s, i = an.solubility_fit()
    assert s == pytest.approx(1.27, abs=0.02)
    for p, w in an.AOQ:
        if p >= 3.0:
            assert i + s * p == pytest.approx(w, abs=0.2)


def test_paths_mid_crust_stays_dry_and_base_melts():
    paths = an.paths()
    mid, base = paths[35], paths[70]
    # the mid-crustal rock never reaches the wet solidus
    t = an.wet_solidus(mid[:, 2])
    ok = ~np.isnan(t)
    assert np.all(mid[ok, 1] < t[ok])
    # the base of the thickened crust exceeds 900 C and enters the amphibole bracket
    assert base[:, 1].max() > 900
    inside = (base[:, 1] >= 875) & (base[:, 1] <= 925) & (base[:, 2] <= 12.5) & (base[:, 2] >= 10)
    assert inside.any()

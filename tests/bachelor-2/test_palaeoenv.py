"""Tests for the palaeoenvironment figure data (figdata/bachelor-2/palaeoenv.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import palaeoenv as pe  # noqa: E402


def test_athy_and_solid_thickness():
    for lith in pe.ORDER:
        assert pe.porosity(lith, 0.0) == pytest.approx(pe.LITH[lith][1])
        # the solid thickness is the integral of (1 - phi): check by the midpoint rule
        n, z1, z2 = 4000, 500.0, 900.0
        num = sum(1 - pe.porosity(lith, z1 + (i + 0.5) * (z2 - z1) / n) for i in range(n)) * (z2 - z1) / n
        assert pe.solid(lith, z1, z2) == pytest.approx(num, rel=1e-7)
    # Year 1 values at 3000 m: sandstone 0.22, shale 0.14, chalk 0.08
    assert round(pe.porosity("sandstone", 3000.0), 2) == 0.22
    assert round(pe.porosity("shale", 3000.0), 2) == 0.14
    assert round(pe.porosity("chalk", 3000.0), 2) == 0.08


def test_restoration_conserves_grains_and_matches_thin_layer_factor():
    h = pe.restored("shale", 766.0, 866.0)
    assert pe.solid("shale", 0.0, h) == pytest.approx(pe.solid("shale", 766.0, 866.0), abs=1e-6)
    assert h > 100.0
    # a thin layer: the restored thickness tends to the factor (1 - phi) / (1 - phi0)
    z, dz = 1000.0, 0.01
    for lith in pe.ORDER:
        assert pe.restored(lith, z, z + dz) / dz == pytest.approx(pe.ratio(lith, z), rel=1e-4)
    # moving a layer back to where it is changes nothing
    assert pe.restored("chalk", 200.0, 300.0, top=200.0) == pytest.approx(100.0, abs=1e-6)


def test_varden_column_matches_the_region_and_the_year3_well():
    assert pe.THICK == {"sandstone": 120.0, "limestone": 180.0, "shale": 100.0}
    dep, g = pe.syncline_depths()
    assert g == pytest.approx(441.0, abs=0.05)
    # the Year 3 well Varden-2: shale from 766 m, limestone from 866 m, sandstone from 1046 m
    assert dep["chalk"] == pytest.approx(766.0, abs=0.05)
    assert dep["shale"] == pytest.approx(866.0, abs=0.05)
    assert dep["limestone"] == pytest.approx(1046.0, abs=0.05)
    assert dep["sandstone"] == pytest.approx(1166.0, abs=0.05)


def test_rates():
    d = pe.numbers()
    assert d["ls_dt"] == pytest.approx(9.5)
    assert d["shale_dt"] == pytest.approx(13.2)
    # the limestone: 180 m now, 8 % porosity, laid down at 51 %
    assert d["ls_restored"] == pytest.approx(180 * 0.92 / 0.49)
    assert d["ls_rate_restored"] == pytest.approx(35.57, abs=0.01)
    assert d["ls_rate_solid"] == pytest.approx(d["ls_rate_restored"] * (1 - 0.51))
    # the solid rate does not depend on the porosity assumed at deposition
    assert pe.rate(180, 0.08, 0.0, 9.5) == pytest.approx(d["ls_rate_solid"])
    assert d["shale_rate_restored"] > d["shale_rate_now"] > d["shale_rate_solid"]
    assert math.isclose(d["shale_mean_phi"], 1 - d["shale_solid"] / 100.0)

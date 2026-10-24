import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
import early_earth as ee  # noqa: E402


def test_young_sun_was_about_70_percent_as_bright():
    assert ee.luminosity(0.0) == pytest.approx(1.0)
    assert ee.luminosity(ee.T_SUN_GYR) == pytest.approx(1 / 1.4)
    assert 0.69 < ee.luminosity(ee.T_SUN_GYR) < 0.72
    # brightening is monotonic
    ls = [ee.luminosity(0.05 * i) for i in range(92)]
    assert all(a > b for a, b in zip(ls, ls[1:]))


def test_equilibrium_temperatures():
    # today's value agrees with grade 10 (255 K)
    assert ee.t_eq(0.0) == pytest.approx(255.1, abs=0.2)
    # four billion years ago: about 237 K, below freezing by about 36 K
    n = ee.numbers()
    assert n["Teq_4Ga"] == pytest.approx(236.7, abs=0.2)
    assert n["Teq_4Ga"] == pytest.approx(ee.t_eq(0.0) * ee.luminosity(4.0) ** 0.25)
    assert n["warming_to_freeze_4Ga"] > 30


def test_eons_follow_the_ledger_and_touch():
    sp = ee.eons()
    assert [s[0] for s in sp] == ["Hadean", "Archean", "Proterozoic", "Phanerozoic"]
    assert sp[0][1] == 4567 and sp[2][1] == 2500
    assert all(a[2] == b[1] for a, b in zip(sp, sp[1:]))


def test_oxygen_schematic_respects_the_bounds():
    ox = dict(ee.OXYGEN)
    assert ox[2.46] <= 1e-5          # anoxic Archean (Pavlov and Kasting 2002)
    assert ox[2.06] <= 0.1           # at most 10 % of today by the end of the GOE
    assert ox[0.0] == 1.0
    ts = [t for t, p in ee.OXYGEN]
    ps = [p for t, p in ee.OXYGEN]
    assert ts == sorted(ts, reverse=True) and ps == sorted(ps)

"""Tests for the shelf forward model and the periodogram scripts (Year 3,
ch. 16)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import lr04_periodogram as lp  # noqa: E402
import shelf_model as sm  # noqa: E402


@pytest.fixture(scope="module")
def model():
    h, shore, surfaces, steps = sm.run()
    tracts, rates = sm.classify(shore)
    return h, shore, steps, tracts, rates


def test_each_step_adds_exactly_the_supplied_volume():
    h = sm.H0 - sm.G * sm.X - sm.sigma(sm.X) * 3.0
    for e in (-20.0, 0.0, 15.0):
        new, xs = sm.fill(h, e, sm.Q * sm.DT)
        assert np.sum(new - h) * sm.DX_M == pytest.approx(sm.Q * sm.DT, rel=1e-9)
        assert np.all(new >= h)


def test_no_deposit_above_sea_level(model):
    _, shore, steps, _, _ = model
    sig = sm.sigma(sm.X)
    for k in range(1, len(steps), 37):
        t, hk = steps[k]
        before = steps[k - 1][1] - sig * sm.DT
        e = sm.sea(t)
        dry = before >= e
        assert np.allclose(hk[dry], before[dry])


def _toe_depth(shore, steps, k):
    """Water depth at the toe of the foreset built in step k."""
    t, xs, e = shore[k]
    h = steps[k + 1][1]
    old = steps[k][1] - sm.sigma(sm.X) * sm.DT
    i = int(np.searchsorted(sm.X, xs))
    while i < len(sm.X) - 1 and h[i] - old[i] > 1e-9:
        i += 1
    return e - h[i]


def test_forced_regression_follows_the_falling_stage_formula(model):
    _, shore, steps, tracts, rates = model
    checked = 0
    for k in range(10, len(shore) - 10, 10):
        if tracts[k - 10] != "F" or tracts[k + 10] != "F":
            continue
        depth = _toe_depth(shore, steps, k)
        ends = (_toe_depth(shore, steps, k - 4), _toe_depth(shore, steps, k + 4))
        if max(abs(d - depth) for d in ends) > 0.1 * depth:
            continue        # the foreset is stepping over the old shelf edge
        pred = sm.Q / depth - rates[k] / sm.TAN          # m/kyr
        obs = (shore[k + 4][1] - shore[k - 4][1]) / (8 * sm.DT) * 1000.0
        assert obs == pytest.approx(pred, rel=0.02)
        checked += 1
    assert checked >= 10


def test_tracts_follow_the_standard_order(model):
    _, _, _, tracts, _ = model
    order = [tracts[0]]
    for lab in tracts[1:]:
        if lab != order[-1]:
            order.append(lab)
    assert order == ["L", "T", "H", "F", "L", "T", "H"]


def test_transgression_needs_rising_relative_sea_level(model):
    _, _, _, tracts, rates = model
    assert all(r > 0 for lab, r in zip(tracts, rates) if lab == "T")
    assert all(r < 0 for lab, r in zip(tracts, rates) if lab == "F")


def test_basinward_shift_is_the_falling_plus_lowstand_regression(model):
    _, shore, _, tracts, _ = model
    shift = sm.basinward_shift(shore, tracts)
    start = next(i for i, lab in enumerate(tracts) if lab == "F")
    end = max(i for i, lab in enumerate(tracts) if lab == "L")
    xs = [s[1] for s in shore]
    assert shift == pytest.approx(max(xs[start:end + 1]) - xs[start - 1])
    assert 30.0 < shift < 40.0


def test_periodogram_finds_a_pure_sine():
    t = np.arange(0.0, 2000.0, 1.0)
    f, p = lp.periodogram(np.sin(2 * np.pi * t / 40.0) + 0.01 * t, 1.0)
    assert 1.0 / f[np.argmax(p)] == pytest.approx(40.0, rel=0.01)


def test_lr04_reads_a_monotonic_record():
    ages, vals = lp.read_lr04()
    assert np.all(np.diff(ages) > 0)
    assert ages[0] == 0.0 and ages[-1] > 2500.0


def test_lr04_windows_show_the_mid_pleistocene_change():
    s = lp.lr04_spectra()
    f, p = s["young"]
    assert 80.0 < 1.0 / f[np.argmax(p)] < 120.0
    f, p = s["old"]
    assert 1.0 / f[np.argmax(p)] == pytest.approx(41.0, abs=2.0)


def test_synthetic_core_peaks_give_back_the_sedimentation_rate():
    z, y = lp.core_series()
    f, p = lp.periodogram(y, 0.01)
    lam = 1.0 / f[np.argmax(p)]
    assert lam * 100.0 / 100.0 == pytest.approx(lp.SED, rel=0.02)

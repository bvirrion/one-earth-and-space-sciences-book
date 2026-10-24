"""Ch. 2 (observing-the-sky): the Planck curves peak where Wien's law says,
bluer colours go with hotter bodies, and the extinction fit recovers its
line."""
import os
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1")
sys.path.insert(0, HERE)
import blackbody_bands as B  # noqa: E402
import extinction_line as E  # noqa: E402


def test_wien_peak():
    for T in B.TEMPS:
        assert abs(B.peak_nm(T) - B.WIEN_B / T * 1e9) < 0.05


def test_bv_ratio_rises_with_temperature():
    r = [B.bv_ratio(T) for T in B.TEMPS]
    assert r[0] < r[1] < r[2]


def test_curves_normalised():
    rows = B.curves([200 + 5 * k for k in range(261)])
    for j in (1, 2, 3):
        assert max(r[j] for r in rows) <= 1.0 + 1e-12
        assert max(r[j] for r in rows) > 0.99


def test_fit_recovers_exact_line():
    obs = [(x, 7.85 + 0.16 * x) for x, _ in E.OBS]
    k, m0 = E.fit(obs)
    assert abs(k - 0.16) < 1e-12 and abs(m0 - 7.85) < 1e-12


def test_printed_fit():
    k, m0 = E.fit()
    assert abs(k - 0.160) < 0.001 and abs(m0 - 7.851) < 0.001
    assert E.rms() < 0.01

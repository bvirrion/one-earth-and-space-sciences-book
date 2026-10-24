"""Tests for figdata/grade-8/standard_atmosphere.py (chapter g8.1)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-8"))
import standard_atmosphere as A  # noqa: E402


def test_layer_base_temperatures():
    # Table 4 gradients from 288.15 K give the standard's base temperatures
    assert [round(t, 2) for t in A.TB] == [288.15, 216.65, 216.65, 228.65, 270.65, 270.65, 214.65, 186.95]


def test_tabulated_pressures():
    # values printed in the standard's tables (geometric altitude)
    for z, p in ((0.0, 101325.0), (11.0, 22699.9), (20.0, 5529.3), (30.0, 1197.0), (50.0, 79.779), (80.0, 1.0524)):
        assert abs(A.pressure(z) - p) / p < 2e-4, z


def test_temperature_above_86_km():
    assert A.temperature(86.0) == A.T7 == 186.8673
    assert abs(A.temperature(91.0) - 186.8673) < 1e-3          # the ellipse starts where the isothermal ends
    assert abs(A.temperature(110.0) - 240.0) < 0.05             # and ends at the defined T9
    assert A.temperature(100.0) > A.temperature(91.0)


def test_continuity_at_86_km():
    assert abs(A.temperature(85.999) - A.temperature(86.0)) < 0.2


def test_half_and_quarter_levels():
    assert abs(A.level(0.5) - 5.48) < 0.01
    assert abs(A.level(0.25) - 10.29) < 0.01
    assert A.pressure(A.level(0.25)) / A.P0 - 0.25 < 1e-6


def test_layers_and_shares():
    lay = A.layers()
    assert [n for n, *_ in lay] == ["troposphere", "stratosphere", "mesosphere", "thermosphere"]
    for (_, _, top), (_, base, _) in zip(lay, lay[1:]):
        assert top == base
    assert round(lay[0][2], 1) == 11.0
    # the coldest air below 100 km is at the mesopause
    assert min(A.temperature(z / 10.0) for z in range(0, 1001)) == A.T7
    assert round(A.share_below(lay[0][2])) == 78
    assert round(A.share_below(30.0)) == 99

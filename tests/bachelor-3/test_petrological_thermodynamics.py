"""Tests for the GASP, Schreinemakers and regular-solution figdata scripts
(Year 3, ch. 11)."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import gasp_tables as gt  # noqa: E402
import regular_solution as rs  # noqa: E402
import schreinemakers as sm  # noqa: E402


def test_gasp_reaction_is_balanced_and_consistent_with_formation_gibbs_energies():
    # 3 CaAl2Si2O8 = Ca3Al2Si3O12 + 2 Al2SiO5 + SiO2: Ca 3, Al 6, Si 6, O 24 on both sides
    left = {"Ca": 3, "Al": 6, "Si": 6, "O": 24}
    right = {"Ca": 3, "Al": 2 + 4, "Si": 3 + 2 + 1, "O": 12 + 10 + 2}
    assert left == right
    dh, ds, dv = gt.reaction_props()
    assert dh == pytest.approx(-36300.0, abs=1e-6)
    assert dv == pytest.approx(-6.610, abs=1e-9)
    # at 298.15 K the formation Gibbs energies of the summary table agree with dH - T dS
    dfg298 = {"grs": -6278.5, "an": -4007.9, "ky": -2443.1, "qz": -856.3}
    dg = sum(n * dfg298[k] for k, n in gt.NU.items()) * 1000.0
    # (formation entropies are not reaction entropies, but the elements cancel)
    assert dg == pytest.approx(dh - 298.15 * ds, abs=1500.0)


def test_constant_properties_and_tables_agree_within_a_few_hundred_bar():
    for i, t in enumerate(gt.TABLE_T):
        assert abs(gt.p_table(i) - gt.p_const(t)) < 150.0
    # slope dP/dT = dS/dV
    assert (gt.p_const(1000.0) - gt.p_const(900.0)) / 100.0 == pytest.approx(
        gt.reaction_props()[1] / gt.reaction_props()[2])
    # the experiment lies higher: 0.9 kbar at 900 K, 1.9 kbar at 1200 K
    assert 800 < gt.p_kn88(900 - 273.15) - gt.p_table(1) < 1000
    assert 1800 < gt.p_kn88(1200 - 273.15) - gt.p_table(4) < 2000


def test_barometer_and_thermometer_intersection():
    t, p = gt.intersect(0.20, 0.10, 0.30)
    assert gt.gb_temperature(p, 0.20) == pytest.approx(t)
    assert gt.gasp_pressure(t, 0.10, 0.30) == pytest.approx(p)
    # pure end members: the barometer gives the end-member line
    assert gt.gasp_pressure(1000.0, 0.5, 0.5) == pytest.approx(gt.p_kn88(1000.0 - 273.15))


def test_schreinemakers_bundle():
    # all four lines pass through the invariant point
    for a in "ABCD":
        assert sm.reaction_dg(a, sm.T0, sm.P0) == pytest.approx(0.0)
    # each line is stable on exactly one side
    for a in "ABCD":
        v, s = sm.direction(a)
        norm = math.hypot(v, s / sm.SCALE)
        stable = []
        for sign in (1, -1):
            t = sm.T0 + sign * v / norm * 50.0
            p = sm.P0 + sign * s / norm * 50.0
            stable.append(all(k in sm.hull_phases(t, p) for k in sm.REACTIONS[a]))
        assert stable.count(True) == 1
    # the metastable extension of the (B)- and (C)-absent lines lies where B, C are stable
    for a in "BC":
        sg = sm.stable_sign(a)
        v, s = sm.direction(a)
        norm = math.hypot(v, s / sm.SCALE)
        t = sm.T0 - sg * v / norm * 50.0
        p = sm.P0 - sg * s / norm * 50.0
        assert a in sm.hull_phases(t, p)
    # no divariant sector spans more than 180 degrees
    angles = []
    for a in "ABCD":
        v, s = sm.direction(a)
        sg = sm.stable_sign(a)
        angles.append(math.atan2(sg * s / sm.SCALE, sg * v) % (2 * math.pi))
    angles.sort()
    gaps = np.diff(angles + [angles[0] + 2 * math.pi])
    assert max(gaps) < math.pi


def test_regular_solution_solvus():
    assert rs.tc() == pytest.approx(rs.W / (2 * rs.R))
    for t in (700.0, 900.0, 1100.0):
        x1, x2, g1, g2 = rs.common_tangent_ok(t)
        # symmetric solution: the common tangent is horizontal, g equal at both limbs
        assert g1 == pytest.approx(g2, abs=1e-6)
        d = 1e-6
        slope = (float(rs.g_mix(x1 + d, t)) - float(rs.g_mix(x1 - d, t))) / (2 * d)
        assert slope == pytest.approx(0.0, abs=1e-3)
        # the binodal lies outside the spinodal
        assert rs.spinodal_t(x1) < t + 1e-6
        assert rs.binodal_t(x1) == pytest.approx(t, rel=1e-9)
    # lever rule
    x1, x2, fr = rs.section(900.0)
    assert x1 * (1 - fr) + x2 * fr == pytest.approx(rs.X0)
    assert rs.section(1200.0)[2] == 0.0

"""Tests for the anthropogenic climate change figure data (figdata/bachelor-2/anthropogenic.py)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import anthropogenic as an  # noqa: E402


def test_erf_table_matches_the_assessment():
    erf = an.read_erf()
    assert erf[0]["year"] == 1750 and erf[-1]["year"] == 2019
    last = erf[-1]
    # AR6 SPM A.4.1 / Table 7.8: 2.72 [1.96 to 3.48] W/m2 in 2019; CO2 2.16; aerosols -1.06
    assert last["anthro"] == pytest.approx(2.72, abs=0.005)
    assert last["anthro_p05"] == pytest.approx(1.96, abs=0.005)
    assert last["anthro_p95"] == pytest.approx(3.48, abs=0.005)
    assert last["co2"] == pytest.approx(2.16, abs=0.005)
    assert last["aerosol"] == pytest.approx(-1.06, abs=0.005)
    # the components add up to the total within the small 'other' term of the table
    for r in erf:
        s = r["co2"] + r["other_ghg"] + r["aerosol"] + r["other_anthro"]
        assert s == pytest.approx(r["anthro"], abs=0.02)
        assert r["anthro_p05"] <= r["anthro"] + 1e-9 or r["year"] == 1750


def test_energy_budget_estimates():
    lam = an.lambda_energy(0.59, 2.20, 1.03)
    assert lam == pytest.approx(-1.563, abs=1e-3)
    assert an.ecs(lam) == pytest.approx(2.5, abs=0.05)          # AR6: effective ECS 2.5
    assert an.tcr_energy(1.03, 2.20) == pytest.approx(1.84, abs=0.01)
    assert an.ecs(-1.16) == pytest.approx(3.39, abs=0.01)
    # equilibrium: dN = 0 when dT = -dF/lambda
    assert an.lambda_energy(0.0, 3.93, an.ecs(-1.16)) == pytest.approx(-1.16)


def test_planck_response_is_the_derivative_of_the_emission():
    g, t, h = 0.4, 288.0, 1e-3
    emit = lambda x: (1 - g) * an.SIGMA * x ** 4  # noqa: E731
    assert an.planck(g, t) == pytest.approx(-(emit(t + h) - emit(t - h)) / (2 * h), rel=1e-8)
    assert an.planck() == pytest.approx(-3.25, abs=0.01)        # AR6: about -3.3


def test_co2_law_and_units():
    assert an.co2_forcing(278.0 * 2) == pytest.approx(an.F2X)
    assert an.co2_forcing(410.0) == pytest.approx(2.20, abs=0.005)
    assert an.per_pgc(0.45) == pytest.approx(1.65, abs=0.005)   # AR6: 1.65 degC per 1000 PgC
    assert an.per_pgc(0.27) == pytest.approx(1.0, abs=0.02)
    assert an.per_pgc(0.63) == pytest.approx(2.3, abs=0.02)


def test_remaining_budget():
    b1 = an.budget(1.5, 0.1)
    assert b1 == pytest.approx(512.2, abs=0.1)
    # 0.1 degC more non-CO2 warming costs 0.1/0.45 x 1000 = 222 GtCO2 (AR6: +-220)
    assert b1 - an.budget(1.5, 0.2) == pytest.approx(222.2, abs=0.1)
    # with no non-CO2 warming, no Earth-system term and no recent emissions, the budget
    # is the TCRE line read at the limit
    assert an.budget(1.5, 0.0, e_since=0, esf=0) == pytest.approx(0.43 / 0.45 * 1000)
    assert math.isclose(an.budget(an.T_HIST, 0.0, e_since=0), 0.0, abs_tol=1e-9)

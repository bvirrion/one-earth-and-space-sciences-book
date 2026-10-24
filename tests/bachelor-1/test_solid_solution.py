"""Tests for figdata/bachelor-1/solid_solution.py (rock-forming-minerals)."""
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "bachelor-1"))
import solid_solution as S  # noqa: E402


def test_end_members_match_ledger_densities():
    assert abs(S.density(1.0) - 3.275) < 1e-12        # hom:forsterite
    assert abs(S.density(0.0) - 4.392) < 1e-12        # hom:fayalite
    assert abs(S.m_fo() - 140.691) < 1e-9 and abs(S.m_fa() - 203.771) < 1e-9


def test_molar_volume_linear_density_not():
    v = [S.molar_volume(i / 10) for i in range(11)]
    d = [v[i + 1] - v[i] for i in range(10)]
    assert max(d) - min(d) < 1e-12
    # the density lies above the straight line by x(1-x)(rho1-rho2)(V1-V2)/V
    for i in range(1, 10):
        x = i / 10
        lin = x * S.RHO_FO + (1 - x) * S.RHO_FA
        gap = x * (1 - x) * (S.RHO_FO - S.RHO_FA) * (S.v_fo() - S.v_fa()) / S.molar_volume(x)
        assert abs(S.density(x) - lin - gap) < 1e-12 and gap > 0


def test_pure_forsterite_recalculates_exactly():
    m = S.m_fo()
    wt = {"SiO2": 100 * S.molar_mass_oxide("SiO2") / m, "MgO": 100 * 2 * S.molar_mass_oxide("MgO") / m}
    cat, _, _ = S.cations(wt)
    assert abs(cat["Si"] - 1) < 1e-12 and abs(cat["Mg"] - 2) < 1e-12


def test_problem_olivine_is_stoichiometric_fo82():
    cat, _, _ = S.cations(S.OLIVINE_WT)
    assert abs(sum(cat.values()) - 3.0) < 1e-3       # 3 cations on 4 oxygens: no Fe3+
    assert abs(cat["Si"] - 1.0) < 1e-3
    assert round(S.forsterite_percent(cat)) == 82    # the problem's named number

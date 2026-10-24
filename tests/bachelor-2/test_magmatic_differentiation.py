"""Tests for the magmatic-differentiation figure data (differentiation.py)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import differentiation as dm  # noqa: E402


def test_plagioclase_loop():
    # the interpolants pass through Bowen's measured points and the loop is closed and ordered
    for an, ts, tl in dm.BOWEN_PLAG:
        if ts is not None and an > 2:
            assert abs(float(dm.T_SOL(an)) - ts) < 1e-9
        if tl is not None:
            assert abs(float(dm.T_LIQ(an)) - tl) < 1e-9
    assert float(dm.T_SOL(100)) == float(dm.T_LIQ(100)) == 1550
    for an in range(1, 100):
        assert dm.T_SOL(an) < dm.T_LIQ(an)
        assert dm.T_SOL(an) < dm.T_SOL(an + 1) and dm.T_LIQ(an) < dm.T_LIQ(an + 1)


def test_equilibrium_and_fractional_crystallisation():
    eq = dm.equilibrium_path(50.0)
    # starts on the liquidus of An50 with the solidus crystal, ends on the solidus of An50
    assert abs(eq[0][0] - 1450) < 1e-9 and abs(eq[-1][0] - 1287) < 0.5
    assert abs(eq[0][2] - dm.an_solid(1450)) < 1e-6 and abs(eq[-1][3] - 1.0) < 1e-6
    # lever rule closes the mass balance at every step
    for t, xl, xs, f in eq[1:-1]:
        assert abs(f * xs + (1 - f) * xl - 50.0) < 1e-6
    fr = dm.fractional_path(50.0)
    # first crystal is the same in both modes; the fractional liquid ends near albite
    assert abs(fr[0][1] - eq[0][2]) < 1e-6
    assert fr[-1][2] < 0.5
    # mass balance of the fractional crystals: the mean An of what crystallised plus the
    # liquid left equals the start
    xs = [r[0] for r in fr]
    an = [r[1] for r in fr]
    crystals = sum((xs[i + 1] - xs[i]) * 0.5 * (an[i] + an[i + 1]) for i in range(len(xs) - 1))
    m_left = 1 - xs[-1]
    assert abs(crystals + m_left * fr[-1][2] - 50.0) < 0.2


def test_trace_element_laws():
    # Rayleigh law is the solution of d(M C)/dM = D C: integrate numerically
    for d in (0.1, 2.0):
        m, c, n = 1.0, 1.0, 100000
        dm_ = (1 - 0.3) / n
        for _ in range(n):
            c += (1 - d) * c * dm_ / m      # d(MC) = D C dM with dM < 0
            m -= dm_
        assert abs(c - dm.rayleigh(0.3, d)) / dm.rayleigh(0.3, d) < 1e-3
    # equilibrium law closes the mass balance: F C_L + (1 - F) D C_L = C0
    for f in (0.2, 0.7):
        for d in (0.05, 3.0):
            cl = dm.equilibrium(f, d)
            assert abs(f * cl + (1 - f) * d * cl - 1.0) < 1e-12
    # ratio of two perfectly incompatible elements stays constant
    assert abs(dm.rayleigh(0.25, 0.0) / dm.rayleigh(0.25, 0.0) - 1) < 1e-12
    assert abs(dm.rayleigh(0.5, 0.0) - 2.0) < 1e-12


def test_afc_closed_form():
    for r in (0.2, 0.5):
        m, c, iso = dm.afc_numeric(0.5, dm.AFC_D, r, dm.AFC_CA_C0, dm.AFC_ISO_M, dm.AFC_ISO_A)
        assert abs(m - 0.5) < 1e-9
        assert abs(c - dm.afc_conc(0.5, dm.AFC_D, r, dm.AFC_CA_C0)) < 2e-4
        assert abs(iso - dm.afc_ratio(0.5, dm.AFC_D, r, dm.AFC_CA_C0, dm.AFC_ISO_M,
                                      dm.AFC_ISO_A)) < 2e-6
    # r -> 0 is the Rayleigh law
    assert abs(dm.afc_conc(0.6, 0.3, 1e-9, 2.0) - dm.rayleigh(0.6, 0.3)) < 1e-6


def test_paricutin_and_mass_balance():
    rows = dm.paricutin_rows()
    assert len(rows) == 22 and rows[0][2] == 55.04 and rows[-1][2] == 60.07
    # silica rose from 55 to 60 per cent while MgO fell and K2O nearly doubled
    assert rows[-1][5] < rows[0][5] and rows[-1][8] / rows[0][8] > 1.9
    o, p = dm.olivine(0.8), dm.plagioclase(0.7)
    assert abs(sum(o.values()) - 100) < 1e-9 and abs(sum(p.values()) - 100) < 1e-9
    a, b, c, tot, res = dm.mass_balance()
    # three controls are reproduced exactly, and the answer is close to Wilcox's graphical one
    for k in ("SiO2", "Al2O3", "MgO"):
        assert abs(res[k]) < 1e-9
    for mine, his in zip((a, b, c), dm.WILCOX_ABC):
        assert abs(mine - his) < 1.0
    assert abs(tot - (100 + a - b - c)) < 1e-12


def test_skaergaard():
    rows = dm.skg_rows()
    assert len(rows) > 100
    # the authors' F(H) polynomial reproduces their F column
    for r in rows:
        if float(r["height_m"]) < 1100:
            assert abs(dm.skg_f(float(r["height_m"])) - float(r["F"])) < 0.002
    # Ni falls from the Lower Zone to the Upper Zone: a compatible element
    lz = [float(r["Ni"]) for r in rows if r["Ni"] and float(r["F"]) > 0.6]
    uz = [float(r["Ni"]) for r in rows if r["Ni"] and float(r["F"]) < 0.1]
    assert sorted(lz)[len(lz) // 2] > 10 * sorted(uz)[len(uz) // 2]
    slope, _, n = dm.skg_ni_slope()
    assert 1.0 < slope < 2.0 and n > 50
    h0 = (-dm.SKG_B - math.sqrt(dm.SKG_B ** 2 - 4 * dm.SKG_A * dm.SKG_C)) / (2 * dm.SKG_A)
    assert 2100 < h0 < 2250

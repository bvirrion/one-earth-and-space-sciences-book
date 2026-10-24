"""Tests for the planet-formation figure data (nebula.py, condensation.py, al26.py,
meteorites.py)."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import al26  # noqa: E402
import condensation as cond  # noqa: E402
import meteorites as met  # noqa: E402
import nebula as neb  # noqa: E402


def test_mmsn_mass_matches_source():
    # Chiang and Youdin: eq. (1) integrated to 100 au gives 0.03 solar masses
    assert abs(neb.disc_mass(100) / neb.M_SUN - 0.03) < 0.002
    # direct numerical integral of 2 pi r Sigma dr agrees with the closed form
    n, R = 20000, 30.0
    s = sum(2 * math.pi * (r * neb.AU) * neb.sigma_gas(r) * (R / n * neb.AU)
            for r in ((i + 0.5) * R / n for i in range(n)))
    assert abs(s / neb.disc_mass(R) - 1) < 1e-2   # midpoint rule, integrable r^-1/2 at 0


def test_snow_lines():
    # Chiang and Youdin: water ice outside ~0.4 au, methane outside ~12 au
    assert abs(neb.r_passive(neb.T_WATER) - 0.4) < 0.05
    assert abs(neb.r_passive(neb.T_METHANE) - 12) < 0.5
    assert abs(neb.t_passive(neb.r_passive(150.0)) - 150.0) < 1e-9
    assert abs(neb.t_grain(neb.r_grain(182.0)) - 182.0) < 1e-9


def test_isolation_mass_definition():
    # at the isolation mass the annulus of width 5 R_H holds exactly the embryo's mass
    r, z = 5.2, 1.0
    m = neb.isolation_mass(r, z)
    rh = (m / (3 * neb.M_SUN)) ** (1 / 3) * r * neb.AU
    annulus = 2 * math.pi * r * neb.AU * 5 * rh * neb.sigma_solid(r, z)
    assert abs(annulus / m - 1) < 1e-12
    # scaling M ~ Sigma^(3/2)
    assert abs(neb.isolation_mass(r, z, factor=4) / m - 8) < 1e-9


def test_condensation_groups():
    r = cond.ranked()
    assert [t for _, t, _ in r] == sorted(t for _, t, _ in r)
    g = {n: cond.group(t) for _, t, n in r}
    assert g["Al"] == "ultra" and g["Ca"] == "high" and g["Mg"] == "common"
    assert g["Fe"] == "common" and g["Na"] == "modvol" and g["S"] == "vol" and g["C"] == "hivol"
    assert g["P"] == "modvol" and g["Pt"] == "refr"


def test_al26_relative_age_and_heating():
    # one mean life later the ratio has fallen by e
    assert abs(al26.ratio(al26.TAU) * math.e / al26.R0 - 1) < 1e-12
    assert abs(al26.relative_age(al26.ratio(2.0 * al26.MYR)) / al26.MYR - 2.0) < 1e-9
    # half-life 0.717 Myr from the mean life 1.035 Myr
    assert abs(al26.TAU * math.log(2) / al26.MYR - 0.717) < 0.002
    # the critical time inverts the peak temperature
    for T in (750.0, 1200.0, 1700.0):
        assert abs(al26.peak(al26.critical_time(T)) - T) < 1e-6
    # dT/dt at accretion equals H0 exp(-t_a/tau) / c
    ta, h = 1.0 * al26.MYR, 1e3 * al26.YR
    slope = (al26.temperature(ta + h, ta) - al26.temperature(ta, ta)) / h
    assert abs(slope / (al26.H0 * math.exp(-ta / al26.TAU) / al26.C) - 1) < 1e-3


def test_meteorite_fractions():
    rows = met.load()
    fr, nf, nd = met.fractions(rows)
    assert nf == 1107 and nd == 44534
    assert abs(sum(r[2] for r in fr) - 100) < 1e-9
    assert fr[0][1] == "ordinary" and fr[0][2] > 75


def test_meteorite_chondrite_share():
    # "achondrite" must not count as a chondrite (substring trap)
    rows = met.load()
    by = {g: r for g, *r in rows}
    nf = sum(r[1] for r in rows)
    chond = sum(by[g][0] for g in by if g.endswith(" chondrite"))
    assert "HED achondrite" in by and by["HED achondrite"][0] > 0
    assert abs(100.0 * chond / nf - 83.02) < 0.01
    assert 100.0 * by["ordinary chondrite"][0] / nf > 75     # "three in four"

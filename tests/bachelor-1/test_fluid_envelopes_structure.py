"""Tests for the fluid-envelopes-structure figures: the standard atmosphere with its
potential temperature, and the seawater equation of state with the T-S diagrams."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import atmosphere_profile as atm  # noqa: E402
import seawater_eos as eos  # noqa: E402


# ------------------------------------------------------------ atmosphere
def test_standard_atmosphere_check_values():
    assert abs(atm.temperature_h(11.0) - 216.65) < 1e-9
    assert abs(atm.pressure_h(11.0) - 22632.0) < 1.0
    assert abs(atm.pressure_h(20.0) - 5474.9) < 0.1
    assert abs(atm.temperature_h(32.0) - 228.65) < 1e-9


def test_hydrostatic_integration_matches_closed_forms():
    for h in (5.0, 11.0, 15.0, 20.0, 27.0, 32.0, 45.0):
        assert abs(atm.hydrostatic_pressure(h) / atm.pressure_h(h) - 1) < 1e-9


def test_dry_adiabat_and_kappa():
    assert abs(atm.KAPPA - 2.0 / 7.0) < 1e-12
    assert abs(atm.CP - 1004.69) < 0.01
    assert abs(atm.GAMMA_D - 9.761) < 1e-3
    # along the dry adiabat T p^-kappa is constant, so theta is constant
    t, p = 300.0, 95000.0
    t2, p2 = t * (60000.0 / p) ** atm.KAPPA, 60000.0
    assert abs(atm.theta(t, p) - atm.theta(t2, p2)) < 1e-9
    assert abs(atm.theta(290.0, atm.P_REF) - 290.0) < 1e-12


def test_theta_increases_with_height_in_the_standard_atmosphere():
    zs = [0.25 * i for i in range(0, 129)]
    th = [atm.theta_at(z) for z in zs]
    assert all(b > a for a, b in zip(th, th[1:]))
    # the stratosphere is far more stable than the troposphere
    assert atm.buoyancy_frequency(216.65, 0.0) > 1.9 * atm.buoyancy_frequency(288.15, 6.5)


def test_stability_criterion_equivalence():
    """N^2 = (g/T)(Gamma_d - Gamma) and N^2 = (g/theta) dtheta/dz agree."""
    for z in (2.0, 6.0, 15.0, 25.0):
        dz = 1e-4
        dth = (atm.theta_at(z + dz) - atm.theta_at(z - dz)) / (2 * dz * 1000.0)
        n2_theta = atm.G0 / atm.theta_at(z) * dth
        dt = (atm.temperature(z + dz) - atm.temperature(z - dz)) / (2 * dz)
        n2_gamma = atm.G0 / atm.temperature(z) * (atm.GAMMA_D + dt) / 1000.0
        assert abs(n2_theta / n2_gamma - 1) < 0.01


# ------------------------------------------------------------ seawater
def test_unesco_check_values():
    assert abs(eos.rho0(35.0, 0.0) - 1028.1063) < 5e-5
    assert abs(eos.theta(40.0, 40.0, 10000.0, 0.0) - 36.89073) < 5e-6
    assert abs(eos.atg(40.0, 40.0, 10000.0) - 3.255976e-4) < 5e-11
    assert abs(eos.depth(10000.0, 30.0) - 9712.653) < 5e-4


def test_pressure_inverts_depth():
    for z in (10.0, 1000.0, 4000.0):
        assert abs(eos.depth(eos.pressure(z, -30.5), -30.5) - z) < 1e-6


def test_linear_eos_near_reference_and_signs():
    s0, t0 = 35.0, 10.0
    assert eos.alpha(s0, t0) > 0 and eos.beta(s0, t0) > 0
    for ds, dt in ((0.2, 1.0), (-0.3, -1.5)):
        exact = eos.rho0(s0 + ds, t0 + dt)
        lin = eos.rho_linear(s0 + ds, t0 + dt, s0, t0)
        assert abs(exact - lin) < 0.02
    # alpha grows strongly with temperature, beta barely changes
    assert eos.alpha(35, 25) > 5 * eos.alpha(35, 0)
    assert abs(eos.beta(35, 25) / eos.beta(35, 0) - 1) < 0.07


def test_isopycnals_are_isopycnal_and_curved():
    for sg in eos.SIGMAS:
        line = eos.isopycnal(sg)
        assert all(abs(eos.sigma(s, th) - sg) < 1e-8 for s, th in line)
    a, b, m, sm = eos.cabbeling()
    assert abs(eos.sigma(*a) - eos.CAB_SIGMA) < 1e-8 and abs(eos.sigma(*b) - eos.CAB_SIGMA) < 1e-8
    assert sm > eos.CAB_SIGMA + 0.1          # the mixture is denser: cabbeling


def test_mixing_line_is_straight():
    a, b = (34.3, 4.3), (35.5, 15.4)
    pts = [eos.mix(a, b, f / 10.0) for f in range(11)]
    for s, th in pts:
        cross = (s - b[0]) * (a[1] - b[1]) - (th - b[1]) * (a[0] - b[0])
        assert abs(cross) < 1e-12


def test_south_atlantic_water_masses():
    """Salinity minimum near 800-1000 m and maximum near 2000-3000 m at 30.5 S (Tomczak's
    description); the 10.5 S maximum is shallower than the 30.5 S one."""
    m = dict(eos.masses())
    assert 700 <= m["AAIW"][0] <= 1100 and m["AAIW"][3] < 34.4
    assert 2000 <= m["NADW"][0] <= 3200 and m["NADW"][3] > 34.85
    assert m["AABW"][2] < 1.0
    sa10 = eos.profile("sa10")
    zmax10 = eos.extreme(sa10, 1200, 3500, "max")[0]
    assert zmax10 < m["NADW"][0]
    for site in eos.SITES:
        prof = eos.profile(site)
        assert all(r[2] <= eos.T68 * 40 for r in prof)
        assert all(abs(r[1] - r[0]) / max(r[0], 1.0) < 0.03 for r in prof)
    arctic = eos.profile("arctic")
    assert arctic[0][3] < 29 and [r for r in arctic if r[0] == 300.0][0][3] > 34.5
    assert math.isfinite(arctic[0][4])

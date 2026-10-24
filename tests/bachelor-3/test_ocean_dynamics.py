"""Tests for the wind-driven gyre and tide scripts (Year 3, ch. 21)."""
import cmath
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import tides  # noqa: E402
import wind_driven_gyre as gyre  # noqa: E402


def test_curl_and_pumping_against_finite_differences():
    """curl and w_E on the sphere agree with centred differences of their definitions."""
    a = gyre.A_EARTH
    for lat in (25.0, 35.0, 44.0):
        h = 1e-4
        p = math.radians(lat)

        def tc(la):
            return gyre.tau(la) * math.cos(math.radians(la))

        def tf(la):
            return gyre.tau(la) * math.cos(math.radians(la)) / (gyre.RHO * gyre.coriolis(la))

        dp = math.radians(2 * h)
        curl = -(tc(lat + h) - tc(lat - h)) / dp / (a * math.cos(p))
        we = -(tf(lat + h) - tf(lat - h)) / dp / (a * math.cos(p))
        assert gyre.curl_tau(lat) == pytest.approx(curl, rel=1e-6)
        assert gyre.ekman_pumping(lat) == pytest.approx(we, rel=1e-6)


def test_sverdrup_closes_the_mass_budget():
    """Ekman transports converge into the gyre (pumping down), the Sverdrup
    interior goes south, and at the centre sphere and beta-plane agree."""
    assert gyre.ekman_transport_y(20.5) > 0 > gyre.ekman_transport_y(49.5)
    assert gyre.ekman_pumping(35.0) < 0
    assert gyre.sverdrup_v(35.0) < 0
    assert -gyre.sverdrup_v(35.0) == pytest.approx(gyre.plane_amplitude(), rel=1e-9)
    assert gyre.plane_amplitude() * gyre.WIDTH / 1e6 == pytest.approx(29.4, abs=0.05)


def test_boundary_layers_satisfy_their_equations():
    """Stommel: r psi'' + beta psi' = curl/rho; Munk: beta psi' = curl/rho + A_H psi''''
    (x-derivatives only, the boundary-layer approximation), with psi from the
    cumulative transport; both vanish at the wall, Munk with no slip."""
    b, a = gyre.beta(35.0), gyre.plane_amplitude()
    curl_over_rho = -a * b
    for x in (20e3, 60e3, 150e3):
        h = 1.0
        vs = gyre.stommel_v
        dvs = (vs(x + h) - vs(x - h)) / (2 * h)
        assert gyre.R_FRIC * dvs + b * vs(x) == pytest.approx(curl_over_rho, rel=1e-6)
        vm = gyre.munk_v
        h3 = 200.0
        d3 = (vm(x + 2 * h3) - 2 * vm(x + h3) + 2 * vm(x - h3) - vm(x - 2 * h3)) / (2 * h3 ** 3)
        peak = b * max(abs(vm(xx * 1e3)) for xx in range(0, 300, 5))
        assert abs(b * vm(x) - gyre.A_H * d3 - curl_over_rho) < 1e-5 * peak
    assert gyre.stommel_cum(0.0) == 0.0 and gyre.munk_cum(0.0) == 0.0
    assert gyre.munk_v(0.0) == pytest.approx(-a)            # no slip: only the tiny interior term
    assert gyre.munk_v(gyre.munk_first_zero() * 0.999) > -a
    assert gyre.munk_first_zero() / 1e3 == pytest.approx(233.5, abs=0.5)


def test_equilibrium_tide():
    k = tides.tide_scale()
    assert k == pytest.approx(0.3568, abs=2e-4)
    # high under the Moon and opposite, low on the great circle between
    assert tides.eq_tide(0.0, 0.0, 0.0) == pytest.approx(k)
    assert tides.eq_tide(0.0, 0.0, 180.0) == pytest.approx(k)
    assert tides.eq_tide(0.0, 0.0, 90.0) == pytest.approx(-k / 2)
    # mean over the sphere is zero (mass conserved)
    n = 400
    s = 0.0
    for i in range(n):
        mu = -1 + (i + 0.5) * 2 / n
        s += tides.p2(mu) * 2 / n
    assert s == pytest.approx(0.0, abs=1e-5)
    # declination makes the two daily high waters unequal at 45 N
    assert tides.eq_tide(45.0, 20.0, 0.0) > tides.eq_tide(45.0, 20.0, 180.0)
    assert tides.eq_tide(45.0, 0.0, 0.0) == pytest.approx(tides.eq_tide(45.0, 0.0, 180.0))


def test_kelvin_wave_and_amphidromes():
    for r in tides.kelvin_check():
        assert abs(r) < 1e-6
    assert tides.kelvin_speed(4000.0) == pytest.approx(198.1, abs=0.1)
    # |Z| vanishes at the amphidromes
    for x, y in tides.amphidromes():
        assert abs(tides.channel_z(x, y)) < 1e-9
    # high water turns anticlockwise round an amphidrome (northern hemisphere):
    # arg Z grows from east to north to west to south
    x0, y0 = tides.amphidromes()[1]
    d = 20e3
    args = [cmath.phase(tides.channel_z(x0 + dx, y0 + dy))
            for dx, dy in ((d, 0), (0, d), (-d, 0), (0, -d))]
    steps = [(args[(i + 1) % 4] - args[i]) % (2 * math.pi) for i in range(4)]
    assert all(0 < s < math.pi for s in steps)
    assert sum(steps) == pytest.approx(2 * math.pi)

"""Tests for the exoplanet scripts (Year 3, ch. 28)."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-3"))
import exoplanet_archive as ea  # noqa: E402
import rv_transit as rt  # noqa: E402


def test_semi_amplitude_of_the_sun_and_51_peg():
    # the Sun moves at about 13 m/s around the Sun-Jupiter barycentre (nobel19:sun-jupiter)
    k = rt.semi_amplitude(rt.M_JUP, rt.M_SUN, 4331 * rt.DAY, 0.049)
    assert k == pytest.approx(12.5, abs=0.1)
    # 51 Peg b: K = 59 m/s, P = 4.23 d gives about 0.47 Jupiter masses for a Sun-like star
    m = rt.minimum_mass(59.0, rt.M_SUN, 4.23 * rt.DAY)
    assert m / rt.M_JUP == pytest.approx(0.47, abs=0.01)
    # minimum_mass inverts semi_amplitude, eccentric orbits included
    for e in (0.0, 0.3, 0.6):
        k = rt.semi_amplitude(8 * rt.M_EARTH, 0.8 * rt.M_SUN, 12 * rt.DAY, e)
        assert rt.minimum_mass(k, 0.8 * rt.M_SUN, 12 * rt.DAY, e) == pytest.approx(
            8 * rt.M_EARTH, rel=1e-9)


def test_kepler_equation_and_zero_mean_velocity():
    for e in (0.0, 0.3, 0.8, 0.95):
        for mean in (0.1, 1.0, 3.0, 5.5):
            big_e = rt.ecc_anomaly(mean, e)
            assert big_e - e * math.sin(big_e) == pytest.approx(mean, abs=1e-12)
    # over one period, the star returns to its place: the time average of v_r is zero
    n = 20000
    mean_v = sum(rt.radial_velocity(i / n, 30.0, 0.3, 1.0) for i in range(n)) / n
    assert abs(mean_v) < 1e-6
    vs = [rt.radial_velocity(i / 2000, 30.0, 0.3, 1.0) for i in range(2000)]
    # the extremes are K (1 + e cos w) and -K (1 - e cos w): the amplitude is 2K
    assert max(vs) - min(vs) == pytest.approx(60.0, rel=1e-3)
    assert max(vs) == pytest.approx(30.0 * (1 + 0.3 * math.cos(1.0)), rel=1e-3)


def test_overlap_area_and_numerical_blocked_flux():
    assert rt.overlap_area(0.0, 0.1) == pytest.approx(math.pi * 0.01)
    assert rt.overlap_area(1.2, 0.1) == 0.0
    # half the planet's disc is inside at z = 1 for a small planet
    assert rt.overlap_area(1.0, 0.01) == pytest.approx(0.5 * math.pi * 1e-4, rel=5e-3)
    for z in (0.0, 0.5, 0.95, 1.0, 1.05):
        assert rt.blocked_flux(z, 0.1, 0.0, 0.0) == pytest.approx(rt.overlap_area(z, 0.1),
                                                                rel=1e-4, abs=1e-9)
    # a planet as large as the star, centred: the whole disc is hidden
    assert rt.blocked_flux(0.0, 1.0, 0.4, 0.25) == pytest.approx(rt.total_flux(0.4, 0.25),
                                                                rel=1e-5)


def test_limb_darkened_depth_and_durations():
    # small planet at the centre: depth = p^2 I(centre) / mean intensity
    p = 0.02
    depth = 1 - rt.transit_flux(0.0, p, 0.4, 0.25)
    assert depth == pytest.approx(p * p / (1 - 0.4 / 3 - 0.25 / 6), rel=1e-3)
    # near the limb the same planet hides less light than a uniform star would
    assert 1 - rt.transit_flux(0.9, p, 0.4, 0.25) < p * p
    t14, t23 = rt.durations(10.0, 15.0, 0.3, 0.1)
    assert t14 > t23 > 0
    # central transit, wide orbit: T14 -> P (1 + p) / (pi a/R)
    t14, _ = rt.durations(365.0, 215.0, 0.0, 0.01)
    assert t14 == pytest.approx(365.0 * 1.01 / (math.pi * 215.0), rel=1e-4)


def test_microlensing():
    assert rt.magnification(1.0) == pytest.approx(3 / math.sqrt(5))
    assert rt.magnification(0.01) == pytest.approx(100.0, rel=1e-3)
    assert rt.magnification(10.0) == pytest.approx(1.0, abs=1e-3)
    th = rt.einstein_angle(0.5 * rt.M_SUN, 4000 * rt.PC, 8000 * rt.PC)
    assert th == pytest.approx(math.sqrt(2 * rt.G * rt.M_SUN / rt.C ** 2 / (8000 * rt.PC)))


def test_archive_selections():
    rows = ea.load_planets()
    assert len(rows) == 6451
    mr = ea.mass_radius(rows)
    assert len(mr) > 1000 and all(m > 0 and r > 0 for m, r in mr)
    pr = ea.period_radius(rows)
    assert all(1 <= p <= 100 for p, _ in pr)
    hist = ea.radius_histogram(pr)
    assert sum(n for *_, n in hist) == sum(1 for _, r in pr if 0.8 <= r < 4.0)
    # the radius valley: the bin at 1.8-1.9 Earth radii holds fewer planets than the
    # peaks on either side (Fulton et al. 2017 place the gap at 1.5-2.0)
    n_at = {round(mid, 1): n for _, _, mid, n in hist}
    assert n_at[1.9] < n_at[1.5] and n_at[1.9] < 0.5 * n_at[2.6]
    counts = ea.method_counts(rows)
    assert counts["Transit"] > counts["Radial Velocity"] > counts["Microlensing"]
    assert sum(counts.values()) == 6451


def test_model_curves_and_solar_system():
    def at(key, m):
        """Radius at mass m, interpolated linearly in log M, log R."""
        pts = ea.zeng_curve(key, 0.0, 1e9)
        for (m0, r0), (m1, r1) in zip(pts, pts[1:]):
            if m0 <= m <= m1:
                f = math.log(m / m0) / math.log(m1 / m0)
                return math.exp(math.log(r0) + f * math.log(r1 / r0))
        raise ValueError(m)
    # the Earth-like model passes through the Earth
    assert at("earthlike", 1.0) == pytest.approx(1.0, abs=0.03)
    # at a given mass, iron is smaller than Earth-like rock, which is smaller than 50 % water
    assert at("iron", 5) < at("earthlike", 5) < at("water50", 5) < at("h2-2pc", 5)
    solar = {n: (m, r, a) for n, m, r, a in ea.solar_system()}
    assert solar["Earth"] == pytest.approx((1.0, 1.0, 1.0), abs=1e-4)
    assert solar["Jupiter"][0] == pytest.approx(318, abs=1)

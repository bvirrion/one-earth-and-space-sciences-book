"""Tests for the plate-kinematics figure data: velocities from Euler vectors,
finite rotations of the South Atlantic fit, and the striped sea floor."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import euler_velocities as ev  # noqa: E402
import gpts_stripes as gs  # noqa: E402
import south_atlantic_fit as sf  # noqa: E402


def test_speed_is_omega_r_sin_delta():
    w = ev.morvel_eu_na()
    for lat, lon in [(64.5, -18.0), (39.44, -29.83), (0.0, 0.0), (-30.0, 100.0)]:
        s, _ = ev.speed_azimuth(w, lat, lon)
        assert abs(s - ev.speed_formula(*ev.MORVEL_EU_NA, lat, lon)) < 1e-9


def test_velocity_vanishes_at_the_pole_and_peaks_at_ninety_degrees():
    w = ev.morvel_eu_na()
    plat, plon, rate = ev.MORVEL_EU_NA
    assert ev.speed_azimuth(w, plat, plon)[0] < 1e-9
    peak = math.radians(rate) / 1e6 * 6371e6
    # a point 90 degrees from the pole moves at omega R
    lat90 = plat - 90.0
    assert abs(ev.speed_azimuth(w, lat90, plon)[0] - peak) < 1e-6


def test_velocity_is_perpendicular_to_the_position_vector():
    w = ev.morvel_eu_na()
    r = ev.unit(64.5, -18.0)
    v = ev.cross(w, r)
    assert abs(ev.dot(v, r)) < 1e-18


def test_morvel_matches_pb2002_along_the_ridge():
    assert ev.mean_relative_difference() < 0.15


def test_iceland_rate_and_direction():
    s, az = ev.speed_azimuth(ev.morvel_eu_na(), *ev.POINTS["iceland"])
    assert 18.0 < s < 19.0 and 95.0 < az < 110.0


def test_relative_vectors_add():
    w_eu_na = ev.morvel_eu_na()
    w_nb_na = ev.euler_vector(*ev.MORVEL_NB_NA)
    w_nb_eu = ev.relative(w_nb_na, w_eu_na)
    assert all(abs(a + b - c) < 1e-24 for a, b, c in zip(w_nb_eu, w_eu_na, w_nb_na))
    # velocities add at every point too: v_EU-NA = v_EU-NB + v_NB-NA at the Azores junction
    lat, lon = ev.POINTS["atj"]
    v1 = ev.velocity_en(w_eu_na, lat, lon)
    v2 = ev.velocity_en(ev.relative(w_eu_na, w_nb_na), lat, lon)
    v3 = ev.velocity_en(w_nb_na, lat, lon)
    assert abs(v1[0] - v2[0] - v3[0]) < 1e-9 and abs(v1[1] - v2[1] - v3[1]) < 1e-9


def test_gakkel_rates_match_the_published_range():
    # morvel:eu-na: rates rise from 11-12 mm/yr along the Gakkel Ridge
    for lat, lon in [(86.0, 60.0), (85.0, 0.0)]:
        assert 10.0 < ev.speed_azimuth(ev.morvel_eu_na(), lat, lon)[0] < 13.0


def test_rotation_matrix_is_orthogonal_with_unit_determinant():
    m = sf.rotation_matrix(*sf.ROT_120)
    mt = tuple(zip(*m))
    p = sf.matmul(m, mt)
    for i in range(3):
        for j in range(3):
            assert abs(p[i][j] - (i == j)) < 1e-12
    assert abs(sf.det(m) - 1.0) < 1e-12


def test_pole_is_fixed_and_points_stay_on_their_small_circle():
    lat, lon, ang = sf.ROT_120
    plat, plon = sf.rotate_point(sf.ROT_120, lat, lon)
    assert abs(plat - lat) < 1e-9 and abs(plon - lon) < 1e-9
    d0 = ev.angular_distance(lat, lon, -8.05, -34.9)
    q = sf.rotate_point(sf.ROT_120, -8.05, -34.9)
    assert abs(ev.angular_distance(lat, lon, *q) - d0) < 1e-9
    # and the point turned through the rotation angle about the pole
    n = sf.unit(lat, lon)
    a, b = sf.unit(-8.05, -34.9), sf.unit(*q)
    pa = [x - ev.dot(a, n) * y for x, y in zip(a, n)]
    pb = [x - ev.dot(b, n) * y for x, y in zip(b, n)]
    c = ev.dot(pa, pb) / (ev.norm(pa) * ev.norm(pb))
    assert abs(math.degrees(math.acos(c)) - ang) < 1e-6


def test_rotations_do_not_commute():
    a = sf.rotation_matrix(*sf.ROT_120)
    b = sf.rotation_matrix(0.0, 0.0, 30.0)
    ab, ba = sf.matmul(a, b), sf.matmul(b, a)
    assert max(abs(ab[i][j] - ba[i][j]) for i in range(3) for j in range(3)) > 0.05


def _nearest_africa(lat, lon):
    best = 1e9
    for piece in sf.africa():
        for plon, plat in piece:
            best = min(best, ev.angular_distance(lat, lon, plat, plon))
    return best


def test_recife_closes_onto_africa_at_120_ma():
    q = sf.rotate_point(sf.ROT_120, -8.05, -34.9)
    assert _nearest_africa(*q) < 2.5


def test_the_other_reading_of_the_table_does_not_close_the_ocean():
    lat, lon, ang = sf.ROT_120
    q = sf.rotate_point((lon, lat, ang), -8.05, -34.9)
    assert _nearest_africa(*q) > 15.0


def test_younger_rotation_leaves_a_narrow_ocean():
    q = sf.rotate_point(sf.ROT_84, -8.05, -34.9)
    d = _nearest_africa(*q)
    assert 5.0 < d < 20.0


def test_stripe_widths_are_rate_times_duration():
    for u in (10.0, 40.0):
        for (w, pol), (top, base, p2) in zip(gs.stripe_widths(u), gs.intervals()):
            assert pol == p2 and abs(w - u * (base - top)) < 1e-12
        rows = gs.stripes(u)
        xs = [x for x, _ in rows]
        assert all(a < b for a, b in zip(xs, xs[1:]))
        assert abs(xs[0] + u * gs.TMAX) < 1e-9 and abs(xs[-1] - u * gs.TMAX) < 1e-9


def test_stripes_are_symmetric_about_the_ridge():
    rows = gs.stripes(10.0)
    def pol_at(x):
        p = rows[0][1]
        for xi, pi in rows:
            if xi <= x:
                p = pi
        return p
    for x in (3.0, 15.0, 33.7, 52.0, 79.0, 100.0):  # away from block edges
        assert pol_at(x) == pol_at(-x + 1e-6) == gs.polarity_at(x / 10.0)


def test_polarity_alternates_and_the_present_is_normal():
    iv = gs.intervals()
    assert iv[0][2] == 1
    assert all(a[2] != b[2] for a, b in zip(iv, iv[1:]))
    assert 0.4 < gs.normal_fraction() < 0.6

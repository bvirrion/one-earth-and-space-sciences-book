"""Tests for the active-margins figure data: projection on a section, least-squares
slab line, small-circle fit of a trench, and the Kuril numbers printed in the text."""
import math
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import slab_seismicity as ss  # noqa: E402


def test_point_on_the_section_line_projects_exactly():
    lon0, lat0, az = 153.2, 45.7, 320.9
    for d in (10.0, 250.0, 700.0):
        lon, lat = ss.destination(lon0, lat0, az, d)
        x, y = ss.along_across(lon0, lat0, az, lon, lat)
        assert abs(x - d) < 1e-6
        assert abs(y) < 1e-6


def test_cross_track_distance_and_side():
    lon0, lat0, az = 153.2, 45.7, 320.9
    foot = ss.destination(lon0, lat0, az, 300.0)
    ahead = ss.destination(lon0, lat0, az, 300.001)
    # the azimuth of the track at the foot (it changes along a great circle)
    p1, p2 = math.radians(foot[1]), math.radians(ahead[1])
    dl = math.radians(ahead[0] - foot[0])
    local = math.degrees(math.atan2(math.sin(dl) * math.cos(p2),
                                    math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)))
    right = ss.destination(foot[0], foot[1], (local + 90.0) % 360.0, 120.0)
    left = ss.destination(foot[0], foot[1], (local - 90.0) % 360.0, 120.0)
    xr, yr = ss.along_across(lon0, lat0, az, *right)
    xl, yl = ss.along_across(lon0, lat0, az, *left)
    assert abs(yr - 120.0) < 1e-3 and abs(yl + 120.0) < 1e-3
    # the foot of the perpendicular stays at 300 km along the track
    assert abs(xr - 300.0) < 1e-3 and abs(xl - 300.0) < 1e-3


def test_least_squares_recovers_a_synthetic_dip():
    rng = random.Random(14)
    dip = 40.0
    pts = []
    for _ in range(200):
        x = rng.uniform(150.0, 700.0)
        pts.append((x, -50.0 + math.tan(math.radians(dip)) * x + rng.gauss(0.0, 15.0)))
    a, s = ss.lsq_line(pts)
    assert abs(math.degrees(math.atan(s)) - dip) < 0.5
    assert abs(a + 50.0) < 10.0
    # exact data give the exact line
    a, s = ss.lsq_line([(0.0, 1.0), (1.0, 3.0), (2.0, 5.0)])
    assert abs(a - 1.0) < 1e-12 and abs(s - 2.0) < 1e-12


def test_small_circle_fit_recovers_a_known_circle():
    pole = (130.0, 58.0)
    pts = [ss.destination(pole[0], pole[1], az, 20.0 * math.pi / 180.0 * ss.R_KM)
           for az in range(120, 200, 5)]
    lon, lat, radius = ss.small_circle(pts)
    assert abs(radius - 20.0) < 1e-6
    assert abs(lon - pole[0]) < 1e-5 and abs(lat - pole[1]) < 1e-5


def test_kuril_numbers():
    origin, toward, sec, volc, v = ss.analysis()
    assert abs(v["toward"] - 320.9) < 0.5            # NW, toward the Okhotsk plate
    assert 40.0 < v["dip"] < 50.0
    assert v["max_depth"] > 600.0                     # deep events beneath the Sea of Okhotsk
    # ledger syracuse:arc-depth: slab 72 to 173 km below arcs (500-km segment means)
    assert 72.0 < v["slab_depth_front"] < 173.0
    assert 150.0 < v["x_front"] < 180.0
    # Frank (1968): radius about half the dip, here within a degree
    assert abs(v["arc_radius"] - v["dip"] / 2.0) < 1.0
    assert 100.0 < v["age_in"] < 140.0


import trench_gravity as tg  # noqa: E402


def test_bilinear_interpolation_is_exact_on_a_plane():
    lons, lats = [0.0, 1.0, 2.0], [10.0, 11.0]
    tab = {(x, y): 3.0 * x - 2.0 * y + 1.0 for x in lons for y in lats}
    assert abs(tg.bilinear(lons, lats, tab, 1.25, 10.5) - (3.0 * 1.25 - 2.0 * 10.5 + 1.0)) < 1e-12
    assert tg.bilinear(lons, lats, tab, 2.5, 10.5) is None


def test_kuril_gravity_profile():
    rows = tg.profile()
    assert len(rows) > 120
    low, rise, deep, abyss, high = tg.extremes(rows)
    # the gravity low and the deepest point lie within 30 km of the PB2002 trench point
    assert abs(low[0]) <= 30.0 and abs(deep[0]) <= 30.0
    assert -300.0 < low[1] < -200.0
    # the outer rise is positive, the forearc and arc strongly positive
    assert 0.0 < rise[1] < 80.0 and -250.0 <= rise[0] <= -60.0
    assert high[1] > 100.0
    # the trench is some 3 to 4 km deeper than the abyssal floor seaward of it
    assert 3000.0 < deep[2] - abyss < 4000.0

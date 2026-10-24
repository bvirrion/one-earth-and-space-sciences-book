"""Tests for the earthquake-source figure data: the Gutenberg--Richter fit, the
focal mechanisms (auxiliary planes, first-motion signs, P and T axes, the
projection) and the interseismic velocity profile."""
import math
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1"))
import beachballs as bb  # noqa: E402
import gutenberg_richter as gr  # noqa: E402
import interseismic as isv  # noqa: E402


# --- Gutenberg--Richter ---------------------------------------------------------

def test_counts_equal_the_dataset():
    mags = gr.load_magnitudes()
    with open(gr.CSV, encoding="utf8") as f:
        rows = sum(1 for _ in f) - 1
    assert len(mags) == rows
    assert gr.cumulative_counts(mags, [6.0])[0] == rows
    counts = gr.cumulative_counts(mags, gr.magnitude_grid(6.0, 9.0))
    assert all(a >= b for a, b in zip(counts, counts[1:]))


def test_catalogue_b_value_is_near_one():
    a, b = gr.b_value(gr.load_magnitudes(), *gr.FIT_RANGE, years=gr.YEARS)
    assert 0.8 < b < 1.2
    assert 10 < 10 ** (a - 7 * b) < 20          # about 14 events of M >= 7 a year


def test_fit_recovers_b_on_a_synthetic_catalogue():
    rng = random.Random(7)
    beta = 1.0 * math.log(10)
    mags = [round(5.95 + rng.expovariate(beta) + 1e-9, 1) for _ in range(200000)]
    mags = [m for m in mags if m >= 6.0]
    _, b = gr.b_value(mags, 6.0, 7.5)
    assert abs(b - 1.0) < 0.05


def test_moment_from_magnitude():
    assert abs(math.log10(gr.seismic_moment(9.1)) - 22.75) < 1e-12
    # one unit of magnitude: 10**1.5 = 31.6 times the moment
    assert abs(gr.seismic_moment(7.0) / gr.seismic_moment(6.0) - 10 ** 1.5) < 1e-9


def test_moment_shares_are_a_decreasing_cdf():
    mags = gr.load_magnitudes()
    grid = gr.magnitude_grid(6.0, 9.1)
    sh = gr.moment_shares(mags, grid)
    assert abs(sh[0] - 1.0) < 1e-12
    assert all(a >= b for a, b in zip(sh, sh[1:]))
    assert sh[grid.index(8.0)] > 0.5            # the few largest dominate


# --- focal mechanisms ---------------------------------------------------------

def _close_plane(a, b, tol=1e-6):
    return (abs((a[0] - b[0] + 180) % 360 - 180) < tol and abs(a[1] - b[1]) < tol
            and abs((a[2] - b[2] + 180) % 360 - 180) < tol)


def test_auxiliary_plane_known_cases():
    # pure normal fault 000/60 (dipping east): the auxiliary plane dips 30 to the west
    assert _close_plane(bb.auxiliary_plane(0, 60, -90), (180, 30, -90))
    # pure thrust 000/30: auxiliary 180/60, also a reverse slip
    assert _close_plane(bb.auxiliary_plane(0, 30, 90), (180, 60, 90))
    # vertical dextral fault striking north: auxiliary plane strikes east, sinistral
    st, dp, rk = bb.auxiliary_plane(0, 90, 180)
    assert abs(dp - 90) < 1e-6 and abs(abs(rk) - 0) < 1e-6
    assert abs(st % 180 - 90) < 1e-6


def test_auxiliary_of_auxiliary_is_the_plane():
    rng = random.Random(3)
    for _ in range(200):
        p = (rng.uniform(0, 360), rng.uniform(5, 85), rng.uniform(-179, 179))
        assert _close_plane(bb.auxiliary_plane(*bb.auxiliary_plane(*p)), p, 1e-6)


def test_sumatra_planes_are_a_pair():
    # the Global CMT solution of 2004: 329/8/110 and 129/83/87, to the degree
    st, dp, rk = bb.auxiliary_plane(329, 8, 110)
    assert abs(st - 129) < 1.5 and abs(dp - 83) < 1.5 and abs(rk - 87) < 1.5


def test_quadrant_signs():
    down = (0.0, 0.0, -1.0)
    assert bb.first_motion(0, 30, 90, down) == 1        # thrust: push at the centre
    assert bb.first_motion(0, 60, -90, down) == -1      # normal: pull at the centre
    ne = (math.sqrt(0.5), math.sqrt(0.5), 0.0)
    nw = (-math.sqrt(0.5), math.sqrt(0.5), 0.0)
    # dextral fault striking north: compression in the NW and SE quadrants
    assert bb.first_motion(0, 90, 180, nw) == 1
    assert bb.first_motion(0, 90, 180, ne) == -1


def test_p_and_t_axes():
    p, t = bb.pt_axes(0, 45, 90)
    assert abs(bb.trend_plunge(t)[1] - 90) < 1e-6        # thrust at 45: T vertical
    tr, pl = bb.trend_plunge(p)
    assert abs(pl) < 1e-6 and abs(tr % 180 - 90) < 1e-6  # P horizontal, east-west
    p, t = bb.pt_axes(0, 45, -90)
    assert abs(bb.trend_plunge(p)[1] - 90) < 1e-6        # normal at 45: P vertical
    # a thrust dipping 30: P and T each 45 from both planes, P plunging 15 to the west
    p, t = bb.pt_axes(0, 30, 90)
    assert abs(bb.trend_plunge(p)[1] - 15) < 1e-6 and abs(bb.trend_plunge(t)[1] - 75) < 1e-6
    # a dextral fault striking north shortens the ground along NE-SW
    p, t = bb.pt_axes(0, 90, 180)
    assert abs(bb.trend_plunge(p)[0] % 180 - 45) < 1e-6
    for st, dp, rk in bb.MECHANISMS.values():
        p, t = bb.pt_axes(st, dp, rk)
        assert bb.first_motion(st, dp, rk, t) == 1
        assert bb.first_motion(st, dp, rk, p) == -1


def test_projection():
    assert bb.project((0.0, 0.0, -1.0)) == (0.0, 0.0)
    x, y = bb.project((1.0, 0.0, 0.0))
    assert abs(x - 1) < 1e-12 and abs(y) < 1e-12
    # equal area: radius sqrt 2 sin(theta/2) at theta from the vertical
    th = math.radians(50)
    x, y = bb.project((0.0, math.sin(th), -math.cos(th)))
    assert abs(y - math.sqrt(2) * math.sin(th / 2)) < 1e-12


def _inside(pts, x, y):
    c = False
    for i in range(len(pts)):
        (x1, y1), (x2, y2) = pts[i - 1], pts[i]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            c = not c
    return c


def _unproject(X, Y):
    U = X * X + Y * Y - 1.0            # from (X, Y) = (E, N) / sqrt(1 - U)
    f = math.sqrt(1.0 - U)
    return (X * f, Y * f, U)


def test_regions_are_compressional_and_cover_half_the_area():
    grid = [(-1 + 0.02 * i, -1 + 0.02 * j) for i in range(101) for j in range(101)]
    grid = [g for g in grid if g[0] ** 2 + g[1] ** 2 < 0.98]
    for name, (st, dp, rk) in bb.MECHANISMS.items():
        regs = bb.compressional_regions(st, dp, rk)
        total = 0.0
        for pts in regs:
            total += 0.5 * abs(sum(pts[i - 1][0] * pts[i][1] - pts[i][0] * pts[i - 1][1]
                                   for i in range(len(pts))))
        inside = pushes = 0
        for X, Y in grid:
            x = _unproject(X, Y)
            fm = bb.first_motion(st, dp, rk, x)
            isin = any(_inside(pts, X, Y) for pts in regs)
            n, d = bb.normal_and_slip(st, dp, rk)
            near = min(abs(bb.dot(n, x)), abs(bb.dot(d, x))) < 0.03
            if not near:
                assert isin == (fm == 1), (name, X, Y)
            inside += isin
            pushes += fm == 1
        # equal-area projection: the two compressional quadrants fill half the disc
        assert abs(total - math.pi / 2) < 0.01, name


# --- interseismic profile -----------------------------------------------------

def test_velocity_profile():
    V, D = 34.0, 15.0
    assert isv.velocity(0.0, V, D) == 0.0
    assert abs(isv.velocity(1e7, V, D) - V / 2) < 1e-3
    assert abs(isv.velocity(-1e7, V, D) + V / 2) < 1e-3
    assert abs(isv.velocity(D, V, D) - V / 4) < 1e-12
    assert abs(isv.locking_depth(30.0, isv.velocity(30.0, V, D), V) - D) < 1e-9
    # the strain rate is the derivative of the velocity
    h = 1e-3
    num = (isv.velocity(7 + h, V, D) - isv.velocity(7 - h, V, D)) / (2 * h)
    assert abs(num - isv.strain_rate(7.0, V, D)) < 1e-7

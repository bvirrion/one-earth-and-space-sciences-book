"""figdata/grade-11/moho_refraction.py: the head-wave formulas and the problem's data."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import moho_refraction as mr  # noqa: E402


def test_head_wave_time_equals_the_path_time():
    for x in (80.0, 150.0, 300.0):
        assert abs(mr.t_head(x) - mr.t_head_geometric(x)) < 1e-9


def test_crossover_is_where_the_two_lines_meet():
    xc = mr.crossover()
    assert abs(mr.t_direct(xc) - mr.t_head(xc)) < 1e-9
    assert xc > mr.critical_distance()


def test_depth_formula_inverts_the_intercept():
    assert abs(mr.depth_from(mr.intercept(), mr.V1, mr.V2) - mr.H) < 1e-9


def test_readings_give_back_the_model():
    n = mr.numbers()
    assert abs(n["fit_v1"] - mr.V1) < 0.1
    assert abs(n["fit_v2"] - mr.V2) < 0.15
    assert abs(n["fit_depth_km"] - mr.H) < 2.0


def test_readings_rounded_to_a_tenth():
    for _, pg, pn in mr.readings():
        for t in (pg, pn):
            if t == t:
                assert abs(t * 10 - round(t * 10)) < 1e-9


def test_critical_angle():
    assert abs(math.degrees(mr.critical_angle(6.0, 8.0)) - 48.59) < 0.01

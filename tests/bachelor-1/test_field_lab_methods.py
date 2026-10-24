"""Tests for figdata/bachelor-1/attitude_stats.py (field-lab-methods-1)."""
import math
import os
import sys

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "bachelor-1"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "figdata", "shared"))
import attitude_stats as A  # noqa: E402


def test_vector_mean_close_to_model():
    rs = A.readings()
    a, d, _ = A.vector_mean(rs)
    assert abs(a - 81) < 1.0 and abs(d - 12) < 1.0
    a, d, _ = A.vector_mean(rs[:12])
    assert round(a) == 81 and round(d) == 12          # the problem's named number, 081/12


def test_vector_mean_across_north():
    """The arithmetic mean of 355 and 005 is 180; the vector mean is 000."""
    a, d, _ = A.vector_mean([(355, 20), (5, 20)])
    assert min(a, 360 - a) < 1e-9 and abs(d - 20) < 0.2


def test_rbar_is_mean_cosine():
    rs = A.readings()
    a, d, rb = A.vector_mean(rs)
    th = A.angles_to(rs, a, d)
    assert abs(rb - sum(math.cos(math.radians(t)) for t in th) / len(th)) < 1e-12


def test_normals_unit_and_counts():
    rs = A.readings()
    for r in rs:
        assert abs(sum(c * c for c in A.normal(*r)) - 1) < 1e-12
    assert sum(c for _, c in A.counts([a for a, _ in rs], 70, 90)) == len(rs)
    assert sum(c for _, c in A.counts([d for _, d in rs], 4, 20)) == len(rs)

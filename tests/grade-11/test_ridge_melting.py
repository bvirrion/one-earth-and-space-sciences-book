"""figdata/grade-11/ridge_melting.py: decompression melting beneath a ridge."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-11"))
import ridge_melting as rm  # noqa: E402


def test_adiabat_crosses_the_solidus_at_the_onset():
    z = rm.onset_depth()
    assert abs(rm.adiabat(z) - rm.solidus_at(z)) < 0.5


def test_solid_below_and_above_solidus_above_the_onset():
    z = rm.onset_depth()
    assert rm.adiabat(z + 20) < rm.solidus_at(z + 20)       # deeper: solid
    assert rm.adiabat(z - 20) > rm.solidus_at(z - 20)       # shallower: above the solidus


def test_onset_a_few_tens_of_kilometres_down():
    assert 40 < rm.onset_depth() < 70


def test_hotter_mantle_starts_melting_deeper():
    assert rm.onset_depth(rm.TP_HOT) > rm.onset_depth() + 20


def test_solidus_falls_much_faster_than_the_adiabat_on_the_way_up():
    assert rm.solidus_slope(50.0) > 5 * rm.G_AD

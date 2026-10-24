"""figdata/grade-10/soil_rates.py: soil production against erosion; hydrolysis mass balance."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import soil_rates as sr  # noqa: E402


def test_ploughing_outpaces_production():
    n = sr.numbers()
    assert 10 < n["ratio_conv_to_production"] < 1000            # one to two orders of magnitude
    assert 300 < n["lifetime_1m_conv_yr"] < 1000                # "a few centuries" for a metre
    assert n["form_1m_yr"] > 50 * n["lifetime_1m_conv_yr"]


def test_hydrolysis_mass_balance():
    # 2 KAlSi3O8: K2 Al2 Si6 O16 ; + 2 H+ + 9 H2O -> Al2Si2O5(OH)4 + 2 K+ + 4 H4SiO4
    left = dict(K=2, Al=2, Si=6, O=16 + 9, H=2 + 18)
    right = dict(K=2, Al=2, Si=2 + 4, O=9 + 16, H=4 + 16)
    assert left == right
    assert abs(sr.hydrolysis_kaolinite_per_kg() - 463.8) < 0.5

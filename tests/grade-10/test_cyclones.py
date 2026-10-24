"""figdata/grade-10/cyclones.py: where tropical cyclones form, and the pressure--wind relation."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import cyclones as cy  # noqa: E402


def test_genesis_avoids_the_equator_and_the_south_atlantic():
    n = cy.numbers()
    assert n["genesis_within_5deg"] / n["storms_1980_2024"] < 0.01      # almost none within 5 degrees
    assert n["south_atlantic_genesis"] <= 5                             # a handful in 45 years
    assert 70 < n["per_year_1991_2020"] < 100


def test_lower_pressure_stronger_wind():
    n = cy.numbers()
    assert n["fit_slope"] < -1.0                                        # hPa per m/s
    assert n["lowest_pressure"] < 900 and n["max_wind_kt"] >= 150


def test_conversions():
    assert abs(cy.speed_of_sound(20) - 343) < 1
    assert abs(cy.surge_per_hpa() * 100 - 1.0) < 0.02                   # about 1 cm per hPa
    n = cy.numbers()
    assert abs(n["latent_W"] - 6.0e14) < 0.1e14                         # reproduces the AOML estimate
    assert 380 < n["efficiency_ratio"] < 420

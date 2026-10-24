"""figdata/grade-10/energy_budget.py: insolation geometry and the AR6 budget closure."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import energy_budget as eb  # noqa: E402


def test_insolation_geometry():
    assert abs(eb.daily_insolation(0, 0) - eb.S0 / math.pi) < 1e-9             # equator at an equinox: S0/pi
    dj = eb.declination(eb.EQUINOX_DAY + eb.YEAR_DAYS / 4)
    assert abs(dj - eb.EPS) < 1e-6                                              # June solstice declination
    pole = eb.daily_insolation(90, dj)
    assert abs(pole - eb.S0 * math.sin(math.radians(eb.EPS))) < 1e-6            # Sun circling at height eps
    assert pole > eb.daily_insolation(0, dj)                                    # the polar maximum beats the equator
    assert eb.daily_insolation(80, -dj) == 0.0                                  # polar night
    assert abs(eb.global_mean() - eb.S0 / 4) < 1.0                              # the sphere average is S0/4


def test_budget_closes():
    c = eb.closure()
    assert abs(c["toa"] - 0.7) < 0.5                    # the TOA imbalance, within the rounding of the figure
    assert abs(c["surface"] - 0.7) < 1.0
    assert abs(c["atmosphere"]) < 1.0
    assert abs(c["solar"]) < 1.0 and abs(c["surface_solar"]) < 1.0


def test_photosynthesis_share():
    n = eb.numbers()
    assert 0.05 < n["photosynthesis_share_pct"] < 0.2
    assert 0.9 < n["evap_m_yr"] < 1.2

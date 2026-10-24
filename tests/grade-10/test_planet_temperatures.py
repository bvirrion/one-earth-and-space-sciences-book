"""figdata/grade-10/planet_temperatures.py: the fact sheets and IAPWS check values."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import planet_temperatures as pt  # noqa: E402


def test_equilibrium_matches_fact_sheets():
    n = pt.numbers()
    for name, sheet in (("Mercury", 439.6), ("Venus", 226.6), ("Earth", 254.0), ("Moon", 270.4), ("Mars", 209.8)):
        assert abs(n[name + "_Teq"] - sheet) < 1.2, name          # NASA black-body temperatures (Earth 255.1 vs 254.0)
    assert n["Venus_greenhouse"] > 400 and 25 < n["Earth_greenhouse"] < 40 and abs(n["Mars_greenhouse"]) < 10


def test_iapws_check_values():
    assert abs(pt.p_melt(260.0) / 1e6 - 138.268) < 0.01              # R14-08 Table 3
    assert abs(pt.p_sub(230.0) / 1e6 - 8.94735e-6) < 1e-10
    assert abs(pt.p_vap(pt.TT) - pt.PT) < 1.0                          # curves meet at the triple point
    assert abs(pt.p_sub(pt.TT) - pt.PT) < 1e-6 and abs(pt.p_melt(pt.TT) - pt.PT) < 1e-6
    assert abs(pt.numbers()["boil_1atm_C"] - 99.97) < 0.05


def test_proxima_and_mars():
    n = pt.numbers()
    assert abs(n["proxima_flux"] - 0.641) < 0.01                       # archive: 0.641
    assert n["proxima_hz_in"] < pt.PROXIMA_A < n["proxima_hz_out"]
    assert 0.0 < n["boil_mars_C"] < 1.0                                # liquid only within ~0.5 degC on Mars

import math
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-12"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "shared"))
import relief_decay as rd  # noqa: E402


def test_rebound_lowers_the_surface_by_a_sixth_of_the_erosion():
    assert rd.rebound_fraction() == pytest.approx(550.0 / 3380.0)
    assert rd.lowering_m(1000.0) == pytest.approx(162.7, abs=0.1)
    # Airy: the column that loses e of crust rises until the mass above the
    # compensation depth is restored, so lowering + rise = e
    e = 1000.0
    rise = e * rd.RHO_C / rd.RHO_M
    assert rd.lowering_m(e) + rise == pytest.approx(e)


def test_calibration_and_e_folding_time():
    # Ahnert's statement: a tenth of the relief left after 11 Myr without uplift
    assert rd.elevation(11.0) / rd.H0 == pytest.approx(0.1)
    for reb in (False, True):
        tau = rd.time_constant(reb)
        assert rd.elevation(tau, rebound=reb) / rd.H0 == pytest.approx(math.exp(-1))
        assert rd.elevation(rd.half_life(reb), rebound=reb) == pytest.approx(rd.H0 / 2)
    assert rd.half_life(True) / rd.half_life(False) == pytest.approx(1 / rd.rebound_fraction())


def test_erosion_budgets_are_of_the_measured_order():
    n = rd.numbers()
    # the Mississippi before 1900 and the world both near the median 10Be basin rate, 54 m/Myr
    assert 30 < n["miss_before_1900_m_per_myr"] < 80
    assert 30 < n["world_m_per_myr"] < 80
    assert n["miss_1987_2006_m_per_myr"] < n["miss_before_1900_m_per_myr"]
    assert 1.4e8 < n["land_area_km2"] < 1.55e8


def test_unconformity_lies_below_the_ground():
    import region as rg
    (ax, ay), (bx, by) = rg.SECTION_AB
    L = math.hypot(bx - ax, by - ay)
    rows = [r for r in rd.unconformity() if not math.isnan(r[0])]
    assert len(rows) > 500
    for s, z in rows[::25]:
        x, y = ax + (bx - ax) * s * 1000 / L, ay + (by - ay) * s * 1000 / L
        assert z <= rg.topo(x, y) + 1e-6
        assert -700 < z < 650


def test_unconformity_is_the_sandstone_base_on_the_unit_grid():
    """Every plotted point has sandstone just above and basement just below, on the
    region's own unit function: none falls in the gap the normal fault opens."""
    import region as rg
    (ax, ay), (bx, by) = rg.SECTION_AB
    L = math.hypot(bx - ax, by - ay)
    rows = [r for r in rd.unconformity() if not math.isnan(r[0])]
    sand = rg.UNIT["sandstone"]
    basement = {rg.UNIT["schist"], rg.UNIT["granite"]}
    for s, z in rows:
        x, y = ax + (bx - ax) * s * 1000 / L, ay + (by - ay) * s * 1000 / L
        if z > rg.topo(x, y) - 2.0:
            continue
        assert rg.unit(x, y, z + 1.0, with_alluvium=False) == sand, (s, z)
        assert rg.unit(x, y, z - 1.0, with_alluvium=False) in basement, (s, z)

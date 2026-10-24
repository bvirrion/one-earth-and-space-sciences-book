"""figdata/grade-10/varden_basin.py: the basin of the Varden river by D8 routing."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-10"))
import varden_basin as vb  # noqa: E402


@pytest.fixture(scope="module")
def model():
    return vb.compute()


def test_every_basin_cell_drains_to_the_outlet(model):
    xs, ys, z, filled, rec, mask = model
    outlet = vb.outlet_cells(xs, ys)
    assert outlet
    for j in range(len(ys)):
        for i in range(len(xs)):
            end = vb.path(rec, (j, i))[-1]
            if mask[j, i]:
                assert end in outlet, (xs[i], ys[j], end)
            else:
                # outside the basin the water leaves the map without touching the floor
                assert not any(vb.on_floor(xs, ys, jj, ii) for jj, ii in vb.path(rec, (j, i)))


def test_flow_always_goes_down_and_fill_is_minimal(model):
    xs, ys, z, filled, rec, mask = model
    assert (filled >= z).all()
    for (j, i), r in rec.items():
        if r is not None:
            assert filled[r] < filled[j, i]
    # the hills are almost free of closed hollows: only a few metres of fill anywhere
    assert (filled - z).max() < 5.0


def test_river_floor_is_in_the_basin_and_the_basin_is_most_of_the_map(model):
    xs, ys, z, filled, rec, mask = model
    for j in range(len(ys)):
        for i in range(len(xs)):
            if vb.on_floor(xs, ys, j, i):
                assert mask[j, i]
    n = vb.numbers(xs, ys, z, filled, mask)
    assert abs(n["map_km2"] - 80.0) < 1e-9
    assert 0.6 < n["basin_share"] < 0.95

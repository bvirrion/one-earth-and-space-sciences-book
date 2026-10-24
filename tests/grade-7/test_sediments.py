"""Tests for figdata/grade-7/varden_column.py (chapter g7.4)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-7"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "shared"))
import region as R  # noqa: E402
import varden_column as V  # noqa: E402


def test_thicknesses_come_from_the_region():
    lay = V.layers(chalk=100.0)
    assert [n for n, *_ in lay] == ["sandstone", "limestone", "shale", "chalk"]
    assert [t for *_, t in lay[:3]] == [R.THICK["sandstone"], R.THICK["limestone"], R.THICK["shale"]]
    assert [(b, t) for _, b, t, _ in lay[:3]] == [(0, 120), (120, 300), (300, 400)]


def test_layers_touch_without_gaps():
    lay = V.layers(chalk=80.0)
    for (_, _, top, _), (_, base, _, _) in zip(lay, lay[1:]):
        assert top == base


def test_chalk_is_drawn_not_measured():
    lay = V.layers()
    assert lay[-1][0] == "chalk" and lay[-1][3] == V.CHALK_DRAWN
    # the region model has chalk at the surface somewhere (so the column is honest)
    assert any(R.unit(x, y, R.topo(x, y)) == R.UNIT["chalk"]
               for x in range(0, 10001, 500) for y in range(0, 8001, 500))


def test_problem_numbers():
    assert round(V.share("limestone")) == 45
    assert V.years("sandstone") == 240_000
    assert V.years("limestone") == 1_800_000
    assert V.years("limestone") / V.years("sandstone") == 7.5


def test_polygons_are_closed():
    for name, ring in V.polygons(chalk=90.0).items():
        assert ring[0] == ring[-1], name

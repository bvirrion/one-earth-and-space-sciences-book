"""figdata/grade-6/earth_layers.py: PREM boundaries, gradients, the model Earth."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-6"))
import earth_layers as el  # noqa: E402


def test_prem_boundaries():
    names = [b[0] for b in el.boundaries()]
    assert names == ["crust", "mantle", "outer-core", "inner-core"]
    oc, ic = el.core_depths()
    assert (oc, ic) == (2891.0, 5149.5)
    assert el.boundaries()[-1][2] == el.R_EARTH_KM


def test_only_the_outer_core_is_liquid():
    assert el.liquid_layers() == ["outer-core"]
    assert [s for *_, s in el.layers()] == ["solid", "solid", "liquid", "solid"]


def test_numbers_in_the_text():
    oc, ic = el.core_depths()
    assert round(el.pct_of_radius(oc)) == 45
    assert round(el.pct_of_radius(ic)) == 81
    assert round(el.R_EARTH_KM / el.KOLA_KM) == 520          # "more than 500 times deeper"
    assert round(el.pct_of_radius(el.KOLA_KM), 1) == 0.2
    assert round(el.R_EARTH_KM - ic) == 1222                    # inner-core radius, ~1220 km
    assert ic - oc == 2258.5                                    # outer core, ~2260 km thick


def test_gradients():
    assert el.temperature(2.0, el.GRADIENTS["mean"]) == 73.0
    assert el.temperature(1.0, el.GRADIENTS["east"]) == 40.0
    assert el.temperature(2.0, el.GRADIENTS["high"]) == 153.0


def test_model_earth_problem():
    mm = dict(el.model_items())
    assert round(el.to_model_mm(mm["oceanic crust"]), 2) == 0.78   # the named final number
    assert round(el.to_model_mm(mm["continental crust"]), 1) == 4.7
    assert round(el.to_model_mm(mm["Kola borehole"]), 1) == 1.9
    assert round(el.to_model_mm(mm["top of outer core"])) == 454
    assert round(el.to_model_mm(mm["inner core radius"])) == 192
    assert el.to_model_mm(el.R_EARTH_KM) == 1000.0

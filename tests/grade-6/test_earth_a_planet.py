"""figdata/grade-6/planets.py: the eight planets from the shared NASA rows."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-6"))
import planets as pl  # noqa: E402


def test_values_are_reread_from_the_ledger():
    led = pl.ledger()
    assert led["planet:Venus.psurf"] == 92 and led["planet:Earth.psurf"] == 1
    assert led["planet:Earth.diameter"] == 12756 and led["planet:Mars.Tmean"] == -65
    assert all("planet:%s.density" % p in led for p in pl.PLANETS)


def test_two_families_by_density():
    kinds = [pl.kind(p) for p in pl.PLANETS]
    assert kinds == ["rocky"] * 4 + ["giant"] * 4
    assert pl.density_gcm3("Saturn") < 1.0          # less dense than water


def test_percentages_quoted_in_the_text():
    assert round(pl.percent_of_earth("Mars")) == 53
    assert round(pl.percent_of_earth("Venus")) == 95
    assert round(pl.value("Jupiter", "diameter") / pl.value("Earth", "diameter")) == 11


def test_venus_is_hotter_than_mercury_though_farther():
    v, m = pl.value("Venus", "Tmean"), pl.value("Mercury", "Tmean")
    assert v > m and pl.value("Venus", "dist") > pl.value("Mercury", "dist")
    t = [pl.value(p, "Tmean") for p in pl.PLANETS[2:]]
    assert t == sorted(t, reverse=True)             # from the Earth outwards, colder and colder


def test_circles_to_scale_fit_the_row():
    rows, scale = pl.circles()
    right = rows[-1][4] + rows[-1][3] / 2
    assert abs(right - pl.ROW_WIDTH_CM) < 0.01
    assert abs(rows[4][3] / rows[2][3] - 142984 / 12756) < 0.01


def test_sun_at_the_same_scale():
    assert 39 < pl.sun_cm() < 41             # "a disc about 40 cm across"


def test_trio_panel_values():
    assert [pl.value(p, "psurf") for p in ("Venus", "Earth", "Mars")] == [92, 1, 0.01]
    assert [pl.value(p, "Tmean") for p in ("Venus", "Earth", "Mars")] == [464, 15, -65]


def test_distance_line_and_scale_model():
    rows = {n: (d, x, xi) for n, d, x, xi in pl.distance_line()}
    assert rows["Neptune"][1] == pl.ROW_WIDTH_CM
    assert rows["Mars"][1] < 0.7 and rows["Mars"][2] < 7.0      # the rocky four crowd near the Sun
    model = {n: (d, m) for n, d, m in pl.scale_model()}
    assert round(model["Sun"][0]) == 109                        # the Sun about 109 Earths wide
    assert round(model["Earth"][1]) == 117                       # the Earth 117 m from the Sun
    assert round(model["Neptune"][1] / 100) * 100 == 3500         # Neptune about 3.5 km away
    assert round(model["Jupiter"][0]) == 11

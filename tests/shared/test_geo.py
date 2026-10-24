"""figdata/shared/geo.py: projections, PB2002 polarity, catalogue sizes."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "shared"))
import geo  # noqa: E402


def test_mollweide_landmarks():
    assert geo.mollweide(0, 0) == (0.0, 0.0)
    x, y = geo.mollweide(180, 0)
    assert abs(x - 2 * math.sqrt(2)) < 1e-9 and abs(y) < 1e-12
    x, y = geo.mollweide(0, 90)
    assert abs(x) < 1e-12 and abs(y - math.sqrt(2)) < 1e-12
    # equal area: the band 0-30 N holds half of the northern hemisphere's area,
    # because sin 30 = 1/2; in Mollweide the band's area is the matching
    # fraction of the half-ellipse, i.e. theta + sin(2 theta)/2 = pi/4
    _, y30 = geo.mollweide(0, 30)
    t = math.asin(y30 / math.sqrt(2))
    assert abs((2 * t + math.sin(2 * t)) / math.pi - 0.5) < 1e-9


def test_subduction_naming():
    assert geo.subducting_plate("NZ\\SA") == "NZ"
    assert geo.overriding_plate("NZ\\SA") == "SA"
    assert geo.subducting_plate("CA/SA") == "SA"
    assert geo.overriding_plate("CA/SA") == "CA"


def _net(name):
    dx = dy = 0.0
    for n, cls, pts in geo.boundary_lines(geo.SUBDUCTION):
        if n == name:
            dx += pts[-1][0] - pts[0][0]
            dy += pts[-1][1] - pts[0][1]
    return dx, dy


def test_overriding_plate_on_the_left():
    # Peru-Chile trench: South America (east) overrides -> the line runs south
    assert _net("NZ\\SA")[1] < -20
    # Lesser Antilles: Caribbean (west) overrides South America -> runs north
    assert _net("CA/SA")[1] > 0
    # Aleutians: North America (north) overrides the Pacific -> runs east
    assert _net("NA/PA")[0] > 0
    # Cascadia: North America (east) overrides Juan de Fuca -> runs south
    assert _net("JF\\NA")[1] < 0


def test_catalogues():
    q = geo.quakes()
    assert 6000 < len(q) < 9000
    assert all(m >= 6.0 for *_, m in q)
    assert len(geo.volcanoes()) > 1000
    assert len(geo.land_rings()) > 100


def test_teeth_on_the_left():
    # a straight line going north: teeth to the west (negative longitude)
    tris = geo.teeth([[(0.0, 0.0), (0.0, 30.0)]], spacing=7, base=2, height=2)
    assert len(tris) == 4
    for t in tris:
        assert t[2][0] < 0 and abs(t[0][0]) < 1e-12


def test_school_merge_drops_internal_boundaries():
    names = {n for n, _, _ in geo.boundary_lines(geo.RIDGE + geo.COLLISION + geo.TRANSFORM,
                                                 geo.SCHOOL_MERGE)}
    assert not any(set(geo._plates(n)) <= {"EU", "AM", "YA"} for n in names)
    assert any(n in ("EU-NA", "NA-EU") for n in names)

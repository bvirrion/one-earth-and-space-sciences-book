"""figdata/grade-4: the physical map raster, its legend and Africa's area."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "grade-4"))
import physical_map as pm  # noqa: E402


def test_colour_bands():
    assert pm.colour(-5000) == "5A9CCF" and pm.colour(-3000) == "84BCE0"
    assert pm.colour(-100) == "DCEEF8" and pm.colour(0) == "9CC98A"
    assert pm.colour(199) == "9CC98A" and pm.colour(200) == "C9DE99"
    assert pm.colour(3500) == "C79E76" and pm.colour(8000) == "ECE8E3"


def test_legend_is_a_staircase():
    rows = pm.band_rows()
    assert len(rows) == 10 and rows[3][2] == 0 and rows[4][1] == 0
    for a, b in zip(rows, rows[1:]):
        assert a[2] == b[1] or (a[2] == 0 and b[1] == 0)


def test_cell_area_sums_to_the_earth():
    total = sum(pm.cell_area_km2(-89.5 + j) for j in range(180)) * 360
    assert abs(total / 510.07e6 - 1) < 0.001


def test_africa_area_and_sahara_share():
    cells = pm.etopo()
    a = pm.africa_area_mkm2(cells)
    assert 28.5 < a < 31.0                     # about 30 million km2
    assert 0.26 < pm.SAHARA_MKM2 / a < 0.30    # "a little more than a quarter"


def test_outline_excludes_neighbours():
    for lon, lat in ((-5.5, 37.5), (14.5, 37.5), (35.5, 30.5), (45.5, 24.5), (24.5, 35.5)):
        assert not pm.inside(pm.AFRICA, lon, lat)     # Spain, Sicily, Sinai, Arabia, Crete
    for lon, lat in ((-5.5, 34.5), (31.5, 30.5), (18.5, -33.5), (46.5, -19.5)):
        assert pm.inside(pm.AFRICA, lon, lat) or pm.inside(pm.MADAGASCAR, lon, lat)

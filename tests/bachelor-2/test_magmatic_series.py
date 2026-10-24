"""Tests for the magmatic-series figure data (series.py)."""
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-2"))
import series as ms  # noqa: E402


def _area(poly):
    return 0.5 * sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]))


def test_tas_polygons_use_the_printed_vertices_and_tile_the_diagram():
    verts = {p for poly in ms.TAS.values() for p in poly}
    for v in ms.BGS_VERTICES:
        assert v in verts
    for poly in ms.TAS.values():
        assert abs(_area(poly)) > 1.0
    rng = random.Random(1)
    for _ in range(20000):
        pt = (rng.uniform(36, 79.9), rng.uniform(0.01, 15))
        hits = [k for k, p in ms.TAS.items() if ms.inside(pt, p)]
        assert len(hits) == 1, (pt, hits)


def test_tas_examples():
    # USGS BHVO-2 (Kilauea 1919): SiO2 49.60, Na2O 2.219, K2O 0.513 -> basalt
    assert ms.tas_field(49.60, 2.219 + 0.513) == "B"
    assert ms.tas_field(75.0, 7.0) == "R"
    assert ms.tas_field(60.0, 6.0) == "O2"
    assert ms.tas_field(53.0, 7.0) == "S2"
    assert ms.tas_field(55.0, 8.0) == "S3"
    assert ms.tas_field(43.0, 12.0) == "F"


def test_k2o_lines_pass_through_the_printed_points():
    for (x, y), lo in (((48, 0.3), True), ((68, 1.2), True), ((48, 1.2), False),
                       ((68, 3.1), False)):
        assert ms.k_class(x, y - 1e-6) == ("low" if lo else "medium")
        assert ms.k_class(x, y + 1e-6) == ("medium" if lo else "high")


def test_afm_geometry_and_irvine_baragar_line():
    assert ms.tern_xy(0, 1, 0) == (0.0, 0.0)
    assert ms.tern_xy(0, 0, 1) == (1.0, 0.0)
    x, y = ms.tern_xy(1, 0, 0)
    assert abs(x - 0.5) < 1e-12 and abs(y - ms.S3) < 1e-12
    for f, a, m in ms.IB71:
        assert abs(f + a + m - 100) < 0.11
    xs = [p[0] for p in ms.IB_XY]
    assert all(b > a for a, b in zip(xs, xs[1:]))
    assert ms.ib_side(70, 10, 20) == "th"      # iron-rich: above the line
    assert ms.ib_side(20, 30, 50) == "ca"


def test_iceland_tholeiitic_cascades_calc_alkaline():
    rows = ms.cath_rows()
    th = [r for r in rows if r["series"] == "th"]
    ca = [r for r in rows if r["series"] == "ca"]
    assert len(th) == 456 and len(ca) == 580
    s_th = [ms.ib_side(r["FeOT"], r["Na2O"] + r["K2O"], r["MgO"]) for r in th]
    s_ca = [ms.ib_side(r["FeOT"], r["Na2O"] + r["K2O"], r["MgO"]) for r in ca]
    assert s_th.count("th") / (s_th.count("th") + s_th.count("ca")) > 0.9
    assert s_ca.count("ca") / (s_ca.count("th") + s_ca.count("ca")) > 0.85


def test_settings_trace_elements_and_tizry():
    st = ms.settings_rows()
    assert len(st) == 756
    med = {s: ms.medians(st, s) for s in ("MORB", "OIB", "IAB")}
    nbla = {s: med[s]["Nb"][0] / med[s]["La"][0] for s in med}
    # the arc basalts have the Nb trough; ocean-island basalts are Nb-rich
    assert nbla["IAB"] < 0.6 < nbla["MORB"] < 1.1 < nbla["OIB"]
    # Ti-Zr-Y fields do not overlap
    rng = random.Random(2)
    for _ in range(5000):
        a, b = sorted((rng.random(), rng.random()))
        t, z, y = a, b - a, 1 - b
        pt = ms.tern_xy(t, z, y)
        hits = [k for k, p in ms.TIZRY.items() if ms.inside(pt, [ms.tern_xy(*q) for q in p])]
        assert len(hits) <= 1
    c = ms.tizry_counts(st)
    oib = c["OIB"]
    assert oib["D"] > 0.8 * sum(oib.values())


def test_logratio_regressions_reproduce_vermeesch_and_pease():
    fits = {s: ms.orthogonal_fit(ms.logratios(s)) for s in ("th", "ca")}
    (s1, b1), (s2, b2) = fits["th"], fits["ca"]
    x0 = (b2 - b1) / (s1 - s2)
    y0 = s1 * x0 + b1
    # the published intersection (x0 = -3.84, y0 = 2.12)
    assert abs(x0 + 3.84) < 0.01 and abs(y0 - 2.12) < 0.01
    # the tholeiitic (Fenner) trend is the steeper one
    assert s1 < s2 < 0
    # principal axis: orthogonal residuals are minimal compared with nearby slopes
    pts = ms.logratios("ca")

    def ssq(m):
        xm = sum(p[0] for p in pts) / len(pts)
        ym = sum(p[1] for p in pts) / len(pts)
        return sum((p[1] - ym - m * (p[0] - xm)) ** 2 / (1 + m * m) for p in pts)
    assert ssq(s2) <= min(ssq(s2 + 0.01), ssq(s2 - 0.01))

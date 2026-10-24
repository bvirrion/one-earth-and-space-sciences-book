"""Magmatic series and tectonic settings (Year 2, magmatic-series): the total alkali--silica
classification, the AFM and K2O--SiO2 diagrams of the tholeiitic and calc-alkaline series,
trace-element patterns of basalts by tectonic setting and the Ti--Zr--Y discrimination
diagram.

  TAS        Field vertices of Le Bas et al. (1986) as printed in BGS Research Report RR 99-06,
             Figure 20b ("coordinates of the line intersections", ledger bgs:tas); the upper
             ends of the phonolite/trachyte/rhyolite boundaries (to the frame of the diagram)
             from GeoplotR inst/TAS.json (ledger geoplotr:tas), which repeats the BGS vertices.
             Polygons in (SiO2, Na2O + K2O) wt %.
  K2O        Low-K / medium-K / high-K lines of BGS RR 99-06 Figure 23 (after Le Maitre et al.
             1989, modified after Peccerillo and Taylor 1976): (48, 0.3)-(68, 1.2) and
             (48, 1.2)-(68, 3.1) (ledger bgs:k2o-sio2); drawn from SiO2 = 48 and extended to 77.
  AFM        A = Na2O + K2O, F = FeO_T, M = MgO, recast to 100.  Dividing line of Irvine and
             Baragar (1971) as tabulated in GeoplotR inst/AFM.json after Le Maitre et al.
             (2002) (ledger geoplotr:afm), 15 points (F, A, M).  Ternary to Cartesian with A at
             (0, 0), M at (1, 0), F at (1/2, sqrt(3)/2): x = M + F/2, y = F sqrt(3)/2 (fractions).
  cath       data/derived/bachelor-2-cath.csv (ledger data:b4-cath): 456 Icelandic
             (tholeiitic) and 580 Cascades (calc-alkaline) rocks, oxides as given.
  settings   data/derived/bachelor-2-basalt-settings.csv (ledger data:b4-basalt-settings): 756
             basalts from mid-ocean ridges (MORB), ocean islands (OIB) and island arcs (IAB).
             Spider diagram: median of each element by setting (samples where it was analysed),
             divided by the primitive mantle of geochem.py (McDonough and Sun 1995, ledger
             ms95:pm-trace); Ti from TiO2.
  TiZrY      Pearce and Cann (1973) fields as tabulated in GeoplotR inst/TiZrY.json (ledger
             geoplotr:tizry): plot coordinates Ti/100, Zr, 3Y recast to 100; A island-arc
             tholeiites, B MORB + island-arc tholeiites + calc-alkali basalts, C calc-alkali
             basalts, D within-plate basalts.  Cartesian as AFM with Ti at the top, Zr at the
             left, 3Y at the right (x = 3Y + Ti/2).

  logratio   ln(A/F) against ln(M/F) for the two series and their orthogonal (principal-axis)
             regression lines, after Vermeesch and Pease (2021), who find the two lines
             meeting at (-3.84, 2.12) (ledger vp21:model).

  parts: tas-<field> (closed polygons), k2o-lines, afm-line, cath-th, cath-ca, lr-th, lr-ca, lr-fits,
         spider, tizry-<field>, tizry-<setting>, values
"""
import csv
import math
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from _table import write_table  # noqa: E402
import geochem  # noqa: E402

ROOT = os.path.join(HERE, "..", "..")
S3 = math.sqrt(3.0) / 2.0

# --- TAS ---------------------------------------------------------------------------------
# vertices (SiO2, Na2O + K2O); points at y = 0 and on the frame close the polygons
TAS = {
    "Pc": [(41, 0), (41, 3), (45, 3), (45, 0)],
    "B": [(45, 0), (45, 5), (52, 5), (52, 0)],
    "O1": [(52, 0), (52, 5), (57, 5.9), (57, 0)],
    "O2": [(57, 0), (57, 5.9), (63, 7), (63, 0)],
    "O3": [(63, 0), (63, 7), (69, 8), (77, 0)],
    "R": [(77, 0), (69, 8), (69, 17.7), (77, 22), (80, 23.5), (80, 0)],
    "S1": [(45, 5), (49.4, 7.3), (52, 5)],
    "S2": [(52, 5), (49.4, 7.3), (53, 9.3), (57, 5.9)],
    "S3": [(57, 5.9), (53, 9.3), (57.6, 11.7), (63, 7)],
    "T": [(63, 7), (57.6, 11.7), (61, 13.5), (63, 16.2), (69, 17.7), (69, 8)],
    "U1": [(41, 3), (41, 7), (45, 9.4), (49.4, 7.3), (45, 5), (45, 3)],
    "U2": [(49.4, 7.3), (45, 9.4), (48.4, 11.5), (53, 9.3)],
    "U3": [(53, 9.3), (48.4, 11.5), (52.5, 14), (57.6, 11.7)],
    "Ph": [(52.5, 14), (42, 18.7), (69, 17.7), (63, 16.2), (61, 13.5), (57.6, 11.7)],
    "F": [(41, 0), (35, 0), (35, 18.7 + 0.448 * 7), (42, 18.7), (52.5, 14), (48.4, 11.5),
          (45, 9.4), (41, 7), (41, 3)],
}
# the vertices printed in BGS RR 99-06 Figure 20b
BGS_VERTICES = [(41, 3), (45, 3), (45, 5), (52, 5), (57, 5.9), (63, 7), (69, 8), (41, 7),
                (45, 9.4), (48.4, 11.5), (52.5, 14), (49.4, 7.3), (53, 9.3), (57.6, 11.7),
                (61, 13.5)]
TAS_NAMES = {"Pc": "picrobasalt", "B": "basalt", "O1": "basaltic andesite", "O2": "andesite",
             "O3": "dacite", "R": "rhyolite", "S1": "trachybasalt",
             "S2": "basaltic trachyandesite", "S3": "trachyandesite",
             "T": "trachyte or trachydacite", "U1": "tephrite or basanite",
             "U2": "phonotephrite", "U3": "tephriphonolite", "Ph": "phonolite",
             "F": "foidite"}

# K2O-SiO2 (BGS Figure 23)
K_LOW = ((48.0, 0.3), (68.0, 1.2))
K_HIGH = ((48.0, 1.2), (68.0, 3.1))

# AFM: Irvine and Baragar (1971) line, (F, A, M) per cent
IB71 = [(35.0, 60.0, 5.0), (37.9, 55.0, 7.1), (40.8, 50.0, 9.2), (43.8, 45.0, 11.2),
        (46.7, 40.0, 13.3), (49.6, 35.0, 15.4), (52.5, 30.0, 17.5), (54.1, 26.4, 19.5),
        (54.5, 23.0, 22.5), (53.5, 20.5, 26.0), (51.0, 19.1, 29.9), (46.9, 18.1, 35.0),
        (42.8, 17.1, 40.1), (38.6, 16.2, 45.2), (34.5, 15.2, 50.3)]

# Ti-Zr-Y fields (Ti/100, Zr, 3Y)
TIZRY = {
    "D": [(24, 55.5, 20.5), (28, 59, 13), (50, 38.5, 11.5), (48, 24, 28), (42.5, 37.5, 30),
          (29.5, 45, 25.5)],
    "C": [(29.5, 45, 25.5), (24, 55.5, 20.5), (16, 63, 21), (10, 62.5, 27.5), (10, 55, 35),
          (19, 40, 41)],
    "B": [(42.5, 37.5, 30), (29.5, 45, 25.5), (19, 40, 41), (30, 26, 44)],
    "A": [(48, 24, 28), (39, 20.5, 40.5), (30, 26, 44), (42.5, 37.5, 30)],
}

SPIDER = ["Rb", "Ba", "Th", "U", "Nb", "Ta", "La", "Ce", "Pb", "Sr", "Nd", "Zr", "Hf", "Sm",
          "Eu", "Ti", "Gd", "Dy", "Y", "Er", "Yb", "Lu"]


def inside(pt, poly):
    """Ray-casting point-in-polygon test (boundary points may go either way)."""
    x, y = pt
    n, ins = len(poly), False
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xc = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xc > x:
                ins = not ins
    return ins


def tas_field(sio2, alk):
    hits = [k for k, p in TAS.items() if inside((sio2, alk), p)]
    return hits[0] if len(hits) == 1 else None


def k_class(sio2, k2o):
    """'low', 'medium' or 'high' K on the BGS lines (extended linearly)."""
    def line(p, x):
        (x1, y1), (x2, y2) = p
        return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    if k2o < line(K_LOW, sio2):
        return "low"
    if k2o < line(K_HIGH, sio2):
        return "medium"
    return "high"


def tern_xy(top, left, right):
    """Cartesian position of a ternary point (any scale): left corner (0,0), right (1,0),
    top (1/2, sqrt(3)/2)."""
    s = top + left + right
    t, r = top / s, right / s
    return r + t / 2.0, t * S3


def afm(feot, alk, mgo):
    """(x, y) of a rock on the AFM triangle, F at the top, A left, M right."""
    return tern_xy(feot, alk, mgo)


def afm_percent(feot, alk, mgo):
    s = feot + alk + mgo
    return 100 * alk / s, 100 * feot / s, 100 * mgo / s


IB_XY = [afm(f, a, m) for f, a, m in IB71]


def ib_side(feot, alk, mgo):
    """'th' if the point lies on the F side of the Irvine-Baragar line, 'ca' if below it,
    None if outside the x range of the line."""
    x, y = afm(feot, alk, mgo)
    for (x1, y1), (x2, y2) in zip(IB_XY, IB_XY[1:]):
        if x1 <= x <= x2:
            yl = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            return "th" if y > yl else "ca"
    return None


def cath_rows():
    with open(os.path.join(ROOT, "data", "derived", "bachelor-2-cath.csv")) as f:
        return [dict(series=r["series"], **{k: float(v) for k, v in r.items() if k != "series"})
                for r in csv.DictReader(f)]


def logratios(series):
    """(ln(A/F), ln(M/F)) of every rock of one series of the cath data."""
    out = []
    for r in cath_rows():
        a, f, m = r["Na2O"] + r["K2O"], r["FeOT"], r["MgO"]
        if r["series"] == series and a > 0 and f > 0 and m > 0:
            out.append((math.log(a / f), math.log(m / f)))
    return out


def orthogonal_fit(pts):
    """Total-least-squares line y = slope x + icept through the points (principal axis)."""
    n = len(pts)
    xm = sum(p[0] for p in pts) / n
    ym = sum(p[1] for p in pts) / n
    sxx = sum((p[0] - xm) ** 2 for p in pts)
    syy = sum((p[1] - ym) ** 2 for p in pts)
    sxy = sum((p[0] - xm) * (p[1] - ym) for p in pts)
    theta = 0.5 * math.atan2(2 * sxy, sxx - syy)
    slope = math.tan(theta)
    return slope, ym - slope * xm


def settings_rows():
    with open(os.path.join(ROOT, "data", "derived", "bachelor-2-basalt-settings.csv")) as f:
        out = []
        for r in csv.DictReader(f):
            d = {"setting": r["setting"]}
            for k, v in r.items():
                if k != "setting":
                    d[k] = float(v) if v != "" else None
            d["Ti"] = d["TiO2"] * 1e4 * geochem.TI_IN_TIO2 if d["TiO2"] is not None else None
            out.append(d)
        return out


def medians(rows, setting):
    out = {}
    for el in SPIDER:
        v = [r[el] for r in rows if r["setting"] == setting and r[el] is not None and r[el] > 0]
        out[el] = (statistics.median(v), len(v))
    return out


def tizry_xyz(ti, zr, y):
    return ti / 100.0, zr, 3.0 * y


def tizry_field(ti, zr, y):
    t, z, yy = tizry_xyz(ti, zr, y)
    pt = tern_xy(t, z, yy)
    for k, poly in TIZRY.items():
        if inside(pt, [tern_xy(*p) for p in poly]):
            return k
    return None


def tizry_counts(rows):
    out = {}
    for s in ("MORB", "OIB", "IAB"):
        c = {"A": 0, "B": 0, "C": 0, "D": 0, None: 0}
        for r in rows:
            if r["setting"] == s and r["Ti"] and r["Zr"] and r["Y"]:
                c[tizry_field(r["Ti"], r["Zr"], r["Y"])] += 1
        out[s] = c
    return out


if __name__ == "__main__":
    for k, poly in TAS.items():
        write_table(__file__, ("SiO2", "alk"), poly + [poly[0]], part="tas-" + k)
    write_table(__file__, ("x", "y_low", "y_high"),
                [(x, 0.3 + 0.045 * (x - 48), 1.2 + 0.095 * (x - 48)) for x in (48, 77)],
                part="k2o-lines")
    write_table(__file__, ("x", "y"), IB_XY, part="afm-line")
    cath = cath_rows()
    for s in ("th", "ca"):
        rows = []
        for r in cath:
            if r["series"] != s:
                continue
            x, y = afm(r["FeOT"], r["Na2O"] + r["K2O"], r["MgO"])
            rows.append((r["SiO2"], r["Na2O"] + r["K2O"], r["K2O"], x, y))
        write_table(__file__, ("SiO2", "alk", "K2O", "afm_x", "afm_y"), rows, part="cath-" + s)
    fits = {}
    for s in ("th", "ca"):
        pts = logratios(s)
        fits[s] = orthogonal_fit(pts)
        write_table(__file__, ("lnAF", "lnMF"), pts, part="lr-" + s)
    write_table(__file__, ("x", "y_th", "y_ca"),
                [(x, fits["th"][0] * x + fits["th"][1], fits["ca"][0] * x + fits["ca"][1])
                 for x in (-4.0, 2.2)], part="lr-fits")
    st = settings_rows()
    med = {s: medians(st, s) for s in ("MORB", "OIB", "IAB")}
    write_table(__file__, ("idx", "el", "morb", "oib", "iab"),
                [(i + 1, el, med["MORB"][el][0] / geochem.PM[el],
                  med["OIB"][el][0] / geochem.PM[el], med["IAB"][el][0] / geochem.PM[el])
                 for i, el in enumerate(SPIDER)], part="spider")
    for k, poly in TIZRY.items():
        pts = [tern_xy(*p) for p in poly]
        write_table(__file__, ("x", "y"), pts + [pts[0]], part="tizry-" + k)
    for s in ("MORB", "OIB", "IAB"):
        pts = [tern_xy(*tizry_xyz(r["Ti"], r["Zr"], r["Y"])) for r in st
               if r["setting"] == s and r["Ti"] and r["Zr"] and r["Y"]]
        write_table(__file__, ("x", "y"), pts, part="tizry-" + s.lower())
    # values quoted in the text
    vals = []
    for s in ("th", "ca"):
        sub = [r for r in cath if r["series"] == s]
        sides = [ib_side(r["FeOT"], r["Na2O"] + r["K2O"], r["MgO"]) for r in sub]
        vals += [("cath_n_" + s, len(sub)),
                 ("cath_" + s + "_th_side", sides.count("th")),
                 ("cath_" + s + "_ca_side", sides.count("ca")),
                 ("cath_" + s + "_outside", sides.count(None))]
        fields = [tas_field(r["SiO2"], r["Na2O"] + r["K2O"]) for r in sub]
        for k in TAS:
            vals.append(("cath_%s_tas_%s" % (s, k), fields.count(k)))
        vals.append(("cath_%s_tas_none" % s, fields.count(None)))
        ks = [k_class(r["SiO2"], r["K2O"]) for r in sub if r["SiO2"] >= 48]
        for k in ("low", "medium", "high"):
            vals.append(("cath_%s_k_%s" % (s, k), ks.count(k)))
        vals.append(("cath_%s_sio2_min" % s, min(r["SiO2"] for r in sub)))
        vals.append(("cath_%s_sio2_max" % s, max(r["SiO2"] for r in sub)))
    for s in ("MORB", "OIB", "IAB"):
        vals.append(("n_" + s, sum(1 for r in st if r["setting"] == s)))
        for el in ("Nb", "La", "Th", "Ba", "Zr", "Y", "Ti", "Yb"):
            vals.append(("med_%s_%s" % (s, el), round(med[s][el][0], 4)))
            vals.append(("nmed_%s_%s" % (s, el), med[s][el][1]))
        vals.append(("nb_la_" + s, round(med[s]["Nb"][0] / med[s]["La"][0], 3)))
    for s in ("th", "ca"):
        vals += [("lr_slope_" + s, round(fits[s][0], 4)), ("lr_icept_" + s, round(fits[s][1], 4))]
    x0 = (fits["ca"][1] - fits["th"][1]) / (fits["th"][0] - fits["ca"][0])
    vals += [("lr_x0", round(x0, 3)), ("lr_y0", round(fits["th"][0] * x0 + fits["th"][1], 3))]
    for s, c in tizry_counts(st).items():
        for k in ("A", "B", "C", "D", None):
            vals.append(("tizry_%s_%s" % (s, k), c[k]))
    write_table(__file__, ("what", "value"), vals, part="values")

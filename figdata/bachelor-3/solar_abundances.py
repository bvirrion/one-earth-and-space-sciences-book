"""The solar abundance curve, and the Sun against the CI chondrites (Year 3, origin of the
elements).

Data: Asplund, Amarsi and Grevesse (2021, A&A 653, A141), Table 2 (data/derived/
bachelor-3-asplund21-elements.csv, ledger data:b5-asplund21): present-day photospheric
abundances log eps(X) = 12 + log10(N_X / N_H) and CI chondrite abundances on the same
scale (renormalised by the authors to the solar silicon abundance). Where no photospheric
value exists, the curve takes the CI value, as the paper's Fig. 1 does (the paper also
corrects those for a small condensation-temperature trend, about 0.04 dex, not applied
here).

  part curve     Z logeps src            src 1 photosphere, 0 meteorites
  part even      Z logeps                even atomic numbers
  part odd       Z logeps                odd atomic numbers
  part compare   Z phot ci diff group    elements with both values; group: 0 normal,
                                         1 depleted in the meteorites (H, He, C, N, O,
                                         noble gases), 2 depleted in the Sun (Li)
  part values    what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DATA = os.path.join(ROOT, "data", "derived", "bachelor-3-asplund21-elements.csv")
# depleted in CI chondrites: the elements the paper sets apart as highly volatile
METEORITE_DEPLETED = {"H", "He", "C", "N", "O", "Ne", "Ar", "Kr", "Xe"}
SUN_DEPLETED = {"Li"}


def load(path=DATA):
    """{Z: (el, phot or None, phot_err, ci or None, ci_err)}"""
    out = {}
    with open(path, encoding="utf8") as f:
        for r in csv.DictReader(f):
            p = float(r["phot"]) if r["phot"] else None
            pe = float(r["phot_err"]) if r["phot_err"] else None
            m = float(r["ci"]) if r["ci"] else None
            me = float(r["ci_err"]) if r["ci_err"] else None
            out[int(r["Z"])] = (r["el"], p, pe, m, me)
    return out


def curve(tab):
    """(Z, log eps, 1 if photospheric else 0), photosphere preferred."""
    rows = []
    for z in sorted(tab):
        el, p, _, m, _ = tab[z]
        rows.append((z, p if p is not None else m, 1 if p is not None else 0))
    return rows


def number_ratio(logeps_x, logeps_y):
    """N_X / N_Y from two log eps values."""
    return 10 ** (logeps_x - logeps_y)


def dex(ratio):
    return math.log10(ratio)


def weighted_mean_difference(tab, exclude):
    """Weighted mean of photosphere - CI over elements with both values, weights
    1/(sigma_p^2 + sigma_m^2); returns (mean, its standard error, n)."""
    sw = swx = 0.0
    n = 0
    for z, (el, p, pe, m, me) in tab.items():
        if p is None or m is None or el in exclude:
            continue
        w = 1 / (pe * pe + me * me)
        sw += w
        swx += w * (p - m)
        n += 1
    return swx / sw, 1 / math.sqrt(sw), n


def main():
    tab = load()
    cur = curve(tab)
    write_table(__file__, ("Z", "logeps", "src"), cur, part="curve")
    write_table(__file__, ("Z", "logeps"), [(z, v) for z, v, _ in cur if z % 2 == 0], part="even")
    write_table(__file__, ("Z", "logeps"), [(z, v) for z, v, _ in cur if z % 2 == 1], part="odd")
    comp = []
    for z in sorted(tab):
        el, p, _, m, _ = tab[z]
        if p is None or m is None:
            continue
        g = 1 if el in METEORITE_DEPLETED else (2 if el in SUN_DEPLETED else 0)
        comp.append((z, p, m, p - m, g))
    write_table(__file__, ("Z", "phot", "ci", "diff", "group"), comp, part="compare")
    d, se, n = weighted_mean_difference(tab, METEORITE_DEPLETED | SUN_DEPLETED)
    lg = {tab[z][0]: v for z, v, _ in cur}
    vals = [["n_elements", len(tab)], ["n_photospheric", sum(s for _, _, s in cur)],
            ["n_both", len(comp)], ["mean_diff", d], ["mean_diff_se", se], ["n_mean", n],
            ["fe_per_h", number_ratio(lg["Fe"], lg["H"])],
            ["h_per_fe", number_ratio(lg["H"], lg["Fe"])],
            ["he_per_h", number_ratio(lg["He"], lg["H"])],
            ["o_per_fe", number_ratio(lg["O"], lg["Fe"])],
            ["fe_per_au", number_ratio(lg["Fe"], lg["Au"])],
            ["li_sun_over_ci", number_ratio(tab[3][1], tab[3][3])],
            ["sc_minus_ca", lg["Sc"] - lg["Ca"]], ["ti_minus_sc", lg["Ti"] - lg["Sc"]],
            ["be_minus_c", lg["Be"] - lg["C"]]]
    for el in ("H", "He", "Li", "Be", "B", "C", "O", "Fe", "Ni", "Sr", "Ba", "Eu", "Pt",
               "Au", "Pb", "Th", "U"):
        vals.append(["logeps_" + el, lg[el]])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

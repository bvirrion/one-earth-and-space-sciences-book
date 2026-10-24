"""Hydrolysis of feldspars and its three degrees (Year 1, weathering-clays).

A hydrolysis reaction is balanced the way the chapter's method does it: all the
aluminium stays in the solid product; the silicon the product cannot hold leaves
as silicic acid H4SiO4; the cations the product cannot hold leave as ions; the
hydrogen ion balances the charge; water balances the oxygen; the hydrogen count
is then a check. The arithmetic is exact (fractions).

Formulas (ledger webmineral:clays-b19, hom:albite, hom:anorthite, hom:orthoclase):
albite NaAlSi3O8, anorthite CaAl2Si2O8, orthoclase KAlSi3O8; the smectite beidellite
Na0.5Al2(Si3.5Al0.5)O10(OH)2 (its interlayer water left out), kaolinite
Al2Si2O5(OH)4, gibbsite Al(OH)3. Atomic weights: CIAAW abridged (ledger ciaaw:*).

  part degrees  degree Na Si Al siAl     per cent of each element of albite
                                         exported in solution, and the Si/Al of
                                         the solid left (1 bisiallitisation to
                                         beidellite, 2 monosiallitisation to
                                         kaolinite, 3 allitisation to gibbsite)
  part values   what value
"""
import os
import sys
from fractions import Fraction as F

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ATOMIC_WEIGHT = {"H": 1.0080, "C": 12.011, "O": 15.999, "Na": 22.990, "Mg": 24.305,
                 "Al": 26.982, "Si": 28.085, "K": 39.098, "Ca": 40.078}

MINERALS = {
    "albite": {"Na": F(1), "Al": F(1), "Si": F(3), "O": F(8)},
    "anorthite": {"Ca": F(1), "Al": F(2), "Si": F(2), "O": F(8)},
    "orthoclase": {"K": F(1), "Al": F(1), "Si": F(3), "O": F(8)},
    "beidellite": {"Na": F(1, 2), "Al": F(5, 2), "Si": F(7, 2), "O": F(12), "H": F(2)},
    "kaolinite": {"Al": F(2), "Si": F(2), "O": F(9), "H": F(4)},
    "gibbsite": {"Al": F(1), "O": F(3), "H": F(3)},
}
CHARGE = {"Na": 1, "K": 1, "Ca": 2, "Mg": 2}
SILICIC_ACID = {"Si": F(1), "O": F(4), "H": F(4)}
WATER = {"H": F(2), "O": F(1)}


def molar_mass(formula):
    return sum(float(n) * ATOMIC_WEIGHT[e] for e, n in formula.items())


def balance(mineral, product):
    """Coefficients of  a mineral + h H+ + w H2O -> 1 product + cations + s H4SiO4,
    returned as a dict with keys mineral, H+, H2O, product, H4SiO4 and each cation.
    All coefficients are exact fractions, scaled so that the product has 1."""
    m, p = MINERALS[mineral], MINERALS[product]
    a = p["Al"] / m["Al"]                       # aluminium stays in the solid
    out = {"mineral": a, "product": F(1)}
    out["H4SiO4"] = a * m.get("Si", 0) - p.get("Si", 0)
    charge = F(0)
    for c, z in CHARGE.items():
        n = a * m.get(c, 0) - p.get(c, 0)
        if n:
            out[c] = n
            charge += z * n
    out["H+"] = charge                          # charge balance
    o_left = a * m["O"]
    o_right = p["O"] + 4 * out["H4SiO4"]
    out["H2O"] = o_right - o_left               # oxygen balance
    return out


def check(mineral, product, coef=None):
    """Element and charge totals on each side; they must be equal."""
    coef = coef or balance(mineral, product)
    left, right = {}, {}

    def add(side, formula, n):
        for e, k in formula.items():
            side[e] = side.get(e, 0) + n * k

    add(left, MINERALS[mineral], coef["mineral"])
    add(left, {"H": F(1)}, coef["H+"])
    add(left, WATER, coef["H2O"])
    add(right, MINERALS[product], coef["product"])
    add(right, SILICIC_ACID, coef["H4SiO4"])
    for c in CHARGE:
        if c in coef:
            add(right, {c: F(1)}, coef[c])
    q_left = coef["H+"]
    q_right = sum(CHARGE[c] * coef[c] for c in CHARGE if c in coef)
    return left, right, q_left, q_right


def exported(mineral, product):
    """Fraction of each element of the mineral that leaves in solution."""
    coef = balance(mineral, product)
    m, p = MINERALS[mineral], MINERALS[product]
    frac = {}
    for e in ("Na", "K", "Ca", "Si", "Al"):
        if e in m:
            frac[e] = 1 - p.get(e, 0) / (coef["mineral"] * m[e])
    return frac


def si_al(formula):
    return formula.get("Si", 0) / formula["Al"]


def per_tonne(mineral, product):
    """Masses (kg) of product and of dissolved silica (as SiO2) and moles of H+ used,
    for the hydrolysis of 1000 kg of the mineral."""
    coef = balance(mineral, product)
    n = 1e6 / molar_mass(MINERALS[mineral])            # mol in a tonne
    k = n / float(coef["mineral"])
    m_sio2 = molar_mass({"Si": 1, "O": 2})
    return {"mol": n,
            "product_kg": k * molar_mass(MINERALS[product]) / 1000.0,
            "silica_kg": k * float(coef["H4SiO4"]) * m_sio2 / 1000.0,
            "h_mol": k * float(coef["H+"])}


DEGREES = (("bisiallitisation", "beidellite"), ("monosiallitisation", "kaolinite"),
           ("allitisation", "gibbsite"))


def main():
    rows = []
    for i, (_, product) in enumerate(DEGREES, start=1):
        f = exported("albite", product)
        rows.append((i, 100 * float(f["Na"]), 100 * float(f["Si"]), 100 * float(f["Al"]),
                     float(si_al(MINERALS[product]))))
    write_table(__file__, ("degree", "Na", "Si", "Al", "siAl"), rows, part="degrees")
    values = []
    for mineral, product in (("albite", "beidellite"), ("albite", "kaolinite"), ("albite", "gibbsite"),
                             ("anorthite", "kaolinite"), ("orthoclase", "kaolinite"),
                             ("anorthite", "gibbsite")):
        c = balance(mineral, product)
        for k in ("mineral", "H+", "H2O", "H4SiO4"):
            values.append(("%s_%s_%s" % (mineral, product, k), float(c[k])))
        t = per_tonne(mineral, product)
        for k in ("product_kg", "silica_kg", "h_mol"):
            values.append(("%s_%s_%s" % (mineral, product, k), t[k]))
    for name in ("albite", "anorthite", "orthoclase", "beidellite", "kaolinite", "gibbsite"):
        values.append(("M_%s" % name, molar_mass(MINERALS[name])))
    write_table(__file__, ("what", "value"), values, part="values")


if __name__ == "__main__":
    main()

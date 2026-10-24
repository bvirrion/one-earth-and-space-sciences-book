"""Minerals and the density of rocks (grade 11, minerals).

1. The mass fractions of the elements of the continental crust, computed from its
   oxide composition (Rudnick and Gao 2014, bulk continental crust, wt %; ledger
   rg14:crust) and the standard atomic weights (CIAAW abridged; ledger ciaaw:*).
   FeO* (all iron as FeO) is taken as FeO.
2. The density of a rock from the volume fractions of its minerals,
   rho = sum(phi_i * rho_i), with the mean mineral densities of webmineral.com
   (ledger wm:densities).

  part elements   symbol frac      element mass fractions of the bulk crust (%)
  part granite    idx phi rho      the granite of the problem: volume fraction, density
  part densities  idx rho          the minerals in order of density (names in DENSITY_ORDER)
  part rocks      rho              the densities of the three example rocks
  part numbers    key value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# standard atomic weights, g/mol (CIAAW abridged)
M = {"O": 15.999, "Si": 28.085, "Ti": 47.867, "Al": 26.982, "Fe": 55.845, "Mn": 54.938,
     "Mg": 24.305, "Ca": 40.078, "Na": 22.990, "K": 39.098, "P": 30.974}

# oxide: (cation, cations per formula, oxygens per formula)
OXIDES = {"SiO2": ("Si", 1, 2), "TiO2": ("Ti", 1, 2), "Al2O3": ("Al", 2, 3), "FeO": ("Fe", 1, 1),
          "MnO": ("Mn", 1, 1), "MgO": ("Mg", 1, 1), "CaO": ("Ca", 1, 1), "Na2O": ("Na", 2, 1),
          "K2O": ("K", 2, 1), "P2O5": ("P", 2, 5)}

# Rudnick and Gao (2014), wt %: bulk and upper continental crust
BULK = {"SiO2": 60.6, "TiO2": 0.72, "Al2O3": 15.9, "FeO": 6.71, "MnO": 0.10, "MgO": 4.66,
        "CaO": 6.41, "Na2O": 3.07, "K2O": 1.81, "P2O5": 0.13}
UPPER = {"SiO2": 66.6, "TiO2": 0.64, "Al2O3": 15.4, "FeO": 5.04, "MnO": 0.10, "MgO": 2.48,
         "CaO": 3.59, "Na2O": 3.27, "K2O": 2.80, "P2O5": 0.15}

# webmineral.com: formula and mean density (g/cm3)
MINERALS = {
    "quartz": ("SiO2", 2.62),
    "orthoclase": ("KAlSi3O8", 2.56),
    "oligoclase": ("(Na,Ca)(Si,Al)4O8", 2.65),
    "labradorite": ("(Ca,Na)(Si,Al)4O8", 2.69),
    "biotite": ("K(Mg,Fe)3AlSi3O10(OH,F)2", 3.09),
    "muscovite": ("KAl2(Si3Al)O10(OH,F)2", 2.82),
    "hornblende": ("Ca2[Mg4(Al,Fe)]Si7AlO22(OH)2", 3.23),
    "augite": ("(Ca,Na)(Mg,Fe,Al,Ti)(Si,Al)2O6", 3.4),
    "olivine": ("(Mg,Fe)2SiO4", 3.32),
}

# the granite of the weekend problem: a point count of 500 points (exercise data)
GRANITE_COUNT = {"quartz": 150, "orthoclase": 175, "oligoclase": 125, "biotite": 30, "muscovite": 20}


def oxide_mass(ox):
    c, n, o = OXIDES[ox]
    return n * M[c] + o * M["O"]


def element_fractions(comp):
    """Mass fractions (%) of the elements, normalised to the oxide total."""
    total = sum(comp.values())
    frac = {"O": 0.0}
    for ox, w in comp.items():
        c, n, o = OXIDES[ox]
        m = oxide_mass(ox)
        frac[c] = frac.get(c, 0.0) + 100.0 * w / total * n * M[c] / m
        frac["O"] += 100.0 * w / total * o * M["O"] / m
    return frac


def rock_density(fractions):
    """Density (g/cm3) of a rock from {mineral: volume fraction}; fractions sum to 1."""
    s = sum(fractions.values())
    assert abs(s - 1.0) < 1e-9, s
    return sum(phi * MINERALS[m][1] for m, phi in fractions.items())


def from_count(count):
    n = sum(count.values())
    return {m: k / n for m, k in count.items()}


EXAMPLES = {
    "granite": from_count(GRANITE_COUNT),
    "basalt": {"labradorite": 0.55, "augite": 0.35, "olivine": 0.10},
    "peridotite": {"olivine": 0.75, "augite": 0.25},
}


def density_order():
    """The minerals sorted from the lightest to the densest."""
    return sorted(MINERALS, key=lambda m: MINERALS[m][1])


def numbers():
    n = {}
    fb, fu = element_fractions(BULK), element_fractions(UPPER)
    for el in ("O", "Si", "Al", "Fe", "Ca", "Mg", "Na", "K"):
        n["bulk_" + el], n["upper_" + el] = fb[el], fu[el]
    n["bulk_O_Si"] = fb["O"] + fb["Si"]
    for name, fr in EXAMPLES.items():
        n["rho_" + name] = rock_density(fr)
    # weighing in air and in water of a 100 cm3 piece of the granite
    rho = n["rho_granite"]
    n["granite_air_g"] = 100 * rho
    n["granite_water_g"] = 100 * rho - 100.0
    return n


if __name__ == "__main__":
    fb = element_fractions(BULK)
    write_table(__file__, ("symbol", "frac"), sorted(fb.items(), key=lambda kv: -kv[1]), part="elements",
                digits=4)
    fr = EXAMPLES["granite"]
    write_table(__file__, ("idx", "phi", "rho"),
                [(i, fr[m], MINERALS[m][1]) for i, m in enumerate(GRANITE_COUNT)], part="granite")
    write_table(__file__, ("idx", "rho"), [(i, MINERALS[m][1]) for i, m in enumerate(density_order())],
                part="densities")
    write_table(__file__, ("rho",), [(rock_density(EXAMPLES[r]),) for r in ("granite", "basalt", "peridotite")],
                part="rocks")
    print("density order:", ", ".join(density_order()))
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

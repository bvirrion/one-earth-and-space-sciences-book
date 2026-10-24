"""The olivine solid solution forsterite Mg2SiO4 -- fayalite Fe2SiO4 (Year 1,
rock-forming-minerals), and the recalculation of a mineral analysis.

Ideal mixing: the molar mass and the molar volume are linear in the forsterite
fraction x; the density is their ratio. End-member densities are the measured
values of the Handbook of Mineralogy (ledger hom:forsterite, hom:fayalite);
atomic weights are CIAAW's abridged values (ledger ciaaw:*).

The olivine analysis (OLIVINE_WT) is invented for the chapter's problem: an
olivine of about Fo82 such as basalts carry. It is not a real-world analysis.

  part curve   x_fo M V rho rho_lin     molar mass (g/mol), molar volume
                                        (cm3/mol), density and the straight
                                        line between the end-member densities
  part values  what value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

AW = {"O": 15.999, "Si": 28.085, "Mg": 24.305, "Fe": 55.845, "Ca": 40.078,
      "Al": 26.982, "Na": 22.990, "K": 39.098, "Mn": 54.938, "Ni": 58.693}
RHO_FO = 3.275          # g/cm3, measured (Handbook of Mineralogy)
RHO_FA = 4.392

# oxide: (cation, cations per oxide, oxygens per oxide)
OXIDES = {"SiO2": ("Si", 1, 2), "FeO": ("Fe", 1, 1), "MnO": ("Mn", 1, 1), "MgO": ("Mg", 1, 1),
          "NiO": ("Ni", 1, 1), "CaO": ("Ca", 1, 1), "Al2O3": ("Al", 2, 3), "Na2O": ("Na", 2, 1),
          "K2O": ("K", 2, 1)}
OLIVINE_WT = {"SiO2": 39.50, "FeO": 16.53, "MnO": 0.23, "MgO": 43.32, "NiO": 0.20, "CaO": 0.22}


def molar_mass_oxide(ox):
    c, n, o = OXIDES[ox]
    return n * AW[c] + o * AW["O"]


def m_fo():
    return 2 * AW["Mg"] + AW["Si"] + 4 * AW["O"]


def m_fa():
    return 2 * AW["Fe"] + AW["Si"] + 4 * AW["O"]


def v_fo():
    return m_fo() / RHO_FO


def v_fa():
    return m_fa() / RHO_FA


def molar_mass(x):
    return x * m_fo() + (1 - x) * m_fa()


def molar_volume(x):
    return x * v_fo() + (1 - x) * v_fa()


def density(x):
    return molar_mass(x) / molar_volume(x)


def cations(wt, n_oxygen=4):
    """Cations per formula unit on n_oxygen oxygens, from oxide weight per cent.
    Returns (dict cation -> number, normalisation factor, table of steps)."""
    steps = []
    o_total = 0.0
    for ox, w in wt.items():
        mol = w / molar_mass_oxide(ox)
        c, n, o = OXIDES[ox]
        steps.append((ox, w, molar_mass_oxide(ox), mol, mol * o, mol * n))
        o_total += mol * o
    f = n_oxygen / o_total
    out = {}
    for ox, w, mm, mol, mo, mc in steps:
        out[OXIDES[ox][0]] = mc * f
    return out, f, steps


def forsterite_percent(cat):
    """Fo = 100 Mg/(Mg + Fe) on the olivine's octahedral cations (Mn, Ni, Ca aside)."""
    return 100 * cat["Mg"] / (cat["Mg"] + cat["Fe"])


if __name__ == "__main__":
    rows = []
    for i in range(0, 101, 5):
        x = i / 100
        rows.append((i, molar_mass(x), molar_volume(x), density(x), RHO_FA + x * (RHO_FO - RHO_FA)))
    write_table(__file__, ("x_fo", "M", "V", "rho", "rho_lin"), rows, part="curve", digits=6)
    cat, f, _ = cations(OLIVINE_WT)
    vals = [("M_fo", m_fo()), ("M_fa", m_fa()), ("V_fo", v_fo()), ("V_fa", v_fa()), ("factor", f)]
    vals += [("cat_" + k, v) for k, v in cat.items()]
    fo = forsterite_percent(cat)
    vals += [("Fo", fo), ("rho_ol", density(fo / 100))]
    write_table(__file__, ("what", "value"), vals, part="values", digits=7)

"""Element abundances of the Earth's reservoirs (Year 2, elements-in-the-earth).

Reference compositions, ppm by mass unless stated:
  CI    CI chondrites, Lodders (2003) Table 3            ledger lodders:ci-table
  PM    primitive mantle = bulk silicate Earth, McDonough and Sun (1995)  ms95:pm-trace
  MORB  ALL MORB mean, Gale et al. (2013) Table 1        gale13:allmorb
  OIB   Hawaiian basalt BHVO-2, USGS (Jochum et al. 2016) usgs:bhvo2-major, usgs:bhvo2-trace
  UCC   upper continental crust, Rudnick and Gao         rg03:ucc-trace
  CORE  core model, McDonough (2003)                     mcd03:core
Condensation temperatures from condensation.py (lodders:tc-table, lodders:tc-more).
Partition coefficients: Budahn (1991) Table 2A (budahn91:d-ree, budahn91:modes).
Core mass fraction from the shared PREM table (data:prem).

  part ree     idx el morb oib ucc          CI-normalised rare earths (Tm left out: no MORB value)
  part spider  idx el morb oib ucc          primitive-mantle-normalised, incompatible first
  part volat   T ratio el                   (X/Mg)_PM / (X/Mg)_CI against 50 % condensation T,
               one file per class: volat-lith, volat-sid, volat-chal
  part budget  idx el share                per cent of the Earth's inventory held in the core
  part dvals   idx el cpx gar ol bulk       partition coefficients and the bulk value of the rock
  part values  what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from _table import write_table  # noqa: E402
import condensation  # noqa: E402

CI = {"Li": 1.46, "B": 0.713, "F": 60.6, "Na": 5010, "Mg": 95870, "Al": 8500, "Si": 106500,
      "S": 54100, "Cl": 704, "K": 530, "Ca": 9070, "Sc": 5.83, "Ti": 440, "V": 55.7,
      "Cr": 2590, "Mn": 1910, "Fe": 182800, "Co": 502, "Ni": 10640, "Cu": 127, "Zn": 310,
      "Ge": 33.2, "Se": 19.7, "Br": 3.43, "Rb": 2.13, "Sr": 7.74, "Y": 1.53, "Zr": 3.96,
      "Nb": 0.265, "Mo": 1.02, "Ru": 0.692, "Pd": 0.588, "Ag": 0.201, "Cd": 0.675, "Sn": 1.68,
      "Te": 2.33, "I": 0.48, "Cs": 0.185, "Ba": 2.31, "La": 0.232, "Ce": 0.621, "Pr": 0.0928,
      "Nd": 0.457, "Sm": 0.145, "Eu": 0.0546, "Gd": 0.198, "Tb": 0.0356, "Dy": 0.238,
      "Ho": 0.0562, "Er": 0.162, "Tm": 0.0237, "Yb": 0.163, "Lu": 0.0237, "Hf": 0.115,
      "Ta": 0.0144, "W": 0.089, "Re": 0.037, "Os": 0.486, "Ir": 0.470, "Pt": 1.004,
      "Au": 0.146, "Pb": 2.56, "Th": 0.0309, "U": 0.0084}

PM = {"Li": 1.6, "B": 0.3, "F": 25, "Na": 2670, "Mg": 228000, "Al": 23500, "Si": 210000,
      "S": 250, "Cl": 17, "K": 240, "Ca": 25300, "Sc": 16.2, "Ti": 1205, "V": 82, "Cr": 2625,
      "Mn": 1045, "Fe": 62600, "Co": 105, "Ni": 1960, "Cu": 30, "Zn": 55, "Ge": 1.1,
      "Se": 0.075, "Br": 0.05, "Rb": 0.6, "Sr": 19.9, "Y": 4.3, "Zr": 10.5, "Nb": 0.658,
      "Mo": 0.050, "Ru": 0.005, "Pd": 0.0039, "Ag": 0.008, "Cd": 0.040, "Sn": 0.13,
      "Te": 0.012, "I": 0.01, "Cs": 0.021, "Ba": 6.6, "La": 0.648, "Ce": 1.675, "Pr": 0.254,
      "Nd": 1.25, "Sm": 0.406, "Eu": 0.154, "Gd": 0.544, "Tb": 0.099, "Dy": 0.674,
      "Ho": 0.149, "Er": 0.438, "Tm": 0.068, "Yb": 0.441, "Lu": 0.0675, "Hf": 0.283,
      "Ta": 0.037, "W": 0.029, "Re": 0.00028, "Os": 0.0034, "Ir": 0.0032, "Pt": 0.0071,
      "Au": 0.001, "Pb": 0.15, "Th": 0.0795, "U": 0.0203}

# element mass fraction of the oxide (K in K2O, Ti in TiO2)
K_IN_K2O = 2 * 39.098 / (2 * 39.098 + 15.999)
TI_IN_TIO2 = 47.867 / (47.867 + 2 * 15.999)

MORB = {"Cs": 0.034, "Rb": 2.88, "Ba": 29.2, "Th": 0.404, "U": 0.119, "Nb": 5.24, "Ta": 0.34,
        "K": 0.160e4 * K_IN_K2O, "La": 5.21, "Ce": 14.86, "Pb": 0.57, "Pr": 2.24, "Sr": 129,
        "Nd": 12.03, "Zr": 116.9, "Hf": 2.79, "Sm": 3.82, "Eu": 1.36, "Ti": 1.68e4 * TI_IN_TIO2,
        "Gd": 4.99, "Tb": 0.90, "Dy": 6.08, "Y": 36.8, "Ho": 1.28, "Er": 3.79, "Yb": 3.63,
        "Lu": 0.53}
OIB = {"Cs": 0.0996, "Rb": 9.261, "Ba": 130.9, "Th": 1.224, "U": 0.412, "Nb": 18.10,
       "Ta": 1.154, "K": 0.5130e4 * K_IN_K2O, "La": 15.20, "Ce": 37.53, "Pb": 1.653,
       "Pr": 5.339, "Sr": 394.1, "Nd": 24.27, "Zr": 171.2, "Hf": 4.470, "Sm": 6.023,
       "Eu": 2.043, "Ti": 2.731e4 * TI_IN_TIO2, "Gd": 6.207, "Tb": 0.9392, "Dy": 5.280,
       "Y": 25.91, "Ho": 0.9887, "Er": 2.511, "Yb": 1.994, "Lu": 0.2754}
UCC = {"Cs": 4.9, "Rb": 84, "Ba": 624, "Th": 10.5, "U": 2.7, "Nb": 12, "Ta": 0.9,
       "K": 2.8e4 * K_IN_K2O, "La": 31, "Ce": 63, "Pb": 17, "Pr": 7.1, "Sr": 320, "Nd": 27,
       "Zr": 193, "Hf": 5.3, "Sm": 4.7, "Eu": 1.0, "Ti": 0.64e4 * TI_IN_TIO2, "Gd": 4.0,
       "Tb": 0.7, "Dy": 3.9, "Y": 21, "Ho": 0.83, "Er": 2.3, "Yb": 2.0, "Lu": 0.31}

CORE = {"Fe": 85.5, "Ni": 5.2, "Si": 6.0, "S": 1.90}        # wt %
CORE_PPM = {"Fe": 855000, "Ni": 52000, "Si": 60000, "S": 19000, "Cr": 9000, "Mo": 5,
            "W": 0.47, "Re": 0.23, "Os": 2.8, "Ir": 2.6, "Pt": 5.7, "Au": 0.5, "Mg": 0,
            "Al": 0, "Ca": 0, "K": 0}                       # mcd03:core
BUDGET = ["Ir", "Pt", "Au", "Mo", "S", "Ni", "W", "Fe", "Cr", "Si", "Mg", "Al", "Ca", "K"]

REE = ["La", "Ce", "Pr", "Nd", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Yb", "Lu"]
SPIDER = ["Cs", "Rb", "Ba", "Th", "U", "Nb", "Ta", "K", "La", "Ce", "Pb", "Pr", "Sr", "Nd",
          "Zr", "Hf", "Sm", "Eu", "Ti", "Gd", "Tb", "Dy", "Y", "Ho", "Er", "Yb", "Lu"]

TC_MORE = {"Th": 1659, "Ir": 1603, "Mo": 1590, "Ru": 1551, "La": 1578, "Ce": 1478,
           "Yb": 1487, "Pt": 1408, "Eu": 1356, "Pd": 1324, "B": 908, "Ge": 883, "Cs": 799,
           "Te": 709, "Sn": 704, "Se": 697, "Br": 546, "I": 535, "Hf": 1684, "Sc": 1659,
           "Y": 1659, "Lu": 1659, "F": 734, "Ag": 996}   # last two: lodders:tc-table
TC = dict(condensation.TC)
TC.update(TC_MORE)

LITH = ["Zr", "Hf", "Al", "Sc", "Y", "Lu", "Th", "U", "Ti", "La", "Ca", "Yb", "Ce", "Sr",
        "Ba", "Eu", "Mg", "Si", "Mn", "Li", "K", "Na", "Cl", "B", "Rb", "Cs", "F", "Br", "I"]
SID = ["Re", "Os", "W", "Ir", "Mo", "Ru", "Pt", "Ni", "Co", "Fe", "Pd", "Au", "Ge"]
CHAL = ["Cu", "Ag", "Zn", "Pb", "Te", "Sn", "Se", "S", "Cd"]

# Budahn (1991) Table 2A: cpx, garnet, olivine+opx+spinel
D = {"La": (0.058, 0.001, 0.001), "Ce": (0.10, 0.0065, 0.0025), "Nd": (0.24, 0.035, 0.0075),
     "Sm": (0.40, 0.11, 0.016), "Eu": (0.48, 0.15, 0.022), "Gd": (0.52, 0.24, 0.030),
     "Tb": (0.59, 0.56, 0.057), "Yb": (0.58, 4.5, 0.16), "Lu": (0.53, 5.8, 0.18)}
MODES = (0.65, 0.18, 0.17)


def core_share(el, x):
    """fraction of the Earth's inventory of el held by a core of mass fraction x"""
    c = x * CORE_PPM[el]
    return c / (c + (1 - x) * PM[el])


def mg_normalised(el):
    """(X/Mg) in the bulk silicate Earth divided by (X/Mg) in CI chondrites"""
    return (PM[el] / PM["Mg"]) / (CI[el] / CI["Mg"])


def normalised(comp, ref, els):
    return [comp[e] / ref[e] for e in els]


def eu_anomaly(comp, ref=CI):
    """Eu/Eu* = Eu_N / sqrt(Sm_N Gd_N)"""
    n = {e: comp[e] / ref[e] for e in ("Sm", "Eu", "Gd")}
    return n["Eu"] / math.sqrt(n["Sm"] * n["Gd"])


def bulk_d(el, modes=MODES):
    return sum(x * d for x, d in zip(modes, D[el]))


def core_fraction(el, core=CORE, bse=PM, ci=CI):
    """Core mass fraction x from a chondritic X/Mg ratio for the bulk Earth:
    (1-x) X_bse + x X_core = r (1-x) Mg_bse, r = (X/Mg)_CI, no Mg in the core."""
    r = ci[el] / ci["Mg"]
    y = (r * bse["Mg"] - bse[el]) / (core[el] * 1e4)      # y = x/(1-x)
    return y / (1 + y)


def core_fraction_lsq(els=("Fe", "Ni"), core=CORE, bse=PM, ci=CI):
    a = [core[e] * 1e4 for e in els]
    b = [ci[e] / ci["Mg"] * bse["Mg"] - bse[e] for e in els]
    y = sum(p * q for p, q in zip(a, b)) / sum(p * p for p in a)
    return y / (1 + y)


def prem_core_fraction(path=os.path.join(HERE, "..", "..", "data", "derived", "prem.csv")):
    rows = [(float(r["depth_km"]), float(r["rho_g_cm3"]), r["region"])
            for r in csv.DictReader(open(path, encoding="utf8"))]
    R = 6371.0

    def mass(pred):
        m = 0.0
        for (d1, r1, g1), (d2, r2, _) in zip(rows, rows[1:]):
            if d2 <= d1 or not pred(g1):
                continue
            a, b, n = R - d2, R - d1, 50
            for i in range(n):          # density linear in radius within a layer
                ra, rb = a + (b - a) * i / n, a + (b - a) * (i + 1) / n
                rm = 0.5 * (ra + rb)
                m += 4 * math.pi * rm * rm * (rb - ra) * (r2 + (r1 - r2) * (rm - a) / (b - a))
        return m * 1e12                  # km3 x g/cm3 -> kg
    return mass(lambda g: "core" in g) / mass(lambda g: True), mass(lambda g: True)


if __name__ == "__main__":
    write_table(__file__, ("idx", "el", "morb", "oib", "ucc"),
                [(i + 1, e, MORB[e] / CI[e], OIB[e] / CI[e], UCC[e] / CI[e])
                 for i, e in enumerate(REE)], part="ree", digits=4)
    write_table(__file__, ("idx", "el", "morb", "oib", "ucc"),
                [(i + 1, e, MORB[e] / PM[e], OIB[e] / PM[e], UCC[e] / PM[e])
                 for i, e in enumerate(SPIDER)], part="spider", digits=4)
    for name, els in (("lith", LITH), ("sid", SID), ("chal", CHAL)):
        write_table(__file__, ("T", "ratio", "el"),
                    sorted(((TC[e], mg_normalised(e), e) for e in els), reverse=True),
                    part="volat-" + name, digits=4)
    write_table(__file__, ("idx", "el", "cpx", "gar", "ol", "bulk"),
                [(i + 1, e) + D[e] + (bulk_d(e),) for i, e in enumerate(D)], part="dvals",
                digits=4)
    xp, mtot = prem_core_fraction()
    write_table(__file__, ("idx", "el", "share"),
                [(i + 1, e, 100 * core_share(e, xp)) for i, e in enumerate(BUDGET)],
                part="budget", digits=4)
    vals = [("core_fraction_Fe", core_fraction("Fe")), ("core_fraction_Ni", core_fraction("Ni")),
            ("core_fraction_lsq", core_fraction_lsq()), ("prem_core_fraction", xp),
            ("prem_earth_mass", mtot),
            ("eu_ucc", eu_anomaly(UCC)), ("eu_morb", eu_anomaly(MORB)), ("eu_oib", eu_anomaly(OIB)),
            ("al_mg_norm", mg_normalised("Al")), ("ni_mg_norm", mg_normalised("Ni")),
            ("ir_mg_norm", mg_normalised("Ir")), ("k_mg_norm", mg_normalised("K"))]
    write_table(__file__, ("what", "value"), vals, part="values", digits=5)

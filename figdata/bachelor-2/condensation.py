"""Condensation sequence (Year 2, planet-formation-meteorites): 50 percent condensation
temperatures of a solar-system composition gas at 1e-4 bar (Lodders 2003, Table 8; ledger
lodders:tc-table, lodders:tc-more) and Lodders' volatility groups (ledger lodders:groups).

  part <group>  idx  T  name     one file per group (ultra, high, refr, common, modvol, vol,
                                  hivol), idx = rank from the coldest (1) to the hottest
  part labels   idx  name
  part values   what value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# (element, 50 % condensation temperature K)
TC = [("Re", 1821), ("Os", 1812), ("W", 1789), ("Zr", 1741), ("Al", 1653),
      ("U", 1610), ("Ti", 1582), ("Ca", 1517),
      ("Sr", 1464), ("Ba", 1455), ("V", 1429), ("Pt", 1408),
      ("Ni", 1353), ("Co", 1352), ("Mg", 1336), ("Fe", 1334), ("Si", 1310), ("Cr", 1296),
      ("P", 1229), ("Mn", 1158), ("Li", 1142), ("Au", 1060), ("Cu", 1037), ("K", 1006),
      ("Na", 958), ("Cl", 948), ("Rb", 800), ("Pb", 727), ("Zn", 726),
      ("S", 664), ("Cd", 652), ("Tl", 532),
      ("Hg", 252), ("O", 180), ("N", 123), ("C", 40)]

# lower bounds of Lodders' groups (K); "common" = Mg, Si, Fe range 1290-1360
GROUPS = [("ultra", 1650), ("high", 1500), ("refr", 1360), ("common", 1290),
          ("modvol", 704), ("vol", 371), ("hivol", 0)]


def group(T):
    for name, lo in GROUPS:
        if T > lo:
            return name
    return "hivol"


def ranked():
    """(idx, T, name) from the coldest (idx 1) to the hottest"""
    s = sorted(TC, key=lambda e: e[1])
    return [(i + 1, t, n) for i, (n, t) in enumerate(s)]


if __name__ == "__main__":
    rows = ranked()
    for g, _ in GROUPS:
        write_table(__file__, ("idx", "T", "name"), [r for r in rows if group(r[1]) == g], part=g)
    write_table(__file__, ("idx", "name"), [(r[0], r[2]) for r in rows], part="labels")
    vals = [("n_elements", len(rows))] + [("count_" + g, sum(1 for r in rows if group(r[1]) == g))
                                           for g, _ in GROUPS]
    write_table(__file__, ("what", "value"), vals, part="values")

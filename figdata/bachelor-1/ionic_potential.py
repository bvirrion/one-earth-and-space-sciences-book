"""The ionic-potential diagram (Year 1, weathering-clays).

Each ion is placed by its effective ionic radius r (angstrom, Shannon 1976, sixfold
coordination, high spin where that applies; ledger shannon:radii-b19) and its
charge z. The ionic potential is z/r. Two straight lines through the origin,
z/r = 3 and z/r = 10 per angstrom (ledger nomad:goldschmidt), divide the diagram
into the soluble cations (below 3), the hydrolysates (3 to 10) and the soluble
oxyanions (above 10).

  part ions     r z ip field label tex anc   one row per ion (field 0, 1, 2, -1 on a
                                              boundary); tex is the printed label and
                                              anc the TikZ anchor angle that places it
  part lines    r z3 z10                the two boundaries, z = 3r and z = 10r
  part values   what value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

LOW, HIGH = 3.0, 10.0      # boundaries of z/r, per angstrom

# symbol, charge, radius (angstrom, VI coordination), label written in the figure
IONS = [
    ("Cs", 1, 1.67), ("Rb", 1, 1.52), ("K", 1, 1.38), ("Na", 1, 1.02), ("Li", 1, 0.76),
    ("Ba", 2, 1.35), ("Sr", 2, 1.18), ("Ca", 2, 1.00), ("Mn2", 2, 0.83), ("Fe2", 2, 0.78),
    ("Mg", 2, 0.72), ("Be", 2, 0.45),
    ("Fe3", 3, 0.645), ("Al", 3, 0.535), ("B", 3, 0.27),
    ("Th", 4, 0.94), ("Zr", 4, 0.72), ("Ti", 4, 0.605), ("Mn4", 4, 0.53), ("Si", 4, 0.40),
    ("C", 4, 0.16),
    ("P", 5, 0.38), ("N", 5, 0.13),
    ("S", 6, 0.29),
]

# where the printed label goes: a = above, b = below, l = left, r = right, bl = below left
PLACE = {"Cs": "a", "Rb": "a", "K": "a", "Na": "a", "Li": "a", "Ba": "a", "Sr": "a", "Ca": "a",
         "Mn2": "b", "Fe2": "a", "Mg": "bl", "Be": "a", "Fe3": "a", "Al": "b", "B": "l",
         "Th": "a", "Zr": "a", "Ti": "b", "Mn4": "a", "Si": "l", "C": "r", "P": "r", "N": "r", "S": "r"}
ANCHOR = {"a": 270, "b": 90, "l": 0, "r": 180, "bl": 45}

FIELDS = ("soluble cation", "hydrolysate", "soluble oxyanion")


def ionic_potential(z, r):
    """z/r, the charge over the radius in angstrom."""
    return z / r


def field(z, r, tol=0.05):
    """0 soluble cation, 1 hydrolysate, 2 soluble oxyanion; -1 on a boundary
    (within tol of 3 or 10, as silicon is)."""
    ip = ionic_potential(z, r)
    if abs(ip - LOW) < tol or abs(ip - HIGH) < tol:
        return -1
    if ip < LOW:
        return 0
    if ip < HIGH:
        return 1
    return 2


def ion(symbol):
    for s, z, r in IONS:
        if s == symbol:
            return z, r
    raise KeyError(symbol)


def tex_label(symbol, z):
    base = "".join(ch for ch in symbol if ch.isalpha())
    return "%s$^{%s+}$" % (base, "" if z == 1 else z)


def main():
    rows = []
    for s, z, r in IONS:
        rows.append((r, z, round(ionic_potential(z, r), 4), field(z, r), s, tex_label(s, z), ANCHOR[PLACE[s]]))
    write_table(__file__, ("r", "z", "ip", "field", "label", "tex", "anc"), rows, part="ions")
    lines = [(r / 100.0, LOW * r / 100.0, HIGH * r / 100.0) for r in range(0, 181, 5)]
    write_table(__file__, ("r", "z3", "z10"), lines, part="lines")
    values = [("ip_%s" % s, round(ionic_potential(z, r), 3)) for s, z, r in IONS]
    write_table(__file__, ("what", "value"), values, part="values")


if __name__ == "__main__":
    main()

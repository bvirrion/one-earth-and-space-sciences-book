"""Planets compared (Year 1, comparative-planetology).

part bodies: radius and mean density of the eight planets, the Moon and
  Pluto, read from the shared ledger rows planet:<Body>.diameter and
  planet:<Body>.density (NASA planetary fact sheet) in sources/data_ledger.md,
  so that the figure cannot drift from the ledger.
part temps: equilibrium temperature T_eq = [S (1 - A) / (4 sigma)]^(1/4) and
  the mean surface temperature for the Moon, Mars, the Earth and Venus. S and
  the Bond albedo A from the NASA fact sheets (ledger nasa:moon, nasa:mars,
  nasa:venus; earth:TSI, earth:albedo); sigma exact (const:sigma). Mean
  surface temperatures: planet:Moon.Tmean (-20 C), nasa:mars (about 214 K),
  earth:Tsurf (288 K), nasa:venus (737 K).

  part bodies  idx name R_km density
  part temps   idx name Teq Tsurf
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
LEDGER = os.path.join(ROOT, "sources", "data_ledger.md")
BODIES = ("Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto")
SIGMA = 5.670374419e-8
# (name, S in W/m2, Bond albedo, mean surface temperature in K)
TEMPS = (("Moon", 1361.0, 0.11, 273.15 - 20.0),
         ("Mars", 586.2, 0.250, 214.0),
         ("Earth", 1361.0, 0.294, 288.0),
         ("Venus", 2601.3, 0.77, 737.0))


def ledger_value(row_id, path=LEDGER):
    pat = re.compile(r"^\|\s*%s\s*\|[^|]*\|\s*([^|]+?)\s*\|" % re.escape(row_id))
    for line in open(path, encoding="utf-8"):
        m = pat.match(line)
        if m:
            return float(m.group(1))
    raise KeyError(row_id)


def bodies():
    return [(i, name, ledger_value("planet:%s.diameter" % name) / 2.0, ledger_value("planet:%s.density" % name))
            for i, name in enumerate(BODIES)]


def t_eq(S, A):
    return (S * (1.0 - A) / (4.0 * SIGMA)) ** 0.25


def temps():
    return [(i, n, t_eq(S, A), Ts) for i, (n, S, A, Ts) in enumerate(TEMPS)]


if __name__ == "__main__":
    write_table(__file__, ("idx", "name", "R_km", "density"), bodies(), part="bodies", digits=6)
    write_table(__file__, ("idx", "name", "Teq", "Tsurf"), temps(), part="temps", digits=5)

"""Crustal melting: solidi, water budgets and the aluminium saturation index (Year 2,
crustal-melting).

  solidi    water-saturated solidus of a biotite granite: 680 C at 2 kbar and 620 C at
            10 kbar (Stern and Wyllie 1981, ledger sw81:wet-solidus), 605 C at 15.3 kbar
            (Boettcher and Wyllie 1968, ledger bw68:wet-solidus); drawn as straight segments
            between the published points, nothing extrapolated.
            Dehydration-melting brackets, drawn as boxes: muscovite schist 750-800 C at
            6-10 kbar (Patino Douce and Harris 1998, pdh98:himalaya); biotite 800-850 C at
            5-7 kbar (Berger and Kalt 1999, bk99:migmatites); amphibole 875-925 C at
            10-12.5 kbar (Skjerlie and Johnston 1996, sj96:amphibole).
            Paths: the pt-paths thickening model (figdata/bachelor-2/ptpaths.py), for the
            rock that starts at 35 km (the chapter-11 path) and for the base of the
            thickened crust (70 km after stacking).
  water     H2O solubility of haplogranite AOQ at 800 C (Holtz et al. 1995, Table 3,
            holtz95:solubility) and its least-squares line between 3 and 8 kbar.
  asi       Shand's indices A/CNK = Al2O3/(CaO + Na2O + K2O) and A/NK = Al2O3/(Na2O + K2O),
            molar, for BHVO-2 (usgs:bhvo2-major), AGV-2 (usgs:agv2-major), SRM 278
            (nist278:majors) and two invented granites (book's own, labelled as such).
  budget    water-limited melt fraction F = X_hyd w_hyd / c_melt (mass balance).

  part solidi   P_kbar, T_C of the wet solidus points
  part boxes    name, Tmin, Tmax, Pmin, Pmax
  part path35   t_Myr, T_C, P_kbar (every 1 Myr)
  part path70   t_Myr, T_C, P_kbar (every 1 Myr)
  part water    P_kbar, H2O_wt
  part waterfit P_kbar, H2O_wt at the ends of the 3-8 kbar fit
  part asi      name, ACNK, ANK
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))
from _table import write_table  # noqa: E402

# molar masses (g/mol) from standard atomic weights
M = {"Al2O3": 101.961, "CaO": 56.077, "Na2O": 61.979, "K2O": 94.196}
M_MUSCOVITE = 398.31      # KAl3Si3O10(OH)2
M_PHLOGOPITE = 417.26     # KMg3AlSi3O10(OH)2
M_H2O = 18.015

WET = [(2.0, 680.0), (10.0, 620.0), (15.3, 605.0)]          # (P kbar, T C)
BOXES = [("muscovite", 750.0, 800.0, 6.0, 10.0),
         ("biotite", 800.0, 850.0, 5.0, 7.0),
         ("amphibole", 875.0, 925.0, 10.0, 12.5)]
AOQ = [(0.5, 2.80), (1.0, 4.09), (3.0, 7.45), (4.0, 8.94), (5.0, 9.97), (8.0, 13.82)]

ROCKS = {
    "BHVO-2": {"Al2O3": 13.44, "CaO": 11.40, "Na2O": 2.219, "K2O": 0.5130},
    "AGV-2": {"Al2O3": 17.03, "CaO": 5.15, "Na2O": 4.204, "K2O": 2.898},
    "SRM-278": {"Al2O3": 14.15, "CaO": 0.983, "Na2O": 4.84, "K2O": 4.16},
    # invented compositions (book's own, for the figure and the problem)
    "S-leuco": {"Al2O3": 15.0, "CaO": 0.55, "Na2O": 3.4, "K2O": 4.9},
    "peralk": {"Al2O3": 10.5, "CaO": 0.30, "Na2O": 4.6, "K2O": 4.5},
}


def wet_solidus(p_kbar):
    """T (C) on the published wet solidus, linear between points; nan outside 2-15.3 kbar."""
    p = np.asarray(p_kbar, dtype=float)
    ps, ts = zip(*WET)
    return np.where((p >= ps[0]) & (p <= ps[-1]), np.interp(p, ps, ts), np.nan)


def moles(ox):
    return {k: ox[k] / M[k] for k in M}


def acnk(ox):
    m = moles(ox)
    return m["Al2O3"] / (m["CaO"] + m["Na2O"] + m["K2O"])


def ank(ox):
    m = moles(ox)
    return m["Al2O3"] / (m["Na2O"] + m["K2O"])


def classify(ox):
    if ank(ox) < 1.0:
        return "peralkaline"
    return "peraluminous" if acnk(ox) > 1.0 else "metaluminous"


def water_fraction(molar_mass, n_h2o=1.0):
    """mass fraction of H2O released by a hydrous mineral holding n_h2o per formula unit."""
    return n_h2o * M_H2O / molar_mass


def melt_fraction(x_hyd, w_hyd, c_melt):
    """water-limited melt fraction (mass): all the water of the hydrous mineral enters
    a melt that holds c_melt (mass fraction) of water."""
    return x_hyd * w_hyd / c_melt


def solubility_fit():
    """least-squares line through the 3-8 kbar points: slope (wt %/kbar), intercept."""
    pts = [(p, w) for p, w in AOQ if 3.0 <= p <= 8.0]
    s, i = np.polyfit([p for p, _ in pts], [w for _, w in pts], 1)
    return s, i


def paths():
    import ptpaths as pt
    out = {}
    for rock in (35e3, 70e3):
        _, path = pt.run(rock=rock)
        out[int(rock / 1e3)] = path
    return out


if __name__ == "__main__":
    write_table(__file__, ("P_kbar", "T_C"), WET, part="solidi")
    write_table(__file__, ("name", "Tmin", "Tmax", "Pmin", "Pmax"), BOXES, part="boxes")
    for k, path in paths().items():
        sel = path[::20]
        write_table(__file__, ("t_Myr", "T_C", "P_kbar"),
                    [tuple(round(float(x), 3) + 0.0 for x in r[:3]) for r in sel],
                    part="path%d" % k)
    write_table(__file__, ("P_kbar", "H2O_wt"), AOQ, part="water")
    s, i = solubility_fit()
    write_table(__file__, ("P_kbar", "H2O_wt"), [(p, round(i + s * p, 4)) for p in (3.0, 8.0)],
                part="waterfit")
    write_table(__file__, ("name", "ACNK", "ANK"),
                [(n, round(acnk(o), 4), round(ank(o), 4)) for n, o in ROCKS.items()], part="asi")

"""Far-from-equilibrium dissolution rates of silicate minerals against pH
(Year 3, water-rock interaction).

Parameters of Palandri and Kharaka (2004), USGS Open-File Report 2004-1068
(ledger pk04:rates): for each mechanism a rate constant at 25 C and pH 0,
log k (mol m-2 s-1), an activation energy E (kJ/mol) and a reaction order n
on a_H+ (negative for the base mechanism),
    r = sum_j k_j exp[-E_j/R (1/T - 1/298.15)] a_H^n_j      (Omega << 1).

  part curves   ph albite kfeldspar forsterite kaolinite    (log r at 25 C)
  part values   what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

R = 8.314462618e-3   # kJ mol-1 K-1
PARAMS = {  # mechanism: (log k, E, n)
    "albite": {"acid": (-10.16, 65.0, 0.457), "neutral": (-12.56, 69.8, 0.0),
               "base": (-15.60, 71.0, -0.572)},
    "kfeldspar": {"acid": (-10.06, 51.7, 0.500), "neutral": (-12.41, 38.0, 0.0),
                  "base": (-21.20, 94.1, -0.823)},
    "forsterite": {"acid": (-6.85, 67.2, 0.470), "neutral": (-10.64, 79.0, 0.0)},
    "kaolinite": {"acid": (-11.31, 65.9, 0.777), "neutral": (-13.18, 22.2, 0.0),
                  "base": (-17.05, 17.9, -0.472)},
}


def rate(mineral, ph, t_c=25.0, mechanism=None):
    T = t_c + 273.15
    tot = 0.0
    for mech, (lk, e, n) in PARAMS[mineral].items():
        if mechanism and mech != mechanism:
            continue
        tot += 10 ** lk * math.exp(-e / R * (1.0 / T - 1.0 / 298.15)) * 10 ** (-n * ph)
    return tot


def log_rate(mineral, ph, t_c=25.0):
    return math.log10(rate(mineral, ph, t_c))


def crossover(mineral, m1, m2):
    """pH at which mechanisms m1 and m2 contribute equally (25 C)."""
    l1, _, n1 = PARAMS[mineral][m1]
    l2, _, n2 = PARAMS[mineral][m2]
    return (l1 - l2) / (n1 - n2)


def main():
    rows = []
    for ph in np.arange(0.0, 14.0001, 0.1):
        ph = round(float(ph), 2)
        rows.append([ph] + [log_rate(m, ph) for m in ("albite", "kfeldspar", "forsterite",
                                                       "kaolinite")])
    write_table(__file__, ("ph", "albite", "kfeldspar", "forsterite", "kaolinite"), rows,
                part="curves")
    vals = [["albite_ph5", log_rate("albite", 5.0)], ["albite_ph7", log_rate("albite", 7.0)],
            ["forsterite_ph5", log_rate("forsterite", 5.0)],
            ["kfs_ph7", log_rate("kfeldspar", 7.0)],
            ["albite_acid_neutral_ph", crossover("albite", "acid", "neutral")],
            ["albite_neutral_base_ph", crossover("albite", "neutral", "base")],
            ["albite_ratio_25_10_ph7", rate("albite", 7.0) / rate("albite", 7.0, 10.0)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

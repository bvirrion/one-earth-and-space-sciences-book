"""The LR04 benthic d18O stack over the last 800 kyr, and the share of the last
glacial maximum signal due to ice volume (Year 3, stable isotopes).

Data: data/derived/lr04.csv (Lisiecki and Raymo 2005; ledger data:lr04). The
file continues after the stack with further blocks whose age starts again at
small values: only the first block (up to the first decrease of age) is read.

Ice volume (ledger white13c9:ice-volume): about 0.011 permil of ocean d18O per
metre of sea level, and a last-glacial sea-level fall of about 125 m, hence
about 1.4 permil. The rest of the glacial-interglacial change of benthic
d18O is a cooling of deep water.

  part stack    age_ka d18O        0-800 ka
  part values   what value         Holocene mean (0-5 ka), LGM maximum (15-25 ka), amplitude
"""
import csv
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(os.path.dirname(os.path.dirname(HERE)), "data", "derived")
PERMIL_PER_M = 0.011
SEA_LEVEL_FALL_M = 125.0


def stack():
    rows, prev = [], -1.0
    with open(os.path.join(DERIVED, "lr04.csv"), encoding="utf8") as f:
        for r in csv.DictReader(f):
            a = float(r["age_ka"])
            if a < prev:
                break
            rows.append((a, float(r["d18O_permil"])))
            prev = a
    return np.array(rows)


def lgm_amplitude(s=None):
    s = stack() if s is None else s
    hol = s[(s[:, 0] >= 0) & (s[:, 0] <= 5), 1].mean()
    lgm = s[(s[:, 0] >= 15) & (s[:, 0] <= 25), 1].max()
    return hol, lgm, lgm - hol


def main():
    s = stack()
    sel = s[s[:, 0] <= 800.0]
    write_table(__file__, ("age_ka", "d18O"), [list(r) for r in sel], part="stack")
    hol, lgm, amp = lgm_amplitude(s)
    ice = PERMIL_PER_M * SEA_LEVEL_FALL_M
    write_table(__file__, ("what", "value"), [
        ["holocene", hol], ["lgm", lgm], ["amplitude", amp], ["ice", ice],
        ["temperature_part", amp - ice]], part="values")


if __name__ == "__main__":
    main()

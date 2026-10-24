"""A magnetostratigraphic section of Kesta formation C matched to the polarity
time scale (Year 3, palaeomagnetism).

GPTS: normal-polarity intervals of Lourens et al. (2004), ledger iodp:gpts2004
(Book 3, read-only), 2.3-3.8 Ma: C2An.1n 2.581-3.032, C2An.2n 3.116-3.207,
C2An.3n 3.330-3.596; reversed otherwise.
The section (invented): accumulation 40 m/Myr from 3.70 Ma to 3.20 Ma, then
55 m/Myr to 2.40 Ma; boundary heights rounded to 0.1 m, as printed.

  part gpts      t pol         polarity step function (1 normal, 0 reversed), 2.3-3.8 Ma
  part section   h pol         the same in the section, height above the base (m)
  part ties      t h           reversal ages and their heights in the section
  part values    what value
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

NORMAL = [(2.581, 3.032), (3.116, 3.207), (3.330, 3.596)]
T_BASE, T_BREAK, T_TOP = 3.70, 3.20, 2.40
RATE_LOW, RATE_HIGH = 40.0, 55.0


def polarity(t):
    return 1 if any(a <= t < b for a, b in NORMAL) else 0


def height(t):
    if t >= T_BREAK:
        return RATE_LOW * (T_BASE - t)
    return RATE_LOW * (T_BASE - T_BREAK) + RATE_HIGH * (T_BREAK - t)


def reversals():
    return sorted([a for a, b in NORMAL] + [b for a, b in NORMAL], reverse=True)


def ties():
    return [(t, round(height(t), 1)) for t in reversals()]


def rates(tie_list):
    """Accumulation rate (m/Myr) between successive ties, oldest first."""
    out = []
    for (t1, h1), (t2, h2) in zip(tie_list[:-1], tie_list[1:]):
        out.append((t1, t2, (h2 - h1) / (t1 - t2)))
    return out


def fit_rate(tie_list):
    t = np.array([a for a, b in tie_list])
    h = np.array([b for a, b in tie_list])
    p = np.polyfit(t, h, 1)
    return -p[0]


if __name__ == "__main__":
    ts = np.round(np.arange(2.300, 3.8001, 0.001), 3)
    write_table(__file__, ("t", "pol"), [(t, polarity(t)) for t in ts], part="gpts")
    hs = np.round(np.arange(0.0, height(T_TOP) + 0.001, 0.1), 1)
    tl = ties()
    def pol_h(h):
        # polarity at height h from the printed (rounded) boundary heights
        hb = [b for a, b in tl]
        n = sum(1 for b in hb if b <= h)
        return 0 if n % 2 == 0 else 1
    write_table(__file__, ("h", "pol"), [(h, pol_h(h)) for h in hs], part="section")
    write_table(__file__, ("t", "h"), tl, part="ties")
    vals = [("top_m", round(height(T_TOP), 1))]
    for t1, t2, r in rates(tl):
        vals.append(("rate_%.3f_%.3f" % (t1, t2), r))
    lower = [x for x in tl if x[0] >= 3.2]
    upper = [x for x in tl if x[0] <= 3.207]
    vals += [("fit_all", fit_rate(tl)), ("fit_lower", fit_rate(lower)), ("fit_upper", fit_rate(upper))]
    write_table(__file__, ("what", "value"), vals, part="values")

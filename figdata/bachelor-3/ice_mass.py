"""Cumulative mass change of the Greenland and Antarctic ice sheets, 1992-2020
(Year 3, gravity-geodesy).

Data: data/derived/bachelor-3-imbie-{greenland,antarctica}.csv (ledger data:b5-imbie):
the IMBIE 2021 reconciled monthly series (altimetry, gravimetry, input-output),
cumulative mass change since 1992 and its one-sigma uncertainty, in Gt.
Trends are least-squares lines through the monthly cumulative values.

  part greenland, antarctica   year cum lo hi     every third month (Gt; lo, hi = cum
                                                  -/+ one sigma)
  part trends    sheet t0 t1 rate fit0 fit1       straight-line fits over 1992-2020 and
                                                  over the GRACE years 2002.25-2017.5
  part values    what value
"""
import csv
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
SHEETS = ("greenland", "antarctica")
WINDOWS = ((1992.0, 2021.0), (2002.25, 2017.5))


def read(sheet):
    path = os.path.join(ROOT, "data", "derived", "bachelor-3-imbie-%s.csv" % sheet)
    with open(path, newline="") as f:
        rows = [(float(r["year"]), float(r["cum_gt"]), float(r["cum_unc"]))
                for r in csv.DictReader(f)]
    return np.array(rows)


def trend(data, t0, t1):
    sel = (data[:, 0] >= t0) & (data[:, 0] < t1)
    p = np.polyfit(data[sel, 0], data[sel, 1], 1)
    return float(p[0]), float(p[1])


if __name__ == "__main__":
    trows, vals = [], []
    for s in SHEETS:
        d = read(s)
        rows = [(t, c, c - u, c + u) for k, (t, c, u) in enumerate(d) if k % 3 == 0 or k == len(d) - 1]
        write_table(__file__, ("year", "cum", "lo", "hi"), rows, part=s)
        for t0, t1 in WINDOWS:
            r, b = trend(d, t0, t1)
            t1e = min(t1, d[-1, 0])
            trows.append((s, t0, t1e, r, r * t0 + b, r * t1e + b))
            vals.append(("%s_rate_%d_%d" % (s, int(t0), int(t1)), round(r, 1)))
        vals.append(("%s_cum_end" % s, round(float(d[-1, 1]), 0)))
        vals.append(("%s_unc_end" % s, round(float(d[-1, 2]), 0)))
    write_table(__file__, ("sheet", "t0", "t1", "rate", "fit0", "fit1"), trows, part="trends")
    write_table(__file__, ("what", "value"), vals, part="values")

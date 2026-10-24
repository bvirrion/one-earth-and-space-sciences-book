"""Sea level over the last 800 kyr (Year 1, diagenesis-basins).

The sea level stack of Spratt and Lisiecki (2016): the first principal component of
seven sea-level reconstructions from marine sediment cores over 0-430 ka (short) and of
five over 0-798 ka (long), scaled on Holocene and Last Glacial Maximum estimates, every
1 kyr, in metres above present sea level, with a one-sigma bootstrap error (dataset
bachelor-1-sealevel-stack.csv, ledger data:b3-sealevel-stack, spratt:stack). The last
glacial minimum is compared with the -134 m of Lambeck et al. (2014; lambeck:lgm).

  part long     age sl lo hi        (0-798 ka, long PC1, +- one sigma)
  part short    age sl lo hi        (0-140 ka, short PC1, +- one sigma)
  part values   what value
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
DATA = os.path.join(ROOT, "data", "derived", "bachelor-1-sealevel-stack.csv")

LAMBECK_LGM = -134.0   # m, ice-volume equivalent sea level at 21 ka (lambeck:lgm)


def read():
    """[(age_ka, sl_short, sig_short, sl_long, sig_long)], None where missing."""
    rows = []
    with open(DATA, encoding="utf8") as f:
        for r in csv.DictReader(f):
            g = lambda k: float(r[k]) if r[k] != "" else None  # noqa: E731
            rows.append((int(r["age_ka"]), g("sl_short"), g("sig_short"),
                         g("sl_long"), g("sig_long")))
    return rows


def series(rows, which="long", tmax=None):
    """[(age, sl, sl - sigma, sl + sigma)] of one principal component."""
    i = 1 if which == "short" else 3
    return [(r[0], r[i], r[i] - r[i + 1], r[i] + r[i + 1]) for r in rows
            if r[i] is not None and (tmax is None or r[0] <= tmax)]


def extreme(rows, which, a, b, fn=min):
    """(age, sl, sigma) of the lowest (fn=min) or highest value between a and b ka."""
    i = 1 if which == "short" else 3
    sel = [(r[i], r[0], r[i + 1]) for r in rows if a <= r[0] <= b and r[i] is not None]
    v, age, sig = fn(sel)
    return age, v, sig


def mean_rate(rows, which, a, b):
    """Mean rate of rise (m per kyr) from b ka to a ka (a < b)."""
    i = 1 if which == "short" else 3
    d = {r[0]: r[i] for r in rows}
    return (d[a] - d[b]) / (b - a)


def fast_rises(rows, which="long", rise=100.0, window=20):
    """[(age of the low, rise)]: each local minimum (lowest within 15 kyr on either
    side) followed, within `window` kyr towards the present, by a rise above `rise` m."""
    i = 1 if which == "short" else 3
    d = {r[0]: r[i] for r in rows if r[i] is not None}
    out = []
    for a, v in sorted(d.items()):
        if all(d.get(a + k, 1e9) >= v and d.get(a - k, 1e9) >= v for k in range(1, 15)):
            top = max(d[a - k] for k in range(1, window + 1) if a - k in d)
            if top - v > rise:
                out.append((a, top - v))
    return out


if __name__ == "__main__":
    rows = read()
    write_table(__file__, ("age", "sl", "lo", "hi"), series(rows, "long"), part="long")
    write_table(__file__, ("age", "sl", "lo", "hi"), series(rows, "short", 140), part="short")
    lgm = extreme(rows, "short", 0, 40)
    e5 = extreme(rows, "short", 110, 135, max)
    vals = [("lgm_age", lgm[0]), ("lgm_sl", lgm[1]), ("lgm_sigma", lgm[2]),
            ("mis5e_age", e5[0]), ("mis5e_sl", e5[1]),
            ("long_min", extreme(rows, "long", 0, 798)[1]),
            ("long_max", extreme(rows, "long", 0, 798, max)[1]),
            ("rate_16_8", mean_rate(rows, "short", 8, 16)),
            ("fast_rises_100m_20kyr", len(fast_rises(rows)))]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

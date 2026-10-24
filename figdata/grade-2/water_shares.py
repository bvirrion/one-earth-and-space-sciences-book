"""All the water of the Earth as 100 buckets (grade 2, water-on-earth).

The shares are the USGS Water Science School table "Where is Earth's water?"
(after Shiklomanov 1993; ledger usgs-wss:water-table), in percent of all the
Earth's water. They are turned into 100 whole buckets by the largest-remainder
rule, so the buckets add up to exactly 100 and no share is rounded unfairly.

  table: bucket (1..100), col, row, kind (0 ocean, 1 ice, 2 groundwater)
  part counts: kind, name, buckets
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# percent of total water (USGS table); lakes, rivers, soil, air and living
# things together are well under one bucket and are told in the text.
SHARES = [("ocean", 96.54), ("ice", 1.74), ("groundwater", 1.69)]
SMALL = {"ground ice and permafrost": 0.022, "lakes": 0.013, "soil moisture": 0.001,
         "atmosphere": 0.001, "swamp water": 0.0008, "rivers": 0.0002, "living things": 0.0001}


def buckets(shares=SHARES, total=100):
    s = sum(v for _, v in shares)
    raw = [(n, v * total / s) for n, v in shares]
    base = {n: math.floor(x) for n, x in raw}
    left = total - sum(base.values())
    for n, x in sorted(raw, key=lambda t: t[1] - math.floor(t[1]), reverse=True)[:left]:
        base[n] += 1
    return base


def layout(counts):
    out, k = [], 0
    for kind, (n, _) in enumerate(SHARES):
        for _ in range(counts[n]):
            row, col = divmod(k, 10)
            out.append((k + 1, col, 9 - row, kind))
            k += 1
    return out


if __name__ == "__main__":
    b = buckets()
    write_table(__file__, ("bucket", "col", "row", "kind"), layout(b))
    write_table(__file__, ("kind", "name", "buckets"),
                [(i, n, b[n]) for i, (n, _) in enumerate(SHARES)], part="counts")
    print(b, "small:", sum(SMALL.values()))

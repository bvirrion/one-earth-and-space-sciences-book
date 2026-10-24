"""How old is the ocean floor, compared with the continents? (grade 12, continental crust)

The ocean-floor ages are the 1-degree cells of the Seton et al. (2020) grid already
used in grade 11 (figdata/grade-11/seafloor_age.py; ledger data:b2-seafloor-age).
Each cell is weighted by its area (cos latitude). The few old basins of the eastern
Mediterranean are left out, as in grade 11. The continental ages are not computed:
the oldest rock, 4.03 Gyr, and the oldest mineral grains, 4.4 Gyr, come from the
ledger (bowring99:acasta, wilde01:zircon).

  part hist     age_lo age_mid share       area share of the ocean floor in 10-Myr bins
  part cumul    age share_younger          share of the ocean floor younger than each age
  part numbers  key value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "grade-11"))
from _table import write_table  # noqa: E402
import seafloor_age as sa  # noqa: E402

BIN = 10.0
OLDEST_ROCK_MYR = 4030.0     # ledger bowring99:acasta (4.00-4.03 Ga)


def weighted_cells():
    import math
    return [(a, math.cos(math.radians(la))) for la, lo, a in sa.cells() if not sa.in_mediterranean(la, lo)]


def histogram(bin_myr=BIN, top=200.0):
    cs = weighted_cells()
    total = sum(w for _, w in cs)
    n = int(top / bin_myr)
    shares = [0.0] * n
    for a, w in cs:
        shares[min(int(a // bin_myr), n - 1)] += w / total
    return [(i * bin_myr, (i + 0.5) * bin_myr, s) for i, s in enumerate(shares)]


def share_younger(age):
    cs = weighted_cells()
    return sum(w for a, w in cs if a < age) / sum(w for _, w in cs)


def numbers():
    cs = weighted_cells()
    oldest = max(a for a, _ in cs)
    return {"oldest_open_myr": oldest, "share_younger_100": share_younger(100.0),
            "share_younger_150": share_younger(150.0),
            "rock_over_floor": OLDEST_ROCK_MYR / oldest}


if __name__ == "__main__":
    write_table(__file__, ("age_lo", "age_mid", "share"), histogram(), part="hist", digits=5)
    write_table(__file__, ("age", "share_younger"), [(a, share_younger(a)) for a in range(0, 201, 10)],
                part="cumul", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)

"""The layered rocks of the Varden Hills as one column (grade 7, sediments
and fossils).

The thicknesses come from the series' region model (figdata/shared/region.py,
imported, never copied): sandstone 120 m, limestone 180 m, shale 100 m, then
chalk. The region model gives the chalk no top: it has been worn away, and
its thickness left changes from place to place (it is thickest in the core of
the syncline). The column therefore draws only the lowest CHALK_DRAWN metres
of it, under a wavy top, and the text says so; no chalk thickness is quoted.

The fossils and marks given to each layer, and the piling-up rates, are
exercise data of this book (the region is invented): ripple marks and
footprints in the sandstone, corals and shells in the limestone, ammonites
in the shale.

  part unit-<name> : x y        (one closed polygon per layer, in metres above
                                 the base of the sandstone; the chalk's top and
                                 the older rocks' top are wavy)
  part ticks       : y          (a tick every 100 m)
  main table       : name base top thickness
  part rates       : name thickness_cm cm_per_years years   (problem, Part III)
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
import region as R  # noqa: E402

CHALK_DRAWN = 80.0            # drawing choice: the chalk goes on upward, its top worn away
BASEMENT_DEPTH = 60.0          # how much of the older rocks the drawing shows
# problem rates (exercise data): one centimetre of rock every N years
YEARS_PER_CM = {"sandstone": 20, "limestone": 100}


def layers(chalk=None):
    """[(name, base, top, thickness)] oldest first, in m above the base of the sandstone."""
    chalk = CHALK_DRAWN if chalk is None else chalk
    out, z = [], 0.0
    for n in ("sandstone", "limestone", "shale"):
        out.append((n, z, z + R.THICK[n], R.THICK[n]))
        z += R.THICK[n]
    out.append(("chalk", z, z + chalk, chalk))
    return out


def share(name, names=("sandstone", "limestone", "shale")):
    """Percentage of the named layer in the three complete layers."""
    return 100.0 * R.THICK[name] / sum(R.THICK[n] for n in names)


def years(name):
    """Years to pile up the layer at the problem's rate."""
    return R.THICK[name] * 100.0 * YEARS_PER_CM[name]


def _wavy(x0, x1, z, amp, n=40, phase=0.0):
    return [(x0 + (x1 - x0) * k / n, z + amp * math.sin(2 * math.pi * 2.5 * k / n + phase)) for k in range(n + 1)]


def polygons(chalk=None):
    """{name: closed polygon} for the drawing; the column is 1 unit wide."""
    out = {}
    lay = layers(chalk)
    for n, b, t, _ in lay[:-1]:
        out[n] = [(0, b), (1, b), (1, t), (0, t), (0, b)]
    n, b, t, _ = lay[-1]
    top = _wavy(1, 0, t - 6.0, 6.0, phase=0.8)            # eroded top
    out[n] = [(0, b), (1, b)] + top + [(0, b)]
    top = _wavy(1, 0, 0.0, 4.0, phase=0.0)               # the older rocks' worn top
    out["older"] = [(0, -BASEMENT_DEPTH), (1, -BASEMENT_DEPTH)] + top + [(0, -BASEMENT_DEPTH)]
    return out


if __name__ == "__main__":
    lay = layers()
    write_table(__file__, ("name", "base", "top", "thickness"), lay)
    for name, ring in polygons(lay[-1][3]).items():
        write_table(__file__, ("x", "y"), [(round(a, 3), round(b, 2)) for a, b in ring], part="unit-" + name)
    write_table(__file__, ("y",), [(y,) for y in range(0, int(lay[-2][2]) + 1, 100)], part="ticks")
    write_table(__file__, ("name", "thickness_cm", "years_per_cm", "years"),
                [(n, int(R.THICK[n] * 100), YEARS_PER_CM[n], int(years(n))) for n in ("sandstone", "limestone")],
                part="rates")

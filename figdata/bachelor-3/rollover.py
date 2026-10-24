"""A listric normal fault and its rollover by the constant-heave construction
(Year 3, extensional and strike-slip tectonics).

The fault, depth positive downward, is f(x) = D (1 - exp(-k x)) for x >= 0,
with k = tan(DIP0) / D so that it dips DIP0 at the surface and flattens into a
detachment at the depth D. Constant heave (vertical simple shear): every
vertical column of the hanging wall moves horizontally by the heave H and
drops by the fall of the fault beneath it, so that a bed at the depth z0
(z0 < D) ends at z0 + s(x), with s(x) = f(x) - f(x - H) for x >= H; the
columns between the fault and x = H are new space (the half-graben, filled by
growth sediments). The area below the original level of a bed, counted to
the fault, is H (D - z0): the depth-to-detachment relation.

  part fault     x z         the fault (km)
  part top       x z         the displaced top surface (rollover), from the fault
  part bed       x z         the displaced bed originally at Z_BED
  part values    what value
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

D = 5.0
DIP0 = 60.0
H = 2.0
Z_BED = 2.0
X_MAX = 24.0


def fault(x, d=D, dip0=DIP0):
    k = math.tan(math.radians(dip0)) / d
    return d * (1.0 - np.exp(-k * np.asarray(x, dtype=float)))


def fault_x(z, d=D, dip0=DIP0):
    """Abscissa at which the fault reaches the depth z < d."""
    k = math.tan(math.radians(dip0)) / d
    return -math.log(1.0 - z / d) / k


def displaced_bed(x, z0, h=H):
    """Depth of the bed first at z0 after the heave h; nan where the point is in
    the footwall or in the new space next to the fault."""
    x = np.asarray(x, dtype=float)
    out = np.full(x.shape, np.nan)
    ok = x >= h + fault_x(z0)
    out[ok] = z0 + fault(x[ok]) - fault(x[ok] - h)
    # the bed's cut-off on the fault: the column that started on the fault
    return out


def sag_area(z0, h=H, n=200001, x_max=200.0):
    """Area between the bed's original level and its displaced position, plus
    the new space between the fault and the moved hanging wall above the bed."""
    x0 = fault_x(z0) if z0 > 0 else 0.0
    xs = np.linspace(0.0, x_max, n)
    dx = xs[1] - xs[0]
    hw_edge = xs - h                       # original abscissa of the column now at x
    depth_after = np.where(hw_edge >= x0, z0 + fault(xs) - fault(np.maximum(hw_edge, 0.0)), np.nan)
    # where no hanging-wall bed is present yet, the space reaches the fault
    lower = np.where(np.isnan(depth_after), np.maximum(fault(xs), z0), depth_after)
    gap = np.clip(lower - z0, 0.0, None)
    gap[xs < x0] = 0.0
    return float(np.sum(gap) * dx)


if __name__ == "__main__":
    xs = np.linspace(0.0, X_MAX, 481)
    write_table(__file__, ("x", "z"), [(x, float(fault(x))) for x in xs], part="fault")
    top = displaced_bed(xs, 0.0)
    write_table(__file__, ("x", "z"), [(x, float(z)) for x, z in zip(xs, top) if z == z], part="top")
    bed = displaced_bed(xs, Z_BED)
    xb = H + fault_x(Z_BED)
    write_table(__file__, ("x", "z"), [(xb, float(Z_BED + fault(xb) - fault(xb - H)))] +
                [(x, float(z)) for x, z in zip(xs, bed) if z == z], part="bed")
    vals = [("sag_top", sag_area(0.0)), ("H_times_D", H * D),
            ("sag_bed", sag_area(Z_BED)), ("H_times_D_minus_z", H * (D - Z_BED)),
            ("max_drop_top", float(np.nanmax(top)))]
    write_table(__file__, ("what", "value"), vals, part="values")

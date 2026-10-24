"""Interseismic velocity across a locked strike-slip fault (Year 1, earthquake-source).

The model of Savage and Burford (ledger usgs:pp1515-thatcher): a vertical
strike-slip fault in an elastic half-space, locked from the surface to the depth D
and slipping steadily at the rate V below it. The surface velocity parallel to the
fault, at the distance x from it, is

    v(x) = (V / pi) arctan(x / D),

which tends to -V/2 and +V/2 far from the fault, the two plates moving at V
relative to each other. The curves use the slip rate of the San Andreas fault at
Wallace Creek, 34 mm/yr (ledger usgs:pp1515-wallace), and three locking depths.

  part profiles  x v5 v15 v25     velocity (mm/yr) against distance (km)
  part values    what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

V_SAF = 34.0          # mm/yr
DEPTHS = (5.0, 15.0, 25.0)


def velocity(x, V, D):
    """Fault-parallel surface velocity at the distance x (same units as D)."""
    return V / math.pi * math.atan2(x, D)


def strain_rate(x, V, D):
    """dv/dx: the engineering shear-strain rate of the surface (V in m/yr, x, D in m)."""
    return V / (math.pi * D) / (1.0 + (x / D) ** 2)


def locking_depth(x, v, V):
    """The locking depth that gives the velocity v at the distance x > 0 (0 < v < V/2)."""
    return x / math.tan(math.pi * v / V)


def main():
    xs = [i * 0.5 for i in range(-200, 201)]
    rows = [(x,) + tuple(velocity(x, V_SAF, D) for D in DEPTHS) for x in xs]
    write_table(__file__, ("x", "v5", "v15", "v25"), rows, part="profiles")
    values = [("V", V_SAF)]
    for D in DEPTHS:
        values.append(("v_at_D_%g" % D, velocity(D, V_SAF, D)))
        values.append(("strain_rate_0_D%g_per_yr" % D, strain_rate(0.0, V_SAF * 1e-3, D * 1e3)))
    write_table(__file__, ("what", "value"), values, part="values")


if __name__ == "__main__":
    main()

"""Pelagic sediments on a ridge flank (Year 1, chemical-biogenic-sediments).

The sea floor deepens with age by the depth--age law of the cooling half-space,
d = 2500 + 350 sqrt(t) (metres, t in Myr; Parsons and Sclater 1977, ledger
parsons:plate-model, valid to about 70 Myr; depth_age.halfspace). A site born at
the ridge above the carbonate compensation depth z_c receives calcareous ooze
until it sinks below z_c, at the age

    t_c = ((z_c - d_r) / C)^2,

and red clay afterwards. The script tabulates the flank profile against the
distance from the ridge for a half-spreading rate u (x = u t) and the crossing
ages for the compensation depths quoted in the text.

  part profile  t x_km depth         (every 0.5 Myr to 70 Myr, u = 25 mm/yr)
  part values   what value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _table import write_table  # noqa: E402
from depth_age import halfspace  # noqa: E402

D_R, C = 2500.0, 350.0
U_MM_YR = 25.0   # half-spreading rate of the figure (invented, mm/yr = km/Myr)


def crossing_age(z_c, d_r=D_R, c=C):
    """Age (Myr) at which the sea floor reaches the depth z_c (m)."""
    if z_c <= d_r:
        return 0.0
    return ((z_c - d_r) / c) ** 2


def distance_km(t_myr, u_mm_yr=U_MM_YR):
    """Distance (km) from the ridge of floor of age t at the half-rate u (mm/yr = km/Myr)."""
    return u_mm_yr * t_myr


def profile(tmax=70.0, step=0.5):
    n = int(round(tmax / step))
    return [(i * step, distance_km(i * step), halfspace(i * step)) for i in range(n + 1)]


if __name__ == "__main__":
    write_table(__file__, ("t", "x_km", "depth"), profile(), part="profile")
    vals = []
    for z in (4000.0, 4100.0, 4500.0, 5000.0, 5100.0):
        vals.append(("t_cross_%d" % z, crossing_age(z)))
        vals.append(("x_cross_%d" % z, distance_km(crossing_age(z))))
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

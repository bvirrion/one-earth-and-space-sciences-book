"""Activity diagram of the system K2O-Al2O3-SiO2-H2O at 25 C (Year 3,
water-rock interaction).

log K at 25 C from the USGS PHREEQC database phreeqc.dat (ledger
phreeqc:silicates), each written with Al+3, H4SiO4 and H+:
    gibbsite   Al(OH)3 + 3H+ = Al+3 + 3H2O                         8.11
    kaolinite  Al2Si2O5(OH)4 + 6H+ = 2Al+3 + 2H4SiO4 + H2O          7.435
    muscovite  KAl3Si3O10(OH)2 + 10H+ = K+ + 3Al+3 + 3H4SiO4       12.703
    K-feldspar KAlSi3O8 + 8H2O = K+ + Al(OH)4- + 3H4SiO4          -20.573
               with Al+3 + 4H2O = Al(OH)4- + 4H+                  -22.7
    quartz     SiO2 + 2H2O = H4SiO4                                -3.98
    amorphous silica                                                -2.71
With water at unit activity and aluminium conserved in the solids, a
mineral with k K, a Al and s Si sets, at equilibrium,
    log(a_Al / a_H^3) = [log K - k X - s Y] / a,
X = log(a_K+/a_H+), Y = log a_H4SiO4. The stable mineral is the one that
gives the lowest Al activity; a boundary is where two are equal (a
straight line in X, Y).

The water samples are invented.

  part lines    x y            boundary segments, blank lines between them
  part quartz   x y            quartz saturation
  part amorph   x y            amorphous silica saturation
  part samples  name x y
  part values   what value
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

LOGK_AL_OH4 = -22.7
MINERALS = {  # log K (to Al+3), k, a, s
    "gibbsite": (8.11, 0, 1, 0),
    "kaolinite": (7.435, 0, 2, 2),
    "muscovite": (12.703, 1, 3, 3),
    "kfeldspar": (-20.573 - LOGK_AL_OH4, 1, 1, 3),
}
LOGK_QUARTZ = -3.98
LOGK_AMORPH = -2.71
XLIM = (0.0, 10.0)
YLIM = (-6.0, -2.0)

# invented water samples: name, K mg/L, pH, SiO2 mg/L
SAMPLES = [
    ("tropical", 0.3, 5.5, 1.5),
    ("stream", 1.2, 5.8, 9.0),
    ("deep", 3.0, 8.2, 19.0),
]
M_K, M_SIO2 = 39.098, 60.084


def level(name, x, y):
    lk, k, a, s = MINERALS[name]
    return (lk - k * x - s * y) / a


def stable(x, y):
    return min(MINERALS, key=lambda n: level(n, x, y))


def boundary(m1, m2):
    """Coefficients (cx, cy, c0) of level(m1) - level(m2) = cx X + cy Y + c0 = 0."""
    l1, k1, a1, s1 = MINERALS[m1]
    l2, k2, a2, s2 = MINERALS[m2]
    return (-k1 / a1 + k2 / a2, -s1 / a1 + s2 / a2, l1 / a1 - l2 / a2)


def sample_xy(k_mgl, ph, sio2_mgl):
    return np.log10(k_mgl / 1000 / M_K) + ph, np.log10(sio2_mgl / 1000 / M_SIO2)


def traced_boundaries(n=4001):
    """Boundary points found on a fine grid, grouped by mineral pair, each
    pair returned as a straight segment between its extreme points."""
    xs = np.linspace(*XLIM, n)
    ys = np.linspace(*YLIM, n)
    segs = {}
    for m1 in MINERALS:
        for m2 in MINERALS:
            if m1 >= m2:
                continue
            cx, cy, c0 = boundary(m1, m2)
            pts = []
            if abs(cx) > 1e-12:
                for y in ys:
                    x = -(cy * y + c0) / cx
                    if XLIM[0] <= x <= XLIM[1]:
                        pts.append((x, y))
            else:
                y = -c0 / cy
                if YLIM[0] <= y <= YLIM[1]:
                    pts = [(x, y) for x in xs]
            keep = []
            for x, y in pts:
                lv = level(m1, x, y)
                if all(level(o, x, y) > lv + 1e-9 for o in MINERALS if o not in (m1, m2)):
                    keep.append((x, y))
            if len(keep) > 1:
                segs[(m1, m2)] = (keep[0], keep[-1])
    return segs


def main():
    rows = []
    for (m1, m2), (p, q) in sorted(traced_boundaries().items()):
        rows += [[p[0], p[1]], [q[0], q[1]], ["nan", "nan"]]
    write_table(__file__, ("x", "y"), rows, part="lines")
    write_table(__file__, ("x", "y"), [[XLIM[0], LOGK_QUARTZ], [XLIM[1], LOGK_QUARTZ]],
                part="quartz")
    write_table(__file__, ("x", "y"), [[XLIM[0], LOGK_AMORPH], [XLIM[1], LOGK_AMORPH]],
                part="amorph")
    write_table(__file__, ("name", "x", "y"),
                [[n] + [float(v) for v in sample_xy(k, ph, si)] for n, k, ph, si in SAMPLES],
                part="samples")
    vals = []
    for (m1, m2) in (("gibbsite", "kaolinite"), ("kaolinite", "muscovite"),
                     ("gibbsite", "muscovite"), ("kfeldspar", "muscovite"),
                     ("kaolinite", "kfeldspar")):
        cx, cy, c0 = boundary(m1, m2)
        vals.append(["%s_%s_cx" % (m1, m2), cx])
        vals.append(["%s_%s_cy" % (m1, m2), cy])
        vals.append(["%s_%s_c0" % (m1, m2), c0])
    vals.append(["logK_kfs_al3", MINERALS["kfeldspar"][0]])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

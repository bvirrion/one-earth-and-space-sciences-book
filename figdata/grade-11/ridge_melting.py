"""Where the rising mantle starts to melt beneath a ridge (grade 11, ocean-ridges).

Beneath a ridge the mantle rises without time to lose heat: its temperature follows
the adiabat T = Tp + 0.45 z (degC, z in km; katsura10:adiabat, Tp = 1300 degC as in
grade-11 geotherm_solidus, porter:lab). The dry peridotite solidus is Hirschmann's
(2000) fit T = a P^2 + b P + c (hirschmann:solidus), with the pressure P(z) the weight
of the rock above (PREM densities, data:prem). Rising, the rock cools by only 0.45
degC per km while its melting temperature drops by about 4 degC per km: it starts to
melt where the two curves cross, without being heated.

The model ignores the heat used up by melting (above the crossing, the rising rock
follows a less steep path): it gives the depth where melting begins, not how much melt.

  part curves   z solidus ad1300 ad1400      0-150 km
  part numbers  key value
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402
import geotherm_solidus as gsol  # noqa: E402
import prem_profiles  # noqa: E402

G_AD = gsol.G_AD                 # 0.45 degC/km
TP = 1300.0                      # degC, as in grade-11 geotherm_solidus
TP_HOT = 1400.0                  # a mantle 100 degC hotter (model choice)


def adiabat(z_km, tp=TP):
    return tp + G_AD * z_km


def solidus_at(z_km, rows=None):
    return gsol.t_solidus(gsol.pressure_gpa(z_km, rows))


def onset_depth(tp=TP, rows=None):
    """Depth (km) where the adiabat of potential temperature tp crosses the solidus
    (bisection between 5 and 250 km; below the crossing the rock is solid)."""
    rows = rows or prem_profiles.prem()
    lo, hi = 5.0, 250.0
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if adiabat(mid, tp) < solidus_at(mid, rows):
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def solidus_slope(z_km=50.0, rows=None):
    """degC per km of the solidus at depth z (finite difference)."""
    rows = rows or prem_profiles.prem()
    return (solidus_at(z_km + 1, rows) - solidus_at(z_km - 1, rows)) / 2.0


def numbers():
    rows = prem_profiles.prem()
    z1, z2 = onset_depth(TP, rows), onset_depth(TP_HOT, rows)
    return {"onset_1300_km": z1, "onset_1400_km": z2, "t_onset_1300": adiabat(z1),
            "solidus_slope_50km": solidus_slope(50.0, rows),
            "p_onset_1300_gpa": gsol.pressure_gpa(z1, rows), "solidus_surface": gsol.t_solidus(0.0)}


if __name__ == "__main__":
    rows = prem_profiles.prem()
    write_table(__file__, ("z", "solidus", "ad1300", "ad1400"),
                [(z, solidus_at(z, rows), adiabat(z), adiabat(z, TP_HOT)) for z in range(0, 151, 2)],
                part="curves", digits=6)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

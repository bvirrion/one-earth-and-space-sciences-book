"""How much does folding shorten a layer? (grade 12, mountain building)

A layer that folds by bending keeps its thickness and its length measured along the
layer (flexural folding; Tulane EENS 1110 notes, ledger tulane:fold-geometry). Its
original length L0 is therefore the length measured along the folded layer, and the
shortening is e = (L0 - L) / L0, with L the horizontal distance the layer spans today.

  chevron fold (straight limbs dipping at theta): L = L0 cos(theta), so e = 1 - cos(theta)
  sine-shaped fold y = A sin(2 pi x / lam): L0 is the arc length, found numerically

The Varden Hills cover (figdata/shared/region.py, imported, never edited) is folded
into a chevron anticline and syncline with limbs dipping 12 degrees: the base of the
sandstone along the east-west line y = 4 km is its profile here.

  part dip      theta e_pct           shortening of a chevron fold against its limb dip
  part sine     x y                   one wavelength and a half of a sine fold, A/lam = 0.25 (figure)
  part ratio    A_over_lam e_pct      shortening of a sine fold against its amplitude
  part varden   x_km z_m              base of the cover along y = 4 km (unfaulted)
  part numbers  key value

The fold axes on section A-B: the vertical axial planes x = AXIS_ANTI and x = AXIS_SYN
cross the section line where its x equals them, but on the hanging wall of the normal
fault the planes were carried by the slip (heave throw/tan(dip) toward the dip
azimuth), so the syncline, wholly on the hanging wall, crosses A-B farther along
(numbers section_anticline_km, section_syncline_km).
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

SINE_RATIO = 0.25          # amplitude over wavelength of the drawn sine fold


def chevron_shortening(theta_deg):
    return 1.0 - math.cos(math.radians(theta_deg))


def length_along(profile):
    """Length of a polyline [(x, y), ...] measured along it."""
    return sum(math.hypot(x1 - x0, y1 - y0) for (x0, y0), (x1, y1) in zip(profile, profile[1:]))


def shortening(profile):
    """(L0 - L) / L0 for a folded layer drawn as a polyline (L = horizontal span)."""
    L0 = length_along(profile)
    L = abs(profile[-1][0] - profile[0][0])
    return (L0 - L) / L0


def sine_profile(ratio, n_waves=1.0, n=2000, lam=1.0):
    A = ratio * lam
    xs = [n_waves * lam * i / n for i in range(n + 1)]
    return [(x, A * math.sin(2 * math.pi * x / lam)) for x in xs]


def varden_profile(y=4000.0, step=10.0):
    xs = [i * step for i in range(int(region.WIDTH / step) + 1)]
    return [(x, region.base_cover(x, y)) for x in xs]


def section_axis_s(x_axis, on_hanging_wall):
    """Distance along section A-B (km) where the vertical axial plane x = x_axis
    meets the section line, after the fault slip if the fold lies on the hanging wall."""
    (ax, ay), (bx, by) = region.SECTION_AB
    L = math.hypot(bx - ax, by - ay)
    if on_hanging_wall:
        a = math.radians(region.FAULT_DIP_AZ)
        heave = region.FAULT_THROW / math.tan(math.radians(region.FAULT_DIP))
        x_axis += math.sin(a) * heave
    return (x_axis - ax) / ((bx - ax) / L) / 1000.0


def numbers():
    n = {}
    n["section_anticline_km"] = section_axis_s(region.AXIS_ANTI, False)
    n["section_syncline_km"] = section_axis_s(region.AXIS_SYN, True)
    n["varden_dip"] = region.LIMB_DIP
    n["varden_e_pct"] = 100 * chevron_shortening(region.LIMB_DIP)
    n["varden_profile_e_pct"] = 100 * shortening(varden_profile())
    n["varden_L0_for_10km"] = 10.0 / math.cos(math.radians(region.LIMB_DIP))
    for d in (30, 45, 60):
        n["chevron_%d_e_pct" % d] = 100 * chevron_shortening(d)
    n["sine_025_e_pct"] = 100 * shortening(sine_profile(SINE_RATIO))
    n["sine_025_max_dip"] = math.degrees(math.atan(2 * math.pi * SINE_RATIO))
    return n


if __name__ == "__main__":
    write_table(__file__, ("theta", "e_pct"),
                [(t, 100 * chevron_shortening(t)) for t in range(0, 91)], part="dip", digits=5)
    write_table(__file__, ("x", "y"), sine_profile(SINE_RATIO, n_waves=1.5, n=150), part="sine", digits=5)
    write_table(__file__, ("A_over_lam", "e_pct"),
                [(r / 100, 100 * shortening(sine_profile(r / 100))) for r in range(0, 51)],
                part="ratio", digits=5)
    write_table(__file__, ("x_km", "z_m"),
                [(x / 1000, z) for x, z in varden_profile(step=100.0)], part="varden", digits=6)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)

"""Groundwater in the Varden Hills (grade 6, water-underground).

A north-south section across the river valley at x = 5.5 km, from the river
(y = 3.2 km) up the northern hillside (y = 6.0 km). The rocks come from the
series' region model (figdata/shared/region.py, imported, never copied): the
chalk of the hills lies on shale, which lies on limestone. The chalk is
porous and permeable; the shale is not, so the water held in the chalk
comes out as a spring where the base of the chalk meets the hillside.

The water table is drawn as a gentle copy of the ground ("subdued replica"):
z_wt = base of chalk + K * (ground - base of chalk), with K larger after the
rainy season than after the dry season. K is a modelling choice of this
book, not a measurement.

  part ground   : s_km z_m                    (ground profile)
  part unit-<n> : s_km z_m                    (rock polygons, rings separated by blank lines)
  part wet      : s_km z_m                    (water table after the rainy season)
  part dry      : s_km z_m                    (water table after the dry season)
  part points   : s_km z_m label              (river, spring)
    part wells    : name s_km z_top z_bottom    (two wells)
  part fresh    : idx label pct               (shares of the Earth's fresh water)
  main table    : the numbers quoted in the text
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
from _table import write_table  # noqa: E402
import region as R  # noqa: E402

X = 5500.0
Y0, Y1 = 3200.0, 6000.0
ZMIN, ZMAX = 0.0, 560.0
K_WET, K_DRY = 0.7, 0.6
# two farm wells on the slope: (name, y in m, depth in m)
WELLS = (("A", 4650.0, 100.0), ("B", 4900.0, 105.0))


def s_km(y):
    return (y - Y0) / 1000.0


def ground(y):
    return R.topo(X, y)


def chalk_base(y):
    return R.contact_elevation("chalk", X, y)


def spring_y(lo=3900.0, hi=4400.0):
    """Where the base of the chalk comes out on the valley side (bisection on
    ground - base, which is negative below the contact, positive above)."""
    f = lambda y: ground(y) - chalk_base(y)  # noqa: E731
    assert f(lo) < 0 < f(hi)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def water_table(y, k):
    """Elevation of the water table in the chalk (None where there is no chalk)."""
    if y < spring_y():
        return None
    b = chalk_base(y)
    return b + k * (ground(y) - b)


def well_state(name):
    """'always' if the bottom is below the dry-season water table, 'wet season
    only' if it is between the two, 'never' if it is above both."""
    _, y, depth = [w for w in WELLS if w[0] == name][0]
    bottom = ground(y) - depth
    if bottom < water_table(y, K_DRY):
        return "always"
    if bottom < water_table(y, K_WET):
        return "wet season only"
    return "never"


FRESH_LABELS = ("ice and permanent snow", "groundwater", "ground ice and permafrost", "lakes")


def fresh_shares():
    """[(label, percent of the Earth's fresh water)] from Book 1's ledger row
    wss:fresh-shares (USGS Water Science School table), re-read here so that
    the figure and the ledger cannot drift apart; "everything else" closes
    the total."""
    path = os.path.join(os.path.dirname(__file__), "..", "..", "sources", "ledger", "book1.md")
    for line in open(path, encoding="utf8"):
        if line.startswith("| wss:fresh-shares |"):
            vals = [float(v) for v in line.split("|")[3].split(";")]
            break
    rows = list(zip(FRESH_LABELS, vals))
    rows.append(("everything else", round(100.0 - sum(vals), 2)))
    return rows


def stored_days(length_m, width_m, thickness_m, yield_pct, use_m3_per_day):
    """The problem's named number: days of water drained from a block of
    saturated rock (volume x the share that drains out), at a daily use."""
    return length_m * width_m * thickness_m * yield_pct / 100.0 / use_m3_per_day


def volume_of_water(volume_m3, pct):
    return volume_m3 * pct / 100.0


if __name__ == "__main__":
    ys = [Y0 + 20.0 * i for i in range(int((Y1 - Y0) / 20.0) + 1)]
    write_table(__file__, ("s_km", "z_m"), [(s_km(y), round(ground(y), 1)) for y in ys], part="ground")
    a, b = (X, Y0), (X, Y1)
    ss, zs, codes, _ = R.section(a, b, zmin=ZMIN, zmax=ZMAX, ds=5.0, dz=2.0)
    polys = R.unit_polygons(codes, ss, zs, tol=1.0)
    for code, name, *_ in R.UNITS:
        rings = polys.get(code, [])
        rows = [r for ring in rings for r in ([()] + [(round(s / 1000, 4), round(z, 1)) for s, z in ring])][1:]
        write_table(__file__, ("s_km", "z_m"), rows, part="unit-" + name)
    ysp = spring_y()
    for part, k in (("wet", K_WET), ("dry", K_DRY)):
        pts = [(s_km(ysp), round(ground(ysp), 1))] + [
            (s_km(y), round(water_table(y, k), 1)) for y in ys if y > ysp]
        write_table(__file__, ("s_km", "z_m"), pts, part=part)
    write_table(__file__, ("s_km", "z_m", "label"),
                [(s_km(R.river_y(X)), round(R.river_z(X), 1), "river"),
                 (s_km(ysp), round(ground(ysp), 1), "spring")], part="points")
    write_table(__file__, ("name", "s_km", "z_top", "z_bottom", "wt_wet", "wt_dry"),
                [(n, s_km(y), round(ground(y), 1), round(ground(y) - d, 1),
                  round(water_table(y, K_WET), 1), round(water_table(y, K_DRY), 1)) for n, y, d in WELLS],
                                part="wells")
    half = 0.012                     # half-width of a well in the drawing (km)
    rings = []
    for n, y, d in WELLS:
        s, top, bot = s_km(y), round(ground(y), 1), round(ground(y) - d, 1)
        rings += ([()] if rings else []) + [(s - half, top), (s + half, top), (s + half, bot), (s - half, bot), (s - half, top)]
    write_table(__file__, ("s_km", "z_m"), rings, part="well-rects")
    write_table(__file__, ("s_km", "z_m", "label"),
                [(s_km(y), round(ground(y), 1), "well~" + n) for n, y, d in WELLS], part="well-labels")
    write_table(__file__, ("idx", "label", "pct"),
                [(i, "{%s}" % lab, p) for i, (lab, p) in enumerate(fresh_shares())], part="fresh")
    write_table(__file__, ("item", "value"),
                [("spring_y_km", ysp / 1000.0), ("spring_z_m", ground(ysp)),
                 ("river_z_m", R.river_z(X)), ("problem_days", stored_days(100, 50, 2, 18, 18))])

"""Fossils and palaeoenvironments (Year 2, palaeoenvironments): compaction of the Varden
cover and the rates at which its units accumulated.

  lithologies  Athy's law phi = phi0 exp(-z / lam) (recalled from the Year 1 volume) with the
               constants bundled in pyBacktrack (grain density, surface porosity, decay length):
               shale 2700 / 0.63 / 1960 m, sandstone 2650 / 0.49 / 3704 m, chalk 2710 / 0.70 /
               1408 m (Sclater and Christie 1980; Book 3 row pybacktrack:compaction) and
               limestone 2850 / 0.51 / 4545 m (Turer and Maynard 2003; row pybacktrack4:limestone).
  varden       the series' invented region (figdata/shared/region.py, read-only import): the
               thicknesses of the cover units, 120 / 180 / 100 m. The ages given to the Jurassic
               units in this chapter are invented for the region but sit on the real time scale:
               limestone = the Toarcian (184.2-174.7 Ma), shale = Aalenian to Callovian
               (174.7-161.5 Ma), ICS chart 2026-06 (row ics4:jurassic-stages).
  rates        the accumulation rate of a layer from its present thickness h, its present mean
               porosity phi and the porosity phi0 it had when laid down:
               r = h (1 - phi) / ((1 - phi0) dt), the grains being conserved.

  part poro     z_m  shale  sandstone  chalk  limestone      (porosity by Athy's law)
  part ratio    z_m  shale  sandstone  chalk  limestone      (thin-layer restoration factor)
  part log      unit  base_m  top_m                          (the Varden column, chalk cut)
  part numbers  key value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

# grain density (kg/m3), surface porosity, decay length (m)
LITH = {"shale": (2700.0, 0.63, 1960.0), "sandstone": (2650.0, 0.49, 3704.0),
        "chalk": (2710.0, 0.70, 1408.0), "limestone": (2850.0, 0.51, 4545.0)}
ORDER = ("shale", "sandstone", "chalk", "limestone")

# ICS 2026-06 stage boundaries (Ma)
STAGE = {"Toarcian": (184.2, 174.7), "Aalenian": (174.7, 170.9), "Bajocian": (170.9, 168.2),
         "Bathonian": (168.2, 165.3), "Callovian": (165.3, 161.5)}

THICK = dict(region.THICK)          # sandstone 120, limestone 180, shale 100 (m)
LIMESTONE_SPAN = (STAGE["Toarcian"][0], STAGE["Toarcian"][1])
SHALE_SPAN = (STAGE["Aalenian"][0], STAGE["Callovian"][1])

# the Varden-2 well of the Year 3 volume, in the syncline: ground 441 m; the chalk is 766 m
# thick there, so the shale lies between 766 and 866 m and the limestone between 866 and 1046 m
SYNCLINE = (7500.0, 7000.0)
PHI_LIMESTONE_NOW = 0.08            # density porosity of the limestone in that well (invented)
CHALK_SHOWN = 60.0                  # chalk drawn in the log above the shale (top eroded)


def porosity(lith, z):
    _, p0, lam = LITH[lith]
    return p0 * math.exp(-z / lam)


def solid(lith, z1, z2):
    """Thickness of grains per unit area between the depths z1 < z2 (Year 1 volume)."""
    _, p0, lam = LITH[lith]
    return (z2 - z1) - p0 * lam * (math.exp(-z1 / lam) - math.exp(-z2 / lam))


def restored(lith, z1, z2, top=0.0):
    """Thickness of the layer z1-z2 moved up (or down) so that its top lies at `top`."""
    s = solid(lith, z1, z2)
    lo, hi = top, top + 10.0 * (z2 - z1) + 100.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if solid(lith, top, mid) < s:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi) - top


def ratio(lith, z):
    """Restoration factor of a thin layer at the depth z brought to the surface."""
    return (1.0 - porosity(lith, z)) / (1.0 - LITH[lith][1])


def rate(h, phi, phi0, dt):
    """Accumulation rate (m per Myr) of a layer of present thickness h and mean porosity phi,
    laid down with the porosity phi0 over dt Myr."""
    return h * (1.0 - phi) / ((1.0 - phi0) * dt)


def syncline_depths():
    """Depths (m below the ground) of the cover contacts in the syncline."""
    x, y = SYNCLINE
    g = region.topo(x, y)
    return {n: g - region.contact_elevation(n, x, y) for n in ("sandstone", "limestone",
                                                                "shale", "chalk")}, g


def numbers():
    d = {}
    dep, g = syncline_depths()
    d["ground_syncline"] = g
    d["top_shale_depth"] = dep["chalk"]
    d["top_limestone_depth"] = dep["shale"]
    d["base_limestone_depth"] = dep["limestone"]
    d["base_sandstone_depth"] = dep["sandstone"]
    # the shale example: Athy porosity at its present depth, restored to the surface
    z1, z2 = dep["chalk"], dep["shale"]
    d["shale_solid"] = solid("shale", z1, z2)
    d["shale_mean_phi"] = 1.0 - d["shale_solid"] / (z2 - z1)
    d["shale_restored"] = restored("shale", z1, z2)
    dt_sh = SHALE_SPAN[0] - SHALE_SPAN[1]
    d["shale_dt"] = dt_sh
    d["shale_rate_now"] = THICK["shale"] / dt_sh
    d["shale_rate_restored"] = d["shale_restored"] / dt_sh
    d["shale_rate_solid"] = d["shale_solid"] / dt_sh
    # the limestone (weekend problem): measured porosity, depositional porosity 0.51
    dt_ls = LIMESTONE_SPAN[0] - LIMESTONE_SPAN[1]
    d["ls_dt"] = dt_ls
    d["ls_rate_now"] = THICK["limestone"] / dt_ls
    d["ls_restored"] = THICK["limestone"] * (1 - PHI_LIMESTONE_NOW) / (1 - LITH["limestone"][1])
    d["ls_rate_restored"] = rate(THICK["limestone"], PHI_LIMESTONE_NOW, LITH["limestone"][1], dt_ls)
    d["ls_rate_solid"] = THICK["limestone"] * (1 - PHI_LIMESTONE_NOW) / dt_ls
    # Athy's law for limestone at the present mid-depth of the limestone, for comparison
    zm = 0.5 * (dep["shale"] + dep["limestone"])
    d["ls_mid_depth"] = zm
    d["ls_athy_phi_mid"] = porosity("limestone", zm)
    d["ls_athy_mean_phi"] = 1.0 - solid("limestone", dep["shale"], dep["limestone"]) / (
        dep["limestone"] - dep["shale"])
    for lith in ORDER:
        d["phi3000_" + lith] = porosity(lith, 3000.0)
        d["ratio1000_" + lith] = ratio(lith, 1000.0)
    return d


if __name__ == "__main__":
    zs = [float(z) for z in range(0, 3001, 50)]
    write_table(__file__, ("z_m",) + ORDER,
                [(z,) + tuple(round(porosity(l, z), 4) for l in ORDER) for z in zs], part="poro")
    write_table(__file__, ("z_m",) + ORDER,
                [(z,) + tuple(round(ratio(l, z), 4) for l in ORDER) for z in zs], part="ratio")
    rows, base = [], 0.0
    for unit in ("sandstone", "limestone", "shale"):
        rows.append((unit, base, base + THICK[unit]))
        base += THICK[unit]
    rows.append(("chalk", base, base + CHALK_SHOWN))
    write_table(__file__, ("unit", "base_m", "top_m"), rows, part="log")
    write_table(__file__, ("key", "value"),
                [(k, round(v, 4)) for k, v in sorted(numbers().items())], part="numbers")

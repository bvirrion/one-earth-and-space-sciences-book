"""Synthetic wireline logs of the well Varden-2 through the cover of the
Varden Hills (Year 3, facies models). Invented: the well, its site, the log
values and the channel architecture of the sandstone; the unit boundaries
come from the series' region model (figdata/shared/region.py).

Site (7500, 7000) m in the syncline, footwall of the fault: the column is
chalk, shale, limestone, sandstone, then the schist basement. Logs every
DZ metres of measured depth:
  GR    gamma ray (API): low in clean sand and carbonate, high in shale;
  RHOB  bulk density (g/cm3) = rho_ma - phi (rho_ma - rho_f);
  DT    sonic transit time (us/ft), time-average: phi DT_f + (1 - phi) DT_ma.
Matrix values: quartz 2.65, calcite 2.71 g/cm3; fluid 1.0 g/cm3; transit
times 52.6 (sandstone), 47.6 (limestone) and 189 us/ft (brine), the fast
ends of the ledger's table (ledger keys:density-porosity, keys:sonic).

The Triassic sandstone is a stack of fluvial channel fills, each a
sharp-based sand (GR 30) passing up through a fining interval (GR rising
linearly to 105) into floodplain mud (GR 105). Net sand: GR below the cutoff
GR_CUT.

  part logs     depth gr rhob dt unit     the whole well, every 0.5 m
  part sand     depth gr rhob dt          the sandstone, every 0.1 m
  part tops     unit top                  measured depth of each unit top
  part values   what value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

SITE = (7500.0, 7000.0)
TD = 1200.0                   # total depth, m below ground
RHO = {"quartz": 2.65, "calcite": 2.71, "fluid": 1.0}
DT_MA = {"sandstone": 52.6, "limestone": 47.6}
DT_F = 189.0
GR_CUT = 60.0
GR_SAND, GR_MUD = 30.0, 105.0
PHI_SAND, PHI_LIME = 0.20, 0.08
# channel fills, base to top: (thickness m, sand fraction, fining fraction)
CHANNELS = [(14, 0.60, 0.25), (9, 0.45, 0.30), (12, 0.55, 0.25), (7, 0.30, 0.40),
            (16, 0.65, 0.20), (10, 0.40, 0.30), (13, 0.55, 0.25), (8, 0.35, 0.35),
            (11, 0.50, 0.25), (12, 0.45, 0.30), (8, 0.30, 0.35)]


def tops():
    """Measured depth (m below ground) of the top of each unit."""
    x, y = SITE
    g = region.topo(x, y)
    out = {"chalk": 0.0}
    for name in ("shale", "limestone", "sandstone"):
        above = {"shale": "chalk", "limestone": "shale", "sandstone": "limestone"}[name]
        out[name] = g - region.contact_elevation(above, x, y)
    out["schist"] = g - region.contact_elevation("sandstone", x, y)
    return out


def unit_at(depth, t=None):
    t = t or tops()
    name = "chalk"
    for n in ("shale", "limestone", "sandstone", "schist"):
        if depth >= t[n]:
            name = n
    return name


def density(phi, matrix):
    return RHO[matrix] - phi * (RHO[matrix] - RHO["fluid"])


def porosity(rhob, matrix):
    return (RHO[matrix] - rhob) / (RHO[matrix] - RHO["fluid"])


def transit(phi, matrix):
    return phi * DT_F + (1 - phi) * DT_MA[matrix]


def sand_gr(height):
    """GR at a height (m) above the base of the sandstone."""
    h0 = 0.0
    for thick, fs, ff in CHANNELS:
        if height < h0 + thick or (thick, fs, ff) == CHANNELS[-1]:
            u = (height - h0) / thick
            if u < fs:
                return GR_SAND
            if u < fs + ff:
                return GR_SAND + (GR_MUD - GR_SAND) * (u - fs) / ff
            return GR_MUD
        h0 += thick
    return GR_MUD


def logs_at(depth, t=None):
    t = t or tops()
    n = unit_at(depth, t)
    if n == "chalk":
        phi = 0.40 - 0.20 * depth / t["shale"]          # compaction with depth
        return 12.0, density(phi, "calcite"), phi * DT_F + (1 - phi) * DT_MA["limestone"], n
    if n == "shale":
        return 110.0, 2.45, 100.0, n
    if n == "limestone":
        return 18.0, density(PHI_LIME, "calcite"), transit(PHI_LIME, "limestone"), n
    if n == "sandstone":
        h = t["schist"] - depth
        gr = sand_gr(h)
        f = (gr - GR_SAND) / (GR_MUD - GR_SAND)          # 0 sand, 1 mud
        phi = PHI_SAND * (1 - f) + 0.10 * f
        rhob = density(PHI_SAND, "quartz") * (1 - f) + 2.50 * f
        dt = transit(PHI_SAND, "sandstone") * (1 - f) + 95.0 * f
        return gr, rhob, dt, n
    return 85.0, 2.75, 50.0, n


def net_sand(dz=0.01):
    t = tops()
    zs = np.arange(t["sandstone"] + dz / 2, t["schist"], dz)
    sand = [logs_at(z, t)[0] < GR_CUT for z in zs]
    return float(np.sum(sand) * dz), t["schist"] - t["sandstone"]


def main():
    t = tops()
    code = {"chalk": 6, "shale": 5, "limestone": 4, "sandstone": 3, "schist": 1}
    rows = []
    for z in np.arange(0.0, TD + 1e-9, 0.5):
        gr, rb, dt, n = logs_at(z, t)
        rows.append([z, gr, rb, dt, code[n]])
    write_table(__file__, ("depth", "gr", "rhob", "dt", "unit"), rows, part="logs")
    rows = []
    for z in np.arange(math.floor(t["sandstone"]) - 5, math.ceil(t["schist"]) + 5 + 1e-9, 0.1):
        gr, rb, dt, n = logs_at(z, t)
        rows.append([z, gr, rb, dt])
    write_table(__file__, ("depth", "gr", "rhob", "dt"), rows, part="sand")
    write_table(__file__, ("unit", "top"), [[k, v] for k, v in t.items()], part="tops")
    net, gross = net_sand()
    write_table(__file__, ("what", "value"),
                [["net_sand_m", net], ["gross_m", gross], ["ntg", net / gross]], part="values")


if __name__ == "__main__":
    main()

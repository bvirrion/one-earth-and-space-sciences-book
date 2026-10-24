"""The Varden seismic model (Year 3, exploration-seismology): the layered
column beneath two points of section A-B of the Varden Hills, with P velocities
and densities chosen inside the ranges of the ledger row mavko:velocities
(chalk 2300-2600 m/s, saturated shales 1100-2500, limestones 3500-6000,
porous sandstones 2000-3500, gneiss 4400-5200 for the schist basement;
densities likewise).

Shared by synthetic_seismogram.py, cmp_nmo.py and refraction_dip.py. The
layer depths come from figdata/shared/region.py (imported, never edited);
contact_elevation() returns nan in the fault gap, so every call is checked.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "shared"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import region as R  # noqa: E402

# model properties (m/s, g/cm3), each inside the ledger range
PROPS = {
    "chalk": (2500.0, 2.00),
    "shale": (2300.0, 2.30),
    "limestone": (4500.0, 2.60),
    "sandstone": (3000.0, 2.30),
    "schist": (5000.0, 2.65),
}
ORDER = ("chalk", "shale", "limestone", "sandstone", "schist")
S_SYNCLINE = 7480.0      # m along A-B: the CMP on the syncline axis (CMP S)
S_REFR = (300.0, 1500.0)  # the refraction spread on the west limb
DATUM_REFR = 440.0        # level ground assumed over the spread (m)


def point(s):
    (ax, ay), (bx, by) = R.SECTION_AB
    L = math.hypot(bx - ax, by - ay)
    return ax + (bx - ax) * s / L, ay + (by - ay) * s / L


def contact(name, s):
    z = R.contact_elevation(name, *point(s))
    if not math.isfinite(z):
        raise ValueError("contact %s cut out by the fault at s = %g" % (name, s))
    return z


def column(s=S_SYNCLINE):
    """Layers below the ground at s: [(name, thickness m, v, rho)], basement last
    with thickness None; and the ground elevation."""
    g = R.topo(*point(s))
    bases = {n: contact(n, s) for n in ("chalk", "shale", "limestone", "sandstone")}
    tops = [g, bases["chalk"], bases["shale"], bases["limestone"], bases["sandstone"]]
    out = []
    for k, name in enumerate(ORDER[:-1]):
        out.append((name, tops[k] - tops[k + 1]) + PROPS[name])
    out.append(("schist", None) + PROPS["schist"])
    return out, g


def impedances(col):
    return [v * rho for name, h, v, rho in col]


def reflection_coefficients(col):
    z = impedances(col)
    return [(z[k + 1] - z[k]) / (z[k + 1] + z[k]) for k in range(len(z) - 1)]


def t0s(col):
    """Two-way vertical times (s) to the base of each layer."""
    t, out = 0.0, []
    for name, h, v, rho in col[:-1]:
        t += 2.0 * h / v
        out.append(t)
    return out

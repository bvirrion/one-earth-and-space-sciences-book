"""Two-layer models of the terrestrial planets from mean density and moment of inertia
(Year 3, planetary interiors).

A planet of radius R: a core of radius xR and uniform density rho_c inside a mantle of
uniform density rho_m (the two-layer proposition of the Year 1 volume):

    rho_bar = rho_m + (rho_c - rho_m) x^3,
    C       = (2/5) (rho_m + (rho_c - rho_m) x^5) / rho_bar,

so that, for an assumed mantle density rho_m,

    x^2   = ((5/2) C rho_bar - rho_m) / (rho_bar - rho_m),
    rho_c = rho_m + (rho_bar - rho_m) / x^3.

Two measured numbers, three unknowns: each planet gives a one-parameter family of
solutions, drawn as a curve of relative core radius x against core density rho_c as
rho_m runs over its possible values. The measured core radius picks one point.

Data: mean densities of the NASA planetary fact sheet (planet:*.density); moment-of-
inertia factors of the NASA fact sheets (nasa:mercury, nasa:moon, nasa:mars) and PREM
(earth:MoI); radii (nasa:*). Core radii: Earth 6371 - 2891 = 3480 km (PREM, data:prem),
Mars 1830 km (jpl:insight-interior), Moon 240 + 90 = 330 km (nasa:moon-core), Mercury
about 2000 km (half of a core 4000 km wide, agu:mercury-core).

  part curve-<body>  rho_m rho_c x     kg/m3, kg/m3, -  (rho_c <= 16000)
  part points        body x rho_c rho_m  at the measured core radius
  part values        what value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

# name: (mean density kg/m3, C, radius km, measured core radius km)
BODIES = {
    "Earth": (5514.0, 0.3308, 6371.0, 3480.0),
    "Mars": (3934.0, 0.366, 3389.5, 1830.0),
    "Moon": (3340.0, 0.394, 1737.4, 330.0),
    "Mercury": (5429.0, 0.35, 2439.7, 2000.0),
}
RHO_C_MAX = 16000.0


def mean_density(x, rho_c, rho_m):
    return rho_m + (rho_c - rho_m) * x ** 3


def moi(x, rho_c, rho_m):
    return 0.4 * (rho_m + (rho_c - rho_m) * x ** 5) / mean_density(x, rho_c, rho_m)


def solve(rho_bar, c, rho_m):
    """(x, rho_c) for an assumed mantle density, or None when no core fits."""
    x2 = (2.5 * c * rho_bar - rho_m) / (rho_bar - rho_m)
    if not 0.0 < x2 < 1.0:
        return None
    x = math.sqrt(x2)
    return x, rho_m + (rho_bar - rho_m) / x ** 3


def mantle_for_core(rho_bar, c, x):
    """The mantle density that makes the core radius x (inverse of solve)."""
    x2 = x * x
    return (2.5 * c * rho_bar - x2 * rho_bar) / (1.0 - x2)


def curve(name, n=400):
    """Sampled in the core radius x, so that the steep end near a small core is resolved."""
    rho_bar, c, _, _ = BODIES[name]
    rows = []
    for i in range(n + 1):
        x = 0.05 + 0.94 * i / n
        rho_m = mantle_for_core(rho_bar, c, x)
        if rho_m < 2500.0:
            continue
        s = solve(rho_bar, c, rho_m)
        if s and s[1] <= RHO_C_MAX:
            rows.append((rho_m, s[1], s[0]))
    rows.sort(key=lambda r: r[0])
    return rows


def main():
    pts, vals = [], []
    for name, (rho_bar, c, r, rcore) in BODIES.items():
        write_table(__file__, ("rho_m", "rho_c", "x"), curve(name), part="curve-" + name)
        x = rcore / r
        rho_m = mantle_for_core(rho_bar, c, x)
        rho_c = solve(rho_bar, c, rho_m)[1]
        pts.append((name, x, rho_c, rho_m))
        vals += [[name + "_x", x], [name + "_rho_m", rho_m], [name + "_rho_c", rho_c]]
    write_table(__file__, ("body", "x", "rho_c", "rho_m"), pts, part="points")
    # Mars with a mantle of 3500 kg/m3 (the problem)
    xm, rcm = solve(3934.0, 0.366, 3500.0)
    vals += [["Mars3500_x", xm], ["Mars3500_rc_km", xm * 3389.5], ["Mars3500_rho_c", rcm]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

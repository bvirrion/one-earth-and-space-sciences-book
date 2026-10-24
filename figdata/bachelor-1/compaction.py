"""Compaction and decompaction of sediments (Year 1, diagenesis-basins).

Porosity. Athy's law phi(z) = phi0 exp(-z/lam), an empirical fit to porosities measured
in wells, with the surface porosity phi0, the decay length lam and the grain density of
each lithology from Sclater and Christie (1980) as tabulated in pyBacktrack (ledger
pybacktrack:compaction): shale 0.63 / 1960 m / 2700 kg m-3; sand 0.49 / 3704 m / 2650;
shaly sand 0.56 / 2564 m / 2680; chalk 0.70 / 1408 m / 2710.

Solid thickness. A layer between the depths z1 < z2 contains, per unit area, the
volume of grains
    s(z1, z2) = (z2 - z1) - phi0 lam (exp(-z1/lam) - exp(-z2/lam)),
the integral of 1 - phi(z). Compaction expels water and keeps the grains: moved to a
new top z1', the layer takes the bottom z2' with s(z1', z2') = s(z1, z2), solved by
Newton's method (ds/dz2 = 1 - phi(z2) > 0, so the root is unique).

  part curves     z  phi_sand phi_shale phi_chalk                 (0 to 5000 m)
  part demo       state solid pore                                (a shale layer)
  part values     what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# lithology: (surface porosity, decay length m, grain density kg m-3)
LITHOLOGIES = {
    "shale": (0.63, 1960.0, 2700.0),
    "sandstone": (0.49, 3704.0, 2650.0),
    "shaly sandstone": (0.56, 2564.0, 2680.0),
    "chalk": (0.70, 1408.0, 2710.0),
}


def porosity(z, lith):
    phi0, lam, _ = LITHOLOGIES[lith]
    return phi0 * math.exp(-z / lam)


def solid_thickness(z1, z2, lith):
    """Thickness of grains (m of solid per m2) in the layer between z1 and z2."""
    phi0, lam, _ = LITHOLOGIES[lith]
    return (z2 - z1) - phi0 * lam * (math.exp(-z1 / lam) - math.exp(-z2 / lam))


def mean_porosity(z1, z2, lith):
    return 1.0 - solid_thickness(z1, z2, lith) / (z2 - z1)


def move_layer(z1, z2, lith, new_top, tol=1e-9):
    """Bottom depth of the layer z1-z2 moved to the top new_top, solid kept."""
    s = solid_thickness(z1, z2, lith)
    b = new_top + (z2 - z1)          # a first guess: the same thickness
    for _ in range(100):
        f = solid_thickness(new_top, b, lith) - s
        b -= f / (1.0 - porosity(b, lith))
        if abs(f) < tol:
            return b
    raise RuntimeError("no convergence")


def decompacted_thickness(z1, z2, lith):
    """Thickness of the layer z1-z2 brought back to the surface."""
    return move_layer(z1, z2, lith, 0.0)


def bulk_density(z1, z2, lith, rho_w=1030.0):
    """Mean density of the water-saturated layer (kg m-3)."""
    phi = mean_porosity(z1, z2, lith)
    return phi * rho_w + (1.0 - phi) * LITHOLOGIES[lith][2]


def loading_factor(rho_m, rho_w, rho_s):
    """Sediment thickness per metre of water-loaded subsidence, for a basin kept full
    to sea level in local isostasy (the proposition of the chapter)."""
    return (rho_m - rho_w) / (rho_m - rho_s)


# the example of the chapter and of the figure: 500 m of shale between 3000 and 3500 m
DEMO = ("shale", 3000.0, 3500.0)


if __name__ == "__main__":
    write_table(__file__, ("z", "phi_sand", "phi_shale", "phi_chalk"),
                [(z, porosity(z, "sandstone"), porosity(z, "shale"), porosity(z, "chalk"))
                 for z in range(0, 5001, 50)], part="curves")
    lith, z1, z2 = DEMO
    s = solid_thickness(z1, z2, lith)
    t0 = decompacted_thickness(z1, z2, lith)
    write_table(__file__, ("state", "solid", "pore"),
                [("buried", s, (z2 - z1) - s), ("surface", s, t0 - s)], part="demo")
    vals = [("demo_solid", s), ("demo_surface_thickness", t0),
            ("demo_mean_phi_buried", mean_porosity(z1, z2, lith)),
            ("demo_mean_phi_surface", mean_porosity(0.0, t0, lith)),
            ("phi_shale_3000", porosity(3000.0, "shale")),
            ("phi_sand_3000", porosity(3000.0, "sandstone")),
            ("phi_chalk_3000", porosity(3000.0, "chalk")),
            ("loading_marine", loading_factor(3300.0, 1030.0, 2300.0)),
            ("loading_air", loading_factor(3300.0, 0.0, 2300.0))]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

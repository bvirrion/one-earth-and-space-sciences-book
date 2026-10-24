"""The layered Earth from PREM (Year 1, layered-earth): velocities and density against
depth, and the functionals computed from the density alone -- enclosed mass, gravity,
pressure, moment of inertia -- plus an Adams-Williamson integration and the shell
masses of the weekend problem.

Data: data/derived/prem.csv (shared dataset, ledger data:prem): PREM, Dziewonski and
Anderson (1981), isotropic, 1 s, as tabulated in ObsPy's TauP file, with the ocean
replaced by crust. Within each region the tabulated values are joined by straight
lines (the published model is a set of polynomials; at the 100-km spacing of the table
the difference in the integrals is below 0.1 %). G from the ledger (const:G).

  part profiles   depth vp vs rho        the table (discontinuities appear twice)
  part functionals depth r g P m         gravity (m/s2), pressure (GPa), enclosed mass
                                         (fraction of the total) every 10 km of radius
  part adams      depth rho_prem rho_aw  lower mantle and outer core: density integrated
                                         downward with the Adams-Williamson equation from
                                         the top of each region, against PREM
  part values     what value             totals, boundary values and the problem's shells
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
PREM = os.path.join(ROOT, "data", "derived", "prem.csv")

G = 6.67430e-11            # const:G
R_EARTH = 6371.0           # km, PREM and earth:Rmean
R_CMB = 3480.0             # km (depth 2891 km)
R_ICB = 1221.5             # km (depth 5149.5 km)
R_660 = 5701.0             # km (PREM's 670-km discontinuity, depth 670 km)
R_LM_TOP = 5600.0          # km (depth 771 km): below the steep gradient under 670 km
STEP = 1.0                 # km, integration step


def table():
    """PREM rows (r_km, vp, vs, rho_g_cm3, region) by increasing radius; each
    discontinuity appears twice (lower side first)."""
    rows = []
    with open(PREM, encoding="utf8") as f:
        for r in csv.DictReader(f):
            rows.append((R_EARTH - float(r["depth_km"]), float(r["vp_km_s"]),
                         float(r["vs_km_s"]), float(r["rho_g_cm3"]), r["region"]))
    return rows[::-1]


_T = None


def _tab():
    global _T
    if _T is None:
        _T = table()
    return _T


def _segment(r, below):
    """The table segment containing radius r; at a discontinuity, the side below
    (below=True) or above."""
    t = _tab()
    for a, b in zip(t, t[1:]):
        if b[0] <= a[0]:
            continue
        if a[0] < r < b[0] or (r == a[0] and not below) or (r == b[0] and below):
            return a, b
    raise ValueError(r)


def _interp(r, k, below=False):
    a, b = _segment(r, below)
    w = (r - a[0]) / (b[0] - a[0])
    return a[k] + w * (b[k] - a[k])


def rho(r, below=False):
    """Density (kg/m3) at radius r (km)."""
    return 1000.0 * _interp(r, 3, below)


def vp(r, below=False):
    return _interp(r, 1, below)


def vs(r, below=False):
    return _interp(r, 2, below)


def seismic_parameter(r, below=False):
    """Phi = vP^2 - 4/3 vS^2 = K/rho, in m2/s2."""
    return 1e6 * (vp(r, below) ** 2 - 4.0 / 3.0 * vs(r, below) ** 2)


def _grid():
    """Mid-point radii (km) and step (km) of the integration cells, by increasing r."""
    n = int(round(R_EARTH / STEP))
    return [(i + 0.5) * STEP for i in range(n)], STEP


_F = None


def functionals():
    """Lists over the cell edges r_k = k*STEP (k = 0..n): r (km), enclosed mass m (kg),
    g (m/s2), P (Pa); and the moment of inertia I (kg m2)."""
    global _F
    if _F is not None:
        return _F
    mids, h = _grid()
    dr = h * 1e3
    m, inert = [0.0], 0.0
    for rm in mids:
        rr = rm * 1e3
        d = rho(rm)
        m.append(m[-1] + 4.0 * math.pi * rr ** 2 * d * dr)
        inert += 8.0 / 3.0 * math.pi * rr ** 4 * d * dr
    r = [k * h for k in range(len(m))]
    g = [0.0] + [G * mk / (rk * 1e3) ** 2 for mk, rk in zip(m[1:], r[1:])]
    p = [0.0] * len(r)
    for k in range(len(r) - 2, -1, -1):      # dP/dr = -rho g, from the surface inward
        gm = 0.5 * (g[k] + g[k + 1])
        p[k] = p[k + 1] + rho(mids[k]) * gm * dr
    _F = (r, m, g, p, inert)
    return _F


def _at(r_km):
    r, m, g, p, _ = functionals()
    k = int(round(r_km / STEP))
    if abs(r[k] - r_km) > 1e-9:          # half-kilometre radii: mean of the two edges
        k0 = int(math.floor(r_km / STEP))
        return tuple(0.5 * (x[k0] + x[k0 + 1]) for x in (m, g, p))
    return m[k], g[k], p[k]


def total_mass():
    return functionals()[1][-1]


def moment_factor():
    r, m, g, p, inert = functionals()
    return inert / (m[-1] * (R_EARTH * 1e3) ** 2)


def mass_within(r_km):
    return _at(r_km)[0]


def gravity(r_km):
    return _at(r_km)[1]


def pressure(r_km):
    return _at(r_km)[2]


def shell(r1, r2):
    """Volume (m3), mass (kg) and mean density (kg/m3) of the shell r1 < r < r2 (km)."""
    vol = 4.0 / 3.0 * math.pi * ((r2 * 1e3) ** 3 - (r1 * 1e3) ** 3)
    mass = mass_within(r2) - mass_within(r1)
    return vol, mass, mass / vol


def adams_williamson(r_top, r_bot, step=1.0):
    """Integrate d rho/dr = -rho g / Phi downward from r_top (PREM density just below
    r_top) to r_bot, with PREM's g and Phi. Returns [(r, rho_prem, rho_aw)]."""
    out = []
    r = r_top
    d = rho(r_top, below=True)
    out.append((r, d, d))
    while r - step >= r_bot - 1e-9:
        rm = r - 0.5 * step
        # midpoint rule: d rho = rho g / Phi * dr (going down, r decreases)
        k1 = d * gravity_cont(rm) / seismic_parameter(rm)
        d = d + k1 * step * 1e3
        r -= step
        out.append((r, rho(r, below=False), d))
    return out


def gravity_cont(r_km):
    """g at any radius by linear interpolation between integration edges."""
    r, m, g, p, _ = functionals()
    k0 = min(int(math.floor(r_km / STEP)), len(r) - 2)
    w = (r_km - r[k0]) / STEP
    return g[k0] + w * (g[k0 + 1] - g[k0])


# The weekend problem's four shells and its rounded mean densities.
SHELLS = (("upper mantle and crust", R_660, R_EARTH), ("lower mantle", R_CMB, R_660),
          ("outer core", R_ICB, R_CMB), ("inner core", 0.0, R_ICB))


def two_layer(rho_mantle, rho_core, r_core=R_CMB):
    """Mass (kg) and I/MR^2 of a two-layer Earth: uniform core and uniform mantle."""
    a, c = R_EARTH * 1e3, r_core * 1e3
    mc = 4.0 / 3.0 * math.pi * c ** 3 * rho_core
    mm = 4.0 / 3.0 * math.pi * (a ** 3 - c ** 3) * rho_mantle
    i = 8.0 / 15.0 * math.pi * (rho_core * c ** 5 + rho_mantle * (a ** 5 - c ** 5))
    return mc + mm, i / ((mc + mm) * a ** 2)


if __name__ == "__main__":
    rows = [(R_EARTH - r, a, b, c) for r, a, b, c, _ in _tab()][::-1]
    write_table(__file__, ("depth", "vp", "vs", "rho"), rows, part="profiles", digits=7)
    r, m, g, p, _ = functionals()
    M = m[-1]
    fun = [(R_EARTH - r[k], r[k], g[k], p[k] / 1e9, m[k] / M) for k in range(0, len(r), 10)]
    write_table(__file__, ("depth", "r", "g", "P", "m"), fun[::-1], part="functionals", digits=6)
    ad = []
    for top, bot in ((R_LM_TOP, R_CMB), (R_CMB, R_ICB)):
        for rr, dp, da in adams_williamson(top, bot)[::10]:
            ad.append((R_EARTH - rr, dp / 1000.0, da / 1000.0))
        ad.append(("nan", "nan", "nan"))
    write_table(__file__, ("depth", "rho_prem", "rho_aw"), ad[:-1], part="adams", digits=6)
    vals = [("mass", M), ("moment_factor", moment_factor()),
            ("P_centre_GPa", pressure(0.0) / 1e9), ("P_icb_GPa", pressure(R_ICB) / 1e9),
            ("P_cmb_GPa", pressure(R_CMB) / 1e9), ("P_660_GPa", pressure(R_660) / 1e9),
            ("g_surface", gravity(R_EARTH)), ("g_cmb", gravity(R_CMB)), ("g_icb", gravity(R_ICB)),
            ("core_fraction", mass_within(R_CMB) / M), ("inner_core_fraction", mass_within(R_ICB) / M)]
    for name, r1, r2 in SHELLS:
        v, mm, d = shell(r1, r2)
        key = name.replace(" ", "_")
        vals += [(key + "_volume", v), (key + "_mass", mm), (key + "_density", d)]
    write_table(__file__, ("what", "value"), vals, part="values", digits=7)

"""Sedimentary basins compared (Year 2, basins-compared): the stretching model, compaction and
backstripping of an invented well.

  stretching  McKenzie's (1978) uniform stretching model with the parameters of the paper as
              restated by Sheplev and Reverdatto (1998, Table 1: a = 125 km, T1 = 1333 degC,
              kappa = 0.008 cm2/s, rho_m = 3330, rho_c = 2800 kg/m3) and by the pyBacktrack
              code (alpha = 3.28e-5 /K; sea water 1030 kg/m3): ledger rows
              sheplev98:parameters, pybacktrack:rifting. Syn-rift (initial) subsidence from the
              isostatic balance of the stretched column; post-rift (thermal) subsidence from the
              first term of the Fourier series of the cooling plate, with the time constant
              tau = a^2 / (pi^2 kappa). `thermal_series` sums the full series and
              `thermal_fd` solves the heat equation by finite differences, for the tests.
  compaction  Athy's law phi = phi0 exp(-z / c) with the lithology constants of Sclater and
              Christie (1980) as bundled in pyBacktrack (Book 3 row pybacktrack:compaction):
              sand 2650 / 0.49 / 3704 m, shale 2700 / 0.63 / 1960 m, chalk 2710 / 0.70 /
              1408 m, shaly sand 2680 / 0.56 / 2564 m (grain density, surface porosity, decay
              length).
  well        an INVENTED well of four units (bottom to top: syn-rift sand 165-150 Ma, shale
              150-100 Ma, chalk 100-60 Ma, shaly sand 60-0 Ma), with invented palaeo water
              depths. Its present depths were designed (calc/ch16design.py in the Book 4 scratch)
              by forward modelling a stretching factor 1.5 of a 35 km crust, then rounded to
              10 m: backstripping the rounded well gives back a factor close to, not exactly, 1.5.

  part curves     t_Myr  b1.2  b1.5  b2  b4           (tectonic subsidence, m, water-loaded)
  part stages     age_Ma  S_m  rho  Wd_m  total_m  Y_m (backstripped well)
  part fit        age_Ma  Y_m                          (best-fit model from the initial subsidence)
  part numbers    key value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

A = 125e3            # lithosphere thickness, m
ALPHA = 3.28e-5      # thermal expansion, 1/K
T1 = 1333.0          # temperature of the asthenosphere, degC
KAPPA = 8e-7         # thermal diffusivity, m2/s
RHO_M, RHO_C, RHO_W = 3330.0, 2800.0, 1030.0
TC = 35e3            # crust before stretching, m
MYR = 3.156e13       # s

LITH = {"sand": (2650.0, 0.49, 3704.0), "shale": (2700.0, 0.63, 1960.0),
        "chalk": (2710.0, 0.70, 1408.0), "shaly sand": (2680.0, 0.56, 2564.0)}

# the invented well: (lithology, age of base, age of top, present top, present base, palaeo
# water depth at the age of its top), bottom unit first
WELL = [("sand", 165.0, 150.0, 4420.0, 6030.0, 200.0),
        ("shale", 150.0, 100.0, 3310.0, 4420.0, 300.0),
        ("chalk", 100.0, 60.0, 1700.0, 3310.0, 150.0),
        ("shaly sand", 60.0, 0.0, 0.0, 1700.0, 100.0)]
RIFT_START, RIFT_END = 165.0, 150.0


# --- stretching model -------------------------------------------------------------------

def tau_myr(a=A, kappa=KAPPA):
    return a * a / (math.pi ** 2 * kappa) / MYR


def syn_rift_max(tc=TC, rho_fill=RHO_W):
    """Initial subsidence for beta -> infinity (m): Si = syn_rift_max * (1 - 1/beta)."""
    num = (RHO_M - RHO_C) * (tc / A) * (1 - ALPHA * T1 * tc / (2 * A)) - ALPHA * T1 * RHO_M / 2
    return A * num / (RHO_M * (1 - ALPHA * T1) - rho_fill)


def syn_rift(beta, tc=TC, rho_fill=RHO_W):
    return syn_rift_max(tc, rho_fill) * (1 - 1 / beta)


def e0(rho_fill=RHO_W):
    return 4 * A * RHO_M * ALPHA * T1 / (math.pi ** 2 * (RHO_M - rho_fill))


def thermal(beta, t_myr, rho_fill=RHO_W):
    """Post-rift subsidence t_myr after the end of stretching, first term of the series (m)."""
    if t_myr <= 0:
        return 0.0
    return e0(rho_fill) * beta / math.pi * math.sin(math.pi / beta) * (1 - math.exp(-t_myr / tau_myr()))


def thermal_final(beta, rho_fill=RHO_W):
    return e0(rho_fill) * beta / math.pi * math.sin(math.pi / beta)


def tectonic(beta, t_myr, tc=TC):
    """Water-loaded subsidence t_myr after instantaneous stretching (m)."""
    return syn_rift(beta, tc) + thermal(beta, t_myr)


def beta_from_initial(si, tc=TC):
    return 1.0 / (1.0 - si / syn_rift_max(tc))


def _initial_excess(beta, z):
    """Temperature just after stretching minus the final linear profile (degC)."""
    t0 = T1 * beta * z / A if z < A / beta else T1
    return t0 - T1 * z / A


def thermal_series(beta, t_myr, nterms=401, nquad=4000):
    """Full Fourier series of the cooling plate (all terms), for the tests (m)."""
    tau = tau_myr()
    total = 0.0
    for n in range(1, nterms + 1):
        # b_n = (2/a) int_0^a excess(z) sin(n pi z / a) dz, by the midpoint rule
        h = A / nquad
        bn = 0.0
        for i in range(nquad):
            z = (i + 0.5) * h
            bn += _initial_excess(beta, z) * math.sin(n * math.pi * z / A)
        bn *= 2.0 / A * h
        integral = bn * A / (n * math.pi) * (1 - math.cos(n * math.pi))
        total += integral * (1 - math.exp(-n * n * t_myr / tau))
    return ALPHA * RHO_M / (RHO_M - RHO_W) * total


def thermal_fd(beta, t_myr, nz=125, dt_myr=0.01):
    """Explicit finite differences of the heat equation in the plate (T = 0 at the top, T1 at
    the base), subsidence from the heat lost (m); for the tests."""
    dz = A / nz
    dt = dt_myr * MYR
    r = KAPPA * dt / dz ** 2
    assert r < 0.5
    T = [T1 * beta * (i * dz) / A if i * dz < A / beta else T1 for i in range(nz + 1)]
    T[0], T[-1] = 0.0, T1
    heat0 = sum(T)
    for _ in range(int(round(t_myr / dt_myr))):
        T = [T[0]] + [T[i] + r * (T[i + 1] - 2 * T[i] + T[i - 1]) for i in range(1, nz)] + [T[-1]]
    lost = (heat0 - sum(T)) * dz
    return ALPHA * RHO_M / (RHO_M - RHO_W) * lost


# --- compaction and backstripping ---------------------------------------------------------

def solid_thickness(z1, z2, phi0, c):
    return (z2 - z1) - phi0 * c * (math.exp(-z1 / c) - math.exp(-z2 / c))


def decompacted_base(z1, ts, phi0, c, tol=1e-6):
    """Base of a layer of solid thickness ts whose top is moved to depth z1 (fixed point)."""
    z2 = z1 + ts
    for _ in range(500):
        new = z1 + ts + phi0 * c * (math.exp(-z1 / c) - math.exp(-z2 / c))
        if abs(new - z2) < tol:
            return new
        z2 = new
    return z2


def layer_mass(z1, z2, lith):
    rho_g, phi0, c = LITH[lith]
    ts = solid_thickness(z1, z2, phi0, c)
    return rho_g * ts + RHO_W * ((z2 - z1) - ts)


def airy_backstrip(s, rho_s, wd, dsl=0.0):
    """Tectonic (water-loaded) subsidence from a fill of thickness s and mean density rho_s
    under water depth wd, sea level dsl above today's (m)."""
    return s * (RHO_M - rho_s) / (RHO_M - RHO_W) + wd - dsl * RHO_M / (RHO_M - RHO_W)


def stage(k, well=WELL):
    """Backstrip the well at the age of the top of unit k (0 = bottom unit): units 0..k are
    decompacted with unit k at the surface. Returns (age, S, mean density, Wd, total, Y)."""
    units = well[: k + 1][::-1]               # top first
    z = 0.0
    mass = 0.0
    for lith, _b, _t, top, base, _wd in units:
        rho_g, phi0, c = LITH[lith]
        ts = solid_thickness(top, base, phi0, c)
        z2 = decompacted_base(z, ts, phi0, c)
        mass += rho_g * ts + RHO_W * (z2 - z - ts)
        z = z2
    rho = mass / z
    wd = well[k][5]
    return well[k][2], z, rho, wd, z + wd, airy_backstrip(z, rho, wd)


def stages(well=WELL):
    return [stage(k, well) for k in range(len(well))]


def fitted_beta(well=WELL):
    return beta_from_initial(stage(0, well)[5])


def numbers():
    st = stages()
    b = fitted_beta()
    d = {"tau_Myr": round(tau_myr(), 2), "Si_max_m": round(syn_rift_max(), 1),
         "E0_m": round(e0(), 1), "beta_fit": round(b, 3)}
    for age, s, rho, wd, tot, y in st:
        tag = "%d" % age
        d["S_%s" % tag] = round(s, 1)
        d["rho_%s" % tag] = round(rho, 1)
        d["Y_%s" % tag] = round(y, 1)
        d["model_%s" % tag] = round(tectonic(b, RIFT_END - age), 1)
    for beta in (1.2, 1.5, 2.0, 4.0):
        d["Si_b%g" % beta] = round(syn_rift(beta), 1)
        d["final_b%g" % beta] = round(syn_rift(beta) + thermal_final(beta), 1)
    return d


if __name__ == "__main__":
    ts_ = [0.5 * i for i in range(0, 401)]                 # 0 to 200 Myr after stretching
    write_table(__file__, ("t_Myr", "b1.2", "b1.5", "b2", "b4"),
                [(t,) + tuple(round(tectonic(b, t), 1) for b in (1.2, 1.5, 2.0, 4.0))
                 for t in ts_], part="curves")
    rows = [(RIFT_START, 0.0, 0.0, 0.0, 0.0, 0.0)]
    rows += [tuple(round(x, 1) for x in r) for r in stages()]
    write_table(__file__, ("age_Ma", "S_m", "rho", "Wd_m", "total_m", "Y_m"), rows, part="stages")
    b = fitted_beta()
    ages = [150.0 - 1.0 * i for i in range(0, 151)]
    fit = [(RIFT_START, 0.0)] + [(a, round(tectonic(b, RIFT_END - a), 1)) for a in ages]
    write_table(__file__, ("age_Ma", "Y_m"), fit, part="fit")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

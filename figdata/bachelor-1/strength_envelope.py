"""Strength envelopes of the lithosphere (Year 1, stress-strain-rheology).

Brittle part. Frictional sliding on the best-oriented fault obeys Byerlee's law
(ledger byerlee:1975: tau = 0.85 sigma_n below 200 MPa, tau = 50 MPa + 0.6 sigma_n above,
in effective stresses). With a lithostatic vertical stress rho g z and a hydrostatic pore
pressure rho_w g z, the vertical effective stress is S = sigma_v - rho_w g z, i.e.
rho g z (1 - lambda) with lambda = rho_w / rho in a uniform layer. Under the ocean the
sea-floor is the reference: the water column adds the same pressure to the rock and to
its pores, and drops out of the effective stresses. A Mohr circle of centre c and radius r is tangent to the line
tau = S0 + mu sigma when r = (S0 + mu c) / sqrt(1 + mu^2). Hence
  normal faulting  (sigma_1 vertical, sigma_1' = S fixed):  r = (S0 + mu S) / (k + mu)
  thrust faulting  (sigma_3 vertical, sigma_3' = S fixed):  r = (S0 + mu S) / (k - mu)
with k = sqrt(1 + mu^2), and the differential stress is 2 r. Byerlee's envelope is the
lower of its two lines, so the circle first touches whichever gives the smaller r.
For S0 = 0 the slopes are 2 mu rho g (1 - lambda) / (k +- mu) (tested).

Ductile part. Dislocation creep at the strain rate e = 1e-15 /s:
  sigma_1 - sigma_3 = (e / A)^(1/n) exp((E + P V) / (n R T))      (MPa)
with wet quartzite (Gleason and Tullis 1995: n 4, E 223 kJ/mol, A 1.1e-4 MPa^-n s^-1)
for the continental crust and dry olivine (Hirth and Kohlstedt 2003: n 3.5, E 530
kJ/mol, A 1e5 MPa^-n s^-1, V 18e-6 m3/mol) for the mantle (ledger lopez:flow-laws);
R from CODATA (ledger codata:R).

Temperatures from figdata/bachelor-1/geotherms.py (chapter 10): the continental
geotherm with q_m = 30 mW/m2 (surface 55 mW/m2), Moho at 35 km (ledger prem:moho-average), and
the oceanic geotherm of 60-Myr-old lithosphere, olivine from the sea floor down (the
7-km crust is ignored). Densities 2700 (crust) and 3300 kg/m3 (mantle), sea water
1000; lithostatic pressure integrated from the surface.

  part continental  depth thrust normal ductile strength     depth km, stresses MPa
  part oceanic      depth thrust normal ductile strength
  part values       what value
  part continental-outline, oceanic-outline   x depth: closed outline of the
                    strength, compression (thrust) positive, extension (normal) negative
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _table import write_table  # noqa: E402
import geotherms as gt  # noqa: E402

G = 9.81
RHO_C, RHO_M, RHO_W = 2700.0, 3300.0, 1000.0
MOHO = 35e3                    # m
R_GAS = 8.314462618            # J/mol/K
RATE = 1e-15                   # 1/s
QM = 30e-3                     # W/m2, continental heat flow from below
OCEAN_AGE = 60.0               # Myr

BYERLEE = ((0.0, 0.85), (50.0, 0.6))     # (S0 MPa, mu)

QUARTZ_WET = dict(n=4.0, E=223e3, A=1.1e-4, V=0.0)          # Gleason and Tullis 1995
OLIVINE_DRY = dict(n=3.5, E=530e3, A=1e5, V=18e-6)          # Hirth and Kohlstedt 2003


def byerlee_tau(sn):
    """Shear stress (MPa) to slide on a surface under the effective normal stress sn."""
    return min(s0 + mu * sn for s0, mu in BYERLEE)


def brittle_diff(s_eff, regime):
    """Differential stress (MPa) at failure, vertical effective stress s_eff (MPa)."""
    best = None
    for s0, mu in BYERLEE:
        k = math.sqrt(1.0 + mu * mu)
        r = (s0 + mu * s_eff) / (k + mu if regime == "normal" else k - mu)
        best = r if best is None else min(best, r)
    return 2.0 * best


def creep_diff(t_c, p_pa, law, rate=RATE):
    """Differential stress (MPa) for dislocation creep at t_c (degC) and pressure p_pa."""
    t = t_c + 273.15
    return (rate / law["A"]) ** (1.0 / law["n"]) * math.exp(
        (law["E"] + p_pa * law["V"]) / (law["n"] * R_GAS * t))


def column(kind, zmax=80e3, dz=250.0):
    """Rows (depth km, thrust, normal, ductile, strength) for 'continental' or 'oceanic'."""
    rows, p, z = [], 0.0, 0.0
    while z <= zmax + 1e-6:
        if kind == "continental":
            rho = RHO_C if z <= MOHO else RHO_M
            t = gt.t_continental(z, QM)
            law = QUARTZ_WET if z <= MOHO else OLIVINE_DRY
        else:
            rho = RHO_M
            t = gt.t_oceanic(z, OCEAN_AGE)
            law = OLIVINE_DRY
        s_eff = (p - RHO_W * G * z) * 1e-6          # hydrostatic pore pressure
        th, no = brittle_diff(s_eff, "thrust"), brittle_diff(s_eff, "normal")
        du = creep_diff(t, p, law) if z > 0 else float("inf")
        rows.append((z / 1e3, th, no, du, min(th, du)))
        p += rho * G * dz
        z += dz
    return rows


def transition(rows, col=1, start_km=0.0):
    """First depth (km) below start_km where the brittle curve (col 1 thrust, 2 normal)
    exceeds the ductile one, by linear interpolation, and the stress there."""
    for a, b in zip(rows, rows[1:]):
        if a[0] < start_km:
            continue
        fa, fb = a[col] - a[3], b[col] - b[3]
        if fa <= 0.0 < fb:
            w = -fa / (fb - fa)
            return a[0] + w * (b[0] - a[0]), a[col] + w * (b[col] - a[col])
    return None, None


def analysis():
    cont, ocean = column("continental"), column("oceanic")
    vals = {}
    for name, rows in (("cont", cont), ("ocean", ocean)):
        for col, reg in ((1, "thrust"), (2, "normal")):
            z, s = transition(rows, col)
            vals[f"{name}_bdt_{reg}_km"] = z
            vals[f"{name}_bdt_{reg}_MPa"] = s
    # the second, mantle transition under the continent (the Moho row itself is crust)
    for col, reg in ((1, "thrust"), (2, "normal")):
        z, st = transition(cont, col, start_km=MOHO / 1e3 + 0.1)
        vals[f"cont_mantle_bdt_{reg}_km"] = z
        vals[f"cont_mantle_bdt_{reg}_MPa"] = st
    # brittle slopes in the crust, MPa per km (mu = 0.85, hydrostatic pore pressure)
    sv = RHO_C * G * 1e3 * (1 - RHO_W / RHO_C) * 1e-6
    vals["slope_thrust_MPa_km"] = brittle_diff(sv, "thrust")
    vals["slope_normal_MPa_km"] = brittle_diff(sv, "normal")
    vals["slope_strike_MPa_km"] = 2.0 * 0.85 * sv / math.sqrt(1 + 0.85 ** 2)
    vals["T_cont_bdt_thrust"] = gt.t_continental(vals["cont_bdt_thrust_km"] * 1e3, QM)
    vals["T_ocean_bdt_thrust"] = gt.t_oceanic(vals["ocean_bdt_thrust_km"] * 1e3, OCEAN_AGE)
    vals["T_moho"] = gt.t_continental(MOHO, QM)
    pm = (RHO_C * MOHO) * G
    vals["quartz_moho_MPa"] = creep_diff(vals["T_moho"], pm, QUARTZ_WET)
    vals["olivine_moho_MPa"] = creep_diff(vals["T_moho"], pm, OLIVINE_DRY)
    return cont, ocean, vals


if __name__ == "__main__":
    cont, ocean, vals = analysis()
    cap = 2500.0
    fmt = lambda rows: [(d, min(t, cap), min(n, cap), min(u, cap), min(s, cap)) for d, t, n, u, s in rows]  # noqa: E731
    head = ("depth", "thrust", "normal", "ductile", "strength")
    write_table(__file__, head, fmt(cont), part="continental")
    write_table(__file__, head, fmt(ocean), part="oceanic")
    write_table(__file__, ("what", "value"), sorted(vals.items()), part="values")
    for name, rows in (("continental", cont), ("oceanic", ocean)):
        # closed outline of the strength: compression (thrust) to the right, extension
        # (normal faulting) to the left as negative stresses
        out = [(min(r[4], cap), r[0]) for r in rows]
        out += [(-min(r[2], r[3], cap), r[0]) for r in reversed(rows)]
        write_table(__file__, ("x", "depth"), out, part=name + "-outline")

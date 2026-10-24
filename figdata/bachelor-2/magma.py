"""Magmas and their emplacement (Year 2, magma-emplacement): melt viscosity and density from
composition, H2O solubility, and the conductive cooling of a sill.

  viscosity   Giordano, Russell & Dingwell (2008) model (ledger grd08:model):
              log10 eta = A + B / (T - C), A = -4.55, B and C linear in mol % oxides plus
              cross-terms; checked against the worked example of the authors' tutorial
              (B 7720, C 334, log eta 3.67 at 1273 K).  F is taken as zero.
  density     ideal mixing of partial molar volumes (DensityX, Iacovino & Till 2019, Table 1,
              ledger densityx:volumes): rho = sum X_i M_i / sum X_i V_i(T, P).  MnO and P2O5
              have no volume in that table and are left out (renormalised).
  melts       anhydrous compositions of Moore et al. (1998), Table 1 (ledger moore98:melts):
              MORB tholeiite TT152-21-35, andesite Mas-12, rhyolite KS.
  solubility  H2O-saturated experiments of Moore et al. (1998), Table 2 (ledger moore98:h2o):
              basalts (TT152-21-35 at 1200 C; 87S35 at 1050-1100 C) and rhyolites (KS at 850 C,
              Shaw DC-1 at 800-900 C, CAM-73 at 900 C).  Least-squares fit of w = s sqrt(P),
              s = sum(w sqrt P) / sum(P), P in MPa.
  sill        a sheet of thickness b intruded at T_m into rock at T_0, same diffusivity kappa,
              no latent heat: T = T_0 + (T_m - T_0)/2 [erf((b/2 - x)/(2 sqrt(kappa t)))
              + erf((b/2 + x)/(2 sqrt(kappa t)))]  (Delaney 1986, eq. 18; ledger delaney86:*);
              solidification with latent heat L (per volume) and heat capacity rho c: the
              Stefan problem, front at 2 lambda sqrt(kappa t),
              L sqrt(pi) / (rho c (T_m - T_0)) = exp(-lambda^2) / (lambda (1 + erf lambda)).

  part visc                T_C basalt andesite rhyolite rhy2 rhy4 rhy6   (log10 Pa s)
  part solub-basalt-data   P_MPa w
  part solub-rhyolite-data P_MPa w
  part solub-fit           P_MPa basalt rhyolite
  part sill                x_m t1 t2 t3 t4   (problem sill, b = 100 m, times in the values part)
  part values              what value
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

MOLAR = {"SiO2": 60.0843, "TiO2": 79.8658, "Al2O3": 101.9613, "Fe2O3": 159.6882,
         "FeO": 71.8444, "MnO": 70.9374, "MgO": 40.3044, "CaO": 56.0774, "Na2O": 61.9789,
         "K2O": 94.1960, "P2O5": 141.9445, "H2O": 18.0153}

# Moore, Vennemann & Carmichael (1998), Table 1, wt %  (ledger moore98:melts)
MORB = {"SiO2": 50.8, "TiO2": 1.84, "Al2O3": 13.7, "FeO": 12.4, "MnO": 0.22, "MgO": 6.67,
        "CaO": 11.5, "Na2O": 2.68, "K2O": 0.15, "P2O5": 0.22}
ANDESITE = {"SiO2": 62.6, "TiO2": 0.63, "Al2O3": 17.3, "Fe2O3": 2.01, "FeO": 2.01, "MnO": 0.06,
            "MgO": 2.65, "CaO": 5.64, "Na2O": 4.05, "K2O": 1.61, "P2O5": 0.24}
RHYOLITE = {"SiO2": 77.5, "Al2O3": 12.5, "FeO": 1.0, "CaO": 0.5, "Na2O": 3.6, "K2O": 4.8}

# Giordano et al. (2008) tutorial, Table 1 and Table 2  (ledger grd08:model, grd08:example)
GRD_A = -4.55
GRD_EXAMPLE = {"SiO2": 62.40, "TiO2": 0.55, "Al2O3": 20.01, "FeO": 0.03, "MnO": 0.02,
               "MgO": 3.22, "CaO": 9.08, "Na2O": 3.52, "K2O": 0.93, "P2O5": 0.12, "H2O": 2.00}

# DensityX Table 1: V (cm3/mol) at Tref (K), dV/dT (1e-3 cm3/mol/K), dV/dP (1e-4 cm3/mol/bar)
VOL = {"SiO2": (26.86, 1773, 0.0, -1.89), "TiO2": (28.32, 1773, 7.24, -2.31),
       "Al2O3": (37.42, 1773, 2.62, -2.26), "Fe2O3": (41.5, 1723, 0.0, -2.53),
       "FeO": (12.68, 1723, 3.69, -0.45), "MgO": (12.02, 1773, 3.27, 0.27),
       "CaO": (16.9, 1773, 3.74, 0.34), "Na2O": (29.65, 1773, 7.68, -2.40),
       "K2O": (47.28, 1773, 12.08, -6.75), "H2O": (22.9, 1273, 9.5, -3.20)}

# Moore et al. (1998), Table 2: (P bar, T C, H2O wt %)  (ledger moore98:h2o)
BASALT_H2O = [(310, 1200, 1.74), (507, 1200, 2.42), (717, 1200, 2.56),
              (2117, 1100, 4.51), (2185, 1050, 4.65), (2206, 1050, 5.43), (2916, 1050, 6.40)]
RHYOLITE_H2O = [(190, 850, 1.46), (500, 850, 3.15), (980, 850, 3.94), (1470, 850, 5.06),
                (1260, 850, 4.43), (1000, 900, 4.3), (2000, 800, 6.2),
                (2827, 900, 8.36), (1848, 900, 6.34)]

# Delaney (1986): heat capacity per volume 2-3 MJ/m3/C, heat of crystallisation 700-1000 MJ/m3,
# diffusivity 0.5-1e-6 m2/s (cold), 0.25-0.75e-6 (basalt above 500 C).  Problem values
# (sill at 1150 C in rock at 100 C, so T_m - T_0 = 1050 K):
RHO_C = 2.5e6        # J/m3/K
LATENT = 9.0e8       # J/m3
KAPPA = 0.7e-6       # m2/s
YEAR = 3.15576e7     # s (Julian year)


def with_water(comp, w):
    """anhydrous composition plus w wt % H2O, the anhydrous part scaled to 100 - w."""
    tot = sum(comp.values())
    out = {k: v * (100 - w) / tot for k, v in comp.items()}
    out["H2O"] = w
    return out


def mol_percent(comp):
    n = {k: v / MOLAR[k] for k, v in comp.items() if v}
    s = sum(n.values())
    return {k: 100 * v / s for k, v in n.items()}


def grd_bc(comp):
    """VFT parameters B and C of the GRD model for a wt % composition (Fe as FeO total)."""
    c = dict(comp)
    if "Fe2O3" in c:   # total iron as FeO
        c["FeO"] = c.get("FeO", 0) + c.pop("Fe2O3") * 2 * MOLAR["FeO"] / MOLAR["Fe2O3"]
    # as in the tutorial's Table 2: anhydrous oxides normalised to 100 - H2O, H2O kept
    w = c.pop("H2O", 0.0)
    dry = sum(c.values())
    c = {k: v * (100 - w) / dry for k, v in c.items()}
    c["H2O"] = w
    m = mol_percent(c)
    g = lambda k: m.get(k, 0.0)  # noqa: E731
    h2o = g("H2O")
    v = h2o                      # V = H2O + F2O-1, no fluorine
    ta = g("TiO2") + g("Al2O3")
    fm = g("FeO") + g("MnO") + g("MgO")
    nk = g("Na2O") + g("K2O")
    b = (159.6 * (g("SiO2") + g("TiO2")) - 173.3 * g("Al2O3")
         + 72.1 * (g("FeO") + g("MnO") + g("P2O5")) + 75.7 * g("MgO") - 39.0 * g("CaO")
         - 84.1 * (g("Na2O") + v) + 141.5 * (v + math.log(1 + h2o))
         - 2.43 * (g("SiO2") + g("TiO2")) * fm
         - 0.91 * (g("SiO2") + ta + g("P2O5")) * (nk + h2o)
         + 17.6 * g("Al2O3") * nk)
    cc = (2.75 * g("SiO2") + 15.7 * ta + 8.3 * fm + 10.2 * g("CaO") - 12.3 * nk
          - 99.5 * math.log(1 + v) + 0.30 * (g("Al2O3") + fm + g("CaO") - g("P2O5")) * (nk + v))
    return b, cc


def log_viscosity(comp, t_c):
    b, c = grd_bc(comp)
    return GRD_A + b / (t_c + 273.15 - c)


def density(comp, t_c, p_bar=1.0):
    """melt density in kg/m3 (DensityX equations 1-3)."""
    c = {k: v for k, v in comp.items() if k in VOL and v}
    n = {k: v / MOLAR[k] for k, v in c.items()}
    s = sum(n.values())
    x = {k: v / s for k, v in n.items()}
    t = t_c + 273.15
    mass = sum(x[k] * MOLAR[k] for k in x)
    vol = sum(x[k] * (VOL[k][0] + VOL[k][2] * 1e-3 * (t - VOL[k][1]) + VOL[k][3] * 1e-4 * (p_bar - 1))
              for k in x)
    return 1000 * mass / vol


def sqrt_fit(data):
    """least-squares s of w = s sqrt(P), P in MPa."""
    return sum(w * math.sqrt(p / 10) for p, _, w in data) / sum(p / 10 for p, _, w in data)


def saturation_pressure(w, s):
    """MPa at which a melt with w wt % H2O becomes saturated."""
    return (w / s) ** 2


def sill_temperature(x, t, b, tm, t0, kappa=KAPPA):
    if t == 0:
        return tm if abs(x) < b / 2 else t0
    r = 2 * math.sqrt(kappa * t)
    return t0 + (tm - t0) / 2 * (math.erf((b / 2 - x) / r) + math.erf((b / 2 + x) / r))


def stefan_lambda(latent=LATENT, rho_c=RHO_C, dt=1050.0):
    """root of L sqrt(pi)/(rho c dT) = exp(-l^2)/(l (1 + erf l)) by bisection."""
    lhs = latent * math.sqrt(math.pi) / (rho_c * dt)
    f = lambda lam: math.exp(-lam * lam) / (lam * (1 + math.erf(lam))) - lhs  # noqa: E731
    lo, hi = 1e-6, 5.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def solidification_time(b, lam, kappa=KAPPA):
    """seconds for fronts from both walls (2 lam sqrt(kappa t) each) to meet at the centre."""
    return (b / 2) ** 2 / (4 * lam * lam * kappa)


if __name__ == "__main__":
    temps = list(range(600, 1401, 10))
    rows = []
    for t in temps:
        rows.append((t, log_viscosity(MORB, t), log_viscosity(ANDESITE, t),
                     log_viscosity(RHYOLITE, t), log_viscosity(with_water(RHYOLITE, 2), t),
                     log_viscosity(with_water(RHYOLITE, 4), t),
                     log_viscosity(with_water(RHYOLITE, 6), t)))
    write_table(__file__, ("T_C", "basalt", "andesite", "rhyolite", "rhy2", "rhy4", "rhy6"),
                rows, part="visc")
    write_table(__file__, ("P_MPa", "w"), [(p / 10, w) for p, _, w in BASALT_H2O],
                part="solub-basalt-data")
    write_table(__file__, ("P_MPa", "w"), [(p / 10, w) for p, _, w in RHYOLITE_H2O],
                part="solub-rhyolite-data")
    sb, sr = sqrt_fit(BASALT_H2O), sqrt_fit(RHYOLITE_H2O)
    write_table(__file__, ("P_MPa", "basalt", "rhyolite"),
                [(p, sb * math.sqrt(p), sr * math.sqrt(p)) for p in range(0, 301, 5)],
                part="solub-fit")
    # the problem's sill: b = 100 m, T_m 1150 C, T_0 100 C
    b, tm, t0 = 100.0, 1150.0, 100.0
    times = [1 * YEAR, 10 * YEAR, 50 * YEAR, 200 * YEAR]
    xs = [i * 1.0 for i in range(-200, 201, 2)]
    write_table(__file__, ("x_m", "t1", "t2", "t3", "t4"),
                [(x,) + tuple(sill_temperature(x, t, b, tm, t0) for t in times) for x in xs],
                part="sill")
    lam = stefan_lambda()
    vals = [
        ("grd_example_B", grd_bc(GRD_EXAMPLE)[0]), ("grd_example_C", grd_bc(GRD_EXAMPLE)[1]),
        ("grd_example_logeta_1273K", log_viscosity(GRD_EXAMPLE, 1273 - 273.15)),
        ("logeta_basalt_1200", log_viscosity(MORB, 1200)),
        ("logeta_andesite_1000", log_viscosity(ANDESITE, 1000)),
        ("logeta_rhyolite_800", log_viscosity(RHYOLITE, 800)),
        ("logeta_rhyolite4_800", log_viscosity(with_water(RHYOLITE, 4), 800)),
        ("logeta_rhyolite6_800", log_viscosity(with_water(RHYOLITE, 6), 800)),
        ("rho_basalt_1200", density(MORB, 1200)),
        ("rho_andesite_1000", density(ANDESITE, 1000)),
        ("rho_rhyolite_850", density(RHYOLITE, 850)),
        ("rho_rhyolite4_850", density(with_water(RHYOLITE, 4), 850)),
        ("s_basalt", sb), ("s_rhyolite", sr),
        ("psat_basalt_0.5wt", saturation_pressure(0.5, sb)),
        ("psat_rhyolite_5wt", saturation_pressure(5.0, sr)),
        ("stefan_lambda", lam),
        ("sill_100m_years", solidification_time(100.0, lam) / YEAR),
        ("sill_L2_over_kappa_years", 50.0 ** 2 / KAPPA / YEAR),
    ]
    write_table(__file__, ("what", "value"), vals, part="values")

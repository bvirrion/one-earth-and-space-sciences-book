"""Kyanite, andalusite, sillimanite: the P-T diagram of Al2SiO5 (grade 12, metamorphic rocks).

The three boundaries are the equilibrium pressures of Holdaway and Mukhopadhyay (1993),
Table 11 (ledger hm93:table11), joined by straight lines between the tabulated
temperatures; their triple point, printed as 504 degC and 3.75 kbar (hm93:triple), is
recomputed here as the meeting point of the three lines. 1 kbar = 0.1 GPa.

Pressure is turned into depth by the weight of the rock above (lithostatic pressure,
P = rho g z) with the mean density of the continental crust, 2830 kg/m3 (ledger
cm95:crust), and g = 9.81 m/s2. A geotherm T = T0 + G z, with T0 = 10 degC at the
surface and the gradients G of three settings (ledger earle:settings: subduction zone
less than 10, typical 30, volcanic areas 40-50 degC per km), becomes a line on the
diagram.

  part andky      T P_GPa                     kyanite = andalusite, 200 degC to the triple point
  part kysil      T P_GPa                     kyanite = sillimanite, triple point to 900 degC
  part andsil     T P_GPa                     andalusite = sillimanite, triple point to 700 degC
  part andsilx    T P_GPa                     the same, continued in a straight line to P = 0 (dashed)
  part geotherms  z_km P_GPa T10 T30 T50      three geotherms, 0 to 45 km
  part depth      P_GPa z_km                  ticks of the depth axis
  part crossings  grad T P_GPa z_km which     where each geotherm crosses a boundary
  part numbers    key value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from _table import write_table  # noqa: E402

RHO = 2830.0          # kg/m3, mean continental crust
G = 9.81              # m/s2
T0 = 10.0             # degC at the surface
GRADIENTS = (10.0, 30.0, 50.0)   # degC per km: subduction zone, typical, volcanic area

# Holdaway and Mukhopadhyay (1993), Table 11: T (degC) -> P (kbar)
AND_KY = {200: 0.16, 300: 1.36, 400: 2.54, 500: 3.71, 600: 4.86, 700: 6.00,
          800: 7.13, 900: 8.24, 1000: 9.33}
KY_SIL = {500: 3.67, 600: 5.77, 700: 7.86, 800: 9.95, 900: 12.05, 1000: 14.16}
AND_SIL = {500: 3.82, 600: 2.30, 700: 0.95}
PRINTED_TRIPLE = (504.0, 3.75)


def _interp(table, t):
    """Pressure (kbar) on a boundary at temperature t (degC): straight lines between the
    tabulated points, the end segments continued beyond them."""
    ts = sorted(table)
    if t <= ts[1]:
        a, b = ts[0], ts[1]
    elif t >= ts[-2]:
        a, b = ts[-2], ts[-1]
    else:
        a = max(x for x in ts if x <= t)
        b = min(x for x in ts if x > t)
    return table[a] + (table[b] - table[a]) * (t - a) / (b - a)


def p_and_ky(t):
    return _interp(AND_KY, t)


def p_ky_sil(t):
    return _interp(KY_SIL, t)


def p_and_sil(t):
    return _interp(AND_SIL, t)


def _bisect(f, lo, hi, tol=1e-9):
    flo = f(lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


def triple_point():
    """Meeting point (T degC, P kbar) of kyanite = andalusite and kyanite = sillimanite."""
    t = _bisect(lambda x: p_and_ky(x) - p_ky_sil(x), 450.0, 590.0)
    return t, p_and_ky(t)


def depth_km(p_gpa):
    """Depth (km) at which the weight of the rock above makes a pressure p (GPa)."""
    return p_gpa * 1e9 / (RHO * G) / 1000.0


def pressure_gpa(z_km):
    """Lithostatic pressure (GPa) at depth z (km): P = rho g z."""
    return RHO * G * z_km * 1000.0 / 1e9


def geotherm_t(z_km, grad):
    return T0 + grad * z_km


def t_on_kysil(p_kbar):
    """Temperature (degC) at which kyanite turns into sillimanite at pressure p (kbar)."""
    return _bisect(lambda x: p_ky_sil(x) - p_kbar, 300.0, 1100.0)


def stable(t, p_kbar):
    """Name of the stable polymorph at (t degC, p kbar)."""
    tt, _ = triple_point()
    if t <= tt:
        return "kyanite" if p_kbar > p_and_ky(t) else "andalusite"
    if p_kbar > p_ky_sil(t):
        return "kyanite"
    return "andalusite" if p_kbar < p_and_sil(t) else "sillimanite"


def crossings(grad):
    """Where a geotherm crosses the boundaries: [(T, P kbar, z km, 'a->b'), ...] going down."""
    out = []
    prev = stable(geotherm_t(0.0, grad), 0.0)
    z, dz = 0.0, 0.01
    while z < 45.0:
        z2 = z + dz
        s = stable(geotherm_t(z2, grad), 10 * pressure_gpa(z2))
        if s != prev:
            def side(q, before=prev):
                return -1.0 if stable(geotherm_t(q, grad), 10 * pressure_gpa(q)) == before else 1.0
            zc = _bisect(side, z, z2)
            out.append((geotherm_t(zc, grad), 10 * pressure_gpa(zc), zc, "%s->%s" % (prev, s)))
            prev = s
        z = z2
    return out


def numbers():
    n = {}
    tt, pt = triple_point()
    n["triple_T"], n["triple_P_kbar"] = tt, pt
    n["triple_P_gpa"] = pt / 10
    n["triple_z_km"] = depth_km(pt / 10)
    n["triple_andsil_gap_kbar"] = p_and_sil(tt) - pt
    n["P_35km_gpa"] = pressure_gpa(35.0)
    n["z_1gpa_km"] = depth_km(1.0)
    n["dPdz_mpa_per_km"] = pressure_gpa(1.0) * 1000
    n["kysil_T_at_6kbar"] = t_on_kysil(6.0)
    n["kysil_z_at_6kbar"] = depth_km(0.6)
    n["kysil_slope_kbar_per_100C"] = KY_SIL[700] - KY_SIL[600]
    n["andky_slope_kbar_per_100C"] = AND_KY[600] - AND_KY[500]
    n["andsil_slope_kbar_per_100C"] = AND_SIL[700] - AND_SIL[600]
    n["andsil_T_at_0"] = _bisect(p_and_sil, 600.0, 900.0)
    for g in GRADIENTS:
        for i, (t, p, z, w) in enumerate(crossings(g)):
            n["cross_%d_%d_T" % (g, i)] = t
            n["cross_%d_%d_z" % (g, i)] = z
    n["sub10_T_at_1gpa"] = geotherm_t(depth_km(1.0), 10.0)
    # the weekend problem: a kyanite schist that crystallised at 0.70 GPa and 600 degC
    n["pb_P_gpa"], n["pb_T"] = 0.70, 600.0
    n["pb_z_km"] = depth_km(0.70)
    n["pb_grad"] = (600.0 - T0) / depth_km(0.70)
    n["pb_kysil_P_at_600_gpa"] = p_ky_sil(600.0) / 10
    n["pb_stable"] = 1.0 if stable(600.0, 7.0) == "kyanite" else 0.0
    return n


if __name__ == "__main__":
    tt, pt = triple_point()
    write_table(__file__, ("T", "P_GPa"),
                [(t, p_and_ky(t) / 10) for t in range(200, 500, 10)] + [(tt, pt / 10)], part="andky", digits=5)
    write_table(__file__, ("T", "P_GPa"),
                [(tt, pt / 10)] + [(t, p_ky_sil(t) / 10) for t in range(510, 910, 10)], part="kysil", digits=5)
    write_table(__file__, ("T", "P_GPa"),
                [(tt, pt / 10)] + [(t, p_and_sil(t) / 10) for t in range(510, 710, 10)], part="andsil", digits=5)
    t0 = _bisect(p_and_sil, 600.0, 900.0)
    write_table(__file__, ("T", "P_GPa"), [(700, p_and_sil(700) / 10), (t0, 0.0)], part="andsilx", digits=5)
    zs = [i * 0.5 for i in range(0, 91)]
    write_table(__file__, ("z_km", "P_GPa", "T10", "T30", "T50"),
                [(z, pressure_gpa(z), *(geotherm_t(z, g) for g in GRADIENTS)) for z in zs],
                part="geotherms", digits=5)
    write_table(__file__, ("P_GPa", "z_km"), [(pressure_gpa(z), z) for z in range(0, 50, 5)],
                part="depth", digits=5)
    write_table(__file__, ("grad", "T", "P_GPa", "z_km", "which"),
                [(g, t, p / 10, z, w) for g in GRADIENTS for t, p, z, w in crossings(g)],
                part="crossings", digits=5)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)

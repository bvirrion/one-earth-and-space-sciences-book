"""Volcanic eruptions (Year 2, eruptive-styles): tephra thinning and volume, the eruption
frequency-size law from the Holocene record, column height against mass eruption rate, and
the surface uplift above a Mogi source.

  thinning   Cotopaxi Layer 5 isopachs, Biass, Bonadonna & Houghton (2019), Table 2 (ledger
             biass19:layer5): thickness T (cm) against the square root of the isopach area
             x = sqrt(A) (km).  Exponential segments ln T = ln T0 - k x fitted by least squares
             (segment 1: the two proximal isopachs; segment 2: the four distal ones); volume
             by integrating T over the area, dA = 2 x dx:
               one segment   V = 2 T0 / k^2
               two segments  V = 2 T0/k1^2 + 2 T0 exp(-k1 X)[(k2 X + 1)/k2^2 - (k1 X + 1)/k1^2],
             X = sqrt(A) where the two fitted lines cross.  The authors' two-segment volume is
             0.29 km3, with thickness half-distances bt_A = ln 2 / k of 1.9 and 5.3 km.
  frequency  data/derived/bachelor-2-gvp-eruptions.csv (GVP Volcanoes of the World, confirmed
             eruptions with a VEI).  Rate of eruptions of VEI >= v per year, counted over a
             window that starts further back for larger eruptions, whose record is complete
             for longer (Brown et al. 2014): v = 3 from 1950, 4 from 1900, 5 from 1800, 6 from
             1500, all to 2024 inclusive.  Least-squares line log10 rate = a - b v over v = 3-6;
             VEI >= 7 since 1000 is shown, not fitted.
  column     top height above the vent H (km) against the mass eruption rate Q (kg/s):
             Mastin et al. (2009) H = 0.304 Q^0.241 and Aubry et al. (2023) H = 0.345 Q^0.226
             (ledger aubry23:fits); example eruptions of Mastin et al. (2009b, Table 2, ledger
             mastin09:examples).
  gas        closed-system degassing of water during ascent: exsolved mass fraction
             x(p) = (w0 - s sqrt(p))/100 below the saturation pressure (s from the square-root fit
             of chapter magma-emplacement to Moore et al. 1998, ledger moore98:h2o), vapour an
             ideal gas, melt incompressible: phi = V_g / (V_g + V_m), V_g = x R T / (M p),
             V_m = (1 - x)/rho_m per kilogram of magma.  Rhyolite: w0 5 wt %, s 0.444,
             850 C, 2300 kg/m3; basalt: w0 1 wt %, s 0.340, 1200 C, 2700 kg/m3.
  mogi       point source of volume change dV at depth z0 in an elastic half-space, Poisson
             ratio nu: u_z(r) = (1 - nu) dV z0 / (pi (r^2 + z0^2)^(3/2)) (Battaglia et al. 2013,
             eq. 16 to leading order and eq. 19, dV = pi a^3 dP / mu; ledger dmodels:mogi).

  part thin-data     sqrtA_km T_cm
  part thin-fit      sqrtA_km seg1 seg2
  part vei-cumul     year f3 f4 f5 f6      (fraction of the eruptions since 1500 recorded by then)
  part vei-rate      vei rate start count
  part vei-rate7     vei rate start count
  part vei-fit       vei rate
  part column        Q mastin aubry
  part column-data   Q H label
  part gas           p_MPa rhyolite basalt   (gas volume fraction)
  part mogi          r_km z2 z4            (uplift in mm for dV = 1e6 m3, nu = 0.25)
  part values        what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "..", "..", "data", "derived", "bachelor-2-gvp-eruptions.csv")

# Cotopaxi Layer 5, isopach sqrt(area) (km) and thickness (cm), Biass et al. 2019, Table 2
LAYER5 = [(7.0, 100.0), (8.9, 50.0), (12.3, 30.0), (17.4, 20.0), (21.4, 10.0), (25.5, 5.0)]
SPLIT = 2                       # break in slope after the second isopach (the authors' choice)

WINDOWS = {3: 1950, 4: 1900, 5: 1800, 6: 1500}
END = 2024
WINDOW7 = 1000

# Mastin et al. (2009b) Table 2 examples: label, H (km above vent), Q (kg/s)
COLUMN_EXAMPLES = [("Etna 2001", 2.0, 5e3), ("Cerro Negro 1992", 7.0, 1e5),
                   ("Ruapehu 1996", 5.0, 2e5), ("Fuego 1974", 10.0, 1e6),
                   ("Soufriere Hills", 10.0, 3e6), ("Spurr 1992", 11.0, 4e6),
                   ("St Helens 1980", 15.0, 1e7), ("St Helens co-ignimbrite", 25.0, 1e8)]


def line_fit(xs, ys):
    """Least-squares slope and intercept of y = a + b x."""
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b


def segment(points):
    """(T0, k) of ln T = ln T0 - k x through the points (least squares)."""
    a, b = line_fit([x for x, _ in points], [math.log(t) for _, t in points])
    return math.exp(a), -b


def volume_one(t0, k):
    """Volume of an exponentially thinning deposit, T0 and k in consistent units."""
    return 2 * t0 / k ** 2


def volume_two(t0, k1, k2, x_ip):
    """Volume of a two-segment deposit, continuous at x_ip."""
    return (2 * t0 / k1 ** 2 + 2 * t0 * math.exp(-k1 * x_ip)
            * ((k2 * x_ip + 1) / k2 ** 2 - (k1 * x_ip + 1) / k1 ** 2))


def layer5():
    """T0 (cm), k1, k2 (1/km), crossing X (km) and volume (km3) of Cotopaxi Layer 5."""
    t01, k1 = segment(LAYER5[:SPLIT])
    t02, k2 = segment(LAYER5[SPLIT:])
    x_ip = math.log(t01 / t02) / (k1 - k2)
    v = volume_two(t01 * 1e-5, k1, k2, x_ip)        # cm -> km
    return t01, k1, t02, k2, x_ip, v


def load_eruptions():
    with open(CSV, encoding="utf8") as f:
        return [(int(r["start_year"]), int(r["vei"])) for r in csv.DictReader(f)]


def rate(eruptions, v, start, end=END):
    """(rate per year, count) of eruptions of VEI >= v starting in [start, end]."""
    n = sum(1 for y, e in eruptions if e >= v and start <= y <= end)
    return n / (end - start + 1), n


def frequency_fit(eruptions):
    """(a, b) of log10 rate(VEI >= v) = a - b v over the windows."""
    vs = sorted(WINDOWS)
    a, slope = line_fit(vs, [math.log10(rate(eruptions, v, WINDOWS[v])[0]) for v in vs])
    return a, -slope


def poisson_at_least_one(lam_per_year, years):
    return 1 - math.exp(-lam_per_year * years)


def mastin(q):
    return 0.304 * q ** 0.241


def aubry(q):
    return 0.345 * q ** 0.226


R_GAS, M_H2O = 8.314, 0.018015
RHYOLITE_GAS = dict(w0=5.0, s=0.444, t_k=1123.15, rho_m=2300.0)
BASALT_GAS = dict(w0=1.0, s=0.340, t_k=1473.15, rho_m=2700.0)


def gas_fraction(p_mpa, w0, s, t_k, rho_m):
    """Volume fraction of exsolved water vapour at pressure p (MPa), closed system."""
    x = max(0.0, w0 - s * math.sqrt(p_mpa)) / 100
    vg = x * R_GAS * t_k / (M_H2O * p_mpa * 1e6)
    vm = (1 - x) / rho_m
    return vg / (vg + vm)


def pressure_at_fraction(phi, **melt):
    """Pressure (MPa) at which the gas volume fraction reaches phi (bisection in log p)."""
    lo, hi = 1e-3, (melt["w0"] / melt["s"]) ** 2
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if gas_fraction(mid, **melt) > phi:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def mogi_uz(r, z0, dv, nu=0.25):
    """Vertical surface displacement (m) at distance r (m) above a Mogi source."""
    return (1 - nu) * dv * z0 / (math.pi * (r * r + z0 * z0) ** 1.5)


def mogi_half_width(z0):
    """Distance at which the uplift falls to half its maximum."""
    return z0 * math.sqrt(2 ** (2 / 3) - 1)


if __name__ == "__main__":
    write_table(__file__, ("sqrtA_km", "T_cm"), LAYER5, part="thin-data")
    t01, k1, t02, k2, x_ip, v5 = layer5()
    write_table(__file__, ("sqrtA_km", "seg1", "seg2"),
                [(x / 2, t01 * math.exp(-k1 * x / 2), t02 * math.exp(-k2 * x / 2))
                 for x in range(0, 61)], part="thin-fit")

    er = load_eruptions()
    rows = []
    totals = {v: sum(1 for y, e in er if e >= v and 1500 <= y <= END) for v in (3, 4, 5, 6)}
    for year in range(1500, END + 1, 4):
        rows.append((year,) + tuple(sum(1 for y, e in er if e >= v and 1500 <= y <= year)
                                    / totals[v] for v in (3, 4, 5, 6)))
    write_table(__file__, ("year", "f3", "f4", "f5", "f6"), rows, part="vei-cumul")
    rr = []
    for v in sorted(WINDOWS):
        lam, n = rate(er, v, WINDOWS[v])
        rr.append((v, lam, WINDOWS[v], n))
    write_table(__file__, ("vei", "rate", "start", "count"), rr, part="vei-rate")
    lam7, n7 = rate(er, 7, WINDOW7)
    write_table(__file__, ("vei", "rate", "start", "count"), [(7, lam7, WINDOW7, n7)],
                part="vei-rate7")
    a, b = frequency_fit(er)
    write_table(__file__, ("vei", "rate"), [(x / 10, 10 ** (a - b * x / 10))
                                            for x in range(25, 76)], part="vei-fit")

    qs = [10 ** (e / 10) for e in range(30, 91)]
    write_table(__file__, ("Q", "mastin", "aubry"), [(q, mastin(q), aubry(q)) for q in qs],
                part="column")
    write_table(__file__, ("Q", "H", "label"),
                [(q, h, lab.replace(" ", "~")) for lab, h, q in COLUMN_EXAMPLES],
                part="column-data")

    ps = [10 ** (e / 50) for e in range(-100, 126)]
    write_table(__file__, ("p_MPa", "rhyolite", "basalt"),
                [(p, gas_fraction(p, **RHYOLITE_GAS), gas_fraction(p, **BASALT_GAS)) for p in ps],
                part="gas")
    write_table(__file__, ("r_km", "z2", "z4"),
                [(r / 10, 1e3 * mogi_uz(r * 100.0, 2000.0, 1e6), 1e3 * mogi_uz(r * 100.0, 4000.0, 1e6))
                 for r in range(-120, 121)], part="mogi")

    lam6 = 10 ** (a - b * 6)
    vals = [("layer5_T0_cm", t01), ("layer5_k1", k1), ("layer5_T02_cm", t02), ("layer5_k2", k2),
            ("layer5_btA1_km", math.log(2) / k1), ("layer5_btA2_km", math.log(2) / k2),
            ("layer5_xip_km", x_ip), ("layer5_volume_km3", v5),
            ("fit_a", a), ("fit_b", b), ("rate_ge6_fit", lam6),
            ("p_ge6_100yr", poisson_at_least_one(lam6, 100)), ("rate_ge7_fit", 10 ** (a - b * 7)),
            ("mogi_half_width_z0", mogi_half_width(1.0)),
            ("mogi_uz0_z2_mm", 1e3 * mogi_uz(0, 2000.0, 1e6)),
            ("mastin_1e7", mastin(1e7)), ("aubry_1e7", aubry(1e7)),
            ("rhy_psat", (RHYOLITE_GAS["w0"] / RHYOLITE_GAS["s"]) ** 2),
            ("bas_psat", (BASALT_GAS["w0"] / BASALT_GAS["s"]) ** 2),
            ("rhy_p85", pressure_at_fraction(0.85, **RHYOLITE_GAS)),
            ("bas_p85", pressure_at_fraction(0.85, **BASALT_GAS)),
            ("rhy_phi_10MPa", gas_fraction(10, **RHYOLITE_GAS)),
            ("bas_phi_1MPa", gas_fraction(1, **BASALT_GAS)),
            ("rhy_phi_0.1", gas_fraction(0.1, **RHYOLITE_GAS)),
            ("bas_phi_0.1", gas_fraction(0.1, **BASALT_GAS))]
    vals += [("rate_ge%d" % v, lam) for v, lam, _, _ in rr]
    vals += [("count_ge%d" % v, n) for v, _, _, n in rr]
    vals += [("rate_ge7_obs", lam7), ("count_ge7", n7)]
    write_table(__file__, ("what", "value"), vals, part="values")

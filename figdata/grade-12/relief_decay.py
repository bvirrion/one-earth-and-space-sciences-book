"""The destruction of mountains (grade 12): erosion rates, isostatic rebound and the
exponential decay of a range's mean elevation.

Rebound (Airy, as in grade-11 lithosphere-asthenosphere): removing a thickness e of
crust from the top of a floating column lowers its surface by only e (1 - rho_c/rho_m);
the rest is made up by the column rising. rho_c = 2830 kg/m3 (ledger cm95:crust),
rho_m = 3380 kg/m3 just below the Moho (ledger data:prem), the values printed in g11.03.

Decay law: the erosion rate is proportional to the relief (Ahnert 1970, ledger
ahnert70:decay): E = k h. Without rebound dh/dt = -k h; with full rebound
dh/dt = -f k h with f = 1 - rho_c/rho_m. k is calibrated on Ahnert's statement that,
with no uplift, the relief falls to a tenth in 11 Myr: k = ln 10 / 11 per Myr.

Erosion budgets: a river's sediment load (mass a year), plus the dissolved load (on
average 15 % of the mass carried, Earle 13.3, ledger earle:loads), spread over its basin
as a layer of rock of density rho_c. Mississippi: 400 Mt/yr before 1900 and 145 Mt/yr in
1987-2006 (ledger mm10:mississippi), basin 1,150,000 mi2 = 2,980,000 km2 (USGS, Kammerer 1990; ledger kammerer:mississippi).
World: prehuman suspended plus bed load 15.5 Gt/yr (Book 1 row syvitski:modern-flux),
land = 29.04 % of a sphere of radius 6371 km (grade-11 hypsometry numbers, ETOPO1).

Varden Hills: the unconformity (base of the Triassic sandstone) along section A-B,
from the shared region model (imported, never edited), below the ground and above the
section frame's floor (-700 m) only.

  part curve        t_Myr h_none h_rebound      mean elevation of a 2000 m range (m)
  part unconformity s_km z_m                    base of the cover along A-B (nan = gap)
  part rates        idx measured budget        bar chart of denudation rates (m/Myr), bottom to top
  part numbers      key value

Measured 10Be rates (Portenga and Bierman 2011, ledger pb11:rates) and the two budgets
computed here, in the order of RATES (labels are typed in the chapter, same order).
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402

RHO_C, RHO_M = 2830.0, 3380.0
K = math.log(10.0) / 11.0                 # per Myr (Ahnert 1970: to 10 % in 11 Myr)
H0 = 2000.0                               # m, the example range
DISSOLVED = 0.15                          # dissolved share of the mass carried
MISS_AREA_KM2 = 2980000.0                  # 1,150,000 mi2 (Kammerer 1990), rounded
MISS_LOAD_MT = {"before 1900": 400.0, "1987-2006": 145.0}
WORLD_LOAD_GT = 15.5
EARTH_R_KM = 6371.0
ZMIN = -700.0                             # m, bottom of the shared section frame
HYPSO = os.path.join(HERE, "..", "out", "grade-11-hypsometry-numbers.dat")


PB11 = (("outcrops, median", 5.4), ("outcrops, mean", 12.0), ("basins, median", 54.0),
        ("arid basins, mean", 100.0), ("quiet basins, mean", 182.0), ("basins, mean", 218.0),
        ("seismic basins, mean", 367.0), ("polar basins, mean", 537.0))


def rates():
    """(label, value, is_budget) sorted by value, the two budgets among the measured rates."""
    n = numbers()
    rows = [(lab, v, False) for lab, v in PB11]
    rows += [("world rivers, budget", n["world_m_per_myr"], True),
             ("Mississippi before 1900, budget", n["miss_before_1900_m_per_myr"], True)]
    return sorted(rows, key=lambda r: r[1])


def rebound_fraction():
    """Share of the eroded thickness by which the surface actually goes down."""
    return 1.0 - RHO_C / RHO_M


def lowering_m(eroded_m):
    return eroded_m * rebound_fraction()


def eroded_for_lowering(lowering):
    return lowering / rebound_fraction()


def elevation(t_myr, h0=H0, rebound=False):
    rate = K * (rebound_fraction() if rebound else 1.0)
    return h0 * math.exp(-rate * t_myr)


def time_constant(rebound=False):
    return 1.0 / (K * (rebound_fraction() if rebound else 1.0))


def half_life(rebound=False):
    return math.log(2.0) * time_constant(rebound)


def time_to_fraction(frac, rebound=False):
    return -math.log(frac) * time_constant(rebound)


def denudation_m_per_myr(load_t_per_yr, area_km2, with_dissolved=True):
    """Mean lowering of the basin by erosion (m per Myr) from a river's load."""
    mass = load_t_per_yr * 1000.0 / (1.0 - DISSOLVED if with_dissolved else 1.0)   # kg a year
    volume = mass / RHO_C                                                            # m3 a year
    return volume / (area_km2 * 1e6) * 1e6


def hypso(key):
    with open(HYPSO, encoding="utf8") as f:
        next(f)
        for line in f:
            k, v = line.split()
            if k == key:
                return float(v)
    raise KeyError(key)


def land_area_km2():
    return hypso("land_fraction") * 4.0 * math.pi * EARTH_R_KM ** 2


def unconformity_z(rg, x, y):
    """Elevation of the base of the sandstone on the vertical through (x, y), or None
    where the normal fault has cut it out. The footwall value counts only if it lies in
    the footwall, the hanging-wall value (restored through the slip) only if it lies in
    the hanging wall; between the two cut-offs a vertical meets no unconformity.
    (region.contact_elevation's fixed-point iteration does not converge in that gap and
    returns a footwall value lying in the hanging wall, hence this check.)"""
    z_fw = rg.base_cover(x, y)
    sx, sy, sz = rg._slip()
    z_hw = rg.base_cover(x - sx, y - sy) + sz
    ok_fw = not rg.hanging_wall(x, y, z_fw)
    ok_hw = rg.hanging_wall(x, y, z_hw)
    if ok_fw and ok_hw:
        return max(z_fw, z_hw)
    if ok_fw:
        return z_fw
    if ok_hw:
        return z_hw
    return None


def unconformity(ds=10.0):
    import region as rg
    (ax, ay), (bx, by) = rg.SECTION_AB
    L = math.hypot(bx - ax, by - ay)
    rows, prev_below = [], None
    n = int(L / ds)
    for i in range(n + 1):
        s = i * ds
        x, y = ax + (bx - ax) * s / L, ay + (by - ay) * s / L
        z = unconformity_z(rg, x, y)
        below = z is not None and ZMIN <= z <= rg.topo(x, y)   # exists here, inside the frame, under the ground
        if below:
            if prev_below is False and rows:
                rows.append((float("nan"), float("nan")))
            rows.append((s / 1000.0, z))
        prev_below = below
    return rows


def numbers():
    n = {}
    f = rebound_fraction()
    n["rebound_fraction"] = f
    n["lowering_per_km_m"] = lowering_m(1000.0)
    n["root_rise_per_km_m"] = 1000.0 - lowering_m(1000.0)
    n["k_per_myr"] = K
    n["tau_none_myr"] = time_constant(False)
    n["tau_rebound_myr"] = time_constant(True)
    n["half_none_myr"] = half_life(False)
    n["half_rebound_myr"] = half_life(True)
    n["t10_none_myr"] = time_to_fraction(0.1, False)
    n["t10_rebound_myr"] = time_to_fraction(0.1, True)
    n["E0_m_per_myr"] = K * H0
    n["h_after_200myr_rebound_m"] = elevation(200.0, rebound=True)
    n["h_after_250myr_rebound_m"] = elevation(250.0, rebound=True)
    n["eroded_for_2000m_km"] = eroded_for_lowering(2000.0) / 1000.0
    for k, v in MISS_LOAD_MT.items():
        tag = k.replace(" ", "_").replace("-", "_")
        n["miss_%s_m_per_myr" % tag] = denudation_m_per_myr(v * 1e6, MISS_AREA_KM2)
        n["miss_%s_susp_only_m_per_myr" % tag] = denudation_m_per_myr(v * 1e6, MISS_AREA_KM2, False)
    la = land_area_km2()
    n["land_area_km2"] = la
    w = denudation_m_per_myr(WORLD_LOAD_GT * 1e9, la)
    n["world_m_per_myr"] = w
    n["world_volume_km3_per_yr"] = WORLD_LOAD_GT * 1e12 / (1.0 - DISSOLVED) / RHO_C / 1e9
    ml = hypso("mean_land_m")
    n["mean_land_m"] = ml
    n["world_time_none_myr"] = ml / w
    n["world_time_rebound_myr"] = ml / w / f
    n["varden_gap_myr"] = 310.0 - 251.902
    return n


if __name__ == "__main__":
    write_table(__file__, ("t_Myr", "h_none", "h_rebound"),
                [(t, elevation(t), elevation(t, rebound=True)) for t in range(0, 101)], part="curve")
    write_table(__file__, ("s_km", "z_m"), unconformity(), part="unconformity", digits=6)
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)
    write_table(__file__, ("idx", "measured", "budget"),
                [(i, float("nan") if b else v, v if b else float("nan")) for i, (lab, v, b) in enumerate(rates(), 1)],
                part="rates", digits=5)
    for i, (lab, v, b) in enumerate(rates(), 1):
        print(i, lab, round(v, 1))

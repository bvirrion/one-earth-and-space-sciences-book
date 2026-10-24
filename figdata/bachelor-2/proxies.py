"""Climate archives and proxies (Year 2, climate-proxies): the ice-volume effect, two
calibrations, the benthic stack and the Antarctic ice core, and an annual-layer age model.

  icevol    the oxygen-isotope shift of the ocean when ice of composition d_ice (permil, VSMOW)
            locks up a layer h of sea level: mass balance on an ocean of mean depth H = 3682.2 m
            (charette:ocean-volume) whose present d18O is taken as 0, the ocean area held fixed:
            d_glacial = -h d_ice / (H - h). Columns for d_ice = -30, -40, -50 permil
            (white13c9:ice-volume, miller20:ice-cal).
  calib     (a) the benthic foraminiferal calibration T = 16.1 - 4.76 [d_b - (d_sw - 0.27)]
            (miller20:paleotemp), written as d_b - d_sw against T; (b) the planktonic Mg/Ca
            calibration Mg/Ca = 0.4 exp(0.09 T) and the fitted 0.372 exp(0.0936 T) (morley24:mgca).
  lr04      the LR04 benthic stack (data:lr04) over the last 800 kyr.
  edc       the EPICA Dome C temperature anomaly (data:edc-jouzel) over the last 800 kyr, one point
            in two to keep the file small (the bags are 55 cm; the plot cannot resolve more).
  co2       the Antarctic ice-core CO2 composite (data:co2-bereiter) over the last 800 kyr.
  gicc05    Table 1 of Svensson et al. (2008) (svensson08:table1): GICC05 age (yr b2k), its
            counting uncertainty and the NorthGRIP depth of 18 climate events, with the mean layer
            thickness between successive events, and, for comparison, the uncertainty the same
            number of uncertain layers would give if their errors were independent.
  numbers   the values quoted in the text, exercises and problem.

  part icevol   h_m d30 d40 d50
  part calib    T dd_benthic mgca_pred mgca_fit
  part lr04     age_ka d18O
  part edc      age_ka dT
  part co2      age_ka co2
  part gicc05   age_ka depth_m err_yr err_random_yr thick_cm
  part numbers  key value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")
H_OCEAN = 3682.2  # m, mean ocean depth (charette:ocean-volume)

# GICC05 (svensson08:table1): event, age (yr b2k), uncertainty (yr), NorthGRIP depth (m)
GICC05 = [
    ("YD/PB", 11703, 50, 1492.45), ("GI-1", 14692, 93, 1604.64), ("GI-2", 23340, 298, 1793.20),
    ("GI-3", 27780, 416, 1869.12), ("GI-4", 28900, 449, 1891.57), ("GI-5", 32500, 566, 1951.66),
    ("GI-6", 33740, 606, 1974.56), ("GI-7", 35480, 661, 2009.45), ("GI-8", 38220, 725, 2070.03),
    ("GI-9", 40160, 790, 2099.62), ("GI-10", 41460, 817, 2124.03), ("GI-11", 43340, 868, 2157.49),
    ("GI-12", 46860, 956, 2222.30), ("GI-13", 49280, 1015, 2256.90), ("GI-14", 54220, 1150, 2345.52),
    ("GI-15", 55800, 1196, 2366.32), ("GI-16", 58280, 1256, 2402.55), ("GI-17", 59440, 1287, 2420.44),
]


def ice_volume_shift(h, d_ice, depth=H_OCEAN):
    """d18O of the glacial ocean (permil) when a layer h (m) of sea level is stored as ice of
    composition d_ice, starting from an ocean at 0 permil."""
    return -h * d_ice / (depth - h)


def benthic_temperature(d_b, d_sw):
    """T (degC) from benthic calcite d_b (VPDB) and seawater d_sw (VSMOW)."""
    return 16.1 - 4.76 * (d_b - (d_sw - 0.27))


def benthic_offset(T):
    """d_b - d_sw (permil) in equilibrium at temperature T."""
    return (16.1 - T) / 4.76 - 0.27


def mgca(T, b=0.4, a=0.09):
    return b * math.exp(a * T)


def mgca_temperature(ratio, b=0.4, a=0.09):
    return math.log(ratio / b) / a


def read(name, cols):
    with open(os.path.join(DERIVED, name + ".csv"), encoding="utf8") as f:
        return [tuple(float(r[c]) for c in cols) for r in csv.DictReader(f)]


def window_mean(rows, lo, hi):
    v = [y for x, y in rows if lo <= x <= hi]
    return sum(v) / len(v)


def lr04():
    return read("lr04", ("age_ka", "d18O_permil"))


def edc():
    return [(a / 1000.0, t) for a, t in read("edc-temperature", ("age_yr_bp", "temp_anomaly_C"))]


def edc_dd():
    return [(a / 1000.0, d) for a, d in read("edc-temperature", ("age_yr_bp", "dD_permil"))]


def co2():
    return [(a / 1000.0, c) for a, c in read("co2-icecore", ("age_yr_bp", "co2_ppm")) if a >= 0]


def uncertain_layers(err):
    """Each uncertain layer counts 1/2 +- 1/2: n uncertain layers give an error n/2."""
    return 2 * err


def random_error(err):
    """The error of the same n uncertain layers if each were independent with sd 1/2."""
    return 0.5 * math.sqrt(uncertain_layers(err))


def numbers():
    lr, ed, dd = lr04(), edc(), edc_dd()
    n = {}
    n["lr04_today"] = lr[0][1]
    n["lr04_lgm"] = window_mean(lr, 19, 23)
    n["lr04_delta"] = n["lr04_lgm"] - n["lr04_today"]
    for h in (125.0, 130.0, 134.0):
        for d in (-30.0, -35.0, -40.0, -50.0):
            n["icevol_h%d_d%d" % (h, -d)] = ice_volume_shift(h, d)
    n["slope_d40_per_m"] = ice_volume_shift(1.0, -40.0)
    n["dice_for_1permil_h130"] = -1.0 * (H_OCEAN - 130.0) / 130.0
    n["cool_mass_balance"] = 4.76 * (n["lr04_delta"] - n["icevol_h130_d40"])
    n["cool_porewater"] = 4.76 * (n["lr04_delta"] - 1.0)
    n["edc_holo_C"] = window_mean(ed, 0, 2)
    n["edc_lgm_C"] = window_mean(ed, 19, 23)
    n["edc_holo_dD"] = window_mean(dd, 0, 2)
    n["edc_lgm_dD"] = window_mean(dd, 19, 23)
    n["edc_slope"] = (n["edc_holo_dD"] - n["edc_lgm_dD"]) / (n["edc_holo_C"] - n["edc_lgm_C"])
    c = co2()
    n["co2_lgm"] = window_mean(c, 19, 23)
    n["co2_preind"] = window_mean(c, 0.2, 2)
    n["gi17_layers_uncertain"] = uncertain_layers(1287)
    n["gi17_random"] = random_error(1287)
    a = GICC05
    n["thick_ydpb_gi1_cm"] = 100 * (a[1][3] - a[0][3]) / (a[1][1] - a[0][1])
    n["thick_gi16_gi17_cm"] = 100 * (a[17][3] - a[16][3]) / (a[17][1] - a[16][1])
    n["mgca_T_2p0"] = mgca_temperature(2.0)
    return n


if __name__ == "__main__":
    write_table(__file__, ("h_m", "d30", "d40", "d50"),
                [(h, round(ice_volume_shift(h, -30), 4), round(ice_volume_shift(h, -40), 4),
                  round(ice_volume_shift(h, -50), 4)) for h in range(0, 151, 5)], part="icevol")
    write_table(__file__, ("T", "dd_benthic", "mgca_pred", "mgca_fit"),
                [(T, round(benthic_offset(T), 4), round(mgca(T), 4), round(mgca(T, 0.372, 0.0936), 4))
                 for T in [x * 0.5 for x in range(-4, 61)]], part="calib")
    write_table(__file__, ("age_ka", "d18O"), [(a, d) for a, d in lr04() if a <= 800], part="lr04")
    write_table(__file__, ("age_ka", "dT"),
                [(round(a, 3), t) for i, (a, t) in enumerate(edc()) if a <= 800 and i % 2 == 0],
                part="edc")
    write_table(__file__, ("age_ka", "co2"), [(round(a, 3), v) for a, v in co2() if a <= 800],
                part="co2")
    rows, prev = [], None
    for name, age, err, depth in GICC05:
        thick = 100 * (depth - prev[3]) / (age - prev[1]) if prev else "nan"
        rows.append((age / 1000.0, depth, err, round(random_error(err), 2),
                     round(thick, 3) if prev else thick))
        prev = (name, age, err, depth)
    write_table(__file__, ("age_ka", "depth_m", "err_yr", "err_random_yr", "thick_cm"), rows,
                part="gicc05")
    write_table(__file__, ("key", "value"),
                [(k, round(v, 4)) for k, v in sorted(numbers().items())], part="numbers")

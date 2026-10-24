"""The layers of the Earth, from PREM (grade 6, inside-the-earth).

The boundaries come from the shared PREM table (data/derived/prem.csv, ledger
data:prem); the radius is earth:Rmean; the crust thicknesses are Book 1's
usgs:crust-thickness row (PREM's single 24.4 km crust is a global average and
is not used for the drawing); the gradients are usgs:gradient-29.

  main table     : layer top_km bottom_km thickness_km top_pct state
  part disc      : layer r_km r_cm                    (cut-open Earth, to scale)
  part profile   : depth_km vp vs rho                 (PREM, every row)
  part geotherm  : depth_km t_low t_east t_mean t_west t_high
  part model     : item km mm                         (a 2 m model Earth)
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PREM = os.path.join(ROOT, "data", "derived", "prem.csv")

R_EARTH_KM = 6371.0          # earth:Rmean
CRUST_KM = {"oceanic": 5.0, "continental": 30.0, "mountain": 100.0}   # usgs:crust-thickness
KOLA_KM = 12.262             # sciam:kola-depth
EVEREST_KM = 8.84886         # tht:everest
SURFACE_C = 15.0             # planet:Earth.Tmean, the model's starting point
GRADIENTS = {"low": 6.0, "east": 25.0, "mean": 29.0, "west": 34.0, "high": 69.0}  # usgs:gradient-29
GEOTHERM_MAX_KM = 2.0        # the drill holes of usgs:gradient-29 reach about 2 km
DISC_R_CM = 2.8              # radius of the cut-open Earth in the figure
MODEL_DIAMETER_MM = 2000.0   # the problem's 2 m model


def prem_rows():
    with open(PREM, encoding="utf8") as f:
        return [dict(depth=float(r["depth_km"]), vp=float(r["vp_km_s"]), vs=float(r["vs_km_s"]),
                     rho=float(r["rho_g_cm3"]), region=r["region"]) for r in csv.DictReader(f)]


def boundaries(rows=None):
    """[(region, top_km, bottom_km)] in order from the surface, from PREM."""
    rows = rows or prem_rows()
    out = []
    for r in rows:
        if not out or out[-1][0] != r["region"]:
            out.append([r["region"], r["depth"], r["depth"]])
        out[-1][2] = r["depth"]
    return [tuple(x) for x in out]


def core_depths():
    """(depth of the top of the outer core, depth of the top of the inner core), km."""
    b = {name: (top, bot) for name, top, bot in boundaries()}
    return b["outer-core"][0], b["inner-core"][0]


def layers():
    """The four layers as printed: crust (USGS continental average), mantle,
    outer core, inner core; tops and bottoms in km below the surface."""
    oc, ic = core_depths()
    crust = CRUST_KM["continental"]
    return [
        ("crust", 0.0, crust, "solid"),
        ("mantle", crust, oc, "solid"),
        ("outer core", oc, ic, "liquid"),
        ("inner core", ic, R_EARTH_KM, "solid"),
    ]


def pct_of_radius(depth_km):
    return 100.0 * depth_km / R_EARTH_KM


def liquid_layers(rows=None):
    """Regions where PREM's shear-wave speed is zero: the waves that cannot
    cross a liquid do not cross them."""
    rows = rows or prem_rows()
    return sorted({r["region"] for r in rows if r["vs"] == 0.0})


def temperature(depth_km, gradient):
    return SURFACE_C + gradient * depth_km


def to_model_mm(km, diameter_mm=MODEL_DIAMETER_MM):
    return km * diameter_mm / (2.0 * R_EARTH_KM)


def model_items():
    oc, ic = core_depths()
    return [
        ("radius", R_EARTH_KM),
        ("oceanic crust", CRUST_KM["oceanic"]),
        ("continental crust", CRUST_KM["continental"]),
        ("Kola borehole", KOLA_KM),
        ("Everest", EVEREST_KM),
        ("top of outer core", oc),
        ("top of inner core", ic),
        ("inner core radius", R_EARTH_KM - ic),
    ]


if __name__ == "__main__":
    write_table(__file__, ("layer", "top_km", "bottom_km", "thickness_km", "top_pct", "state"),
                [("{%s}" % n, t, b, b - t, pct_of_radius(t), s) for n, t, b, s in layers()])
    oc, ic = core_depths()
    write_table(__file__, ("layer", "r_km", "r_cm"),
                [(n, r, DISC_R_CM * r / R_EARTH_KM) for n, r in
                 (("earth", R_EARTH_KM), ("outercore", R_EARTH_KM - oc), ("innercore", R_EARTH_KM - ic))],
                part="disc")
    write_table(__file__, ("depth_km", "vp", "vs", "rho"),
                [(r["depth"], r["vp"], r["vs"], r["rho"]) for r in prem_rows()], part="profile")
    steps = [i * 0.1 for i in range(int(GEOTHERM_MAX_KM * 10) + 1)]
    write_table(__file__, ("depth_km", "t_low", "t_east", "t_mean", "t_west", "t_high"),
                [(z,) + tuple(temperature(z, GRADIENTS[k]) for k in ("low", "east", "mean", "west", "high"))
                 for z in steps], part="geotherm")
    write_table(__file__, ("item", "km", "mm"),
                [("{%s}" % n, km, to_model_mm(km)) for n, km in model_items()], part="model")

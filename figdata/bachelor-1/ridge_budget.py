"""Ridge budget from the PB2002 boundary steps (Year 1, rifts-ridges-margins).

Every step of the PB2002 model (shared dataset pb2002-steps.csv, ledger
data:pb2002) has its end points, its class (OSR = oceanic spreading ridge,
OTF = oceanic transform fault, ...) and the relative velocity of its two
plates resolved into a divergent component div_mm_a (mm/yr).

  * the length of all spreading-ridge steps and the area of new sea floor they
    make each year, sum(length x divergence);
  * the length of all subduction steps (SUB) and the area of sea floor they consume
    each year, sum(length x convergence), the convergence being -div_mm_a;
  * the volume of crust made each year with the mean igneous thickness of the
    oceanic crust from seismic refraction, 7.1 km (ledger white:crust);
  * the offset of the Mid-Atlantic Ridge by the two Charlie-Gibbs transforms
    near 52-53 N, the summed length of their OTF steps between the North
    American and Eurasian plates;
  * back-arc spreading: the divergence of the Philippine Sea - Mariana ridge steps
    between 17.5 and 18.5 N (Mariana Trough), and the fastest divergence of the
    Tonga - Niuafo'ou and Tonga - Australia ridge steps (Lau Basin);
  * the area balance over all boundaries: the area made by every diverging step and
    the area destroyed by every converging step, whatever its class;
  * the Azores triple junction: the point where the NA-EU, NA-AF and EU-AF
    boundaries meet, and the class of the steps that leave it.

  part values  what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
STEPS = os.path.join(ROOT, "data", "derived", "pb2002-steps.csv")
R_KM = 6371.0
CRUST_KM = 7.1


def steps():
    with open(STEPS, encoding="utf8") as f:
        return list(csv.DictReader(f))


def arc_km(lat0, lon0, lat1, lon1):
    """Great-circle distance (km) between two points given in degrees."""
    p0, p1 = math.radians(lat0), math.radians(lat1)
    c = math.sin(p0) * math.sin(p1) + math.cos(p0) * math.cos(p1) * math.cos(math.radians(lon1 - lon0))
    return R_KM * math.acos(max(-1.0, min(1.0, c)))


def step_length(r):
    return arc_km(float(r["lat0"]), float(r["lon0"]), float(r["lat1"]), float(r["lon1"]))


def ridge_production(rows=None):
    """(length km, new sea floor km2/yr) of all OSR steps; converging steps add nothing."""
    rows = steps() if rows is None else rows
    length = area = 0.0
    for r in rows:
        if r["class"] != "OSR":
            continue
        ell = step_length(r)
        length += ell
        area += ell * max(0.0, float(r["div_mm_a"])) * 1e-6
    return length, area


def subduction_consumption(rows=None):
    """(length km, consumed sea floor km2/yr) of all SUB steps; diverging steps add nothing."""
    rows = steps() if rows is None else rows
    length = area = 0.0
    for r in rows:
        if r["class"] != "SUB":
            continue
        ell = step_length(r)
        length += ell
        area += ell * max(0.0, -float(r["div_mm_a"])) * 1e-6
    return length, area


def area_balance(rows=None):
    """(area made, area destroyed) per year, km2, summed over every step of every class."""
    rows = steps() if rows is None else rows
    made = lost = 0.0
    for r in rows:
        ell, v = step_length(r), float(r["div_mm_a"])
        made += ell * max(0.0, v) * 1e-6
        lost += ell * max(0.0, -v) * 1e-6
    return made, lost


def charlie_gibbs_offset(rows=None):
    """Summed length (km) and count of the NA-EU transform steps between 51.9 and 52.8 N."""
    rows = steps() if rows is None else rows
    sel = [r for r in rows if r["name"] == "NA-EU" and r["class"] == "OTF"
           and 51.9 < float(r["lat"]) < 52.8 and -36.0 < float(r["lon"]) < -29.0]
    return sum(step_length(r) for r in sel), len(sel)


def backarc_rates(rows=None):
    """(mean divergence of the PS-MA OSR steps between 17.5 and 18.5 N, fastest
    divergence of the TO-NI and TO-AU OSR steps), mm/yr."""
    rows = steps() if rows is None else rows
    mar = [float(r["div_mm_a"]) for r in rows if r["name"] == "PS-MA" and r["class"] == "OSR"
           and 17.5 <= float(r["lat"]) <= 18.5]
    lau = [float(r["div_mm_a"]) for r in rows if r["name"] in ("TO-NI", "TO-AU") and r["class"] == "OSR"]
    return sum(mar) / len(mar), max(lau)


def azores_junction(rows=None):
    """The point shared by the NA-EU, NA-AF and EU-AF boundaries, and the classes of
    the step of each boundary that touches it."""
    rows = steps() if rows is None else rows
    ends = {}
    for r in rows:
        if r["name"] not in ("NA-EU", "NA-AF", "EU-AF"):
            continue
        for k in ("0", "1"):
            p = (round(float(r["lat" + k]), 3), round(float(r["lon" + k]), 3))
            ends.setdefault(p, {})[r["name"]] = r["class"]
    shared = [(p, c) for p, c in ends.items() if len(c) == 3]
    if len(shared) != 1:
        raise ValueError("expected one triple point, found %d" % len(shared))
    return shared[0]


if __name__ == "__main__":
    rows = steps()
    length, area = ridge_production(rows)
    sub_len, sub_area = subduction_consumption(rows)
    off, n = charlie_gibbs_offset(rows)
    (lat, lon), classes = azores_junction(rows)
    mariana, lau = backarc_rates(rows)
    made, lost = area_balance(rows)
    vals = [("ridge_length_km", length), ("new_floor_km2_per_yr", area),
            ("new_crust_km3_per_yr", area * CRUST_KM),
            ("subduction_length_km", sub_len), ("consumed_km2_per_yr", sub_area),
            ("charlie_gibbs_offset_km", off), ("charlie_gibbs_steps", n),
            ("all_made_km2_per_yr", made), ("all_lost_km2_per_yr", lost),
            ("mariana_18n_mm_yr", mariana), ("lau_max_mm_yr", lau),
            ("azores_lat", lat), ("azores_lon", lon),
            ("azores_all_ridges", 1 if set(classes.values()) == {"OSR"} else 0)]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

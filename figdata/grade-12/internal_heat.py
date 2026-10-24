"""The Earth's internal heat (grade 12): heat flow, radiogenic heat back in time, the
heat budget, the cooling of the ocean floor and the time conduction would need.

Radiogenic heat by isotope. KamLAND (Gando et al. 2011, ledger kamland11:geonu): U-238
and Th-232 together release 20.0 TW today, with the Earth's Th/U mass ratio fixed at 3.9;
K-40 is known to add 4 TW. The split between U-238 and Th-232, and U-235 scaled from U-238,
use the isotopic heat generation and natural abundances of Dye (2012) Table 2 (ledger
dye12:isotopes). Half-lives from NuDat 3 (ledger nndc:halflives). Back in time each
isotope's heat grows as exp(lambda t), lambda = ln 2 / half-life (the decay law, read
backwards).

Budget: surface heat flow 46.7 TW (ledger b2dd10:continents, Davies and Davies 2010
Table 7); secular cooling = the rest.

Ocean floor: q = C / sqrt(t) with C = 490 mW m-2 Myr^0.5, used by Davies and Davies for
lithosphere younger than 66.5 Myr (ledger b2dd10:half-space).

Conduction across the mantle: t ~ L^2 / kappa, L = 2891 km (PREM mantle, ledger data:prem),
kappa = 1e-6 m2/s as in England, Molnar and Richter (2007), Table 1 (Book 3 row
england:kelvin).

  part past      t_Ga Th232 U238 K40 U235 total    radiogenic heat (TW), 0-4.5 Ga ago
  part halfspace t_Myr q                           ocean-floor heat flow (mW/m2), 0.5-180 Myr
  part budget    bar uth kuf secular surface       stacked bars: sources (1), losses (2), TW
  part numbers   key value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

# isotope: (half-life in Gyr, heat generation in microwatts per kg of the isotope)
ISOTOPES = {"Th232": (14.0, 26.28), "U238": (4.468, 95.13), "K40": (1.248, 28.47), "U235": (0.704, 568.47)}
ABUND_U238, ABUND_U235 = 0.992796, 0.007204   # natural abundance in uranium (Dye 2012)
TH_U = 3.9                                  # Th/U mass ratio used by KamLAND
KAMLAND_UTH_TW = 20.0
K40_TW = 4.0
TOTAL_TW = 46.7
CONT_MEAN, OCEAN_MEAN = 70.9, 105.4          # mW/m2
C_HALFSPACE = 490.0                         # mW m-2 Myr^0.5
AGE_LIMIT = 66.5                            # Myr
MANTLE_KM = 2891.0
KAPPA = 1.0e-6                              # m2/s
YEAR_S = 365.25 * 86400.0
K_GRANITE = 2.72                            # W/m/K (ledger roy:conductivity)
GRADIENT = 29.0                             # degC/km (ledger usgs:gradient-29, Book 1 row)
A_GRANITE, A_ULTRAMAFIC = 2.429, 0.111      # microW/m3, medians (ledger b2vila:heat-production)


def lam(name):
    return math.log(2.0) / ISOTOPES[name][0]


def per_kg_uranium():
    """Heat (microW) of U-238, U-235 and Th-232 per kg of natural uranium in the Earth."""
    return {"U238": ABUND_U238 * ISOTOPES["U238"][1], "U235": ABUND_U235 * ISOTOPES["U235"][1],
            "Th232": TH_U * ISOTOPES["Th232"][1]}


def present_tw():
    h = per_kg_uranium()
    u238 = KAMLAND_UTH_TW * h["U238"] / (h["U238"] + h["Th232"])
    return {"Th232": KAMLAND_UTH_TW - u238, "U238": u238, "K40": K40_TW,
            "U235": u238 * h["U235"] / h["U238"]}


def heat_tw(t_ga):
    """Radiogenic heat of each isotope t_ga billion years ago (TW)."""
    return {k: h * math.exp(lam(k) * t_ga) for k, h in present_tw().items()}


def total_tw(t_ga=0.0):
    return sum(heat_tw(t_ga).values())


def halfspace_q(t_myr):
    return C_HALFSPACE / math.sqrt(t_myr)


def numbers():
    n = {}
    p = present_tw()
    for k, v in p.items():
        n["now_%s_TW" % k] = v
    n["radiogenic_TW"] = total_tw(0.0)
    n["secular_TW"] = TOTAL_TW - total_tw(0.0)
    n["share_radiogenic"] = total_tw(0.0) / TOTAL_TW
    n["ratio_total_4.5Ga"] = total_tw(4.5) / total_tw(0.0)
    n["total_4.5Ga_TW"] = total_tw(4.5)
    n["total_3Ga_TW"] = total_tw(3.0)
    for k in ISOTOPES:
        n["ratio_%s_4.5Ga" % k] = math.exp(lam(k) * 4.5)
    past = heat_tw(4.5)
    n["share_U235_K40_4.5Ga"] = (past["U235"] + past["K40"]) / total_tw(4.5)
    n["q_1Myr"] = halfspace_q(1.0)
    n["q_10Myr"] = halfspace_q(10.0)
    n["q_66.5Myr"] = halfspace_q(AGE_LIMIT)
    n["age_where_q_equals_cont_Myr"] = (C_HALFSPACE / CONT_MEAN) ** 2
    t = (MANTLE_KM * 1000.0) ** 2 / KAPPA / YEAR_S
    n["conduction_time_Gyr"] = t / 1e9
    n["borehole_q_mW"] = K_GRANITE * GRADIENT
    n["granite_10km_mW"] = A_GRANITE * 1e-6 * 10000.0 * 1000.0
    n["granite_over_ultramafic"] = A_GRANITE / A_ULTRAMAFIC
    n["ktb_gradient"] = (265.0 - 10.0) / 9.101
    n["total_3Ga_ratio"] = total_tw(3.0) / total_tw(0.0)
    past3 = heat_tw(3.0)
    for k in ISOTOPES:
        n["%s_3Ga_TW" % k] = past3[k]
    n["share_U235_K40_3Ga"] = (past3["U235"] + past3["K40"]) / total_tw(3.0)
    for k, v in per_kg_uranium().items():
        n["perkgU_%s_microW" % k] = v
    return n


if __name__ == "__main__":
    rows = []
    for i in range(0, 91):
        t = i * 0.05
        h = heat_tw(t)
        rows.append((t, h["Th232"], h["U238"], h["K40"], h["U235"], sum(h.values())))
    write_table(__file__, ("t_Ga", "Th232", "U238", "K40", "U235", "total"), rows, part="past")
    write_table(__file__, ("t_Myr", "q"), [(t, halfspace_q(t)) for t in
                                           [0.5 * i for i in range(1, 20)] + list(range(10, 181, 2))],
                part="halfspace")
    p = present_tw()
    # one row per bar (1 = sources, 2 = losses), one column per stacked segment
    write_table(__file__, ("bar", "uth", "kuf", "secular", "surface"),
                [(1, p["Th232"] + p["U238"], p["K40"] + p["U235"], TOTAL_TW - total_tw(0.0), 0.0),
                 (2, 0.0, 0.0, 0.0, TOTAL_TW)], part="budget")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers", digits=5)

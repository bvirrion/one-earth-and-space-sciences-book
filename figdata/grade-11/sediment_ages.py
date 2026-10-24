"""Basement ages against distance from the ridge, South Atlantic at 30 S (grade 11,
drift-to-spreading).

Source (ledger dsdp3:table5): Deep Sea Drilling Project Leg 3, Initial Reports
volume 3, chapter 13 (Shipboard Scientific Party 1970), Table 5: for the seven
Mid-Atlantic Ridge sites, the magnetic anomaly number and its age (after Heirtzler
et al. 1968), the palaeontological age of the sediment just above the basalt and the
linear distance from the ridge axis. The test checks the rows against the ledger.

A constant half rate u makes age = distance / u: the best line through the origin
(least squares on the distance) has slope u = sum(d t) / sum(t^2) in km per Myr,
i.e. u/10 cm per year.

  part sites    site dist_km dist_err age age_err   palaeontological ages
  part magnetic site dist_km age                    magnetic ages (mid-range)
  part fit      dist_km age                         the fitted line
  part numbers  key value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

import seafloor_age  # noqa: E402

# site: (anomaly, magnetic age range Ma or None, palaeontological age Ma, error,
#        linear distance km, error)
TABLE5 = {
    16: ("5", (9, 9), 11, 1, 191, 5),
    15: ("6", (21, 21), 24, 1, 380, 10),
    18: (None, None, 26, 1, 506, 20),
    17: (None, (34, 38), 33, 2, 643, 20),
    14: ("13-14", (38, 39), 40, 1.5, 727, 10),
    19: ("21", (53, 53), 49, 1, 990, 10),
    20: ("30", (70, 72), 67, 1, 1270, 20),
}


def rate_through_origin(pairs):
    """Half rate (cm/yr) of the line distance = u * age through the origin."""
    sdt = sum(d * t for d, t in pairs)
    stt = sum(t * t for _, t in pairs)
    return sdt / stt / 10.0


def palaeo_pairs():
    return [(v[4], v[2]) for v in TABLE5.values()]


def magnetic_pairs(include_uncertain=False):
    """(distance, mid age) for the sites whose magnetic age is given; site 17's
    position in the anomaly pattern is uncertain (Table 5, note a)."""
    return [(v[4], 0.5 * (v[1][0] + v[1][1])) for s, v in TABLE5.items()
            if v[1] is not None and (include_uncertain or v[0] is not None)]


def numbers():
    up = rate_through_origin(palaeo_pairs())
    um = rate_through_origin(magnetic_pairs())
    sa = seafloor_age.numbers()
    edge = sa["east_edge_km_30s"]
    return {"rate_palaeo_cm_yr": up, "rate_magnetic_cm_yr": um,
            "full_rate_palaeo_cm_yr": 2 * up,
            "east_edge_km": edge, "east_edge_age_grid": sa["east_edge_age_30s"],
            "age_east_edge_palaeo": edge / (10.0 * up),
            "age_east_edge_magnetic": edge / (10.0 * um),
            "mean_rate_to_edge_cm_yr": edge / sa["east_edge_age_30s"] / 10.0,
            "site20_age_from_rate": TABLE5[20][4] / (10.0 * up)}


if __name__ == "__main__":
    write_table(__file__, ("site", "dist_km", "dist_err", "age", "age_err"),
                [(s, v[4], v[5], v[2], v[3]) for s, v in sorted(TABLE5.items(), key=lambda kv: kv[1][4])],
                part="sites")
    write_table(__file__, ("site", "dist_km", "age"),
                [(s, v[4], 0.5 * (v[1][0] + v[1][1])) for s, v in sorted(TABLE5.items(), key=lambda kv: kv[1][4])
                 if v[1] is not None and v[0] is not None], part="magnetic")
    u = rate_through_origin(palaeo_pairs())
    write_table(__file__, ("dist_km", "age"), [(0, 0), (1400, 1400 / (10.0 * u))], part="fit")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

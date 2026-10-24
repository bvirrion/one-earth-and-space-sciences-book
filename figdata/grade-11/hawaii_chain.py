"""Ages of the volcanoes of the Hawaiian-Emperor chain against their distance from
Kilauea (grade 11, plate-motions).

Clague and Dalrymple (1987), USGS Professional Paper 1350, chapter 1, Table 1.4
(ledger cd87:ages): distance from Kilauea along the trend of the chain (km) and best
potassium-argon age (Ma), with its uncertainty. Kahoolawe (a minimum age, '>1.03') and
Kilauea (active, 0-0.4) are listed but left out of the fits.

For a plume fixed under a plate moving at a steady speed v, a volcano built over the
plume at time t ago now lies at the distance d = v t: age = d / v. The speed is found by
the least-squares line through the origin, age = d / v, i.e.
1/v = sum(d * age) / sum(d^2) (km and Myr: v in km/Myr = mm/yr).

  part hawaiian  name dist age err    the volcanoes before the bend (d < 3400 km)
  part emperor   name dist age err    the bend (Daikakuji) and the Emperor seamounts
  part fit       dist age             the fitted line over the Hawaiian segment
  part numbers   key value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# Table 1.4: (name, distance km, age Ma, uncertainty Ma)
TABLE = [
    ("Kilauea", 0, 0.2, 0.2), ("Mauna Kea", 54, 0.375, 0.05), ("Kohala", 100, 0.43, 0.02),
    ("Haleakala", 182, 0.75, 0.04), ("Kahoolawe", 185, 1.03, 0.18), ("West Maui", 221, 1.32, 0.04),
    ("Lanai", 226, 1.28, 0.04), ("East Molokai", 256, 1.76, 0.07), ("West Molokai", 280, 1.90, 0.06),
    ("Koolau", 339, 2.6, 0.1), ("Waianae", 374, 3.7, 0.1), ("Kauai", 519, 5.1, 0.20),
    ("Niihau", 565, 4.89, 0.11), ("Kaula", 600, 4.0, 0.2), ("Nihoa", 780, 7.2, 0.3),
    ("Unnamed 20", 913, 9.2, 0.8), ("Necker", 1058, 10.3, 0.4), ("La Perouse Pinnacles", 1209, 12.0, 0.4),
    ("Brooks Bank", 1256, 13.0, 0.6), ("Gardner Pinnacles", 1435, 12.3, 1.0), ("Laysan", 1818, 19.9, 0.3),
    ("Northampton Bank", 1841, 26.6, 2.7), ("Pearl and Hermes Reef", 2281, 20.6, 0.5),
    ("Midway", 2432, 27.7, 0.6), ("Unnamed 57", 2600, 28.0, 0.4), ("Unnamed 63", 2825, 27.4, 0.5),
    ("Colahan", 3128, 38.6, 0.3), ("Abbott", 3280, 38.7, 0.9), ("Daikakuji", 3493, 42.4, 2.3),
    ("Yuryaku", 3520, 43.4, 1.6), ("Kimmei", 3668, 39.9, 1.2), ("Koko (southern)", 3758, 48.1, 0.8),
    ("Ojin", 4102, 55.2, 0.7), ("Jingu", 4175, 55.4, 0.9), ("Nintoku", 4452, 56.2, 0.6),
    ("Suiko (southern)", 4794, 59.6, 0.6), ("Suiko (central)", 4860, 64.7, 1.1),
]
EXCLUDED = ("Kilauea", "Kahoolawe")
BEND_KM = 3400                 # the bend lies between Abbott (3280) and Daikakuji (3493)


def segment(hawaiian=True):
    return [r for r in TABLE if r[0] not in EXCLUDED and ((r[1] < BEND_KM) == hawaiian)]


def speed_through_origin(rows):
    """v (km/Myr = mm/yr) of the line age = d / v through the origin."""
    return sum(d * d for _, d, _, _ in rows) / sum(d * a for _, d, a, _ in rows)


def numbers():
    h = segment(True)
    e = segment(False)
    return {"v_hawaiian": speed_through_origin(h), "v_all": speed_through_origin(h + e),
            "v_emperor_free": _slope_speed(e), "n_hawaiian": len(h), "n_emperor": len(e),
            "midway_speed": 2432 / 27.7, "kauai_speed": 519 / 5.1}


def _slope_speed(rows):
    """Speed from the free least-squares line age = a + d / v over the rows."""
    n = len(rows)
    md = sum(r[1] for r in rows) / n
    ma = sum(r[2] for r in rows) / n
    b = sum((r[1] - md) * (r[2] - ma) for r in rows) / sum((r[1] - md) ** 2 for r in rows)
    return 1 / b


if __name__ == "__main__":
    hd = ("name", "dist", "age", "err")
    q = lambda rows: [(n.replace(" (", "-").replace(")", "").replace(" ", "-"), d, a, s)
                      for n, d, a, s in rows]
    write_table(__file__, hd, q(segment(True)), part="hawaiian")
    write_table(__file__, hd, q(segment(False)), part="emperor")
    v = speed_through_origin(segment(True))
    write_table(__file__, ("dist", "age"), [(0, 0), (3500, 3500 / v)], part="fit")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

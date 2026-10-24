"""Where large earthquakes happen (grade 7, plate-tectonics).

The share of the M >= 6 earthquakes of 1976-2025 (USGS ComCat, ledger
data:usgs-comcat) whose epicentre lies within DIST_KM of a PB2002 plate
boundary (Bird 2003, data:pb2002), measured along the Earth's surface to the
nearest boundary vertex (vertices are ~30-100 km apart, so the distance is
slightly overestimated: the share is a lower bound). Also writes the decimated
map tables: M >= 6.5 for the world map.

  part a: one row, n_total n_near share_percent dist_km
  part bands: dist_km n_near share_percent for 100, 300 and 500 km (exercise 12)
  part map: lon lat mag   (M >= 6.5)
"""
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R_KM = 6371.0          # ledger earth:Rmean
DIST_KM = 300.0
BANDS_KM = (100.0, 300.0, 500.0)


def _read(name):
    with open(os.path.join(ROOT, "data", "derived", name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


def nearest_boundary_km(qlat, qlon, blat, blon):
    """Great-circle distance (km) from each quake to its nearest boundary vertex."""
    out = np.empty(len(qlat))
    bl, bo = np.radians(blat), np.radians(blon)
    for k in range(0, len(qlat), 500):
        la = np.radians(qlat[k:k + 500])[:, None]
        lo = np.radians(qlon[k:k + 500])[:, None]
        h = (np.sin((bl - la) / 2) ** 2 + np.cos(la) * np.cos(bl) * np.sin((bo - lo) / 2) ** 2)
        out[k:k + 500] = (2 * R_KM * np.arcsin(np.sqrt(np.clip(h, 0, 1)))).min(axis=1)
    return out


def share_near(dist_km=DIST_KM):
    q = _read("usgs-m6")
    b = _read("pb2002")
    d = nearest_boundary_km(np.array([float(e["lat"]) for e in q]), np.array([float(e["lon"]) for e in q]),
                            np.array([float(p["lat"]) for p in b]), np.array([float(p["lon"]) for p in b]))
    n_near = int((d <= dist_km).sum())
    return len(q), n_near, 100.0 * n_near / len(q)


if __name__ == "__main__":
    n, near, pct = share_near()
    write_table(__file__, ("n_total", "n_near", "share_percent", "dist_km"), [(n, near, round(pct, 1), DIST_KM)],
                part="a")
    rows = []
    for dk in BANDS_KM:
        _, nb, pb = share_near(dk)
        rows.append((dk, nb, round(pb, 1)))
    write_table(__file__, ("dist_km", "n_near", "share_percent"), rows, part="bands")
    write_table(__file__, ("lon", "lat", "mag"),
                [(float(e["lon"]), float(e["lat"]), float(e["mag"])) for e in _read("usgs-m6")
                 if float(e["mag"]) >= 6.5], part="map")

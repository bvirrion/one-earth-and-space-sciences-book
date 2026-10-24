"""Spectral signatures (Year 3, remote sensing): five laboratory reflectance spectra
and what the bands of a multispectral sensor see of them.

Spectra: ECOSTRESS Spectral Library v1.0 (data/derived/bachelor-3-eco-*.csv, ledger
data:b5-ecostress): green rye grass, tap water, a brown sand soil, kaolinite and
haematite powders, reflectance as a fraction. Bands: Landsat 8/9 OLI bands 2-7 and
TIRS band 10 (ledger usgs:landsat8-bands).

Band value: the mean of the spectrum over the band's interval (a flat spectral
response, the simplest model of a filter). NDVI = (NIR - red)/(NIR + red) from OLI
bands 5 and 4. Thermal emissivity in TIRS band 10 by Kirchhoff's law for an opaque
sample, e = 1 - R (the physics books), for the three spectra that extend to 14 um.

  part spectra  um grass water soil kaol hem   0.40-2.50 um every 0.01 um (linear interp.)
  part bands    band lo hi mid                 the OLI bands drawn on the figure
  part means    band grass water soil kaol hem band means
  part values   what value
"""
import csv
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

MATERIALS = ("grass", "water", "soil", "kaolinite", "hematite")
SHORT = {"grass": "grass", "water": "water", "soil": "soil", "kaolinite": "kaol",
         "hematite": "hem"}
# Landsat 8 OLI (and TIRS band 10), micrometres, from the USGS Landsat 8 page
OLI = {"B2": (0.450, 0.51), "B3": (0.53, 0.59), "B4": (0.64, 0.67), "B5": (0.85, 0.88),
       "B6": (1.57, 1.65), "B7": (2.11, 2.29)}
TIRS10 = (10.6, 11.19)


def read(name):
    path = os.path.join(ROOT, "data", "derived", "bachelor-3-eco-%s.csv" % name)
    with open(path, encoding="utf8") as f:
        rows = [(float(r["um"]), float(r["refl"])) for r in csv.DictReader(f)]
    um = np.array([a for a, _ in rows])
    r = np.array([b for _, b in rows])
    return um, r


def band_mean(um, r, lo, hi):
    m = (um >= lo) & (um <= hi)
    if not m.any():
        return float("nan")
    return float(r[m].mean())


def ndvi(nir, red):
    return (nir - red) / (nir + red)


def means():
    out = {}
    for name in MATERIALS:
        um, r = read(name)
        out[name] = {b: band_mean(um, r, lo, hi) for b, (lo, hi) in OLI.items()}
        out[name]["T10"] = band_mean(um, r, *TIRS10)
    return out


def main():
    grid = np.round(np.arange(0.40, 2.5001, 0.01), 2)
    cols = []
    for name in MATERIALS:
        um, r = read(name)
        cols.append(np.interp(grid, um, r))
    write_table(__file__, ("um",) + tuple(SHORT[n] for n in MATERIALS),
                [(g,) + tuple(c[i] for c in cols) for i, g in enumerate(grid)], part="spectra")
    write_table(__file__, ("band", "lo", "hi", "mid"),
                [(b[1:], lo, hi, 0.5 * (lo + hi)) for b, (lo, hi) in OLI.items()], part="bands")
    m = means()
    write_table(__file__, ("band",) + tuple(SHORT[n] for n in MATERIALS),
                [(b,) + tuple(m[n][b] for n in MATERIALS) for b in list(OLI) + ["T10"]],
                part="means")
    vals = []
    for n in MATERIALS:
        vals.append(["ndvi_" + n, ndvi(m[n]["B5"], m[n]["B4"])])
    for n in ("grass", "water", "soil"):
        vals.append(["emis_t10_" + n, 1.0 - m[n]["T10"]])
    um, r = read("kaolinite")
    w = (um > 2.1) & (um < 2.3)
    vals.append(["kaol_min_um", float(um[w][np.argmin(r[w])])])
    um, r = read("grass")
    vals.append(["grass_red_edge_um", float(np.interp(0.5 * (m["grass"]["B4"] + m["grass"]["B5"]),
                                                      r[(um > 0.68) & (um < 0.78)],
                                                      um[(um > 0.68) & (um < 0.78)]))])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

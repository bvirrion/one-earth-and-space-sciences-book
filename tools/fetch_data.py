#!/usr/bin/env python3
"""Shared real-world datasets: fetch the raw files, derive small tidy tables.

    python3 tools/fetch_data.py fetch [id ...]    # network: data/raw/<id>.<ext>
    python3 tools/fetch_data.py derive [id ...]   # offline: data/derived/<id>.csv
    python3 tools/fetch_data.py list

Every dataset is a row of DATASETS below: its URL, its licence or terms, and the
ledger row (sources/data_ledger.md) that cites it. `fetch` records the access
date, size and sha256 of each raw file in data/MANIFEST.md; `derive` turns a raw
file into a small CSV under data/derived/ that the figdata scripts read. Only
data/derived/ and data/MANIFEST.md are kept in the repository (data/raw/ is
ignored), so `make figdata` never needs the network.

Rules (sources/BATCH_BOOKS_1-5.md): the User-Agent names the project and its
site and carries NO e-mail address; a source that demands one is not used. A
dataset used by one book only may be added here by that book's agent, with an
id that starts with its year (`bachelor-2-...`).
"""
import csv
import datetime
import hashlib
import io
import json
import math
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
DERIVED = os.path.join(ROOT, "data", "derived")
MANIFEST = os.path.join(ROOT, "data", "MANIFEST.md")
UA = "OneCourseBooks/1.0 (+https://one-course.com)"

DATASETS = {
    "ne-land-110m": dict(
        url="https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_land.geojson",
        ext="geojson", ledger="data:ne-land",
        terms="Natural Earth, public domain (naturalearthdata.com/about/terms-of-use)"),
    "ne-land-50m": dict(
        url="https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_land.geojson",
        ext="geojson", ledger="data:ne-land",
        terms="Natural Earth, public domain"),
    "pb2002": dict(
        url="https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json",
        ext="geojson", ledger="data:pb2002",
        terms="Bird (2003) PB2002 model, GeoJSON conversion by H. Ahlenius (fraxen/tectonicplates), "
              "Open Data Commons Attribution License (ODC-By 1.0): credit in the caption"),
    "pb2002-steps": dict(
        url="https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_steps.json",
        ext="geojson", ledger="data:pb2002",
        terms="as pb2002"),
    "etopo-1deg": dict(
        url="https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?"
            "altitude%5B(-89.5):60:(89.5)%5D%5B(-179.5):60:(179.5)%5D",
        ext="csv", ledger="data:etopo1",
        terms="NOAA NCEI ETOPO1 (Amante and Eakins 2009), sampled every 60th node (1 degree) "
              "by NOAA ERDDAP; US Government work, public domain"),
    "usgs-m6": dict(
        url="https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&orderby=time-asc"
            "&starttime=1976-01-01&endtime=2026-01-01&minmagnitude=6",
        ext="csv", ledger="data:usgs-comcat",
        terms="USGS ANSS Comprehensive Catalog (ComCat), US Government work, public domain"),
    "gvp-holocene": dict(
        url="https://webservices.volcano.si.edu/geoserver/GVP-VOTW/ows?service=WFS&version=2.0.0"
            "&request=GetFeature&typeName=GVP-VOTW:Smithsonian_VOTW_Holocene_Volcanoes&outputFormat=csv",
        ext="csv", ledger="data:gvp",
        terms="Global Volcanism Program, Smithsonian Institution, Volcanoes of the World: "
              "locations and types only (facts), cited; no text or photograph reused"),
    "prem": dict(
        url="https://raw.githubusercontent.com/obspy/obspy/master/obspy/taup/data/prem.nd",
        ext="nd", ledger="data:prem",
        terms="PREM, Dziewonski and Anderson (1981), isotropic, 1 s reference period, "
              "as tabulated in ObsPy's TauP model file (values are the published model)"),
    "co2-mlo-monthly": dict(
        url="https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.txt",
        ext="txt", ledger="data:co2-mlo",
        terms="NOAA GML (Lan, Tans and Thoning) and Scripps (Keeling), public domain; "
              "acknowledge NOAA GML"),
    "co2-mlo-annual": dict(
        url="https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt",
        ext="txt", ledger="data:co2-mlo", terms="as co2-mlo-monthly"),
    "gistemp": dict(
        url="https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv",
        ext="csv", ledger="data:gistemp",
        terms="NASA GISS Surface Temperature Analysis v4 (GISTEMP Team; Lenssen et al. 2019), "
              "public domain"),
    "co2-icecore": dict(
        url="https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/antarctica2015co2composite.txt",
        ext="txt", ledger="data:co2-bereiter",
        terms="Bereiter et al. (2015) Antarctic CO2 composite, NOAA NCEI Paleoclimatology, "
              "public domain with citation"),
    "edc-temperature": dict(
        url="https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/epica_domec/edc3deuttemp2007.txt",
        ext="txt", ledger="data:edc-jouzel",
        terms="Jouzel et al. (2007) EPICA Dome C deuterium and temperature, NOAA NCEI "
              "Paleoclimatology, public domain with citation"),
    "lr04": dict(
        url="https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/lisiecki2005/lisiecki2005.txt",
        ext="txt", ledger="data:lr04",
        terms="Lisiecki and Raymo (2005) LR04 benthic d18O stack, NOAA NCEI Paleoclimatology, "
              "public domain with citation"),
    "gmsl-altimetry": dict(
        url="https://www.star.nesdis.noaa.gov/socd/lsa/SeaLevelRise/slr/slr_sla_gbl_free_ref_90.csv",
        ext="csv", ledger="data:gmsl-lsa",
        terms="NOAA Laboratory for Satellite Altimetry, public domain; acknowledgment "
              "'Altimetry data are provided by NOAA Laboratory for Satellite Altimetry.'"),
}


# ----------------------------------------------------------------------------
# fetch
# ----------------------------------------------------------------------------
def raw_path(key):
    return os.path.join(RAW, "%s.%s" % (key, DATASETS[key]["ext"]))


def fetch(key):
    d = DATASETS[key]
    req = urllib.request.Request(d["url"], headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=300) as r:
        body = r.read()
    os.makedirs(RAW, exist_ok=True)
    with open(raw_path(key), "wb") as f:
        f.write(body)
    sha = hashlib.sha256(body).hexdigest()
    today = datetime.date.today().isoformat()
    rows = _manifest_rows()
    rows[key] = (today, str(len(body)), sha, d["url"], d["terms"], d["ledger"])
    _write_manifest(rows)
    print("  %-18s %9d bytes  %s" % (key, len(body), sha[:12]))


def _manifest_rows():
    rows = {}
    if os.path.exists(MANIFEST):
        for line in open(MANIFEST, encoding="utf8"):
            if line.startswith("| ") and not line.startswith("| id ") and not line.startswith("|---"):
                c = [x.strip() for x in line.strip().strip("|").split("|")]
                if len(c) == 7:
                    rows[c[0].strip("`")] = tuple(c[1:])
    return rows


def _write_manifest(rows):
    with open(MANIFEST, "w", encoding="utf8") as f:
        f.write("# Raw data manifest\n\nWritten by `tools/fetch_data.py fetch`: one row per raw file "
                "(data/raw/ is not kept in the repository). The access date is the ledger's access "
                "date; the sha256 lets a later fetch tell whether the source changed.\n\n"
                "| id | accessed | bytes | sha256 | url | terms | ledger |\n"
                "|---|---|---|---|---|---|---|\n")
        for k in sorted(rows):
            f.write("| `%s` | %s |\n" % (k, " | ".join(rows[k])))


# ----------------------------------------------------------------------------
# derive: raw -> data/derived/<id>.csv (small, tidy, stable)
# ----------------------------------------------------------------------------
def _write_csv(name, header, rows):
    os.makedirs(DERIVED, exist_ok=True)
    with open(os.path.join(DERIVED, name + ".csv"), "w", encoding="utf8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)
    print("  %-22s %6d rows" % (name, len(rows)))


def _rings(geom):
    if geom["type"] == "Polygon":
        return geom["coordinates"]
    if geom["type"] == "MultiPolygon":
        return [r for poly in geom["coordinates"] for r in poly]
    if geom["type"] == "LineString":
        return [geom["coordinates"]]
    if geom["type"] == "MultiLineString":
        return geom["coordinates"]
    return []


def derive_land(key):
    """Every ring of the land polygons: ring, lon, lat (5 decimals)."""
    gj = json.load(open(raw_path(key), encoding="utf8"))
    rows, n = [], 0
    for feat in gj["features"]:
        for ring in _rings(feat["geometry"]):
            n += 1
            rows += [(n, "%.5f" % p[0], "%.5f" % p[1]) for p in ring]
    _write_csv(key, ("ring", "lon", "lat"), rows)


def derive_pb2002(key):
    """Plate boundaries: segment, name (e.g. AF-AN), lon, lat."""
    gj = json.load(open(raw_path(key), encoding="utf8"))
    rows, n = [], 0
    for feat in gj["features"]:
        name = feat["properties"].get("Name", "")
        for line in _rings(feat["geometry"]):
            n += 1
            rows += [(n, name, "%.4f" % p[0], "%.4f" % p[1]) for p in line]
    _write_csv(key, ("segment", "name", "lon", "lat"), rows)


def derive_pb2002_steps(key):
    """One row per PB2002 step: midpoint, class (SUB, OSR, OTF, CRB, CTF, CCB, OCB),
    the relative velocity (mm/a) and its azimuth, its divergent component (+ opening,
    - closing) and its right-lateral component, as published in the steps table
    (Bird 2003: PB2002_steps, fields VELOCITYLE, VELOCITYAZ, VELOCITYDI, VELOCITYRI)."""
    gj = json.load(open(raw_path(key), encoding="utf8"))
    rows = []
    for feat in gj["features"]:
        pr = feat["properties"]
        coords = _rings(feat["geometry"])[0]
        lon = (coords[0][0] + coords[-1][0]) / 2
        lat = (coords[0][1] + coords[-1][1]) / 2
        rows.append((pr["PLATEBOUND"], pr["STEPCLASS"], "%.3f" % lon, "%.3f" % lat,
                     "%.3f" % pr["STARTLONG"], "%.3f" % pr["STARTLAT"],
                     "%.3f" % pr["FINALLONG"], "%.3f" % pr["FINALLAT"],
                     "%.1f" % pr["VELOCITYLE"], "%.0f" % pr["VELOCITYAZ"],
                     "%.1f" % pr["VELOCITYDI"], "%.1f" % pr["VELOCITYRI"]))
    _write_csv(key, ("name", "class", "lon", "lat", "lon0", "lat0", "lon1", "lat1",
                     "vel_mm_a", "vel_az", "div_mm_a", "rslip_mm_a"), rows)


def derive_etopo(key):
    """lat, lon, elevation (m) on the 1-degree grid (cell centres)."""
    rows = []
    with open(raw_path(key), encoding="utf8") as f:
        r = csv.reader(f)
        next(r); next(r)                       # ERDDAP: names, then units
        for lat, lon, alt in r:
            rows.append(("%.1f" % float(lat), "%.1f" % float(lon), "%d" % round(float(alt))))
    _write_csv(key, ("lat", "lon", "elev_m"), rows)


def derive_usgs(key):
    rows = []
    with open(raw_path(key), encoding="utf8") as f:
        for e in csv.DictReader(f):
            if e["type"] != "earthquake":
                continue
            rows.append((e["time"][:10], "%.3f" % float(e["latitude"]), "%.3f" % float(e["longitude"]),
                         "%.1f" % float(e["depth"]), "%.1f" % float(e["mag"]), e["magType"]))
    _write_csv(key, ("date", "lat", "lon", "depth_km", "mag", "mag_type"), rows)


def derive_gvp(key):
    rows = []
    with open(raw_path(key), encoding="utf8") as f:
        for v in csv.DictReader(f):
            rows.append((v["Volcano_Number"], v["Volcano_Name"], "%.3f" % float(v["Latitude"]),
                         "%.3f" % float(v["Longitude"]), v["Elevation"], v["Primary_Volcano_Type"],
                         v["Tectonic_Setting"], v["Last_Eruption_Year"]))
    rows.sort(key=lambda r: int(r[0]))
    _write_csv(key, ("number", "name", "lat", "lon", "elev_m", "type", "setting", "last_eruption"), rows)


def derive_prem(key):
    """depth_km, vp, vs (km/s), rho (g/cm3); discontinuities appear twice."""
    rows, region = [], "crust"
    for line in open(raw_path(key), encoding="utf8"):
        t = line.split()
        if len(t) == 1:
            region = t[0]
            continue
        if len(t) >= 4:
            rows.append(("%.2f" % float(t[0]), t[1], t[2], t[3], region))
    _write_csv(key, ("depth_km", "vp_km_s", "vs_km_s", "rho_g_cm3", "region"), rows)


def derive_co2_monthly(key):
    rows = []
    for line in open(raw_path(key), encoding="utf8"):
        if line.startswith("#") or not line.strip():
            continue
        t = line.split()
        # year month decimal average deseasonalized ndays sdev unc
        rows.append((t[0], t[1], t[2], t[3], t[4]))
    _write_csv(key, ("year", "month", "decimal_year", "co2_ppm", "co2_deseason_ppm"), rows)


def derive_co2_annual(key):
    rows = []
    for line in open(raw_path(key), encoding="utf8"):
        if line.startswith("#") or not line.strip():
            continue
        t = line.split()
        rows.append((t[0], t[1], t[2]))
    _write_csv(key, ("year", "co2_ppm", "unc_ppm"), rows)


def derive_gistemp(key):
    """Annual global mean (J-D), deg C relative to 1951-1980."""
    rows = []
    lines = open(raw_path(key), encoding="utf8").read().splitlines()
    r = csv.reader(lines[1:])
    head = next(r)
    jd = head.index("J-D")
    for t in r:
        if t[jd].strip() not in ("***", ""):
            rows.append((t[0], t[jd]))
    _write_csv(key, ("year", "anomaly_C_1951_1980"), rows)


def _numeric_block(path, ncols, start_marker=None):
    """Rows of a NOAA paleo text file that are all numbers (after a marker)."""
    out, on = [], start_marker is None
    for line in open(path, encoding="latin-1"):
        if not on:
            on = start_marker in line
            continue
        t = line.split()
        if len(t) < ncols:
            continue
        try:
            out.append([float(x) for x in t[:ncols]])
        except ValueError:
            continue
    return out


def derive_co2_icecore(key):
    """age (years before 1950), CO2 (ppm), 1-sigma (ppm)."""
    rows = _numeric_block(raw_path(key), 3, start_marker="age_gas_calBP")
    _write_csv(key, ("age_yr_bp", "co2_ppm", "sigma_ppm"),
               [("%.1f" % a, "%.2f" % c, "%.2f" % s) for a, c, s in rows])


def derive_edc(key):
    """depth, age (years before 1950), deuterium (permil), temperature anomaly (C)."""
    rows = []
    for t in _numeric_block(raw_path(key), 5, start_marker="Bag"):
        bag, depth, age, dd, temp = t
        if not math.isnan(temp):
            rows.append(("%.2f" % depth, "%.1f" % age, "%.1f" % dd, "%.2f" % temp))
    _write_csv(key, ("depth_m", "age_yr_bp", "dD_permil", "temp_anomaly_C"), rows)


def derive_lr04(key):
    """age (ka), benthic d18O (permil), standard error."""
    rows = _numeric_block(raw_path(key), 3, start_marker="Time (ka)")
    # the NOAA file appends further numeric blocks after the stack (Book 2
    # report, 2026-10-23): keep the stack only, up to the first age decrease
    for i in range(1, len(rows)):
        if rows[i][0] < rows[i - 1][0]:
            rows = rows[:i]
            break
    _write_csv(key, ("age_ka", "d18O_permil", "se_permil"),
               [("%g" % a, "%.3f" % d, "%.3f" % s) for a, d, s in rows])


def derive_gmsl(key):
    """decimal year, sea-level anomaly (mm), whichever mission reports it."""
    rows = []
    for line in open(raw_path(key), encoding="utf8"):
        if line.startswith("#") or line.startswith("year"):
            continue
        t = line.strip().split(",")
        vals = [x for x in t[1:] if x.strip()]
        if vals:
            rows.append(("%.4f" % float(t[0]), "%.2f" % float(vals[0])))
    _write_csv(key, ("decimal_year", "gmsl_mm"), rows)


DERIVE = {
    "ne-land-110m": derive_land, "ne-land-50m": derive_land,
    "pb2002": derive_pb2002, "pb2002-steps": derive_pb2002_steps,
    "etopo-1deg": derive_etopo, "usgs-m6": derive_usgs, "gvp-holocene": derive_gvp,
    "prem": derive_prem, "co2-mlo-monthly": derive_co2_monthly,
    "co2-mlo-annual": derive_co2_annual, "gistemp": derive_gistemp,
    "co2-icecore": derive_co2_icecore, "edc-temperature": derive_edc,
    "lr04": derive_lr04, "gmsl-altimetry": derive_gmsl,
}


def main(argv):
    if not argv or argv[0] not in ("fetch", "derive", "list"):
        print(__doc__)
        return 2
    keys = argv[1:] or sorted(DATASETS)
    for k in keys:
        if k not in DATASETS:
            print("unknown dataset: %s" % k)
            return 2
    if argv[0] == "list":
        for k in keys:
            print("%-18s %s" % (k, DATASETS[k]["terms"]))
        return 0
    for k in keys:
        if argv[0] == "fetch":
            fetch(k)
        else:
            DERIVE[k](k)
    return 0


# ============================================================================
# Book 1: datasets used by Book 1 only (grades 1-9). Ids start with the year.
# Added by the Book 1 agent, 2026-10-22 (sources/BATCH_BOOKS_1-5.md, Sync 1).
# ============================================================================
_NE = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/"
_NORMALS = "https://www.ncei.noaa.gov/data/normals-monthly/1991-2020/access/%s.csv"
_NORMALS_TERMS = ("NOAA NCEI U.S. Climate Normals 1991-2020, monthly (Arguez et al.), "
                  "US Government work, public domain")
_B1_STATIONS = {  # station ids verified in the files' STATION and NAME columns
    "grade-5-normals-phoenix": "USW00023183",    # PHOENIX SKY HARBOR INTL AP, AZ US
    "grade-5-normals-utqiagvik": "USW00027502",  # BARROW POST ROGERS AP, AK US
    "grade-5-normals-hilo": "USW00021504",       # HILO INTL AP, HI US
    "grade-5-normals-seattle": "USW00024233",    # SEATTLE TACOMA INTL AP, WA US
}
for _k, _s in _B1_STATIONS.items():
    DATASETS[_k] = dict(url=_NORMALS % _s, ext="csv", ledger="data:b1-noaa-normals",
                        terms=_NORMALS_TERMS)
DATASETS.update({
    "grade-8-nsidc-sep-extent": dict(
        url="https://noaadata.apps.nsidc.org/NOAA/G02135/north/monthly/data/N_09_extent_v4.0.csv",
        ext="csv", ledger="data:b1-nsidc-sea-ice",
        terms="NSIDC Sea Ice Index G02135 v4 (Fetterer et al. 2025, doi:10.7265/a98x-0f50); "
              "free to use, citation required (cited in the caption and the credits)"),
    "grade-4-ne-rivers": dict(
        url=_NE + "ne_110m_rivers_lake_centerlines.geojson", ext="geojson",
        ledger="data:b1-ne-rivers", terms="Natural Earth, public domain"),
    "grade-4-ne-lakes": dict(
        url=_NE + "ne_110m_lakes.geojson", ext="geojson",
        ledger="data:b1-ne-rivers", terms="Natural Earth, public domain"),
    "grade-6-ne-places": dict(
        url=_NE + "ne_110m_populated_places_simple.geojson", ext="geojson",
        ledger="data:b1-ne-places", terms="Natural Earth, public domain"),
})


def derive_b1_normals(key):
    """month, mean temperature (deg C), precipitation (mm) from the NOAA monthly normals
    (published in deg F and inches)."""
    rows = []
    for r in csv.DictReader(open(raw_path(key), encoding="utf8")):
        t_f = float(r["MLY-TAVG-NORMAL"])
        p_in = float(r["MLY-PRCP-NORMAL"])
        rows.append((int(r["DATE"]), "%.1f" % ((t_f - 32.0) * 5.0 / 9.0), "%.1f" % (p_in * 25.4)))
    _write_csv(key, ("month", "tavg_C", "prcp_mm"), rows)


def derive_b1_nsidc(key):
    """year, September mean Arctic sea-ice extent (million km2); missing years skipped."""
    rows = []
    for line in open(raw_path(key), encoding="utf8").read().splitlines()[1:]:
        c = [x.strip() for x in line.split(",")]
        if len(c) >= 5 and float(c[4]) > 0:
            rows.append((int(c[0]), "%.2f" % float(c[4])))
    _write_csv(key, ("year", "extent_Mkm2"), rows)


def derive_b1_lines(key):
    """Every line or ring of a Natural Earth layer: ring, name, scalerank, lon, lat."""
    gj = json.load(open(raw_path(key), encoding="utf8"))
    rows, n = [], 0
    for feat in gj["features"]:
        p = feat["properties"]
        name = (p.get("name") or p.get("NAME") or "").replace(",", " ")
        rank = p.get("scalerank", p.get("SCALERANK", ""))
        for ring in _rings(feat["geometry"]):
            n += 1
            rows += [(n, name, rank, "%.4f" % q[0], "%.4f" % q[1]) for q in ring]
    _write_csv(key, ("ring", "name", "scalerank", "lon", "lat"), rows)


def derive_b1_places(key):
    """name, adm0name, lon, lat, pop_max of the Natural Earth 1:110m populated places."""
    gj = json.load(open(raw_path(key), encoding="utf8"))
    rows = []
    for feat in gj["features"]:
        p = feat["properties"]
        lon, lat = feat["geometry"]["coordinates"][:2]
        rows.append(((p.get("name") or "").replace(",", " "),
                     (p.get("adm0name") or "").replace(",", " "),
                     "%.4f" % lon, "%.4f" % lat, int(p.get("pop_max") or 0)))
    rows.sort()
    _write_csv(key, ("name", "country", "lon", "lat", "pop_max"), rows)


for _k in _B1_STATIONS:
    DERIVE[_k] = derive_b1_normals
DERIVE.update({
    "grade-8-nsidc-sep-extent": derive_b1_nsidc,
    "grade-4-ne-rivers": derive_b1_lines, "grade-4-ne-lakes": derive_b1_lines,
    "grade-6-ne-places": derive_b1_places,
})
# ============================================================================
# end of Book 1 block
# ============================================================================

# ============================================================================
# Book 2: datasets used by Book 2 only (grades 10-12). Ids start with the year.
# Added by the Book 2 agent, 2026-10-22 (sources/BATCH_BOOKS_1-5.md, Sync 1).
# ============================================================================
_IBTRACS = ("https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-"
            "stewardship-ibtracs/v04r01/access/csv/ibtracs.since1980.list.v04r01.csv")
DATASETS.update({
    "grade-10-ibtracs": dict(
        url=_IBTRACS, ext="csv", ledger="data:b2-ibtracs",
        terms="IBTrACS v04r01, NOAA NCEI (Gahtan et al. 2024, doi:10.25921/82ty-9e16; "
              "Knapp et al. 2010, doi:10.1175/2009BAMS2755.1); developed for research, commercial "
              "use guided by WMO Resolution 40 (free exchange of essential data); used non-"
              "commercially, cited in the caption and the credits; raw file 145 MB, not kept"),
})


def _b2_float(x):
    x = x.strip()
    return float(x) if x else None


def derive_b2_ibtracs(key):
    """Two small tables from the 145 MB IBTrACS file (main tracks, tropical storms and
    stronger only, i.e. lifetime maximum USA_WIND >= 34 kt):
    grade-10-ibtracs.csv: sid, season, basin, lat, lon at 00 UTC of each day;
    grade-10-ibtracs-storms.csv: sid, season, basin, name, first record lat/lon, position
    where the USA wind first reaches 34 kt (tropical-storm strength), lifetime maximum wind
    (kt, USA 1-minute) and minimum pressure (hPa, USA, else WMO)."""
    storms, order = {}, []
    with open(raw_path(key), encoding="utf8", newline="") as f:
        rd = csv.reader(f)
        head = next(rd)
        next(rd)                                   # units row
        ix = {h: i for i, h in enumerate(head)}
        for r in rd:
            if r[ix["TRACK_TYPE"]].strip() != "main":
                continue
            sid = r[ix["SID"]]
            s = storms.get(sid)
            if s is None:
                s = storms[sid] = dict(season=int(r[ix["SEASON"]]), basin=r[ix["BASIN"]].strip() or "NA",
                                       name=r[ix["NAME"]].strip().replace(",", " "), pts=[],
                                       lat0=float(r[ix["LAT"]]), lon0=float(r[ix["LON"]]),
                                       wmax=None, pmin=None, ts=None)
                order.append(sid)
            w = _b2_float(r[ix["USA_WIND"]])
            p = _b2_float(r[ix["USA_PRES"]]) or _b2_float(r[ix["WMO_PRES"]])
            if w is not None and w >= 34 and s["ts"] is None:
                s["ts"] = (float(r[ix["LAT"]]), float(r[ix["LON"]]))
            if w is not None and (s["wmax"] is None or w > s["wmax"]):
                s["wmax"] = w
            if p is not None and (s["pmin"] is None or p < s["pmin"]):
                s["pmin"] = p
            if r[ix["ISO_TIME"]].endswith("00:00:00"):
                s["pts"].append((float(r[ix["LAT"]]), float(r[ix["LON"]])))
    keep = [sid for sid in order if storms[sid]["wmax"] is not None and storms[sid]["wmax"] >= 34]
    rows = []
    for sid in keep:
        s = storms[sid]
        rows += [(sid, s["season"], s["basin"], "%.1f" % la, "%.1f" % lo) for la, lo in s["pts"]]
    _write_csv(key, ("sid", "season", "basin", "lat", "lon"), rows)
    srows = [(sid, storms[sid]["season"], storms[sid]["basin"], storms[sid]["name"],
              "%.1f" % storms[sid]["lat0"], "%.1f" % storms[sid]["lon0"],
              "%.1f" % storms[sid]["ts"][0], "%.1f" % storms[sid]["ts"][1],
              "%d" % storms[sid]["wmax"], "" if storms[sid]["pmin"] is None else "%d" % storms[sid]["pmin"])
             for sid in keep]
    _write_csv(key + "-storms", ("sid", "season", "basin", "name", "lat0", "lon0", "lat34", "lon34",
                                 "wmax_kt", "pmin_hpa"), srows)


DERIVE.update({"grade-10-ibtracs": derive_b2_ibtracs})

# WOA23 objectively analysed climatology at 1 deg, one depth column per site and
# variable through the NCEI THREDDS OPeNDAP ASCII service (a few kB each).
_WOA = ("https://www.ncei.noaa.gov/thredds-ocean/dodsC/woa23/DATA/%s/netcdf/decav/1.00/"
        "woa23_decav_%s%s_01.nc.ascii?%s_an%%5B0%%5D%%5B0:%d%%5D%%5B%d%%5D%%5B%d%%5D")
_WOA_TERMS = ("World Ocean Atlas 2023 (Reagan et al. 2024, NCEI Accession 0270533; Locarnini et al. "
              "2023, doi:10.25923/54bh-1613; Reagan et al. 2023, doi:10.25923/70qt-9574); file "
              "attribute: 'These data are openly available to the public', acknowledgment requested")
_B2_WOA_SITES = {  # site: (lat, lon) of the 1-degree cell centre; index = lat+89.5, lon+179.5
    "warmpool": (5.5, 150.5),       # tropical western Pacific
    "atlantic": (40.5, -30.5),      # mid-latitude North Atlantic
    "arctic": (75.5, -150.5),       # Canada Basin
    "peru": (-13.5, -77.5),         # off Peru
    "gyre": (-20.5, -110.5),        # South Pacific subtropical gyre
}
for _site, (_la, _lo) in _B2_WOA_SITES.items():
    for _var, _dir in (("t", "temperature"), ("s", "salinity")):
        DATASETS["grade-10-woa23-%s-%s" % (_site, _var)] = dict(
            url=_WOA % (_dir, _var, "00", _var, 101, int(_la + 89.5), int(_lo + 179.5)),
            ext="txt", ledger="data:b2-woa23", terms=_WOA_TERMS)
for _m in ("02", "08"):   # February and August, mid-latitude North Atlantic (57 levels)
    _la, _lo = _B2_WOA_SITES["atlantic"]
    DATASETS["grade-10-woa23-atlantic-t%s" % _m] = dict(
        url=_WOA % ("temperature", "t", _m, "t", 56, int(_la + 89.5), int(_lo + 179.5)),
        ext="txt", ledger="data:b2-woa23", terms=_WOA_TERMS)


def derive_b2_woa(key):
    """depth_m, value of one WOA23 column (deg C or practical salinity); empty levels
    (below the sea floor, fill value ~1e37) dropped."""
    import re
    txt = open(raw_path(key), encoding="utf8").read()
    vals = [float(m) for m in re.findall(r"^\[0\]\[\d+\]\[0\], (\S+)$", txt, re.M)]
    dep = re.search(r"\.depth\[\d+\]\n([^\n]+)", txt).group(1)
    deps = [float(x) for x in dep.split(",")]
    assert len(vals) == len(deps), key
    _write_csv(key, ("depth_m", "value"),
               [("%g" % d, "%.4f" % v) for d, v in zip(deps, vals) if abs(v) < 1e3])


for _k in DATASETS:
    if _k.startswith("grade-10-woa23-"):
        DERIVE[_k] = derive_b2_woa

# USGS NWIS (public domain, US Government work): station 01646500, Potomac River
# near Washington DC, Little Falls pump station -- annual peaks and one flood's
# daily mean discharge (cubic feet per second, converted to m3/s in the derive).
_NWIS_TERMS = ("USGS National Water Information System, station 01646500 (Potomac River near "
               "Washington DC, Little Falls pump station); US Government work, public domain")
DATASETS.update({
    "grade-10-usgs-potomac-peaks": dict(
        url="https://nwis.waterdata.usgs.gov/nwis/peak?site_no=01646500&agency_cd=USGS&format=rdb",
        ext="rdb", ledger="data:b2-usgs-potomac", terms=_NWIS_TERMS),
    "grade-10-usgs-potomac-dv": dict(
        url=("https://waterservices.usgs.gov/nwis/dv/?format=rdb&sites=01646500&startDT=1996-01-05"
             "&endDT=1996-02-29&parameterCd=00060&statCd=00003"),
        ext="rdb", ledger="data:b2-usgs-potomac", terms=_NWIS_TERMS),
})
_CFS = 0.3048 ** 3          # m3/s per cubic foot per second (exact)


def _rdb_rows(key):
    rows = [l.split("\t") for l in open(raw_path(key), encoding="utf8").read().splitlines()
            if l and not l.startswith("#")]
    return rows[0], rows[2:]                 # header, data (the second line is the format row)


def derive_b2_peaks(key):
    """water_year, date, peak_m3s, code: the annual peak discharges (one per water year,
    October to September); peaks without a discharge are dropped."""
    head, data = _rdb_rows(key)
    ix = {h: i for i, h in enumerate(head)}
    out = []
    for r in data:
        if not r[ix["peak_va"]].strip():
            continue
        d = r[ix["peak_dt"]]
        y, m = int(d[:4]), int(d[5:7] or 1)
        wy = y + 1 if m >= 10 else y
        out.append((wy, d, "%.0f" % (float(r[ix["peak_va"]]) * _CFS), r[ix["peak_cd"]].strip().replace(",", " ")))
    _write_csv(key, ("water_year", "date", "peak_m3s", "code"), out)


def derive_b2_dv(key):
    """date, day (from the first date), mean daily discharge (m3/s)."""
    import datetime as _dt
    head, data = _rdb_rows(key)
    col = [i for i, h in enumerate(head) if h.endswith("_00060_00003")][0]
    d0 = None
    out = []
    for r in data:
        d = _dt.date.fromisoformat(r[2])
        d0 = d0 or d
        out.append((r[2], (d - d0).days, "%.0f" % (float(r[col]) * _CFS)))
    _write_csv(key, ("date", "day", "q_m3s"), out)


DERIVE.update({"grade-10-usgs-potomac-peaks": derive_b2_peaks, "grade-10-usgs-potomac-dv": derive_b2_dv})

# Age of the ocean floor, Seton et al. (2020), version 2020.1, Gee and Kent (2007)
# timescale, 6 arc-minute NetCDF-3 grid (25 MB, not kept). Licence CC BY 4.0 (the
# Zenodo record of the data set, doi:10.5281/zenodo.5341342 lists 'cc-by-4.0').
# Derived: a 1-degree table (median of the 6' nodes of each cell, kept when at
# least half of its 100 nodes are ocean floor) and one native row along 30 S.
DATASETS.update({
    "grade-11-seafloor-age": dict(
        url="https://www.earthbyte.org/webdav/ftp/earthbyte/agegrid/2020/Grids/age.2020.1.GeeK2007.6m.grd",
        ext="grd", ledger="data:b2-seafloor-age",
        terms="Seton et al. 2020, G-cubed 21, e2020GC009214, doi:10.1029/2020GC009214; EarthByte "
              "age grid 2020.1 (GeeK2007, 6 arc-min); CC BY 4.0 (Zenodo record 5341342); credit "
              "in the caption and the credits; raw file 25 MB, not kept"),
})


def derive_b2_seafloor_age(key):
    """grade-11-seafloor-age.csv: lat, lon (1-degree cell centres), age (Myr), the median
    of the cell's 6' nodes when at least 50 of its 100 nodes have an age;
    grade-11-seafloor-age-30s.csv: lon, age (Myr) of every node on the parallel 30 S."""
    import numpy as np
    from scipy.io import netcdf_file
    f = netcdf_file(raw_path(key), "r", mmap=False)
    lon = np.array(f.variables["lon"][:], dtype=float)
    lat = np.array(f.variables["lat"][:], dtype=float)
    z = np.array(f.variables["z"][:], dtype=float)
    f.close()
    assert lon[0] == -180 and lat[0] == -90 and abs(lon[1] - lon[0] - 0.1) < 1e-9
    rows = []
    for j in range(180):              # cell [lat0, lat0+1) x [lon0, lon0+1)
        block_rows = z[10 * j:10 * j + 10]
        for i in range(360):
            b = block_rows[:, 10 * i:10 * i + 10]
            v = b[np.isfinite(b)]
            if v.size >= 50:
                rows.append(("%.1f" % (-89.5 + j), "%.1f" % (-179.5 + i), "%.1f" % float(np.median(v))))
    _write_csv(key, ("lat", "lon", "age"), rows)
    j30 = int(round((-30.0 - lat[0]) / 0.1))
    assert abs(lat[j30] + 30.0) < 1e-9
    _write_csv(key + "-30s", ("lon", "age"),
               [("%.1f" % lo, "%.2f" % a) for lo, a in zip(lon, z[j30]) if np.isfinite(a)])


DERIVE.update({"grade-11-seafloor-age": derive_b2_seafloor_age})

# Daily GNSS positions of two stations, Nevada Geodetic Laboratory, IGS20 frame,
# tenv3 format (Blewitt, Hammond and Kreemer 2018). MKEA: Mauna Kea, Hawaii (Pacific
# plate); WTZR: Wettzell, Germany (Eurasian plate). Derived: monthly means of the east
# and north positions (mm) from the first month, and the number of days in each month.
_NGL = "https://geodesy.unr.edu/gps_timeseries/IGS20/tenv3/IGS20/%s.tenv3"
_NGL_TERMS = ("Nevada Geodetic Laboratory GPS time series (IGS20 tenv3), NBMG data products policy: "
              "supplied as-is, free use; citation requested: Blewitt, Hammond and Kreemer (2018), "
              "Eos 99, doi:10.1029/2018EO104623; cited in the caption and the credits")
for _k, _s in (("grade-11-gnss-mkea", "MKEA"), ("grade-11-gnss-wtzr", "WTZR")):
    DATASETS[_k] = dict(url=_NGL % _s, ext="tenv3", ledger="data:b2-ngl-gnss", terms=_NGL_TERMS)


def derive_b2_gnss(key):
    """year (decimal, mean of the month's days), east_mm, north_mm (monthly means of the
    daily positions, from the first month's mean), days (number of daily solutions)."""
    months = {}
    for line in open(raw_path(key), encoding="utf8"):
        c = line.split()
        if len(c) < 13 or c[0] == "site":
            continue
        e = float(c[7]) + float(c[8])          # integer part + fractional part (m)
        n = float(c[9]) + float(c[10])
        months.setdefault(c[1][:5], []).append((float(c[2]), e, n))
    rows = []
    for m in sorted(months.values(), key=lambda v: v[0][0]):
        k = len(m)
        rows.append((sum(x[0] for x in m) / k, sum(x[1] for x in m) / k, sum(x[2] for x in m) / k, k))
    e0, n0 = rows[0][1], rows[0][2]
    _write_csv(key, ("year", "east_mm", "north_mm", "days"),
               [("%.4f" % t, "%.2f" % (1000 * (e - e0)), "%.2f" % (1000 * (n - n0)), k)
                for t, e, n, k in rows])


DERIVE.update({"grade-11-gnss-mkea": derive_b2_gnss, "grade-11-gnss-wtzr": derive_b2_gnss})

# India's journey (g12 mountain-building): past positions of two present-day points, one
# in central India (78 E, 20 N) and Lhasa (91.1 E, 29.65 N, on the Asian side of the
# suture), from the GPlates Web Service (EarthByte, University of Sydney) in two published
# plate models in a mantle reference frame: MULLER2022 (Mueller et al. 2022, Solid Earth 13,
# doi:10.5194/se-13-1127-2022, CC BY 4.0) and MULLER2019 (Mueller et al. 2019, Tectonics 38,
# doi:10.1029/2018TC005462, CC BY-NC-ND 4.0). One GeoJSON answer per model and age (a few
# bytes each); the derive merges them into one table.
_GWS = "https://gws.gplates.org/reconstruct/reconstruct_points/?lons=78,91.1&lats=20,29.65&time=%g&model=%s"
_GWS_TERMS = ("GPlates Web Service reconstruct_points (open-source service, EarthByte); model %s; "
              "numbers only, cited in the caption and the credits")
_B2_GWS_MODELS = {"MULLER2022": "Mueller et al. 2022 (CC BY 4.0)",
                  "MULLER2019": "Mueller et al. 2019 (CC BY-NC-ND 4.0)"}
_B2_GWS_AGES = sorted(set(range(0, 105, 5)) | {66})
for _m in _B2_GWS_MODELS:
    for _t in _B2_GWS_AGES:
        DATASETS["grade-12-gws-%s-%03d" % (_m.lower(), _t)] = dict(
            url=_GWS % (_t, _m), ext="json", ledger="data:b2-gws-india",
            terms=_GWS_TERMS % _B2_GWS_MODELS[_m])


def derive_b2_gws(key):
    """grade-12-gws-india.csv: model, age_Ma, lon/lat of the India point and of Lhasa, for
    every model and age whose raw answer is present (the same table whichever key runs)."""
    rows = []
    for m in _B2_GWS_MODELS:
        for t in _B2_GWS_AGES:
            k = "grade-12-gws-%s-%03d" % (m.lower(), t)
            if not os.path.exists(raw_path(k)):
                continue
            (lo1, la1), (lo2, la2) = json.load(open(raw_path(k), encoding="utf8"))["coordinates"]
            rows.append((m, t, "%.4f" % lo1, "%.4f" % la1, "%.4f" % lo2, "%.4f" % la2))
    _write_csv("grade-12-gws-india", ("model", "age_Ma", "india_lon", "india_lat",
                                      "lhasa_lon", "lhasa_lat"), rows)


for _k in DATASETS:
    if _k.startswith("grade-12-gws-"):
        DERIVE[_k] = derive_b2_gws

# North-east Japan (grade 12, subduction-magmatism): USGS ComCat, M >= 4.5, 1976-2025, a band
# across the arc at 37.5-40.5 N. The shared usgs-m6 file has too few intermediate-depth events
# under Japan for a section (g11.06 found 5 between 100 and 600 km).
DATASETS.update({
    "grade-12-usgs-ne-japan": dict(
        url="https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&orderby=time-asc"
            "&starttime=1976-01-01&endtime=2026-01-01&minmagnitude=4.5"
            "&minlatitude=37.5&maxlatitude=40.5&minlongitude=138&maxlongitude=146",
        ext="csv", ledger="data:b2-usgs-ne-japan",
        terms="USGS ANSS Comprehensive Catalog (ComCat), US Government work, public domain"),
})
DERIVE.update({"grade-12-usgs-ne-japan": derive_usgs})

# The Sunda shelf at the Last Glacial Maximum (grade 12, past-climates): ETOPO1 every 6th node
# (0.1 degree) over 11 S - 24 N, 92 - 122 E. The shared 1-degree grid is too coarse for a
# regional coastline.
DATASETS.update({
    "grade-12-etopo-sunda": dict(
        url="https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?"
            "altitude%5B(-11):6:(24)%5D%5B(92):6:(122)%5D",
        ext="csv", ledger="data:b2-etopo-sunda",
        terms="NOAA NCEI ETOPO1 (Amante and Eakins 2009), every 6th node (0.1 degree) over "
              "11 S-24 N, 92-122 E, by NOAA ERDDAP; US Government work, public domain"),
})
DERIVE.update({"grade-12-etopo-sunda": derive_etopo})
# ============================================================================
# end of Book 2 block
# ============================================================================


# ============================================================================
# Book 3: datasets used by Book 3 only (University Year 1). Ids start with the year.
# Added by the Book 3 agent, 2026-10-22 (sources/BATCH_BOOKS_1-5.md, Sync 1).
# ============================================================================
DATASETS.update({
    "bachelor-1-cie1931": dict(
        url="https://files.cie.co.at/Publications-datasets/CIE_xyz_1931_2deg.csv",
        ext="csv", ledger="data:b3-cie1931",
        terms="CIE (2019), Colour-matching functions of CIE 1931 standard colorimetric observer, "
              "doi:10.25039/CIE.DS.xvudnb9b; CC BY-SA 4.0 (licence in the file's metadata record): "
              "credit in the caption and the credits"),
    "bachelor-1-cie-d65": dict(
        url="https://files.cie.co.at/Publications-datasets/CIE_std_illum_D65.csv",
        ext="csv", ledger="data:b3-cie-d65",
        terms="CIE (2019), CIE standard illuminant D65, doi:10.25039/CIE.DS.hjfjmt59; CC BY-SA 4.0 "
              "(licence in the file's metadata record): credit in the caption and the credits"),
})


def derive_b3_cie1931(key):
    """nm, xbar, ybar, zbar: the CIE 1931 2-degree colour-matching functions, 360-830 nm
    every nanometre, as published (the raw file has no header)."""
    rows = []
    for line in open(raw_path(key), encoding="utf8").read().splitlines():
        c = [x.strip() for x in line.split(",")]
        if len(c) == 4 and c[0].isdigit():
            rows.append((int(c[0]), c[1], c[2], c[3]))
    _write_csv(key, ("nm", "xbar", "ybar", "zbar"), rows)


def derive_b3_d65(key):
    """nm, s: the relative spectral power of CIE standard illuminant D65, 300-830 nm every
    nanometre, as published (no header)."""
    rows = []
    for line in open(raw_path(key), encoding="utf8").read().splitlines():
        c = [x.strip() for x in line.split(",")]
        if len(c) == 2 and c[0].isdigit():
            rows.append((int(c[0]), c[1]))
    _write_csv(key, ("nm", "s"), rows)


DERIVE.update({"bachelor-1-cie1931": derive_b3_cie1931, "bachelor-1-cie-d65": derive_b3_d65})

# Kuril subduction zone (ch. 14 active-margins): USGS ComCat, M >= 5, 1976-2025, one box.
# The shared usgs-m6 file holds too few intermediate and deep events for one slab.
DATASETS.update({
    "bachelor-1-usgs-kuril": dict(
        url="https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&orderby=time-asc"
            "&starttime=1976-01-01&endtime=2026-01-01&minmagnitude=5"
            "&minlatitude=40&maxlatitude=56&minlongitude=138&maxlongitude=165",
        ext="csv", ledger="data:b3-usgs-kuril",
        terms="USGS ANSS Comprehensive Catalog (ComCat), US Government work, public domain"),
})
DERIVE.update({"bachelor-1-usgs-kuril": derive_usgs})

# Hotspots (ch. 15 hotspots): positions, track azimuths and rates in the hotspot frame,
# Table 1 of W. J. Morgan and J. P. Morgan (2007), "Plate velocities in hotspot reference
# frame: electronic supplement", the supplement of their chapter in GSA Special Paper 430
# (Plates, Plumes and Planetary Processes). The PDF is read from the Internet Archive copy of
# mantleplumes.org (whose certificate chain is incomplete); pdftotext (poppler) reads it.
DATASETS.update({
    "bachelor-1-hotspots": dict(
        url="https://web.archive.org/web/20260414214433id_/https://www.mantleplumes.org/"
            "P%5E4/P%5E4Chapters/MorganP4ElectronicSupp1.pdf",
        ext="pdf", ledger="data:b3-hotspots",
        terms="Morgan and Morgan (2007), electronic supplement, Table 1; the derived table is "
              "facts (positions, azimuths, rates), cited"),
})

_MM_PLATES = {"eu": "Eurasian", "ch": "China", "af": "African", "an": "Antarctic",
              "sa": "South American", "na": "North American", "au": "Australian",
              "nz": "Nazca", "co": "Cocos", "pa": "Pacific"}


def derive_b3_hotspots(key):
    """name, plate, lat, lon, w, quality, az, saz, rate, srate, az_model, rate_model: one row per
    (hotspot, plate) of Table 1. w is empty and quality holds the letter (A almost certainly a
    hotspot but no track, B perhaps a hotspot) when the table gives a letter instead of a weight;
    N.D. (not determined) is written empty. Samoa is listed twice on the Pacific plate, at
    169.1 W and at 168.2 W with the same track; the entry of the supplement text gives
    168.2 W, and that row is kept."""
    import re
    import subprocess
    txt = subprocess.run(["pdftotext", "-layout", raw_path(key), "-"], check=True,
                         capture_output=True, text=True).stdout
    txt = txt[txt.index("TABLE 1. AZIMUTH AND RATE OF EACH TRACK"):txt.index("TABLE 2. PACIFIC")]
    num = r"(-?[\d.]+)"
    nd = r"(N\.D\.\*?|±?\d+)"
    pat = re.compile(r"^(\S+)\s+(%s)\s+%s\s+%s\s+([\d.]+|[AB][+-]?)\s+%s\s+%s\s+%s\s+%s\s+%s\s+%s\s*$"
                     % ("|".join(_MM_PLATES), num, num, nd, nd, nd, nd, nd, nd))
    clean = lambda v: "" if v.startswith("N.D") else v.lstrip("±").lstrip("0") or "0"  # noqa: E731
    out, seen = [], {}
    for line in txt.splitlines():
        m = pat.match(line.strip())
        if not m:
            continue
        name, pl, lat, lon, w, az, saz, v, sv, azm, vm = m.groups()
        is_w = re.fullmatch(r"[\d.]+", w) is not None
        row = (name, _MM_PLATES[pl], lat, lon, w if is_w else "", "" if is_w else w,
               clean(az), clean(saz), clean(v), clean(sv), clean(azm), clean(vm))
        k = (name, pl)
        if k in seen:
            out[seen[k]] = row
            continue
        seen[k] = len(out)
        out.append(row)
    _write_csv(key, ("name", "plate", "lat", "lon", "w", "quality", "az", "saz", "rate", "srate",
                     "az_model", "rate_model"), out)


DERIVE.update({"bachelor-1-hotspots": derive_b3_hotspots})

# Kuril Trench gravity (ch. 14 active-margins): free-air anomaly and topography from the
# Scripps marine gravity model (Sandwell et al. 2014), extracted by the Scripps ASCII
# service for one box around the Kuril section (mag=0.1: anomaly in mGal; mag=1:
# topography in m). Every point listed: lon, lat, value; spacing 1 arc-minute in lon.
_KURIL_BOX = "north=48.5&south=43.5&east=157&west=149"
DATASETS.update({
    "bachelor-1-grav-kuril": dict(
        url="https://topex.ucsd.edu/cgi-bin/get_data.cgi?" + _KURIL_BOX + "&mag=0.1",
        ext="txt", ledger="data:b3-grav-kuril",
        terms="Scripps Institution of Oceanography satellite-derived marine gravity "
              "(Sandwell et al. 2014, Science 346, 65-67), freely available; cite the model"),
    "bachelor-1-topo-kuril": dict(
        url="https://topex.ucsd.edu/cgi-bin/get_data.cgi?" + _KURIL_BOX + "&mag=1",
        ext="txt", ledger="data:b3-grav-kuril",
        terms="Scripps Institution of Oceanography global topography (SRTM15+ family), freely "
              "available; cite the model"),
})


def _b3_xyz(key):
    pts = {}
    for line in open(raw_path(key), encoding="utf8"):
        c = line.split()
        if len(c) == 3:
            pts[(round(float(c[0]), 4), round(float(c[1]), 4))] = float(c[2])
    return pts


def derive_b3_grav_kuril(key):
    """lon, lat, faa_mgal, depth_m: every fourth node in longitude and in latitude of the
    two Scripps extractions (about 4 by 3 arc-minutes), where both are given; depth is
    the topography with its sign changed (positive below sea level)."""
    if key != "bachelor-1-grav-kuril":
        return
    g, t = _b3_xyz("bachelor-1-grav-kuril"), _b3_xyz("bachelor-1-topo-kuril")
    lons = sorted({k[0] for k in g})
    lats = sorted({k[1] for k in g})
    keep_lon, keep_lat = set(lons[::4]), set(lats[::4])
    rows = [(lo, la, "%.1f" % g[(lo, la)], "%.0f" % -t[(lo, la)])
            for la in lats if la in keep_lat for lo in lons if lo in keep_lon
            if (lo, la) in g and (lo, la) in t]
    _write_csv("bachelor-1-grav-kuril", ("lon", "lat", "faa_mgal", "depth_m"), rows)


DERIVE.update({"bachelor-1-grav-kuril": derive_b3_grav_kuril,
               "bachelor-1-topo-kuril": derive_b3_grav_kuril})

# Sea level over the last 800 kyr (ch. 23 diagenesis-basins): the stack of Spratt and
# Lisiecki (2016), Clim. Past 12, 1079-1092, as archived by NOAA NCEI Paleoclimatology
# (study 19982, dataset doi:10.25921/rd66-5820); tab-separated, '#' header lines.
DATASETS.update({
    "bachelor-1-sealevel-stack": dict(
        url="https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/spratt2016/"
            "spratt2016-noaa.txt",
        ext="txt", ledger="data:b3-sealevel-stack",
        terms="NOAA NCEI World Data Service for Paleoclimatology, Spratt and Lisiecki (2016); "
              "US Government data, free of restriction; cite the publication and the dataset DOI"),
})


def derive_b3_sealevel(key):
    """age_ka, sl_short, sig_short, sl_long, sig_long: the stack every 1 kyr, metres above
    present sea level; short = first principal component of seven records (0-430 ka),
    long = of five records (0-798 ka), each with its one-sigma bootstrap error; NaN
    written empty."""
    rows, header = [], None
    for line in open(raw_path(key), encoding="utf8"):
        if line.startswith("#") or not line.strip():
            continue
        c = line.rstrip("\n").split("\t")
        if header is None:
            header = c
            continue
        v = dict(zip(header, c))
        rows.append(tuple("" if v[k] == "NaN" else v[k] for k in (
            "age_calkaBP", "SeaLev_shortPC1", "SeaLev_shortPC1_err_sig",
            "SeaLev_longPC1", "SeaLev_longPC1_err_sig")))
    _write_csv(key, ("age_ka", "sl_short", "sig_short", "sl_long", "sig_long"), rows)


DERIVE.update({"bachelor-1-sealevel-stack": derive_b3_sealevel})

# Radiocarbon calibration (ch. 25 radiometric-methods): the IntCal20 Northern Hemisphere
# curve of Reimer et al. (2020), Radiocarbon 62, doi:10.1017/RDC.2020.41, as distributed
# with the rintcal package (file inst/extdata/intcal20.14c, pinned to a commit) because
# intcal.org did not answer; comma-separated, '#' header lines; every 1 cal yr to 5 cal
# kBP, then 5, 10 and 20 yr (to 15, 25 and 55 cal kBP).
DATASETS.update({
    "bachelor-1-intcal20": dict(
        url="https://raw.githubusercontent.com/Maarten14C/rintcal/"
            "e2e3db195c04bca2d5a8235a31e2dd1727808d8a/inst/extdata/intcal20.14c",
        ext="14c", ledger="data:b3-intcal20",
        terms="IntCal20 (Reimer et al. 2020, Radiocarbon 62, open access); copy distributed "
              "with the rintcal R package (M. Blaauw); cite the publication"),
})


def derive_b3_intcal20(key):
    """cal_bp, c14_age, c14_sigma, d14c, d14c_sigma: the IntCal20 curve as published,
    calendar years before AD 1950 (0-55000), conventional radiocarbon age (years BP)
    with its one-sigma error, and Delta-14C (per mil) with its error; sorted by
    increasing calendar age."""
    rows = []
    for line in open(raw_path(key), encoding="utf8"):
        if line.startswith("#") or not line.strip():
            continue
        rows.append(tuple(x.strip() for x in line.split(",")))
    rows.sort(key=lambda r: int(r[0]))
    _write_csv(key, ("cal_bp", "c14_age", "c14_sigma", "d14c", "d14c_sigma"), rows)


DERIVE.update({"bachelor-1-intcal20": derive_b3_intcal20})

# WOA23 annual columns (same service, template and derive as Book 2's, read only)
# for the T-S diagrams of the Year 1 chapter fluid-envelopes-structure: two South
# Atlantic stations on 25.5 W, at 10.5 S and 30.5 S, to the sea floor.
_B3_WOA_SITES = {"sa10": (-10.5, -25.5), "sa30": (-30.5, -25.5)}
for _site, (_la, _lo) in _B3_WOA_SITES.items():
    for _var, _dir in (("t", "temperature"), ("s", "salinity")):
        _k = "bachelor-1-woa23-%s-%s" % (_site, _var)
        DATASETS[_k] = dict(
            url=_WOA % (_dir, _var, "00", _var, 101, int(_la + 89.5), int(_lo + 179.5)),
            ext="txt", ledger="data:b3-woa23", terms=_WOA_TERMS)
        DERIVE[_k] = derive_b2_woa

# NCEP-NCAR Reanalysis 1, long-term monthly means 1991-2020 (NOAA PSL THREDDS,
# OPeNDAP ASCII, T62 Gaussian grid 94 x 192) for the Year 1 chapter
# radiation-heat-transport: top-of-atmosphere solar down and up and longwave up;
# surface latent and sensible heat fluxes (positive upwards) and precipitation.
# Derived to zonal, annual means (months weighted by their length).
_NCEP = "https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/%s/%s.%s.mon.ltm.1991-2020.nc.ascii?%s[0:1:11][0:1:93][0:1:191]"
_NCEP_TERMS = ("NCEP-NCAR Reanalysis 1 (Kalnay et al. 1996, BAMS 77, 437-471), long-term monthly "
               "means 1991-2020, data provided by the NOAA PSL, Boulder, Colorado, USA, from "
               "https://psl.noaa.gov (acknowledgement requested)")
_B3_NCEP = {"dswrf-toa": ("other_gauss", "dswrf", "ntat"), "uswrf-toa": ("other_gauss", "uswrf", "ntat"),
            "ulwrf-toa": ("other_gauss", "ulwrf", "ntat"), "lhtfl": ("surface_gauss", "lhtfl", "sfc"),
            "shtfl": ("surface_gauss", "shtfl", "sfc"), "prate": ("surface_gauss", "prate", "sfc")}


def derive_b3_ncep_zonal(key):
    """lat, value: zonal and annual mean of one NCEP R1 long-term monthly mean field
    (latitudes north to south as in the file, from 88.542 N to 88.542 S); months
    weighted by their number of days (February 28.25)."""
    import re
    txt = open(raw_path(key), encoding="utf8").read()
    days = (31, 28.25, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    rows = {}
    for m in re.finditer(r"^\[(\d+)\]\[(\d+)\], (.+)$", txt, re.M):
        vals = [float(x) for x in m.group(3).split(",")]
        if len(vals) != 192:
            continue
        rows[(int(m.group(1)), int(m.group(2)))] = sum(vals) / len(vals)
    lat = re.search(r"\.lat\[94\]\n([^\n]+)", txt).group(1)
    lats = [float(x) for x in lat.split(",")]
    assert len(rows) == 12 * 94 and len(lats) == 94, key
    out = []
    for j, la in enumerate(lats):
        v = sum(days[i] * rows[(i, j)] for i in range(12)) / sum(days)
        out.append(("%.3f" % la, "%.6g" % v))
    _write_csv(key, ("lat", "value"), out)
    # the twelve monthly zonal means as well (<key>-monthly.csv: month, lat, value)
    _write_csv(key + "-monthly", ("month", "lat", "value"),
               [(str(i + 1), "%.3f" % la, "%.6g" % rows[(i, j)])
                for i in range(12) for j, la in enumerate(lats)])


for _name, (_grid, _var, _lev) in _B3_NCEP.items():
    _k = "bachelor-1-ncep-" + _name
    DATASETS[_k] = dict(url=_NCEP % (_grid, _var, _lev, _var), ext="txt",
                        ledger="data:b3-ncep", terms=_NCEP_TERMS)
    DERIVE[_k] = derive_b3_ncep_zonal

# Zonal-mean winds and sea-level pressure (ch. 28 atmospheric-circulation): NCEP-NCAR
# Reanalysis 1 long-term monthly means 1991-2020 on the 2.5-degree grid, the winds on the
# 12 standard pressure levels from 1000 to 100 hPa (every second longitude, 5 degrees:
# the server cuts full-resolution answers at about 12 MB) and at sigma 0.995, the
# sea-level pressure.
_NCEP25 = "https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/%s.mon.ltm.1991-2020.nc.ascii?%s%s[0:1:72]%s"
_B3_NCEP25 = {"uwnd-p": ("pressure/uwnd", "uwnd", "[0:1:11][0:1:11]", "[0:2:143]"),
              "vwnd-p": ("pressure/vwnd", "vwnd", "[0:1:11][0:1:11]", "[0:2:143]"),
              "uwnd-sfc": ("surface/uwnd.sig995", "uwnd", "[0:1:11]", "[0:1:143]"),
              "slp": ("surface/slp", "slp", "[0:1:11]", "[0:1:143]")}
_PLEVELS = (1000, 925, 850, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10)


def derive_b3_ncep25_zonal(key):
    """month, [level,] lat, value: zonal means of one NCEP R1 2.5-degree long-term
    monthly mean field (months 1-12; latitudes 90 N to 90 S; levels in hPa)."""
    import re
    txt = open(raw_path(key), encoding="utf8").read()
    lat = [float(x) for x in re.search(r"\.lat\[73\]\n([^\n]+)", txt).group(1).split(",")]
    out = []
    for m in re.finditer(r"^((?:\[\d+\])+), (.+)$", txt, re.M):
        idx = [int(i) for i in re.findall(r"\d+", m.group(1))]
        vals = [float(x) for x in m.group(2).split(",")]
        if len(vals) not in (72, 144):
            continue
        z = sum(vals) / len(vals)
        if len(idx) == 3:
            out.append((str(idx[0] + 1), str(_PLEVELS[idx[1]]), "%.1f" % lat[idx[2]], "%.6g" % z))
        else:
            out.append((str(idx[0] + 1), "%.1f" % lat[idx[1]], "%.6g" % z))
    if len(out[0]) == 4:
        assert len(out) == 12 * 12 * 73, (key, len(out))
        _write_csv(key, ("month", "level", "lat", "value"), out)
    else:
        assert len(out) == 12 * 73, (key, len(out))
        _write_csv(key, ("month", "lat", "value"), out)


for _name, (_path, _var, _dims, _lons) in _B3_NCEP25.items():
    _k = "bachelor-1-ncep-" + _name
    DATASETS[_k] = dict(url=_NCEP25 % (_path, _var, _dims, _lons), ext="txt",
                        ledger="data:b3-ncep-circ", terms=_NCEP_TERMS)
    DERIVE[_k] = derive_b3_ncep25_zonal
# ============================================================================
# end of Book 3 block
# ============================================================================


# ============================================================================
# Book 4: datasets used by Book 4 only (University Year 2). Ids start with the year.
# Added by the Book 4 agent, 2026-10-23 (sources/BATCH_BOOKS_1-5.md, Sync 2).
# ============================================================================
# Meteorite falls and finds by class (ch. 2 planet-formation-meteorites): NASA's export of
# the Meteoritical Bulletin Database (The Meteoritical Society), 45,716 records.
DATASETS.update({
    "bachelor-2-meteorites": dict(
        url="https://data.nasa.gov/docs/legacy/meteorite_landings/Meteorite_Landings.csv",
        ext="csv", ledger="data:b4-meteorites",
        terms="NASA Open Data Portal, Meteorite Landings (compiled from the Meteoritical Bulletin "
              "Database of The Meteoritical Society); US Government open data, no restrictions"),
})


def _b4_meteorite_group(rc):
    """Group a Meteoritical Bulletin class string into the classes of ch. 2."""
    import re
    rc = rc.strip()
    if rc.startswith("Iron"):
        return "iron"
    if rc.startswith(("Pallasite", "Mesosiderite")):
        return "stony-iron"
    if rc.startswith(("Eucrite", "Howardite", "Diogenite")):
        return "HED achondrite"
    if rc.startswith(("Aubrite", "Ureilite", "Angrite", "Acapulcoite", "Lodranite", "Winonaite",
                      "Brachinite", "Martian", "Lunar", "Achondrite")):
        return "other achondrite"
    if re.match(r"^(H|L|LL|OC|H/L|L/LL)(\d|\?|$|/|-|\s)", rc) or rc in ("H", "L", "LL", "OC"):
        return "ordinary chondrite"
    if re.match(r"^C(I|M|O|V|K|R|H|B|\d|$|-)", rc):
        return "carbonaceous chondrite"
    if re.match(r"^E(H|L|\d|$)", rc):
        return "enstatite chondrite"
    if re.match(r"^(R|K)\d", rc):
        return "other chondrite"
    return "unclassified"


def derive_b4_meteorites(key):
    """group, falls, finds, finds_antarctic: valid meteorites (not relicts) counted by class
    group; finds_antarctic counts the finds recorded south of 60 S (finds with no recorded
    position, given as 0,0, are not counted there). The year column is not used (it holds a
    few impossible values)."""
    import collections
    falls, finds, ant = collections.Counter(), collections.Counter(), collections.Counter()
    with open(raw_path(key), encoding="utf8") as f:
        for r in csv.DictReader(f):
            if r["nametype"] != "Valid":
                continue
            g = _b4_meteorite_group(r["recclass"])
            if r["fall"] == "Fell":
                falls[g] += 1
            else:
                finds[g] += 1
                if r["reclat"] and float(r["reclat"]) <= -60.0:
                    ant[g] += 1
    order = ("ordinary chondrite", "carbonaceous chondrite", "enstatite chondrite",
             "other chondrite", "HED achondrite", "other achondrite", "iron", "stony-iron",
             "unclassified")
    _write_csv(key, ("group", "falls", "finds", "finds_antarctic"),
               [(g, falls[g], finds[g], ant[g]) for g in order])


DERIVE.update({"bachelor-2-meteorites": derive_b4_meteorites})

# Sr-Nd-Pb isotopes of ocean island basalts (ch. 4 isotope-geochemistry): Stracke et al. 2022
# data release on GRO.data (CC BY 4.0), Tristan da Cunha, Gough, St. Helena, Cook-Austral.
DATASETS.update({
    "bachelor-2-oib-isotopes": dict(
        url="https://data.goettingen-research-online.de/api/access/datafile/49490",
        ext="tab", ledger="data:b4-oib-isotopes",
        terms="Stracke, A., Willig, M., Genske, F., Beguelin, P., Todd, E. (2022), Chemical and "
              "radiogenic isotope data of ocean island basalts from Tristan da Cunha, Gough, "
              "St. Helena, and the Cook-Austral Islands, GRO.data V1, doi:10.25625/BQENGN; CC BY 4.0"),
})

_B4_OIB_TYPE = {"St. Helena": "HIMU", "Mangaia": "HIMU", "Tubuai": "HIMU",
                "Tristan": "EM1", "Gough": "EM1"}


def derive_b4_oib_isotopes(key):
    """island, type, sample, sr87_86, nd143_144, pb206_204, sr_ppm, nd_ppm: every sample of the
    St. Helena, Mangaia, Tubuai (HIMU type islands) and Tristan, Gough (EM1 type) groups that
    has both a Sr and a Nd isotope ratio; Pb blank where not measured. The table's header
    row is the one whose first cell is "Location (Island)"."""
    with open(raw_path(key), encoding="utf8") as f:
        rows = list(csv.reader(f, delimiter="\t"))
    h = next(i for i, r in enumerate(rows) if r and r[0] == "Location (Island)")
    hdr = rows[h]
    ci = {n: hdr.index(n) for n in ("87Sr/86Sr", "143Nd/144Nd", "206Pb/204Pb", "Sr", "Nd")}
    out = []
    for r in rows[h + 1:]:
        if not r or r[0] not in _B4_OIB_TYPE:
            continue
        try:
            sr, nd = float(r[ci["87Sr/86Sr"]]), float(r[ci["143Nd/144Nd"]])
        except ValueError:
            continue
        pb = r[ci["206Pb/204Pb"]].strip()
        out.append((r[0], _B4_OIB_TYPE[r[0]], r[1].strip(), "%.6f" % sr, "%.6f" % nd,
                    "%.3f" % float(pb) if pb else "", "%.4g" % float(r[ci["Sr"]]),
                    "%.4g" % float(r[ci["Nd"]])))
    _write_csv(key, ("island", "type", "sample", "sr87_86", "nd143_144", "pb206_204", "sr_ppm",
                     "nd_ppm"), out)


DERIVE.update({"bachelor-2-oib-isotopes": derive_b4_oib_isotopes})

# Holocene eruptions with their Volcanic Explosivity Index (ch. 6 eruptive-styles): the GVP
# Volcanoes of the World eruption list, WFS layer Smithsonian_VOTW_Holocene_Eruptions.
DATASETS.update({
    "bachelor-2-gvp-eruptions": dict(
        url="https://webservices.volcano.si.edu/geoserver/GVP-VOTW/ows?service=WFS&version=2.0.0"
            "&request=GetFeature&typeName=GVP-VOTW:Smithsonian_VOTW_Holocene_Eruptions&outputFormat=csv",
        ext="csv", ledger="data:b4-gvp-eruptions",
        terms="Global Volcanism Program, Smithsonian Institution, Volcanoes of the World: "
              "eruption dates and VEI only (facts), cited; no text or photograph reused"),
})


def derive_b4_gvp_eruptions(key):
    """volcano_number, volcano, eruption_number, start_year, vei: every Confirmed Eruption
    that has a VEI, sorted by start year then eruption number. Uncertain eruptions and
    eruptions without a VEI are dropped; the VEI modifier (+, ?) is ignored."""
    out = []
    with open(raw_path(key), encoding="utf8") as f:
        for r in csv.DictReader(f):
            if r["Activity_Type"] != "Confirmed Eruption" or r["ExplosivityIndexMax"] == "":
                continue
            out.append((int(r["Volcano_Number"]), r["Volcano_Name"], int(r["Eruption_Number"]),
                        int(r["StartDateYear"]), int(r["ExplosivityIndexMax"])))
    out.sort(key=lambda r: (r[3], r[2]))
    _write_csv(key, ("volcano_number", "volcano", "eruption_number", "start_year", "vei"), out)


DERIVE.update({"bachelor-2-gvp-eruptions": derive_b4_gvp_eruptions})

# Whole-rock analyses of the Skaergaard intrusion (ch. 8 magmatic-differentiation): Tegner et
# al. 2023, GEUS Bulletin 53, 8316, Supplementary Data File 1 (GEUS Dataverse, CC BY 4.0).
DATASETS.update({
    "bachelor-2-skaergaard": dict(
        url="https://dataverse.geus.dk/api/access/datafile/45024",
        ext="xlsx", ledger="data:b4-skaergaard",
        terms="Tegner, C. et al. (2023), A whole-rock data set for the Skaergaard intrusion, East "
              "Greenland, GEUS Bulletin 53, 8316, doi:10.34194/geusb.v53.8316; Supplementary Data "
              "File 1, GEUS Dataverse doi:10.22008/FK2/HOWW6F; CC BY 4.0"),
})


def _b4_xlsx_rows(path, sheet_name):
    """Rows of one sheet of an .xlsx file as {column letter: text} (stdlib only)."""
    import re
    import xml.etree.ElementTree as ET
    import zipfile
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    z = zipfile.ZipFile(path)
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(ns + "si"):
            shared.append("".join(t.text or "" for t in si.iter(ns + "t")))
    names = [s.get("name") for s in ET.fromstring(z.read("xl/workbook.xml")).iter(ns + "sheet")]
    sheet = ET.fromstring(z.read("xl/worksheets/sheet%d.xml" % (names.index(sheet_name) + 1)))
    rows = []
    for r in sheet.iter(ns + "row"):
        row = {}
        for c in r.iter(ns + "c"):
            v = c.find(ns + "v")
            if v is None:
                continue
            col = re.match(r"[A-Z]+", c.get("r")).group(0)
            row[col] = shared[int(v.text)] if c.get("t") == "s" else v.text
        rows.append(row)
    return rows


def derive_b4_skaergaard(key):
    """height_m, F, subzone, SiO2, MgO, FeOt, CaO, Na2O, K2O, Ni, Cr, Zr, Rb, Sr (XRF, ppm):
    the cumulate samples of the Layered Series reference profile (profile no. 1 of the
    article's Table 1: surface samples and drill core 90-22), stratigraphic height above the
    base of LZa and the authors' fraction of melt remaining F; rows between the 'Reference
    profile' heading and the next heading row (a row with text in column A only)."""
    rows = _b4_xlsx_rows(raw_path(key), "data")
    cols = dict(height_m="H", F="J", subzone="K", SiO2="P", MgO="V", FeOt="AC", CaO="W",
                Na2O="X", K2O="Y", Ni="AJ", Cr="AI", Zr="AP", Rb="AM", Sr="AN")
    out, inside = [], False
    for r in rows:
        a = r.get("A", "")
        if a.startswith("Reference profile"):
            inside = True
            continue
        if inside and a and not r.get("B"):  # the next profile's heading row
            break
        if not inside or r.get("B") != "Cumulate" or not r.get("H") or not r.get("J"):
            continue
        rec = []
        for name, c in cols.items():
            v = r.get(c, "")
            if name == "subzone":
                rec.append(v.strip())
            elif name == "height_m":
                rec.append("%.0f" % float(v))
            elif name == "F":
                rec.append("%.4f" % (round(float(v), 4) + 0.0))  # no "-0.0000"
            else:
                try:
                    rec.append("%.2f" % float(v) if name in ("SiO2", "MgO", "FeOt", "CaO", "Na2O",
                                                             "K2O") else "%.1f" % float(v))
                except ValueError:
                    rec.append("")
        out.append(rec)
    out.sort(key=lambda x: float(x[0]))
    _write_csv(key, tuple(cols), out)


DERIVE.update({"bachelor-2-skaergaard": derive_b4_skaergaard})

# Magmatic series and tectonic settings (ch. 9 magmatic-series): two data sets distributed with
# the GeoplotR package of P. Vermeesch (GPL-3), pinned to commit e404f524 (2026-07-09):
# 456 tholeiitic rocks from Iceland and 580 calc-alkaline rocks from the Cascades (the
# compilation of Rollinson and Pease 2021 used by Vermeesch and Pease 2021, GPL 18, 1-6), and
# 756 basalts of known setting (MORB, OIB, island-arc basalts) used by Vermeesch (2006, GCA 70,
# 1839-1848). Factual analyses compiled from the literature; attribution in the ledger.
_B4_GEOPLOTR = "https://raw.githubusercontent.com/pvermees/GeoplotR/e404f524655c664d9cf3b30079ed39bb5803e645/inst/"
DATASETS.update({
    "bachelor-2-cath": dict(
        url=_B4_GEOPLOTR + "cath.csv", ext="csv", ledger="data:b4-cath",
        terms="GeoplotR (P. Vermeesch, GPL-3) inst/cath.csv: Iceland (tholeiitic) and Cascades "
              "(calc-alkaline) whole-rock analyses compiled by Rollinson and Pease (2021); "
              "factual data, cited as Vermeesch and Pease (2021), Geochem. Persp. Let. 19, 1-6"),
    "bachelor-2-basalt-settings": dict(
        url=_B4_GEOPLOTR + "training.csv", ext="csv", ledger="data:b4-basalt-settings",
        terms="GeoplotR (P. Vermeesch, GPL-3) inst/training.csv: 756 basalts from mid-ocean "
              "ridges, ocean islands and island arcs compiled from PetDB and GEOROC for "
              "Vermeesch (2006), Geochim. Cosmochim. Acta 70, 1839-1848; factual data"),
})


def derive_b4_cath(key):
    """series (th = Iceland, ca = Cascades), SiO2, TiO2, Al2O3, FeOT, CaO, MgO, Na2O, K2O
    (wt %, as given): every row with all eight oxides."""
    names = ("SiO2", "TiO2", "Al2O3", "FeOT", "CaO", "MgO", "Na2O", "K2O")
    out = []
    with open(raw_path(key), encoding="utf8") as f:
        for r in csv.DictReader(f):
            try:
                vals = ["%.2f" % float(r[n]) for n in names]
            except (KeyError, ValueError):
                continue
            out.append([r["affinity"].strip()] + vals)
    _write_csv(key, ("series",) + names, out)


_B4_SETTING_TRACE = ("Rb", "Ba", "Th", "U", "Nb", "Ta", "La", "Ce", "Pb", "Sr", "Nd", "Zr",
                     "Hf", "Sm", "Eu", "Gd", "Dy", "Y", "Er", "Yb", "Lu")


def derive_b4_basalt_settings(key):
    """setting (MORB, OIB, IAB), SiO2, TiO2, FeOT, MgO, Na2O, K2O (wt %; FeOT = FeO +
    0.8998 Fe2O3, blank if either is missing), then the trace elements of
    _B4_SETTING_TRACE in ppm (blank where not analysed)."""
    out = []
    with open(raw_path(key), encoding="utf8") as f:
        for r in csv.DictReader(f):
            def num(n):
                v = r.get(n, "").strip()
                try:
                    return float(v)
                except ValueError:
                    return None
            fe2, fe = num("Fe2O3"), num("FeO")
            feot = fe + 0.8998 * fe2 if (fe is not None and fe2 is not None) else None
            rec = [r["AFFINITY"].strip()]
            for v in (num("SiO2"), num("TiO2"), feot, num("MgO"), num("Na2O"), num("K2O")):
                rec.append("" if v is None else "%.2f" % v)
            for n in _B4_SETTING_TRACE:
                v = num(n)
                rec.append("" if v is None else "%g" % v)
            out.append(rec)
    _write_csv(key, ("setting", "SiO2", "TiO2", "FeOT", "MgO", "Na2O", "K2O")
               + _B4_SETTING_TRACE, out)


DERIVE.update({"bachelor-2-cath": derive_b4_cath,
               "bachelor-2-basalt-settings": derive_b4_basalt_settings})

# The Alps (ch. 13 alpine-orogen): ETOPO1 every 3rd node (0.05 degree) over 43.5-48.5 N,
# 5-14 E for the relief map and the 8 E profile; Moho depth picks of the AlpArray receiver
# functions (Michailos et al. 2023, Zenodo, CC BY 4.0) for the crustal root.
DATASETS.update({
    "bachelor-2-etopo-alps": dict(
        url="https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?"
            "altitude%5B(43.5):3:(48.5)%5D%5B(5):3:(14)%5D",
        ext="csv", ledger="data:b4-etopo-alps",
        terms="NOAA NCEI ETOPO1 (Amante and Eakins 2009), every 3rd node (0.05 degree) over "
              "43.5-48.5 N, 5-14 E, by NOAA ERDDAP; US Government work, public domain"),
    "bachelor-2-alps-moho": dict(
        url="https://zenodo.org/api/records/7695125/files/moho_depths_all.csv/content",
        ext="csv", ledger="data:b4-alps-moho",
        terms="Michailos, K. et al. (2023), European Alps Receiver Function Database, Zenodo, "
              "doi:10.5281/zenodo.7695125, file moho_depths_all.csv; CC BY 4.0"),
})


def derive_b4_etopo_alps(key):
    """lat, lon (3 decimals: the 0.05-degree nodes), elevation (m)."""
    rows = []
    with open(raw_path(key), encoding="utf8") as f:
        r = csv.reader(f)
        next(r); next(r)                       # ERDDAP: names, then units
        for lat, lon, alt in r:
            rows.append(("%.3f" % float(lat), "%.3f" % float(lon), "%d" % round(float(alt))))
    _write_csv(key, ("lat", "lon", "elev_m"), rows)


def derive_b4_alps_moho(key):
    """lon, lat, moho_km: every manually picked Moho depth, in the file's order."""
    rows = []
    with open(raw_path(key), encoding="utf8") as f:
        r = csv.reader(f)
        next(r)                                # header: Longitude, Latitude, Moho depth
        for rec in r:
            if len(rec) < 3 or not rec[0].strip():
                continue
            lon, lat, z = (float(x) for x in rec[:3])
            rows.append(("%.4f" % lon, "%.4f" % lat, "%.2f" % z))
    _write_csv(key, ("lon", "lat", "moho_km"), rows)


DERIVE.update({"bachelor-2-etopo-alps": derive_b4_etopo_alps,
               "bachelor-2-alps-moho": derive_b4_alps_moho})

# Two plateaus (ch. 14 himalaya-andes): ETOPO1 every 6th node (0.1 degree) over Tibet and
# the Himalaya (25-40 N, 75-100 E) and over the Central Andes (30-10 S, 75-60 W), for the
# relief maps and the swath profiles. Same derivation as the Alps window.
DATASETS.update({
    "bachelor-2-etopo-tibet": dict(
        url="https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?"
            "altitude%5B(25):6:(40)%5D%5B(75):6:(100)%5D",
        ext="csv", ledger="data:b4-etopo-tibet",
        terms="NOAA NCEI ETOPO1 (Amante and Eakins 2009), every 6th node (0.1 degree) over "
              "25-40 N, 75-100 E, by NOAA ERDDAP; US Government work, public domain"),
    "bachelor-2-etopo-andes": dict(
        url="https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?"
            "altitude%5B(-30):6:(-10)%5D%5B(-75):6:(-60)%5D",
        ext="csv", ledger="data:b4-etopo-andes",
        terms="NOAA NCEI ETOPO1 (Amante and Eakins 2009), every 6th node (0.1 degree) over "
              "30-10 S, 75-60 W, by NOAA ERDDAP; US Government work, public domain"),
})
DERIVE.update({"bachelor-2-etopo-tibet": derive_b4_etopo_alps,
               "bachelor-2-etopo-andes": derive_b4_etopo_alps})

# The Phanerozoic Earth (ch. 19 phanerozoic-earth). (1) Sea level since 250 Ma from the
# Miller et al. (2005) study at NOAA NCEI Paleo (dataset doi:10.25921/kc41-xy86): the New
# Jersey backstripped curve with its estimated lowstands (Kominz et al. 2008) and the Haq et
# al. (1987) curve as tabulated there. (2) Palaeocoastlines: today's coastlines carried back
# to 0, 50, 100, 200, 300 and 500 Ma in the plate model of Merdith et al. (2021, Zenodo
# record 12525525, CC BY 4.0), reconstructed by the GPlates Web Service (EarthByte).
_B4_MILLER = "https://www.ncei.noaa.gov/pub/data/paleo/contributions_by_author/miller2005/"
_B4_MILLER_TERMS = ("NOAA NCEI Paleoclimatology, Miller et al. (2005) Phanerozoic record of "
                    "global sea-level change, dataset doi:10.25921/kc41-xy86; NOAA/World Data "
                    "Service for Paleoclimatology data, free to use with citation")
DATASETS.update({
    "bachelor-2-miller2005-kominz08": dict(
        url=_B4_MILLER + "miller2005-kominz08-noaa.txt", ext="txt",
        ledger="data:b4-sealevel", terms=_B4_MILLER_TERMS),
    "bachelor-2-miller2005-haq87": dict(
        url=_B4_MILLER + "miller2005-haq87-noaa.txt", ext="txt",
        ledger="data:b4-sealevel", terms=_B4_MILLER_TERMS),
})
for _t in (0, 50, 100, 200, 300, 500):
    DATASETS["bachelor-2-palaeocoast-%d" % _t] = dict(
        url="https://gws.gplates.org/reconstruct/coastlines/?time=%d&model=MERDITH2021" % _t,
        ext="json", ledger="data:b4-palaeocoast",
        terms="Merdith, A. S. et al. (2021), plate model 1000-0 Ma, Zenodo record 12525525, "
              "CC BY 4.0; coastlines reconstructed to %d Ma by the GPlates Web Service "
              "(EarthByte, gws.gplates.org)" % _t)


def derive_b4_miller(key):
    """age_ma (2012 time scale, the file's age-GTS12_ma column), then the sea-level columns
    of the file as given (m above modern sea level): Kominz 2008 backstrip and backstrip with
    the estimated lowstands, or the Haq 1987 curve. Rows with a missing value are dropped."""
    with open(raw_path(key), encoding="utf8") as f:
        lines = [ln.rstrip("\n").split("\t") for ln in f if not ln.startswith("#") and ln.strip()]
    hdr, rows = lines[0], lines[1:]
    cols = [c for c in hdr if c.startswith("sealev")]
    out = []
    for r in rows:
        d = dict(zip(hdr, r))
        vals = [d.get("age-GTS12_ma", "")] + [d.get(c, "") for c in cols]
        if any(v.strip() in ("", "NA") for v in vals):
            continue
        out.append(["%.3f" % float(vals[0])] + ["%.2f" % float(v) for v in vals[1:]])
    out.sort(key=lambda r: float(r[0]))
    _write_csv(key, ["age_ma"] + [c.replace("sealev-", "") for c in cols], out)


def _b4_ring_area_km2(ring):
    """Area of a lon/lat ring on a sphere of radius 6371 km (the smaller of the two sides)."""
    s = 0.0
    for (l1, p1), (l2, p2) in zip(ring, ring[1:] + ring[:1]):
        dl = l2 - l1
        if dl > 180:
            dl -= 360
        elif dl < -180:
            dl += 360
        s += math.radians(dl) * (2 + math.sin(math.radians(p1)) + math.sin(math.radians(p2)))
    a = abs(s) / 2 * 6371.0 ** 2
    return min(a, 4 * math.pi * 6371.0 ** 2 - a)


def derive_b4_palaeocoast(key):
    """ring, lon, lat (2 decimals): every coastline ring of more than 50,000 km2, thinned so
    that kept points are at least 1 degree apart (distance in degrees, longitude scaled by
    the cosine of the latitude); rings in the service's order."""
    with open(raw_path(key), encoding="utf8") as f:
        d = json.load(f)
    rows, n = [], 0
    for feat in d["features"]:
        g = feat["geometry"]
        polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"]
        for poly in polys:
            for ring in poly:
                if _b4_ring_area_km2(ring) < 5.0e4:
                    continue
                kept = [ring[0]]
                for p in ring[1:]:
                    q = kept[-1]
                    if math.hypot((p[0] - q[0]) * math.cos(math.radians(p[1])), p[1] - q[1]) >= 1.0:
                        kept.append(p)
                n += 1
                rows += [(n, "%.2f" % p[0], "%.2f" % p[1]) for p in kept]
    _write_csv(key, ("ring", "lon", "lat"), rows)


DERIVE.update({"bachelor-2-miller2005-kominz08": derive_b4_miller,
               "bachelor-2-miller2005-haq87": derive_b4_miller})
DERIVE.update({"bachelor-2-palaeocoast-%d" % _t: derive_b4_palaeocoast
               for _t in (0, 50, 100, 200, 300, 500)})

# Four cities carried back in the same plate model (ch. 19): Paris, New York, Sydney and Cape
# Town at their GeoNames coordinates (ledger geonames4:*), reconstructed to each time.
_B4_CITIES = (("Paris", 2.3488, 48.85341), ("NewYork", -74.00597, 40.71427),
              ("Sydney", 151.20732, -33.86785), ("CapeTown", 18.42322, -33.92584))
for _t in (50, 100, 200, 300, 500):
    DATASETS["bachelor-2-palaeopos-%d" % _t] = dict(
        url="https://gws.gplates.org/reconstruct/reconstruct_points/?points=%s&time=%d"
            "&model=MERDITH2021" % (",".join("%g,%g" % (c[1], c[2]) for c in _B4_CITIES), _t),
        ext="json", ledger="data:b4-palaeopos",
        terms="Merdith, A. S. et al. (2021), plate model 1000-0 Ma, Zenodo record 12525525, "
              "CC BY 4.0; points reconstructed to %d Ma by the GPlates Web Service "
              "(EarthByte, gws.gplates.org)" % _t)


def derive_b4_palaeopos(key):
    """city, lon, lat (degrees, 2 decimals): the reconstructed position of each city of
    _B4_CITIES, in the order of the request."""
    with open(raw_path(key), encoding="utf8") as f:
        pts = json.load(f)["coordinates"]
    _write_csv(key, ("city", "lon", "lat"),
               [(c[0], "%.2f" % p[0], "%.2f" % p[1]) for c, p in zip(_B4_CITIES, pts)])


DERIVE.update({"bachelor-2-palaeopos-%d" % _t: derive_b4_palaeopos
               for _t in (50, 100, 200, 300, 500)})
# One morning sounding (ch. 21 atmospheric-thermodynamics): Norman, Oklahoma (IGRA2 station
# USM00072357, 35.18 N 97.44 W, 345 m), 16 April 2026 12 UTC, from the Integrated Global
# Radiosonde Archive version 2 (NOAA NCEI). The period-of-record file is a zip of the
# station's whole history; the derive step keeps the one sounding.
DATASETS.update({
    "bachelor-2-sounding": dict(
        url="https://www.ncei.noaa.gov/data/integrated-global-radiosonde-archive/access/"
            "data-por/USM00072357-data.txt.zip",
        ext="zip", ledger="data:b4-sounding",
        terms="Durre, I. et al., Integrated Global Radiosonde Archive (IGRA) Version 2, NOAA "
              "National Centers for Environmental Information, doi:10.7289/V5X63K0Q; US "
              "Government work, no restrictions"),
})
_B4_SOUNDING = (2026, 4, 16, 12)


def derive_b4_sounding(key):
    """p_hPa, z_m, T_C, Td_C, RH_pct, lvltyp: every level of the 16 April 2026 12 UTC sounding
    down to 100 hPa with a pressure and a temperature (IGRA2 data record columns); the dew
    point is T minus the reported dew-point depression, empty where it is missing."""
    import io
    import zipfile
    with zipfile.ZipFile(raw_path(key)) as z:
        name = [n for n in z.namelist() if n.endswith(".txt")][0]
        lines = io.TextIOWrapper(z.open(name), encoding="ascii", errors="replace")
        rows, keep = [], False
        for line in lines:
            if line.startswith("#"):
                if keep:
                    break
                keep = (int(line[13:17]), int(line[18:20]), int(line[21:23]),
                        int(line[24:26])) == _B4_SOUNDING
                continue
            if not keep:
                continue
            p, zz, t = int(line[9:15]), int(line[16:21]), int(line[22:27])
            rh, dp = int(line[28:33]), int(line[34:39])
            if p < 10000 or t <= -8888:
                continue
            rows.append(("%.2f" % (p / 100.0), zz if zz > -8888 else "", "%.1f" % (t / 10.0),
                         "%.1f" % (t / 10.0 - dp / 10.0) if dp > -8888 else "",
                         "%.1f" % (rh / 10.0) if rh > -8888 else "", line[0:2]))
    _write_csv(key, ("p_hPa", "z_m", "T_C", "Td_C", "RH_pct", "lvltyp"), rows)


DERIVE.update({"bachelor-2-sounding": derive_b4_sounding})

# ENSO and NAO indices (ch. 23 climate-variability): NOAA Climate Prediction Center text
# files, US Government works. The CPC updates them monthly: the derived tables freeze the
# version fetched on the access date in data/MANIFEST.md.
_B4_CPC = "NOAA NCEP Climate Prediction Center; US Government work, no restrictions"
DATASETS.update({
    "bachelor-2-oni": dict(
        url="https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt",
        ext="txt", ledger="data:b4-oni",
        terms="Oceanic Nino Index (ERSSTv6, 3-month running mean, centred 30-year base "
              "periods), " + _B4_CPC),
    "bachelor-2-roni": dict(
        url="https://www.cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt",
        ext="txt", ledger="data:b4-roni",
        terms="Relative Oceanic Nino Index (official ENSO index from 1 February 2026, NWS PNS "
              "26-05), " + _B4_CPC),
    "bachelor-2-nino34": dict(
        url="https://www.cpc.ncep.noaa.gov/data/indices/detrend.nino34.ascii.txt",
        ext="txt", ledger="data:b4-nino34",
        terms="monthly Nino 3.4 SST, adjusted climatology and anomaly (the monthly input of the "
              "ONI), " + _B4_CPC),
    "bachelor-2-nao": dict(
        url="https://www.cpc.ncep.noaa.gov/products/precip/CWlink/pna/"
            "norm.nao.monthly.b5001.current.ascii",
        ext="txt", ledger="data:b4-nao",
        terms="monthly standardized North Atlantic Oscillation index since 1950, " + _B4_CPC),
})


def derive_b4_oni(key):
    """season, year, total_C, anom_C from the CPC ONI or RONI table (RONI has no total)."""
    rows = []
    with open(raw_path(key), encoding="ascii", errors="replace") as f:
        next(f)
        for line in f:
            c = line.split()
            if len(c) == 4:
                rows.append((c[0], int(c[1]), c[2], c[3]))
            elif len(c) == 3:
                rows.append((c[0], int(c[1]), "", c[2]))
    _write_csv(key, ("season", "year", "total_C", "anom_C"), rows)


def derive_b4_nino34(key):
    """year, month, total_C, clim_C, anom_C: monthly Nino 3.4 values."""
    rows = []
    with open(raw_path(key), encoding="ascii", errors="replace") as f:
        next(f)
        for line in f:
            c = line.split()
            if len(c) == 5:
                rows.append((int(c[0]), int(c[1]), c[2], c[3], c[4]))
    _write_csv(key, ("year", "month", "total_C", "clim_C", "anom_C"), rows)


def derive_b4_nao(key):
    """year, month, nao: the monthly standardized NAO index."""
    rows = []
    with open(raw_path(key), encoding="ascii", errors="replace") as f:
        for line in f:
            c = line.split()
            if len(c) == 3:
                rows.append((int(c[0]), int(c[1]), "%.2f" % float(c[2])))
    _write_csv(key, ("year", "month", "nao"), rows)


# The CPC's own historical ONI table (one decimal), from which it colours the El Nino and La
# Nina episodes; the two-decimal text file above cannot reproduce its rounding.
DATASETS.update({
    "bachelor-2-oni-table": dict(
        url="https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso/oni/v6/",
        ext="html", ledger="data:b4-oni",
        terms="Oceanic Nino Index table (ERSSTv6), historical El Nino / La Nina episodes, "
              + _B4_CPC),
})


def derive_b4_oni_table(key):
    """season, year, anom_C (one decimal) from the rows 'YYYY v1 ... v12' of the CPC table."""
    import re
    with open(raw_path(key), encoding="utf8", errors="replace") as f:
        text = re.sub(r"<[^>]+>", " ", f.read())
    rows, seen = [], set()
    for m in re.finditer(r"\b(19[5-9][0-9]|20[0-9][0-9])((?:\s+-?[0-9]\.[0-9](?![0-9])){1,12})",
                         text):
        y = int(m.group(1))
        if y in seen:
            continue
        seen.add(y)
        for s, v in zip("DJF JFM FMA MAM AMJ MJJ JJA JAS ASO SON OND NDJ".split(),
                        m.group(2).split()):
            rows.append((s, y, v))
    _write_csv(key, ("season", "year", "anom_C"), rows)


DERIVE.update({"bachelor-2-oni": derive_b4_oni, "bachelor-2-roni": derive_b4_oni,
               "bachelor-2-nino34": derive_b4_nino34, "bachelor-2-nao": derive_b4_nao,
               "bachelor-2-oni-table": derive_b4_oni_table})


# Orbital elements and mid-month insolation of Berger and Loutre (1991), 0 to 5 Myr before
# 1950 at 1-kyr steps (ch. 25 orbital-forcing): NOAA NCEI / World Data Service for
# Paleoclimatology, Orbital Variations and Insolation Database (contribution 92-007).
DATASETS.update({
    "bachelor-2-orbit91": dict(
        url="https://www.ncei.noaa.gov/pub/data/paleo/climate_forcing/orbital_variations/"
            "insolation/orbit91",
        ext="txt", ledger="data:b4-orbit91",
        terms="Berger and Loutre (1991) via NOAA NCEI Paleoclimatology (US Government work; cite "
              "Berger and Loutre 1991, Quat. Sci. Rev. 10, 297-317)"),
})


def derive_b4_orbit91(key):
    """age_ka (positive before 1950), ecc, omega_deg (longitude of perihelion from the moving
    vernal equinox), obl_deg, prec (e sin omega), i65NJul, i65SJan, i15NJul, i15SJan (mid-month
    insolation, W/m2, solar constant 1360). Duplicate ages in the file are kept once."""
    rows, seen = [], set()
    with open(raw_path(key), encoding="ascii", errors="replace") as f:
        for line in f:
            c = line.split()
            if len(c) != 9:
                continue
            try:
                age = -int(c[0])
            except ValueError:
                continue
            if age in seen:
                continue
            seen.add(age)
            rows.append([age] + c[1:])
    rows.sort(key=lambda r: r[0])
    _write_csv(key, ("age_ka", "ecc", "omega_deg", "obl_deg", "prec", "i65NJul", "i65SJan",
                     "i15NJul", "i15SJan"), rows)


DERIVE.update({"bachelor-2-orbit91": derive_b4_orbit91})
# ----------------------------------------------------------------------------
# Book 4 (second writer): datasets of ch. 26-31, added 2026-10-23 by the second Book 4
# agent (sources/book4/PROGRESS-B.md). Ids start with the year.
# ----------------------------------------------------------------------------
# Cenozoic benthic foraminifer d18O and d13C splice (ch. 26 deep-time-climate): CENOGRID,
# Westerhold et al. 2020, PANGAEA child dataset S34 (binned and LOESS smoothed), CC BY 4.0.
DATASETS.update({
    "bachelor-2-cenogrid": dict(
        url="https://doi.pangaea.de/10.1594/PANGAEA.917717?format=textfile",
        ext="txt", ledger="data:b4-cenogrid",
        terms="Westerhold, T. (2020), S34. Binned and LOESS smoothed Cenozoic deep-sea benthic "
              "foraminifer stable carbon and oxygen isotope reference splice, PANGAEA, "
              "doi:10.1594/PANGAEA.917717, in the CENOGRID series doi:10.1594/PANGAEA.917503 "
              "(Westerhold et al. 2020, Science 369, 1383); CC BY 4.0"),
    # Phanerozoic CO2 (ch. 26): Foster, Royer and Lunt 2017, Nat. Commun. 8, 14845,
    # Supplementary Data 2 (LOESS fit to the CO2 compilation), CC BY 4.0.
    "bachelor-2-foster2017": dict(
        url="https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fncomms14845/"
            "MediaObjects/41467_2017_BFncomms14845_MOESM2875_ESM.xlsx",
        ext="xlsx", ledger="data:b4-foster2017",
        terms="Foster, G. L., Royer, D. L. and Lunt, D. J. (2017), Future climate forcing "
              "potentially without precedent in the last 420 million years, Nat. Commun. 8, "
              "14845, doi:10.1038/ncomms14845, Supplementary Data 2; CC BY 4.0"),
})


def _b4b_cenogrid_rows(key):
    """(age, d13C interp, d18O interp, d18O long-term LOESS) from the PANGAEA text file; the
    header ends at the first line '*/' and the column-name line that follows it."""
    out = []
    with open(raw_path(key), encoding="utf8") as f:
        lines = f.read().split("\n")
    i = lines.index("*/") + 2
    for line in lines[i:]:
        c = line.split("\t")
        if len(c) < 12 or not c[0]:
            continue
        out.append((float(c[0]), float(c[3]), float(c[6]), float(c[11])))
    return out


def derive_b4b_cenogrid(key):
    """Two files. bachelor-2-cenogrid.csv: age_Ma (centre of a 100 kyr bin), d13C and d18O
    (permil VPDB, means of the interpolated binned splice over the bin), d18O_lt (the
    long-term LOESS of the dataset at the bin centre, nearest row). bachelor-2-cenogrid-petm.csv:
    every row of the splice between 55.0 and 57.0 Ma (age_Ma, d13C, d18O)."""
    rows = _b4b_cenogrid_rows(key)
    out = []
    nbin = int(round(rows[-1][0] / 0.1))
    k = 0
    for b in range(nbin):
        lo, hi = b * 0.1, (b + 1) * 0.1
        sel = [r for r in rows[k:] if lo <= r[0] < hi]
        k += len(sel)
        if not sel:
            continue
        mid = lo + 0.05
        near = min(sel, key=lambda r: abs(r[0] - mid))
        out.append(("%.2f" % mid, "%.3f" % (sum(r[1] for r in sel) / len(sel)),
                    "%.3f" % (sum(r[2] for r in sel) / len(sel)), "%.3f" % near[3]))
    _write_csv(key, ("age_Ma", "d13C", "d18O", "d18O_lt"), out)
    _write_csv(key + "-petm", ("age_Ma", "d13C", "d18O"),
               [("%.3f" % r[0], "%.3f" % r[1], "%.3f" % r[2]) for r in rows if 55.0 <= r[0] <= 57.0])


def derive_b4b_foster(key):
    """age_Ma, co2 (ppm, the probability maximum of the LOESS fit), lo68 and hi68 (ppm, the
    68 % band): Supplementary Data 2, sheet 'LOESS Fit', columns A, B, D, E."""
    out = []
    for r in _b4_xlsx_rows(raw_path(key), "LOESS Fit"):
        try:
            v = [float(r[c]) for c in "ABDE"]
        except (KeyError, ValueError):
            continue
        out.append(("%.3f" % v[0], "%.1f" % v[1], "%.1f" % v[2], "%.1f" % v[3]))
    _write_csv(key, ("age_Ma", "co2", "lo68", "hi68"), out)


DERIVE.update({"bachelor-2-cenogrid": derive_b4b_cenogrid, "bachelor-2-foster2017": derive_b4b_foster})
# Historical effective radiative forcing 1750-2019 (ch. 27 anthropogenic-climate-change): IPCC
# AR6 WG1 Annex III Extended Data, Table A3.3 (best estimate, 5th and 95th percentiles), Zenodo
# record 5705391, CC BY 4.0.
_B4B_ERF = ("https://zenodo.org/api/records/5705391/files/"
            "table_A3.3_historical_ERF_1750-2019_%s.csv/content")
_B4B_ERF_TERMS = ("IPCC AR6 WG1 Annex III Extended Data (Smith, C. et al. 2021), Table A3.3 "
                  "historical ERF 1750-2019, %s, Zenodo doi:10.5281/zenodo.5705391; CC BY 4.0")
DATASETS.update({
    "bachelor-2-ar6-erf": dict(url=_B4B_ERF % "best_estimate", ext="csv",
                               ledger="data:b4-ar6-erf", terms=_B4B_ERF_TERMS % "best estimate"),
    "bachelor-2-ar6-erf-p05": dict(url=_B4B_ERF % "5th_percentile", ext="csv",
                                   ledger="data:b4-ar6-erf", terms=_B4B_ERF_TERMS % "5th percentile"),
    "bachelor-2-ar6-erf-p95": dict(url=_B4B_ERF % "95th_percentile", ext="csv",
                                   ledger="data:b4-ar6-erf", terms=_B4B_ERF_TERMS % "95th percentile"),
})


def _b4b_erf_table(key):
    with open(raw_path(key), encoding="utf8") as f:
        return {int(r["year"]): r for r in csv.DictReader(f)}


def derive_b4b_erf(key):
    """bachelor-2-ar6-erf.csv, W/m2 relative to 1750, one row per year 1750-2019: co2;
    other_ghg (CH4, N2O, halogenated gases, ozone, stratospheric water vapour); aerosol
    (aerosol-radiation + aerosol-cloud); other_anthro (contrails, black carbon on snow, land
    use); anthro (total anthropogenic) with its 5th and 95th percentiles (anthro_p05,
    anthro_p95, from the two percentile tables); volcanic; solar; total. Derived from the
    three tables together, whichever key is asked for."""
    best = _b4b_erf_table("bachelor-2-ar6-erf")
    p05 = _b4b_erf_table("bachelor-2-ar6-erf-p05")
    p95 = _b4b_erf_table("bachelor-2-ar6-erf-p95")
    out = []
    for y in sorted(best):
        r = best[y]
        v = {k: float(x) for k, x in r.items() if k != "year"}
        other = v["nonco2_wmghg"] + v["o3"] + v["h2o_stratospheric"]
        aer = v["aerosol-radiation_interactions"] + v["aerosol-cloud_interactions"]
        oth = v["contrails"] + v["bc_on_snow"] + v["land_use"]
        out.append((y, "%.4f" % v["co2"], "%.4f" % other, "%.4f" % aer, "%.4f" % oth,
                    "%.4f" % v["total_anthropogenic"],
                    "%.4f" % float(p05[y]["total_anthropogenic"]),
                    "%.4f" % float(p95[y]["total_anthropogenic"]),
                    "%.4f" % v["volcanic"], "%.4f" % v["solar"], "%.4f" % v["total"]))
    _write_csv("bachelor-2-ar6-erf", ("year", "co2", "other_ghg", "aerosol", "other_anthro",
                                      "anthro", "anthro_p05", "anthro_p95", "volcanic", "solar",
                                      "total"), out)


DERIVE.update({"bachelor-2-ar6-erf": derive_b4b_erf, "bachelor-2-ar6-erf-p05": derive_b4b_erf,
               "bachelor-2-ar6-erf-p95": derive_b4b_erf})
# Porphyry copper deposits of the world (ch. 29 ore-deposits): Singer, Berger and Moring
# (2008), USGS Open-File Report 2008-1155, tab-separated text table (Latin-1, CR line ends);
# tonnage in millions of metric tons at the lowest possible cut-off (production + reserves +
# resources), grades in percent (Cu, Mo) and g/t (Au, Ag). US Government work, public domain.
DATASETS.update({
    "bachelor-2-porphyry-cu": dict(
        url="https://pubs.usgs.gov/of/2008/1155/data/PorCuTX2008.txt", ext="txt",
        ledger="data:b4-porphyry-cu",
        terms="Singer, D.A., Berger, V.I. and Moring, B.C. (2008), Porphyry copper deposits of "
              "the world: database and grade and tonnage models, USGS Open-File Report "
              "2008-1155; US Government work, public domain"),
})


def derive_b4b_porphyry(key):
    """name, country, tonnage_Mt, cu_pct, mo_pct, au_gt, subtype (USGS type 17, 20c or 21a):
    the deposits with both a tonnage and a copper grade above zero."""
    text = open(raw_path(key), "rb").read().decode("latin-1")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    rows = list(csv.reader(io.StringIO(text), delimiter="\t"))
    h = rows[0]
    ix = {k: h.index(k) for k in ("NameDeposit", "Country", "Tonnage", "Copper grade",
                                  "Molybdenum grade", "Gold grade", "Subtype")}
    out = []
    for r in rows[1:]:
        try:
            t, cu = float(r[ix["Tonnage"]]), float(r[ix["Copper grade"]])
        except (ValueError, IndexError):
            continue
        if t <= 0 or cu <= 0:
            continue
        g = lambda k: float(r[ix[k]] or 0)
        out.append((r[ix["NameDeposit"]].strip(), r[ix["Country"]].strip(), "%g" % t, "%g" % cu,
                    "%g" % g("Molybdenum grade"), "%g" % g("Gold grade"),
                    r[ix["Subtype"]].strip()))
    _write_csv(key, ("name", "country", "tonnage_Mt", "cu_pct", "mo_pct", "au_gt", "subtype"),
               out)


DERIVE.update({"bachelor-2-porphyry-cu": derive_b4b_porphyry})
# Density of pure CO2 with depth (ch. 30 energy-geology): NIST Chemistry WebBook, SRD 69,
# thermophysical properties of fluid systems (Span and Wagner 1996 equation of state for CO2),
# one single-point isothermal query per depth along the conditions of the IPCC SRCCS (2005)
# Figure 5.2: surface 15 degC, geothermal gradient 25 degC/km, hydrostatic pressure (here fresh
# water, 1000 kg/m3, g = 9.80665 m/s2, plus one atmosphere). Depths 0 to 3000 m every 100 m.
_B4B_NIST = ("https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C124389&Type=IsoTherm"
             "&Digits=6&PLow=%.6f&PHigh=%.6f&PInc=1&T=%.4f&RefState=DEF&TUnit=C&PUnit=MPa"
             "&DUnit=kg%%2Fm3&HUnit=kJ%%2Fkg&WUnit=m%%2Fs&VisUnit=uPa*s&STUnit=N%%2Fm")
_B4B_NIST_TERMS = ("NIST Chemistry WebBook, NIST Standard Reference Database 69 (Lemmon, McLinden "
                   "and Friend), fluid properties of carbon dioxide from the Span and Wagner (1996) "
                   "equation of state; (c) U.S. Secretary of Commerce, Standard Reference Data Act; "
                   "single values cited with attribution")


def _b4b_co2_point(z):
    """(depth m, temperature degC, pressure MPa) of the SRCCS Figure 5.2 profile."""
    return z, 15.0 + 0.025 * z, 0.101325 + 1000.0 * 9.80665 * z / 1e6


for _z in range(0, 3001, 100):
    _d, _t, _p = _b4b_co2_point(_z)
    DATASETS["bachelor-2-co2-nist-z%04d" % _z] = dict(
        url=_B4B_NIST % (_p, _p, _t), ext="txt", ledger="data:b4-co2-density",
        terms=_B4B_NIST_TERMS)


def derive_b4b_co2(key):
    """bachelor-2-co2-density.csv: depth_m, t_c, p_mpa, rho (kg/m3), phase (NIST label), from
    the 31 single-point files, whichever key is asked for."""
    out = []
    for z in range(0, 3001, 100):
        with open(raw_path("bachelor-2-co2-nist-z%04d" % z), encoding="utf8") as f:
            lines = [ln for ln in f.read().split("\n") if ln.strip()]
        h = lines[0].split("\t")
        c = lines[1].split("\t")
        rho = float(c[h.index("Density (kg/m3)")])
        _, t, p = _b4b_co2_point(z)
        out.append((z, "%.3f" % t, "%.6f" % p, "%.3f" % rho, c[h.index("Phase")].strip()))
    _write_csv("bachelor-2-co2-density", ("depth_m", "t_c", "p_mpa", "rho", "phase"), out)


DERIVE.update({"bachelor-2-co2-nist-z%04d" % _z: derive_b4b_co2 for _z in range(0, 3001, 100)})
# ----------------------------------------------------------------------------
# end of Book 4 (second writer) sub-block
# ----------------------------------------------------------------------------
# ============================================================================
# end of Book 4 block
# ============================================================================


# ============================================================================
# Book 5: datasets used by Book 5 only (University Year 3). Ids start with the year.
# Added by the Book 5 agent, 2026-10-23 (sources/BATCH_BOOKS_1-5.md, Sync 3).
# ============================================================================
# Ice-sheet mass balance 1992-2020 (ch. 3 gravity-geodesy, ch. 24 glaciology): IMBIE 2021
# reconciled estimates, UK Polar Data Centre, doi:10.5285/77B64C55-7166-4A06-9DEF-2E400398E452,
# Open Government Licence v3.0 (the IMBIE open tables; no login).
_B5_IMBIE = ("https://ramadda.data.bas.ac.uk/repository/entry/get/%s?entryid=synth%%3A"
             "77b64c55-7166-4a06-9def-2e400398e452%%3A%s")
_B5_IMBIE_TERMS = ("IMBIE Team (2021), Antarctic and Greenland Ice Sheet mass balance 1992-2020 "
                   "for IPCC AR6, UK Polar Data Centre, doi:10.5285/77B64C55-7166-4A06-9DEF-"
                   "2E400398E452; Open Government Licence v3.0")
DATASETS.update({
    "bachelor-3-imbie-greenland": dict(
        url=_B5_IMBIE % ("imbie_greenland_2021_Gt.csv",
                         "L2ltYmllX2dyZWVubGFuZF8yMDIxX0d0LmNzdg%3D%3D"),
        ext="csv", ledger="data:b5-imbie", terms=_B5_IMBIE_TERMS),
    "bachelor-3-imbie-antarctica": dict(
        url=_B5_IMBIE % ("imbie_antarctica_2021_Gt.csv",
                         "L2ltYmllX2FudGFyY3RpY2FfMjAyMV9HdC5jc3Y%3D"),
        ext="csv", ledger="data:b5-imbie", terms=_B5_IMBIE_TERMS),
})


def derive_b5_imbie(key):
    """year, dm_gt_yr, dm_unc, cum_gt, cum_unc: the monthly IMBIE 2021 series as published
    (mass balance and its 1-sigma uncertainty in Gt/yr, cumulative mass change since 1992 and
    its uncertainty in Gt), columns renamed, values unchanged."""
    out = []
    with open(raw_path(key), encoding="utf8") as f:
        for r in csv.reader(f):
            if not r or not r[0][:1].isdigit():
                continue
            out.append(tuple(x.strip() for x in r[:5]))
    _write_csv(key, ("year", "dm_gt_yr", "dm_unc", "cum_gt", "cum_unc"), out)


DERIVE.update({"bachelor-3-imbie-greenland": derive_b5_imbie,
               "bachelor-3-imbie-antarctica": derive_b5_imbie})
# IGRF-14 (ch. 4 palaeomagnetism): Schmidt semi-normalised Gauss coefficients 1900-2025 and the
# secular variation 2025-2030, IAGA Division V-MOD, distributed by NOAA NCEI.
DATASETS.update({
    "bachelor-3-igrf14": dict(
        url="https://www.ngdc.noaa.gov/IAGA/vmod/coeffs/igrf14coeffs.txt",
        ext="txt", ledger="data:b5-igrf",
        terms="International Geomagnetic Reference Field, 14th generation (IAGA Division V, "
              "Working Group V-MOD, 2024), coefficient file distributed by NOAA NCEI; free to "
              "use with citation"),
})


def derive_b5_igrf(key):
    """gh, n, m, then one column per model epoch (g1900 ... g2025, nT) and sv (nT/yr,
    2025-2030): the coefficient table as published, header from the file's epoch row."""
    with open(raw_path(key), encoding="utf8") as f:
        lines = [ln.split() for ln in f if ln.strip() and not ln.startswith("#")]
    hdr = lines[1]
    epochs = [h for h in hdr[3:]]
    cols = ["gh", "n", "m"] + ["e%s" % e.split(".")[0] if "-" not in e else "sv" for e in epochs]
    out = [tuple(r) for r in lines[2:]]
    _write_csv(key, tuple(cols), out)


DERIVE.update({"bachelor-3-igrf14": derive_b5_igrf})
# Near-surface air temperature (ch. 22 climate-models, the Budyko-Sellers model): NCEP-NCAR
# Reanalysis 1 long-term monthly means 1991-2020 at sigma 0.995, 2.5-degree grid, the
# same server, terms and zonal-mean derivation as the Book 3 block's uwnd-sfc (its
# derive_b3_ncep25_zonal is called, not changed).
DATASETS.update({
    "bachelor-3-ncep-air-sfc": dict(
        url=_NCEP25 % ("surface/air.sig995", "air", "[0:1:11]", "[0:1:143]"),
        ext="txt", ledger="data:b5-ncep-air", terms=_NCEP_TERMS),
})
DERIVE.update({"bachelor-3-ncep-air-sfc": derive_b3_ncep25_zonal})
# Ch. 24 glaciology: (1) a west-east transect of the Greenland ice-sheet surface at 72.5 N,
# ETOPO1 Ice Surface every 6th node (0.1 degree), by NOAA ERDDAP (shared derive_etopo, called
# not changed); (2) Arctic sea-ice extent, monthly means for March (maximum) and September
# (minimum), NSIDC Sea Ice Index G02135 v4, derived by the Book 1 block's derive_b1_nsidc
# (called, not changed).
_B5_NSIDC_TERMS = ("NSIDC Sea Ice Index G02135 v4 (Fetterer et al. 2025, doi:10.7265/a98x-0f50); "
                   "free to use, citation required (cited in the caption and the credits)")
DATASETS.update({
    "bachelor-3-etopo-greenland": dict(
        url="https://coastwatch.pfeg.noaa.gov/erddap/griddap/etopo180.csv?"
            "altitude%5B(72.5):1:(72.5)%5D%5B(-58):6:(-20)%5D",
        ext="csv", ledger="data:b5-etopo-greenland",
        terms="NOAA NCEI ETOPO1 Ice Surface (Amante and Eakins 2009), every 6th node (0.1 degree) "
              "along 72.5 N, 58-20 W, by NOAA ERDDAP; US Government work, public domain"),
    "bachelor-3-nsidc-mar-extent": dict(
        url="https://noaadata.apps.nsidc.org/NOAA/G02135/north/monthly/data/N_03_extent_v4.0.csv",
        ext="csv", ledger="data:b5-nsidc-extent", terms=_B5_NSIDC_TERMS),
    "bachelor-3-nsidc-sep-extent": dict(
        url="https://noaadata.apps.nsidc.org/NOAA/G02135/north/monthly/data/N_09_extent_v4.0.csv",
        ext="csv", ledger="data:b5-nsidc-extent", terms=_B5_NSIDC_TERMS),
})
DERIVE.update({"bachelor-3-etopo-greenland": derive_etopo,
               "bachelor-3-nsidc-mar-extent": derive_b1_nsidc,
               "bachelor-3-nsidc-sep-extent": derive_b1_nsidc})
# Ch. 25 remote sensing: five laboratory reflectance spectra from the ECOSTRESS Spectral
# Library v1.0 (Meerdink et al. 2019; formerly the ASTER library, Baldridge et al. 2009),
# one ASCII file each: green rye grass, tap water, a brown sand soil, kaolinite and
# haematite (fine powders). The USGS splib07 release (ScienceBase) refused scripted access
# (403, browser challenge) on 2026-10-23, hence this approved alternative.
_B5_ECO = "https://speclib.jpl.nasa.gov/ecospeclibdata/%s.spectrum.txt"
_B5_ECO_TERMS = ("ECOSTRESS Spectral Library v1.0 (Meerdink, Hook, Roberts and Abbott 2019, "
                 "Remote Sens. Environ. 230, 111196; Baldridge et al. 2009); reproduced through "
                 "the courtesy of the Jet Propulsion Laboratory, California Institute of "
                 "Technology, Pasadena, California (citation requested; values plotted, credited "
                 "in the caption and the credits)")
_B5_ECO_FILES = {
    "grass": "vegetation.grass.unknown.unknown.all.grass.jhu.becknic",
    "water": "water.tapwater.none.liquid.all.tapwater.jhu.becknic",
    "soil": "soil.entisol.quartzipsamment.none.all.87p706.jhu.becknic",
    "kaolinite": "mineral.silicate.phyllosilicate.fine.vswir.ps-1a.jpl.beckman",
    "hematite": "mineral.oxide.none.fine.vswir.o-1a.jpl.beckman",
}
DATASETS.update({
    "bachelor-3-eco-%s" % k: dict(url=_B5_ECO % v, ext="txt", ledger="data:b5-ecostress",
                                  terms=_B5_ECO_TERMS)
    for k, v in _B5_ECO_FILES.items()})


def derive_b5_eco(key):
    """um, refl: wavelength (micrometres) and reflectance (fraction, the published percent
    divided by 100), 0.40-14.0 um (the TIR part exists for grass, water and soil only),
    sorted by wavelength; the header lines dropped."""
    out = []
    with open(raw_path(key), encoding="latin-1") as f:
        for ln in f:
            p = ln.split()
            if len(p) != 2:
                continue
            try:
                um, pc = float(p[0]), float(p[1])
            except ValueError:
                continue
            if 0.4 - 1e-9 <= um <= 14.0 + 1e-9:
                out.append((um, pc / 100.0))
    out.sort()
    _write_csv(key, ("um", "refl"), [("%.4f" % a, "%.5f" % b) for a, b in out])


DERIVE.update({"bachelor-3-eco-%s" % k: derive_b5_eco for k in _B5_ECO_FILES})
# Ch. 28 exoplanets: the NASA Exoplanet Archive Planetary Systems Composite Parameters table
# (pscomppars, one row per confirmed planet), by the archive's public TAP service; the
# columns needed for the mass-radius and period-radius diagrams and the counts by method.
_B5_PS_COLS = ("pl_name,discoverymethod,disc_year,pl_orbper,pl_orbsmax,pl_rade,pl_radeerr1,"
               "pl_radeerr2,pl_bmasse,pl_bmasseerr1,pl_bmasseerr2,pl_bmassprov,tran_flag,"
               "st_teff,st_rad,st_mass")
DATASETS.update({
    "bachelor-3-pscomp": dict(
        url="https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+%s+from+"
            "pscomppars&format=csv" % _B5_PS_COLS,
        ext="csv", ledger="data:b5-pscomp",
        terms="NASA Exoplanet Archive, Planetary Systems Composite Parameters table, "
              "operated by the California Institute of Technology under "
              "contract with NASA under the Exoplanet Exploration Program; public, "
              "acknowledgement requested (in the caption and the credits)"),
})


def derive_b5_pscomp(key):
    """name, method, year, period_d, a_au, rade, rade_e1, rade_e2, masse, masse_e1, masse_e2,
    mass_prov, transit, teff, st_rad, st_mass: one row per confirmed planet as published
    (radii and masses in Earth units, period in days, semi-major axis in au), sorted by name; empty cells kept
    empty, trailing zeros of the archive's fixed-point numbers dropped (values unchanged)."""
    def tidy(x):
        x = x.strip()
        if "." in x and x.replace(".", "", 1).lstrip("-").isdigit():
            x = x.rstrip("0").rstrip(".")
        return x
    out = []
    with open(raw_path(key), encoding="utf8") as f:
        rd = csv.reader(f)
        next(rd)
        for r in rd:
            if r:
                out.append(tuple(tidy(x) for x in r))
    out.sort(key=lambda r: r[0])
    _write_csv(key, ("name", "method", "year", "period_d", "a_au", "rade", "rade_e1", "rade_e2",
                     "masse", "masse_e1", "masse_e2", "mass_prov", "transit", "teff",
                     "st_rad", "st_mass"), out)


DERIVE.update({"bachelor-3-pscomp": derive_b5_pscomp})
# Ch. 28 exoplanets: model mass-radius curves of L. Zeng and others (2019, PNAS 116, 9723;
# 2016, ApJ 819, 127), the tables published on the first author's model page (masses and
# radii in Earth units; radius at the 1 mbar level for the curves with volatiles).
_B5_ZENG = "https://lweb.cfa.harvard.edu/~lzeng/tables/%s.txt"
_B5_ZENG_TERMS = ("Mass-radius tables of L. Zeng et al. (2019, PNAS 116, 9723-9728; 2016, ApJ "
                  "819, 127), from the author's planet-models page; model values plotted with "
                  "citation (caption and credits)")
_B5_ZENG_FILES = {
    "iron": "massradiusFe",
    "earthlike": "massradiusEarthlikeRocky",
    "water50": "massradius_50percentH2O_500K_1mbar",
    "h2-2pc": "Earthlike2h500K1mbar",
}
DATASETS.update({
    "bachelor-3-zeng-%s" % k: dict(url=_B5_ZENG % v, ext="txt", ledger="data:b5-zeng",
                                   terms=_B5_ZENG_TERMS)
    for k, v in _B5_ZENG_FILES.items()})


def derive_b5_zeng(key):
    """mass, radius: the model curve as published (Earth units), two whitespace-separated
    columns per line."""
    out = []
    with open(raw_path(key), encoding="utf8") as f:
        for ln in f:
            p = ln.split()
            if len(p) >= 2:
                out.append((float(p[0]), float(p[1])))
    _write_csv(key, ("mass", "radius"), [("%g" % a, "%g" % b) for a, b in out])


DERIVE.update({"bachelor-3-zeng-%s" % k: derive_b5_zeng for k in _B5_ZENG_FILES})
# Ch. 29 Milky Way and galaxies: the OGLE-IV classical Cepheids of the Large Magellanic
# Cloud (Soszynski et al. 2015, Acta Astron. 65, 297, 2019 update), as distributed by the
# CDS (VizieR J/AcA/65/297, file lmccep.dat.gz, gzipped fixed-width; byte ranges from its ReadMe).
DATASETS.update({
    "bachelor-3-ogle-lmc-cep": dict(
        url="https://cdsarc.cds.unistra.fr/ftp/J/AcA/65/297/lmccep.dat.gz",
        ext="dat.gz", ledger="data:b5-ogle-lmc-cep",
        terms="OGLE Collection of Variable Stars, classical Cepheids in the Magellanic "
              "System, I. Soszynski et al. (2015), Acta Astron. 65, 297, distributed by "
              "the CDS, Strasbourg (VizieR J/AcA/65/297); free for scientific and "
              "educational use with citation of the authors and the publication"),
})


def derive_b5_ogle_cep(key):
    """mode, star, i_mag, v_mag, period_d: one row per Cepheid with both mean magnitudes,
    as published (intensity-mean I and V magnitudes, longest period in days); columns from
    the CDS ReadMe byte ranges 1-8, 10-26, 29-34, 36-41, 43-53. Stars lacking a magnitude
    ("-") are left out."""
    import gzip
    out = []
    with gzip.open(raw_path(key), "rt", encoding="utf8") as f:
        for ln in f:
            mode, star = ln[0:8].strip(), ln[9:26].strip()
            i_mag, v_mag, per = ln[28:34].strip(), ln[35:41].strip(), ln[42:53].strip()
            if not star or "-" in (i_mag, v_mag) or not i_mag or not v_mag or not per:
                continue
            out.append((mode, star, i_mag, v_mag, per))
    _write_csv(key, ("mode", "star", "i_mag", "v_mag", "period_d"), out)


DERIVE.update({"bachelor-3-ogle-lmc-cep": derive_b5_ogle_cep})
# Ch. 30 origin of the elements: the solar abundances of Asplund, Amarsi and Grevesse
# (2021, A&A 653, A141), read from the LaTeX source of the paper on arXiv (2105.01661),
# which carries its tables as text: Table 2 (photosphere and CI chondrites, log eps with
# log eps(H) = 12) and Table B.1 (proto-solar isotopic fractions and log eps).
DATASETS.update({
    "bachelor-3-asplund21": dict(
        url="https://arxiv.org/e-print/2105.01661",
        ext="tar.gz", ledger="data:b5-asplund21",
        terms="M. Asplund, A. M. Amarsi and N. Grevesse (2021), The chemical make-up of "
              "the Sun: a 2020 vision, A&A 653, A141 (arXiv:2105.01661v2, arXiv "
              "non-exclusive distribution licence); numerical values used with citation"),
})


def _b5_asplund_tex(key):
    import tarfile
    with tarfile.open(raw_path(key), "r:gz") as t:
        return t.extractfile("sun_abund2.tex").read().decode("utf8")


def _b5_cells(line):
    line = line.split("\\\\")[0]
    return [c.strip() for c in line.split("&")]


def _b5_pm(cell):
    """'$ 12.00 \\pm 0.00 $' -> ('12.00', '0.00'); empty cell -> ('', '')."""
    cell = cell.replace("$", "").strip()
    if not cell:
        return "", ""
    v, e = cell.split("\\pm")
    return v.strip(), e.strip()


def derive_b5_asplund(key):
    """Two tables. bachelor-3-asplund21-elements.csv: Z, el, phot, phot_err, ci, ci_err,
    comment (blank photosphere where the paper gives none). bachelor-3-asplund21-isotopes.csv:
    Z (from the element symbol), el, A, frac_pct, logeps (proto-solar), long_lived (1 for the isotopes the table
    marks as long-lived radioactive, whose values are corrected for decay)."""
    tex = _b5_asplund_tex(key).splitlines()
    i = next(k for k, ln in enumerate(tex) if "\\label{t:abund}" in ln)
    j = next(k for k in range(i, len(tex)) if "\\end{tabular}" in tex[k])
    els = []
    for ln in tex[i:j]:
        c = _b5_cells(ln)
        if len(c) < 10 or not c[0].isdigit():
            continue
        for h in (c[0:5], c[5:10]):
            if not h[0].isdigit():
                continue
            p, pe = _b5_pm(h[2])
            m, me = _b5_pm(h[3])
            els.append((int(h[0]), h[1], p, pe, m, me, h[4]))
    els.sort()
    _write_csv("bachelor-3-asplund21-elements", ("Z", "el", "phot", "phot_err", "ci", "ci_err",
                                                 "comment"), els)
    zof = {e[1]: e[0] for e in els}
    i = next(k for k, ln in enumerate(tex) if "\\label{t:isotopes}" in ln)
    j = next(k for k in range(i, len(tex)) if "\\end{longtable}" in tex[k])
    iso = []
    for ln in tex[i:j]:
        c = _b5_cells(ln)
        if len(c) < 5 or not any(c[k].isdigit() for k in range(0, len(c) - 4, 5)):
            continue
        for k in range(0, len(c) - 4, 5):
            h = c[k:k + 5]
            if h[0].isdigit():
                star = "\\tablefootmark" in h[1]
                el = h[1].split("\\")[0].strip()
                # Z from the symbol: in six rows of the table (the first isotope of Rh,
                # Pd, Ag, Cd, In and Sn) the printed Z is that of the previous element
                iso.append((zof[el], el, int(h[2]), h[3], h[4], int(star)))
    iso.sort()
    _write_csv("bachelor-3-asplund21-isotopes", ("Z", "el", "A", "frac_pct", "logeps",
                                                 "long_lived"), iso)


DERIVE.update({"bachelor-3-asplund21": derive_b5_asplund})
# Ch. 30: Maxwellian-averaged neutron-capture cross sections (KADoNiS v0.3, the
# recommended (n,gamma) MACS at kT = 5-100 keV, tab-separated, in millibarn), and the
# metallicities of the Geneva-Copenhagen survey re-analysed by Casagrande et al. (2011,
# A&A 530, A138; CDS J/A+A/530/A138, catalog.dat.gz, byte ranges from its ReadMe).
DATASETS.update({
    "bachelor-3-kadonis-macs": dict(
        url="https://exp-astro.de/kadonis1.0/maketable.php?type=macs",
        ext="txt", ledger="data:b5-kadonis",
        terms="KADoNiS v0.3, Karlsruhe Astrophysical Database of Nucleosynthesis in Stars, "
              "I. Dillmann, R. Plag, F. Kaeppeler and T. Rauscher (2009), online database "
              "of recommended values, cited as its authors ask"),
    "bachelor-3-gcs": dict(
        url="https://cdsarc.cds.unistra.fr/ftp/J/A+A/530/A138/catalog.dat.gz",
        ext="dat.gz", ledger="data:b5-gcs",
        terms="Casagrande et al. (2011), A&A 530, A138, distributed by the CDS, "
              "Strasbourg (VizieR J/A+A/530/A138); free for scientific and educational "
              "use with citation of the authors and the publication"),
})


def derive_b5_kadonis(key):
    """Z, A, isomer, el, macs30_mb, err30_mb: the recommended MACS at kT = 30 keV and its
    uncertainty (rows without a 30 keV value are left out)."""
    out = []
    with open(raw_path(key), encoding="utf8") as f:
        next(f)
        for ln in f:
            c = ln.rstrip("\n").split("\t")
            if len(c) < 17 or c[9] in ("", "-"):
                continue
            out.append((int(c[0]), int(c[1]), c[2].strip() or "-", c[3].strip(),
                        "%.6g" % float(c[9]), "%.6g" % float(c[15])))
    _write_csv(key, ("Z", "A", "isomer", "el", "macs30_mb", "err30_mb"), out)


def derive_b5_gcs(key):
    """hip, feh, mh, afe, mass_padova: the stars of 'irfm' pedigree (best photometry,
    likely single and non-variable) with a metallicity; columns from the ReadMe byte
    ranges 6-11, 76-80, 82-86, 88-92, 383-387 (median Padova mass; -9.99 when absent)."""
    import gzip
    out = []
    with gzip.open(raw_path(key), "rt", encoding="utf8") as f:
        for ln in f:
            if ln[0:4] != "irfm":
                continue
            feh = ln[75:80].strip()
            if not feh or feh == "-9.99":
                continue
            out.append((ln[5:11].strip() or "-", feh, ln[81:86].strip(), ln[87:92].strip(),
                        ln[382:387].strip() or "-9.99"))
    _write_csv(key, ("hip", "feh", "mh", "afe", "mass_padova"), out)


DERIVE.update({"bachelor-3-kadonis-macs": derive_b5_kadonis,
               "bachelor-3-gcs": derive_b5_gcs})
# Ch. 30: half-lives and main decay modes of the ground states of all nuclides (IAEA
# Nuclear Data Section, Live Chart of Nuclides API, from ENSDF), to follow the s path.
DATASETS.update({
    "bachelor-3-iaea-gs": dict(
        url="https://www-nds.iaea.org/relnsd/v1/data?fields=ground_states&nuclides=all",
        ext="csv", ledger="data:b5-iaea-gs",
        terms="IAEA Nuclear Data Section, Live Chart of Nuclides, ground-state data from "
              "ENSDF (and NUBASE where ENSDF gives none), openly served by the IAEA API; "
              "cited as the source"),
})


def derive_b5_iaea(key):
    """Z, N, el, half_life_s (blank for stable), decay_1, decay_1_pct: nuclides with
    Z <= 92 that are stable or live longer than one second."""
    out = []
    with open(raw_path(key), encoding="latin-1") as f:
        for r in csv.DictReader(f):
            try:
                z, n = int(r["z"]), int(r["n"])
            except ValueError:
                continue
            if z < 1 or z > 92:
                continue
            if r["half_life"].strip() == "STABLE":
                out.append((z, n, r["symbol"], "", "", ""))
                continue
            try:
                t = float(r["half_life_sec"])
            except ValueError:
                continue
            if t >= 1:
                out.append((z, n, r["symbol"], "%.6g" % t, r["decay_1"].strip(),
                            r["decay_1_%"].strip()))
    _write_csv(key, ("Z", "N", "el", "half_life_s", "decay_1", "decay_1_pct"), out)


DERIVE.update({"bachelor-3-iaea-gs": derive_b5_iaea})
# ============================================================================
# end of Book 5 block
# ============================================================================


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

"""The Phanerozoic Earth (Year 2, phanerozoic-earth): palaeogeographic maps, sea level since
250 Ma, the ridge-volume model of long-term sea level, the hypsometric curve and flooding,
and the timeline of mass extinctions, large igneous provinces and oceanic anoxic events.

  maps        today's coastlines carried back to 0, 50, 100, 200, 300, 500 Ma in the plate
              model of Merdith et al. 2021 (GPlates Web Service; data:b4-palaeocoast), and four
              cities (data:b4-palaeopos; 999.99 = not in the model at that time). Mollweide
              projection centred on 0 E (figdata/shared/geo.py), x and y in Earth radii.
  sealevel    Haq et al. 1987 and the New Jersey backstripped curve with its estimated
              lowstands (Kominz et al. 2008), both as tabulated in the Miller et al. 2005 NOAA
              study (data:b4-sealevel), 2012 time scale; long-term curves are 10-Myr running
              means (centred, only where the window is full).
  ridge       depth of the ocean floor against age (ps77:depth-age): half-space law
              d = 2500 + 350 sqrt(t) m; plate law d = 6400 - 3200 exp(-t/62.8) m beyond the
              age where the two laws cross (26.3 Myr), the half-space law before. A steady
              ocean floor of area A_f, made at ridges and destroyed at age tau, with every age
              equally represented ("uniform" model): mean depth = average of d over 0..tau.
              Doubling the spreading rate at fixed A_f and ridge length halves tau. Sea-level
              rise = (rho_m - rho_w)/rho_m * (A_f/A_o) * (decrease of the mean depth), with
              A_f the area of the age grid (Book 2 row data:b2-seafloor-age, read-only csv),
              A_o = 361.84e6 km2 (charette:ocean-volume), rho_m = 3300 (katz03:thermo),
              rho_w = 1025 kg/m3 (noaa:seawater-1025); tau = twice the mean age 64.2 Myr of
              seton:mean-age.
  agehist     area of ocean floor in 10-Myr age bins (the age grid, one-degree cells
              weighted by the cosine of the latitude), Mkm2.
  hyps        hypsometric curve from the shared ETOPO1 one-degree grid (data:etopo-1deg):
              per cent of the Earth's surface above each elevation; land area flooded by a
              sea-level rise h (area of the cells with 0 < z <= h).
  extinct     the big five (ages and marine genus losses of Kaiho 2022, Table 1, Sepkoski
              1996 column; kaiho22:table), large igneous provinces (cr03:table), oceanic
              anoxic events (zaffani24:oaes), the Chicxulub impact (cee26:chicxulub).

  part map-<t>     x y          (land rings, blank line between rings)
  part cities-<t>  city tag x y lat
  part grat        x y          (graticule: parallels every 30 deg, meridians every 60 deg)
  part sealevel-haq / -kominz / -haqlt / -kominzlt   age_ma sl_m
  part ridge       f ds_hs ds_plate     (sea-level rise, m, against the spreading-rate factor)
  part depth       t d_hs d_plate       (depth--age laws)
  part agehist     age area_Mkm2 uniform_Mkm2
  part hyps        pct z                (cumulative per cent of surface above z)
  part flood       h flooded_pct        (per cent of today's land flooded by a rise h)
  part ext / lip / oae   age value label
  part numbers     key value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
from geo import mollweide  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")
TIMES = (0, 50, 100, 200, 300, 500)


def read(name):
    with open(os.path.join(DERIVED, name + ".csv"), encoding="utf8") as f:
        return list(csv.DictReader(f))


# --- maps -------------------------------------------------------------------------------
def map_rings(t):
    """Projected land rings at t Ma: a list of lists of (x, y)."""
    rings, cur, last = [], [], None
    for r in read("bachelor-2-palaeocoast-%d" % t):
        if r["ring"] != last and cur:
            rings.append(cur)
            cur = []
        last = r["ring"]
        cur.append(mollweide(float(r["lon"]), float(r["lat"])))
    if cur:
        rings.append(cur)
    return rings


def cities(t):
    """(city, lon, lat) at t Ma; lon and lat None when the model has no position."""
    if t == 0:
        return [("Paris", 2.3488, 48.85341), ("NewYork", -74.00597, 40.71427),
                ("Sydney", 151.20732, -33.86785), ("CapeTown", 18.42322, -33.92584)]
    out = []
    for r in read("bachelor-2-palaeopos-%d" % t):
        lon, lat = float(r["lon"]), float(r["lat"])
        out.append((r["city"], None, None) if abs(lon) > 360 else (r["city"], lon, lat))
    return out


TAGS = {"Paris": "P", "NewYork": "N", "Sydney": "S", "CapeTown": "C"}


def graticule():
    lines = []
    for lat in (-60, -30, 0, 30, 60):
        lines.append([mollweide(lon, lat) for lon in range(-180, 181, 5)])
    for lon in (-180, -120, -60, 0, 60, 120, 180):
        lon_ = lon if abs(lon) < 180 else math.copysign(179.999, lon)
        lines.append([mollweide(lon_, lat) for lat in range(-90, 91, 5)])
    return lines


# --- sea level --------------------------------------------------------------------------
def sealevel(name, col):
    return [(float(r["age_ma"]), float(r[col])) for r in read(name)]


def running_mean(series, window=10.0, step=1.0):
    """Centred running mean of an irregular series, evaluated every `step` Myr where the whole
    window lies inside the record."""
    a0, a1 = series[0][0], series[-1][0]
    out = []
    t = math.ceil(a0 + window / 2)
    while t <= a1 - window / 2:
        vals = [v for a, v in series if t - window / 2 <= a <= t + window / 2]
        out.append((t, sum(vals) / len(vals)))
        t += step
    return out


# --- ridge volume -----------------------------------------------------------------------
D0, C_HS = 2500.0, 350.0
D_INF, D_AMP, T_PL = 6400.0, 3200.0, 62.8
RHO_M, RHO_W = 3300.0, 1025.0
A_OCEAN = 361.84e6                 # km2
MEAN_AGE = 64.2                    # Myr, whole grid (seton:mean-age)
TAU = 2 * MEAN_AGE


def depth_hs(t):
    return D0 + C_HS * math.sqrt(t)


def t_cross():
    lo, hi = 10.0, 40.0
    f = lambda t: depth_hs(t) - (D_INF - D_AMP * math.exp(-t / T_PL))
    for _ in range(80):
        m = 0.5 * (lo + hi)
        if f(lo) * f(m) <= 0:
            hi = m
        else:
            lo = m
    return 0.5 * (lo + hi)


T_X = t_cross()


def depth_plate(t):
    return depth_hs(t) if t <= T_X else D_INF - D_AMP * math.exp(-t / T_PL)


def mean_depth(tau, law=depth_hs, n=4000):
    """Mean depth of a floor whose ages are spread evenly over 0..tau (Simpson's rule)."""
    if law is depth_hs:
        return D0 + 2.0 / 3.0 * C_HS * math.sqrt(tau)
    h = tau / n
    s = law(0.0) + law(tau)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * law(i * h)
    return s * h / 3 / tau


def floor_area():
    """Area of the ocean floor in the age grid (Mkm2-scale, km2), one-degree cells."""
    a = 0.0
    da = math.radians(1.0) ** 2 * 6371.0 ** 2
    for r in read("grade-11-seafloor-age"):
        a += da * math.cos(math.radians(float(r["lat"])))
    return a


def sea_rise(f, law=depth_hs, tau=TAU, a_floor=None):
    """Sea-level rise (m) when the spreading rate is multiplied by f (ages scale by 1/f)."""
    a_floor = floor_area() if a_floor is None else a_floor
    dd = mean_depth(tau, law) - mean_depth(tau / f, law)
    return (RHO_M - RHO_W) / RHO_M * a_floor / A_OCEAN * dd


def factor_for(rise, law=depth_hs, a_floor=None):
    lo, hi = 1.0, 4.0
    for _ in range(80):
        m = 0.5 * (lo + hi)
        if sea_rise(m, law, a_floor=a_floor) < rise:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def age_hist(width=10.0):
    da = math.radians(1.0) ** 2 * 6371.0 ** 2
    bins = {}
    for r in read("grade-11-seafloor-age"):
        b = int(float(r["age"]) // width)
        bins[b] = bins.get(b, 0.0) + da * math.cos(math.radians(float(r["lat"])))
    return bins


# --- hypsometry -------------------------------------------------------------------------
def cells():
    out = []
    for r in read("etopo-1deg"):
        out.append((float(r["elev_m"]), math.cos(math.radians(float(r["lat"])))))
    return out


def hypsometry():
    """(per cent of surface above z, z) for z every 100 m."""
    cs = cells()
    tot = sum(w for _, w in cs)
    zmin = int(min(z for z, _ in cs) // 100 * 100)
    zmax = int(max(z for z, _ in cs) // 100 * 100 + 100)
    return [(100.0 * sum(w for z, w in cs if z > lev) / tot, lev) for lev in range(zmin, zmax + 1, 100)]


def flooded_pct(h, cs=None):
    cs = cells() if cs is None else cs
    land = sum(w for z, w in cs if z > 0)
    return 100.0 * sum(w for z, w in cs if 0 < z <= h) / land


def floor_mean_depth():
    """Mean depth (m) of the ETOPO1 one-degree cells below sea level that carry an age."""
    el = {(r["lat"], r["lon"]): float(r["elev_m"]) for r in read("etopo-1deg")}
    num = den = 0.0
    for r in read("grade-11-seafloor-age"):
        z = el.get((r["lat"], r["lon"]))
        if z is not None and z < 0:
            w = math.cos(math.radians(float(r["lat"])))
            num += -z * w
            den += w
    return num / den


def level_for_volume(v_km3, cs=None):
    """Rise s (m) of a sea of today's area A_o that spreads over the land it floods, for an
    added volume v (km3): v = integral from 0 to s of (A_o + land area below z) dz, with the
    land of the one-degree grid scaled to the Earth's surface."""
    cs = cells() if cs is None else cs
    tot = sum(w for _, w in cs)
    earth = 4 * math.pi * 6371.0 ** 2
    ws = sorted((z, w) for z, w in cs if z > 0)
    s, vol, i, below = 0.0, 0.0, 0, 0.0
    step = 0.1
    while True:
        while i < len(ws) and ws[i][0] <= s:
            below += ws[i][1]
            i += 1
        area = A_OCEAN + below / tot * earth
        dv = area * step / 1000.0
        if vol + dv >= v_km3:
            return s + (v_km3 - vol) / area * 1000.0
        vol += dv
        s += step


def land_fraction(cs=None):
    cs = cells() if cs is None else cs
    return sum(w for z, w in cs if z > 0) / sum(w for _, w in cs)


# --- extinctions, provinces, anoxic events ---------------------------------------------
EXTINCT = ((444.0, 52, "end-Ordovician"), (372.0, 41, "Late Devonian"),
           (251.9, 66, "end-Permian"), (201.4, 46, "end-Triassic"), (66.0, 45, "end-Cretaceous"))
LIPS = ((259.0, "Emeishan"), (250.0, "Siberian"), (201.0, "CAMP"), (183.0, "Karoo--Ferrar"),
        (133.0, "Paran\\'a--Etendeka"), (122.0, "Ontong Java"), (65.5, "Deccan"),
        (61.0, "N. Atlantic"), (30.0, "Ethiopia"), (16.0, "Columbia R."))
OAES = ((183.0, "T-OAE"), (120.0, "OAE 1a"), (111.0, "OAE 1b"), (94.0, "OAE 2"))


def numbers():
    af = floor_area()
    cs = cells()
    haq = sealevel("bachelor-2-miller2005-haq87", "haq")
    kom = sealevel("bachelor-2-miller2005-kominz08", "backstrip-low")
    haqlt, komlt = running_mean(haq), running_mean(kom)
    hmax = max(haqlt, key=lambda p: p[1])
    kmax = max(komlt, key=lambda p: p[1])
    k80 = [v for a, v in komlt if 75 <= a <= 85]
    rise2 = sea_rise(2.0, a_floor=af)
    d = {"A_floor_Mkm2": round(af / 1e6, 1), "A_floor_frac": round(af / A_OCEAN, 4),
         "tau": TAU, "t_cross": round(T_X, 1),
         "dbar_hs": round(mean_depth(TAU), 1), "dbar_hs_half": round(mean_depth(TAU / 2), 1),
         "dbar_pl": round(mean_depth(TAU, depth_plate), 1),
         "dbar_pl_half": round(mean_depth(TAU / 2, depth_plate), 1),
         "rise2_hs": round(rise2, 1), "rise2_pl": round(sea_rise(2.0, depth_plate, a_floor=af), 1),
         "f_for_100_hs": round(factor_for(100.0, a_floor=af), 3),
         "f_for_100_pl": round(factor_for(100.0, depth_plate, a_floor=af), 3),
         "iso_factor": round((RHO_M - RHO_W) / RHO_M, 4),
         "land_frac": round(land_fraction(cs), 4),
         "flood_100": round(flooded_pct(100, cs), 1), "flood_200": round(flooded_pct(200, cs), 1),
         "flood_rise2": round(flooded_pct(rise2, cs), 1),
         "haq_lt_max": round(hmax[1], 1), "haq_lt_max_age": hmax[0],
         "kom_lt_max": round(kmax[1], 1), "kom_lt_max_age": kmax[0],
         "kom_lt_75_85": round(sum(k80) / len(k80), 1),
         "haq_raw_max": max(v for _, v in haq), "haq_raw_min": min(v for _, v in haq)}
    for h in (300, 400, 500):
        d["flood_%d" % h] = round(flooded_pct(h, cs), 1)
    d["floor_mean_depth"] = round(floor_mean_depth())
    d["level_rise2_spread"] = round(level_for_volume(rise2 * A_OCEAN / 1000.0, cs), 1)
    hist = age_hist()
    d["floor_lt_60_pct"] = round(100 * sum(v for b, v in hist.items() if b < 6) / sum(hist.values()), 1)
    return d


if __name__ == "__main__":
    for t in TIMES:
        rows = []
        for ring in map_rings(t):
            if rows:
                rows.append(())
            rows += [(round(x, 4), round(y, 4)) for x, y in ring]
        write_table(__file__, ("x", "y"), rows, part="map-%d" % t)
        crow = []
        for name, lon, lat in cities(t):
            if lon is None:
                continue
            x, y = mollweide(lon, lat)
            crow.append((name, TAGS[name], round(x, 4), round(y, 4), round(lat, 1)))
        write_table(__file__, ("city", "tag", "x", "y", "lat"), crow, part="cities-%d" % t)
    rows = []
    for line in graticule():
        if rows:
            rows.append(())
        rows += [(round(x, 4), round(y, 4)) for x, y in line]
    write_table(__file__, ("x", "y"), rows, part="grat")
    haq = sealevel("bachelor-2-miller2005-haq87", "haq")
    kom = sealevel("bachelor-2-miller2005-kominz08", "backstrip-low")
    write_table(__file__, ("age_ma", "sl_m"), haq, part="sealevel-haq")
    write_table(__file__, ("age_ma", "sl_m"), kom, part="sealevel-kominz")
    write_table(__file__, ("age_ma", "sl_m"), [(a, round(v, 1)) for a, v in running_mean(haq)],
                part="sealevel-haqlt")
    write_table(__file__, ("age_ma", "sl_m"), [(a, round(v, 1)) for a, v in running_mean(kom)],
                part="sealevel-kominzlt")
    af = floor_area()
    write_table(__file__, ("f", "ds_hs", "ds_plate"),
                [(round(f, 2), round(sea_rise(f, a_floor=af), 1),
                  round(sea_rise(f, depth_plate, a_floor=af), 1))
                 for f in [1.0 + 0.05 * i for i in range(0, 41)]], part="ridge")
    write_table(__file__, ("t", "d_hs", "d_plate"),
                [(t, round(depth_hs(t), 1), round(depth_plate(t), 1)) for t in range(0, 201, 2)],
                part="depth")
    hist = age_hist()
    uni = af / 1e6 / (TAU / 10.0)
    write_table(__file__, ("age", "area_Mkm2", "uniform_Mkm2"),
                [(b * 10 + 5, round(hist.get(b, 0.0) / 1e6, 2),
                  round(uni * min(1.0, max(0.0, (TAU - b * 10) / 10.0)), 2))
                 for b in range(0, 20)], part="agehist")
    write_table(__file__, ("pct", "z"), [(round(p, 3), z) for p, z in hypsometry()], part="hyps")
    cs = cells()
    write_table(__file__, ("h", "flooded_pct"),
                [(h, round(flooded_pct(h, cs), 2)) for h in range(0, 1001, 20)], part="flood")
    write_table(__file__, ("age", "value", "label"),
                [(a, v, "{%s}" % n) for a, v, n in EXTINCT], part="ext")
    write_table(__file__, ("age", "label"), [(a, "{%s}" % n) for a, n in LIPS], part="lip")
    write_table(__file__, ("age", "label"), [(a, "{%s}" % n) for a, n in OAES], part="oae")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

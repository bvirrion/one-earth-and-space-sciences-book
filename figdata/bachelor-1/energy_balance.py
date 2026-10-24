"""Zonal top-of-atmosphere radiation, the implied poleward heat transport and the
surface heat fluxes (Year 1, radiation-heat-transport).

Source (ledger data:b3-ncep): NCEP-NCAR Reanalysis 1, long-term monthly means
1991-2020, zonal and annual means derived by tools/fetch_data.py
(data/derived/bachelor-1-ncep-*.csv): solar down and up and longwave up at the
nominal top of the atmosphere; latent and sensible heat fluxes at the surface
(positive upwards) and the precipitation rate. Mean radius of the Earth 6371 km
(earth:Rmean); latent heat of vaporisation 2.47 MJ/kg near 15 C (nist:water-latent).

The reanalysis's radiation does not balance exactly over the globe; the global mean
of the net radiation is removed before the integration, so that the transport
vanishes at both poles:

    T(phi) = 2 pi a^2 * integral from -90 deg to phi of (R_net - <R_net>) cos(phi') dphi'.

Each Gaussian latitude stands for the band between the midpoints to its
neighbours (the poles close the outermost bands).

  part toa        lat asr olr net albedo       (zonal means, W/m2)
  part transport  lat T_PW                     (northward transport at the band edges)
  part surface    lat lh sh bowen precip_mm lp (zonal means; precipitation in mm/day, and
                                               as the latent heat it releases, L_V P, W/m2)
  part latent     lat T_PW                     (northward latent-heat transport by the
                                               atmosphere: integral of LH - L_V P, mean removed)
  part bands      lo hi down albedo asr olr net (10-degree band means, for the problem)
  part values     what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DERIVED = os.path.join(ROOT, "data", "derived")
A = 6371.0e3            # m, earth:Rmean
L_V = 2.4655e6          # J/kg at 288 K, nist:water-latent
DAY = 86400.0


def column(name):
    with open(os.path.join(DERIVED, "bachelor-1-ncep-%s.csv" % name), encoding="utf8") as f:
        rows = [(float(r["lat"]), float(r["value"])) for r in csv.DictReader(f)]
    rows.sort()                                   # south to north
    return rows


def lats():
    return [la for la, _ in column("dswrf-toa")]


def edges(lat_list):
    """Band edges (deg), south to north, midpoints between latitudes, poles at the ends."""
    e = [-90.0]
    e += [0.5 * (a + b) for a, b in zip(lat_list, lat_list[1:])]
    e.append(90.0)
    return e


def weights(lat_list):
    """Fraction of the sphere's area in each band: (sin upper - sin lower) / 2."""
    e = edges(lat_list)
    return [(math.sin(math.radians(b)) - math.sin(math.radians(a))) / 2 for a, b in zip(e, e[1:])]


def global_mean(values, lat_list):
    return sum(w * v for w, v in zip(weights(lat_list), values))


def toa():
    la = lats()
    down = [v for _, v in column("dswrf-toa")]
    up = [v for _, v in column("uswrf-toa")]
    olr = [v for _, v in column("ulwrf-toa")]
    asr = [d - u for d, u in zip(down, up)]
    net = [a - o for a, o in zip(asr, olr)]
    alb = [u / d if d > 0 else float("nan") for d, u in zip(down, up)]
    return la, down, up, asr, olr, net, alb


def transport(net, lat_list, remove_mean=True):
    """[(edge latitude, northward transport in PW)] from the South Pole to the North Pole."""
    m = global_mean(net, lat_list) if remove_mean else 0.0
    w = weights(lat_list)
    e = edges(lat_list)
    out, acc = [(e[0], 0.0)], 0.0
    for wi, v, top in zip(w, net, e[1:]):
        acc += (v - m) * wi * 4 * math.pi * A ** 2
        out.append((top, acc / 1e15))
    return out


def cumulative(values, lat_list):
    """[(edge latitude, integral of the field from the South Pole to that edge, in W)]."""
    out, acc = [(-90.0, 0.0)], 0.0
    for wi, v, top in zip(weights(lat_list), values, edges(lat_list)[1:]):
        acc += v * wi * 4 * math.pi * A ** 2
        out.append((top, acc))
    return out


def band_means(values, lat_list, step=10.0):
    """[(lo, hi, mean)] over bands of `step` degrees: the cumulative integral read at the
    band edges (linear between the Gaussian band edges) divided by the band's area."""
    c = cumulative(values, lat_list)
    out = []
    lo = -90.0
    while lo < 90.0 - 1e-9:
        hi = lo + step
        area = 2 * math.pi * A ** 2 * (math.sin(math.radians(hi)) - math.sin(math.radians(lo)))
        out.append((lo, hi, (interp(c, hi) - interp(c, lo)) / area))
        lo = hi
    return out


def bands(step=10.0):
    """10-degree band means: insolation, albedo (reflected / incoming), absorbed, OLR, net."""
    la, down, up, asr, olr, net, alb = toa()
    bd, bu, bo = band_means(down, la, step), band_means(up, la, step), band_means(olr, la, step)
    return [(lo, hi, d, u / d, d - u, o, d - u - o)
            for (lo, hi, d), (_, _, u), (_, _, o) in zip(bd, bu, bo)]


def latent_transport():
    """Northward transport of latent heat by the atmosphere (PW at the band edges): the
    water evaporated south of a latitude and not rained out there crosses it as vapour,
    so T_L = integral from the South Pole of (LH - L_V P) dA, global mean removed."""
    la, lh, sh, pr = surface()
    src = [e - L_V * p / DAY for e, p in zip(lh, pr)]
    return transport(src, la)


def interp(series, x):
    for (x1, y1), (x2, y2) in zip(series, series[1:]):
        if x1 <= x <= x2:
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    raise ValueError(x)


def peak(series, north=True):
    pts = [p for p in series if (p[0] > 0) == north]
    key = (lambda p: p[1]) if north else (lambda p: -p[1])
    return max(pts, key=key)


def surface():
    la = lats()
    lh = [v for _, v in column("lhtfl")]
    sh = [v for _, v in column("shtfl")]
    pr = [v * DAY for _, v in column("prate")]           # kg/m2/s -> mm/day
    return la, lh, sh, pr


def values():
    la, down, up, asr, olr, net, alb = toa()
    T = transport(net, la)
    pn, ps = peak(T, True), peak(T, False)
    v = [("global_down", global_mean(down, la)), ("global_up", global_mean(up, la)),
         ("global_asr", global_mean(asr, la)), ("global_olr", global_mean(olr, la)),
         ("global_net", global_mean(net, la)),
         ("global_albedo", global_mean(up, la) / global_mean(down, la)),
         ("peak_N_lat", pn[0]), ("peak_N_PW", pn[1]), ("peak_S_lat", ps[0]), ("peak_S_PW", ps[1]),
         ("T_40N", interp(T, 40.0)), ("T_35N", interp(T, 35.0)), ("T_43N", interp(T, 43.0)),
         ("T_40S", interp(T, -40.0)), ("T_equator", interp(T, 0.0)),
         ("T_north_end", T[-1][1])]
    # zonal values at chosen latitudes (nearest Gaussian latitude)
    for target in (0.0, 20.0, 40.0, 60.0, 80.0):
        j = min(range(len(la)), key=lambda i: abs(la[i] - target))
        v += [("lat_%g" % target, la[j]), ("asr_%g" % target, asr[j]), ("olr_%g" % target, olr[j]),
              ("net_%g" % target, net[j]), ("albedo_%g" % target, alb[j])]
    # where the net radiation (mean removed) changes sign in each hemisphere
    m = global_mean(net, la)
    for i in range(len(la) - 1):
        if (net[i] - m) * (net[i + 1] - m) < 0:
            x = la[i] + (la[i + 1] - la[i]) * (net[i] - m) / (net[i] - net[i + 1])
            v.append(("net_zero_lat", x))
    TL = latent_transport()
    v += [("TL_40N", interp(TL, 40.0)), ("TL_35N", interp(TL, 35.0)), ("TL_40S", interp(TL, -40.0)),
          ("TL_peakN_lat", peak(TL, True)[0]), ("TL_peakN_PW", peak(TL, True)[1])]
    sla, lh, sh, pr = surface()
    v += [("global_lh_minus_lp", global_mean([e - L_V * p / DAY for e, p in zip(lh, pr)], sla))]
    glh, gsh, gpr = global_mean(lh, sla), global_mean(sh, sla), global_mean(pr, sla)
    v += [("global_lh", glh), ("global_sh", gsh), ("global_bowen", gsh / glh),
          ("global_precip_mm_day", gpr), ("global_precip_m_yr", gpr * 365.25 / 1000),
          ("precip_energy_Wm2", gpr / DAY * L_V)]
    for target in (0.0, 25.0, 45.0, 70.0):
        j = min(range(len(sla)), key=lambda i: abs(sla[i] - target))
        v += [("lh_%g" % target, lh[j]), ("sh_%g" % target, sh[j]), ("bowen_%g" % target, sh[j] / lh[j]),
              ("pr_%g" % target, pr[j])]
    return v


if __name__ == "__main__":
    la, down, up, asr, olr, net, alb = toa()
    write_table(__file__, ("lat", "asr", "olr", "net", "albedo"),
                list(zip(la, asr, olr, net, alb)), part="toa")
    write_table(__file__, ("lat", "T_PW"), transport(net, la), part="transport")
    sla, lh, sh, pr = surface()
    write_table(__file__, ("lat", "lh", "sh", "bowen", "precip_mm", "lp"),
                [(a, b, c, c / b if abs(b) > 1 else float("nan"), d, L_V * d / DAY)
                 for a, b, c, d in zip(sla, lh, sh, pr)], part="surface")
    write_table(__file__, ("lat", "T_PW"), latent_transport(), part="latent")
    write_table(__file__, ("lo", "hi", "down", "albedo", "asr", "olr", "net"), bands(), part="bands")
    write_table(__file__, ("what", "value"), values(), part="values", digits=7)

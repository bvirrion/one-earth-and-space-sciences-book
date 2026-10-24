"""Orbital forcing (Year 2, orbital-forcing): the orbital elements of Berger and Loutre (1991), the
daily-mean insolation computed from them, its spectrum against that of the benthic stack, and a
first-order ice-volume model.

  The orbital elements come from data/derived/bachelor-2-orbit91.csv (data:b4-orbit91): age (kyr
  before 1950), eccentricity e, longitude of perihelion omega measured from the moving vernal
  equinox (heliocentric, as in the tables), obliquity eps, climatic precession e sin(omega), and
  the tabulated mid-month insolation at 65 N in July, computed by Berger and Loutre with a solar
  constant of 1360 W/m2. The daily-mean insolation at latitude phi when the Sun's true longitude
  is lambda is (S0/pi)(a/r)^2 (h0 sin phi sin delta + cos phi cos delta sin h0), with
  sin delta = sin eps sin lambda and r/a = (1 - e^2)/(1 - e cos(lambda - omega)); mid-July in the
  tables is lambda = 120 deg (the test checks the 1001 rows of the last Myr to 0.01 W/m2).

  elements  age_ka ecc obl prec                    last 1000 kyr
  jul65     age_ka tab calc resid jun65             last 1000 kyr (resid = calc - tab)
  lat       lat jun_0 jun_10 ann_lo ann_hi          June-solstice insolation today and 10 ka;
                                                    annual mean for eps 22.1 and 24.5 (e today)
  spectrum  period amp_ins amp_young amp_old        normalised amplitude spectra: 65 N July
                                                    insolation 0-700 ka; LR04 0-700 ka and
                                                    1250-1950 ka (data:lr04)
  lag       age_ka forcing model lr04               standardised forcing (minus insolation),
                                                    lag model with tau = 10 kyr, standardised
                                                    LR04, 0-800 ka
  numbers   key value
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")
S0 = 1360.0     # W/m2, solar constant of the 1991 tables (data:b4-orbit91)
TAU = 10.0      # kyr, response time of the lag model: a model choice, stated as such
JULY = 120.0    # deg, true longitude of the Sun at mid-July in the tables
JUNE = 90.0     # deg, June solstice


def orbit():
    with open(os.path.join(DERIVED, "bachelor-2-orbit91.csv"), encoding="utf8") as f:
        return [dict(age=int(r["age_ka"]), e=float(r["ecc"]), om=float(r["omega_deg"]),
                     eps=float(r["obl_deg"]), prec=float(r["prec"]), jul=float(r["i65NJul"]))
                for r in csv.DictReader(f)]


def distance_factor(lam, e, om):
    """(a/r)^2 when the Sun's true longitude is lam (deg)."""
    return ((1.0 - e * math.cos(math.radians(lam - om))) / (1.0 - e * e)) ** 2


def daily_insolation(phi, lam, e, om, eps, s0=S0):
    """Daily-mean insolation (W/m2) at latitude phi (deg) when the Sun's true longitude is lam."""
    p, l, ob = math.radians(phi), math.radians(lam), math.radians(eps)
    d = math.asin(math.sin(ob) * math.sin(l))
    x = -math.tan(p) * math.tan(d) if abs(phi) < 90 else (-1e9 if phi * d > 0 else 1e9)
    h0 = math.pi if x < -1 else (0.0 if x > 1 else math.acos(x))
    return s0 / math.pi * distance_factor(lam, e, om) * (
        h0 * math.sin(p) * math.sin(d) + math.cos(p) * math.cos(d) * math.sin(h0))


def annual_mean(phi, e, eps, s0=S0, n=1440):
    """Annual-mean insolation at latitude phi: the time average, with dt proportional to r^2
    dlambda (Kepler's second law), equals the lambda average of the insolation at the mean
    distance divided by sqrt(1 - e^2); it does not depend on omega."""
    tot = 0.0
    for k in range(n):
        lam = (k + 0.5) * 360.0 / n
        tot += daily_insolation(phi, lam, 0.0, 0.0, eps, s0)
    return tot / n / math.sqrt(1.0 - e * e)


def pole_annual(e, eps, s0=S0):
    return s0 * math.sin(math.radians(eps)) / (math.pi * math.sqrt(1.0 - e * e))


def read_lr04():
    with open(os.path.join(DERIVED, "lr04.csv"), encoding="utf8") as f:
        return [(float(r["age_ka"]), float(r["d18O_permil"])) for r in csv.DictReader(f)]


def regular(series, lo, hi):
    """Linear interpolation on a 1-kyr grid lo..hi."""
    x = np.array([a for a, _ in series])
    y = np.array([v for _, v in series])
    g = np.arange(lo, hi + 1, 1.0)
    return g, np.interp(g, x, y)


def amplitude(y, periods):
    """Amplitude spectrum of a 1-kyr series (linear trend removed, Hann taper), normalised to
    its maximum over the periods given."""
    t = np.arange(len(y), dtype=float)
    y = y - np.polyval(np.polyfit(t, y, 1), t)
    y = y * np.hanning(len(y))
    a = np.array([abs(np.sum(y * np.exp(-2j * np.pi * t / p))) for p in periods])
    return a / a.max()


def lag_model(forcing, tau=TAU, dt=1.0, v0=0.0):
    """Integrate dV/dt = (F - V)/tau forward in time with the exact step for constant F over dt.
    forcing is ordered from old to young."""
    k = math.exp(-dt / tau)
    v, out = v0, []
    for f in forcing:
        v = f + (v - f) * k
        out.append(v)
    return out


def standardise(y):
    y = np.asarray(y, dtype=float)
    return (y - y.mean()) / y.std()


def numbers():
    orb = orbit()
    by = {r["age"]: r for r in orb}
    n = {}
    for age in (0, 6, 10, 116, 125, 127):
        r = by[age]
        n["e_%d" % age] = r["e"]
        n["om_%d" % age] = r["om"]
        n["eps_%d" % age] = r["eps"]
        n["prec_%d" % age] = r["prec"]
        n["jul65_tab_%d" % age] = r["jul"]
        n["jun65_%d" % age] = daily_insolation(65, JUNE, r["e"], r["om"], r["eps"])
        n["fac_jun_%d" % age] = distance_factor(JUNE, r["e"], r["om"])
    last = [r for r in orb if r["age"] <= 1000]
    n["e_min_1myr"] = min(r["e"] for r in last)
    n["e_max_1myr"] = max(r["e"] for r in last)
    n["eps_min_1myr"] = min(r["eps"] for r in last)
    n["eps_max_1myr"] = max(r["eps"] for r in last)
    n["jul65_min_800"] = min(r["jul"] for r in last if r["age"] <= 800)
    n["jul65_max_800"] = max(r["jul"] for r in last if r["age"] <= 800)
    n["resid_max_1myr"] = max(abs(daily_insolation(65, JULY, r["e"], r["om"], r["eps"]) - r["jul"])
                              for r in last)
    e0 = by[0]["e"]
    n["peri_aph_ratio_0"] = ((1 + e0) / (1 - e0)) ** 2
    n["global_ann_emax"] = S0 / (4 * math.sqrt(1 - n["e_max_1myr"] ** 2))
    n["global_ann_emin"] = S0 / (4 * math.sqrt(1 - n["e_min_1myr"] ** 2))
    n["pole_ann_221"] = pole_annual(e0, 22.1)
    n["pole_ann_245"] = pole_annual(e0, 24.5)
    n["eq_ann_221"] = annual_mean(0, e0, 22.1)
    n["eq_ann_245"] = annual_mean(0, e0, 24.5)
    n["jun65_today_e0"] = daily_insolation(65, JUNE, 0.0, 0.0, by[0]["eps"])
    per = np.arange(10.0, 150.5, 0.5)
    for key, amp in zip(("ins", "young", "old"), spectra(per)):
        top = sorted(range(len(per)), key=lambda i: -amp[i])
        n["peak_%s" % key] = float(per[top[0]])
    f, m, lr = lag_series()
    n["lag_r_model_lr04"] = float(np.corrcoef(m, lr)[0, 1])
    n["lag_r_forcing_lr04"] = float(np.corrcoef(f, lr)[0, 1])
    return n


def spectra(per):
    orb = orbit()
    ins = [(r["age"], r["jul"]) for r in orb]
    lr = read_lr04()
    _, yi = regular(ins, 0, 700)
    _, yy = regular(lr, 0, 700)
    _, yo = regular(lr, 1250, 1950)
    return amplitude(yi, per), amplitude(yy, per), amplitude(yo, per)


def lag_series():
    """Forcing = minus standardised 65 N July insolation (less sunshine, more ice), integrated
    from 1000 ka to 0; the model and LR04 compared over 0-800 ka (all standardised)."""
    orb = [r for r in orbit() if r["age"] <= 1000]
    orb.sort(key=lambda r: -r["age"])                     # old to young
    f = -standardise([r["jul"] for r in orb])
    v = lag_model(list(f))
    ages = [r["age"] for r in orb]
    keep = [i for i, a in enumerate(ages) if a <= 800]
    keep.reverse()                                        # young to old, ages 0..800
    g, ylr = regular(read_lr04(), 0, 800)
    m = standardise([v[i] for i in keep])
    ff = standardise([f[i] for i in keep])
    return ff, m, standardise(ylr)


if __name__ == "__main__":
    orb = orbit()
    last = [r for r in orb if r["age"] <= 1000]
    write_table(__file__, ("age_ka", "ecc", "obl", "prec"),
                [(r["age"], r["e"], r["eps"], r["prec"]) for r in last], part="elements")
    write_table(__file__, ("age_ka", "tab", "calc", "resid", "jun65"),
                [(r["age"], r["jul"],
                  round(daily_insolation(65, JULY, r["e"], r["om"], r["eps"]), 2),
                  round(daily_insolation(65, JULY, r["e"], r["om"], r["eps"]) - r["jul"], 3),
                  round(daily_insolation(65, JUNE, r["e"], r["om"], r["eps"]), 2))
                 for r in last], part="jul65")
    by = {r["age"]: r for r in orb}
    r0, r10 = by[0], by[10]
    e0 = r0["e"]
    rows = []
    for k in range(-36, 37):
        lat = 2.5 * k
        rows.append((lat, round(daily_insolation(lat, JUNE, r0["e"], r0["om"], r0["eps"]), 2),
                     round(daily_insolation(lat, JUNE, r10["e"], r10["om"], r10["eps"]), 2),
                     round(annual_mean(lat, e0, 22.1), 2), round(annual_mean(lat, e0, 24.5), 2)))
    write_table(__file__, ("lat", "jun_0", "jun_10", "ann_lo", "ann_hi"), rows, part="lat")
    per = np.arange(10.0, 150.5, 0.5)
    ai, ay, ao = spectra(per)
    write_table(__file__, ("period", "amp_ins", "amp_young", "amp_old"),
                [(float(p), round(float(a), 4), round(float(b), 4), round(float(c), 4))
                 for p, a, b, c in zip(per, ai, ay, ao)], part="spectrum")
    f, m, lr = lag_series()
    write_table(__file__, ("age_ka", "forcing", "model", "lr04"),
                [(a, round(float(x), 4), round(float(y), 4), round(float(z), 4))
                 for a, x, y, z in zip(range(0, 801), f, m, lr)], part="lag")
    write_table(__file__, ("key", "value"),
                [(k, round(v, 4)) for k, v in sorted(numbers().items())], part="numbers")

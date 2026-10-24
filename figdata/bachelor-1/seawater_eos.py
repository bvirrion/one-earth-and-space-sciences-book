"""Seawater density, potential temperature and T-S diagrams (Year 1,
fluid-envelopes-structure).

Sources (ledger):
- the one-atmosphere equation of state EOS-80 with the coefficients printed in
  UNESCO Technical Paper 44 (unesco:eos80; check value rho(35, 0, 0) = 1028.1063);
- the adiabatic lapse rate ATG of Bryden (1973) and the fourth-order Runge-Kutta
  potential temperature THETA of Fofonoff (1977), as printed in UNESCO 44 with their
  check values (unesco44:atg-theta); depth from pressure with Saunders and
  Fofonoff's formula DEPTH (unesco:eos80-checks, z = 9712.653 m at 10 000 dbar, 30 deg);
- WOA23 annual temperature and salinity, one 1-degree column per site: two South
  Atlantic columns at 25.5 W (10.5 S and 30.5 S; data:b3-woa23) and Book 2's Canada
  Basin column at 75.5 N 150.5 W (data:b2-woa23);
- the 1.00024 scaling from ITS-90 to IPTS-68 temperatures (teos10:its90), applied
  before the UNESCO formulas, which take IPTS-68.

Densities are potential densities referred to the surface: sigma_theta =
rho(S, theta, 0) - 1000, the quantity oceanographers compare on a T-S diagram.

  part prof-<site>   depth p theta s sigma      (site: sa10, sa30, arctic; 0-5500 m)
  part ts-<site>     s theta                    (0-5500 m for the T-S diagram)
  part iso-<sigma>   s theta                    (isopycnal sigma_theta = 24 ... 28)
  part isolab        s theta lab                (upper end of each isopycnal)
  part masses        s theta name               (the water-mass cores read on sa30)
  part cabbeling     s theta                    (two waters of equal density, the
                                                 mixing line and the mixture)
  part values        what value
"""
import csv
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DERIVED = os.path.join(ROOT, "data", "derived")
SITES = {"sa10": ("bachelor-1-woa23-sa10", -10.5), "sa30": ("bachelor-1-woa23-sa30", -30.5),
         "arctic": ("grade-10-woa23-arctic", 75.5)}
T68 = 1.00024                       # teos10:its90
SIGMAS = (24.0, 25.0, 26.0, 26.5, 27.0, 27.5, 28.0)
CAB_SIGMA, CAB_T = 27.0, (2.0, 14.0)   # the two parent waters of the cabbeling example


# ---------------------------------------------------------------- equation of state
def rho0(s, t):
    """Density (kg/m3) at practical salinity s, temperature t (deg C, IPTS-68), one
    atmosphere: EOS-80 one-atmosphere polynomial (UNESCO 44)."""
    rw = ((((6.536332e-9 * t - 1.120083e-6) * t + 1.001685e-4) * t - 9.095290e-3) * t
          + 6.793952e-2) * t + 999.842594
    a = (((5.3875e-9 * t - 8.2467e-7) * t + 7.6438e-5) * t - 4.0899e-3) * t + 8.24493e-1
    b = (-1.6546e-6 * t + 1.0227e-4) * t - 5.72466e-3
    c = 4.8314e-4
    return rw + (a + b * math.sqrt(s) + c * s) * s


def sigma(s, t):
    return rho0(s, t) - 1000.0


def alpha(s, t, h=1e-3):
    """Thermal expansion coefficient -(1/rho) d rho / dT (1/K), centred difference."""
    return -(rho0(s, t + h) - rho0(s, t - h)) / (2 * h) / rho0(s, t)


def beta(s, t, h=1e-3):
    """Haline contraction coefficient (1/rho) d rho / dS (per unit of salinity)."""
    return (rho0(s + h, t) - rho0(s - h, t)) / (2 * h) / rho0(s, t)


def rho_linear(s, t, s0, t0):
    """Linearised equation of state about (s0, t0)."""
    r = rho0(s0, t0)
    return r * (1 - alpha(s0, t0) * (t - t0) + beta(s0, t0) * (s - s0))


# ------------------------------------------------------- adiabat and depth (UNESCO 44)
def atg(s, t, p):
    """Adiabatic temperature gradient (deg C per decibar), Bryden (1973)."""
    ds = s - 35.0
    return ((((-2.1687e-16 * t + 1.8676e-14) * t - 4.6206e-13) * p
             + ((2.7759e-12 * t - 1.1351e-10) * ds + ((-5.4481e-14 * t + 8.733e-12) * t
                                                       - 6.7795e-10) * t + 1.8741e-8)) * p
            + (-4.2393e-8 * t + 1.8932e-6) * ds
            + ((6.6228e-10 * t - 6.836e-8) * t + 8.5258e-6) * t + 3.5803e-5)


def theta(s, t0, p0, pr=0.0):
    """Potential temperature at reference pressure pr: UNESCO 44 THETA (Runge-Kutta)."""
    p, t = p0, t0
    h = pr - p
    xk = h * atg(s, t, p)
    t = t + 0.5 * xk
    q = xk
    p = p + 0.5 * h
    xk = h * atg(s, t, p)
    t = t + 0.29289322 * (xk - q)
    q = 0.58578644 * xk + 0.121320344 * q
    xk = h * atg(s, t, p)
    t = t + 1.707106781 * (xk - q)
    q = 3.414213562 * xk - 4.121320344 * q
    p = p + 0.5 * h
    xk = h * atg(s, t, p)
    return t + (xk - 2.0 * q) / 6.0


def depth(p, lat):
    """Depth (m) from pressure (dbar): UNESCO 44 DEPTH (Saunders and Fofonoff)."""
    x = math.sin(lat / 57.29578) ** 2
    gr = 9.780318 * (1.0 + (5.2788e-3 + 2.36e-5 * x) * x) + 1.092e-6 * p
    return ((((-1.82e-15 * p + 2.279e-10) * p - 2.2512e-5) * p + 9.72659) * p) / gr


def pressure(z, lat):
    """Pressure (dbar) at depth z (m): DEPTH inverted by Newton's method."""
    p = z
    for _ in range(30):
        f = depth(p, lat) - z
        d = (depth(p + 0.5, lat) - depth(p - 0.5, lat))
        p -= f / d
        if abs(f) < 1e-9:
            break
    return p


# ------------------------------------------------------------------ T-S diagram
S_RANGE = (33.5, 37.0)                 # salinity window of the T-S diagram


def salinity_on(sig, th, lo=0.0, hi=45.0):
    """Salinity at which sigma(S, theta) = sig (bisection; sigma increases with S)."""
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if sigma(mid, th) < sig:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def isopycnal(sig, th_lo=-2.0, th_hi=30.0, n=321):
    """Points of the isopycnal inside the salinity window of the diagram."""
    pts = [(salinity_on(sig, th_lo + (th_hi - th_lo) * i / (n - 1)),
            th_lo + (th_hi - th_lo) * i / (n - 1)) for i in range(n)]
    return [(s, th) for s, th in pts if S_RANGE[0] <= s <= S_RANGE[1]]


def mix(a, b, f):
    """Mixture of f of water a and 1 - f of water b (salinity and potential temperature
    mix linearly by mass)."""
    return (f * a[0] + (1 - f) * b[0], f * a[1] + (1 - f) * b[1])


def cabbeling():
    """Two waters on sigma_theta = 27.0 at 2 and 14 deg C, and their 50:50 mixture."""
    a = (salinity_on(CAB_SIGMA, CAB_T[0]), CAB_T[0])
    b = (salinity_on(CAB_SIGMA, CAB_T[1]), CAB_T[1])
    m = mix(a, b, 0.5)
    return a, b, m, sigma(m[0], m[1])


# ------------------------------------------------------------------ profiles
def _column(stem, var):
    with open(os.path.join(DERIVED, "%s-%s.csv" % (stem, var)), encoding="utf8") as f:
        return {float(r["depth_m"]): float(r["value"]) for r in csv.DictReader(f)}


def profile(site):
    """[(depth m, pressure dbar, theta, S, sigma_theta)] for a WOA23 column."""
    stem, lat = SITES[site]
    t, s = _column(stem, "t"), _column(stem, "s")
    out = []
    for z in sorted(t):
        if z not in s:
            continue
        p = pressure(z, lat)
        th = theta(s[z], T68 * t[z], p)
        out.append((z, p, th, s[z], sigma(s[z], th)))
    return out


def extreme(prof, zlo, zhi, which):
    rows = [r for r in prof if zlo <= r[0] <= zhi]
    key = (lambda r: r[3])
    return (min if which == "min" else max)(rows, key=key)


def masses():
    """Water-mass cores read on the 30.5 S column: Central Water (200 m level), the
    salinity minimum (Antarctic Intermediate Water), the deep salinity maximum (North
    Atlantic Deep Water), the bottom level (Antarctic Bottom Water)."""
    p = profile("sa30")
    central = [r for r in p if r[0] == 200.0][0]
    aaiw = extreme(p, 500, 1500, "min")
    nadw = extreme(p, 1500, 3500, "max")
    aabw = p[-1]
    return [("Central", central), ("AAIW", aaiw), ("NADW", nadw), ("AABW", aabw)]


def values():
    v = [("rho_35_0", rho0(35, 0)), ("theta_check", theta(40, 40, 10000, 0)),
         ("atg_check", atg(40, 40, 10000)), ("depth_check", depth(10000, 30)),
         ("rho_35_10", rho0(35, 10)), ("rho_35_25", rho0(35, 25)), ("rho_0_4", rho0(0, 4)),
         ("alpha_35_10", alpha(35, 10)), ("beta_35_10", beta(35, 10)),
         ("alpha_35_0", alpha(35, 0)), ("alpha_35_25", alpha(35, 25)),
         ("beta_35_0", beta(35, 0)), ("beta_35_25", beta(35, 25)),
         ("theta_35_2_4000", theta(35, 2, 4000)), ("theta_35_2_10000", theta(35, 2, 10000))]
    for name, r in masses():
        v += [("%s_depth" % name, r[0]), ("%s_theta" % name, r[2]), ("%s_S" % name, r[3]),
              ("%s_sigma" % name, r[4])]
    a, b, m, sm = cabbeling()
    v += [("cab_Sa", a[0]), ("cab_Sb", b[0]), ("cab_Sm", m[0]), ("cab_thm", m[1]),
          ("cab_sigma_mix", sm)]
    for site in SITES:
        p = profile(site)
        v += [("%s_bottom_depth" % site, p[-1][0]), ("%s_theta0" % site, p[0][2]),
              ("%s_S0" % site, p[0][3]), ("%s_sigma0" % site, p[0][4])]
    return v


if __name__ == "__main__":
    for site in SITES:
        prof = profile(site)
        write_table(__file__, ("depth", "p", "theta", "s", "sigma"), prof, part="prof-" + site)
        write_table(__file__, ("s", "theta"), [(r[3], r[2]) for r in prof], part="ts-" + site)
    for sg in SIGMAS:
        write_table(__file__, ("s", "theta"), isopycnal(sg), part="iso-%g" % sg)
    # each isopycnal is labelled at its upper end, on the right edge of the diagram
    write_table(__file__, ("s", "theta", "lab"),
                [isopycnal(sg)[-1] + ("%g" % sg,) for sg in SIGMAS], part="isolab")
    write_table(__file__, ("s", "theta", "name"), [(r[3], r[2], n) for n, r in masses()],
                part="masses")
    a, b, m, _ = cabbeling()
    write_table(__file__, ("s", "theta"), [a, m, b], part="cabbeling")
    write_table(__file__, ("what", "value"), values(), part="values", digits=8)

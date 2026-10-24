"""Equilibrium tide and Kelvin-wave amphidromes (Year 3, ocean dynamics).

Equilibrium tide of the Moon. The degree-2 tidal potential of a body of mass
M at distance d is -(G M a^2/d^3) P2(cos theta), theta the angle from the
sub-lunar point; a fluid surface in equilibrium with it stands at

    eta = K P2(cos theta),  K = (M/M_E) (a/d)^3 a,  P2(c) = (3c^2 - 1)/2,

and at latitude lat, lunar declination dec and lunar hour angle H,
cos theta = sin lat sin dec + cos lat cos dec cos H. Masses and the mean
distance from the NASA Moon fact sheet (ledger moon5:orbit), a the mean
radius (earth:Rmean). The lunar day is twice the period of M2, 12.4206 h
(stewart:tide-constituents).

Amphidromes in a channel. Two Kelvin waves of equal amplitude travel in
opposite directions along a channel 0 <= y <= W of depth H at latitude LAT
(an exercise shelf sea): one eastward, trapped against the southern wall,
one westward, against the northern wall. Their complex amplitude is

    Z(x, y) = exp(-y/L_R) exp(i k x) + exp(-(W - y)/L_R) exp(-i k x),

with c = sqrt(g H), L_R = c/f, k = 2 pi/(c T_M2), and the surface is
eta = Re(Z exp(-i omega t)). High water comes at omega t = arg Z: lines of
constant arg Z are cotidal lines, lines of constant |Z| co-range lines. The
amphidromic points sit on the centre line at k x = pi/2 + n pi.

  part bulge   x y            the equilibrium surface r = 1 + EXAG P2(cos theta)
                              in the plane of the Moon, Moon along +x
  part series  t eta0 eta20   equilibrium tide (m) at 45 N over two lunar days,
                              declination 0 and 20 deg (H = 0 at t = 0)
  part cot-<deg> x y          cotidal line arg Z = deg (km), segments separated by nan
  part cor     lev x y        co-range lines |Z| = lev (km)
  part amph    x y            amphidromic points (km)
  part values  what value
"""
import cmath
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
from region import trace  # noqa: E402  (marching squares, read-only use)

M_MOON = 0.07346e24
M_EARTH = 5.9724e24
D_MOON = 0.3844e9
A_EARTH = 6371.0e3
T_M2_H = 12.4206
OMEGA = 7.292115e-5
G = 9.81
EXAG = 0.12
# exercise shelf sea
LAT = 55.0
DEPTH = 50.0
WIDTH_KM = 400.0
LENGTH_KM = 1600.0
PHASES = range(0, 360, 30)
CORANGE = (0.2, 0.4, 0.6, 0.8, 1.0)


def tide_scale(m=M_MOON, d=D_MOON, a=A_EARTH):
    """K = (M/M_E)(a/d)^3 a, metres."""
    return (m / M_EARTH) * (a / d) ** 3 * a


def p2(c):
    return 1.5 * c * c - 0.5


def eq_tide(lat, dec, hour_angle):
    """Equilibrium tide (m) of the Moon; angles in degrees."""
    la, de, h = (math.radians(v) for v in (lat, dec, hour_angle))
    c = math.sin(la) * math.sin(de) + math.cos(la) * math.cos(de) * math.cos(h)
    return tide_scale() * p2(c)


def lunar_day_h():
    return 2 * T_M2_H


def coriolis(lat):
    return 2 * OMEGA * math.sin(math.radians(lat))


def kelvin_speed(depth=DEPTH):
    return math.sqrt(G * depth)


def rossby_radius(depth=DEPTH, lat=LAT):
    return kelvin_speed(depth) / coriolis(lat)


def wavenumber(depth=DEPTH):
    return 2 * math.pi / (kelvin_speed(depth) * T_M2_H * 3600.0)


def channel_z(x, y, depth=DEPTH, lat=LAT, width=WIDTH_KM * 1e3):
    """Complex tide amplitude of the two-Kelvin-wave channel; x, y in metres."""
    lr, k = rossby_radius(depth, lat), wavenumber(depth)
    return np.exp(-y / lr) * np.exp(1j * k * x) + np.exp(-(width - y) / lr) * np.exp(-1j * k * x)


def amphidromes(length=LENGTH_KM * 1e3, depth=DEPTH, width=WIDTH_KM * 1e3):
    k = wavenumber(depth)
    out, n = [], 0
    while True:
        x = (math.pi / 2 + n * math.pi) / k
        if x > length:
            return out
        out.append((x, width / 2))
        n += 1


def kelvin_check(depth=DEPTH, lat=LAT):
    """Residuals of the three shallow-water equations for an eastward Kelvin
    wave eta = exp(-y/L_R) cos(k x - omega t), u = (g/c) eta, v = 0, at a
    sample point (finite differences)."""
    c, lr, k = kelvin_speed(depth), rossby_radius(depth, lat), wavenumber(depth)
    w = k * c
    f = coriolis(lat)

    def eta(x, y, t):
        return math.exp(-y / lr) * math.cos(k * x - w * t)

    def u(x, y, t):
        return G / c * eta(x, y, t)

    x0, y0, t0 = 1.0e5, 5.0e4, 3000.0
    hx, ht = 10.0, 0.1
    du_dt = (u(x0, y0, t0 + ht) - u(x0, y0, t0 - ht)) / (2 * ht)
    deta_dx = (eta(x0 + hx, y0, t0) - eta(x0 - hx, y0, t0)) / (2 * hx)
    deta_dy = (eta(x0, y0 + hx, t0) - eta(x0, y0 - hx, t0)) / (2 * hx)
    deta_dt = (eta(x0, y0, t0 + ht) - eta(x0, y0, t0 - ht)) / (2 * ht)
    du_dx = (u(x0 + hx, y0, t0) - u(x0 - hx, y0, t0)) / (2 * hx)
    scale = G * abs(deta_dx) + 1e-30
    return ((du_dt + G * deta_dx) / scale,
            (f * u(x0, y0, t0) + G * deta_dy) / scale,
            (deta_dt + depth * du_dx) / (abs(deta_dt) + 1e-30))


def phase_lines(xs, ys, zgrid, deg):
    """Cotidal line arg Z = deg: zero line of Im(Z e^{-i deg}) where the real
    part is positive (the other half is the line deg + 180)."""
    rot = zgrid * cmath.exp(-1j * math.radians(deg))
    rows = []
    for line in trace(rot.imag, xs, ys, 0.0):
        seg = []
        for x, y in line:
            i = min(int(round((x - xs[0]) / (xs[1] - xs[0]))), len(xs) - 1)
            j = min(int(round((y - ys[0]) / (ys[1] - ys[0]))), len(ys) - 1)
            if rot.real[j, i] > 0:
                seg.append((x, y))
            else:
                if len(seg) > 2:
                    rows += seg + [("nan", "nan")]
                seg = []
        if len(seg) > 2:
            rows += seg + [("nan", "nan")]
    return rows[:-1]


def main():
    rows = []
    for i in range(0, 361):
        th = math.radians(i)
        r = 1 + EXAG * p2(math.cos(th))
        rows.append([r * math.cos(th), r * math.sin(th)])
    write_table(__file__, ("x", "y"), rows, part="bulge")
    ser = []
    for i in range(0, 497):
        t = i * 0.1
        h = 360.0 * t / lunar_day_h()
        ser.append([t, eq_tide(45.0, 0.0, h), eq_tide(45.0, 20.0, h)])
    write_table(__file__, ("t", "eta0", "eta20"), ser, part="series")
    xs = np.linspace(0.0, LENGTH_KM, 321)
    ys = np.linspace(0.0, WIDTH_KM, 81)
    X, Y = np.meshgrid(xs * 1e3, ys * 1e3)
    zg = channel_z(X, Y)
    for deg in PHASES:
        write_table(__file__, ("x", "y"), phase_lines(xs, ys, zg, deg), part="cot-%d" % deg)
    cor = []
    for lev in CORANGE:
        for line in trace(np.abs(zg), xs, ys, lev):
            if len(line) < 3:
                continue
            cor += [(lev, x, y) for x, y in line] + [("nan", "nan", "nan")]
    write_table(__file__, ("lev", "x", "y"), cor[:-1], part="cor")
    write_table(__file__, ("x", "y"), [(x / 1e3, y / 1e3) for x, y in amphidromes()], part="amph")
    k_m = tide_scale()
    vals = [["K_moon_m", k_m], ["range_eq_m", 1.5 * k_m], ["semidiurnal_eq_m", 0.75 * k_m],
            ["mass_ratio", M_MOON / M_EARTH], ["lunar_day_h", lunar_day_h()],
            ["c_shelf", kelvin_speed()], ["LR_shelf_km", rossby_radius() / 1e3],
            ["lambda_shelf_km", 2 * math.pi / wavenumber() / 1e3],
            ["amph_spacing_km", math.pi / wavenumber() / 1e3],
            ["max_eta20_m", max(r[2] for r in ser)], ["max_eta0_m", max(r[1] for r in ser)]]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

"""Radial-velocity curves, transit light curves and microlensing magnification (Year 3,
exoplanets).

1. Radial velocity of a star with one planet on a Keplerian orbit,

       v_r(t) = K [cos(nu + omega) + e cos omega],
       K = (2 pi G / P)^(1/3) m_p sin i / (M_* + m_p)^(2/3) / sqrt(1 - e^2),

   nu the true anomaly from Kepler's equation M = E - e sin E (Newton iteration),
   omega the argument of periastron of the star's orbit (const:G).
2. Transit light curve of a dark disc of radius p (in stellar radii) crossing a star with
   the quadratic limb-darkening law I(mu)/I(1) = 1 - u1 (1 - mu) - u2 (1 - mu)^2,
   mu = sqrt(1 - r^2): the blocked flux is the integral over the stellar radius r of
   I(r) times the arc of the circle of radius r inside the planet's disc (numerical,
   Simpson on a grid fine near the disc's edges); a uniform star (u1 = u2 = 0) has the
   closed-form overlap area of two discs. Circular orbit: z(t) = (a/R_*)
   sqrt(sin^2(2 pi t/P) + cos^2 i cos^2(2 pi t/P)).
3. Point-lens microlensing (admitted from general relativity): magnification
   A(u) = (u^2 + 2) / (u sqrt(u^2 + 4)), u(t) = sqrt(u0^2 + (t/t_E)^2) in Einstein radii;
   Einstein radius theta_E = sqrt((4 G M / c^2) (D_S - D_L) / (D_L D_S)) (const:G,
   const:c, iau:parsec).

The planets of the figures are invented: P = 10 d, K = 30 m/s (circular, and e = 0.3,
omega = 60 deg); a transit with p = 0.1, a/R_* = 15, b = 0.3, u1 = 0.40, u2 = 0.25.

  part rv       phase v_circ v_ecc                  m/s, two orbits
  part transit  t_h flux_ld flux_uni                hours from mid-transit
  part lens     t_tE A01 A03 A10                    u0 = 0.1, 0.3, 1.0
  part values   what value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

G = 6.67430e-11
C = 299792458.0
M_SUN = 1.9884e30
M_EARTH = 5.97e24
M_JUP = 1898e24
R_SUN = 695700e3
R_EARTH = 6378e3
R_JUP = 71492e3
AU = 149597870700.0
PC = 3.085677581e16
DAY = 86400.0

# invented planets of the figures
RV_P, RV_K, RV_E, RV_OMEGA = 10.0, 30.0, 0.3, math.radians(60.0)
TR_P, TR_A, TR_B, TR_U1, TR_U2 = 0.1, 15.0, 0.3, 0.40, 0.25
TR_PERIOD = 10.0  # days


def semi_amplitude(m_p, m_star, period, e=0.0, sini=1.0):
    """K (m/s) for masses in kg and a period in s."""
    return ((2 * math.pi * G / period) ** (1 / 3) * m_p * sini
            / (m_star + m_p) ** (2 / 3) / math.sqrt(1 - e * e))


def minimum_mass(k, m_star, period, e=0.0):
    """m_p sin i (kg) from K, neglecting m_p against M_* (one fixed-point step corrects it)."""
    m = k * math.sqrt(1 - e * e) * m_star ** (2 / 3) / (2 * math.pi * G / period) ** (1 / 3)
    for _ in range(3):
        m = (k * math.sqrt(1 - e * e) * (m_star + m) ** (2 / 3)
             / (2 * math.pi * G / period) ** (1 / 3))
    return m


def semi_major_axis(m_star, period, m_p=0.0):
    return (G * (m_star + m_p) * period ** 2 / (4 * math.pi ** 2)) ** (1 / 3)


def ecc_anomaly(mean, e):
    big_e = mean if e < 0.8 else math.pi
    for _ in range(50):
        d = (big_e - e * math.sin(big_e) - mean) / (1 - e * math.cos(big_e))
        big_e -= d
        if abs(d) < 1e-13:
            break
    return big_e


def true_anomaly(mean, e):
    big_e = ecc_anomaly(mean, e)
    return 2 * math.atan2(math.sqrt(1 + e) * math.sin(big_e / 2),
                          math.sqrt(1 - e) * math.cos(big_e / 2))


def radial_velocity(phase, k, e=0.0, omega=0.0):
    """v_r at orbital phase (time since periastron / P)."""
    nu = true_anomaly(2 * math.pi * (phase % 1.0), e)
    return k * (math.cos(nu + omega) + e * math.cos(omega))


def overlap_area(z, p):
    """Area of a disc of radius p centred at distance z from a unit disc's centre, inside it."""
    if z >= 1 + p:
        return 0.0
    if z <= 1 - p:
        return math.pi * p * p
    if z <= p - 1:
        return math.pi
    k0 = math.acos((p * p + z * z - 1) / (2 * p * z))
    k1 = math.acos((1 - p * p + z * z) / (2 * z))
    return (p * p * k0 + k1
            - 0.5 * math.sqrt(max(0.0, 4 * z * z - (1 + z * z - p * p) ** 2)))


def intensity(r, u1, u2):
    mu = math.sqrt(max(0.0, 1 - r * r))
    return 1 - u1 * (1 - mu) - u2 * (1 - mu) ** 2


def total_flux(u1, u2):
    """Integral of I over the unit disc: pi (1 - u1/3 - u2/6)."""
    return math.pi * (1 - u1 / 3 - u2 / 6)


def _arc(r, z, p):
    """Angle (rad) of the circle of radius r that lies inside the planet's disc."""
    if r <= 0:
        return 2 * math.pi if z < p else 0.0
    if r + z <= p:
        return 2 * math.pi
    if r >= z + p or r <= z - p:
        return 0.0
    c = (r * r + z * z - p * p) / (2 * r * z)
    return 2 * math.acos(max(-1.0, min(1.0, c)))


def blocked_flux(z, p, u1, u2, n=400):
    """Integral over r of I(r) r arc(r): Simpson on [max(0, z-p), min(1, z+p)]."""
    lo, hi = max(0.0, z - p), min(1.0, z + p)
    if hi <= lo:
        return 0.0
    # the substitution r = lo + (hi-lo) (1 - cos t)/2 crowds nodes near both ends
    m = 2 * n
    s = 0.0
    for j in range(m + 1):
        t = math.pi * j / m
        r = lo + (hi - lo) * (1 - math.cos(t)) / 2
        w = 1 if j in (0, m) else (4 if j % 2 else 2)
        s += w * intensity(r, u1, u2) * r * _arc(r, z, p) * (hi - lo) * math.sin(t) / 2
    return s * (math.pi / m) / 3


def transit_flux(z, p, u1=0.0, u2=0.0):
    """Relative flux of the star while the planet's centre is at z stellar radii."""
    if u1 == 0.0 and u2 == 0.0:
        return 1.0 - overlap_area(z, p) / math.pi
    return 1.0 - blocked_flux(z, p, u1, u2) / total_flux(u1, u2)


def separation(t, period, a_rs, inc):
    ph = 2 * math.pi * t / period
    return a_rs * math.sqrt(math.sin(ph) ** 2 + (math.cos(inc) * math.cos(ph)) ** 2)


def durations(period, a_rs, b, p):
    """Total (T14) and full (T23) transit durations, same unit as the period."""
    inc = math.acos(b / a_rs)
    t14 = period / math.pi * math.asin(math.sqrt((1 + p) ** 2 - b * b) / (a_rs * math.sin(inc)))
    t23 = period / math.pi * math.asin(math.sqrt(max(0.0, (1 - p) ** 2 - b * b))
                                       / (a_rs * math.sin(inc)))
    return t14, t23


def magnification(u):
    return (u * u + 2) / (u * math.sqrt(u * u + 4))


def einstein_angle(m_lens, d_l, d_s):
    return math.sqrt(4 * G * m_lens / C ** 2 * (d_s - d_l) / (d_l * d_s))


def main():
    rows = []
    for i in range(0, 401):
        ph = 2.0 * i / 400
        rows.append((ph, radial_velocity(ph, RV_K), radial_velocity(ph, RV_K, RV_E, RV_OMEGA)))
    write_table(__file__, ("phase", "v_circ", "v_ecc"), rows, part="rv")

    inc = math.acos(TR_B / TR_A)
    rows = []
    for i in range(0, 241):
        t_h = -4.0 + 8.0 * i / 240
        z = separation(t_h / 24.0, TR_PERIOD, TR_A, inc)
        rows.append((t_h, transit_flux(z, TR_P, TR_U1, TR_U2), transit_flux(z, TR_P)))
    write_table(__file__, ("t_h", "flux_ld", "flux_uni"), rows, part="transit")

    rows = []
    for i in range(0, 241):
        x = -3.0 + 6.0 * i / 240
        rows.append((x, *[magnification(math.hypot(u0, x)) for u0 in (0.1, 0.3, 1.0)]))
    write_table(__file__, ("t_tE", "A01", "A03", "A10"), rows, part="lens")

    t14, t23 = durations(TR_PERIOD, TR_A, TR_B, TR_P)
    th_e = einstein_angle(0.5 * M_SUN, 4000 * PC, 8000 * PC)
    vals = [
        ["K_jupiter_sun", semi_amplitude(M_JUP, M_SUN, 4331 * DAY, 0.049)],
        ["K_earth_sun", semi_amplitude(M_EARTH, M_SUN, 365.2 * DAY, 0.017)],
        ["depth_jupiter_sun", (R_JUP / R_SUN) ** 2],
        ["depth_earth_sun", (R_EARTH / R_SUN) ** 2],
        ["t14_h", t14 * 24], ["t23_h", t23 * 24],
        ["depth_ld_mid", 1 - transit_flux(separation(0, TR_PERIOD, TR_A, inc), TR_P, TR_U1,
                                          TR_U2)],
        ["depth_uni_mid", 1 - transit_flux(separation(0, TR_PERIOD, TR_A, inc), TR_P)],
        ["thetaE_mas", th_e * 180 / math.pi * 3600e3],
        ["RE_au", th_e * 4000 * PC / AU],
        ["A_u1", magnification(1.0)], ["A_u01", magnification(0.1)],
    ]
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

"""The Sun's apparent position for Book 3 (Year 1), shared by the ch. 1 and
ch. 27 scripts (spherical-astronomy, radiation-heat-transport).

A Kepler-orbit model of the Sun's apparent motion, from ledger values only:
  eccentricity e = 0.0167, obliquity 23.44 deg (NASA Earth fact sheet,
  ledger earth:ecc, earth:obliquity); longitude of perihelion 102.94719 deg
  (heliocentric, so the Sun's geocentric longitude of perigee is 282.94719 deg;
  ledger nasa:earth-perihelion-longitude); tropical year 365.2422 d (USNO,
  usno:tropical-year); the March equinox of 2026 on 20 March 14:46 UT
  (usno:seasons-2026), that is t = 78.615 d after 1 January 0 h UT.
Time t is in days after 1 January 0 h UT. No refraction, no nutation: the
model is good to a fraction of a degree, which is what the figures need.
"""
import math

ECC = 0.0167
OBL = math.radians(23.44)
VARPI = math.radians(102.94719 + 180.0)      # geocentric longitude of perigee
YEAR = 365.2422
T_EQUINOX = 31 + 28 + 19 + (14 + 46 / 60) / 24   # 20 March 14:46 UT


def kepler(M, e=ECC):
    """Eccentric anomaly E from the mean anomaly M (radians), Newton's method."""
    E = M
    for _ in range(30):
        E -= (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
    return E


def true_from_mean(M, e=ECC):
    E = kepler(M, e)
    return 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))


def mean_from_true(nu, e=ECC):
    E = 2 * math.atan2(math.sqrt(1 - e) * math.sin(nu / 2), math.sqrt(1 + e) * math.cos(nu / 2))
    return E - e * math.sin(E)


M_EQUINOX = mean_from_true(-VARPI)           # Sun at longitude 0 at the March equinox


def mean_anomaly(t):
    return M_EQUINOX + 2 * math.pi * (t - T_EQUINOX) / YEAR


def perihelion_time():
    """t (days after 1 Jan 0 h) of the perihelion that precedes the March equinox."""
    return T_EQUINOX - (M_EQUINOX % (2 * math.pi)) / (2 * math.pi) * YEAR


def longitude(t):
    """The Sun's ecliptic longitude (radians, in [0, 2 pi))."""
    return (true_from_mean(mean_anomaly(t)) + VARPI) % (2 * math.pi)


def distance_ratio(t):
    """r / a, the Sun--Earth distance in units of the semi-major axis."""
    E = kepler(mean_anomaly(t))
    return 1 - ECC * math.cos(E)


def declination(t):
    """sin(delta) = sin(epsilon) sin(lambda), in radians."""
    return math.asin(math.sin(OBL) * math.sin(longitude(t)))


def right_ascension(t):
    lam = longitude(t)
    return math.atan2(math.cos(OBL) * math.sin(lam), math.cos(lam)) % (2 * math.pi)


def equation_of_time(t):
    """Apparent minus mean solar time, in minutes (positive: the sundial is fast)."""
    L = (mean_anomaly(t) + VARPI) % (2 * math.pi)      # mean Sun's longitude
    d = (L - right_ascension(t) + math.pi) % (2 * math.pi) - math.pi
    return math.degrees(d) * 4.0


def altitude(phi, dec, H):
    """sin h = sin phi sin delta + cos phi cos delta cos H (radians)."""
    return math.asin(math.sin(phi) * math.sin(dec) + math.cos(phi) * math.cos(dec) * math.cos(H))


def azimuth(phi, dec, H):
    """Azimuth from north through east (radians, [0, 2 pi)); H > 0 west of the meridian."""
    h = altitude(phi, dec, H)
    c = (math.sin(dec) - math.sin(phi) * math.sin(h)) / (math.cos(phi) * math.cos(h))
    A = math.acos(max(-1.0, min(1.0, c)))
    return A if math.sin(H) <= 0 else 2 * math.pi - A


def rising_hour_angle(phi, dec):
    """H0 with cos H0 = -tan phi tan delta (radians); 0 if never rises, pi if never sets."""
    c = -math.tan(phi) * math.tan(dec)
    if c >= 1:
        return 0.0
    if c <= -1:
        return math.pi
    return math.acos(c)


def day_length(phi, dec):
    """Hours between the geometric rising and setting of the centre of the Sun."""
    return 2 * math.degrees(rising_hour_angle(phi, dec)) / 15.0

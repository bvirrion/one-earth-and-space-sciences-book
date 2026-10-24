"""Ch. 1 (spherical-astronomy): the Sun's paths, day lengths, the equation of
time, the celestial sphere and the spherical triangle obey their defining
formulas."""
import math
import os
import sys

HERE = os.path.join(os.path.dirname(__file__), "..", "..", "figdata", "bachelor-1")
sys.path.insert(0, HERE)
import _solar as S  # noqa: E402
import sun_paths as P  # noqa: E402
import day_length as D  # noqa: E402
import celestial_sphere as C  # noqa: E402
import spherical_triangle as T  # noqa: E402


def test_noon_altitude():
    # noon altitude = 90 - phi + delta (Sun south of the zenith)
    for d in (23.44, 0.0, -23.44):
        assert abs(P.noon_altitude(d) - (90 - 45 + d)) < 1e-9


def test_equinox_rises_due_east():
    path = P.path(0.0)
    az0, alt0 = path[0]
    assert abs(alt0) < 1e-9 and abs(az0 - 90.0) < 1e-6
    assert abs(path[-1][0] - 270.0) < 1e-6


def test_day_lengths():
    assert abs(S.day_length(math.radians(45), 0.0) - 12.0) < 1e-9
    assert abs(D.length(0, 172.0) - 12.0) < 1e-9                  # equator: always 12 h
    assert D.length(70, 172.0) == 24.0                             # midnight sun in June
    assert D.length(70, 355.0) == 0.0                              # polar night in December
    # symmetry: phi -> -phi at the opposite declination
    assert abs(S.day_length(math.radians(-30), math.radians(-10))
               - S.day_length(math.radians(30), math.radians(10))) < 1e-9


def test_declination_at_equinox_and_solstice():
    assert abs(math.degrees(S.declination(S.T_EQUINOX))) < 1e-6
    june = max(math.degrees(S.declination(t / 4)) for t in range(0, 4 * 365))
    assert abs(june - 23.44) < 0.01


def test_model_perihelion_near_usno():
    # USNO: perihelion 2026 on 3 January 17:15 UT, t = 2.72 d
    assert abs(S.perihelion_time() - 2.72) < 1.0


def test_equation_of_time():
    mx, mn, zeros = D.eot_extremes()
    assert 15.5 < mx[1] < 17.0 and 295 < mx[0] < 315        # early November, about +16 min
    assert -15.0 < mn[1] < -13.5 and 30 < mn[0] < 50         # mid-February, about -14 min
    assert len(zeros) == 4


def test_celestial_sphere():
    h, A = C.star_hA()
    # the star satisfies the altitude formula
    s = (math.sin(math.radians(45)) * math.sin(math.radians(25))
         + math.cos(math.radians(45)) * math.cos(math.radians(25)) * math.cos(math.radians(50)))
    assert abs(math.sin(h) - s) < 1e-12
    assert math.sin(A) < 0                         # west of the meridian, on the drawn half
    hc = C.hour_circle()
    assert abs(hc[0][0] + 2 * math.cos(math.radians(45))) < 1e-9     # starts at the pole
    assert abs(hc[0][1] - 2 * 0.9539 * math.sin(math.radians(45))) < 1e-9
    # the hour circle passes through the star
    sx, sy, _ = C.project(h, A)
    assert min(math.hypot(x - sx, y - sy) for x, y, _ in C.hour_circle(n=900)) < 0.01


def test_spherical_triangle_rules():
    A, B, Cv, a, b, c, aA, aB, aC = T.triangle()
    r = math.radians
    assert abs(math.cos(r(a)) - (math.cos(r(b)) * math.cos(r(c))
                                 + math.sin(r(b)) * math.sin(r(c)) * math.cos(r(aA)))) < 1e-12
    assert abs(math.sin(r(aA)) / math.sin(r(a)) - math.sin(r(aB)) / math.sin(r(b))) < 1e-12
    assert abs(math.sin(r(aB)) / math.sin(r(b)) - math.sin(r(aC)) / math.sin(r(c))) < 1e-12
    assert aA + aB + aC > 180
    for v in (A, B, Cv):
        assert T.project(v)[2] > 0                  # visible hemisphere

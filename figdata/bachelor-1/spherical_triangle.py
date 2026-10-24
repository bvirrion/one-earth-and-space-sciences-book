"""A spherical triangle drawn on a sphere of radius R = 2.4 cm in orthographic
projection (Year 1, spherical-astronomy). The view looks at the sphere from
latitude 20 deg, longitude 0 (sphere frame), with the sphere's axis tilted
toward the reader; every point drawn lies on the visible hemisphere.

  part ab | bc | ca    x y   great-circle arcs between the vertices
  part angA            x y   a small arc round A from AB to AC (the angle A)
  part verts           name x y
  part sides           name deg   the sides a, b, c and the angles A, B, C
                                  (degrees), with the cosine-rule check
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

R = 2.4
VIEW_LAT, VIEW_LON = math.radians(20), 0.0
VERT = {"A": (68.0, -5.0), "B": (8.0, -42.0), "C": (12.0, 38.0)}   # lat, lon in degrees


def unit(lat, lon):
    la, lo = math.radians(lat), math.radians(lon)
    return np.array([math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la)])


VIEW = unit(math.degrees(VIEW_LAT), VIEW_LON)
EAST = np.array([0.0, 1.0, 0.0])
UP = np.cross(VIEW, EAST)


def project(v):
    return (R * float(v @ EAST), R * float(v @ UP), float(v @ VIEW))


def slerp(p, q, n=40):
    w = math.acos(max(-1.0, min(1.0, float(p @ q))))
    return [(math.sin((1 - t) * w) * p + math.sin(t * w) * q) / math.sin(w)
            for t in (k / n for k in range(n + 1))]


def side(p, q):
    return math.degrees(math.acos(max(-1.0, min(1.0, float(p @ q)))))


def angle(at, p, q):
    """Angle of the spherical triangle at vertex `at` between the arcs to p and q."""
    tp = p - (p @ at) * at
    tq = q - (q @ at) * at
    return math.degrees(math.acos(float(tp @ tq) / (np.linalg.norm(tp) * np.linalg.norm(tq))))


def angle_arc(at, p, q, rad=0.16, n=24):
    tp = p - (p @ at) * at
    tp /= np.linalg.norm(tp)
    tq = q - (q @ at) * at
    tq /= np.linalg.norm(tq)
    w = math.acos(float(tp @ tq))
    pts = []
    for k in range(n + 1):
        t = k / n
        d = (math.sin((1 - t) * w) * tp + math.sin(t * w) * tq) / math.sin(w)
        pts.append(math.cos(rad) * at + math.sin(rad) * d)
    return pts


def triangle():
    A, B, C = (unit(*VERT[k]) for k in "ABC")
    a, b, c = side(B, C), side(C, A), side(A, B)
    return A, B, C, a, b, c, angle(A, B, C), angle(B, C, A), angle(C, A, B)


if __name__ == "__main__":
    A, B, C, a, b, c, aA, aB, aC = triangle()
    for name, (p, q) in {"ab": (A, B), "bc": (B, C), "ca": (C, A)}.items():
        write_table(__file__, ("x", "y"), [project(v)[:2] for v in slerp(p, q)], part=name, digits=5)
    write_table(__file__, ("x", "y"), [project(v)[:2] for v in angle_arc(A, B, C)], part="angA", digits=5)
    write_table(__file__, ("name", "x", "y"),
                [(k,) + project(v)[:2] for k, v in zip("ABC", (A, B, C))], part="verts", digits=5)
    cosrule = math.degrees(math.acos(math.cos(math.radians(b)) * math.cos(math.radians(c))
                                     + math.sin(math.radians(b)) * math.sin(math.radians(c))
                                     * math.cos(math.radians(aA))))
    write_table(__file__, ("name", "deg"),
                [("a", a), ("b", b), ("c", c), ("A", aA), ("B", aB), ("C", aC), ("a_cosrule", cosrule)],
                part="sides", digits=5)

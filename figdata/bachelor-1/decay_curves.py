"""Parent and radiogenic daughter against time (Year 1, radiometric-methods).

In a closed system with no initial daughter, the parent decays as
P = P0 2^(-n) after n half-lives and the radiogenic daughter grows as
D* = P0 (1 - 2^(-n)); their sum stays P0 and D*/P = 2^n - 1. No real number
enters: time is counted in half-lives.

  part curves   n P D            (n = 0-5 in half-lives; P and D* as fractions of P0)
  part marks    n P D ratio      (whole half-lives; ratio = D*/P)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402


def parent(n):
    return 2.0 ** (-n)


def daughter(n):
    return 1.0 - 2.0 ** (-n)


def ratio(n):
    return daughter(n) / parent(n)


if __name__ == "__main__":
    ns = [i / 20.0 for i in range(0, 101)]
    write_table(__file__, ("n", "P", "D"), [(n, parent(n), daughter(n)) for n in ns], part="curves")
    write_table(__file__, ("n", "P", "D", "ratio"),
                [(n, parent(n), daughter(n), ratio(n)) for n in range(0, 6)], part="marks")

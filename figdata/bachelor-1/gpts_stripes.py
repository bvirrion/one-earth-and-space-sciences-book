"""The geomagnetic polarity timescale 0-11 Ma and the striped sea floor it writes
(Year 1, plate-kinematics).

Normal-polarity intervals of the astronomically tuned timescale of Lourens et al.
(2004, ATNTS2004, as in the Geologic Time Scale 2004), as tabulated in the IODP
Expedition 320/321 methods chapter, Table T6 (ledger iodp:gpts2004); every normal
interval from the present to the base of C5n.2n (11.040 Ma) is kept, and the
reversed intervals are the gaps between them. Polarity 1 = normal, 0 = reversed.

A ridge spreading symmetrically at the half rate u (mm/yr = km/Myr) puts the crust
of age t at the distance x = u t on either side: each polarity interval becomes a
pair of stripes of width u * (duration).

  part gpts        age pol           (step function, for const plot)
  part stripes10   x pol             (half rate 10 mm/yr, x in km, both flanks)
  part stripes40   x pol             (half rate 40 mm/yr)
  part values      what value
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from _table import write_table  # noqa: E402

# normal-polarity intervals (top, base) in Ma, with their names (IODP Table T6)
NORMALS = [
    (0.000, 0.781, "C1n Brunhes"), (0.988, 1.072, "C1r.1n Jaramillo"),
    (1.173, 1.185, "C1r.2n Cobb Mountain"), (1.778, 1.945, "C2n Olduvai"),
    (2.128, 2.148, "C2r.1n Reunion"), (2.581, 3.032, "C2An.1n Gauss"),
    (3.116, 3.207, "C2An.2n"), (3.330, 3.596, "C2An.3n"),
    (4.187, 4.300, "C3n.1n Cochiti"), (4.493, 4.631, "C3n.2n Nunivak"),
    (4.799, 4.896, "C3n.3n Sidufjall"), (4.997, 5.235, "C3n.4n Thvera"),
    (6.033, 6.252, "C3An.1n"), (6.436, 6.733, "C3An.2n"), (7.140, 7.212, "C3Bn"),
    (7.251, 7.285, "C3Br.1n"), (7.454, 7.489, "C3Br.2n"), (7.528, 7.642, "C4n.1n"),
    (7.695, 8.108, "C4n.2n"), (8.254, 8.300, "C4r.1n"), (8.769, 9.098, "C4An"),
    (9.312, 9.409, "C4Ar.1n"), (9.656, 9.717, "C4Ar.2n"), (9.779, 9.934, "C5n.1n"),
    (9.987, 11.040, "C5n.2n"),
]
TMAX = NORMALS[-1][1]

# (base age in Ma, polarity of the interval that ends at this base)
CHRONS = []
for _i, (_top, _base, _name) in enumerate(NORMALS):
    if _top > 0:
        CHRONS.append((_top, 0))      # the reversed interval above this normal one
    CHRONS.append((_base, 1))


def intervals():
    """[(top, base, polarity)] from the present down to the base of C5n."""
    out, top = [], 0.0
    for base, pol in CHRONS:
        out.append((top, base, pol))
        top = base
    return out


def polarity_at(age):
    for top, base, pol in intervals():
        if top <= age < base:
            return pol
    raise ValueError(age)


def step_rows(scale=1.0, tmax=TMAX):
    """Rows (x, pol) for a const plot: one row at the top of each interval, and a
    closing row at the end; x = scale * age."""
    rows = [(scale * top, pol) for top, base, pol in intervals() if top < tmax]
    rows.append((scale * tmax, rows[-1][1]))
    return rows


def stripes(half_rate, tmax=TMAX):
    """Both flanks: x = -u t on the left, +u t on the right (km for mm/yr and Myr)."""
    right = step_rows(half_rate, tmax)
    # left flank as a const plot from -u tmax to 0: each block starts at -u*base
    lrows = []
    for top, base, pol in reversed(intervals()):
        if top < tmax:
            lrows.append((-half_rate * min(base, tmax), pol))
    return lrows + right


def stripe_widths(half_rate):
    return [(half_rate * (base - top), pol) for top, base, pol in intervals()]


def normal_fraction(tmax=TMAX):
    return sum(base - top for top, base, pol in intervals() if pol == 1) / tmax


if __name__ == "__main__":
    write_table(__file__, ("age", "pol"), step_rows(), part="gpts", digits=6)
    write_table(__file__, ("x", "pol"), stripes(10.0), part="stripes10", digits=6)
    write_table(__file__, ("x", "pol"), stripes(40.0), part="stripes40", digits=6)
    vals = [("n_intervals", len(intervals())), ("normal_fraction", normal_fraction()),
            ("c5n_young_edge", 9.779), ("c2an_young_edge", 2.581), ("brunhes_base", 0.781)]
    write_table(__file__, ("what", "value"), vals, part="values", digits=6)

"""Ancient massifs and the Wilson cycle (Year 2, wilson-cycle): a model ocean through one
cycle, and the supercontinents on a time chart.

  ocean     a model ocean of the Iapetus type, between two continents A and B. Rifting ends and
            sea-floor spreading starts at T_OPEN (Ma) at the full rate V_S (km/Myr = mm/yr);
            the ocean widens at V_S. At T_SUB a subduction zone starts at the margin of A and
            consumes the ocean floor at V_C relative to A while the ridge keeps spreading at
            V_S, so the ocean narrows at V_C - V_S until it is closed (collision). The model
            values are assumptions chosen for the figure, not measurements; the chapter cites
            the real ages (rifting c. 600 Ma, Caledonian phases 490-400 Ma: ledger rows
            mckerrow00:caledonian, mckerrow00:phases, schiffer20:caledonides).
  ridge     with symmetric spreading, the ridge moves relative to A at V_C - V_S / 2; it
            reaches the trench after d / (V_C - V_S / 2) if it starts d away.
  decay     after collision the mean elevation decays as h0 exp(-k f t) (the high-school
            volume's model): erosion rate k h with k = ln 10 / 11 per Myr (relief to 10 % in
            11 Myr without uplift, Book 2 ledger row ahnert70:decay) and isostatic rebound
            leaving the fraction f = (rho_m - rho_c) / rho_m of each eroded metre as lost
            height (2700 and 3300 kg/m3).
  supercontinents  assembly-to-breakup intervals of Nance (2022) (ledger nance22:supercontinents):
            Ur c. 3.0 Ga (a point), Kenorland 2.7-2.5 Ga, Nuna/Columbia 1.6-1.4 Ga, Rodinia
            950-800 Ma, Pannotia 620-580 Ma (debated), Pangaea 325-200 Ma.

  part ocean            t_Ma width_km   (model of the course text)
  part supercontinents  name row start_Ma end_Ma mid_Ma half_Ma
  part numbers          key value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

RHO_C, RHO_M = 2700.0, 3300.0
K_EROSION = math.log(10.0) / 11.0          # per Myr
F_REBOUND = (RHO_M - RHO_C) / RHO_M

# the course model (assumed rates)
T_OPEN, T_SUB = 570.0, 490.0               # Ma
V_S, V_C = 30.0, 60.0                      # km/Myr (= mm/yr)

SUPERCONTINENTS = [("Ur", 3000.0, 3000.0), ("Kenorland", 2700.0, 2500.0),
                   ("Nuna/Columbia", 1600.0, 1400.0), ("Rodinia", 950.0, 800.0),
                   ("Pannotia", 620.0, 580.0), ("Pangaea", 325.0, 200.0)]


def ocean_width(t_ma, t_open=T_OPEN, t_sub=T_SUB, vs=V_S, vc=V_C):
    """Width (km) of the model ocean at age t_ma (Ma, decreasing with time)."""
    if t_ma >= t_open:
        return 0.0
    if t_ma >= t_sub:
        return vs * (t_open - t_ma)
    w = vs * (t_open - t_sub) - (vc - vs) * (t_sub - t_ma)
    return max(w, 0.0)


def max_width(t_open=T_OPEN, t_sub=T_SUB, vs=V_S):
    return vs * (t_open - t_sub)


def closure_age(t_open=T_OPEN, t_sub=T_SUB, vs=V_S, vc=V_C):
    """Age (Ma) at which the model ocean closes."""
    return t_sub - max_width(t_open, t_sub, vs) / (vc - vs)


def ridge_arrival(d_km, vs, vc):
    """Myr for a ridge d_km from the trench to reach it (symmetric spreading)."""
    return d_km / (vc - vs / 2.0)


def decay_tau(k=K_EROSION, f=F_REBOUND):
    return 1.0 / (k * f)


def time_to_height(h0, h1, k=K_EROSION, f=F_REBOUND):
    """Myr for the mean elevation to fall from h0 to h1."""
    return decay_tau(k, f) * math.log(h0 / h1)


def supercontinent_rows():
    return [(n, i, a, b, (a + b) / 2.0) for i, (n, a, b) in enumerate(SUPERCONTINENTS)]


def mid_spacings():
    mids = [r[4] for r in supercontinent_rows()]
    return [mids[i] - mids[i + 1] for i in range(len(mids) - 1)]


def numbers():
    sp = mid_spacings()
    d = {"max_width_km": max_width(), "closure_Ma": closure_age(),
         "k_per_Myr": round(K_EROSION, 5), "f": round(F_REBOUND, 5),
         "tau_Myr": round(decay_tau(), 3), "mean_spacing_Myr": round(sum(sp) / len(sp), 1)}
    for i, x in enumerate(sp):
        d["spacing_%d_Myr" % (i + 1)] = x
    return d


if __name__ == "__main__":
    ages = [600.0 - 2.0 * i for i in range(0, 121)]          # 600 to 360 Ma
    write_table(__file__, ("t_Ma", "width_km"), [(t, round(ocean_width(t), 1)) for t in ages],
                part="ocean")
    write_table(__file__, ("name", "row", "start_Ma", "end_Ma", "mid_Ma", "half_Ma"),
                [(n.replace("/", "-"), i, a, b, m, (a - b) / 2.0)
                 for n, i, a, b, m in supercontinent_rows()],
                part="supercontinents")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")

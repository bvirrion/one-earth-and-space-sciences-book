"""Climate over geological time (Year 2, deep-time-climate): the silicate-weathering thermostat
as a one-box model of the excess carbon of the ocean--atmosphere, the Cenozoic benthic
isotope record (CENOGRID) and the Phanerozoic CO2 compilation (Foster et al. 2017).

  thermostat  dM/dt = V - W(M), M the excess carbon of the ocean--atmosphere over its steady
              state (PgC). The air keeps a fraction f = 0.08 of it once the ocean and the
              carbonates have taken their share (colbourn13:timescale), so C/C0 = 1 + f M / A0
              with A0 = 591 PgC, the pre-industrial air (ar6ch5:fig512). Warming
              dT = S log2(C/C0), S = 3 K (Book 2 row ipcc:ecs). Silicate weathering
              W = W0 exp(k dT), W0 = 11.5 Tmol C/yr (derry24:fluxes, 11-12) = 0.13813 PgC/yr
              (1 Tmol C = 0.012011 PgC); k = kT = 0.09 /K (colbourn13:weathering), or
              kT + beta krun = 0.09 + 0.65 x 0.045 with the run-off factor. Steady state at
              V = W0. Linearised e-folding time tau = A0 ln2 / (f k S W0).
  ceno        data/derived/bachelor-2-cenogrid.csv (data:b4-cenogrid), 100-kyr means of the
              benthic d18O and the dataset's long-term LOESS.
  petm        data/derived/bachelor-2-cenogrid-petm.csv, 55.5-56.3 Ma, d13C and d18O.
  co2         data/derived/bachelor-2-foster2017.csv (data:b4-foster2017), LOESS maximum and
              68 % band, every second row.

  part pulse    t_kyr M_nl M_lin dT_nl     (5000 PgC added at t = 0; k = kT)
  part step     t_kyr dT_nl dT_lin         (outgassing raised by 20 % at t = 0; k = kT)
  part ceno     age d18O d18O_lt
  part petm     age d13C d18O
  part co2      age co2 lo68 hi68
  part numbers  key value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

DERIVED = os.path.join(HERE, "..", "..", "data", "derived")

A0 = 591.0              # PgC, pre-industrial atmosphere (AR6 Fig. 5.12)
F_AIR = 0.08            # share of an excess left in the air for silicate weathering
S = 3.0                 # K per doubling of CO2 (ECS best estimate)
TMOL = 0.012011         # PgC per Tmol of carbon
W0 = 11.5 * TMOL        # PgC/yr, silicate weathering (Derry 2024: 11-12 Tmol/yr)
KT = 0.09               # 1/K, temperature sensitivity (Ea 63 kJ/mol at 288 K)
BETA, KRUN = 0.65, 0.045
K_RUN = KT + BETA * KRUN
LN2 = math.log(2.0)


def warming(m, s=S, f=F_AIR):
    """Warming (K) for an excess m (PgC) of the ocean--atmosphere."""
    return s * math.log(1.0 + f * m / A0, 2.0)


def weathering(m, k=KT, s=S, f=F_AIR):
    """Silicate weathering (PgC/yr) at an excess m."""
    return W0 * math.exp(k * warming(m, s, f))


def tau(k=KT, s=S, f=F_AIR, w=W0, c_ratio=1.0):
    """Linearised e-folding time (yr) about a steady state where C/C0 = c_ratio and the
    weathering equals w."""
    return A0 * c_ratio * LN2 / (f * k * s * w)


def steady_warming(v_ratio, k=KT):
    """Steady warming (K) when the outgassing is v_ratio times W0: W = V."""
    return math.log(v_ratio) / k


def steady_excess(v_ratio, k=KT, s=S, f=F_AIR):
    """Steady excess carbon (PgC) when the outgassing is v_ratio times W0."""
    return (2.0 ** (steady_warming(v_ratio, k) / s) - 1.0) * A0 / f


def integrate(m0, v_ratio, t_end, dt=200.0, k=KT):
    """RK4 integration of dM/dt = v_ratio W0 - W(M); returns [(t, M)] every dt years."""
    def rate(m):
        return v_ratio * W0 - weathering(m, k)
    out, m, t = [(0.0, m0)], m0, 0.0
    while t < t_end - 1e-9:
        k1 = rate(m)
        k2 = rate(m + 0.5 * dt * k1)
        k3 = rate(m + 0.5 * dt * k2)
        k4 = rate(m + dt * k3)
        m += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        t += dt
        out.append((t, m))
    return out


def time_to_fraction(m0, frac, dt=200.0, k=KT):
    """Years until a pulse m0 has fallen to frac of its size (non-linear model)."""
    m, t = m0, 0.0
    while m > frac * m0:
        k1 = W0 - weathering(m, k)
        k2 = W0 - weathering(m + 0.5 * dt * k1, k)
        k3 = W0 - weathering(m + 0.5 * dt * k2, k)
        k4 = W0 - weathering(m + dt * k3, k)
        m_new = m + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        if m_new <= frac * m0:
            return t + dt * (m - frac * m0) / (m - m_new)
        m, t = m_new, t + dt
    return t


def read_csv(name):
    with open(os.path.join(DERIVED, name), encoding="utf8") as f:
        return [{k: float(v) for k, v in r.items()} for r in csv.DictReader(f)]


PULSE = 5000.0
STEP = 1.2


def main():
    t_lin = tau()
    rows = []
    for t, m in integrate(PULSE, 1.0, 1.0e6, dt=200.0)[::25]:
        rows.append((t / 1e3, m, PULSE * math.exp(-t / t_lin), warming(m)))
    write_table(__file__, ("t_kyr", "M_nl", "M_lin", "dT_nl"), rows, part="pulse")

    m_star = steady_excess(STEP)
    dT_star = steady_warming(STEP)
    t_step = tau(c_ratio=1.0 + F_AIR * m_star / A0, w=STEP * W0)
    rows = []
    for t, m in integrate(0.0, STEP, 1.0e6, dt=200.0)[::25]:
        rows.append((t / 1e3, warming(m), dT_star * (1.0 - math.exp(-t / t_step))))
    write_table(__file__, ("t_kyr", "dT_nl", "dT_lin"), rows, part="step")

    ceno = read_csv("bachelor-2-cenogrid.csv")
    write_table(__file__, ("age", "d18O", "d18O_lt"),
                [(r["age_Ma"], r["d18O"], r["d18O_lt"]) for r in ceno], part="ceno")
    petm = read_csv("bachelor-2-cenogrid-petm.csv")
    write_table(__file__, ("age", "d13C", "d18O"),
                [(r["age_Ma"], r["d13C"], r["d18O"]) for r in petm
                 if 55.5 <= r["age_Ma"] <= 56.3], part="petm")
    co2 = read_csv("bachelor-2-foster2017.csv")
    write_table(__file__, ("age", "co2", "lo68", "hi68"),
                [(r["age_Ma"], r["co2"], r["lo68"], r["hi68"]) for r in co2[::2]], part="co2")

    nums = [
        ("W0_PgC", W0), ("tau_kT_kyr", t_lin / 1e3), ("tau_run_kyr", tau(k=K_RUN) / 1e3),
        ("k_run", K_RUN), ("tau_ess8_kyr", tau(s=8.0) / 1e3),
        ("dT_pulse0", warming(PULSE)), ("C_pulse0_ratio", 1 + F_AIR * PULSE / A0),
        ("rate_pulse0", weathering(PULSE) - W0),
        ("t90_lin_kyr", t_lin * math.log(10.0) / 1e3),
        ("t90_nl_kyr", time_to_fraction(PULSE, 0.1) / 1e3),
        ("dT_step", dT_star), ("M_step", m_star), ("C_step_ratio", 1 + F_AIR * m_star / A0),
        ("tau_step_kyr", t_step / 1e3),
    ]
    write_table(__file__, ("key", "value"), nums, part="numbers")


if __name__ == "__main__":
    main()

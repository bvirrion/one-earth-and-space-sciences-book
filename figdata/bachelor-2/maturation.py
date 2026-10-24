"""Maturation of kerogen (Year 2, energy-geology): first-order Arrhenius kinetics at a
constant heating rate, and vitrinite reflectance along a burial history.

  Kerogen kinetics: Green River oil shale, sample GR1, first-order distributed activation
  energy model (Gaussian), Fletcher and Pugmire (DOE topical report DE-FE0001243, OSTI 1176871),
  Table 5-2: A = 9.21e13 s^-1, mean E/R = 26,800 K, sigma/R = 481 K (ledger fp:gr-daem).

  Vitrinite reflectance: the Easy%Ro model of Sweeney and Burnham (1990) as tabulated in the
  Advanced Chemistry Basins Project final report (OSTI 830009), Table 5: A = 1e13 s^-1,
  activation energies 34 to 72 kcal/mol with weights (per cent, summing to 85), and
  %Ro = exp(-1.6 + 3.7 F), F the weighted converted fraction (ledger acb:easyro).

  tr        transformation ratio TR(T) = 1 - x of the Green River kerogen heated at a constant
            rate beta = 1 and 10 degC per million years from 10 degC; and the single-energy
            first-order approximation of the proposition (E/R = 26,800 K) for both rates.
  burial    the illustrative basin of the text (invented): sediment surface at 10 degC,
            gradient 30 degC/km, sediment accumulating at 100 m/Myr from 100 to 70 Ma and 35 m/Myr
            from 70 Ma to the present, no compaction. Depth (m) of the horizons deposited at
            100, 90, ..., 10 Ma against time (Ma), "nan" before deposition.
  fronts    depth (m) at which %Ro = 0.6 and 1.3 against time (Ma) in that basin, "nan" while
            no horizon has reached the value.
  vk        van Krevelen points of the Green River kerogen GR3.9 (Fletcher and Pugmire, Tables 2-4
            and 4-1; ledger fp14:gr-kerogen, fp14:gr-chars): atomic H/C and O/C of the kerogen
            and of its chars after laboratory heating at 10 K/min to 400-525 degC (t_c = 0 for the
            unheated kerogen). Atomic masses C 12.011, H 1.008, O 15.999.
  numbers   key values quoted in the text.

  part vk       t_c hc oc
  part tr       t_c tr1 tr10 app1 app10
  part burial   t_ma d100 d90 d80 d70 d60 d50 d40 d30 d20 d10
  part fronts   t_ma z06 z13
  part numbers  key value
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

MYR = 1e6 * 365.25 * 86400.0          # seconds in a million (Julian) years
R = 8.314462618                        # J/(mol K), CODATA (exact)
KCAL = 4184.0                          # J per thermochemical kilocalorie

# Green River GR1 (Fletcher and Pugmire, Table 5-2)
GR_A, GR_ER, GR_SR = 9.21e13, 26800.0, 481.0

# Easy%Ro (Sweeney and Burnham 1990): A, energies (kcal/mol) and weights (per cent)
RO_A = 1.0e13
RO_E = [34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72]
RO_W = [3, 3, 4, 4, 5, 5, 6, 4, 4, 7, 6, 6, 6, 5, 5, 4, 3, 2, 2, 1]

# illustrative basin of the text
TS, GRAD = 10.0, 30.0                  # degC, degC per km
PHASES = [(100.0, 70.0, 100.0), (70.0, 0.0, 35.0)]   # (from Ma, to Ma, m per Myr)


def gaussian_energies(e_r, s_r, n=241, width=6.0):
    """Activation energies (as E/R, K) and normalised weights of a Gaussian distribution."""
    x = np.linspace(-width, width, n)
    w = np.exp(-0.5 * x * x)
    return e_r + s_r * x, w / w.sum()


def tr_constant_rate(t_c, beta_c_per_myr, a=GR_A, e_r=GR_ER, s_r=GR_SR, t0_c=10.0, dt=0.05):
    """Transformation ratio at the temperatures t_c (degC, increasing) of a first-order
    distributed-energy reaction heated at a constant rate from t0_c: for each energy
    x_E = exp(-(A/beta) int_T0^T exp(-E/RT') dT'), and TR = 1 - sum w_E x_E."""
    beta = beta_c_per_myr / MYR
    es, ws = gaussian_energies(e_r, s_r)
    tk = np.arange(t0_c, max(t_c) + dt, dt) + 273.15
    k = np.exp(-es[:, None] / tk[None, :])                        # (nE, nT)
    integ = np.concatenate([np.zeros((len(es), 1)),
                            np.cumsum(0.5 * (k[:, 1:] + k[:, :-1]) * dt, axis=1)], axis=1)
    x = (ws[:, None] * np.exp(-(a / beta) * integ)).sum(axis=0)
    return np.interp(np.asarray(t_c) + 273.15, tk, 1.0 - x)


def x_single_approx(t_c, beta_c_per_myr, a=GR_A, e_r=GR_ER):
    """Unconverted fraction of the proposition: x = exp(-(A T^2/(beta E/R)) exp(-E/RT))."""
    tk = np.asarray(t_c) + 273.15
    beta = beta_c_per_myr / MYR
    return np.exp(-(a * tk * tk / (beta * e_r)) * np.exp(-e_r / tk))


def x_single_numeric(t_c, beta_c_per_myr, a=GR_A, e_r=GR_ER, t0_c=10.0, dt=0.01):
    """The same single-energy reaction integrated numerically (no approximation)."""
    beta = beta_c_per_myr / MYR
    tk = np.arange(t0_c, t_c + dt / 2, dt) + 273.15
    k = np.exp(-e_r / tk)
    integ = np.sum(0.5 * (k[1:] + k[:-1])) * dt
    return math.exp(-(a / beta) * integ)


def t_half(beta_c_per_myr, a=GR_A, e_r=GR_ER):
    """Temperature (degC) at which the single-energy reaction is half converted, from the
    proposition's approximation (bisection)."""
    lo, hi = 0.0, 400.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if x_single_approx(mid, beta_c_per_myr, a, e_r) > 0.5:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def easy_ro(times_myr, temps_c):
    """%Ro along a temperature history (times in Myr, increasing; temperatures in degC),
    Easy%Ro, temperature linear within each step. Returns the %Ro at every time."""
    es = np.array(RO_E, float) * KCAL / R            # E/R in K
    ws = np.array(RO_W, float) / 100.0
    integ = np.zeros(len(es))
    out = [math.exp(-1.6)]
    for i in range(1, len(times_myr)):
        dts = (times_myr[i] - times_myr[i - 1]) * MYR
        # Simpson on the step (temperature linear in time)
        t_a, t_b = temps_c[i - 1] + 273.15, temps_c[i] + 273.15
        t_m = 0.5 * (t_a + t_b)
        integ += RO_A * dts * (np.exp(-es / t_a) + 4 * np.exp(-es / t_m) + np.exp(-es / t_b)) / 6
        f = float((ws * (1.0 - np.exp(-integ))).sum())
        out.append(math.exp(-1.6 + 3.7 * f))
    return out


def sediment_thickness(t_ma, phases=PHASES):
    """Thickness (m) accumulated since the start of the first phase, at time t_ma."""
    s = 0.0
    for a, b, rate in phases:
        if t_ma >= a:
            break
        s += rate * (a - max(t_ma, b))
    return s


def depth(tau_ma, t_ma, phases=PHASES):
    """Depth (m) at time t_ma of the horizon deposited at tau_ma (t_ma <= tau_ma)."""
    return sediment_thickness(t_ma, phases) - sediment_thickness(tau_ma, phases)


def horizon_ro(tau_ma, step=0.1, ts=TS, grad=GRAD, phases=PHASES):
    """(times Ma, depths m, temperatures degC, %Ro) of the horizon deposited at tau_ma."""
    n = int(round(tau_ma / step))
    t_ma = [tau_ma - k * step for k in range(n + 1)]
    z = [depth(tau_ma, t, phases) for t in t_ma]
    temp = [ts + grad * zz / 1000.0 for zz in z]
    ro = easy_ro([tau_ma - t for t in t_ma], temp)
    return t_ma, z, temp, ro


def fronts(levels=(0.6, 1.3), step=1.0):
    """For every time t (Ma), the depth at which %Ro equals each level, interpolated between
    horizons deposited every `step` Myr."""
    taus = [100.0 - k * step for k in range(int(round(100.0 / step)))]
    hist = {tau: horizon_ro(tau) for tau in taus}
    out = []
    for kt in range(0, 101):
        t = 100.0 - kt
        row = [t]
        for lev in levels:
            pts = []
            for tau in taus:
                if tau < t:
                    continue
                tm, z, _, ro = hist[tau]
                i = int(round((tau - t) / 0.1))
                pts.append((z[i], ro[i]))
            pts.sort()
            val = "nan"
            for (z1, r1), (z2, r2) in zip(pts, pts[1:]):
                if r1 <= lev <= r2 and r2 > r1:
                    val = z1 + (lev - r1) * (z2 - z1) / (r2 - r1)
                    break
            row.append(val)
        out.append(tuple(row))
    return out


def crossing(tau_ma, level):
    """Time (Ma) and depth (m) at which the horizon deposited at tau_ma reaches %Ro = level."""
    tm, z, temp, ro = horizon_ro(tau_ma)
    for i in range(1, len(ro)):
        if ro[i - 1] < level <= ro[i]:
            f = (level - ro[i - 1]) / (ro[i] - ro[i - 1])
            return tm[i - 1] + f * (tm[i] - tm[i - 1]), z[i - 1] + f * (z[i] - z[i - 1]), \
                temp[i - 1] + f * (temp[i] - temp[i - 1])
    return None


def numbers():
    t_now = horizon_ro(100.0)
    c06, c13 = crossing(100.0, 0.6), crossing(100.0, 1.3)
    return {
        "oldest_ro06_t_ma": c06[0], "oldest_ro06_z": c06[1], "oldest_ro06_temp": c06[2],
        "oldest_ro13_t_ma": c13[0], "oldest_ro13_z": c13[1], "oldest_ro13_temp": c13[2],
        "t_half_1": t_half(1.0), "t_half_10": t_half(10.0),
        "rt2e_at_t_half_1": (t_half(1.0) + 273.15) ** 2 / GR_ER,
        "x_approx_150_1": float(x_single_approx(150.0, 1.0)),
        "x_exact_150_1": x_single_numeric(150.0, 1.0),
        "tr_daem_150_1": float(tr_constant_rate([150.0], 1.0)[0]),
        "tr_daem_150_10": float(tr_constant_rate([150.0], 10.0)[0]),
        "ro_oldest_now": t_now[3][-1], "z_oldest_now": t_now[1][-1], "t_oldest_now": t_now[2][-1],
        "ro_min": math.exp(-1.6), "ro_max": math.exp(-1.6 + 3.7 * sum(RO_W) / 100.0),
    }


# Green River GR3.9: kerogen, then chars (final temperature degC, wt% C, H, O by difference)
GR39 = [(0, 76.2, 9.5, 8.1), (400, 79.77, 9.45, 5.19), (434, 80.84, 9.22, 2.93),
        (450, 81.22, 8.61, 3.44), (460, 82.64, 8.32, 1.78), (470, 82.31, 7.89, 1.84),
        (490, 82.50, 4.93, 0.86), (525, 82.64, 3.77, 1.25)]


def atomic_ratios(c, h, o):
    """Atomic H/C and O/C from mass percentages."""
    nc = c / 12.011
    return (h / 1.008) / nc, (o / 15.999) / nc


def main():
    write_table(__file__, ("t_c", "hc", "oc"),
                [(t,) + atomic_ratios(c, h, o) for t, c, h, o in GR39], part="vk")
    temps = [10.0 + 2.0 * k for k in range(0, 121)]   # 10 to 250 degC
    tr1 = tr_constant_rate(temps, 1.0)
    tr10 = tr_constant_rate(temps, 10.0)
    ap1 = 1.0 - x_single_approx(temps, 1.0)
    ap10 = 1.0 - x_single_approx(temps, 10.0)
    write_table(__file__, ("t_c", "tr1", "tr10", "app1", "app10"),
                [(t, a, b, c, d) for t, a, b, c, d in zip(temps, tr1, tr10, ap1, ap10)], part="tr")

    taus = [100.0, 90.0, 80.0, 70.0, 60.0, 50.0, 40.0, 30.0, 20.0, 10.0]
    rows = []
    for kt in range(0, 201):
        t = 100.0 - 0.5 * kt
        rows.append(tuple([t] + [depth(tau, t) if t <= tau else "nan" for tau in taus]))
    write_table(__file__, ("t_ma",) + tuple("d%d" % tau for tau in taus), rows, part="burial")

    write_table(__file__, ("t_ma", "z06", "z13"), fronts(), part="fronts")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")


if __name__ == "__main__":
    main()

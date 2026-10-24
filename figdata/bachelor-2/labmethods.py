"""Field and laboratory methods II (Year 2, field-lab-methods-2): point counting, an XRF
accuracy check, isotope dilution, the exponential mass-bias law, and a mapping traverse
across the basement inlier of the Varden Hills.

  pc        relative standard error of a modal proportion p estimated from n counted points,
            sqrt((1 - p)/(n p)), for p = 0.05, 0.2, 0.5 (binomial counting).
  xrf       measured minus recommended SiO2 (wt %) for ten rock reference materials, USGS
            WDXRF fused-bead method: J. E. Taggart and D. F. Siems, USGS Open-File Report
            02-223-T, Table 2 (ledger usgsT:sio2-table). Columns: rec, meas, s, diff.
  stations  two west-east traverses across the basement inlier (y = 3.7 and 4.4 km,
            x = 2.8 to 4.2 km every 100 m): the unit at the ground surface of each station,
            read from the region model figdata/shared/region.py (code as region.UNITS).
  numbers   key values (station counts per unit; the worked isotope-dilution example).

Isotope data (ledger ciaaw:sr-isotopes, cheong14:spike): natural Sr isotope abundances
84 0.0056, 86 0.0986, 87 0.0700, 88 0.8258 (CIAAW); 84Sr-enriched spike with
84Sr/88Sr 561.4, 86Sr/88Sr 0.7661, 87Sr/88Sr 0.1819 and 15.271 ug/g Sr (Cheong, Jeong and
Kwon 2014); atomic masses of 86Sr 85.909261, 87Sr 86.908878, 88Sr 87.905612 (CIAAW).

  part pc        n rel05 rel20 rel50
  part xrf       rm rec meas s diff
  part stations  id x_km y_km z_m unit
  part numbers   key value
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "..", "shared"))
from _table import write_table  # noqa: E402
import region  # noqa: E402

# --- point counting -------------------------------------------------------------------
def binomial_sigma(p, n):
    """Standard error of a proportion p estimated from n independent points."""
    return math.sqrt(p * (1.0 - p) / n)


def relative_error(p, n):
    return binomial_sigma(p, n) / p


def points_needed(p, sigma):
    """Number of points for a standard error sigma (absolute) on a proportion p."""
    return p * (1.0 - p) / sigma ** 2


# --- XRF: USGS OFR 02-223-T Table 2, SiO2, rock reference materials --------------------
# (name, recommended value, measured mean, standard deviation), wt %
XRF_SIO2 = [
    ("BCR-2", 54.1, 54.17, 0.13),
    ("JA-2", 56.18, 56.5, 0.2),
    ("OU-1", 58.247, 57.93, 0.06),
    ("AGV-2", 59.3, 59.21, 0.18),
    ("AMH-1", 60.337, 59.84, 0.18),
    ("OU-4", 63.34, 63.22, 0.09),
    ("GBPG-1", 65.12, 65.14, 0.16),
    ("RGM-1", 73.45, 72.89, 0.19),
    ("YG-1", 73.363, 73.22, 0.14),
    ("OU-3", 74.090, 74.17, 0.11),
]


def least_squares(xs, ys):
    """Slope and intercept of the least-squares line y = a x + b."""
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    a = sxy / sxx
    return a, my - a * mx


# --- isotopes -------------------------------------------------------------------------
NAT = {84: 0.0056, 86: 0.0986, 87: 0.0700, 88: 0.8258}      # CIAAW amount fractions
SPIKE_OVER_88 = {84: 561.4, 86: 0.7661, 87: 0.1819, 88: 1.0}  # Cheong et al. 2014
SPIKE_CONC = 15.271e-6                                        # g Sr per g spike solution
SPIKE_AW = 83.9242                                            # atomic weight of spike Sr
NAT_AW = 87.62                                                # standard atomic weight of Sr
MASS = {86: 85.909261, 87: 86.908878, 88: 87.905612}
REF_86_88 = 0.1194


def spike_fraction(iso):
    tot = sum(SPIKE_OVER_88.values())
    return SPIKE_OVER_88[iso] / tot


def id_moles(n_spike86, r_spike, r_sample, r_mix):
    """Isotope dilution: moles of the reference isotope (86Sr) in the sample, from the moles
    of it in the spike and the 84/86 ratios of spike, sample and mixture."""
    return n_spike86 * (r_spike - r_mix) / (r_mix - r_sample)


def mix_ratio(n_sample86, n_spike86, r_spike, r_sample):
    """84/86 of the mixture (forward model, used by the tests)."""
    return (r_sample * n_sample86 + r_spike * n_spike86) / (n_sample86 + n_spike86)


def error_magnification(r_spike, r_sample, r_mix):
    """d ln N / d ln R_mix for the isotope dilution equation (absolute value)."""
    return r_mix * (r_spike - r_sample) / ((r_spike - r_mix) * (r_mix - r_sample))


def exp_law_beta(measured_86_88):
    """Exponent of the exponential mass-bias law from a measured 86Sr/88Sr."""
    return math.log(REF_86_88 / measured_86_88) / math.log(MASS[86] / MASS[88])


def exp_law_correct(measured, m_num, m_den, beta):
    """Correct a measured ratio of masses m_num/m_den with the exponential law."""
    return measured * (m_num / m_den) ** beta


def id_example(sample_g=0.1000, spike_g=0.2500, ppm=250.0):
    """Worked example: forward mixture ratio for a sample of known Sr content."""
    n_s86 = spike_g * SPIKE_CONC / SPIKE_AW * spike_fraction(86)
    n_x86 = sample_g * ppm * 1e-6 / NAT_AW * NAT[86]
    r_s = SPIKE_OVER_88[84] / SPIKE_OVER_88[86]
    r_x = NAT[84] / NAT[86]
    return n_s86, n_x86, r_s, r_x, mix_ratio(n_x86, n_s86, r_s, r_x)


# --- Varden Hills traverses -----------------------------------------------------------
def traverse(y, x0=2800.0, x1=4200.0, step=100.0):
    out = []
    x = x0
    while x <= x1 + 1e-6:
        z = region.topo(x, y)
        out.append((x, y, z, region.unit(x, y, z)))
        x += step
    return out


def stations():
    rows = []
    for y in (3700.0, 4400.0):
        rows.extend(traverse(y))
    return rows


def numbers():
    d = {}
    st = stations()
    names = {u[0]: u[1] for u in region.UNITS}
    for code in sorted(set(s[3] for s in st)):
        d["stations_" + names[code]] = sum(1 for s in st if s[3] == code)
    d["stations_total"] = len(st)
    n_s86, n_x86, r_s, r_x, r_m = id_example()
    d.update({"id_n_spike86": n_s86, "id_n_sample86": n_x86, "id_r_spike": r_s,
              "id_r_sample": r_x, "id_r_mix": r_m,
              "id_magnification": error_magnification(r_s, r_x, r_m),
              "id_r_mix_optimum": math.sqrt(r_s * r_x)})
    diffs = [m - r for _, r, m, _ in XRF_SIO2]
    d["xrf_mean_diff"] = sum(diffs) / len(diffs)
    d["xrf_max_abs_diff"] = max(abs(v) for v in diffs)
    return d


def main():
    ns = [100, 150, 200, 300, 400, 500, 700, 1000, 1500, 2000, 3000]
    write_table(__file__, ("n", "rel05", "rel20", "rel50"),
                [(n, 100 * relative_error(0.05, n), 100 * relative_error(0.2, n),
                  100 * relative_error(0.5, n)) for n in ns], part="pc")
    write_table(__file__, ("rm", "rec", "meas", "s", "diff"),
                [(nm, r, m, s, m - r) for nm, r, m, s in XRF_SIO2], part="xrf")
    write_table(__file__, ("id", "x_km", "y_km", "z_m", "unit"),
                [(i + 1, x / 1000, y / 1000, z, u) for i, (x, y, z, u) in enumerate(stations())],
                part="stations")
    write_table(__file__, ("key", "value"), sorted(numbers().items()), part="numbers")


if __name__ == "__main__":
    main()

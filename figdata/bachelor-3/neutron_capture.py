"""Neutron captures: which nuclei the s and r processes reach, and the sigma-N curve
(Year 3, origin of the elements).

Data: proto-solar isotopic abundances of Asplund, Amarsi and Grevesse (2021, Table B.1;
data/derived/bachelor-3-asplund21-isotopes.csv, ledger data:b5-asplund21), which also
serve as the list of the nuclei found in nature (stable or long-lived); Maxwellian-averaged
(n, gamma) cross sections at kT = 30 keV from KADoNiS v0.3 (data/derived/
bachelor-3-kadonis-macs.csv, ledger data:b5-kadonis).

Classification (the simplest form of the reasoning of Kaeppeler et al. 2011, Sect. I):
  s path    from 56Fe, capture a neutron; if the product is found in nature, go on from
            it. If not, look up its half-life and main decay mode (IAEA Live Chart of
            Nuclides, data/derived/bachelor-3-iaea-gs.csv, ledger data:b5-iaea-gs): if it
            lives longer than T_CAPTURE (1000 years, the time between two captures being
            hundreds to thousands of years, ledger cowan21:timescales) it captures again;
            otherwise it decays by its main mode (beta-minus: Z + 1; electron capture or
            beta-plus: Z - 1) until a nucleus found in nature, or a long-lived one, is
            reached: this is the main path, used for the sigma-N curve. At the branch
            points listed by Kaeppeler et al. (2011, Table III) the flow is followed both
            ways when the nuclei are classified (this brings 80Kr in, through 79Se); the
            branching through the isomer of 176Lu is not modelled, so 176Hf, which the
            literature counts as s-only, is classed here with the p nuclei. The path ends
            at 209Bi. Only nuclei beyond the iron peak (Z >= 31) are classified.
  r         the r process makes very neutron-rich nuclei that decay by beta-minus along
            their isobar; the chain stops at the first nucleus found in nature, the one of
            lowest Z. Any other isobar is shielded from the r process.
  classes   s-only (on the s path, shielded), r-only (reached by r, not on the s path),
            s+r (both), p (neither: the proton-rich nuclei).

sigma-N: for each s-only nucleus, the product of its cross section (mb) and its proto-solar
abundance N (per 1e6 silicon atoms). The classical model (Kaeppeler et al. 2011, eq. 5):
  sigma_A N_A = (G N56 / tau0) prod_{i = 56Fe .. A} (1 + 1/(tau0 sigma_i))^-1,
the product over the nuclei of the s path that capture a neutron, is fitted to the
s-only nuclei with A > 90 (G, the fraction of 56Fe irradiated, and tau0, the mean neutron
exposure in neutrons per mb), leaving out 176Lu, 176Hf, 187Os (made also by the decay of
the long-lived 176Lu and 187Re, or destroyed by it).

  part chart     Z N A cls             cls 0 s-only, 1 s+r, 2 r-only, 3 p; the strip
                                        Z 48-56 (Cd-Ba), N 60-84
  part path      Z0 N0 dZ dN kind       arrows of the s flow inside the strip, branch
                                        points followed both ways (kind 0 capture,
                                        1 decay)
  part unstable  Z N A                  unstable nuclei the s flow passes through there
  part sigman    A sigN Z el            s-only nuclei (mb per 1e6 Si)
  part fitted    A sigN_model           the classical curve at every capturing nucleus
  part values    what value
"""
import csv
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(HERE, ".."))
from _table import write_table  # noqa: E402

ISO = os.path.join(ROOT, "data", "derived", "bachelor-3-asplund21-isotopes.csv")
MACS = os.path.join(ROOT, "data", "derived", "bachelor-3-kadonis-macs.csv")
GS = os.path.join(ROOT, "data", "derived", "bachelor-3-iaea-gs.csv")
ZMIN = 31     # classification beyond the iron peak (Ga and heavier)
# branch points of the s path listed by Kaeppeler et al. (2011, Table III), where the
# flow splits between capture and decay (ledger kaeppeler11:branchings)
BRANCH_POINTS = {(28, 63), (34, 79), (36, 81), (36, 85), (40, 95), (55, 134), (55, 135),
                 (60, 147), (61, 147), (61, 148), (62, 151), (63, 154), (63, 155),
                 (64, 153), (65, 160), (67, 163), (69, 170), (69, 171), (73, 179), (74, 185),
                 (81, 204)}
YEAR = 3.15576e7
T_CAPTURE = 1000 * YEAR
STRIP = ((48, 56), (60, 84))
EXCLUDE_FIT = {(71, 176), (72, 176), (76, 187)}
SYMBOLS = {}


def load_isotopes(path=ISO):
    """{(Z, A): (el, fraction, log eps)}"""
    out = {}
    with open(path, encoding="utf8") as f:
        for r in csv.DictReader(f):
            out[(int(r["Z"]), int(r["A"]))] = (r["el"], float(r["frac_pct"]) / 100,
                                               float(r["logeps"]))
            SYMBOLS[int(r["Z"])] = r["el"]
    return out


def load_macs(path=MACS):
    """{(Z, A): MACS at 30 keV, mb} for ground states (isomers left out)."""
    out = {}
    with open(path, encoding="utf8") as f:
        for r in csv.DictReader(f):
            if r["isomer"] in ("-", "g"):
                out[(int(r["Z"]), int(r["A"]))] = float(r["macs30_mb"])
    return out


def load_decay(path=GS):
    """{(Z, A): (half-life in s or None for stable, main decay mode)}"""
    out = {}
    with open(path, encoding="utf8") as f:
        for r in csv.DictReader(f):
            z, n = int(r["Z"]), int(r["N"])
            t = float(r["half_life_s"]) if r["half_life_s"] else None
            out[(z, z + n)] = (t, r["decay_1"])
    return out


def isobars(nat, a):
    return sorted(z for z, aa in nat if aa == a)


def s_path(nat, decay, start=(26, 56), end=(83, 209)):
    """Steps (Z, A, kind) of the main s path: kind 'n' for a nucleus reached by a capture,
    'b' for one reached by a decay; also returns the nuclei that capture a neutron (found
    in nature, or unstable but longer-lived than T_CAPTURE)."""
    z, a = start
    steps = [(z, a, "start")]
    capturing = [(z, a)]
    while (z, a) != end:
        a += 1
        steps.append((z, a, "n"))
        while True:
            if (z, a) in nat:
                break
            t, mode = decay.get((z, a), (0.0, ""))
            if t is not None and t > T_CAPTURE:
                break
            if mode == "B-":
                z += 1
            elif mode.startswith("EC") or mode.startswith("B+"):
                z -= 1
            else:
                return steps, capturing       # alpha decay or unknown: the end (210Po)
            steps.append((z, a, "b"))
        capturing.append((z, a))
    return steps, capturing


def r_reached(nat):
    """Nuclei found in nature that the r-process decay chains reach: for each mass
    number, the isobar of lowest Z; plus everything heavier than 209 (Th, U)."""
    out = set()
    for a in {aa for _, aa in nat}:
        iso = isobars(nat, a)
        out.add((iso[0], a))
    return out | {(z, a) for z, a in nat if a > 209}


def successors(nat, decay, z, a, branches):
    """Next nuclei of the s flow from (Z, A): [(Z', A', kind)]. Main rule as in s_path; at
    the branch points of BRANCH_POINTS both the capture and the decay are followed."""
    t, mode = decay.get((z, a), (None, ""))
    long_lived = (z, a) in nat or (t is not None and t > T_CAPTURE)
    cap = (z, a + 1, "n")
    if mode == "B-":
        dec = (z + 1, a, "b")
    elif mode.startswith("EC") or mode.startswith("B+"):
        dec = (z - 1, a, "b")
    else:
        dec = None
    out = [cap] if long_lived else ([dec] if dec else [])
    if branches and (z, a) in BRANCH_POINTS:
        other = dec if long_lived else cap
        if other and other not in out:
            out.append(other)
    return out


def s_network(nat, decay, start=(26, 56), end=(83, 209)):
    """All nuclei the s flow reaches when the branch points are followed both ways, and
    the edges (Z, A, Z', A', kind)."""
    seen, edges, todo = {start}, [], [start]
    while todo:
        z, a = todo.pop()
        if (z, a) == end:
            continue
        for z2, a2, kind in successors(nat, decay, z, a, True):
            edges.append((z, a, z2, a2, kind))
            if (z2, a2) not in seen and a2 <= end[1]:
                seen.add((z2, a2))
                todo.append((z2, a2))
    return seen, edges


def classify(nat, decay, zmin=ZMIN):
    """Classes of the nuclei found in nature with Z >= zmin (beyond the iron peak)."""
    reached, _ = s_network(nat, decay)
    s = {k for k in reached if k in nat}
    r = r_reached(nat)
    cls = {}
    for k in nat:
        if k[0] < zmin:
            continue
        if k in s and k not in r:
            cls[k] = 0
        elif k in s and k in r:
            cls[k] = 1
        elif k in r:
            cls[k] = 2
        else:
            cls[k] = 3
    return cls


def abundance_per_si(nat, z, a):
    """Proto-solar number of atoms of (Z, A) per 1e6 silicon atoms. The element's log eps is
    rebuilt from all its isotopes (sum), so that rounding of the table to 0.01 dex
    averages out; the isotope's share is its fraction."""
    def elem(zz):
        return math.log10(sum(10 ** v[2] for (z2, _), v in nat.items() if z2 == zz))
    return nat[(z, a)][1] * 10 ** (elem(z) - elem(14) + 6)


def sigma_n(nat, macs, cls):
    rows = []
    for (z, a), c in sorted(cls.items(), key=lambda kv: kv[0][1]):
        if c == 0 and (z, a) in macs:
            rows.append((a, macs[(z, a)] * abundance_per_si(nat, z, a), z, SYMBOLS[z]))
    return rows


def classical(capturing, macs, g_n56, tau0):
    """sigma N at each capturing nucleus (list of (A, Z, value)); nuclei without a
    measured cross section are skipped (factor 1)."""
    out = []
    prod = 1.0
    for z, a in capturing:
        s = macs.get((z, a))
        if s is not None and s > 0:
            prod /= (1 + 1 / (tau0 * s))
        out.append((a, z, g_n56 / tau0 * prod))
    return out


def fit_classical(capturing, macs, points):
    """Least squares in log10 sigma N over points (A, Z, sigN): returns G N56, tau0, rms
    (dex)."""
    from scipy.optimize import least_squares
    idx = {(z, a): i for i, (z, a) in enumerate(capturing)}

    def resid(p):
        g, t = math.exp(p[0]), math.exp(p[1])
        model = classical(capturing, macs, g, t)
        return [math.log10(model[idx[(z, a)]][2]) - math.log10(v) for a, z, v in points]

    sol = least_squares(resid, [math.log(10.0), math.log(0.3)], method="lm")
    g, t = math.exp(sol.x[0]), math.exp(sol.x[1])
    rms = math.sqrt(sum(x * x for x in sol.fun) / len(sol.fun))
    return g, t, rms


def main():
    nat = load_isotopes()
    macs = load_macs()
    decay = load_decay()
    cls = classify(nat, decay)
    steps, capturing = s_path(nat, decay)
    (z0, z1), (n0, n1) = STRIP
    write_table(__file__, ("Z", "N", "A", "cls"),
                [(z, a - z, a, c) for (z, a), c in sorted(cls.items())
                 if z0 <= z <= z1 and n0 <= a - z <= n1], part="chart")
    arrows = []
    _, edges = s_network(nat, decay)
    for za, aa, zb, ab, kind in sorted(set(edges)):
        if z0 <= za <= z1 and n0 <= aa - za <= n1 and z0 <= zb <= z1 and n0 <= ab - zb <= n1:
            arrows.append((za, aa - za, zb - za, (ab - zb) - (aa - za), 0 if kind == "n" else 1))
    write_table(__file__, ("Z0", "N0", "dZ", "dN", "kind"), arrows, part="path")
    reached, _ = s_network(nat, decay)
    write_table(__file__, ("Z", "N", "A"),
                sorted((z, a - z, a) for z, a in reached if (z, a) not in nat
                       and z0 <= z <= z1 and n0 <= a - z <= n1), part="unstable")
    sn = sigma_n(nat, macs, cls)
    write_table(__file__, ("A", "sigN", "Z", "el"), sn, part="sigman")
    pts = [(a, z, v) for a, v, z, _ in sn if a > 90 and (z, a) not in EXCLUDE_FIT]
    g, t, rms = fit_classical(capturing, macs, pts)
    model = classical(capturing, macs, g, t)
    write_table(__file__, ("A", "sigN_model"), [(a, v) for a, _, v in model], part="fitted")
    n56 = abundance_per_si(nat, 26, 56)
    vals = [["n_nuclides", len(nat)], ["n_s_only", sum(c == 0 for c in cls.values())],
            ["n_s_and_r", sum(c == 1 for c in cls.values())],
            ["n_r_only", sum(c == 2 for c in cls.values())],
            ["n_p", sum(c == 3 for c in cls.values())],
            ["G_N56", g], ["tau0_per_mb", t], ["fit_rms_dex", rms], ["n_fit", len(pts)],
            ["N56_per_1e6Si", n56], ["G", g / n56]]
    for a, v, z, el in sn:
        vals.append(["sigN_%s%d" % (el, a), v])
    for z, a in ((52, 122), (52, 123), (52, 124), (62, 148), (62, 150), (56, 134), (56, 136),
                 (52, 128), (52, 130), (52, 120)):
        vals.append(["N_%s%d" % (SYMBOLS[z], a), abundance_per_si(nat, z, a)])
        vals.append(["macs_%s%d" % (SYMBOLS[z], a), macs[(z, a)]])
    write_table(__file__, ("what", "value"), vals, part="values")


if __name__ == "__main__":
    main()

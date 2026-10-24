"""Chemical formulas and equations as the books write them (mhchem syntax).

Shared by tools/check_ce_balance.py (every equation in the book is balanced)
and tools/molar_mass.py (every molar mass in a solution is computed, never
typed from memory). Standard library only, so the gates run with the system
python3; the figure-data scripts in figdata/ import it too.

What is understood, which is what the books use:

    2H2 + O2 -> 2H2O            coefficients, ' + ' between species
    1/2O2, 3/2 O2               fractional coefficients
    Cu^{2+}, Cu^2+, SO4^{2-}    charges after ^ ...
    OH-, H3O+, NH4+, Cl-        ... or a trailing sign (one or several)
    e-, 2e-, e^-                electrons
    (aq) (s) (l) (g)            states, ignored
    Ca(OH)2, [Cu(H2O)6]^{2+}    groups in round or square brackets
    CuSO4.5H2O, CuSO4*5H2O      addition compounds
    CH3-CH2-OH, CH2=CH2, HC#CH  bonds, ignored
    ->  <=>  <->  <=>>  <<=>  <-   arrows, with optional [above][below] labels
    CO2 ^ ,  AgCl v             gas and precipitate marks, ignored

A species written as a lowercase word (``methane + oxygen -> ...``) makes the
whole expression a word equation, which is not checked.
"""
import collections
import fractions
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, "..", "sources", "data_ledger.md")

ARROWS = ("<=>>", "<<=>", "<=>", "<->", "->", "<-")
STATES = re.compile(r"\((?:aq|s|l|g|sol|solv|cr)\)$")
COEF = re.compile(r"^(\d+/\d+|\d+(?:\.\d+)?|\(\d+/\d+\))\s*(?=[A-Z(\[e]|$)")


class ParseError(ValueError):
    pass


def atomic_weights(path=LEDGER):
    """{symbol: weight} from the ledger's ``aw:<Symbol>`` rows."""
    w = {}
    for line in open(path, encoding="utf8"):
        m = re.match(r"\|\s*aw:([A-Z][a-z]?)\s*\|[^|]*\|\s*([0-9.]+)\s*\|", line)
        if m:
            w[m.group(1)] = float(m.group(2))
    return w


def strip_arrow_labels(s, i):
    """Skip [..][..] labels following an arrow at position i (balanced)."""
    while i < len(s) and s[i] == "[":
        depth = 0
        j = i
        while j < len(s):
            if s[j] == "[":
                depth += 1
            elif s[j] == "]":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        i = j + 1
    return i


def split_arrow(expr):
    """(left, arrow, right) or None when the expression has no arrow."""
    # find the first arrow outside braces/brackets
    depth = 0
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in "{[":
            depth += 1
        elif c in "}]":
            depth -= 1
        elif depth == 0:
            for a in ARROWS:
                if expr.startswith(a, i):
                    j = strip_arrow_labels(expr, i + len(a))
                    return expr[:i], a, expr[j:]
        i += 1
    return None


def parse_charge(s):
    """Split a species into (body, charge)."""
    m = re.search(r"\^\{?(\d*)([+-])\}?$", s)
    if m:
        n = int(m.group(1) or 1)
        return s[:m.start()], n if m.group(2) == "+" else -n
    m = re.search(r"\^\{?([+-]+)\}?$", s)
    if m:
        signs = m.group(1)
        return s[:m.start()], signs.count("+") - signs.count("-")
    m = re.search(r"(?<=[A-Za-z0-9)\]])([+-]+)$", s)
    if m:
        signs = m.group(1)
        return s[:m.start()], signs.count("+") - signs.count("-")
    return s, 0


def parse_formula(s):
    """Atom counts of a formula body (no charge, no state, no coefficient)."""
    s = s.replace("{", "").replace("}", "")
    s = re.sub(r"^\^\d+", "", s)                  # isotope mass number
    parts = re.split(r"[.*·](?=\d*\s*[A-Z(\[])", s)
    total = collections.Counter()
    for k, part in enumerate(parts):
        mult = 1
        if k > 0:
            m = re.match(r"(\d+)\s*", part)
            if m:
                mult = int(m.group(1))
                part = part[m.end():]
        for el, n in _parse_group(part).items():
            total[el] += n * mult
    return total


def _parse_group(s):
    stack = [collections.Counter()]
    i = 0
    while i < len(s):
        c = s[i]
        if c in "-=#~ ":                         # bonds
            i += 1
        elif c in "([":
            stack.append(collections.Counter())
            i += 1
        elif c in ")]":
            if len(stack) == 1:
                raise ParseError("unbalanced bracket in %r" % s)
            grp = stack.pop()
            m = re.match(r"\d+", s[i + 1:])
            n = int(m.group(0)) if m else 1
            i += 1 + (m.end() if m else 0)
            for el, k in grp.items():
                stack[-1][el] += k * n
        elif c.isupper():
            m = re.match(r"([A-Z][a-z]?)(\d*)", s[i:])
            stack[-1][m.group(1)] += int(m.group(2) or 1)
            i += m.end()
        else:
            raise ParseError("cannot read %r in %r" % (c, s))
    if len(stack) != 1:
        raise ParseError("unbalanced bracket in %r" % s)
    return stack[0]


def parse_species(token):
    """(coefficient, atoms, charge) of one side's term."""
    t = token.strip()
    t = re.sub(r"\s+[v^]$", "", t)               # precipitate / gas marks
    coef = fractions.Fraction(1)
    m = COEF.match(t)
    if m:
        coef = fractions.Fraction(m.group(1).strip("()"))
        t = t[m.end():].strip()
    t = STATES.sub("", t).strip()
    if re.fullmatch(r"e(?:\^?\{?-\}?)", t):
        return coef, collections.Counter(), -1
    body, charge = parse_charge(t)
    body = STATES.sub("", body).strip()
    if not body:
        raise ParseError("empty species in %r" % token)
    return coef, parse_formula(body), charge


def is_word_equation(expr):
    return bool(re.search(r"(^|[\s+>])[a-z]{3,}", expr))


def side(text):
    terms = [t for t in re.split(r"\s\+\s", " " + text.strip() + " ") if t.strip()]
    return [parse_species(t) for t in terms]


def balance(expr):
    """None if balanced; otherwise a short description of the imbalance.

    Raises ParseError if the expression cannot be read, and returns "" for an
    expression with nothing to check (no arrow, or a word equation).
    """
    sp = split_arrow(expr)
    if sp is None:
        return ""
    left, _, right = sp
    if is_word_equation(left + " + " + right):
        return ""
    if not left.strip() or not right.strip():
        raise ParseError("an arrow with an empty side")
    if split_arrow(right) is not None:          # A -> B -> C: check each step
        first = balance(left + " -> " + split_arrow(right)[0])
        if first:
            return first
        return balance(right)
    tot = collections.Counter()
    q = fractions.Fraction(0)
    for sign, terms in ((1, side(left)), (-1, side(right))):
        for coef, atoms, charge in terms:
            for el, n in atoms.items():
                tot[el] += sign * coef * n
            q += sign * coef * charge
    bad = {el: n for el, n in tot.items() if n != 0}
    if not bad and q == 0:
        return None
    msg = []
    if bad:
        msg.append("atoms " + ", ".join("%s %+g" % (el, float(n)) for el, n in sorted(bad.items())))
    if q != 0:
        msg.append("charge %+g" % float(q))
    return "; ".join(msg)


def molar_mass(formula, weights=None):
    weights = weights or atomic_weights()
    body, _ = parse_charge(STATES.sub("", formula.strip()))
    atoms = parse_formula(body)
    missing = [el for el in atoms if el not in weights]
    if missing:
        raise KeyError("no ledger row aw:%s" % ", aw:".join(missing))
    return sum(weights[el] * n for el, n in atoms.items())

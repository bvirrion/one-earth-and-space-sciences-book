"""Book 4 (University, Year 2) -- es. Curation only; the rules live in tools/termlink/.

Curated 2026-10-30 by the Book 4 `es` agent from this edition's own harvest
(453 harvested, 467 linkable terms), with the frequency and chapter-set census
against the English twin (draft/b4-run/tools/census.py) and a context read of
every flagged site. University: AMBIG_POLICY = "drop", as book4_en.py.

A STOP entry keeps the term linked inside its own defining chapter (a local
definition) and stops it everywhere else; so each word below that is also an
ordinary Spanish word, or the name of another notion, links only where it is
defined, and the wrong senses inside that chapter are masked by EXTRA_PROTECT.

STOP:
  ley, leyes, ley (de un mineral)   ore grade (ch. 29); everywhere else "ley" is
                         a law (de Stokes, de Arrhenius, de Bragg, de Moseley,
                         de Rayleigh, exponencial, lognormal ...)
  exposición, exposición (a un peligro)   exposure to a hazard (ch. 28); ch. 17
                         and the climate chapters use the ordinary word
  detección, detección (del cambio climático)   detection of climate change
                         (ch. 27); ch. 22, 28 and 31 use detection methods,
                         detection time, limits of detection
  atribución             attribution of climate change (ch. 27 only)

EXTRA_PROTECT (a sense the term does not carry inside its own chapter):
  ley lognormal / normal / exponencial, según la ley, la ley espera, ley de X
                         ch. 29: the log-normal law, not the grade
  razón de mezcla que minimiza   ch. 31: the isotope-dilution mixture ratio,
                         not the atmospheric mixing ratio
"""

AMBIG_POLICY = "drop"

STOP = {
    "ley", "leyes", "Ley", "Leyes", "ley (de un mineral)",
    "exposición", "Exposición", "exposición (a un peligro)",
    "detección", "Detección", "detección (del cambio climático)",
    "atribución", "Atribución",
}

NO_CAPITAL = set()

EXTRA = {}

DROP = set()
DERIVED = {}
PRIMARY_OK = set()

EXTRA_PROTECT = [
    # ch. 29: "ley" as a law (log-normal, normal, exponential, a named law)
    r'(?<!\w)ley(?:es)?(?=\s+(?:lognormal|normal|exponencial|de\s+[A-Z]))',
    r'(?<=según la )ley(?!\w)',
    r'(?<=espera la )ley(?!\w)',
    # ch. 31: the isotope-dilution mixture ratio, not the atmospheric mixing ratio
    r'(?<!\w)razón de mezcla(?=\s+que\s+minimiza)',
]

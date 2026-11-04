"""Book 5 (University, Year 3) -- es. Curation only; the rules live in tools/termlink/.

Curated 2026-11-03 for the pilot edition, from the census against English (pilot_translation/census.py).
AMBIG_POLICY = "drop", as book5_en.py. STOP mirrors book5_en.py, plus one Spanish homograph; a STOP keeps a term linked
inside its defining chapter.

STOP:
  polo                   a pole on a net (ch. 8); elsewhere the Earth's poles
  línea de visión        InSAR (ch. 25); ch. 28 and 29 use the line of sight of radial velocity
  estado estacionario    the steady profile (ch. 18); generic elsewhere
  remolino               atmospheric eddy (ch. 20)
  edad modelo            ch. 13; ch. 26 uses crater model ages
  recuperación           crystal recovery (ch. 7); ch. 14 and 25 use the ordinary word
EXTRA:
  masculine forms of *limitada por ...* (the definition is about *incisión*, the text about *un río*), the
  plural of *variación* (the tail doesn't handle -ción/-ciones), and two surface forms English links.
"""

STOP = {
    "polo", "polos", "Polo", "Polos",
    "línea de visión", "líneas de visión", "Línea de visión",
    "estado estacionario", "estados estacionarios", "Estado estacionario",
    "remolino", "remolinos", "Remolino", "Remolinos",
    "edad modelo", "edades modelo", "Edad modelo",
    "recuperación", "Recuperación",
}
NO_CAPITAL = set()
EXTRA = {
    "limitado por el arranque": "def:b3:quantitative-geomorphology:limited",
    "limitados por el arranque": "def:b3:quantitative-geomorphology:limited",
    "limitado por el transporte": "def:b3:quantitative-geomorphology:limited",
    "limitados por el transporte": "def:b3:quantitative-geomorphology:limited",
    "variaciones del tiempo de tránsito": "def:b3:exoplanets:ttv",
    "cúmulo masivo de galaxias": "def:b3:milky-way-galaxies:groups",
    "extensión media del hielo marino": "def:b3:glaciology:sea-ice",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"
EXTRA_PROTECT = [
    r'(?<!\w)tasas?\s+de\s+producción\s+del\s+suelo\b',
    r'(?<!\w)tasas?\s+de\s+producción\s+de\s+suelo\b',
]

"""Book 4 (University, Year 2) -- fr. Curation only; the rules live in tools/termlink/.

Curated 2026-10-28 by the coordinator from this edition's own harvest, with the
frequency census against the English twin (translation_instruction.md). Each
entry is a French homograph or a missing form, judged against its own target.
"""

_ORE = "def:b2:ore-deposits:"

# STOP: ordinary words outside their defining chapter (the term still links in
# it), each against its target:
# - gisement(s): an ore deposit (ch29); elsewhere oil and gas fields and
#   geothermal reservoirs (ch16, 30), which English links as "field", never as
#   "deposit";
# - teneur(s): the grade of an ore (ch29); elsewhere the content of a rock or a
#   melt (teneur en silice, en eau: ch05, 12, 31);
# - détection, attribution: detection and attribution of climate change (ch27);
#   elsewhere a detection limit (ch31) and the attribution of a disaster (ch28);
# - nappe(s): a thrust sheet, in the Alps chapter (ch13) that defines it, where
#   the text uses the short form as English does; elsewhere a sill-like sheet
#   of magma (ch05), a pumice sheet or groundwater (ch06, 28, 29) and a debris
#   apron (ch17). "nappe de charriage" still links everywhere. STOP does not
#   hold back the EXTRA "nappe" below, so EXTRA_PROTECT masks those senses.
STOP = {"gisement", "Gisement", "gisements", "Gisements",
        "teneur", "Teneur", "teneurs", "Teneurs",
        "détection", "Détection", "attribution", "Attribution",
        "nappe", "Nappe", "nappes", "Nappes"}
NO_CAPITAL = set()
EXTRA = {
    # the short form of "nappe de charriage", as English links "nappe"; the
    # other senses are masked in EXTRA_PROTECT
    "nappe": "def:b2:alpine-orogen:nappes",
    "nappes": "def:b2:alpine-orogen:nappes",
    # the masculine and plural forms of the alumina-saturation classes, which
    # the definition gives in the feminine (une roche hyperalumineuse)
    "hyperalumineux": "def:b2:crustal-melting:asi",
    "Hyperalumineux": "def:b2:crustal-melting:asi",
    "hyperalumineuses": "def:b2:crustal-melting:asi",
    "métalumineux": "def:b2:crustal-melting:asi",
    "métalumineuses": "def:b2:crustal-melting:asi",
    "hyperalcalin": "def:b2:crustal-melting:asi",
    "hyperalcalins": "def:b2:crustal-melting:asi",
    "hyperalcalines": "def:b2:crustal-melting:asi",
    # the plural of planétésimal
    "planétésimaux": "def:b2:planet-formation-meteorites:planetesimal",
    "Planétésimaux": "def:b2:planet-formation-meteorites:planetesimal",
    # the definition names the metamorphism; the text uses the pressure range
    # (English links "ultrahigh-pressure")
    "ultra-haute pression": "def:b2:pt-paths:uhp",
    "Ultra-haute pression": "def:b2:pt-paths:uhp",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    # nappe: groundwater, a debris apron or a pumice sheet, not a thrust sheet
    # (EXTRA "nappe" is global; STOP does not hold an EXTRA entry back)
    r'\bune\s+nappe\s+de\s+débris', r'\bla\s+nappe\s+affleurant',
    r'\bla\s+nappe\s+peut', r'\bau-dessus\s+de\s+la\s+nappe',
    r'\bAvec\s+la\s+nappe\s+à', r'\bune\s+nappe\s+à\s+', r'\bnappe\s+souterraine',
    r'\bnappe\s+phréatique', r'\bmonter\s+la\s+nappe', r'\bnappe\s+de\s+ponce',
]

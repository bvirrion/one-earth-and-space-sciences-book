"""Book 5 (University, Year 3) -- nl. Curation only; the rules live in tools/termlink/.

Curated 2026-11-03 by the pilot run's coordinator from the census against English. AMBIG_POLICY = "drop", as book5_en.py.

STOP mirrors book5_en.py: the geographic and magnetic poles (pool, not the pole to a plane), any line of sight (zichtlijn in the
astronomy chapters, not the radar's), any steady state (stationaire toestand, not a landscape's), wervel (eddy), a crater-count
model age (modelouderdom, not an isotopic one). Added for Dutch: herstel (recovery of a deformed crystal) also means the
restoration of a section (ch. 8) and isostatic rebound. A STOP keeps a term linked in the chapter that pins its one sense.

EXTRA: Dutch welds compounds, so the harvest misses these targets; each form below was found unlinked in the text. Links are
accepted below English's per-target counts where a compound hides the term.
"""

_LIM = "def:b3:quantitative-geomorphology:limited"
_RD = "prop:b3:stable-isotopes:rayleigh-distillation"
_APW = "def:b3:palaeomagnetism:apw"
_ESM = "def:b3:climate-models:esm"
_SV = "thm:b3:ocean-dynamics:sverdrup"
_CB = "thm:b3:origin-of-elements:closed-box"

STOP = {"pool", "polen", "zichtlijn", "zichtlijnen", "stationaire toestand", "stationaire toestanden", "wervel", "wervels",
        "modelouderdom", "modelouderdommen", "herstel", "Herstel"}
NO_CAPITAL = set()
EXTRA = {
    "transportbeperkt": _LIM, "transportbeperkte": _LIM, "losmakingsbeperkt": _LIM, "losmakingsbeperkte": _LIM,
    "Rayleighdestillatie": _RD,
    "schijnbare poolverschuiving": _APW, "schijnbaar poolverschuivingspad": _APW,
    "aardsysteemmodel": _ESM, "aardsysteemmodellen": _ESM,
    "Sverdrupbalans": _SV,
    "gesloten-doosmodel": _CB, "gesloten doos": _CB,
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"
EXTRA_PROTECT = []

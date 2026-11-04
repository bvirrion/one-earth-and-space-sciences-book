"""Book 5 (University, Year 3) -- pt. Curation only; the rules live in tools/termlink/.

Curated 2026-11-03 by the Book 5 pt coordinator from this edition's own harvest, read against the English
twin's per-target link counts (pilot_translation/census.py), not copied from another edition. Homographs checked:

- "polo" / "polos": the pole to a plane (ch08), but the geographic and magnetic poles everywhere else, as English;
- "linha de visada": the radar's (ch25), but any line of sight to a star in ch28 and ch29, as English;
- "estado estacionário": a landscape's (ch18), but any steady state from ch19 on, as English;
- "turbilhão" / "turbilhões": the atmospheric eddy (ch20), but eddy viscosity in ch21, as English;
- "idade-modelo": an isotopic model age (ch13), but a crater-count model age in ch26, as English.
"""

STOP = {"polo", "Polo", "polos", "Polos",
        "linha de visada", "Linha de visada",
        "estado estacionário", "Estado estacionário",
        "turbilhão", "Turbilhão", "turbilhões", "Turbilhões",
        "idade-modelo", "Idade-modelo", "idades-modelo", "Idades-modelo"}
NO_CAPITAL = set()
EXTRA = {
    # a form the engine does not derive, at a site English links
    "variações do tempo de trânsito": "def:b3:exoplanets:ttv",
    "extensão média do gelo marinho": "def:b3:glaciology:sea-ice",
    # the index keys read "incisão limitada ..."; the prose says "um rio limitado ..."
    "limitado pelo destacamento": "def:b3:quantitative-geomorphology:limited",
    "limitado pelo transporte": "def:b3:quantitative-geomorphology:limited",
    "limitada pelo destacamento": "def:b3:quantitative-geomorphology:limited",
    "limitada pelo transporte": "def:b3:quantitative-geomorphology:limited",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"
EXTRA_PROTECT = []

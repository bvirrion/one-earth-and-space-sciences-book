"""Book 4 (University, Year 2) -- pt. Curation only; the rules live in tools/termlink/.

Curated 2026-10-30 by the Book 4 pt agent from this edition's own harvest, read
against the English twin's per-target link counts and chapter sets (census), not
copied from another edition. The link engine only links a term in its defining
chapter and later ones, so each entry below is judged on the chapters after the
definition. The English homographs of this book, checked in the pt displays:

- "teor" / "teores": the grade of an ore (ch29), but the content of a rock or a
  melt everywhere else ("o teor de sílica", ch31);
- "queda" / "quedas": a meteorite fall (ch02), but the ordinary word "drop, fall"
  in every later chapter (queda de temperatura, de pressão, de cinzas, queda
  livre: ch06, 07, 18, 19, 22, 23, 24, 26, 28, 29);
- "terreno" / "terrenos": a tectonic terrane (ch15), but the ground, the land
  or the terrain in ch18 (the two kinds of Archean terrain), ch20, ch28, ch29
  ("terreno mineralizado") and ch30 ("terreno oxidado"); inside ch15 the land
  surface ("superfície de terreno") is masked below;
- "detecção": the detection of climate change (ch27), but a detection limit in
  ch28 and ch31;
- "alóctones" / "autóctones": the plural harvested from the nappe sense
  ("alóctone (unidade rochosa)", ch13) caught the fossil assemblages of ch20,
  whose singulars link to their own definition; held to ch13.
"""

STOP = {"teor", "Teor", "teores", "Teores",
        "queda", "Queda", "quedas", "Quedas",
        "terreno", "Terreno", "terrenos", "Terrenos",
        "detecção", "Detecção",
        "alóctones", "autóctones"}
NO_CAPITAL = set()
EXTRA = {
    # irregular plurals the link engine does not derive (-ão -> -ões, -m -> -ns),
    # and adjective-first word orders; each is a site English links
    "seções balanceadas": "def:b2:alpine-orogen:balanced",
    "passagens oceânicas": "def:b2:deep-time-climate:gateway",
    "voláteis magmáticos": "def:b2:magma-emplacement:volatiles",
    "sistema de alerta sísmico precoce": "def:b2:geological-hazards:warning",
    # irregular and compound plurals (-ão -> -ões, -al -> -ais, -il -> -eis,
    # -ol -> -óis, a plural on the head noun of a hyphenated or multi-word term)
    "elementos incompatíveis": "def:b2:elements-in-the-earth:partition",
    "Elementos incompatíveis": "def:b2:elements-in-the-earth:partition",
    "elementos compatíveis": "def:b2:elements-in-the-earth:partition",
    "coeficientes de partição mineral--fundido": "def:b2:elements-in-the-earth:partition",
    "elementos-traço": "def:b2:elements-in-the-earth:trace",
    "Elementos-traço": "def:b2:elements-in-the-earth:trace",
    "reações metamórficas": "def:b2:metamorphic-facies:reaction",
    "reações de desvolatilização": "def:b2:metamorphic-facies:reaction",
    "inclinações de Clapeyron": "def:b2:metamorphic-facies:clapeyron",
    "icnofósseis": "def:b2:palaeoenvironments:fossil-kinds",
    "fósseis corporais": "def:b2:palaeoenvironments:fossil-kinds",
    "planetesimais": "def:b2:planet-formation-meteorites:planetesimal",
    "formações ferríferas bandadas": "def:b2:precambrian-earth:bif",
    "cinturões de rochas verdes": "def:b2:precambrian-earth:greenstone",
    "Cinturões de rochas verdes": "def:b2:precambrian-earth:greenstone",
    "atóis": "def:b2:oceanic-islands:reefs",
    "interglaciais": "def:b2:orbital-forcing:glacials",
    "monções": "def:b2:climate-variability:monsoon",
    "Monções": "def:b2:climate-variability:monsoon",
    "teleconexões": "def:b2:climate-variability:teleconnection",
    "nuvens moleculares": "def:b2:ism-star-formation:molecular-cloud",
    "Nuvens moleculares": "def:b2:ism-star-formation:molecular-cloud",
    "frações de fundido": "def:b2:mantle-melting:fraction",
    "pressões de vapor": "def:b2:atmospheric-thermodynamics:moist-air",
    "supersaturações": "def:b2:atmospheric-thermodynamics:microphysics",
    # ch24 and its solutions write the full name, as English does
    "reta da água meteórica": "prop:b2:isotope-geochemistry:mwl",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

# Lookaheads and lookbehinds only: nothing here consumes a `$`.
EXTRA_PROTECT = [
    # terreno in ch15 (its defining chapter): the land surface, not a terrane
    r'(?<!\w)superfície\s+de\s+terreno',
    r'(?<=e o )terreno(?=\s+tinha)',
    # razão de mistura: the CO2 mole fraction of the air (ch26), as English
    # protects "what mixing ratio"
    r'(?<!\w)que\s+razão\s+de\s+mistura',
    # "tempo de exposição": the exposure time of the exceedance law (ch28),
    # which English leaves unlinked; only exposure to a hazard links
    r'(?<!\w)tempo\s+de\s+exposição',
]

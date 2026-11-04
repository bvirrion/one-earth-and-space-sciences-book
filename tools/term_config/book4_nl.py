"""Book 4 (University, Year 2) -- nl. Curation only; the rules live in tools/termlink/.

Curated 2026-10-30 by the Book 4 nl agent from this edition's own harvest, the
frequency and chapter-set censuses against the English twin
(draft/b4-run/tools/census.py) and a scan of the inflected forms the Dutch
WORD_TAIL cannot make. Each entry was judged against its own target.

Dutch homographs of this book (each checked in context):
- gang (a dyke, b2.05): also "op gang houden" (b2.23) and "in gang zetten"
  (b2.18, b2.19), masked below. The burrows of b2.20, first written "gangen",
  are now "graafgangen" in the text, the precise word, so they never collide.
- mengverhouding: the mixing ratio of water vapour (b2.21); the CO2 mole
  fraction of b2.26 is masked below, as English masks it; the mixture ratio
  of isotope dilution (b2.31) now reads "verhouding van het mengsel".
- orogeen: the noun (b2.13); "Orogeen goud" (b2.29, orogenic gold) is the
  adjective, masked.
- detectie: harvested capitalised only (the definition opens on it); the
  lowercase uses (b2.28 warning systems, b2.31 detection limits) are other
  senses, so nothing is added.
- blootstelling: always exposure to a hazard (b2.28), as in English.
Kept although English does not link there, because the target is right:
oceaaneiland(en) in b2.26, oceaaneilandbasalt(en) in b2.09 (English writes the
hyphenated "ocean-island basalt" there), zeldzame aarde(n) (English links its
definition through no surface), peritectisch punt in b2.07 (English writes
"the peritectic P"), sporenelementen in b2.04/07/31.

EXTRA: the adjective inflection (-e) and the irregular plurals (vowel
shortening, -'s, consonant doubling) that WORD_TAIL (e?[ns]) cannot make, each
form found unlinked in the text; and the forms English links whose Dutch
surface differs from the harvested one.
"""

_E = "def:b2:elements-in-the-earth:"

STOP = set()
NO_CAPITAL = set()
EXTRA = {
    # b2.01-02: irregular plurals
    "protosterren": "def:b2:ism-star-formation:protostar",
    "protoplanetaire schijven": "def:b2:ism-star-formation:disc",
    "planetesimalen": "def:b2:planet-formation-meteorites:planetesimal",
    "condensatietemperaturen": "def:b2:planet-formation-meteorites:condensation",
    "petrologische types": "def:b2:planet-formation-meteorites:type",
    # English links "short-lived radionuclides" (b2.02 table caption)
    "kortlevende radionucliden": "def:b2:planet-formation-meteorites:slr",
    # b2.03: adjective + plural noun of the element classes
    "lithofiele elementen": _E + "goldschmidt",
    "Lithofiele elementen": _E + "goldschmidt",
    "siderofiele elementen": _E + "goldschmidt",
    "Siderofiele elementen": _E + "goldschmidt",
    "chalcofiele elementen": _E + "goldschmidt",
    "Chalcofiele elementen": _E + "goldschmidt",
    "atmofiele elementen": _E + "goldschmidt",
    "refractaire elementen": _E + "volatility",
    "vluchtige elementen": _E + "volatility",
    "incompatibele elementen": _E + "partition",
    "Incompatibele elementen": _E + "partition",
    "compatibele elementen": _E + "partition",
    "Compatibele elementen": _E + "partition",
    # b2.04: English links "mantle end-members"
    "eindleden van de mantel": "def:b2:isotope-geochemistry:end-members",
    # b2.05-07: magmas and eruptions
    "magma's": "def:b2:magma-emplacement:magma",
    "Magma's": "def:b2:magma-emplacement:magma",
    "magmatische vluchtige bestanddelen": "def:b2:magma-emplacement:volatiles",
    "pyroclastische stromen": "def:b2:eruptive-styles:pdc",
    "pyroclastische dichtheidsstromen": "def:b2:eruptive-styles:pdc",
    "primaire magma": "def:b2:mantle-melting:primary",
    "primaire magma's": "def:b2:mantle-melting:primary",
    # b2.08: Harker diagrams (English links the plural four times)
    "Harkerdiagrammen": "def:b2:magmatic-differentiation:harker",
    "cumulaten": "def:b2:magmatic-differentiation:cumulate",
    "incongruente smelten": "def:b2:mantle-melting:peritectic",
    # b2.10: English links "invariant point" and "univariant (lines)"
    "invariante punt": "def:b2:metamorphic-facies:invariant",
    "univariante lijnen": "def:b2:metamorphic-facies:univariant",
    # b2.12: migmatite parts
    "leucosomen": "def:b2:crustal-melting:migmatite",
    "melanosomen": "def:b2:crustal-melting:migmatite",
    # b2.13-17: orogens, basins, islands
    "orogenen": "def:b2:alpine-orogen:orogen",
    "botsingsorogenen": "def:b2:himalaya-andes:types",
    "intracratonische bekkens": "def:b2:basins-compared:types",
    "atollen": "def:b2:oceanic-islands:reefs",
    # b2.19-20, b2.26: oceanic anoxic events
    "oceanische anoxische gebeurtenissen": "def:b2:phanerozoic-earth:oae",
    # b2.21-23: the atmosphere
    "virtuele temperaturen": "def:b2:atmospheric-thermodynamics:virtual",
    "thermodynamische diagrammen": "def:b2:atmospheric-thermodynamics:diagram",
    "Köhlerkromme": "prop:b2:atmospheric-thermodynamics:kohler",
    "Köhlerkrommen": "prop:b2:atmospheric-thermodynamics:kohler",
    "Rossby-golven": "def:b2:weather-systems:rossby",
    "extratropische cyclonen": "def:b2:weather-systems:cyclones",
    # b2.24-25: archives and age models
    "speleothemen": "def:b2:climate-proxies:archives",
    "interglacialen": "def:b2:orbital-forcing:glacials",
    # b2.28-31
    "geologische gevaren": "def:b2:geological-hazards:risk",
    "hydrothermale vloeistoffen": "def:b2:ore-deposits:hydrothermal",
    "geothermische systemen": "def:b2:energy-geology:geothermal",
    "isotopenverdunning": "prop:b2:field-lab-methods-2:id",
    "Isotopenverdunning": "prop:b2:field-lab-methods-2:id",
    "gesmolten tabletten": "def:b2:field-lab-methods-2:xrf",
}
# the see-reference key and the inverted index key are harvested as terms but
# are never prose
DROP = {"waterhoudend smelten|see{fluxsmelten}", "zwakke jonge Zon, probleem van de"}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    # gang: idioms, not a dyke (b2.18, b2.19, b2.23)
    r'(?<!\w)op\s+gang\b', r'(?<!\w)in\s+gang\b', r'(?<!\w)aan\s+de\s+gang\b',
    # mengverhouding: the CO2 mole fraction of the air (b2.26), as English
    r'(?<!\w)welke\s+mengverhouding\b',
    # orogeen: the adjective of "orogenic gold" (b2.29)
    r'(?<!\w)Orogeen\s+goud\b',
]

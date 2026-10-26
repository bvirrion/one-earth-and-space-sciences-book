"""Book 2 (High School, grades 10-12) -- fr. Curation only; the rules live in tools/termlink/.

Curated 2026-10-25 by the Book 2 `fr` agent from this edition's own harvest,
with the frequency and chapter-set censuses against the English twin
(translation_instruction.md). Book 1 fr's protects were re-verified against
Book 2's text; only the Part-heading protect applies here (the Varden Hills
are named in Book 2, but never next to a linkable term in another sense).
"""

# STOP: ordinary words outside their defining chapter (the term still links
# inside it), each against its target:
# - stable, instable, stabilité: of air (g10.04); elsewhere stable layers of
#   water (g10.06), minerals (g10.07, g11.08, g12.03), cratons (g12.01) and
#   isotopes (g12.07), as English; "air stable" and "air instable" still link;
# - saturé, saturation: of air (g10.04); elsewhere a saturation content in the
#   storm chapter and peridotite saturated with water, as English;
# - flux: a flux of water (g10.09); elsewhere heat flow ("flux de chaleur",
#   g11.03, g12.06) and the energy flux of forcing (g12.10), as English;
# - stock: of water (g10.09); elsewhere a store of heat (g12.07 problem);
# - piège: of oil and gas (g11.09); elsewhere the verb (microbes trap grains,
#   g12.08 solutions), as English;
# - volcanique: the adjective is everywhere (volcanic islands, regions, front);
#   the term is reached through "roche volcanique", as English;
# - œil: the cyclone's eye (g10.05); elsewhere "à l'œil nu" and "d'un coup
#   d'œil" (g11.08, g12.03), as English;
# - aplatissement: of the ellipsoid (g10.01), as English (not met elsewhere);
# - orage: the thunderstorm (g10.05); elsewhere French "orage" translates the
#   English "storm" of a rainstorm on a field or a drainage basin (g10.07,
#   g10.08), which English never links;
# - éclair: lightning (g10.05); elsewhere a flash flood ("crues éclair",
#   g10.08) and flashes of light from a pebble (g11.07);
# - cassure: the fracture of a mineral (g11.07); elsewhere a fault is "une
#   cassure" (g12.02) and obsidian's conchoidal fracture (g11.08), which
#   English writes "fracture" unlinked.
STOP = {"stable", "Stable", "instable", "Instable", "stabilité",
        "saturé", "Saturé", "saturation", "Saturation",
        "flux", "stock", "piège", "volcanique", "œil", "aplatissement",
        "orage", "éclair", "cassure"}
NO_CAPITAL = set()
EXTRA = {
    # g12 climate-change: the chapter uses the short forms of its terms, as
    # English does ("forcing", "feedback", "scenario", "climate sensitivity")
    "forçage": "def:g12:climate-change:forcing",
    "forçages": "def:g12:climate-change:forcing",
    "rétroaction": "def:g12:climate-change:feedback",
    "rétroactions": "def:g12:climate-change:feedback",
    "scénario": "def:g12:climate-change:scenario",
    "scénarios": "def:g12:climate-change:scenario",
    "sensibilité climatique": "def:g12:climate-change:ecs",
    # g12 past-climates: English links its short "proxy" nine times; French
    # says "indicateur" for it, and the word has no other use in this book
    "indicateur": "def:g12:past-climates:proxy",
    "indicateurs": "def:g12:past-climates:proxy",
    # g11 fossil-fuel-geology: English links its short "seal" eighteen times;
    # French says "couverture" (the cover senses are protected below)
    "couverture": "def:g11:fossil-fuel-geology:reservoir",
    "couvertures": "def:g11:fossil-fuel-geology:reservoir",
    # g11 subduction-zones: English links its short "slab" everywhere; French
    # shortens "panneau plongeant" to "panneau" in the same places (the word
    # has no other use after the definition)
    "panneau": "def:g11:subduction-zones:slab",
    "panneaux": "def:g11:subduction-zones:slab",
}
DROP = set()
# French plurals in -aux and of "minéral" that the shared morphology does not
# derive (English links "tropical cyclones", "slabs", "clay minerals", "index
# minerals", "phenocrysts")
DERIVED = {
    "cyclone tropical": ["cyclones tropicaux", "Cyclones tropicaux"],
    "panneau plongeant": ["panneaux plongeants"],
    "minéral argileux": ["minéraux argileux"],
    "minéral index": ["minéraux index"],
    "phénocristal": ["phénocristaux", "Phénocristaux"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"

EXTRA_PROTECT = [
    # run-in paragraph headings stay unlinked, like section titles
    r'\\paragraph\{[^{}]*\}',
    # \pageref and inline \tikz, as in English
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # the bold Part headings of a weekend problem (as Book 1 fr)
    r'\\textbf\{Partie\s+[IVX]+\b(?:[^{}]|\{[^{}]*\})*\}',
    # intermédiaire: "par l'intermédiaire de" (by way of, g12.07) and an
    # emission scenario in the g12.10 table, not the rock composition
    r"\bpar\s+l'intermédiaire\b", r'&\s*intermédiaires?\s*&',
    # racine: the mathematical root, not a mountain root (g12.06, g12.08)
    r'\bracines?\s+(?:carrées?|quatrièmes?|cubiques?)\b',
    # océan profond: the depth of an ocean floor (g12.03), not the layer below
    # the thermocline (English protects "deep ocean floor")
    r'\bocéan\s+profond\s+de\s+\\qty\b',
    # lame mince: a thin sheet of magma (g12.03), not a thin section
    r'\blames?\s+minces?\s+de\s+magma\b',
    # débit: a mass flow rate of hot water (g12.06), not a river's discharge
    r'\bdébits?\s+massiques?\b',
    # roche mère: in g12.03 the parent rock of a metamorphic rock, the soil
    # sense of g10.07 that English links there; "nearest preceding" would send
    # it to the petroleum source rock of g11.09, so these three stay unlinked
    r'\best\s+sa\s+roche\s+mère\b', r'\\textbf\{roche\s+mère\}',
    r'\bchaque\s+roche\s+mère\b',
    # couverture: the sedimentary cover of a basement and the cloud cover,
    # not the seal of an oil trap
    r'\bcouvertures?\s+(?:sédimentaires?|de\s+sédiments|plissées?|brillantes?)\b',
    r'\b[Ll]a\s+couverture\s+(?:des\s+collines|repose|a\s+donc)\b',
    # proper names: the Last Interglacial (an AR6 reference period), the Glarus
    # and McConnell thrusts (named faults), as English
    r'\bdernier\s+interglaciaire\b',
    r'\bchevauchements?\s+(?:de\s+Glaris|de\s+McConnell)\b',
]

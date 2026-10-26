"""Book 2 (High School, grades 10-12) -- nl. Curation only; the rules live in tools/termlink/.

Curated 2026-10-25 by the Book 2 `nl` agent from this edition's own harvest,
frequency census and chapter-set census against the English twin.

English homographs of this book, kept as English keeps them (book2_en.py):
- oog (eye), flux, afplatting (flattening), verzadigd/verzadiging
  (saturated/saturation), stabiel/onstabiel (stable/unstable; "stabiele lucht"
  and "onstabiele lucht" still link), val (trap), vulkanisch (volcanic): STOP,
  linked only in their defining chapters.
Dutch homographs of this book (each checked in context):
- breuk: fracture of a mineral (g11.07) vs a fault in a rock (every tectonic
  chapter) and a fraction: STOP;
- val: also "de val" (a fall) and, with the -s tail, "vals" (false): STOP;
- gang: a dyke (g11.08) vs "aan de gang", "op gang", "de gang van zaken";
- voorraad: a stock of water (g10.09) vs a store of heat (g12.07);
- projectie: the climate projection (g12.10) vs a map projection (g10.01).
Irregular plurals the Dutch WORD_TAIL cannot make (vowel shortening,
consonant doubling, -'s) and the compounds the text uses are declared in EXTRA.
"""

STOP = {
    # as English
    "oog", "flux", "afplatting", "verzadigd", "verzadiging",
    "stabiel", "Stabiel", "onstabiel", "val", "vulkanisch",
    # Dutch homographs
    "breuk", "Breuk",
}
NO_CAPITAL = set()
EXTRA = {
    # g11 minerals: the definition opens on capitalised "Splijting", so the
    # lowercase noun never linked; "twee splijtrichtingen" is English's "two
    # cleavages" (coordinator, 2026-10-25, after the es report; English got
    # the same EXTRA)
    # g11 fossil fuels: the definition opens on capitalised "Migratie" (the same
    # trap; English got EXTRA "migration")
    "migratie": "def:g11:fossil-fuel-geology:migration",
    "splijting": "def:g11:minerals:cleavage",
    "splijtrichting": "def:g11:minerals:cleavage",
    "splijtrichtingen": "def:g11:minerals:cleavage",
    # g11 solutions/06: the defined force in other words, as English's EXTRA
    # "pull of the sinking slab"; the definition opens on capitalised
    # "Slabtrek" (coordinator, 2026-10-26)
    "trek van de wegzakkende slab": "def:g11:subduction-zones:slab-pull",
    "slabtrek": "def:g11:subduction-zones:slab-pull",
    # g12 climate-change: the chapter uses the short forms of its terms, as
    # English does (book2_en.py)
    "forcering": "def:g12:climate-change:forcing",
    "forceringen": "def:g12:climate-change:forcing",
    "stralingsforceringen": "def:g12:climate-change:forcing",
    "terugkoppeling": "def:g12:climate-change:feedback",
    "terugkoppelingen": "def:g12:climate-change:feedback",
    "klimaatterugkoppelingen": "def:g12:climate-change:feedback",
    "scenario": "def:g12:climate-change:scenario",
    "scenario's": "def:g12:climate-change:scenario",
    "uitstootscenario": "def:g12:climate-change:scenario",
    "klimaatgevoeligheid": "def:g12:climate-change:ecs",
    # irregular plurals (f -> v)
    "P-golven": "def:g11:seismic-structure:body-waves",
    "S-golven": "def:g11:seismic-structure:body-waves",
    # inflected adjective + noun, which the Dutch tail cannot make
    "sedimentaire bekkens": "def:g11:fossil-fuel-geology:basin",
    # coal compounds and the coal rank, as English links "bituminous coal",
    # "coal seam"
    "bitumineuze kool": "def:g11:fossil-fuel-geology:coal",
    "steenkoollaag": "def:g11:fossil-fuel-geology:coal",
    "steenkoollagen": "def:g11:fossil-fuel-geology:coal",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
EXTRA_PROTECT = [
    # run-in paragraph headings stay unlinked, like section titles
    r'\\paragraph\{[^{}]*\}',
    # \pageref and inline \tikz, as in English
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # gang: "in progress", "under way", "the course of"
    r'\baan\s+de\s+gang\b', r'\bop\s+gang\b', r'\bgang\s+van\s+zaken\b',
    # projectie: a map projection
    r'\bprojectie\s+van\s+Mollweide\b',
    # voorraad: a store of heat (g12.07), not a stock of water
    r'\bvoorraad\s+warmte\b', r'\b[Dd]e\s+voorraad\s+verliest\b', r'\bdezelfde\s+voorraad\b',
    # gelaagdheid: the bedding of a mud (g12.03), not the layering of the ocean
    r'\bgelaagdheid\s+van\s+de\s+modder\b',
    # proper names, as English: the Last Interglacial (an AR6 reference
    # period), the Glarus and McConnell thrusts (named faults)
    r'\b[Ll]aatste\s+interglaciaal\b', r'\b(?:Glarus|McConnell)-overschuiving\b',
    r'\bVarden\s+Hills\b',
]

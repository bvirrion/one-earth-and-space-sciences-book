"""Book 2 (High School, grades 10-12) -- id. Curation only; the rules live in tools/termlink/.

Curated 2026-10-26 by the Book 2 `id` agent from this edition's own harvest,
with the frequency and chapter-set censuses against the English twin
(translation_instruction.md). Book 1 id's protects were re-verified against
Book 2's text; only those that meet a Book 2 sentence are kept (Part heading,
\\pageref, inline \\tikz, Perbukitan Varden, "Gunung X").
"""

# STOP: ordinary words outside their defining chapter (the term still links
# inside it), each against its target, as English where English has the twin:
# - stabil, tidak stabil: of air (g10.04); elsewhere stable layers of water,
#   minerals, cratons and isotopes, as English; "udara stabil" and "udara tidak
#   stabil" still link;
# - jenuh, kejenuhan: of air (g10.04); elsewhere saturated with water (g12.04),
#   a saturation content, as English;
# - fluks: a flux of water (g10.09); elsewhere heat flux (g12.06) and the
#   energy flux of forcing (g12.10), as English;
# - stok: of water (g10.09); elsewhere a store of heat or of carbon;
# - perangkap: of oil and gas (g11.09); elsewhere "a trap" in another sense, as
#   English STOPs "trap";
# - mata: the cyclone's eye (g10.05); elsewhere "mata telanjang" (the naked
#   eye) and "mata air" (a spring), as English STOPs "eye";
# - penggepengan: of the ellipsoid (g10.01), as English "flattening";
# - peringkat: the rank of coal (g11.09); in g10.08 the rank m of a flood peak
#   in a sorted list, which English writes "rank" unlinked;
# - pecahan: the fracture of a mineral (g11.07); elsewhere a fragment ("sebuah
#   pecahan meteorit", g12.07), which English never links;
# - proyeksi: the climate projection (g12.10); a map projection elsewhere would
#   not be the term (none at present, kept as a guard);
# - vulkanik: the adjective is everywhere; English STOPs "volcanic" (an EXTRA
#   entry bypasses STOP, so the non-rock uses are protected below);
# - gaya: the EXTRA short form of "gaya radiatif" (below), linked inside the
#   climate-change chapter only: elsewhere "gaya" is a force (slab pull, ridge
#   push, buoyancy), never the forcing.
STOP = {"stabil", "Stabil", "tidak stabil", "Tidak stabil",
        "jenuh", "Jenuh", "kejenuhan", "Kejenuhan",
        "fluks", "stok", "perangkap", "Perangkap", "mata", "Mata",
        "penggepengan", "peringkat", "pecahan", "Pecahan", "proyeksi",
        "gaya", "Gaya", "gaya-gaya", "Gaya-gaya", "vulkanik"}
NO_CAPITAL = set()
EXTRA = {
    # g12 climate-change: the chapter uses the short forms of its terms, as
    # English does ("forcing", "feedback", "scenario", "climate sensitivity");
    # "gaya" is STOPped above so it links in that chapter only
    "gaya": "def:g12:climate-change:forcing",
    "Gaya": "def:g12:climate-change:forcing",
    "gaya-gaya": "def:g12:climate-change:forcing",
    "Gaya-gaya": "def:g12:climate-change:forcing",
    "umpan balik": "def:g12:climate-change:feedback",
    "Umpan balik": "def:g12:climate-change:feedback",
    "umpan balik-umpan balik": "def:g12:climate-change:feedback",
    "skenario": "def:g12:climate-change:scenario",
    "Skenario": "def:g12:climate-change:scenario",
    "skenario-skenario": "def:g12:climate-change:scenario",
    "sensitivitas iklim": "def:g12:climate-change:ecs",
    # g11 igneous-rocks: English links the bare adjectives "volcanic" (inside
    # its chapter, being STOPped) and "plutonic"; the definition harvests only
    # "batuan vulkanik/plutonik" ("vulkanik" is STOPped below, as English)
    "plutonik": "def:g11:igneous-rocks:volcanic-plutonic",
    "vulkanik": "def:g11:igneous-rocks:volcanic-plutonic",
    # reduplicated plural, which WORD_TAIL does not derive (English links
    # "clay minerals" in g11.07)
    "mineral-mineral lempung": "def:g10:soil-formation:clay",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
EXTRA_PROTECT = [
    # run-in paragraph headings stay unlinked, like section titles
    r'\\paragraph\{[^{}]*\}',
    # the bold Part headings of a weekend problem (as Book 1 id): the shared
    # list masks "\textbf{Part I ...}" only, not its translation
    r'\\textbf\{Bagian\s+[IVX]+\b(?:[^{}]|\{[^{}]*\})*\}',
    # \pageref and inline \tikz, as in English
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # proper names: the invented Varden Hills; "Gunung St.~Helens" and the
    # other named mountains (as Book 1 id)
    r'\bPerbukitan\s+Varden\b', r'\bGunung\s+[A-Z][A-Za-z]*',
    # proper names: the Last Interglacial (an AR6 reference period), the Glarus
    # and McConnell thrusts (named faults), as English
    r'\bInterglasial\s+Terakhir\b',
    r'\bSesar\s+(?:Naik|Anjak)\s+(?:Glarus|McConnell)\b',
    # belahan: the hemispheres ("Belahan Bumi Utara/Selatan", "kedua belahan
    # bumi"), not the cleavage of a mineral
    r'\b[Bb]elahan\s+[Bb]umi\b', r'\b(?:dua|satu|kedua)\s+belahan\b',
    # akar: the mathematical root, not a mountain root (as English protects
    # square/fourth/cube root); the roots of plants in the soil chapter
    r'\bakar\s+(?:kuadrat|pangkat|kubik|dari)\b',
    r'\bakar(?:-akar)?\s+(?:tumbuhan|pohon|tanaman)\b',
    # samudra dalam: the deep ocean floor (bathymetry), not the layer below the
    # thermocline (English protects "deep ocean floor")
    r'\bdasar\s+samudra\s+dalam\b',
    # intrusi: a saltwater intrusion into an aquifer, not an igneous intrusion
    r'\bintrusi\s+air\s+(?:laut|asin)\b',
    # vulkanik (EXTRA above, which bypasses STOP): the volcanic front of an arc
    # (g12.04) and a volcanic area (g12.06) are not the rock; English links
    # "volcanic" only for the rock ("means volcanic", "a volcanic glass")
    r'\bfront\s+vulkanik\b', r'\bkawasan\s+vulkanik\b',
]

"""Book 2 (High School, grades 10-12) -- en. Curation only; the rules live in tools/termlink/.

The book's writer curates this file in Phase C: Earth-science homographs to
check against each target (a fault in a rock vs a fault of reasoning; a plate vs
a dinner plate; a front in the weather vs the front of a house; a bed of rock vs
a river bed or a bed; a mantle; a shield; a cell (Hadley vs a living cell); a
basin; a scale (map, time, Richter); a table (water table vs a data table); a
current; a range; a crust; a core (Earth's core vs an ice core); a trench; a
ridge; an arc; a delta; a facies; a phase; a cycle; a season; a mass; a zone).
Use STOP (ordinary word outside its defining chapter), DROP (never a link),
EXTRA_PROTECT (regex phrases in another sense; multi-word patterns use \\s+).
Watch the capitalised-harvest trap: a display opening its sentence is
harvested capitalised, and STOP/DROP match case-sensitively.
"""

# Curated 2026-10-23 (Phase C), each against its target:
# - eye: the cyclone's eye (g10.05); elsewhere "the naked eye" (g11.08, g12.03);
# - flux: a flux of water (g10.09); elsewhere heat flux (g12.06), flux melting (g12.04);
# - flattening: of the ellipsoid (g10.01); elsewhere "flattening forests" (g12.04);
# - saturated, saturation: of air (g10.04); elsewhere peridotite saturated with water (g12.04);
# - stable, unstable, stability: of air (g10.04); elsewhere stable minerals,
#   isotopes, cratons (g11.08, g12.01, g12.03, g12.07); "stable air" and
#   "unstable air" still link;
# - trap: of oil and gas (g11.09); elsewhere the verb (dams trap sediment,
#   microbes trap grains);
# - volcanic: the adjective is everywhere (volcanic gases, arcs, ash); the term
#   is reached through "volcanic rock".
STOP = {"eye", "flux", "flattening", "saturated", "Saturated", "saturation",
        "stable", "Stable", "unstable", "stability", "trap", "volcanic"}
NO_CAPITAL = set()
EXTRA = {
    # g12 climate-change: the chapter uses the short forms of its terms
    "forcing": "def:g12:climate-change:forcing",
    "forcings": "def:g12:climate-change:forcing",
    "feedback": "def:g12:climate-change:feedback",
    "feedbacks": "def:g12:climate-change:feedback",
    "scenario": "def:g12:climate-change:scenario",
    "scenarios": "def:g12:climate-change:scenario",
    "climate sensitivity": "def:g12:climate-change:ecs",
    # g11 minerals: the definition opens on the capitalised display "Cleavage",
    # so the lowercase noun (30 sites, all the mineral sense) never linked
    # (es Book 2 agent, 2026-10-25)
    "cleavage": "def:g11:minerals:cleavage",
    "cleavages": "def:g11:minerals:cleavage",
    # g11 subduction solutions: the defined force in other words (es agent)
    "pull of the sinking slab": "def:g11:subduction-zones:slab-pull",
    # g11 fossil fuels: the definition opens on capitalised "Migration", so the
    # lowercase noun never linked (pt agent); Book 2 uses it in no other sense
    "migration": "def:g11:fossil-fuel-geology:migration",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"

EXTRA_PROTECT = [
    # intermediate: the depth of earthquakes (g11.06) and an emission scenario
    # (g12.10 table), not the rock composition
    r'\bIntermediate\s+and\s+deep\b', r'&\s*intermediate\s*&',
    # root: the mathematical root, not a mountain root
    r'\b(?:square|fourth|cube)[\s-]+root\b',
    # root: the roots of former volcanoes (g12.04), not a mountain root
    r'\btheir\s+roots\s+are\b', r'\broots\s+of\s+a\s+line\s+of\b',
    # deep ocean: the deep ocean floor (bathymetry), not the layer below the
    # thermocline
    r'\bdeep\s+ocean\s+floor\b',
    # proper names: the Last Interglacial (an AR6 reference period), the Glarus
    # and McConnell thrusts (named faults)
    r'\bLast\s+Interglacial\b', r'\b(?:Glarus|McConnell)\s+Thrust\b',
    # slab: a slab of rock (the black-shale specimen of g11.09 and its caption),
    # not the subducting slab (pt Book 2 agent, 2026-10-25)
    r'\bslab\s+of\s+black\s+shale\b', r'\bthe\s+slab\s+is\s+about\b',
    # heat flow: the verb "heat flows out of / from hot to cold" (g12.06), not
    # the measured quantity (pt agent)
    r'\b[Hh]eat\s+flows\s+(?:out|from)\b',
    # slab pull: "its slab pulls it down" (g12.02) and "the whole slab pulls"
    # (g11.06 solutions) are a noun and a verb, not the term (nl Book 2 agent,
    # 2026-10-25)
    r'\bslab\s+pulls\b',
    # run-in paragraph headings stay unlinked, like section titles
    r'\\paragraph\{[^{}]*\}',
]

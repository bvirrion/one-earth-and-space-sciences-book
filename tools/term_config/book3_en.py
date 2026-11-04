"""Book 3 (University, Year 1) -- en. Curation only; the rules live in tools/termlink/.

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
# - stable, stability, stably: of a triple junction (b1.12); elsewhere stable
#   minerals, isotopes, air and water columns (b1.07, 19, 25, 26, 29); the
#   multi-word terms "stable triple junction", "static stability" and "stable
#   stratification" still link;
# - extension: the strain e (b1.16); elsewhere the amount of rifting in
#   kilometres (b1.13) and "its extension in the Northern Hemisphere" (b1.28);
# - order: of an interference colour (b1.08); elsewhere "in order", "of the
#   order of", "to first order" (every chapter);
# - relief: optical relief (b1.08); elsewhere the topographic relief (b1.10,
#   11, 14, 15, 17, 20, 21);
# - series, system, stage, group, formation, member: the stratigraphic units
#   (b1.24); elsewhere "a series of", the solar system, a closed isotopic
#   system, "at this stage", deep-water formation, "a member of";
# - flux: of a source (b1.02); elsewhere heat, buoyancy, sediment and carbon
#   fluxes (b1.15, 19, 20, 27).
STOP = {"stable", "Stable", "stability", "stably", "extension", "order",
        "relief", "series", "system", "stage", "group", "formation",
        "member", "flux"}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    # declination: the magnetic declination of a compass (b1.06), not the
    # celestial coordinate
    r'\bmagnetic\s+declination\b',
    r'\bdeclination\s+(?:setting|correction|has\s+changed)\b',
    r'\b(?:for|set)\s+the\s+declination\b', r'\bThe\s+declination\.',
    # trend: a statistical trend (b1.20, b1.25), not the trend of a line
    r'\bExplain\s+the\s+trend\b', r'\boff\s+the\s+trend\b',
    # dip: a fall of the overturning (b1.29), not the dip of a plane
    r'\bmajor\s+dip\b',
    # strike: the verb (earthquakes, rays)
    r'\bfaulting\s+strike\b', r'\bstrikes\s+the\s+(?:boundary|Moho)\b',
    r'\breflection\s+strikes\b',
    # stretch: a stretch of a fault or of a rift, to stretch the crust
    r'\b(?:that|same|central)\s+stretch\b', r'\bstretch\s+of\s+(?:the|its)\b',
    r'\bstretch\s+the\s+crust\b',
    # sorting: the verb (states of stress), not the sorting of a sediment
    r'\bway\s+of\s+sorting\b',
    # mineral: the discipline
    r'\bmineral\s+physics\b',
    # order: "to first order", "in that order" (b1.08), not a colour order;
    # the first-order formula of the relief (b1.08 solutions)
    r'\bto\s+first\s+order\b', r'\bin\s+that\s+order\b', r'\bfirst-order\s+formula\b',
    # stable: stable parts of a plate (b1.12), not a stable junction
    r'\bon\s+stable\s+parts\b',
    # group: a working group of the subcommission, a nannofossil group (b1.24)
    r'\bworking\s+group\b', r'\bthe\s+group\s+proposed\b', r'\bnannofossil\s+group\b',
    # member: the voting members of a commission (b1.24), not a lithostratigraphic
    # member (found by the French edition, 2026-10-26; the box and the body linked them)
    r'\bvoting\s+members\b', r'\bmembers\s+not\s+voting\b',
    # cleavage: the cleavage of a mineral (b1.21), not of a rock
    r'\bgood\s+cleavage\b',
    # contacts: grain contacts (b1.23), not geological contacts on a map
    r'\bgrain\s+contacts\b',
    # proper names: the North Sea's Viking and Central Grabens (b1.23),
    # Darwin's book title The Structure and Distribution of Coral Reefs (b1.22)
    r'\bCentral\s+Grabens\b', r'\bCoral\s+Reefs\b',
]

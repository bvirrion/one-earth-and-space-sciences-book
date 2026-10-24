"""Book 4 (University, Year 2) -- en. Curation only; the rules live in tools/termlink/.

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

# Curated 2026-10-23 (Phase C), each link target checked:
# - allochthonous / autochthonous: the nappe sense (b2.13, indexed "... (rock
#   unit)") and the fossil sense (b2.20) are both defined; the harvest sees the
#   word defined twice and pins each sense to its own chapter, so b2.13 links
#   to the nappes and b2.20 to the assemblages, and no other chapter links;
# - exposure: to a hazard (b2.28); "exposure time" in the probability
#   formulas of b2.28 is a duration, protected below;
# - mixing ratio: of water vapour (b2.21); the carbon dioxide mixing ratio of
#   b2.26 is a mole fraction, protected below;
# - magma, dyke, sill, tonnage, atoll, chondrite, interglacial, climatology,
#   corona, snow line (always the protoplanetary disc's), free-fall time,
#   supersaturation (b2.21 onwards, cloud droplets only): every use checked,
#   one sense each.
STOP = set()
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    # exposure: the exposure time of a probability (b2.28), a duration
    r'\bexposure\s+time\b',
    # mixing ratio: the CO2 mole fraction of the air (b2.26)
    r'\bwhat\s+mixing\s+ratio\b',
]

"""Book 5 (University, Year 3) -- en. Curation only; the rules live in tools/termlink/.

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

# Ordinary words outside their defining chapter: the geographic and magnetic
# poles (not the pole to a plane), any line of sight (not the radar's), any
# steady state (not a landscape's), eddy viscosity (not an atmospheric eddy),
# a crater-count model age (not an isotopic one).
STOP = {"pole", "poles", "line of sight", "steady state", "eddy",
        "model age", "model ages"}
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "drop"

EXTRA_PROTECT = [
    r'\bsoil\s+production\s+rates?\b',
]

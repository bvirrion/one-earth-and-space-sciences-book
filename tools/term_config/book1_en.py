"""Book 1 (Primary and Middle School, grades 1-9) -- en. Curation only; the rules live in tools/termlink/.

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
# - intensity: physics owns light/sound intensity; the seismic sense is
#   reached through "intensity scale" (EXTRA) only;
# - cast, mould: ordinary words ("mould" of a fossil is defined inside the
#   fossil definition; elsewhere a cast/mould is a kitchen or casting object).
# - plan: g2's drawing; later chapters only use it as "evacuation plan",
#   "no plan", "to plan" (and its derived form caught "planes" in g9.5).
STOP = {"intensity", "Intensity", "cast", "mould", "plan", "plans", "planes"}
NO_CAPITAL = set()
EXTRA = {
    # g7 defines "tectonic plate (or simply a plate)": the short form is the
    # one the later chapters use
    "plate": "def:g7:plate-tectonics:plate",
    "plates": "def:g7:plate-tectonics:plate",
    "plate boundaries": "def:g7:plate-tectonics:plate-boundary",
    "divergent boundaries": "def:g7:plate-tectonics:plate-boundary",
    "convergent boundaries": "def:g7:plate-tectonics:plate-boundary",
    "transform boundaries": "def:g7:plate-tectonics:plate-boundary",
    "intensity scale": "def:g7:earthquakes:intensity",
}
DROP = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"

EXTRA_PROTECT = [
    # spring: the season and the steel spring of a seismometer (g7.3)
    r'\b(?:in|to|of|every)\s+spring\b', r'\bhot\s+springs?\b',
    r'\b(?:on\s+a|its|by\s+its|held\s+only\s+by\s+its)\s+spring\b',
    r'\bspring\s+of\s+\d',
    # well: the adverb
    r'\bwell\s+(?:back|below|above|away|beyond|before|after|known)\b',
    r'\bhow\s+well\b', r'\bas\s+well\b', r'\bfossilise\s+well\b',
    # source: of pollution, of data, of an air mass, of oil
    r'\bsources?\s+(?:rock|regions?|of)\b', r'\ba\s+source\s+of\b',
    r'\b(?:fixed|farther)\s+source\b', r'\breleased\s+at\s+the\s+source\b',
    # front: of a house, of a block
    r'\b(?:the|its)\s+front\s+(?:of|face)\b', r'\bin\s+front\s+of\b', r'\bfront\s+face\b',
    # scale: drawing to scale, time and other scales
    r'\bto\s+scale\b',
    r'\b(?:time|logarithmic|vertical|same|right|left|human|magnitude|this)\s+scales?\b',
    r'\blarge-scale\b', r'\bstep\s+of\s+the\s+scale\b',
    r'\b(?:the|a)\s+scale\s+of\b', r'\bon\s+(?:a|the|our)\s+scale\b',
    # proper names: the invented Varden Hills (a region, not the landform
    # definition), the Caspian Sea (a lake), the Hawaiian Volcano Observatory
    r'\bVarden\s+Hills\b', r'\bCaspian\s+Sea\b', r'\bVolcano\s+Observatory\b',
    # crust: the skin of a lava flow ("fresh lava crust", g7.2), not the Earth's crust
    r'\blava\s+crust\b',
    # snow: the National Snow and Ice Data Center (an institution, g8.5)
    r'\bNational\s+Snow\b',
    # sea: the NSIDC Sea Ice Index (a dataset name, g8.5)
    r'\bSea\s+Ice\s+Index\b',
    # coast: the United States Coast Guard (an institution, g9.2)
    r'\bCoast\s+Guard\b',
    # weather: the verb ("gold hardly weathers", g9.3)
    r'\bhardly\s+weathers\b',
    # run-in paragraph headings stay unlinked, like section titles
    r'\\paragraph\{[^{}]*\}',
    # sand: White Sands (a place name, g9.4)
    r'\bWhite\s+Sands\b',
    # institutions: the NOAA National Weather Service, the Intergovernmental
    # Panel on Climate Change
    r'\bNational\s+Weather\s+Service\b', r'\bPanel\s+on\s+Climate\s+Change\b',
    # table header (g6.3) and a place name (Big Spring, Missouri, g6.5)
    r'\brock\s*&\s*family\b', r'\bBig\s+Spring\b',
    # sea: the figure of speech ("a sea of snow-covered summits", g4.3)
    r'\ba\s+sea\s+of\s+snow',
    # pole: the Pole Star, a steel pole
    r'\bPole\s+Star\b', r'\bsteel\s+pole\b',
    # parallel: the adjective
    r'\bparallel\s+(?:to|lines)\b', r'\b(?:arrives|are|run|runs|lie|lies)\s+parallel\b',
    # core: an ice core
    r'\bice\s+cores?\b',
    # risk: the everyday phrase
    r'\bat\s+risk\b',
    # plan: a prevention plan
    r'\bprevention\s+plans?\b',
    # relief: the name of a dataset; era: the industrial era
    r'\bETOPO1\s+relief\b', r'\bindustrial\s+era\b',
    # \pageref is not in the shared protect list: a link inside its label
    # broke the build (g3.2, "fig:g3:...:world-map")
    r'\\pageref\{[^{}]*\}',
    # an inline \tikz command (a lithology swatch in a g7.5 table) is not in
    # the shared list either: a link inside its options broke the build
    r'\\tikz\b[^;$]*;',
    # plate: of ice, of coccoliths
    r'\bfloating\s+plates?\s+of\b', r'\btiny\s+plates\b',
]

"""Book 1 (Primary and Middle School, grades 1-9) -- nl. Curation only; the rules live in tools/termlink/.

Curated 2026-10-25 by the Book 1 `nl` agent from this edition's own harvest,
frequency census and chapter-set census against the English twin.

Dutch homographs of this book (each checked in context):
- meer: lake (g1) vs the adverb "more" -- the noun follows an article;
- weer: weather (g1) vs the adverb "again" -- the noun follows an article or
  "welk/voor/soort/rustig";
- hoogte: altitude (g4) vs any height (a bar, a wave, a star above the
  horizon, "op de hoogte"): linked only in its defining chapter; English's
  altitude target is reached through "zeeniveau" everywhere else;
- bron: river source (g5) vs groundwater spring (g6), resolved by
  nearest-preceding; "bron van" (a source of) is protected;
- schaal: the map scale (g2) vs "op schaal", time scales, the Richter-type
  scales;
- plaat/platen: the tectonic plate (g7, short form, as English) vs stone
  slabs (g3), plates of ice;
- front: the weather front (g8.3) vs the front of a lava flow;
- kern: the Earth's core (g6.4) vs an ice core (ijskern is a compound, so
  never matched) -- no collision found;
- intensiteit, afdruk, afgietsel: as English (intensity, cast, mould), linked
  only in their defining chapters.
Irregular plurals the Dutch WORD_TAIL cannot make (vowel shortening,
consonant doubling, -'s) are declared in EXTRA.
"""

STOP = {
    "hoogte", "Hoogte", "hoogten",
    "intensiteit", "Intensiteit",
    "afdruk", "afgietsel",
}
NO_CAPITAL = set()
EXTRA = {
    # coordinator, 2026-10-25: g6 defines the full name; the text uses the short
    # form (English now links "date line" by EXTRA too)
    "datumgrens": "def:g6:latitude-longitude:date-line",
    # g7 defines "tektonische plaat (of kortweg plaat)": the short form is the
    # one later chapters use, as in English
    "plaat": "def:g7:plate-tectonics:plate",
    "platen": "def:g7:plate-tectonics:plate",
    "plaatgrenzen": "def:g7:plate-tectonics:plate-boundary",
    # irregular plurals
    "meren": "def:g1:landscapes-around-us:water",
    "oceanen": "def:g2:water-on-earth:ocean",
    "zeeën": "def:g2:water-on-earth:ocean",
    "vulkanen": "def:g4:volcanoes-earthquakes-first-look:volcano",
    "polen": "def:g3:continents-and-oceans:poles",
    "kliffen": "def:g9:landforms:cliff",
    "grotten": "def:g9:landforms:karst",
    "zinkgaten": "def:g9:landforms:karst",
    "landschappen": "def:g1:landscapes-around-us:landscape",
    "mineralen": "def:g6:rocks-and-minerals:mineral",
    "delta's": "def:g5:water-shapes-the-land:delta",
    "tsunami's": "def:g7:earthquakes:tsunami",
    "meridianen": "def:g6:latitude-longitude:longitude",
    "luchtmassa's": "def:g8:fronts-and-weather-maps:air-mass",
    "isobaren": "def:g8:fronts-and-weather-maps:isobar",
    "anticyclonen": "def:g8:fronts-and-weather-maps:depression",
    "seismogrammen": "def:g7:earthquakes:seismometer",
    "era's": "def:g7:geological-time:era-period",
    "ijskappen": "def:g8:ice-on-earth:ice-sheet",
    "ijsplaten": "def:g8:ice-on-earth:ice-sheet",
    "convectiecellen": "def:g8:winds-global-circulation:convection-cell",
    "natuurgevaren": "def:g5:natural-hazards:hazard",
    "oceanische ruggen": "def:g8:the-oceans:seafloor",
    "diepzeetroggen": "def:g8:the-oceans:seafloor",
    "abyssale vlakten": "def:g8:the-oceans:seafloor",
    "toeslagmaterialen": "def:g9:earth-resources:aggregate",
    "bouwstenen": "def:g3:stones-pebbles-sand:building-stone",
    "rotsplaneten": "def:g6:earth-a-planet:planet-types",
    "reuzenplaneten": "def:g6:earth-a-planet:planet-types",
    "klimaatdiagrammen": "def:g5:weather-and-climate:climate-chart",
    # named members of a defined class, as English links "Tropic", "moraine"
    "Kreeftskeerkring": "def:g5:weather-and-climate:tropics",
    "Steenbokskeerkring": "def:g5:weather-and-climate:tropics",
    "noordpoolcirkel": "def:g5:weather-and-climate:tropics",
    "zuidpoolcirkel": "def:g5:weather-and-climate:tropics",
    "zijmorene": "def:g8:ice-on-earth:glacial-landforms",
    "eindmorene": "def:g8:ice-on-earth:glacial-landforms",
    "eindmorenen": "def:g8:ice-on-earth:glacial-landforms",
    "noorderbreedte": "def:g6:latitude-longitude:latitude",
    "zuiderbreedte": "def:g6:latitude-longitude:latitude",
}
# "Pyro" is the emphasised etymology inside the pyroclastic-flow definition
DROP = {"Pyro"}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"

EXTRA_PROTECT = [
    # meer: the adverb "more" -- the lake follows an article or a demonstrative
    r'(?<!\bhet\s)(?<!\bHet\s)(?<!\been\s)(?<!\bEen\s)(?<!\bhet~)\bmeer\b',
    # weer: the adverb "again"
    r'(?<!\bhet\s)(?<!\bHet\s)(?<!\bwelk\s)(?<!\bWelk\s)(?<!\bvoor\s)(?<!\bsoort\s)'
    r'(?<!\brustig\s)(?<!\bmooi\s)(?<!\bslecht\s)(?<!\bWat\s)(?<!\bwat\s)\bweer\b',
    r'\bheen\s+en\s+weer\b',
    r'\bMeer\s+(?:dan|of)\b',
    # monding: the mouth of a bay is not a river mouth
    r'\bmonding\s+van\s+(?:een|de)\s+baai\b',
    r'\blaat\s+het\s+weer\b',
    # bron: a source of something (data, energy, pollution)
    r'\bbronn?e?n?\s+van\b', r'\bBron:',
    # schaal: drawing to scale, other scales
    r'\b(?:niet\s+)?op\s+schaal\b', r'\bop\s+(?:grote|kleine|wereldwijde)\s+schaal\b',
    r'\b(?:verticale|horizontale|logaritmische|zelfde|dezelfde|menselijke)\s+schaal\b',
    r'\bschaal\s+van\s+(?:Richter|Mercalli|Mohs|de\s+tijd)\b',
    # plaat/platen: stone slabs, plates of ice, coccolith plates
    r'\b(?:stenen|dunne|piepkleine)\s+platen\b', r'\bplaten\s+van\s+(?:steen|ijs|gesteente)\b',
    r'\bplaatjes?\b',
    # plaat + the Dutch plural tail -s makes "plaats" (a place): never a plate
    r'\b[Pp]laats\b',
    r'\bplaat\s+(?:sediment|zandsteen|ijs|gesteente)\b',
    # schaal: an eggshell, a shell, a bowl; "on the scale of a lifetime"
    r'\b[Oo]p\s+(?:de|een|deze)\s+schaal\b',
    r'\b(?:breekbare|harde|ronde)\s+schaal\b', r'\b[Dd]e\s+schaal\s+is\s+als\b',
    r'\b(?:over|rond|in)\s+de\s+schaal\b', r'\bin\s+een\s+schaal\b',
    r'\bstap\s+van\s+de\s+schaal\b', r'\b[Dd]e\s+schaal\s+van\s+de\s+magnitude\b',
    # afzetting(en): a deposit (of ore, of old mudflows), not the process
    r'\b(?:zulke|bekende|nieuwe|armere|oude)\s+afzettingen\b', r'\buit\s+afzettingen\b',
    r'\bafzettingen\s+van\s+(?:oude\s+)?modderstromen\b',
    r'\b(?:een|de)\s+afzettinge?n?\s+(?:leeg|gaat|in\s+riviergrind|worden\s+ontgonnen)\b',
    # bron: the source of an earthquake's energy
    r'\bbij\s+de\s+bron\s+vrijkomt\b',
    # breuk: a fraction
    r'\b(?:op|als)\s+een\s+eenvoudige\s+breuk(?=\.)',
    # reliëf: the name of a dataset
    r'\breliëf\s+(?:van\s+)?(?:NOAA\s+)?ETOPO1\b',
    # uitbarstingen: bursts of strain release on a ridge (g7.1 solutions)
    r'\bkorte\s+uitbarstingen\b', r'\bjaren\s+en\s+uitbarstingen\b',
    # front: the front of a lava flow
    r'\bfront\s+van\s+een\s+lavastroom\b', r'\bhet\s+front\s+van\s+een\b',
    # proper names and institutions
    r'\bVarden\s+Hills\b', r'\bWhite\s+Sands\b', r'\bBig\s+Spring\b',
    r'\bNational\s+Weather\s+Service\b', r'\bCoast\s+Guard\b', r'\bSea\s+Ice\s+Index\b',
    r'\bKaspische\s+Zee\b',
    # run-in paragraph headings, \pageref and inline \tikz, as in English
    r'\\paragraph\{[^{}]*\}', r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # pool: the Pole Star
    r'\bPoolster\b',
    # risico: the everyday phrase
    r'\bloopt?\s+(?:geen\s+)?(?:gevaar|risico)\b',
]

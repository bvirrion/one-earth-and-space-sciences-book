"""Book 1 (Primary and Middle School, grades 1-9) -- es. Curation only; the rules live in tools/termlink/.

STUB written by the coordinator (2026-10-24). The Book 1 `es` agent curates it
from ITS OWN edition's harvest -- never by translating book1_en.py, never by
copying another book's config. book1_en.py's docstring lists the Earth-science
homographs to check (fault, plate, front, bed, mantle, shield, cell, basin,
scale, table, current, range, crust, core, trench, ridge, arc, delta, phase,
cycle, season, mass, zone); the target language has its own, found with the
frequency and chapter-set censuses (translation_instruction.md).

Curated 2026-10-25 by the Book 1 es agent, from the per-target census against
English (every target English reaches is reached) and a context read of every
over-linked target. The Spanish homographs, each checked against its target:
  tiempo   weather / time            (the time senses are protected below)
  escala   map scale / any scale     ("a escala", "a la misma escala", ...)
  frente   weather front / "frente a" (opposite, versus) / a glacier's snout
  plano    plan / flat / "en plano" / "primer plano"
  era      geological era / the verb "era" (was)
  longitud longitude / length
  globo    globe / balloon (the weather balloon of g8.1)
  placa    tectonic plate / a plate of ice, the plates of algae
  canto    pebble / "de canto" (on edge)
  falla    fault / "¿qué falla?" (what is wrong?)
  magnitud seismic magnitude / "orden de magnitud", "en magnitud"
  estrato  stratus cloud / rock layer / its etymology ("estrato significa capa")
"""

# "Piro" is harvested from the etymology in g7.2 ("\emph{Piro} significa fuego").
STOP = set()
# "Ecuador" capitalised is the country (g4.2 solutions); the line is "el ecuador"
NO_CAPITAL = {"ecuador"}
EXTRA = {
    # coordinator, 2026-10-25: g6 defines the full name; the text uses the short
    # form (English now links "date line" by EXTRA too)
    "línea de cambio de fecha": "def:g6:latitude-longitude:date-line",
    # g7 defines "placa tectónica (o simplemente una placa)": the short form
    # is the one the later chapters use
    "placa": "def:g7:plate-tectonics:plate",
    "placas": "def:g7:plate-tectonics:plate",
    # Spanish plurals the shared morphology misses (the stressed vowel loses
    # or gains its accent: volcán -> volcanes, inundación -> inundaciones)
    "volcanes": "def:g4:volcanoes-earthquakes-first-look:volcano",
    "inundaciones": "def:g5:water-shapes-the-land:flood",
    "erupciones": "def:g4:volcanoes-earthquakes-first-look:eruption",
    "erupciones explosivas": "def:g7:volcanoes:eruption-types",
    "erupciones efusivas": "def:g7:volcanoes:eruption-types",
    "anticiclones": "def:g8:fronts-and-weather-maps:depression",
    "glaciaciones": "def:g8:ice-on-earth:ice-age",
    "estaciones meteorológicas": "def:g4:clouds-rain-snow:weather-station",
    "globos terráqueos": "def:g3:continents-and-oceans:globe",
    # the short forms the later chapters use: "el globo", "los cantos"
    "globo": "def:g3:continents-and-oceans:globe",
    "globos": "def:g3:continents-and-oceans:globe",
    "canto": "def:g3:stones-pebbles-sand:pebble",
    "cantos": "def:g3:stones-pebbles-sand:pebble",
    # the short forms g7.2 and g8.4 use: "la boca" (of a volcano), "el giro"
    # (the earlier everyday uses, a jar's mouth in g4.1 and the Earth's turn
    # in g6.2, come before the definitions and are never linked)
    "boca": "def:g7:volcanoes:vent",
    "bocas": "def:g7:volcanoes:vent",
    "giro": "def:g8:the-oceans:current",
    "giros": "def:g8:the-oceans:current",
    # a river in flood: "en las crecidas, el río se desborda"
    "crecida": "def:g5:water-shapes-the-land:flood",
    "crecidas": "def:g5:water-shapes-the-land:flood",
    # English "flood zone" (g9.2), where Spanish says "zona inundable"
    "zona inundable": "def:g5:water-shapes-the-land:flood",
    # the seismic intensity scale (the hazard's intensity in g9.2 is not it)
    "escala de intensidad": "def:g7:earthquakes:intensity",
    "escala de intensidades": "def:g7:earthquakes:intensity",
}
DROP = {"Piro"}
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"

EXTRA_PROTECT = [
    # tiempo: time, not weather
    r'\bmás\s+de\s+tiempo\b',
    r'\b(?:[Mm]ucho|[Mm]uchísimo|poco|más|tanto|[Cc]uánto|cuanto|largo|otro|mismo)\s+tiempo\b',
    r'\btodo\s+el\s+tiempo\b(?!\s+meteorol)',
    r'\bun\s+tiempo\b(?!\s+(?:poco|seco|estable))',
    r'\ba\s+tiempo\b', r'\b[Cc]on\s+el\s+tiempo\b', r'\btodo\s+tiempo\b',
    r'\b[Tt]iempos\b(?!\s+son:)',
    r'\btiempo\s+(?:suficiente|inmenso|que\s+tardan?|de\s+(?:crecer|infiltrarse|explotación|formación|uso)|para|sale|avanza|después)\b',
    r'\b(?:escalas?|eje|intervalos|abismo|función|error)\s+del?\s+tiempo\b(?!\s+geol)',
    r'\b(?:falta|da|eran|tienen?|mide\s+este|ese)\s+tiempo\b',
    r'\bavanza\s+(?:en\s+)?el\s+tiempo\b',
    r'\bel\s+agua\s+y\s+el\s+tiempo\b',
    # escala: drawing to scale and the other scales
    r'\b(?:no\s+|sin\s+)?a\s+escala\b', r'\bsin\s+escala\b',
    r'\ba\s+la\s+misma\s+escala\b', r'\b[Aa]\s+la\s+escala\s+del?\b',
    r'\b(?:las\s+)?mismas\s+escalas\b', r'\besta\s+escala\b', r'\ben\s+una\s+escala\b',
    r'\bescalas?\s+(?:vertical|de\s+(?:magnitud(?:es)?|colores|la\s+izquierda|la\s+derecha))\b',
    r'\bpaso\s+de\s+la\s+escala\b', r'\bgran\s+escala\b',
    # frente: "frente a" (opposite, versus) and a glacier's or a dune's front
    r'\b[Ff]rente\s+a\b', r'\\emph\{frente\}',
    r'\bfrente\s+(?:de\s+(?:este|un)\s+glaciar|del\s+glaciar|de\s+(?:19|20)\d\d|(?:había\s+)?retroced\w*|redondeado|en\s+cada|entre\s+19|para\s+llegar|de\s+la\s+altura|estuvo|es\s+hielo)',
    r'\b(?:[Ss]u|[Ee]n\s+su|posiciones\s+del|posición\s+del|debajo\s+del|R\s+y\s+el|hielo\s+del|necesitaría\s+el|llega\s+al)\s+frente\b',
    r'\(c\)\s+El\s+frente\.',
    # plano: the adjective, "en plano", "primer plano"
    r'\ben\s+(?:un\s+)?planos?\b', r'\bmapa\s+plano\b', r'\bprimer\s+plano\b',
    r'\bes\s+plano\b', r'\b(?:y|fondo)\s+plano\b', r'\bplanos\s+horizontales\b',
    r'\bbloque\s+azul\s+plano\b',
    # era: the verb (was), and the industrial era
    r'\bera\s+industrial\b',
    r'\b(?:lo|misión|anual|2019|cambiaba|Armero|autoridades)\s+era\b', r'\bEra\s+también\b',
    # longitud: a length
    r'(?<=\})\s+de\s+longitud\b', r'\blongitud\s+(?:de\s+cuerda|total|\(km\))',
    r'\b(?:algunas|las)\s+longitudes\b', r'\b[Qq]ué\s+longitud\b', r'\bLongitud:',
    # globo: the weather balloon (g8.1), "como un globo" (g7.2)
    r'\bglobos?\s+(?:sonda|aerostático|lleno|se\s+hincha|sube|estall\w*|crece|está\s+en)\b',
    r'\b(?:suelta|hincha|sube)\s+el\s+globo\b', r'\bdebajo\s+del\s+globo\b',
    r'\bglobos\s+y\s+paracaídas\b', r'\bcomo\s+un\s+globo\b', r'\bel\s+globo\s+a\s+\\qty',
    r'\bel\s+globo\s+estall\w*', r'\bque\s+el\s+globo\b',
    # placa: a plate of ice, the plates of algae (g9.4)
    r'\bdiminutas\s+placas\b', r'\bplacas?\s+de\s+hielo\b',
    # canto: "de canto" (on edge)
    r'\b(?:puestas?|ponerse|ponen)\s+de\s+canto\b',
    # falla, magnitud, intensidad in their everyday senses
    r'\b[Qq]ué\s+falla\?', r'\ben\s+magnitud\b', r'\borden(?:es)?\s+de\s+magnitud\b',
    r'\bsu\s+intensidad\s+y\s+su\s+frecuencia\b',
    # estrato: its etymology (g7.2) and the plural inside the layer definition
    r'\\emph\{estrato\}\s+significa', r'en\s+plural,\s+\\emph\{estratos\}',
    # proper names: the invented Colinas de Varden (a region, not the
    # landform definition), the mar Caspio (a lake), the city of Río de Janeiro
    r'\bColinas\s+de\s+Varden\b', r'\bmar\s+Caspio\b', r'\bRío\s+de\s+Janeiro\b',
    # data credits and dataset names: "Costas: Natural Earth", "relieve ETOPO1";
    # hydrothermal "manantiales calientes" (not the spring definition)
    r'\bCostas(?::|\s+de)\s+Natural\s+Earth\b', r'\brelieve\s+ETOPO1\b',
    r'\bmanantiales?\s+calientes?\b',
    # run-in paragraph headings, page references, inline TikZ (as English)
    r'\\paragraph\{[^{}]*\}', r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
]

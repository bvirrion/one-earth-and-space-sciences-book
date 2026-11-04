"""Book 3 (University, Year 1) -- es. Curation only; the rules live in tools/termlink/.

Curated by the Book 3 `es` agent from this edition's own harvest (488 linkable
terms), with a context read of every Spanish word that is also an ordinary word
(census of the linked texts against English, 2026-10-27). University:
AMBIG_POLICY = "drop", as book3_en.py.

Spanish harvests a defined term under its qualifier-stripped text: "altura (de
un astro)" links the bare word altura, "dirección (de una recta)" the bare word
dirección. So a STOP entry must name the FULL harvested key, and a homograph
that is wrong in some sentences is protected by pattern (EXTRA_PROTECT), with
each protected sense listed here.

STOP (the whole term is wrong wherever it occurs):
  ambiente de depósito   facies key: the depositional environment is not facies
  correlación            log key: the biostratigraphic and sectional correlation
                         of Book 3 ch. 24 is not the log correlation of ch. 5
  correlación (de registros)   the same word, same key
  grupo (litoestratigráfico)   ch. 24: the working group, and nanofossil groups

EXTRA_PROTECT (a sense the term does not carry, the rest still links):
  longitud de onda, longitud de desintegración, longitud de placa ...:
                         length, not the geographic longitude; "latitud y
                         longitud" and any longitud followed by an angle, a
                         lambda, phi or hemisphere within the sentence still link
  estable / estables     ordinary "steady", not the stable triple junction;
                         "estratificación estable" and "unión triple estable"
                         still link
  dirección              ordinary "direction", not the trend; trend stays before
                         an angle, a $t$, "media" or "opuesta"; dirección de
                         buzamiento keeps its own link
  declinación            magnetic declination (Book 3 ch. 6 and ch. 1), not the
                         celestial declination
  miembros con voto, miembros sin votar   ch. 24: the voting members
  grupo de trabajo, grupo propuso, grupo de nanofósiles   ch. 24: working
                         groups and nanofossil groups, not lithostratigraphic groups

EXTRA (accent-less plurals the linker cannot match: its morphology keeps the
accent of the singular, rotación -> rotaciones loses it):
  anticiclones, estratificaciones cruzadas, inmersiones, rotaciones finitas,
  soluciones sólidas, uniones triples, exageraciones verticales, radiaciones
  netas, clasificaciones
"""

AMBIG_POLICY = "drop"

STOP = {
    # global homographs: the bare word of a qualified key ("flujo (de una
    # fuente)" links the word flujo wherever it occurs; "altura (de un astro)",
    # "orden (de un color de interferencia)", "relieve (óptico)" likewise). A
    # defined sense that lives in one chapter survives this (it is local) and
    # is kept on purpose; the generic occurrences elsewhere are not linked.
    "estable", "Estable", "inestable",
    "flujo", "flujos", "Flujo",
    "orden", "Orden",
    "extensión", "Extensión",
    "relieve", "Relieve",
    "grupo", "grupos", "sistema", "sistemas", "serie", "series",
    "formación", "formaciones", "miembro", "miembros", "etapa", "etapas",
    "altura", "dirección", "tendencia",
    "ambiente de depósito",
    "correlación", "Correlación", "correlación (de registros)",
    "grupo (litoestratigráfico)",
}

NO_CAPITAL = set()

EXTRA = {
    "anticiclones": "def:b1:atmospheric-circulation:cyclone",
    "estratificaciones cruzadas": "def:b1:clastic-sediments:cross-bedding",
    "inmersiones": "def:b1:field-lab-methods-1:trend-plunge",
    "rotaciones finitas": "def:b1:plate-kinematics:finite-rotation",
    "soluciones sólidas": "def:b1:rock-forming-minerals:solid-solution",
    "uniones triples": "def:b1:plate-kinematics:triple-junction",
    "exageraciones verticales": "def:b1:cross-sections:section",
    "radiaciones netas": "def:b1:radiation-heat-transport:net-radiation",
    "clasificaciones": "def:b1:clastic-sediments:sorting",
}

EXTRA_PROTECT = [
    # length, not longitude (Book 3 ch. 2, 8, 12, 14, 16, 17, 18, 23)
    r'longitud(?:es)?\s+de\s+onda',
    r'longitud(?:es)?\s+de\s+desintegraci[oó]n',
    r'(?<!latitud y )(?<!latitudes y )(?<!latitud, )(?<!latitudes, )'
    r'longitud(?:es)?(?![^.\n]{0,40}?(?:latitud|\\ang|\\lambda|\\varphi|\\degree|hemisferio|meridian))',
    # ordinary "steady", not the stable triple junction
    r'(?<!triple )(?<!estratificación )\bestables?\b',
    # ordinary "direction", not the trend of a line
    r'dirección(?!\s+(?:\\ang|\$|media\b|opuesta|de\s+buzamiento))',
    # magnetic declination (Book 3 ch. 1 and ch. 6), not celestial declination
    r'declinaci[oó]n(?=\s+magn[ée]tica)',
    r'(?<=sin ajuste de )declinaci[oó]n',
    r'(?<=ajustada para la )declinaci[oó]n',
    r'(?<=ajustar la )declinaci[oó]n',
    r'(?<=ajuste de )declinaci[oó]n',
    r'(?<=corrección de la )declinaci[oó]n',
    r'(?<=mientras la )declinaci[oó]n',
    r'declinaci[oó]n(?=\s+mientras)',
    # ch. 24: the voting members of the ICS
    r'grupos?(?=\s+(?:de\s+(?:trabajo|nanofósiles)|propuso))',
    r'miembros?(?=\s+(?:con\s+voto|sin\s+votar))',
]
DROP = set()

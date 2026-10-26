"""Book 2 (High School, grades 10-12) -- es. Curation only; the rules live in tools/termlink/.

STUB (coordinator, 2026-10-25). The Book 2 `es` agent curates this file from
THIS edition's own harvest, with the frequency and chapter-set censuses against
the English twin (translation_instruction.md). `book1_es.py` holds the
language-level homograph knowledge of Book 1 (temps/tiempo, plaque, echelle,
...): re-verify every entry against Book 2's own harvest before copying it --
its EXTRA values are Book 1 labels and would dangle here, and its protects are
another book's judgement. `book2_en.py` lists the English homographs of this
book (eye, flux, flattening, saturated, stable, trap, volcanic, root,
intermediate, deep ocean, forcing/feedback/scenario short forms).

Curated 2026-10-25 by the Book 2 es agent, from this edition's own harvest,
the per-target frequency and chapter-set censuses against English, and a
context read of every flagged target. Spanish homographs met here, each
checked against its target:
  rayo       lightning / a seismic ray (g11.02: 27 links), cosmic rays (g12.05)
  flujo      a flux of water (g10.09) / heat flow, the mantle flow, the net
             flow of energy (g11.03, g11.05, g12.06, g12.10)
  reserva    a stock of water / a naval reserve (g11.01), a heat reserve (g12.07)
  estable    stable air / stable minerals, isotopes, cratons (as English)
  saturado   saturated air / used again in g10.05 (English stops it too)
  estratificación, estratificado  the layered ocean / rock bedding (g12.03),
             a layered stromatolite (g12.08)
  afloramiento  oceanic upwelling / a rock OUTCROP (g12.05) -- one Spanish word
  brillo     a mineral's lustre / the Sun's brightness (g12.03, g12.10)
  volcánica  the rock term / the adjective (zona volcánica, islas volcánicas)
  raíz       a mountain root / the square and fourth roots of mathematics
  fractura   a mineral's fracture / rock fractures (g11.08)
  intermedia(s)  the rock composition / intermediate samples, an emission
             scenario (as English)
  ojo        a cyclone's eye / "a simple vista" is used, but stopped as English
"""

# outside its defining chapter each of these is an ordinary word (see above)
STOP = {"rayo", "rayos", "Rayos", "flujo", "flujos", "reserva", "reservas",
        "estable", "Estable", "inestable", "saturado", "saturación",
        "estratificación", "estratificado", "afloramiento", "brillo",
        "volcánica", "ojo"}
NO_CAPITAL = set()
EXTRA = {
    # feminine forms of the composition adjectives (rocas máficas, una roca
    # félsica), which the shared morphology does not derive
    "máfica": "def:g11:igneous-rocks:felsic-mafic",
    "máficas": "def:g11:igneous-rocks:felsic-mafic",
    "félsica": "def:g11:igneous-rocks:felsic-mafic",
    "félsicas": "def:g11:igneous-rocks:felsic-mafic",
    "intermedia": "def:g11:igneous-rocks:felsic-mafic",
    "intermedias": "def:g11:igneous-rocks:felsic-mafic",
    # the plural keeps the singular adjective: formaciones de hierro bandeado
    "formaciones de hierro bandeado": "def:g12:early-earth:bif",
    "Formaciones de hierro bandeado": "def:g12:early-earth:bif",
    # g12 climate-change: the chapter uses the short forms of its terms (as
    # English does)
    "forzamiento": "def:g12:climate-change:forcing",
    "forzamientos": "def:g12:climate-change:forcing",
    "retroalimentación": "def:g12:climate-change:feedback",
    "retroalimentaciones": "def:g12:climate-change:feedback",
    "escenario": "def:g12:climate-change:scenario",
    "escenarios": "def:g12:climate-change:scenario",
    "sensibilidad climática": "def:g12:climate-change:ecs",
    # plurals of the two-word and the stem-changing intrusion names, which
    # the shared morphology does not derive (English links "sills", "plutons")
    "filones capa": "def:g11:igneous-rocks:intrusion",
    "plutones": "def:g11:igneous-rocks:intrusion",
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
    # raíz: the mathematical roots, not a mountain root
    r'\braíz\s+(?:cuadrada|cuarta|cúbica)\b',
    # fractura: the fractures of a rock (g11.08), not a mineral's fracture
    r'\bpor\s+las\s+fracturas\b',
    # intermedias: two intermediate samples (g12.07), an emission scenario
    # (g12.10 table), not the rock composition
    r'\bmuestras\s+intermedias\b', r'&\s*intermedias\s*&',
    # proper names: the Last Interglacial (an AR6 reference period)
    r'\bÚltimo\s+Interglacial\b',
]

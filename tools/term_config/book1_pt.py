"""Book 1 (Primary and Middle School, grades 1-9) -- pt. Curation only; the rules live in tools/termlink/.

Curated 2026-10-25 by the Book 1 `pt` agent from this edition's own harvest
(`link_defined_terms.py --book 1 --lang pt --terms`) and the frequency and
chapter-set censuses against English (translation_instruction.md). Brazilian
Portuguese homographs met in this book, each against its target:

- tempo: the weather (g1) and time ("muito tempo", "ao mesmo tempo", "a tempo",
  "quanto tempo", "o eixo do tempo"); time is protected phrase by phrase, so
  that "o tempo que faz", "mapa do tempo", "tempo firme" keep their link.
- era: the geological era (g7.5) and the imperfect of "ser" ("Armero era",
  "a sua média anual era") -- STOP, so it links in its defining chapter only.
- planta: the floor plan (g2.2) and a plant -- STOP (English STOPs "plan").
- escala: the drawing scale (g2.2) and "em escala", "fora de escala", "a
  escala do tempo", "na escala de uma vida", logarithmic and vertical scales.
- seca: drought (g5.3), the adjective "seca" (dry) and the verb "seca" (dries)
  -- STOP.
- depressão: the weather depression (g8.3) and a hollow in the ground (a trench,
  a sinkhole, the Challenger Deep) -- STOP.
- intensidade, molde, contramolde: as English (intensity, cast, mould).
- frente: a weather front and "à frente", "para a frente", "de frente".
- fonte: a spring (g6.5) and a lava fountain, a heat source, hot springs.
- lama: mud (g3 sand definition) inside "fluxo de lama" (mudflow, one word in
  English, never linked there).
- vale: a valley and the verb "vale" (is worth: "vale a pena", "vale 9.8").
- placa: English links the short form "plate"; the same EXTRA here, with the
  thin plates of slate, glass, ice and algae protected.
- manto: the mantle, not the ice sheets ("dois enormes mantos").
- estrato: stratus (g4.1) and stratum (g7.4); "estrato quer dizer camada" in
  g7.2 is an etymology, not either term.
- Piro: harvested from the etymology "Piro quer dizer fogo" (g7.2) -- DROP.

Irregular plurals the tail "(?:e?s)?" cannot make (-m -> -ns, -ao -> -oes,
-al -> -ais, -il -> -eis, -vel -> -veis) are listed in DERIVED.
"""

STOP = {
    "era", "Era",
    "planta", "Planta",
    "seca", "Seca",
    "depressão", "Depressão", "depressão (meteorologia)",
    "intensidade", "Intensidade",
    "molde", "contramolde",
}
NO_CAPITAL = set()
EXTRA = {
    # coordinator, 2026-10-25: g6 defines the full name; the text uses the short
    # form (English now links "date line" by EXTRA too)
    "linha de data": "def:g6:latitude-longitude:date-line",
    # g7 defines "placa tectônica (ou simplesmente placa)": the short form is
    # the one the later chapters use, as in English
    "placa": "def:g7:plate-tectonics:plate",
    "placas": "def:g7:plate-tectonics:plate",
    # the seismic sense of "intensidade" is reached through the scale only
    "escala de intensidade": "def:g7:earthquakes:intensity",
    # "seca" is STOPped (dry, dries); the drought English links in g6.5
    "longa seca": "def:g5:natural-hazards:drought",
}
DROP = {"Piro"}
DERIVED = {
    "nuvem": ["nuvens"],
    "paisagem": ["paisagens"],
    "imagem de satélite": ["imagens de satélite"],
    "fóssil": ["fósseis"],
    "icnofóssil": ["icnofósseis"],
    "permeável": ["permeáveis"],
    "impermeável": ["impermeáveis"],
    "erupção": ["erupções"],
    "erupção efusiva": ["erupções efusivas"],
    "erupção explosiva": ["erupções explosivas"],
    "inundação": ["inundações"],
    "vulcão": ["vulcões"],
    "precipitação": ["precipitações"],
    "glaciação": ["glaciações"],
    "projeção cartográfica": ["projeções cartográficas"],
    "projeção equivalente": ["projeções equivalentes"],
    "previsão do tempo": ["previsões do tempo"],
    "estação meteorológica": ["estações meteorológicas"],
    "mineral": ["minerais"],
    "litoral": ["litorais"],
    "pontal": ["pontais"],
    "ameaça natural": ["ameaças naturais"],
    "desastre natural": ["desastres naturais"],
    "elemento natural": ["elementos naturais"],
    "dorsal oceânica": ["dorsais oceânicas"],
    "planície abissal": ["planícies abissais"],
    "plataforma continental": ["plataformas continentais"],
    "mapa-múndi": ["mapas-múndi"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"

# The list is ONE alternation scanned left to right: a pattern that starts
# earlier eats the text a later one needed ("própria escala" hid "escala do
# tempo"), so overlapping phrases are written as one pattern.
EXTRA_PROTECT = [
    # tempo: time, not weather
    r'\b(?:[Mm]uito|[Pp]ouco|mesmo|[Qq]uanto|tanto|mais|longo)\s+(?:de\s+)?tempo\b',
    r'\b(?:por|obter|de)\s+um\s+tempo\b',
    r'\b[Cc]om\s+(?:o|muito)\s+tempo\b', r'\ba\s+tempo\b',
    r'\btempo\s+suficiente\b', r'\bt[eê]m\s+(?:muito\s+)?tempo\b',
    r'\b(?:dá|falta)\s+tempo\b',
    r'\b(?:eixo|abismo|intervalos?|erro|função|partir)\s+d[eo]\s+tempo\b',
    r'\bao\s+longo\s+do\s+tempo\b', r'\bavança\s+no\s+tempo\b',
    r'\bno\s+tempo\s+de\s+uma\s+vida\b', r'\bpor\s+algum\s+tempo\b',
    r'\b[Tt]empos\b',
    r'\btempo\s+(?:corre|sai|todo|das\s+ondas|da\s+lavra)\b',
    r'\b[Oo]\s+tempo\s+que\s+(?:o\s+eco|um\s+sinal|uma\s+mina)\b',
    r'\b(?:mede|esse)\s+esse\s+tempo\b', r'\bmede\s+esse\s+tempo\b',
    r'\besse\s+tempo\s+importa\b',
    # escala: to scale, other scales
    r'\b(?:em|fora\s+de)\s+escala\b',
    r'\bescalas?\s+(?:da\s+(?:esquerda|direita|caixa|Terra|cidade|vida)|de\s+(?:uma\s+vida|tempo)|vertical)\b',
    r'\bescala\s+do\s+tempo\b(?!\s+geológico)',
    r'\bmesmas?\s+escalas?\b', r'\bgrande\s+escala\b',
    r'\bpasso\s+da\s+escala\b', r'\bnossa\s+escala(?:\s+d[eo]\s+tempo)?\b',
    r'\bnuma\s+escala\s+em\s+que\b', r'\bpr[óo]pria\s+escala(?:\s+d[eo]\s+tempo(?!\s+geológico))?\b',
    r'\bnessa\s+escala\b', r'\b[Aa]\s+escala\s+de\s+(?:intensidade|magnitude)\b',
    # frente: the adverbial phrases
    r'\b(?:à|de|para\s+a)\s+frente\b', r'\bà\s+sua\s+frente\b',
    # fonte: fountains of lava, a heat source, hot springs
    r'\bfontes?\s+(?:de\s+(?:gotas|lava|Lava|calor|referência|dados)|termais)\b',
    r'\bem\s+fontes\b',
    # lama: mudflows
    r'\bfluxos?\s+de\s+lama\b',
    # vale: the verb
    r'\bvale\s+(?:a\s+pena|\d)', r'\bvalem\s+a\s+pena\b',
    # ("cada mês vale cerca de", "um quadrado vale 20 km", "só vale para",
    # "não vale lá no fundo"); a lookahead, never consuming the $ of "vale $4540"
    r'\bvalem?(?=\s+(?:\$|\\qty|\\num|cerca|para|dez|lá\s+no\s+fundo))',
    # the country, not the line
    r'\bEquador\b',
    # an etymology (g7.2)
    r'\\emph\{estrato\}',
    # lava: the verb ("a chuva lava o solo", g5.1)
    r'\blava\s+o\s+solo\b',
    # manto: the two ice sheets (g8.5)
    r'\benormes\s+mantos\b',
    # relevo: the name of a dataset
    r'\brelevo\s+(?:NOAA\s+)?ETOPO1\b',
    # placa: thin plates that are not tectonic
    r'\bplacas?\s+(?:finas|planas|de\s+(?:vidro|gelo|algas))\b',
    r'\bminúsculas\s+placas\b', r'\bem\s+placas\b',
    # institutions and place names
    r'\bNational\s+Weather\s+Service\b', r'\bWhite\s+Sands\b',
    r'\bBig\s+Spring\b', r'\bCoast\s+Guard\b', r'\bVolcano\s+Observatory\b',
    r'\bRio\s+de\s+Janeiro\b',
    # data credits in captions: English leaves "coastlines from Natural Earth" unlinked
    r'\b[Ll]itora(?:l|is)\s+(?:d[eo]\s+)?Natural\s+Earth\b',
    r'\bColinas\s+de\s+Varden\b', r'\bSea\s+Ice\s+Index\b',
    r'\bPainel\s+Intergovernamental\s+sobre\s+Mudanças\s+Climáticas\b',
    # risco: the everyday phrase; era industrial
    r'\bem\s+risco\b', r'\bera\s+industrial\b',
    # the bold Part headings of a weekend problem: the shared rule matches the
    # English word "Part" only
    r'\\textbf\{Parte\s+[IVX]+\b(?:[^{}]|\{[^{}]*\})*\}',
    # run-in paragraph headings stay unlinked, like section titles
    r'\\paragraph\{[^{}]*\}',
    # as English: \pageref labels and inline \tikz commands
    r'\\pageref\{[^{}]*\}', r'\\tikz\b[^;$]*;',
    # núcleo: an ice core
    r'\btestemunhos?\s+de\s+gelo\b',
]

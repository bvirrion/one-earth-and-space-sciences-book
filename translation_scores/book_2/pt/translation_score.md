# Translation score — Earth and Space Sciences Book 2 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 2 (High School, grades 10–12) |
| **Language** | Brazilian Portuguese (`pt`), one variety throughout |
| **Quality bar** | native Brazilian *ensino médio* Earth science, as a Brazilian textbook writes it: a high-school register that carries the reasoning, the mathematics and the dated assessments. English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Register reference measured before drafting** | the shipped Book 1 `pt` edition of this series and the Brazilian Portuguese physics, biology and chemistry editions: imperative *você* exercise stems (*Encontre, Calcule, Explique, Mostre, Dê, Leia*), decimal point kept in numbers, ``…'' quotes |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-25 |
| **Scope** | 28 chapters + 28 solution files = **56 files**, written directly in Portuguese through `tools/id_apply.py` (no machine draft); `tools/term_config/book2_pt.py` curated from this edition's own harvest; `frontmatter/image-credits-book2.pt.tex` (59 items); ASCII sort keys on accented index entries; per-figure label checks |

## Verdict in one line

A Brazilian high-school Earth and space science course that reads as written
in Portuguese, on a forced build at
**0 errors / 0 undefined / 0 overfull / 0 missing characters / 0 invalid-in-math**,
nullfont at the English baseline (3,291), **373 pages**, **56/56** translated
files in the `.fls`, and green `check_translation.sh` for grades 10, 11 and 12.

## Conventions (the Book 1 `pt` conventions, kept)

* Decimal point kept (the series rule); *bilhões*, *milhões de anos*; *há
  4567 milhões de anos*; 24-hour times; *século~XXI*.
* *gás carbônico*, *vapor de água*; *testemunho de gelo*, *manto de gelo*,
  *glaciação* for an ice age.
* IPCC likelihood and confidence language in the Brazilian IPCC wording:
  *virtualmente certo, extremamente provável, muito provável, provável, tão
  provável quanto não, improvável, muito improvável*; *alta confiança, média
  confiança, muito alta confiança*.
* Cross-references *Livro 1, 7º ano*; *os livros de física / química /
  biologia*; solution heads `\section*{Capítulo \ref{…} --- …}`; *Problema de
  fim de semana --- …*; `\textbf{Parte I --- …}`.
* Credits *e colaboradores*, *(domínio público)*, *Ilustração gerada por IA.*
* The English acronyms of the paleoclimate intervals (PETM, EECO, MPWP, LIG,
  LGM, MH) are kept, as Brazilian literature keeps them; the caption says
  *Siglas em inglês*.
* *limite manto--núcleo* everywhere (one display for the core–mantle
  boundary, unified across g11.02 and g12.06).

## Dimension scores

| Dimension | Score | Notes |
|-----------|------:|-------|
| Structural fidelity | **99** | Counted over the 56 files against their twins: 420 `exercise`, 28 `problem`, 448 `solution`, 205 `omfigure`, 141 `tikzpicture`, 104 `axis`, 658 `\node`, 100 `\includegraphics`, 764 `\label`, 752 `\item`, 141 `definition`, 28 `recall`, 34 `method`, 43 `example`, 12 `history`, 1 `inthefield`, 1 `inthelab`, 2 `safety`, 5 `dated`, 219 `\index`, 371 `\emph`, 74 `\foreach`, 561 `% ledger:`, 38 `\text{}`, 3,686 `\qty`, 132 `\cref`, 24 `tabular` — all exact |
| Terminology | **96** | Brazilian geoscience usage: *intemperismo, denudação, isostasia, raiz (de montanha), dobra / anticlinal / sinclinal, cavalgamento, nappe, ofiolito, xisto azul, eclogito, mineral índice, auréola de contato, clivagem / fratura, brilho, rocha félsica / máfica / intermediária, porfirítica, fenocristal, rocha geradora / reservatório / selante, armadilha, janela de geração, onda frontal, zona de sombra, limite manto--núcleo, fluxo de calor, sistema fechado, isócrona, idade da Terra, desgaseificação, paradoxo do Sol jovem fraco, estromatólito, formação ferrífera bandada, Grande Evento de Oxidação, camadas vermelhas, indicador indireto, arquivo climático, período glacial / interglacial, Último Máximo Glacial, forçamento radiativo, retroalimentação climática, sensibilidade climática de equilíbrio, atribuição, cenário de emissões*. 219 index keys in Portuguese, the same 219 entries as English |
| Register / tone | **96** | High-school *você* imperatives (*Calcule, Encontre, Explique, Mostre, Dê*); chapter openings as Brazilian narrative prose; boxes *O que você já sabe, No campo, No laboratório, História, Dados de, Segurança* |
| Fluency | **95** | Drafted sentence by sentence in Portuguese; reworded only for meaning or to fit a table, never to satisfy a gate |
| Accuracy | **97** | Numeric census of every file against its twin: four differences, all explained (*terceiro ano* for "Year~3", *século~XXI* for "21st century", *oxigênio-18* in a table cell English writes "oxygen isotopes", and a census artefact from `\%`). Every solution of grade 12 chapters 7–10 recomputed along the rounded path |
| Term links | **95** | **2,249 links to 137 targets** against English's 2,208 / 135 (the coordinator's final English layer: `slab pulls` protected, *cleavage* and *pull of the sinking slab* EXTRAs) — every English target reached; the two extra targets are the defined sense (*Anomalias magnéticas*, g11.01 caption, 1; *migração* of oil and gas, g11.09, 4). *clivagem / fratura* 25 against English 24: the one-link surplus is *fratura conchoidal* in g11.08, the fracture half of the same definition. Curated homographs: *olho, fluxo, saturado, estável, vulcânica* (STOP, as English), *raio* (lightning vs radius, STOP), *dique* (dyke vs levee), *raiz* (root of a mountain, of a number, of a plant), *dobra* (the verb), *brilho, intermediário, fratura, oceano profundo*, the *Último Interglacial* and the *Colinas de Varden*; irregular plurals and feminines through `DERIVED`. Dry run: `links to insert: 0` |
| Figures | **95** | 20 `!draw` ranges (below), each a `\foreach` label list, a symbolic tick list or a `yticklabels`/`xticklabels` list; the coordinator's drawing census shows four differences only, all English words inside English node text (*circle*, *arc*). Figure pages rendered at 130 dpi and a word-overlap scan (`pdftotext -bbox`) over all 373 pages: every translated label that grew by a quarter or more over its English twin (50 nodes) was located and its page re-rendered, and every collision with a curve, a frame or a neighbouring label was fixed (15 figures): the thunderstorm legend, the Potomac base-flow label, the mixed-layer and upwelling labels, the asthenosphere column labels, the petroleum-system and passive-margin labels, the suture/mountain-belt pair, the foliation arrows, the two isochron slope labels, the faint-young-Sun luminosity label, the banded-iron labels, the Sunda Shelf and the 30 000-year carbon-dioxide label (reworded, or broken with `\shortstack` inside the node text so the drawing code is untouched) |

## `!draw` ranges

| File | Range (English line) | What |
|---|---|---|
| g10/02 | 133-134 | symbolic x coords (planet names) |
| g10/02 | 299 | `\foreach` planet/distance list |
| g10/03 | 226-229 | `\foreach` albedo surface list |
| g10/05 | 58 | `\foreach` storm-stage titles |
| g10/08 | 329-330 | date xticklabels, axis labels |
| g10/09 | 188-191 | reservoir and residence-time tick labels |
| g11/06 | 216-217 | plate-name xticklabels |
| g11/07 | 634 | mineral yticklabels |
| g11/08 | 153 | `\foreach` rock-name list |
| g11/08 | 162-169 | `\foreach` mineral list (Bowen chart) |
| g11/09 | 542 | coal-rank yticklabels |
| g12/01 | 117 | crust yticklabels |
| g12/01 | 122 | symbolic point meta *uns 70* |
| g12/05 | 85-87 | denudation-rate yticklabels |
| g12/05 | 272 | `\foreach` isostasy panel titles |
| g12/06 | 170 | *fontes / perdas* yticklabels |
| g12/06 | 287 | `\foreach` *fossa* labels |
| g12/09 | 270 | `\textdegree L` in an xticklabel |
| g12/10 | 200-202 | forcing yticklabels |
| g12/10 | 396-397 | attribution yticklabels |

## Censuses

* `\text{}` census over course **and** solutions: 38 / 38, all Portuguese or units.
* Frequency and chapter-set census: surviving differences are the defined sense — *umidade / saturada* in g10.04 (73 vs 60), *estoque / fluxo* (39 vs 35), *maré de tempestade* (6 vs 3), *hidrotermal* (4 vs 2), *idade da Terra* (10 vs 8), *onda frontal* (26 vs 23); a few below English where Portuguese varies the phrasing (*fluxo de calor* 22 vs 24, *plutônica* in g12.04 6 vs 8, *reservatório* 20 vs 22), and *laje* (slab) in g11.09, 0 vs 2, where English mislinks a slab of shale.
* Display-drift census (`check_term_display_drift.py`): 59 targets with several displays, all inflection or the multi-term definitions English also has; the one real drift (*limite núcleo--manto* / *limite manto--núcleo*) was unified.
* Line-edge sweeps (quote, punctuation, hyphen at line edges): 0 outside TikZ `.. controls` continuations, which are identical in English.

## Why not 100

* Twenty `!draw` ranges: each justified, but each is a figure the census no longer guards.
* Five tables and two bar charts were reworded to fit the line (e.g. *cordilheiras (média)* for "mountain belts (average)", *temperatura do fundo* for "deep-water temperature"): the meaning is kept, the wording is tighter than the prose. Fifteen figure labels were likewise shortened or broken onto two lines (*reservatório* for *rocha reservatório*, *força* for *empurrão*, *ondas P* for "P speed").
* *raiz*, *dique*, *dobra* and *brilho* are protected phrase by phrase; a new phrase added later in the other sense would link.

## Coordinator amendments

- 2026-10-26: g11 solutions/08 answer 16 rewritten by the coordinator after an English canon fix (reported by hi): ≈ 950 days, 2.6 years, within the intrusion range, not "between the two". Gates for grade 11 re-run, green; linker dry run 0.
- 2026-10-26: g11/01 "Motonari" → "Motonori" Matuyama, and the g12/02 fold-shortening chart labels (Varden label no longer clipped, 13 % label moved below-right of its point), both English-canon fixes after the Arabic report; mirrored by the coordinator.

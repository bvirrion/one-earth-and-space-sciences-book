# Translation score — Earth and Space Sciences Book 1 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 1 (Primary and Middle School, grades 1–9) |
| **Language** | Brazilian Portuguese (`pt`), one variety throughout |
| **Quality bar** | native Brazilian *ensino fundamental* Earth science, as a Brazilian textbook writes it — a young child's register in grades 1–5, a middle-school register in grades 6–9. English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Register reference measured before drafting** | the shipped Brazilian Portuguese biology and chemistry editions (`../one-biology-book/parts/*/pt/`, `../one-chemistry-book/parts/*/pt/`): imperative *você* exercise stems (*Encontre, Escreva, Dê, Leia, Calcule, Diga, Observe*), decimal point kept in numbers, ``…'' quotes |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-25 |
| **Scope** | 32 chapters + 32 solution files = **64 files**, written directly in Portuguese through `tools/id_apply.py` (no machine draft); `tools/term_config/book1_pt.py` curated from this edition's own harvest; the preface and image-credits pages; the Aside block of `styles/lang/pt.tex` checked; ASCII sort keys on accented index entries; per-figure label checks |

## Verdict in one line

A Brazilian Earth and space science course from first grade to the ninth
year that reads as written in Portuguese, on a forced build at
**0 errors / 0 undefined / 0 overfull / 0 missing characters / 0 invalid-in-math**,
nullfont at the English baseline (6,633), **336 pages** (English 324),
**64/64** translated files in the `.fls`, and green `check_translation.sh`
for all nine years.

## Conventions

* Compass **N L S O** (*norte, leste, sul, oeste*) in prose, figures and
  coordinates (*\ang{14.4} Leste*, *$140^\circ$\,L*); hemispheres *hemisfério
  norte / hemisfério sul*, place names *Polo Norte / Polo Sul*.
* Decimal point kept (the series rule); 24-hour times (*17~h*); dates
  *13~de~novembro*; centuries *século~XIX*; decades *anos 1880*.
* *gás carbônico*, *vapor de água* (one form, 17 uses); IPCC likelihood
  language in the Brazilian IPCC wording (*virtualmente certo, extremamente
  provável, muito provável, provável, tão provável quanto não, improvável,
  inequívoco, alta confiança*).

## Dimension scores

| Dimension | Score | Notes |
|-----------|------:|-------|
| Structural fidelity | **99** | Counted over the 64 files against their twins: 370 `exercise`, 20 `problem`, 390 `solution`, 234 `omfigure`, 161 `tikzpicture`, 73 `axis`, 677 `\node`, 120 `\includegraphics`, 816 `\label` (set diff 0), 468 `\item`, 140 `definition`, 30 `recall`, 42 `method`, 60 `example`, 10 `history`, 7 `inthefield`, 7 `safety`, 2 `dated`, 237 `\index` (per-file equal), 455 `\emph`, 150 `\foreach`, 588 `% ledger:` (on their lines), 14 `\text{}` — all exact. `\qty` 836 vs 834: one idiom (*de \qty{4}{hPa} em \qty{4}{hPa}* for *every 4 hPa*). `\cref` 105 vs 103: two `\Cref` at sentence start rendered *O \cref{…}* |
| Terminology | **96** | Brazilian school usage: *intemperismo, erosão, deposição, nascente / foz / afluente, planície de inundação, lençol freático, aquífero, poço, rocha ígnea / sedimentar / metamórfica, ciclo das rochas, dureza (escala de Mohs), tectônica de placas, limite divergente / convergente / transformante, dorsal oceânica, fossa oceânica, ponto quente, câmara magmática, fluxo piroclástico, foco / epicentro, sismômetro / sismograma, discordância, datação relativa, princípio da superposição, escala do tempo geológico, massa de ar, frente fria / quente, isóbara, depressão / anticiclone, alísios, giro, manto de gelo, plataforma de gelo, gelo marinho, testemunho de gelo, efeito estufa, ameaça / vulnerabilidade / risco, jazida, teor, minério, reserva, carste, dolina, falésia, deriva litorânea, pontal, curva de nível, equidistância, projeção de Mercator, sensoriamento remoto*. All 237 index keys in Portuguese; accented keys carry ASCII sort keys |
| Register / tone | **96** | Child-directed *você* imperatives and short sentences in grades 1–5 (*Observe, Desenhe, Diga, Ligue*); the same stems with longer reasoning in grades 6–9 (*Encontre* 15, *Escreva* 9, *Dê* 9, *Leia* 8, *Calcule* 8 as item openers). Problems: *Problema de fim de semana --- …*, *Parte I --- …*; boxes *O que você já sabe, No campo, No laboratório, História, Dados de, Segurança* |
| Fluency | **95** | Drafted sentence by sentence in Portuguese; reworded only for meaning, never to satisfy a gate. Chapter openings read as Brazilian narrative prose (checked all 32); every definition re-read |
| Accuracy | **97** | Numeric census of every file against its twin: the only differences are 24-hour times, *século~XIX*, inline label tables replacing figdata label files, and the *de 4 em 4 hPa* idiom; the six coordinator canon fixes of 2026-10-25 (Steno, Hutton caption, 26 de março, 1350 km, −86 °C, 1200 m) and the `\textbf{20 anos}` math-span fix mirrored |
| Term links | **95** | **6,060 links to 137 targets** against English's 6,102 / 136 — every English target reached; the extra target is *escala do tempo geológico* (1 link, g7.5, the defined term). Curated Brazilian homographs: *tempo* (weather vs time, 22 time phrases protected), *escala* (to scale, other scales), *planta* (plan vs plant), *era* (the verb), *seca* (adjective, verb), *depressão* (a hollow), *frente* (*à frente*), *fonte* (lava fountain, heat source), *lama* (*fluxo de lama*), *vale* (the verb *valer*), *placa* (EXTRA for the short form, thin plates protected), *Rio de Janeiro*, *Equador* the country, *Parte I* headings; irregular plurals (*nuvens, vulcões, erupções, minerais, fósseis, permeáveis…*) via `DERIVED`. Dry run: `links to insert: 0` |
| Figures | **95** | 47 `!draw` ranges (listed in the run report), each a `\foreach` list, a symbolic tick list or an inline label table replacing an English-only figdata label file; label overlaps found by eye and fixed in grades 1, 6, 7, 8 and 9; the coordinator's drawing census shows one difference only (an en dash in the *2020--25* tick label) |

## Censuses

* `\text{}` census over course **and** solutions: 14 / 14, all Portuguese or units.
* Chapter-set census: surviving flags are the defined sense — *altitude* (113 vs 68: pt says *altitude* where English says *height* or *elevation*, and *nível do mar* is part of the altitude definition), *jazida* (20 vs 10, the defined word where English varies), *relevo* in g8.5 (2), and single extra-chapter links to *continente, mapa-múndi, precipitação, deposição, intemperismo* that are the defined sense.
* Display-drift census (`check_term_display_drift.py`): 82 targets with several displays, all inflection or the multi-term definitions English also has.
* Line-edge sweeps (quote, punctuation, hyphen at line edges): 0.

## Why not 100

* Forty-seven `!draw` ranges: each justified, but each is a figure the census no longer guards.
* English printed from figdata label files (grade 3, 6, 7, 8, 9) had to be re-entered as inline tables in the Portuguese source; a regeneration of those `.dat` files would not reach this edition.
* *tempo* stays one word for weather and time; the time senses are protected phrase by phrase, so a new time phrase added later would link.

## Coordinator addendum (2026-10-25, after wave 1)

Re-verified by the coordinator after the wave-1 canon fixes and tool changes:
- a forced build: 336 pp, 0 errors / 0 undefined / 0 overfull, nullfont 6,633, `.fls` 64 = 64;
- `check_translation.sh` 9/9 PASSED under the stricter gates (per-range `!draw`, the 12-character dup tier, the whole-word tokenizer);
- relinked with the multilingual Part-heading protect: **6065 links**, 138 targets (English's 137 plus the time-scale definition, which English never links), dry run 0. The date-line EXTRA was added by the coordinator, to match English's new EXTRA (5 links).

The coordinator mirrored the canon fixes listed in `sources/WAVE1_FINDINGS.md` §1 into this edition, among them the problem-6 date (**25** March, which reverts the first fix to 26) and the three rainy afternoons. The score is unchanged.

# Translation score — Earth and Space Sciences Book 3 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 3 (University Year 1, `bachelor-1`) |
| **Language** | French (`fr`) |
| **Quality bar** | **native French university-course prose** (first-year licence level: astronomie de position, photométrie, planétologie comparée, cartes et coupes géologiques, minéralogie, Terre en couches, bilan thermique, isostasie, cinématique des plaques, marges, points chauds, rhéologie, failles et plis, source sismique, altération, érosion, sédiments, diagenèse, échelle stratigraphique, géochronologie, enveloppes fluides, rayonnement, circulations atmosphérique et océanique). English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Sense / register references measured before drafting** | the English canon (content); this series' French Books 1 and 2 (`parts/grade-*/fr/`, their score files, `book1_fr.py`, `book2_fr.py`) for every convention and every term they own; the French physics and chemistry editions for shared vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-26 |
| **Model** | `claude-sonnet-5-5` (Sonnet 5.5): translation agent and coordinator (recorded 2026-10-27) |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 29 chapters + 29 solution twins = **58 files**, every one written through `tools/id_apply.py` line-range patches over the English twin; `frontmatter/image-credits-book3.fr.tex` (frame and descriptions translated, every credit, author, dataset and licence kept exactly); a curated `tools/term_config/book3_fr.py`; the defined-term link layer; two small edits to `tools/check_latin_prose.py`; this score |

## Verdict in one line

A French Book 3 that reads as one French first-year university course in the
sciences of the Earth and of space, continuing Books 1–2 with their conventions
(N/E/S/O, spaced punctuation, guillemets, decimal point, *Ma* in prose) and the
infinitive instruction register, with every structural and prose gate green and
a forced TeX Live 2026 build of **0 errors / 0 undefined / 0 overfull**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 58 files against their 58 twins: **348 `exercise`**, **29 `problem`**, **377 `\begin{solution}`**, **160 `omfigure`**, **144 `tikzpicture`**, **90 `axis`**, **73 `\includegraphics`**, **47 `tabular`**, **587 `\emph`**, **449 `\index`**, **1,010 `\label`**, **1,044 `\item`**, **743 `\node`**, **734 `% ledger:`**, **366 `\ce`**, **5,028 `\qty`**, and per environment **193 `definition`, 127 `proposition`, 136 `proof`, 22 `theorem`, 35 `method`, 17 `example`, 4 `remark`, 29 `recall`, 15 `inthefield`, 10 `inthelab`, 20 `history`, 8 `dated`, 1 `safety`** — all equal to English. `\cref{` is 460 against 450 only because French writes *Le \cref{tab…}* where English opens the sentence with `\Cref{tab…}` (eight files, ten sites; `\Cref`/`\cref` are the same reference) |
| Terminology | **96** | Consistent French university vocabulary shared with Books 1–2: *hauteur, azimut, déclinaison (céleste), angle horaire, ascension droite, point vernal, temps sidéral, équation du temps, grand/petit cercle, triangle sphérique*; *seeing, masse d'air, rendement quantique, rapport signal sur bruit, magnitude, parallaxe*; *planète tellurique, géante gazeuse, géante de glaces, facteur de moment d'inertie*; *attitude, direction, pendage, isohypse structurale, plongement, pitch*; *flux géothermique, géotherme, adiabate du manteau, pesanteur normale, anomalie à l'air libre/de Bouguer, plaque de Bouguer*; *point triple, pôle/vecteur d'Euler, rotation finie, plaque nubienne/eurasienne*; *marge passive, glacis, core complex océanique*; *panneau plongeant, zone de Wadati–Benioff, avant-arc, bassin d'arrière-arc, distance arc–fosse*; *point chaud, panache mantellique, renflement, grande province magmatique, trapps*; *contrainte, déformation, rhéologie, cisaillement pur/simple, critère de Coulomb, loi de Byerlee*; *compartiment supérieur/inférieur (toit/mur), glissement net, stries, miroir de faille, plis droit/couché/incliné/renversé, clivage de plan axial*; *rebond élastique, moment sismique, magnitude de moment, mécanisme au foyer, plan nodal, valeur b*; *hydrolyse, bisiallitisation, potentiel ionique, minéral argileux*; *charge dissoute/en suspension/de fond, paramètre de Shields, diagramme de Hjulström*; *classement, faciès, milieu de dépôt, delta dominé par les marées*; *usine à carbonates, ooïde, plate-forme bordée, rampe, profondeur de compensation des carbonates, lysocline, sabkha*; *loi d'Athy, cimentation, accommodation, eustatisme, niveau marin relatif*; *biozone, première/dernière apparition, GSSP, chronostratigraphie*; *isochrone, désintégration à embranchement, âge radiocarbone, courbe d'étalonnage, température de fermeture*; *parcelle d'air, température potentielle, fréquence de flottabilité, diagramme T–S, masse d'eau*; *insolation journalière moyenne, rayonnement infrarouge sortant, réanalyse, transport méridien de chaleur, rapport de Bowen*; *vent géostrophique, fonction de courant méridienne moyenne, cellules de Hadley/Ferrel, ZCIT, circulation de Walker, courant-jet*; *tension du vent, gyre, transport/spirale d'Ekman, pompage d'Ekman, courant de bord ouest, circulation méridienne de retournement*. All 449 `\index{}` keys in French with ASCII sort keys |
| Register / tone | **96** | University-course voice: course text in the present with impersonal *on*, definitions and propositions in the third person, history narrated in the passé simple; exercise stems open with infinitives (*Calculer, Déterminer, Montrer, Estimer, Comparer*) and nominal openers, **0** *tu*. Physical-science wording only, no policy statements |
| Typography | **97** | Spaced punctuation (`~:` `~;` `~?` `~!`) and guillemets `«~…~»`; decimal point and `\,` thousands as the series' siunitx setting does (as Books 1–2); final sweeps: **0** lines ending on an elision apostrophe (89 sites were found and moved after a first sweep: a newline after *l'*/*d'* prints a space), **0** dangling hyphens, **0** straight quotes |
| Fidelity / accuracy | **95** | Every course paragraph, proof, worked example, exercise and solution translated against its twin; every solution re-read against its question in French and the arithmetic recomputed along the rounded path a student follows (scripts `notes/chk0N.py`). One slip of my own caught and fixed in a solution (a wrong wind-direction item in `solutions/29`). Seven English-canon slips found and reported, not silently fixed (below). Math spans are byte-frozen except the `\text{}` inside them, which is translated |
| Figures | **94** | Every visible label translated (nodes, legends, tick labels, titles, multi-line `\\` labels); `\foreach` lists with visible words translated under per-range `!draw` (list below). Rendered figure pages were inspected one by one at about 100 dpi for all 160 figures except a few caption-less drawings of ch. 3, 8 and 19 (checked in the build, not re-read at 130 dpi); about twenty label collisions found that way were fixed in the node text (ch. 9, 10, 11, 14, 17, 19, 20, 21, 22, 23, 26, 27, 29). Not every figure was re-read at 130 dpi |
| Links | **95** | **4,475 `\omterm` links on 185 targets** (def 4,454, prop 16, thm 5) against English's **4,654 on 184**: every English target is linked (**0 missing**), plus one English never reaches (below). Dry run: **links to insert: 0**; `--check`: every file matches what the config generates |

## Gates

`bash tools/check_translation.sh bachelor-1 fr`: **PASSED** (structural
censuses, duplicate labels, ledger ids, `\ce` freeze and balance, the
twin-comparison prose gate — **no multi-word finding**; the advisory one-word
tier (102 hits in 58 files) was read: cognates and proper names — *horizon,
Mars, Jupiter, Uranus, granite, gabbro, Adams–Williamson, Insolation*, units
such as *arcsec* inside math, the symbolic coordinate keys listed below — and
`chemistry twin gate: OK (58 files)`).
`bash tools/gates.sh bachelor-1`: **rc 0** (`gates OK`).
`tools/check_orphan_lines.py`: **0**.
`tools/check_term_display_drift.py`: every multi-display target is inflection
(singular/plural), or one of several terms a definition introduces; read
against English.
Drawing census (`coord/drawcensus.py fr`, 15 files differ): every difference is
node text, a translated `\foreach` label list under `!draw`, or a label
position moved on purpose after a rendered-page check (anchor or coordinate of
a node): ch. 04, 05, 06, 11, 14, 17, 18, 20, 21, 22, 23, 24, 26, 27, 29. No
drawing path, scale, data table or colour differs.

Build (`scratchpad/build.sh`, forced `-g`, TeX Live 2026 as CI, memory-capped,
after the last edit): `grep -ac '^!'` **0**, `grep -aci undefined` **0**,
`grep -ac Overfull` **0**, nullfont **0** (the English build is also 0; this
book has no blank-line map tables), non-backtick "Missing character" **0**,
invalid-in-math **0**, "Discard zero height" **0**; **496 pages** (English
475); the `.fls` lists **58** French chapter and solution files = **58** on disk.

## Conventions recorded

* **Books 1–2 fr conventions kept**: N, E, S, **O**; `\ang{50}~N`; spaced
  French punctuation and guillemets; the decimal point; *au \cref{…}*;
  *(livre~1, année~N)*, *(les volumes de physique, …)* for the sister series;
  *\section{Exercices}*; *Problème du week-end --- …*; solution headers
  `\section*{Chapitre \ref{…} --- Titre}`; *Données~:*; *(domaine public)*;
  *Illustration générée par IA.*; *la région imaginaire de la série*, *données
  d'exercice*; *GIEC*; the Book 1 likelihood words (*très probable, probable* …)
  and *confiance moyenne / élevée*.
* **Exercise register**: infinitive stems.
* **Units in prose**: `\Ma` for both dates and durations, `\Ga` for a billion
  years, *an* for year (*mm/an*, *m/Ma*), *jours*, *heures* as words outside
  `\qty`. See the frozen math sites below.
* **Frozen math sites (tool limit).** A `\qty` inside a math span is frozen by
  the math census, so the English `Myr`, `Gyr` and `yr` stay in 166 lines (each
  holds one to three such units): `10-heat-budget` 618, 651, 810;
  `12-plate-kinematics` 104, 249, 254; `13-rifts-ridges-margins` 473, 474, 477,
  563, 565, 786, 787, 799, 800; `14-active-margins` 245; `15-hotspots` 266, 319,
  492; `18-earthquake-source` 661, 887; `20-erosion-transport` 632, 639;
  `22-chemical-biogenic-sediments` 411; `25-radiometric-methods` 304, 819;
  `29-ocean-circulation` 96; and in the solutions `10` 79, 98, 108, 110; `11`
  128; `12` (32 lines, 4–234); `13` (32 lines, 7–221); `14` (14 lines, 18–163);
  `15` (11 lines, 14–226); `18` (13 lines, 10–213); `20` (8 lines, 91–203);
  `21` 169; `22` 44, 46–48, 106, 109; `24` (11 lines, 11–202); `25` 50, 88, 115,
  159, 212, 216. The three *Gyr* math sites the run file names are
  `10-heat-budget` 600 and `solutions/10-heat-budget` 98 (twice). **Superseded:** the coordinator ran that
  pass on 2026-10-26 after delivery (see "Coordinator addendum" at the end), so no
  `Myr`, `Gyr` or `yr` is left in any unit of the French tree.
* **Image credits**: `frontmatter/image-credits-book3.fr.tex` translated, every
  credit, author, dataset and licence kept exactly.
* **Elision at line end**: a French edition may never end a source line on
  *l'*, *d'*, *qu'*…; a final sweep enforces this (89 sites fixed).

### `!draw` ranges (each checked by eye)

* `04-geological-maps` 127–134 (legend matrix cells);
* `05-cross-sections` 384 (rock list `\foreach`);
* `06-field-lab-methods-1` 363, 371–372, 374 (`\comp` macro text arguments);
* `17-faults-folds-fabrics` 639, 649 (fold-type labels);
* `18-earthquake-source` 77, 482–485 (labels; keys `normal`, `reverse`, … kept);
* `21-clastic-sediments` 357;
* `22-chemical-biogenic-sediments` 142 (names `\foreach`);
* `23-diagenesis-basins` 534–535 (`\col` macro arguments);
* `24-stratigraphic-scale` 589–601 (chart data labels replaced by coordinates);
* `26-fluid-envelopes-structure` 340 (stability verdict labels);
* `29-ocean-circulation` 436 (warm / cold labels).

## Link layer

`tools/term_config/book3_fr.py` curated from this edition's own harvest (473
linkable terms) and the frequency and chapter-set censuses against English, with
a context read of every flagged site:

* **STOP** (linked only in the defining chapter): *stable/stables/stabilité*,
  *extension*, *étirement*, *ordre*, *relief*, *série*, *système*, *étage*,
  *groupe*, *formation*, *membre*, *flux*, *direction*, *hauteur*, *mi-hauteur*
  (all with their capitalised and plural forms) — French words that also have an
  ordinary sense (a *hauteur* of a star vs. a height, an *ordre* of a magnitude,
  a *groupe* of workers, a *système* of equations …).
* **EXTRA_PROTECT**: *déclinaison magnétique* and the compass-adjustment uses of
  *déclinaison* (the celestial *déclinaison* keeps its links); *non attribué ou
  un chevauchement*; *sur les flancs de nombreuses*; *de bon clivage*; *plus
  grand cercle inscrit*; *Service / Commission de la carte géologique*; *aux
  contacts entre grains*; *les points triples près de*; *masse d'air (par
  seconde | comprise | entrant)*.
* `AMBIG_POLICY = "drop"`.

Target reached by French but not English: *parcelle d'air*
(`def:b1:fluid-envelopes-structure:parcel`, 6 links, all in chapter 26 and its
solutions: English says *parcel* and *air parcel* and never links the word).
Counts above English, each read and in the defined sense: *courant-jet* 11 vs 4
(a one-word term), *stratification entrecroisée / paléocourant* 16 vs 8,
*rapport signal sur bruit* 10 vs 2, *point triple* 30 vs 10, *première
apparition* (biozone) 56 vs 12, *diagramme T–S / masse d'eau* 15 vs 7. English's
capitalised-definition and compound-keyword misses are the cause, not French
over-linking.

## English-canon defects reported

None changed in the English files. All are cosmetic rounding along the printed
path, or a forward reference, and the conclusions stand.

1. `parts/bachelor-1/solutions/02-observing-the-sky.tex` l. 71–72:
   `e^{-0.147×2.31} = e^{-0.340}` printed 0.711; along the printed rounded path
   0.7118 → 0.712 (0.711 comes from the unrounded 0.3405).
2. `parts/bachelor-1/solutions/05-cross-sections.tex` l. 140–141 (problem item
   7): `0.2155 × 0.9869 = 0.21268 → 0.2127`, printed 0.2126; and l. 48 (exercise
   7): `100/0.2155 = 464.0`, printed 464.1 (both come from the unrounded 0.215482).
3. `parts/bachelor-1/solutions/06-field-lab-methods-1.tex` l. 46–47 (exercise 7):
   `tan p = 0.2126×0.7660 = 0.1628`, `p = arctan 0.1628 = 9.25° → 9.2`, printed
   9.3 (the unrounded 0.16283 gives 9.248 → 9.2 as well).
4. `parts/bachelor-1/solutions/07-rock-forming-minerals.tex` exercise 11 (l.
   109–113): `Al = 2×0.28344×2.72446 = 1.544` (printed 1.545); `Al − 1 = 0.544 = Ca`
   exactly, not 0.545; large site 0.544 + 0.448 + 0.017 = 1.009 (printed 1.010).
   An 53.9 unchanged.
5. `parts/bachelor-1/solutions/09-layered-earth.tex` exercise 2 (l. 14): the K
   change `(644.1 − 655.6)/655.6 = −1.754 %` along the printed path (−1.8 %),
   printed −1.7 % (the unrounded value is −1.749 %).
6. `parts/bachelor-1/solutions/24-stratigraphic-scale.tex` problem item 17 (the
   solution's l. 178–181 in the English): "They span 16 thousand years, less than
   the uncertainty of each (about 28 thousand years, question 19)". Question 16
   is the first appearance of *V. ultimum*: `f = (65.8 − 5.0)/66 = 0.921`,
   `(52.0 − 8.0)/48 = 0.917`, `(24.8 − 3.0)/24 = 0.908`, and
   `σ_t = 0.04 √((1−f)² + f²) = 0.0370, 0.0368, 0.0366 Myr`, i.e. about **37**
   thousand years. The 28 thousand years are the *V. medium* ages of question 19
   (f ≈ 0.48), asked later (a forward reference). The conclusion (16 < 37, and
   16 < 28) stands. Kept as in English in the French edition.
7. `parts/bachelor-1/solutions/24-stratigraphic-scale.tex` problem item 15
   (English l. 173–175): `B to A = 25/(152.10 − 151.67) = 58.1` along the printed
   path; printed 58.5 comes from the unrounded 151.6727 (25/0.4273). Cosmetic.

## Gate and tool fixes

* `tools/check_latin_prose.py`: (a) `_has_lowercase_word` now strips siunitx
  option brackets (`\qty|num|ang|unit|si|SI|qtyrange|numrange|angle[…]`), so
  `\qty[text-series-to-math=true]{1660}{km}` is no longer read as an English
  word; (b) an append-only `ALLOWED_BY_LANG["fr"]` entry with an explanatory
  comment block for words identical in French and English or file keys that must
  match a figdata table: `buried`, `surface` (ch. 23 `symbolic x coords`),
  `zrupb`, `spupb`, `hbar`, `mssr`, `msar`, `btsr`, `btar`, `zrft`, `kfsar`,
  `apft` (ch. 25 `symbolic y coords`), `monosiallitisation`, `allitisation`,
  `anticyclone` (identical French terms, ch. 19 and 28).
* The run's private `mk.py` (assembler of patch chunks, not a repo tool) gained
  a rule that reverts `\Ma`/`an`/`\Ga` to the English `Myr`/`yr`/`Gyr` inside
  math spans (and keeps `\Ma` where the English math itself has it), so the
  patch files can write the prose form everywhere.
* Elision at line end and the TeX Live 2026 `\textsuperscript` rule (brace it:
  `{1\textsuperscript{er}}` in a pgfplots axis, ch. 27) are documented in the
  repository `CLAUDE.md` already.

## Departures from Books 1–2 fr

* **Unit symbols inside math** stay English `Myr`/`yr`/`Gyr` (166 lines, listed),
  where Book 2 fr was later converted to *Ma* formula by formula; prose uses
  *Ma*/*Ga*/*an*, as Books 1–2.
* **Instruction register**: infinitives, as Book 2 (university and lycée), not
  Book 1's collège imperative.
* **Real-world names**: some university-level proper names keep their original
  form (the region *Basin and Range* is kept in English in the text and glossed
  *Grand Bassin* in the table row of ch. 10; catalogue names such as *Adams–Williamson*, *Hjulström*, *Bouma*, *Folk*).
* **Kept anglicisms where French texts keep them**: *seeing*, *backstripping*,
  *core complex* (as *core complexes océaniques*), *pitch*, the acronyms *GSSP*,
  *OLR* (introduced as *rayonnement infrarouge sortant*, "de l'anglais
  *outgoing longwave radiation*") and *AAIW, NADW, AABW* (each spelled out in the
  text of ch. 26 and 29); the French acronym *ZCIT* replaces *ITCZ*.

## Resumability

Nothing remains: every file is written, linked and built. Scratch, patch files
and notes are under the agent's scratchpad (`fr3/`); the repo files are
authoritative.


## Coordinator addendum (2026-10-26, after delivery)

Changes made by the coordinator after the agent's report, so that this file
describes what is on disk. Every one was followed by the gates, the linker
`--check` and a dry run of 0, and by a final forced build (below).

* **Time units, one convention.** The 172 `\qty`/`\unit` arguments that still
  held `Myr`, `\Myr`, `Gyr` or `yr` (162 in math spans, 10 in prose) were
  rewritten to `\Ma`, `\Ga` and `\year` in the 21 files concerned, line counts
  unchanged. `\year` now prints *an* in French (`\omunitYear` in `styles/lang/fr.tex`,
  a conditional `\DeclareSIUnit` in `styles/oneearth.sty`), so a rate reads
  *mm an⁻¹* and *km Ma⁻¹*, as in French geoscience texts. The math spans therefore
  differ from English in those units on purpose; a probe of chapters 14 and 18
  checked the rendering. This is the same convention as Book 2 fr.
* **Three English-canon fixes**, mirrored into the French tree (digits only):
  `solutions/02` `e^{-0.340} = 0.712` (was 0.711); `solutions/06` `p = 9.2°` (was
  9.3: arctan 0.1628 = 9.248°); `solutions/07` exercise 11, Al 1.544, `2.453 + 1.544
  = 3.997`, large site 1.009, Al − 1 = 0.544, An = 100×0.544/1.009 = 53.9 (the
  printed 1.545 was a double rounding of 1.5444). The other four reported slips
  were checked and left: 464.1 m and 58.5 km/Myr are right from the unrounded
  values, −1.7 % is right unrounded (−1.749), and the forward reference to
  question 19 is deliberate.
* **Wrong-sense links.** "Voting members" of a commission linked to the
  lithostratigraphic *member*, in English (2 body + 2 box sites) and in French
  (*membres votants*, *membres ne votant pas*); French also linked *groupe de
  travail* and *le groupe a proposé*. All are protected now. Links: English
  4,654 → **4,650**, French 4,475 → **4,468 on 185 targets** (the extra target is
  *parcel*, 6 links).
* **`Tableau`.** The caption label and the `\cref` name for tables are
  *Tableau* (style and `fr.tex`).
* **Shared tool.** The agent's two edits to `tools/check_latin_prose.py`
  (siunitx option brackets stripped; an append-only `ALLOWED_BY_LANG["fr"]` entry)
  were read and accepted: the first only makes the gate more lenient.

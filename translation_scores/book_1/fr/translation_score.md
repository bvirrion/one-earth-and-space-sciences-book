# Translation score — Earth and Space Sciences Book 1 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 1 (Primary and Middle School, Grades 1–9) |
| **Language** | French (`fr`) |
| **Quality bar** | **native school prose at every level**: a French children's science book in grades 1–5, a French collège textbook (SVT / sciences de la Terre) in grades 6–9. English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); the shipped French Biology Book 1 (`../one-biology-book/parts/grade-*/fr/`) for the *tu* register of exercise stems, the solution headers and typography; the French Chemistry Book 1 for the series toolchain conventions; the French physics editions for shared physical vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-25 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 32 chapters + 32 solution twins = **64 files**, every one written through `tools/id_apply.py`; `frontmatter/preface.fr.tex` and `frontmatter/image-credits.fr.tex`; the aside-box block of `styles/lang/fr.tex` (*Tu sais déjà*); the `\bookline` / `\author` lines of the entry file (already French, kept); a curated `tools/term_config/book1_fr.py`; the defined-term link layer; French index keys with ASCII sort keys; a per-figure label check of the rendered PDF; and this score |

## Verdict in one line

A French Book 1 that reads as one French school course in the sciences of the
Earth from the first year to the ninth: *tu* and short sentences for the
youngest readers, *nous* / *on* in the course text of the collège years,
2sg imperative exercise stems throughout (*Utilise*, *Nomme*, *Regarde*,
*Range*, *Associe*, *Donne*), French spaced punctuation and guillemets,
French cartographic and meteorological conventions (O for west, A/D for
pressure centres, 24-hour clock), with every structural and prose gate green
over the nine years and a forced build of **0 errors / 0 undefined /
0 overfull**, 340 pages, `.fls` 64 = 64 files on disk.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 64 files against their 64 twins: **370 `exercise`**, **20 `problem`**, **390 `\begin{solution}`**, **234 `omfigure`**, **161 `tikzpicture`**, **73 `axis`**, **120 raster includes**, **455 `\emph`**, **237 `\index`**, **105 `\cref`**, **816 `\label`**, **468 `\item`**, **834 `\qty`**, **588 `% ledger:`** comments, and per environment **140 `definition`, 4 `proposition`, 42 `method`, 60 `example`, 24 `remark`, 30 `recall`, 7 `inthefield`, 9 `inthelab`, 10 `history`, 2 `dated`, 7 `safety`** — all equal to English; `\label` set diff **0 / 0**. `\node` is 741 against 677: every English label read from a figdata table (`meta=name/label`, `yticklabels from table`) became explicit French `\node`s or tick labels, coordinates copied from the `.dat` rows. A per-file number census against English finds only the expected differences (24-hour clock, *xix*e siècle, explicit label coordinates, the explicit grid lists below) |
| Terminology | **96** | French collège vocabulary, consistent across nine years: *temps qu'il fait, tableau météo, station météo, pluviomètre, girouette*; *plan, carte, légende, échelle, rose des vents, points cardinaux*; *galet, sable, roche, boue*; *planisphère, équateur, hémisphère nord/sud*; *altitude, niveau de la mer, relief, carte physique*; *altération, érosion, dépôt, source, embouchure, affluent, méandre, crue, plaine d'inondation*; *aléa naturel, catastrophe naturelle*; *planète rocheuse/géante, parallèle, méridien d'origine, fuseau horaire, ligne de changement de date*; *minéral, roche magmatique/sédimentaire/métamorphique, grès, argilite, cycle des roches, échelle de Mohs*; *croûte, manteau, noyau, ondes P/S*; *ruissellement, infiltration, porosité, perméabilité, nappe, aquifère*; *plaque tectonique, limite divergente/convergente/transformante, dorsale, fosse, Pangée*; *chambre magmatique, bouche éruptive, cratère, coulée pyroclastique, point chaud*; *foyer, épicentre, magnitude, intensité, sismomètre, tsunami*; *strate, fossile, moule/moulage*; *principe de superposition/recoupement/inclusion, discordance, ère, période géologique, échelle des temps géologiques* (ICS names in French); *troposphère … thermosphère, couche d'ozone, alizés, vents d'ouest, pot-au-noir, masse d'air, front froid/chaud/occlus, dépression, anticyclone, isobare, prévision météorologique*; *plateau continental, plaine abyssale, gyre, banquise*; *névé, zone d'accumulation/d'ablation, front glaciaire, vallée en U, moraine, calotte glaciaire, plate-forme de glace, pergélisol, glaciation*; *gaz à effet de serre, anomalie de température, réchauffement climatique, GIEC* with the GIEC's own calibrated likelihood words; *aléa, vulnérabilité, risque, prévention, carte des aléas, crue centennale*; *gisement, facteur de concentration, teneur, filon, placer, granulats, réserves*; *soulèvement, barkhane, face d'avalanche, encoche, plate-forme d'abrasion, dérive littorale, flèche littorale, karst, doline*; *projection de Mercator / équivalente, échelle numérique/graphique, courbe de niveau, équidistance, point coté, courbe maîtresse, dénivelée, télédétection, positionnement par satellite*. All 237 `\index{}` keys in French, with ASCII sort keys (`vallee en U@vallée en U`). Place names take French exonyms (*Groenland, Le Cap, Le Caire, Bombay, Londres, mer du Nord*) |
| Register / tone | **97** | Measured, not assumed. Grades 1–5: *tu* throughout; grades 6–9: course text in *nous* / impersonal *on*, exercise stems in 2sg imperative (the register of the French Biology Book 1 school volumes); **0** *vous* anywhere. The commonest exercise openers: *Sur* ×34, *Vrai ou faux* ×18, *Utilise* ×17, *Nomme* ×12, *Regarde* ×10, *Range* ×9, *Associe* ×8. Box names: *Tu sais déjà*, *Sur le terrain*, *Au laboratoire*, *Histoire des sciences*, *Chiffres de*, *Sécurité*. Observation-only wording kept everywhere (cliffs observed from a distance, the Sun never looked at) |
| Typography | **97** | French spaced punctuation (`~:` `~;` `~?` `~!`) and guillemets `«~…~»`; the decimal point and `\,` thousands kept as the series' siunitx setting does; `\textsc{xix}\textsuperscript{e}~siècle`; *million(s) de* agreement; final sweeps: **0** lines ending on an elision apostrophe, **0** prose lines opening on punctuation, **0** dangling hyphens, **0** straight quotes |
| Fidelity / accuracy | **95** | Every course paragraph, worked example, exercise and solution translated against its twin with the numbers recomputed while translating; every solution re-read against its question in French. Six English-canon slips were found and are reproduced, not silently fixed (listed below). Figdata tables that carry English visible labels were translated by explicit nodes whose coordinates were copied from the `.dat` rows and checked |
| Figures | **95** | Every rendered figure page of grades 8–9 read at 100 dpi in the final pass (grades 1–7 in earlier passes); collisions found and fixed: the greenhouse-effect diagram (absorbed-radiation label over the atmosphere label), the coal-formation panels (four captions running into each other), the copper flow chart (*extraire, broyer,* over a box edge), the magma-body label, the risk grid (rotated *vulnérabilité* over *faible*), the plate-boundary bar chart (narrowed after a 4 pt overfull), and earlier ones in grades 1–7. A leader line dropped from the effusive-volcano sketch (grade 7) was restored. Two known layout blemishes, both from the longer French problem statements: the grade-9 weekend problems of chapters 29 and 32 start low on a page, so their map moves to the next page and leaves a third of the page blank |
| Links | **95** | **6003 `\omterm` links on 137 targets** against English's **6102 on 136**: every English target is linked (**0 missing**), plus the international date line, which English defines but never matches (its text always says "date line"). Dry run over the wrapped tree: **links to insert: 0**; `--check` clean |

## Gates

`bash tools/check_translation.sh grade-N fr` for N = 1 … 9: **9 / 9 PASSED**
(structural censuses, duplicate labels, ledger ids, the twin-comparison prose
gate — no multi-word finding; the advisory one-word tier is cognates and
proper names only: *stratus, cumulus, cirrus, granite, Andes, Sahara, Delta,
Magma, Magnitude, Tsunami, Dune, Seattle, Nazca* …; orphan lines 0 in every
year). `bash tools/gates.sh grade-N` for N = 1 … 9: **rc 0** each.
`tools/check_orphan_lines.py`: **0** in all nine years.
`tools/check_term_display_drift.py` over the edition: every multi-display
target is inflection (singular/plural, capital) or one of the several terms a
definition introduces.

Build (`latexmk -g`, forced, through the run's wrapper under its memory cap):
`grep -ac '^!'` **0**, `grep -aci undefined` **0**,
`grep -ac Overfull` **0**, invalid-in-math **0**, missing characters
other than the backtick-in-nullfont noise every Book 1 build shares with
English **0**; **340 pages**; the `.fls` lists **64** French
chapter and solution files = **64** on disk.

## Conventions recorded

* **Compass and hemisphere letters**: N, E, S, **O** (`\omnameCompassW{O}`);
  coordinates in prose, figures and ticks use the same letters
  (`$41^\circ$\,N`, `\ang{30} S`, `$150^\circ$O`).
* **Pressure centres**: H/L of the English weather maps become **A/D**
  (anticyclone / dépression), the French weather-service convention, explained
  where they first appear.
* **Clock**: 24-hour (*15~h*), so solutions that convert times read in hours.
* **Cross-references**: *au \cref{…}* / *le \cref{…}* with the chapter
  number; *Problème du week-end --- …*, *Partie I --- …*.
* **AI images**: *(illustration générée par IA d'une scène générique)*;
  sketches *(un croquis, sans souci d'échelle)*.

## Link layer

`tools/term_config/book1_fr.py` was curated from this edition's own
`--terms` harvest (249 entries) and a per-target census
against English (chapter set, frequency, missing) plus a context read of
every flagged site — never translated from `book1_en.py`. French homographs
handled, each with evidence in the config:

* *échelle* — a drawing *à l'échelle*, *sans souci d'échelle*, the scale of a
  graph (*l'échelle de gauche*), *échelle des temps*, *notre échelle de
  temps*, *à grande échelle*, *à l'échelle de la ville*: only the map scale
  links (87 sites → 15; English links 15); *échelle d'intensité* is EXTRA to
  the seismic intensity, as English does with "intensity scale";
* *front* — the snout of a glacier (24 sites in chapter 27) and the face of a
  cliff; stopped outside the weather-fronts chapter, where English links it;
* *symbole* — English defines the two-word "map symbol"; the bare French word
  also names weather-front and trail signs;
* *plaque* (EXTRA, the short form of *plaque tectonique* the later chapters
  use, as English's EXTRA "plate") — but not *plaque de glace / de verre*;
* *carte postale*, *l'Équateur* (the country), *coulées de boue* (English
  "mudflow", one word), *relief ETOPO1*, *ère industrielle*, *parallèle*
  as an adjective, *source de chaleur / région source / sources chaudes*,
  *gisement de pétrole*, *risque de* (verb), the Natural Earth credit lines
  (*côtes*), *Organisation météorologique mondiale*;
* the bold *Partie I/II/III* headings of the weekend problems (the shared
  protect list masks only the English "Part");
* *minéraux* (EXTRA: the plural is not a WORD_TAIL form), *bouche* (EXTRA:
  the volcano's *bouche*, short for *bouche éruptive*), *météo /
  météorologique* (EXTRA to the weather: French says *le temps*, a homograph
  of time, which cannot be linked).

Target counts that differ most from English, each read: *temps qu'il fait*
36 vs 99 (French cannot link *le temps*; it links *météo*, *météorologique*
and the defined phrase); *gisement* 22 vs 10 (French uses the defined
word where English says "deposits"); *altitude*, *relief*, *dépôt* reach a
few chapters English does not, in the defined sense (French says *altitude*
where English says "height").

## English-canon defects reported (not fixed in the canon)

1. `parts/grade-7/05-geological-time.tex` line 75 and caption 28–30: the
   principle of superposition is credited to Hutton (end of the eighteenth
   century); it is Steno's (1669).
2. `parts/grade-7/solutions/05-geological-time.tex` pb 6, lines 115–117:
   "about 84 days … 25 March"; by the rounding convention of solutions 5 and 7,
   84 days is 26 March (25 March only with the unrounded 83.6).
3. `parts/grade-8/solutions/03-fronts-and-weather-maps.tex` line 63: "About
   1250 km (four scale bars and a little more)"; the figure's centres give
   about 1352 km (4.5 bars).
4. `parts/grade-8/01-the-atmosphere.tex` lines 291–292 give about −90 °C at
   the top of the mesosphere; the solution of exercise 2(d) reads −86 °C from
   the same profile.
5. `parts/grade-8/solutions/04-the-oceans.tex` line 36: "between 1500 and
   2700 m"; with plains at 3500–5000 m and the crest at 2300 m the range starts
   at 1200 m.
6. (minor) `parts/grade-9/solutions/04-landforms.tex` pb 10: 19.5 years after
   2024 is given as 2043 (arguably 2043/44).
7. (link layer) `tools/term_config/book1_en.py`: the international date line
   is defined as "international date line" but the text always says "date
   line", so English never links it (French: 5 links).
8. (figdata) English visible labels inside figdata tables (`meta=name`,
   `yticklabels from table`): `grade-3-globe-*-labels`, `grade-6-cities-map`,
   `grade-6-planets-sizes`, `grade-6-water_table-*`, `grade-7-volcano_settings`,
   `grade-7-quake_counts`, `grade-7-time_scale-*`, `grade-7-earth_calendar-*`,
   `grade-8-standard_atmosphere-*`, `grade-9-climate_records-decades`,
   `grade-9-concentration` — no edition can translate them; each became
   explicit nodes or tick labels under `!draw`.

## Coordinator addendum (2026-10-25, after wave 1)

Re-verified by the coordinator after the wave-1 canon fixes and tool changes:
- a forced build: 340 pp, 0 errors / 0 undefined / 0 overfull, nullfont 6,633, `.fls` 64 = 64;
- `check_translation.sh` 9/9 PASSED under the stricter gates (per-range `!draw`, the 12-character dup tier, the whole-word tokenizer);
- relinked with the multilingual Part-heading protect: **6003 links**, 137 targets, dry run 0.

The coordinator mirrored the canon fixes listed in `sources/WAVE1_FINDINGS.md` §1 into this edition, among them the problem-6 date (**25** March, which reverts the first fix to 26) and the three rainy afternoons. The score is unchanged.

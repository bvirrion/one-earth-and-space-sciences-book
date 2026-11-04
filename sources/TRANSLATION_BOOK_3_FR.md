# Translation run — One Earth and Space Sciences Book 3 into French (`fr`)

The binding run file for the French edition of Book 3 (University Year 1,
`parts/bachelor-1`): 29 chapters + 29 solution files = **58 files, 31,599
lines**, ~475 pp in English. User request, 2026-10-26: *"do the translation in
French of one earth and space sciences book 3"*. One subagent owns the edition.
No other language is in scope; the six others will follow in a later run and
will start from `sources/WAVE1_FINDINGS_B3.md`, which the coordinator writes
when this edition closes.

**Models (recorded 2026-10-27):** the edition agent and the coordinator both ran
`claude-sonnet-5-5` (Sonnet 5.5).

This is the **first translation of Book 3**, and the first university volume of
this series: nobody has ever read the English canon in a second language. Books
1 and 2 shipped in eight languages with this same toolchain; their run files
(`sources/TRANSLATION_BOOK_1.md`, `sources/TRANSLATION_BOOK_2.md`) and findings
(`WAVE1_FINDINGS.md`, `WAVE1_FINDINGS_B2.md`, `WAVE2_FINDINGS_B2.md`) are
**still binding** wherever this file does not say otherwise. Where they
disagree, **this file wins**.

If you are the edition agent, this file and your brief are your instructions.
Read everything in "Reading list" before you write a line.

## Reading list (in this order, whole files)

1. `../CLAUDE.md` (workspace root) and `../book_style.md`.
2. `../translation_instruction.md` — **the whole file**, including both
   "Lessons from the … Earth and space translations" sections at its end.
   Nearly every paragraph is a defect class some earlier edition shipped.
3. `CLAUDE.md` (its "Language editions" sections above all), `CONTRIBUTING.md`,
   `OUTLINE.md` (the Book 3 chapter list) and `sources/SERIES_DEFINITIONS.md`.
4. `sources/TRANSLATION_BOOK_1.md`, `sources/WAVE1_FINDINGS.md`,
   `sources/TRANSLATION_BOOK_2.md`, `sources/WAVE1_FINDINGS_B2.md`,
   `sources/WAVE2_FINDINGS_B2.md`.
5. This file.

## Your reference editions (read before drafting)

- **This series' French Books 1 and 2** — `parts/grade-{1..12}/fr/`,
  `translation_scores/book_{1,2}/fr/translation_score.md` (their **Conventions**
  sections) and `tools/term_config/book{1,2}_fr.py`. Book 3 recalls ~all of their
  notions (*plaque, dorsale, fosse, isobare, front, cycle de l'eau, cycle des
  roches, isostasie, flux géothermique, onde P/S, Moho, lame mince, …*): grep
  them before choosing a word. **Keep every convention they recorded**: compass
  and hemisphere letters (N, E, S, **O**; already in `styles/lang/fr.tex`),
  `\ang{21}~S`, spaced punctuation and guillemets, *GIEC*, the likelihood words,
  place-name exonyms, box names, solution headers, `Données~:`, *au \cref{…}*.
  A disagreement with Books 1–2 is reported, not made silently.
- **The register of a university course.** Book 3 is Licence 1 (18–19 years):
  a lecture-and-textbook voice, impersonal *on* and the present tense, no longer
  the lycée voice of Book 2. **Measure the instruction register of your
  exercise stems against the French University Year 1 editions of the sister
  series before you score, and convert as a reviewed pass, never a regex**:
  `../one-physics-book/parts/bachelor-1/fr/`,
  `../one-biology-book/parts/bachelor-1/fr/`,
  `../one-chemistry-book/parts/bachelor-1/fr/` (and their score files). Book 2 fr
  used infinitive stems (*Calculer*, *Expliquer*): do not copy that blindly;
  count what the university volumes do and follow them, state the counts in the
  score file.
- **Terms a sister series owns** — physics (energy, radiation, pressure, waves,
  heat transfer, black body, spectra), chemistry (every `\ce` species, isotopes,
  solutions, pH, redox, equilibrium, ionic potential), biology (carbonate
  producers, life): use the rendering your language's edition of that series
  already uses (`grep` its `parts/**/fr/`) and report a disagreement instead of
  diverging silently.

## Hard rules (all binding)

1. **You own exactly one edition.** You write only:
   - `parts/bachelor-1/fr/*.tex` and `parts/bachelor-1/solutions/fr/*.tex`;
   - `tools/term_config/book3_fr.py` (a stub is waiting — curate it from YOUR
     edition's harvest, never by translating `book3_en.py` and never by copying
     `book2_fr.py`: Book 2's EXTRA values are Book 2 labels, its protects another
     book's judgement — re-verify each entry you reuse);
   - `translation_scores/book_3/fr/translation_score.md`;
   - `frontmatter/image-credits-book3.fr.tex` (an English stand-in now: keep
     every photograph credit, author name, dataset name and licence exactly;
     translate the frame and the descriptions; the model is
     `frontmatter/image-credits-book2.fr.tex`; the preface
     `frontmatter/preface.fr.tex` is shared and already done — do not touch it);
   - your entry file's `\bookline` and `\author` lines only
     (`one_earth_and_space_sciences_book_3_university_year_1_fr.tex`; the
     coordinator wrote `Livre 3~: L'université -- Année 1`).
   Nothing in `styles/lang/fr.tex` should need to change; if a string is missing
   or wrong for Book 3, report it.
2. **Never edit the English canon** (`parts/bachelor-1/*.tex`, `solutions/*.tex`),
   the style file, shared tools, other books' files or another language's files.
   A canon defect is REPORTED to the coordinator with file, line and evidence;
   the coordinator verifies it against the book's own model (the figure, its
   data, the sibling answers) and fixes it. Work around it in your edition only
   if the fix is obvious and local, and say so.
3. **Never run a repo-wide git command** — no `git checkout -- .`, `git restore`,
   `git stash`, `git clean`, `git reset`. The repo holds the coordinator's
   uncommitted Step-0 work; on Biology Book 4 one such command destroyed every
   uncommitted change in the repo, and `git clean` would delete every translated
   file. To undo your own work, rewrite that specific file. **Never commit.**
   Read-only git (`git diff`, `git status`, `git log`) is fine. Never wildcard-`rm`.
4. **Shared tools are shared.** `tools/check_*_prose.py`, `tools/id_apply.py`,
   `tools/check_translation.sh`, `tools/check_orphan_lines.py`,
   `tools/check_chem_twin.py`, `tools/termlink/*`, `styles/*`: report bugs
   instead of editing. The one exception is a per-language allow-list entry
   (`ALLOWED_BY_LANG["fr"]` in `check_latin_prose.py`), **append-only, with a
   comment giving the reason and "Book 3 fr"**, placed BEFORE any
   `if __name__ == "__main__"` guard, and run once to confirm it changed the
   output. An agent that rewords correct prose to satisfy a gate has found a gate
   bug: report it.
5. **Scratch files go in your PRIVATE directory**
   `/tmp/claude-1000/-home-bvirrion-repositories-one-course/97f0e3f2-5701-4b88-a267-b9eb75b5601f/scratchpad/fr3/`
   (patch files, probes, helper scripts). Keep your patch files: they are the
   only record of a chapter before `id_apply` writes it. `/tmp` has been wiped
   mid-run before: after every chapter written, the chapter on disk is the record.
6. **Resources** (the user's 19 GB laptop; you are the only agent, but the
   coordinator may build too):
   - **every full-book build goes through the wrapper**
     `bash /tmp/claude-1000/-home-bvirrion-repositories-one-course/97f0e3f2-5701-4b88-a267-b9eb75b5601f/scratchpad/build.sh one_earth_and_space_sciences_book_3_university_year_1_fr <outdir-name>`
     — TeX Live 2026 (as CI), forces `-g`, holds one machine-wide build slot,
     caps memory, builds into the scratchpad (not the repo) and prints pages /
     errors / undefined / overfull / nullfont / non-backtick "Missing
     character" / invalid-in-math, the `.fls` count against the files on disk,
     and "Discard zero height". A build takes 6–12 minutes: **run it with
     `run_in_background`**. Never call `latexmk` on a whole book directly,
     never `make`, never build a book that is not yours;
   - for overfull work, `\input` a single chapter into a probe of the book's
     preamble (seconds) instead of rebuilding the book; write the probe into
     your private directory and run it from the repo root with the same
     `-cnf-line` memory flags as `latexmkrc` and `PATH` starting with
     `~/texlive/2026/bin/x86_64-linux`;
   - every other long job: `nice -n 19`, `OMP_NUM_THREADS=1`, one at a time;
     never run the repo's pytest suite.
7. **Never name a programme** (no "licence de géologie", "L1 SVT", "CPGE",
   "BCPST", "PCSI", "programme de …", no year or version of a national syllabus).
   The part title `Licence 1re année (18--19 ans)` is in the shared
   `styles/lang/fr.tex` and is not yours; an ordinary school-stage noun for the
   reader's age (*université*, *premier cycle*) is fine.
8. **Labels never translate**: `\label`, `\cref`/`\ref`/`\pageref` targets,
   `\begin{solution}{key}`, the first argument of `\omterm`, file names, image
   paths, figdata table paths, TikZ node names, colours, styles, pic names,
   pgfmath macro names (`\W`, `\H`, `\dx` …).

## Earth and space conventions (as in Books 1–2, plus what is new in Book 3)

- **`% ledger: <id>, …` comments stay on their line, unchanged** (734 in Book
  3). Gate 12 (`check_chem_twin.py`) compares the id multiset of every file with
  its English twin.
- **Book 3 has 366 `\ce{}` formulas**, most in running prose outside any math
  span. They are frozen byte for byte: `id_apply`'s `chem` census at write time
  and gate 12 on disk after every later edit; gate 13 checks every reaction still
  balances. Never localise a state symbol (`(aq)`, `(s)`), a mineral formula or an
  arrow; translate the words around them. Ion and species names in prose follow
  the French chemistry edition.
- **Code arguments stay byte-identical**: `\omwx{…}`, `\omlith{…}`, `\omve{N}`,
  every `lith <rock>` / `om lith` style, every pic, every figdata path.
- **New in Book 3 — environments and macros the earlier books did not use**:
  `lemma` (1) and `notation` (1) heads (`\omnameLemma` = *Lemme*, `\omnameNotation`
  = *Notation*, in the style); `table` with `\caption` (12) and **`\cref{tab:…}`
  (27)** — the coordinator added `\omnameTable`/`\omnameTables` (*Tableau/Tableaux*)
  and a `\crefname{table}` to the style on 2026-10-26, because cleveref printed
  its English "table"; check one rendered reference; `groupplot` (3, pgfplots
  group plots), `pmatrix` (6, in math), `description` (1), `\si{}` (37, legacy
  siunitx), `\admitted` (13, a style macro that prints a proof head and the string
  `\omadmittedtext`, already *Admis à ce niveau.* in `fr.tex`: nothing to translate),
  `\textquoteleft` (the Hawaiian
  *ʻokina* of *Puʻu ʻŌʻō*: keep), 366 `\ce`, `\sverdrup`, `\gal`, `\mag`, `\angstrom`,
  `\dex`, `\darcy` units (frozen).
- **Units.** Never a non-ASCII character or a word inside `\qty{}`, `\unit{}`,
  `\num{}`. Before the run the coordinator moved the words *days* and *years*
  out of every `\qty` (7 sites, listed below), so you can write *jours*, *ans*.
  `hPa`, `dbar`, `ppm`, `GPa`, `Myr`, `Gyr`, `mas`, `nmol`, `kbar`, `mol`, `kWh`,
  `atm`, `min`, `mPa.s`, `Mkm^2`, `Mkm^3` are symbols and stay. **Million-year
  units**: English writes `Ma` for a date and `Myr` for a duration. French uses
  `Ma` for both in prose (as Books 1–2 fr) and `Ga` for a billion years; inside
  math spans the frozen `\qty` keeps English's unit (`Myr`, `Gyr`): list each such
  site in the score file as a tool limit. `Gyr` (a billion years) occurs at `10-heat-budget` 88 (table header), 532, 533, 776,
  778 and `solutions/10-heat-budget` 58, 100 in prose, and at `10-heat-budget` 600 and
  `solutions/10-heat-budget` 98 (twice) inside math spans: French writes `Ga` in prose
  (`\qty{4.54}{\Ga}` is fine: `\Ga` is a style unit), and the three math sites are
  frozen. Record the choice in the score file.
- **Compass, hemisphere and coordinate letters**: keep Books 1–2's convention
  exactly (`\omnameCompass*`; `\ang{50}~N` → `\ang{50}~N`, but *O* for West).
  Book 3 adds coordinates in tick labels, in the weather map labels and in
  tables.
- **Place names** take the established French exonym (*Islande, île de la
  Réunion, Groenland, Hawaï*); institutions, datasets, missions, model names
  keep their proper names (USGS, NOAA, GISTEMP, ETOPO1, PB2002, PREM, MORVEL,
  ICS, …), with any descriptive gloss translated. Titles of papers and any gloss
  a translator adds to them **never link** (protect them).
- **Observation only**: the canon never sends the reader to a quarry, a cliff, a
  cave, a volcano or a river in flood, never has them hammer a rock or look at
  the Sun. Keep that true in your wording (a stem "a geologist measures the dip"
  must not become "mesurer le pendage sur l'affleurement"). The optical
  mineralogy and spherical astronomy chapters use a polarising microscope and a
  telescope in the lab or the observatory: as in the canon.
- **Physical science only on climate** (ch. 26–29): no policy wording.
- **Spherical astronomy and angle notation.** Chapters 1–2 write hours, minutes
  and seconds, declinations and altitudes with `\ang{}` and a small family of
  custom macros; the compass letters, *hauteur*, *azimut*, *déclinaison*,
  *ascension droite*, *angle horaire*, *temps sidéral*, *équation du temps*,
  *méridien*, *zénith*, *nadir*, *écliptique*, *équinoxe*, *solstice* follow
  French usage; the degrees/hours notation inside math is frozen.

## Visible text that is NOT an ordinary prose line — every site, with its line

**`\foreach` lists with visible words** (compared byte for byte by `id_apply`'s
`draw` census, so translating one costs an `@@ N-M !draw` on that range — record
each in the score file and check the list by eye; translate only the visible
fields, keep numbers, colours, node names). The coordinator listed the lists
whose fields carry words; **verify each by eye in the rendered figure, and look
for any I missed** (a list of single capital letters is code):

- `05-cross-sections` 384 (`colour/y/rock`: *chalk, shale, limestone, sandstone,
  …*; the `ics…` colour names are code)
- `17-faults-folds-fabrics` 639 (*gentle, open, tight, isoclinal*), 649 (*upright,
  inclined, recumbent*)
- `18-earthquake-source` 77 (panel captions), 482 (focal-mechanism captions with
  `\\` and `$…$`)
- `21-clastic-sediments` 357 (*plane bed, ripples, dunes, upper plane bed,
  antidunes*)
- `22-chemical-biogenic-sediments` 142 (*fringing reef, barrier reef, atoll*)
- `26-fluid-envelopes-structure` 340 (*stable layer: the parcel sinks back* …)
- `29-ocean-circulation` 436 (*warm*, *cold*)

**pgfplots string keys and legends** (`xticklabels=`, `yticklabels=`, `\legend{}`,
`\addlegendentry{}`; blanked by the census, translated freely) — 50 legend sites
and the tick-label keys, by chapter and line: 01: 400, 446, 490, 499 · 02: 533 ·
03: 314, 322 · 05: 140 · 08: 341 · 09: 134, 159, 161, 163, 265, 267, 269, 434,
446, 450, 453 · 10: 454–462 · 11: 507–525 · 12: 269, 271, 273, 501 · 13: 509–515 ·
14: 188, 291, 298–304, 376–380 · 15: 306, 308, 339, 341, 450–454 · 16: 756 · 18:
653 · 19: 214, 222 · 20: 334 · 21: 182 · 22: 584 · 23: 183, 188, 189, 195 · 25:
499, 570–573 · 26: 602 · 27: 278, 539 · 28: 661 · 29: 344–350, 577, 583. Latitude
tick labels use your hemisphere letters.

**`symbolic x coords` cannot hold non-ASCII.** `23-diagenesis-basins` 188
(`{buried, surface}`, columns of `compaction-demo.dat`) prints its keys as tick
labels: keep the ASCII keys (the `.dat` file uses them) and add an explicit
`xticklabels={…}` in French under `!draw`.

**Figdata tables whose text reaches the page** — the only ones in Book 3:
`24-stratigraphic-scale` 589–601, the ICS chart: `bachelor-1-ics_chart-eras.dat`
(*Paleozoic, Mesozoic, Cenozoic*), `-periods.dat` (the eleven period names),
`-events.dat` (*end-Permian, end-Cretaceous*), and the node at 602 (*Quaternary*).
Replace each `meta=name` plot by explicit nodes (or an `xticklabels` list)
coordinate by coordinate, under a per-range `!draw`, using the `.dat` coordinates,
and **render the page and check every label against its band.** The other
`meta=` tables hold numbers (`05` varden labels, `26` isopycnal values, `28`
pressure labels, `03` temperatures), ion formulas (`19`, `Cs$^{+}$`) or
acronyms (`AAIW`, `NADW`, `AABW` — keep); confirm each on the rendered page.

**Multi-line node labels** (`{340\\incoming}`): translate them like any node
text; `check_latin_prose.py` reads `\\` as a separator.

## Pre-run canon fixes (coordinator, 2026-10-26; line counts unchanged)

- **Accent escapes → UTF-8** (9 sites in the chapters, 5 names in the credits): `Réunion` ×3 and
  `Paraná` ×2 in `15-hotspots` (48, 349, 590, 608, 609), `Höfn` in
  `12-plate-kinematics` 721 and 929 and `solutions/12-plate-kinematics` 239,
  `PawełS` in `05-cross-sections` 513; `frontmatter/image-credits-book3.tex` (and
  your stand-in): `PawełS`, `Michel-Lévy`, `Mohorovičić`, `Þingvellir`,
  `Galápagos`.
- **Words moved out of `\qty` (9 sites)**: `\qty{365.25}{days}` → `\num{365.25}~days`
  (`20-erosion-transport` 749, 866 and `solutions/20` 5), `\qty{4000}{years}` →
  `\num{4000}~years` (`21-clastic-sediments` 1196, 1203), `\qty{12}{days}` and
  `\qty{3.2}{years}` (`solutions/10-heat-budget` 56, 57), and in math spans
  `\num{365.2425}\text{ days}` (`01-spherical-astronomy` 556),
  `\num{72}\text{ years}` (`solutions/20` 124), `\num{4000}\text{ years}`
  (`solutions/21` 162). The `\text{}` inside a math span is translatable
  (`id_apply`'s math census blanks it): *jours*, *ans*.
- **A `\crefname` for tables** in the style (above).
- Audited and clean: no `\qty` without a unit argument; no term defined twice
  (same `\index` key in two definitions); the 25 capitalised definition displays
  harvest correctly (every lowercase use is either linked or deliberately not —
  the "Diagenesis" count of 137 was an artefact of the label text); the
  line-edge sweeps on English (the 5 lines ending in an apostrophe are English
  possessive plurals or a math prime; harmless in English, and your French lines
  must not copy that shape); every `\cref` prefix has a `\crefname` after the
  table fix.

## The pipeline (as in Books 1–2)

1. **Write every body through `tools/id_apply.py`** — the translator writes only
   prose, as line-range replacements of the English twin; unnamed lines are
   copied byte-identically, and the write is refused unless labels, environments,
   solution keys, `\emph`/`\index` adjacency, math spans, `\ce`, drawing code,
   image paths, delimiters and braces match. Read its docstring. Line numbers
   refer to the English file with `\omterm` unwrapped
   (`python3 -c "import sys; sys.path.insert(0,'tools'); import id_apply as a; print(a.unwrap_omterm(open(F).read()))"`).
   `!draw` is **per range**: every range that changes drawing code needs its own
   `!draw`. **Do not machine-translate**: draft at native register directly.
   The coordinator verified (2026-10-26) that an identity patch (`@@ 1` with line
   1 unchanged) is accepted on all 58 files.
2. **Build with the wrapper every time a translated file has been created since
   the last build**; its `.fls` count must equal the number of files on disk.
3. **Gates**: `bash tools/check_translation.sh bachelor-1 fr`. Build log: errors,
   undefined, overfull all **0**; `nullfont` equal to the English baseline
   (below: **0** — unlike Books 1–2 there are no blank-line map tables, so any nullfont line is a real defect: an accent inside a unit, a lost glyph); non-backtick "Missing character" **0**; invalid-in-math **0**;
   "Discard zero height" **0**. Also `bash tools/gates.sh bachelor-1`.
4. **Term links**: curate `book3_fr.py` (`AMBIG_POLICY = "drop"`, as
   `book3_en.py`: a university book), then
   `python3 tools/link_defined_terms.py --book 3 --lang fr --unwrap --apply` and
   `--apply`; then the per-target **frequency** and **chapter-set** censuses from
   `translation_instruction.md` (both), the target-set diff against English, the
   `\index{}` key diff against English, the `\text{}` census over **course and
   solutions**, and `tools/check_term_display_drift.py`. English homographs of
   this book (from `book3_en.py`): *stable, extension, order, relief, series,
   system, stage, group, formation, member, flux, declination, trend, dip,
   strike, stretch, sorting, mineral*; plus Books 1–2's *fault, plate, front,
   bed, mantle, shield, cell, basin, scale, table, current, range, crust, core,
   trench, ridge, arc, delta, phase, cycle, season, mass, zone, spring, well,
   source*. French has its own — expect *plan* (plane / plan), *contrainte*
   (stress / constraint), *dilatation*, *déformation*, *faille*, *pendage*,
   *temps*, *champ*, *carte*, *pression*, *noyau*, *front*, *gisement*,
   *milieu*, *ordre*, *série*, *système*: find them with the two censuses and
   read every flagged site. **Capital-harvest**: 25 English definitions open with
   a capitalised term; if your translation also opens the sentence with the term,
   check that its lowercase occurrences still link (or reword, *On appelle
   \emph{x}…*), and check the case actually harvested before you STOP or DROP
   anything. `EXTRA` wins over `STOP`. Every protect starts `(?<!\w)`. A lookaround
   anchored on a word that is itself a linked term breaks silently: finish with
   the plain dry run.
5. **Native pass** until ≥ 95/100: openings, definitions, propositions and their
   proofs, exercise stems, solution headers, method boxes; the register measure.
6. **A scripted re-read of every solution against its question**, in French,
   before you score. Book 3 is computation-heavy (spherical trigonometry,
   gravity corrections, isostasy, heat flow, Euler poles, stress tensors, Mohr
   circles, isochrons, radiocarbon, Stokes settling, Ekman and Sverdrup
   transport): recompute along the rounded path a student follows; **report**
   English-canon slips to the coordinator with your arithmetic — never "fix" a
   number silently, and never assume a reported slip is real until it is checked
   against the figure, its data and the sibling answers.
7. **Last, measure — do not edit after measuring.** Re-run the line-edge sweeps
   (`['’]\s*$`, `^\s*([.,;:)?!]|~[;:?!])`, `[a-zà-ÿ]-\s*$`; rewrap, never end a
   line with `%`) after the final file lands, re-link, re-run both censuses, the
   dry run `python3 tools/link_defined_terms.py --book 3 --lang fr | grep 'links to insert'`
   (must print 0), every gate, then the forced build.
8. **Score** to `translation_scores/book_3/fr/translation_score.md` (model:
   `translation_scores/book_2/fr/translation_score.md`, including a "Conventions
   recorded" section, the register counts and the `!draw` list). Ship only at **≥ 95**.

## French notes (what earlier French editions got wrong)

- Never end a source line on an elision apostrophe: TeX prints `d' entropie`.
- A unit-less `\qty` followed by an accented word crashes the build; no accent
  inside any siunitx argument.
- `{1\textsuperscript{er}}`: brace `\textsuperscript` inside a pgfplots `axis`
  node (TeX Live 2026 kernel).
- Spaced punctuation `~:` `~;` `~?` `~!`, guillemets `«~…~»`, the decimal point
  and `\,` thousands as the series' siunitx setting does.
- Verify with TeX Live 2026 (`~/texlive/2026/bin/x86_64-linux` first in `PATH`):
  the system TeX Live 2022 has no `french.ldf`.
- Translated labels are longer: every earlier edition found collisions on
  rendered charts. Render every figure you touch and read each label against its
  own point; after a fix, render again.
- **Instruction register, history in the passé simple, `on` in course text**, as
  the university volumes of the sister series.

## Your report to the coordinator (final message)

Pages; `\omterm` links and distinct targets, and the targets English reaches that
you do not (with English's own count for each); every gate's result; the
build-log numbers; the `.fls` count; your score; **every English-canon defect you
suspect** (file, line, evidence, your arithmetic); **every gate or tool bug**
(including any allow-list entry you appended, with its reason); every `!draw`
range; every convention where you departed from Books 1–2 fr, and why.

## English baselines (measured 2026-10-26, after the pre-run canon fixes)

| | Book 3 |
|---|---:|
| files (body + solutions) | 29 + 29 |
| lines | 31,599 |
| pages (English PDF, TL 2026) | 475 |
| `\omterm` links | 4,654 (def 4,633, prop 16, thm 5) |
| distinct link targets | 184 |
| `nullfont` | **0** |
| `\index{}` | 449 |
| `\emph{}` | 587 |
| `\qty{}` | 5,028 |
| `% ledger:` comments | 734 |
| `\ce{}` | 366 |
| `\foreach` | 105 |
| `\legend`/`\addlegendentry` | 50 |
| `exercise` / `problem` / `solution` | 348 / 29 / 377 |
| `omfigure` / `tikzpicture` / `axis` / `\node` | 160 / 144 / 90 / 743 |
| `\label` / `\cref` | 1,010 / 460 |
| `definition` / `proposition` / `proof` / `theorem` | 193 / 127 / 136 / 22 |
| linker dry run, links to insert | 0 |
| `gates.sh bachelor-1` | green |

## Probe builds (2026-10-26, still-English bodies, through the wrapper)

| entry | pages | errors / undefined / overfull | nullfont | other Missing character | invalid-in-math |
|---|---:|---|---:|---:|---:|
| `en` | **475** | 0 / 0 / 0 | **0** | 0 | 0 |
| `fr` (pdfTeX, babel-french loaded) | 474 | 0 / 0 / 10 (all `in paragraph`: English prose under French hyphenation) | 0 | 0 | 0 |

The gates are therefore: **`nullfont` = 0**, **non-backtick Missing character = 0**,
**overfull = 0** at the end, **invalid-in-math = 0**, **zero-height = 0**, and the
`.fls` count = 58.

Controls run by the coordinator (2026-10-26) on a scratch copy of the English tree
passed off as French: gate 9 reports 640 `title`, 291 `node-1word` … hits; gate 10
reports 14,874 orphan English lines; a tampered `\ce` and a tampered ledger id each
trip gate 12; `id_apply --dry-run` accepts an identity patch on all 58 files.

## Toolchain changes for this run (coordinator, 2026-10-26)

- `one_earth_and_space_sciences_book_3_university_year_1_fr.tex` (derived from the
  French Book 2 entry), registered in `latexmkrc` and `release.yml`;
  `frontmatter/image-credits-book3.fr.tex` (English stand-in); the directories
  `parts/bachelor-1/fr` and `parts/bachelor-1/solutions/fr`; `book3_fr.py` stub;
  `LANGS[3] = ("en", "fr")` in `tools/termlink/books.py`.
- `styles/oneearth.sty` + `styles/lang/fr.tex`: `\crefname{table}` and the
  `\omnameTable`/`\omnameTables` strings (conditional on the language file
  defining them, so every other edition is byte-identical to before), and
  `\tablename` = *Tableau* for the caption label (babel-french's own string is
  *Table*, set again at `\begin{document}`, hence the `\captionsfrench` hook).
  A rendered caption reads *Tableau 7.1 – …*, as the `\cref` reads *Tableau 7.1*.
  Check one caption and one reference in your build. The other six languages
  still need the same two strings: a note for `WAVE1_FINDINGS_B3.md`.

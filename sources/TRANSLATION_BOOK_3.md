# Translation run — One Earth and Space Sciences Book 3 into nl, es, pt, hi, ar, id

The binding run file for the six remaining language editions of Book 3
(University Year 1, `parts/bachelor-1`): 29 chapters + 29 solution files =
**58 files, 31,599 lines**, ~475 pp in English. User request, 2026-10-27:
*"write the translations in Dutch, Spanish, Portuguese, Hindi, Indonesian and
Arabic of one earth and space sciences book 3 … batches of 4 books max … one sub
agent max per book."* One subagent owns each edition.

**Models (user rule 2026-10-27, recorded at launch):** every edition agent runs
`claude-haiku-5-5` (Haiku 5.5) at effort **high**; the coordinator runs
`claude-opus-5-5` (Opus 5.5). Write both lines in your score file; add the
coordinator's model only if the coordinator later edits your edition (it will
say so).

## Waves

| wave | editions | why together |
|---|---|---|
| 1 | `nl`, `es`, `pt`, `id` | the Latin-script editions (`check_latin_prose.py`; id also `check_indonesian_prose.py`) |
| 2 | `hi`, `ar` | the non-Latin editions; Arabic gains most from wave 1's fixes |

Wave 2 also reads `sources/WAVE1_FINDINGS_B3_W2.md`, which the coordinator
writes when wave 1 closes.

The French edition of Book 3 (`parts/bachelor-1/fr/`, shipped 2026-10-26, 96/100)
is your **sense and structure reference**, not your ceiling: read the French
chapter before drafting yours.

If you are an edition agent, this file and your brief are your instructions.
Read everything in "Reading list" before you write a line.

## Reading list (in this order, whole files)

1. `../CLAUDE.md` (workspace root) and `../book_style.md`.
2. `../translation_instruction.md` — **the whole file**, including every "Lessons
   from the … Earth and space translations" section at its end. Nearly every
   paragraph is a defect class some earlier edition shipped.
3. Your language's style card if it has one: `../hindi_style_card.md`,
   `../arabic_style_card.md` (§6 above all), `../indonesian_style_card.md`.
4. `CLAUDE.md` (its three "Language editions" sections above all),
   `CONTRIBUTING.md`, `OUTLINE.md` (the Book 3 chapter list) and
   `sources/SERIES_DEFINITIONS.md`.
5. `sources/TRANSLATION_BOOK_3_FR.md` (the French run file: every site list below
   comes from it) and **`sources/WAVE1_FINDINGS_B3.md`** (what French found).
6. `sources/TRANSLATION_BOOK_2.md`, `sources/WAVE1_FINDINGS_B2.md`,
   `sources/WAVE2_FINDINGS_B2.md` (Arabic: §3a, the leading-run rule).
7. This file. Where any earlier file disagrees with this one, **this file wins**.

## Your reference editions (read before drafting)

- **Your language's Books 1 and 2 of this series** — `parts/grade-{1..12}/<lang>/`,
  `translation_scores/book_{1,2}/<lang>/translation_score.md` (their
  **Conventions** sections) and `tools/term_config/book{1,2}_<lang>.py`. Book 3
  recalls ~all of their notions (*plate, ridge, trench, isobar, front, water
  cycle, rock cycle, isostasy, heat flow, P/S wave, Moho, thin section …*): grep
  them before choosing a word. **Keep every convention they recorded**: compass
  and hemisphere letters (already in `styles/lang/<lang>.tex`), coordinate
  notation, place-name exonyms, likelihood words of the climate chapters, box
  names, solution headers, the data-line wording, the article before `\cref`. A
  disagreement with Books 1–2 is reported, not made silently.
- **The register of a university course.** Book 3 is the first university year
  (18–19 years): a lecture-and-textbook voice, no longer the high-school voice
  of Book 2. **Measure the instruction register of your exercise stems against
  your language's University Year 1 editions of the sister series before you
  score, and convert as a reviewed pass, never a regex**:
  `../one-physics-book/parts/bachelor-1/<lang>/`,
  `../one-biology-book/parts/bachelor-1/<lang>/`,
  `../one-chemistry-book/parts/bachelor-1/<lang>/` and their score files
  (`translation_scores/book_3/<lang>/` in physics and biology, `book_2/<lang>/`
  in chemistry). Count what they do (e.g. Spanish impersonal *se* vs *tú*
  imperative; Dutch *je* vs *u*; Portuguese *você* imperative; Hindi आप/-इए;
  Indonesian bare imperative; Arabic second-person vs impersonal) and follow
  them; state the counts in your score file.
- **Terms a sister series owns** — physics (energy, radiation, pressure, waves,
  heat transfer, black body, spectra), chemistry (every `\ce` species, isotopes,
  solutions, pH, redox, equilibrium, ionic potential), biology (carbonate
  producers, life): use the rendering your language's edition of that series
  already uses (`grep` its `parts/**/<lang>/`) and report a disagreement instead
  of diverging silently.

## Hard rules (all binding)

1. **You own exactly one edition.** You write only:
   - `parts/bachelor-1/<lang>/*.tex` and `parts/bachelor-1/solutions/<lang>/*.tex`;
   - `tools/term_config/book3_<lang>.py` (a stub is waiting — curate it from YOUR
     edition's harvest, never by translating `book3_en.py`/`book3_fr.py` and
     never by copying `book2_<lang>.py`: Book 2's EXTRA values are Book 2 labels,
     its protects another book's judgement — re-verify each entry you reuse);
   - `translation_scores/book_3/<lang>/translation_score.md`;
   - `frontmatter/image-credits-book3.<lang>.tex` (an English stand-in now: keep
     every photograph credit, author name, dataset name and licence exactly;
     translate the frame and the descriptions; the model is your
     `frontmatter/image-credits-book2.<lang>.tex`; the preface
     `frontmatter/preface.<lang>.tex` is shared and already done — do not touch it);
   - your entry file's `\bookline` and `\author` lines only
     (`one_earth_and_space_sciences_book_3_university_year_1_<lang>.tex`; the
     coordinator wrote a `\bookline` modelled on Book 2's — correct it if it is
     not idiomatic, and say so).
   `styles/lang/<lang>.tex` already carries the Book 3 strings (tables, below); if
   a string is missing or wrong for Book 3, report it.
2. **Never edit the English canon** (`parts/bachelor-1/*.tex`, `solutions/*.tex`),
   the French edition, the style file, shared tools, other books' files or another
   language's files. A canon defect is REPORTED to the coordinator with file, line
   and evidence; the coordinator verifies it against the book's own model (the
   figure, its data, the sibling answers) and fixes it, then sends every running
   agent the exact old and new text to mirror. Work around a defect in your
   edition only if the fix is obvious and local, and say so.
3. **Never run a repo-wide git command** — no `git checkout -- .`, `git restore`,
   `git stash`, `git clean`, `git reset`. The repo holds the coordinator's
   uncommitted work, the French edition and three other agents' editions; on
   Biology Book 4 one such command destroyed every uncommitted change in the repo,
   and `git clean` would delete every translated file. To undo your own work,
   rewrite that specific file. **Never commit.** Read-only git (`git diff`,
   `git status`, `git log`) is fine. Never wildcard-`rm`; delete scratch files by
   name.
4. **Shared tools are shared.** `tools/check_*_prose.py`, `tools/id_apply.py`,
   `tools/check_translation.sh`, `tools/check_orphan_lines.py`,
   `tools/check_chem_twin.py`, `tools/termlink/*`, `styles/*`: report bugs
   instead of editing. The one exception is a per-language allow-list entry
   (`ALLOWED_BY_LANG["<lang>"]` in `check_latin_prose.py`, or the equivalent
   allow-list of your script gate), **append-only, with a comment giving the
   reason and "Book 3 <lang>"**, placed BEFORE any `if __name__ == "__main__"`
   guard, and run once to confirm it changed the output. An agent that rewords
   correct prose to satisfy a gate has found a gate bug: report it.
5. **Scratch files go in your PRIVATE directory**
   `/tmp/claude-1000/-home-bvirrion-repositories-one-course/a9157bf7-58d5-404b-ae29-1d263a897841/scratchpad/<lang>3/`
   (patch files, probes, helper scripts). Four agents share the scratchpad: never
   write outside your own subdirectory. Keep your patch files: they are the only
   record of a chapter before `id_apply` writes it. `/tmp` has been wiped mid-run
   before: after every chapter written, the chapter on disk is the record.
6. **Resources** (the user's 19 GB laptop, shared by up to four agents):
   - **every full-book build goes through the wrapper**
     `bash /tmp/claude-1000/-home-bvirrion-repositories-one-course/a9157bf7-58d5-404b-ae29-1d263a897841/scratchpad/build.sh one_earth_and_space_sciences_book_3_university_year_1_<lang> <lang>-<n>`
     — TeX Live 2026 (as CI), forces `-g`, holds ONE machine-wide build slot
     (you may wait for another agent's build: that is normal), caps memory,
     builds into the scratchpad (not the repo) and prints pages / errors /
     undefined / overfull / nullfont / non-backtick "Missing character" /
     invalid-in-math, the `.fls` count against the files on disk, and "Discard
     zero height". A build takes 6–15 minutes plus queueing: **run it with
     `run_in_background`**. Never call `latexmk` on a whole book directly, never
     `make`, never build a book that is not yours. Build sparingly: after a batch
     of chapters, not after each one;
   - for overfull work, `\input` a single chapter into a probe of the book's
     preamble (seconds) instead of rebuilding the book; write the probe into your
     private directory and run it from the repo root with
     `PATH=$HOME/texlive/2026/bin/x86_64-linux:$PATH`, `nice -n 19`, and the same
     engine and `-cnf-line` memory flags as `latexmkrc` (hi: XeLaTeX, ar:
     LuaLaTeX, the rest pdfLaTeX);
   - every other long job: `nice -n 19`, `OMP_NUM_THREADS=1`, one at a time;
     never run the repo's pytest suite.
7. **Never name a programme** (no "licence", "L1", "BCPST", "grado en Geología",
   "bachelor geologie", "S1 Geologi", no year or version of a national
   syllabus). The part title is in the shared `styles/lang/<lang>.tex` and is not
   yours; an ordinary stage noun for the reader's age (*universiteit,
   universidad, universidade, विश्वविद्यालय, الجامعة, universitas*) is fine.
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
  your language's chemistry edition.
- **Code arguments stay byte-identical**: `\omwx{…}`, `\omlith{…}`, `\omve{N}`,
  every `lith <rock>` / `om lith` style, every pic, every figdata path.
- **New in Book 3**: `lemma` (1) and `notation` (1) heads (strings already in
  your `styles/lang/<lang>.tex`); `table` with `\caption` (12) and
  **`\cref{tab:…}` (27)** — the coordinator added `\omnameTable`/`\omnameTables`
  and the caption word `\tablename` to every language file on 2026-10-27 (nl
  *Tabel*, es *Tabla*, pt *Tabela*, hi *तालिका*, ar *جدول*, id *Tabel*); check one
  rendered caption and one rendered reference in your build. Also `groupplot` (3),
  `pmatrix` (6, in math), `description` (1), `\si{}` (37, legacy siunitx),
  `\admitted` (13, a style macro that prints its own localised string: nothing to
  translate), `\textquoteleft` (the Hawaiian *ʻokina* of *Puʻu ʻŌʻō*: keep), the
  units `\sverdrup`, `\gal`, `\mag`, `\angstrom`, `\dex`, `\darcy` (frozen).
- **Units — decided before the run (WAVE1_FINDINGS_B3 §2.2).** Never a non-ASCII
  character or a word inside `\qty{}`, `\unit{}`, `\num{}`. The canon's unit words
  *days*/*years* were moved out of every `\qty` before the French run, so you
  write them in your language.
  - **nl, es, pt, hi, ar**: keep English's units exactly, as your Books 1–2 do —
    `Ma` for a date, `Myr` for a duration, `Gyr`, `yr` — in prose and in
    formulas. Every unit argument stays byte-identical to English. Nothing to
    convert.
  - **id**: as Indonesian Books 1–2, **Ma for dates AND durations, Ga for a
    billion years**, and `yr` kept (`mm/yr`, as Book 2 id). Draft with the
    English unit arguments byte-identical (so every patch passes the `math`
    census), then, **after your last chapter lands**, run ONE scripted
    conversion over your own 58 files only: `\Myr` → `\Ma`, unit-string `Myr` →
    `Ma`, `Gyr` → `Ga`, inside `\qty`/`\unit`/`\si` unit arguments and nowhere
    else. Put the lookbehind AFTER the optional backslash (the French pass's
    `(?<![A-Za-z])\\?Myr` matched `\per\Myr` at the `M` and printed `\per\\Ma`),
    then `grep -rn '\\\\[MG]a' parts/bachelor-1/id parts/bachelor-1/solutions/id` (a doubled backslash before Ma/Ga) must print nothing; then `check_chem_twin`,
    gates, build. Prose words for durations (*juta tahun*) are yours to choose
    as Book 2 id did. List the conversion in the score file; the coordinator
    diffs your math spans against English afterwards and expects only unit swaps.
- **Compass, hemisphere and coordinate letters**: keep Books 1–2's convention
  exactly (`\omnameCompass*` in your language file). Book 3 adds coordinates in
  tick labels, in the weather-map labels and in tables.
- **Place names** take your language's established exonym; institutions,
  datasets, missions and model names keep their proper names (USGS, NOAA,
  GISTEMP, ETOPO1, PB2002, PREM, MORVEL, ICS, …), with any descriptive gloss
  translated. Titles of papers and any gloss a translator adds to them **never
  link** (protect them).
- **Observation only**: the canon never sends the reader to a quarry, a cliff, a
  cave, a volcano or a river in flood, never has them hammer a rock or look at
  the Sun. Keep that true in your wording (gate 7b). The optical-mineralogy and
  spherical-astronomy chapters use a polarising microscope and a telescope in the
  lab or the observatory, as in the canon.
- **Physical science only on climate** (ch. 26–29): no policy wording.
- **Spherical astronomy and angle notation.** Chapters 1–2 write hours, minutes
  and seconds, declinations and altitudes with `\ang{}` and a small family of
  custom macros; the degrees/hours notation inside math is frozen; the terms
  (altitude, azimuth, declination, right ascension, hour angle, sidereal time,
  equation of time, meridian, zenith, nadir, ecliptic, equinox, solstice) follow
  your language's astronomical usage (your physics edition is the reference).

## Visible text that is NOT an ordinary prose line — every site, with its line

**`\foreach` lists with visible words** (compared byte for byte by `id_apply`'s
`draw` census, so translating one costs an `@@ N-M !draw` on that range — record
each in the score file and check the list by eye; translate only the visible
fields, keep numbers, colours, node names). **Verify each by eye in the rendered
figure, and look for any missed** (a list of single capital letters is code):

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

**`symbolic x/y coords` keys are code.** `23-diagenesis-basins` 188
(`{buried, surface}`) and `25-radiometric-methods` 567 (ten closure-chart keys)
are ASCII keys matched to figdata columns and are never printed (the axis prints
its `xticklabels`/`yticklabels`, which you translate). Keep the keys
byte-identical (non-ASCII in a symbolic coordinate is a fatal build abort). The
coordinator taught `check_latin_prose.py` on 2026-10-27 to skip such keys when
the axis has explicit tick labels, so no allow-list entry is needed for them.

**Figdata tables whose text reaches the page** — the only ones in Book 3:
`24-stratigraphic-scale` 589–601, the ICS chart: `bachelor-1-ics_chart-eras.dat`
(*Paleozoic, Mesozoic, Cenozoic*), `-periods.dat` (the eleven period names),
`-events.dat` (*end-Permian, end-Cretaceous*), and the node at 602 (*Quaternary*).
Replace each `meta=name` plot by explicit nodes coordinate by coordinate, under a
per-range `!draw`, using the `.dat` coordinates — **the French edition already did
exactly this: read `parts/bachelor-1/fr/24-stratigraphic-scale.tex` and mirror its
structure** — then **render the page and check every label against its band.**
The other `meta=` tables hold numbers (`05` varden labels, `26` isopycnal values,
`28` pressure labels, `03` temperatures), ion formulas (`19`, `Cs$^{+}$`) or
acronyms (`AAIW`, `NADW`, `AABW` — keep); confirm each on the rendered page.

**Multi-line node labels** (`{340\\incoming}`): translate them like any node
text; `check_latin_prose.py` reads `\\` as a separator.

## Pre-run canon state

Every canon fix of the French run is already in the English files you read
(`WAVE1_FINDINGS_B3.md` §1: accent escapes, unit words out of `\qty`, three double
roundings, the *voting members* protect). The French edition's own reports that
were checked and left are listed there too — do not re-report them.

One more canon edit, made in Step 0 of this run (and mirrored into the French
edition): `02-observing-the-sky` line 77, the spectrum `\foreach`, `4/1 \textmu m,
6/100 \textmu m,` → `4/1 \unit{\micro m}, 6/100 \unit{\micro m},` (the hi/ar
faces have no µ glyph; siunitx's `\micro` prints in every edition). Any later
canon edit is sent to you verbatim (old → new text) by the coordinator: mirror it
in your edition at once.

## The pipeline (as in Books 1–2)

1. **Write every body through `tools/id_apply.py`** — the translator writes only
   prose, as line-range replacements of the English twin; unnamed lines are
   copied byte-identically, and the write is refused unless labels, environments,
   solution keys, `\emph`/`\index` adjacency, math spans, `\ce`, drawing code,
   image paths, delimiters and braces match. **Read its docstring first.** Line
   numbers refer to the English file with `\omterm` unwrapped
   (`python3 -c "import sys; sys.path.insert(0,'tools'); import id_apply as a; print(a.unwrap_omterm(open(F).read()))"`).
   `!draw` is **per range**: every range that changes drawing code needs its own
   `!draw`. For hi/ar/id, `id_apply` also runs your script's prose gate on the
   written file, so a range you forgot is refused. **Do not machine-translate**:
   draft at native register directly. A patch file holds many files: work one
   chapter (body + its solutions) at a time, write it, check it, move on. The
   coordinator verified (2026-10-27) that an identity patch is accepted by every
   structural census on all 58 files for all six languages.
   - **Work chapter by chapter in the canon's order**, and translate EVERY prose
     line of a chapter before you move on: an absorbed or skipped line is copied
     through as English, and gates 9/10 will fail it later.
   - **A chapter is not done until its FIGURE TEXT is done too** (added
     2026-10-27, wave 1): node labels, `\legend`/`\addlegendentry`, tick-label
     keys, axis labels, visible `\foreach` fields, the ICS chart. Translate them in
     the same pass as the prose (the census blanks most of them; `\foreach` needs
     its per-range `!draw`) and run `check_latin_prose.py` (or your script gate)
     on the chapter before moving on: its `node`/`legend`/`foreach` classes must
     be empty for that chapter. A first pass that leaves every figure English
     costs a second pass over the whole book.
   - **One cumulative patch per file** (wave 1): `id_apply` rebuilds a file from
     the English twin plus the ranges in the patch, so a later patch holding only
     some ranges silently puts English back everywhere else. Keep ONE patch file
     per chapter file, edit it, and re-apply it whole.
   - **Context economy**: read each English chapter once, in chunks; keep tool
     output short (`--quiet`, `| tail`); don't re-read finished files. If you
     must stop before the end, write a PROGRESS file in your private dir first
     (what is done, what is next, every `!draw` range) so the coordinator can
     resume you.
2. **Build with the wrapper every time a translated file has been created since
   the last build**; its `.fls` count must equal the number of files on disk.
3. **Gates**: `bash tools/check_translation.sh bachelor-1 <lang>`. Build log:
   errors, undefined, overfull all **0**; `nullfont` **0** (Book 3 has no
   blank-line map tables, so any nullfont line is a real defect: an accent inside
   a unit, a lost glyph); non-backtick "Missing character" **0**;
   invalid-in-math **0**; "Discard zero height" **0**. Also
   `bash tools/gates.sh bachelor-1`.
4. **Term links**: curate `book3_<lang>.py` (`AMBIG_POLICY = "drop"`, as
   `book3_en.py`: a university book), then
   `python3 tools/link_defined_terms.py --book 3 --lang <lang> --unwrap --apply`
   and `--apply`; then the per-target **frequency** and **chapter-set** censuses
   from `translation_instruction.md` (both), the target-set diff against English,
   the `\index{}` key diff against English, the `\text{}` census over **course and
   solutions**, and `tools/check_term_display_drift.py`. English homographs of
   this book (from `book3_en.py`): *stable, extension, order, relief, series,
   system, stage, group, formation, member, flux, declination, trend, dip,
   strike, stretch, sorting, mineral*; plus Books 1–2's *fault, plate, front,
   bed, mantle, shield, cell, basin, scale, table, current, range, crust, core,
   trench, ridge, arc, delta, phase, cycle, season, mass, zone, spring, well,
   source*. Your language has its own: find them with the two censuses and read
   every flagged site. French found *groupe de travail* / *le groupe a proposé*
   (→ lithostratigraphic *group*) and *membres votants* (→ *member*): **the same
   two phrases in your language will collide the same way** — protect them.
   **Capital-harvest**: 25 English definitions open with a capitalised term; if
   your translation also opens the sentence with the term, check that its
   lowercase occurrences still link (or reword so the term is not
   sentence-initial), and check the case actually harvested before you STOP or
   DROP anything. Welded compounds (Dutch above all) are skipped by `harvest.py`
   (no space): recover each missing English target with `EXTRA`. `EXTRA` wins
   over `STOP`. Every protect starts `(?<!\w)`. A lookaround anchored on a word
   that is itself a linked term breaks silently: finish with the plain dry run.
5. **Native pass** until ≥ 95/100: openings, definitions, propositions and their
   proofs, exercise stems, solution headers, method boxes; the register measure.
6. **A scripted re-read of every solution against its question**, in your
   language, before you score. Book 3 is computation-heavy (spherical
   trigonometry, gravity corrections, isostasy, heat flow, Euler poles, stress
   tensors, Mohr circles, isochrons, radiocarbon, Stokes settling, Ekman and
   Sverdrup transport): recompute along the rounded path a student follows;
   **report** English-canon slips to the coordinator with your arithmetic —
   never "fix" a number silently, and never assume a reported slip is real until
   it is checked against the figure, its data and the sibling answers (the four
   French reports left as correct are in `WAVE1_FINDINGS_B3.md` §1).
7. **Last, measure — do not edit after measuring.** Re-run the line-edge sweeps
   (`['’]\s*$` excluding the closing `''`, `^\s*([.,;:)?!]|~[;:?!])`,
   `[a-zà-ÿ]-\s*$`; rewrap, never end a line with `%`) after the final file lands,
   re-link, re-run both censuses, the dry run
   `python3 tools/link_defined_terms.py --book 3 --lang <lang> | grep 'links to insert'`
   (must print 0), every gate, then the forced build.
8. **Score** to `translation_scores/book_3/<lang>/translation_score.md` (model:
   your `translation_scores/book_2/<lang>/translation_score.md`, including a
   "Conventions recorded" section, the register counts, the `!draw` list and the
   **model line**). Ship only at **≥ 95**.
9. **Render and read** (not optional): every figure page you changed text in, at
   ~110–130 dpi (`pdftoppm -r 120 -f N -l N`), each label against its own point;
   one table caption and one `\cref{tab:…}`; the ICS chart; after any label fix,
   render again.

## Language notes

- **nl** — informal *je* or formal *u*: measure the Dutch University Year 1
  editions and follow them. Welded compounds cost targets (EXTRA). Dutch exposes
  `'s`/`'t` at line ends (sweep). `WORD_TAIL` manufactures homographs (*leveren*
  from *lever*): read your `lang_nl.py` before curating.
- **es** — impersonal *se* in course text; the exercise-stem register as the
  Spanish University Year 1 editions do it. Spanish *tiempo* = time and weather.
  The `-se` passive agrees with its object; six nouns are spelled like the
  imperative (*nombre, cierre, cruce, contraste, ajuste, apunte*).
- **pt** — Brazilian Portuguese only (*você*, *-ção*, Brazilian spelling).
- **id** — the unit conversion above; `TAIL_AFTER_S` and *-nya*; split
  reduplication at a line end breaks the linker (hyphen sweep); `check_indonesian_prose.py`
  runs inside `id_apply` and in gate 8.
- **hi** — XeLaTeX; `hindi_style_card.md`; आप register measured against the
  Hindi University Year 1 editions; Devanagari emphasis is weight, not italic;
  `harvest.py` cannot harvest a display from a statement environment in a
  non-Latin script unless it carries an adjacent `\index{}` (check the target
  diff).
- **ar** — LuaLaTeX, `bidi=basic`; `arabic_style_card.md` §6, Books 1–2's Arabic
  notes (`TRANSLATION_BOOK_2.md` "Arabic notes", `WAVE2_FINDINGS_B2.md` §3a):
  - a leading number, Latin word, `\ang` or `\qty{…}{\degree}` reverses at the
    start of `\foreignlanguage{arabic}{…}` in a one-line node, tick label, legend
    entry, axis label/title, or table cell (15 → 51, "°60"): box the leading run
    only, `\mbox{\textdir TLT …}`; `$…$` and `\num` are safe;
  - mixed node lines need `\foreignlanguage{arabic}{…}` line by line; Latin runs
    in axis labels need `\babelsublr{…}`;
  - inline matrices/arrays in INLINE math reverse their cells
    (`\babelsublr{$…$}`); Book 3 has 6 `pmatrix` — check each rendered;
  - **tables are new**: read every rendered table (cells, column order right to
    left, brackets);
  - before closing: scan the PDF for pages whose only text is the running header
    and the page number; grep the log for "Discard zero height";
  - confirm direction with `pdftotext -bbox` glyph x-positions, not by eye.

## Your report to the coordinator (final message)

Pages; `\omterm` links and distinct targets, and the targets English reaches that
you do not (with English's own count for each); every gate's result; the
build-log numbers; the `.fls` count; your score; **every English-canon defect you
suspect** (file, line, evidence, your arithmetic); **every gate or tool bug**
(including any allow-list entry you appended, with its reason); every `!draw`
range; every `--force-classes` use (there should be none); every convention where
you departed from your Books 1–2, and why. Keep it under ~80 lines.

## English baselines (measured 2026-10-27, Step 0)

| | Book 3 |
|---|---:|
| files (body + solutions) | 29 + 29 |
| lines | 31,599 |
| pages (English PDF, TL 2026) | 475 |
| `\omterm` links | 4,650 |
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
| French edition (reference) | 496 pp, 4,468 links / 185 targets |

## Probe builds (2026-10-27, still-English bodies, through the wrapper)

| entry | engine | pages | errors / undefined / overfull | nullfont | other Missing character | invalid-in-math | zero-height |
|---|---|---:|---|---:|---:|---:|---:|
| `en` | pdfTeX | **475** | 0 / 0 / 0 | **0** | 0 | 0 | 0 |
| `nl` | pdfTeX + babel-dutch | 475 | 0 / 0 / 0 | 0 | 0 | 0 | 0 |
| `es` | pdfTeX + babel-spanish | 474 | 0 / **1** / 8 | 0 | 0 | 0 | 0 |
| `pt` | pdfTeX + babel-brazilian | 475 | 0 / 0 / 2 | 0 | 0 | 0 | 0 |
| `id` | pdfTeX + babel-bahasai | 475 | 0 / 0 / 1 | 0 | 0 | 0 | 0 |
| `hi` | XeLaTeX | 499 | 0 / 0 / 57 | 0 | 2 → **0** | 0 | 0 |
| `ar` | LuaLaTeX | 492 | 0 / 0 / 8 | 0 | 2 → **0** | 0 | 0 |

- Every overfull box of the probes is `in paragraph`: English prose under another
  language's hyphenation or script face. None is a fixed-width box.
- **es "undefined 1" is not a reference.** It is `LaTeX Font Warning: Font shape
  T1/lmr/bx/sc undefined` from the table of contents: babel-spanish prints the
  Part's roman numeral in small caps, and the ToC's Part line is bold. LaTeX falls
  back to bold upright; Books 1–2 es ship the same. **The es baseline is
  therefore 1 on the wrapper's `undefined` count**, and every other undefined
  line must be 0 (`grep -a 'undefined' <log> | grep -v 'Font shape'`).
- hi/ar "Missing character µ" came from `\textmu` in the ch. 2 spectrum
  `\foreach` (line 77), which the Devanagari and Naskh faces lack. Fixed in the
  canon before the run (below); a single-chapter probe now prints µm in hi and en.
- Rendered and read: the table caption and `\cref{tab:…}` in every language
  (*Tabel 7.1*, *Tabla 7.1*, *Tabela 7.1*, *Tabel 7.1*, *तालिका 7.1*, *جدول 7.1*,
  caption separator a colon).
- **Arabic, table cells:** the English-bodied probe shows table cells laid out
  right to left with **numeric ranges reversed** ("4.39–3.28" for 3.28–4.39,
  "°93 two" in ch. 7's mineral table). Every Arabic table cell that starts with
  or holds a number range needs the leading-run box; read every table rendered.

## Toolchain changes for this run (coordinator, 2026-10-27)

- Six entry files `one_earth_and_space_sciences_book_3_university_year_1_<lang>.tex`,
  each derived from the same language's Book 2 entry (Arabic keeps its
  `\emergencystretch`), registered in `latexmkrc` and `release.yml`;
  `frontmatter/image-credits-book3.<lang>.tex` (English stand-ins); the
  directories `parts/bachelor-1/<lang>` and `parts/bachelor-1/solutions/<lang>`;
  `book3_<lang>.py` stubs; `LANGS[3] = LANGS[1]` in `tools/termlink/books.py`.
- `styles/lang/{nl,es,pt,hi,ar,id}.tex`: `\omnameTable`/`\omnameTables` (for the
  style's conditional `\crefname{table}`) and `\tablename` plus the babel
  `\captions<language>` hook, so the caption and the reference agree.
- `tools/check_latin_prose.py`: `symbolic x/y coords` keys are skipped when the
  same axis gives explicit tick labels for that direction (lenient only).
- The hi/ar/id prose gates were checked on the siunitx option shape
  (`\qty[text-series-to-math=true]`, `\qty[uncertainty-mode=separate]`): silent on
  target-language prose, firing on English.

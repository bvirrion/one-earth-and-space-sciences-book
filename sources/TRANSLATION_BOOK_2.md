# Translation run — One Earth and Space Sciences Book 2 into fr, nl, es, pt, hi, ar, id

The binding run file for the seven language editions of Book 2 (High School,
grades 10–12, `parts/grade-10` … `parts/grade-12`): 28 chapters + 28 solution
files = **56 files**, ~23,000 lines, 362 pp in English. User request,
2026-10-25: one subagent per edition, **at most four at a time** (4 then 3).

This is the second volume of this series to be translated. Book 1 (grades 1–9)
shipped in all seven languages on 2026-10-25 with this same toolchain: its run
file `sources/TRANSLATION_BOOK_1.md` and `sources/WAVE1_FINDINGS.md` are
**still binding** wherever this file does not say otherwise. Where they
disagree, **this file wins**.

If you are an edition agent, this file and your brief are your instructions.
Read everything in "Reading list" before you write a line.

## Waves

| Wave | Editions | Notes |
|---|---|---|
| 1 | `fr` `nl` `es` `pt` | first readers of the Book 2 canon; share gate 9; `fr` becomes the sense twin |
| 2 | `hi` `ar` `id` | inherit the fixed canon, the gate fixes and the French twin; each has its own prose gate |

Between the waves the coordinator re-measures every delivered edition on its
own forced build, verifies and fixes reported canon defects (propagating each
fix into the delivered editions), fixes gate bugs (lenient fixes only while
agents hold patches), re-measures the English baselines and writes
`sources/WAVE1_FINDINGS_B2.md`. **Every wave-2 agent reads it before starting.**

## Reading list (in this order, whole files)

1. `../CLAUDE.md` (workspace root) and `../book_style.md`.
2. `../translation_instruction.md` — **the whole file**, including "Lessons
   from the first Earth and space translations" at its end. Nearly every
   paragraph is a defect class some earlier edition shipped.
3. Your language's style card: `../hindi_style_card.md`,
   `../arabic_style_card.md` or `../indonesian_style_card.md`. The Latin four
   have none: your language's shipped editions (below) are your style
   reference.
4. `CLAUDE.md` (its "Language editions" section above all), `CONTRIBUTING.md`
   and `OUTLINE.md` of this repo, and `sources/SERIES_DEFINITIONS.md`.
5. `sources/TRANSLATION_BOOK_1.md`, then `sources/WAVE1_FINDINGS.md` (Book 1's
   wave-1 lessons: per-range `!draw`, figdata label tables, the link layer).
6. This file, then `sources/WAVE1_FINDINGS_B2.md` if it exists.

## Your reference editions (read before drafting)

- **Your language's Book 1 edition of THIS series** —
  `parts/grade-{1..9}/<lang>/`, `translation_scores/book_1/<lang>/translation_score.md`
  (its **Conventions** section) and `tools/term_config/book1_<lang>.py`. Book 2
  is its continuation for 15–18-year-olds. **Keep every convention Book 1
  recorded**: compass and hemisphere letters (already in `styles/lang/<lang>.tex`),
  coordinate notation, place-name exonyms, the rendering of every term Book 1
  owns (Book 2 recalls ~all of Book 1's notions: *plate, ridge, trench,
  isobar, front, water cycle, rock cycle …* — grep your Book 1 edition before
  choosing a word), box names, solution headers. A disagreement with Book 1 is
  reported, not made silently.
- **Your language's high-school editions of the sister series** for register:
  `../one-biology-book/parts/grade-1{0,1,2}/<lang>/` (Biology Book 2, the same
  three grades) and `../one-physics-book/parts/grade-1{0,1,2}/<lang>/` if
  present. **Measure the instruction register of your exercise stems against
  Biology Book 2 and your Book 1 edition before you score**, and convert as a
  reviewed pass, never a regex. The register here is a lycée/high-school
  textbook: clear, precise, no longer the grade-1 voice.
- Terms a sister series owns (physics: energy, radiation, pressure, waves,
  heat transfer; chemistry: every `\ce` species, isotopes, solutions, pH,
  oxidation; biology: photosynthesis, life): use the rendering your language's
  edition of that series already uses (`grep` its `parts/**/<lang>/`); report a
  disagreement instead of diverging silently.
- Wave 2 also has this book's French edition as the sense and structure
  reference (not the ceiling).

## Hard rules (all binding)

1. **You own exactly one edition.** You write only:
   - `parts/grade-1{0,1,2}/<lang>/*.tex` and `parts/grade-1{0,1,2}/solutions/<lang>/*.tex`;
   - `tools/term_config/book2_<lang>.py` (a stub is waiting — curate it from
     YOUR edition's harvest, never by translating `book2_en.py` and never by
     copying `book1_<lang>.py`: Book 1's EXTRA values are Book 1 labels, its
     protects are another book's judgement — re-verify each entry you reuse);
   - `translation_scores/book_2/<lang>/translation_score.md`;
   - `frontmatter/image-credits-book2.<lang>.tex` (an English stand-in now:
     keep every photograph credit, author name, dataset name and licence
     exactly; translate the frame and the descriptions; the preface
     `frontmatter/preface.<lang>.tex` is shared with Book 1 and is already
     done — do not touch it);
   - your entry file's `\bookline` and `\author` lines only, if you want to
     improve the coordinator's wording (it must name a school stage, never a
     programme).
   Nothing in `styles/lang/<lang>.tex` should need to change; if a string is
   missing or wrong for Book 2, report it.
2. **Never edit the English canon** (`parts/grade-*/*.tex`, `solutions/*.tex`),
   the style file, shared tools, Book 1 files or another language's files. A
   canon defect is REPORTED to the coordinator with file, line and evidence;
   the coordinator verifies it against the book's own model (the figure, its
   data, the sibling answers) and fixes it. Work around it in your edition only
   if the fix is obvious and local, and say so.
3. **Never run a repo-wide git command** — no `git checkout -- .`,
   `git restore`, `git stash`, `git clean`, `git reset`. The repo holds the
   coordinator's uncommitted Step-0 work and four agents' untracked editions;
   on Biology Book 4 one such command destroyed every uncommitted change in the
   repo, and `git clean` would delete every translated file. To undo your own
   work, rewrite that specific file. **Never commit.** Read-only git
   (`git diff`, `git status`, `git log`) is fine.
4. **Shared tools are shared.** `tools/check_*_prose.py`, `tools/id_apply.py`,
   `tools/check_translation.sh`, `tools/check_orphan_lines.py`,
   `tools/check_chem_twin.py`, `tools/termlink/*`, `styles/*`: report bugs
   instead of editing. The one exception is a per-language allow-list entry
   (`ALLOWED_BY_LANG[<lang>]` in `check_latin_prose.py`; the `ALLOWED_WORDS` /
   `NOT_GATED` blocks of your script's own gate), **append-only, with a comment
   giving the reason and "Book 2 <lang>"**, placed BEFORE any
   `if __name__ == "__main__"` guard, and run once to confirm it changed the
   output. An agent that rewords correct prose to satisfy a gate has found a
   gate bug: report it.
5. **Scratch files go in your PRIVATE directory**
   `/tmp/claude-1000/-home-bvirrion-repositories-one-course/19132ca1-6889-4a73-b873-4fc92dbcdaad/scratchpad/<lang>2/`
   (e.g. `fr2/`, `hi2/`). Four agents share the parent folder; a file named
   `p/07.patch` there will be overwritten by someone else's. Keep your patch
   files: they are the only record of a chapter before `id_apply` writes it.
6. **Resources** (the machine is the user's 19 GB laptop, four agents at once):
   - **every full-book build goes through the shared wrapper**
     `bash /tmp/claude-1000/-home-bvirrion-repositories-one-course/19132ca1-6889-4a73-b873-4fc92dbcdaad/scratchpad/build.sh <your-entry-file>`
     — it forces `-g`, holds one of two machine-wide build slots (waiting for
     a free one), caps memory, and prints pages / errors / undefined /
     overfull / nullfont / non-backtick "Missing character" / invalid-in-math
     and the `.fls` count against the files on disk. A build takes 3–6
     minutes, more when it queues: **run it with `run_in_background`**. Never
     call `latexmk` on a whole book directly, never `make`, never build a book
     that is not yours;
   - for overfull work, `\input` a single chapter into a probe of the book's
     preamble (seconds) instead of rebuilding the book; write the probe into
     your private directory and run it from the repo root with the same
     `-cnf-line` memory flags as `latexmkrc`;
   - every other long job: `nice -n 19`, `OMP_NUM_THREADS=1`, one at a time;
     never run the repo's pytest suite.
7. **Never name a programme** (no "seconde", "première S", "terminale" as a
   curriculum, "SVT", "enseignement scientifique", "havo/vwo", "bachillerato
   LOMLOE", "BNCC", "CBSE", "SMA kurikulum", …); an ordinary school-stage noun
   for the reader's age is fine (the shipped `\bookline`s use them).
8. **Labels never translate**: `\label`, `\cref`/`\ref`/`\pageref` targets,
   `\begin{solution}{key}`, the first argument of `\omterm`, file names, image
   paths, figdata table paths, TikZ node names, colours, styles, pic names,
   pgfmath macro names (`\W`, `\H`, `\dx` …).

## Earth and space conventions (as in Book 1, plus what is new in Book 2)

- **`% ledger: <id>, …` comments stay on their line, unchanged** (561 in Book
  2). Gate 12 (`check_chem_twin.py`) compares the id multiset of every file
  with its English twin.
- **NEW: Book 2 has 141 `\ce{}` formulas** (g10/02, g10/03, g10/07, g11/07,
  g11/08, g12/01, g12/03, g12/04, g12/08 …), most in running prose outside any
  math span. They are frozen byte for byte: `id_apply`'s `chem` census at write
  time and gate 12 on disk after every later edit; gate 13 checks every
  reaction still balances. Never localise a state symbol (`(aq)`, `(s)`), a
  mineral formula or an arrow; translate the words around them. Ion and
  species names in prose (*iron(III)*, *carbonic acid*) are prose: use the
  rendering of your language's chemistry edition. `xticklabels={\ce{SiO2}, …}`
  (g12/01) stays as it is. Arabic: inline `\ce` is now wrapped LTR by the
  style (ported from chemistry 2026-10-25) — check one rendered reaction with
  `pdftotext -bbox` anyway.
- **Code arguments stay byte-identical**: `\omwx{…}`, `\omlith{…}`, `\omve{N}`,
  every `lith <rock>` / `om lith` style, every pic, every figdata path.
- **`\foreach` lists with visible words** (compared byte for byte by
  `id_apply`'s `draw` census, so translating one costs an `@@ N-M !draw` on
  that range — record each in the score file and check the list by eye;
  translate only the visible fields, keep numbers, colours, node names):
  - `grade-10/02-habitable-planet.tex` 299 (`\n/\d`: planet names)
  - `grade-10/03-earth-energy-budget.tex` 226 (`\lab/\lo/\hi/\n`: *fresh snow, sea ice, desert sand …*)
  - `grade-10/05-storms-and-cyclones.tex` 58 (`\dx/\title`: *1. growing …*)
  - `grade-11/08-igneous-rocks.tex` 153 (`\x/\a/\b`: rock names), 162 (`\m`: mineral names; `\c` are colours)
  - `grade-12/05-destruction-of-mountains.tex` 272 (`\lab`, with `$e$` inside)
  - `grade-12/06-internal-heat.tex` 287 (`\lab`: *trench*)
  The lists in `grade-12/02` 219, 232 and `grade-12/08` 229 are colours: code.
- **pgfplots string keys** (`xticklabels=`, `yticklabels=`, `\legend{}`,
  `\addlegendentry{}`) are blanked by the census and are translated freely
  (26 tick-label keys, 29 legends): g10/03 167 (month initials), g10/07 283,
  g10/08 329 (dates), 454, g10/09 188–189, g11/06 216 (plate names), g11/07
  634, g11/09 542, g12/01 117, g12/05 85, g12/06 170, g12/09 271 (latitudes:
  your hemisphere letters), 580, g12/10 200, 396 (the SSP names in 461 stay).
- **`symbolic x coords` cannot hold non-ASCII.** `grade-10/02` 133
  (`{Mercury,Venus,Earth,Moon,Mars}`, used by the table column `x=name` of
  `grade-10-planet_temperatures-planets.dat`) prints its keys as the tick
  labels and has no `xticklabels`: keep the ASCII keys (the `.dat` file uses
  them) and add an explicit `xticklabels={…}` in your language under `!draw`.
  That is **the only figdata table in Book 2 whose text reaches the page**
  (the others hold numbers, element symbols or proper names of seamounts).
- **Multi-line node labels**: ~95 node texts put a word right after a TeX line
  break (`{340\\incoming}`, `{dew\\point}`). Translate them like any node text.
  `check_latin_prose.py` read `\\incoming` as a macro and could not see an
  untranslated one; fixed before the run (2026-10-25).
- **Units**: never a non-ASCII character or a word inside `\qty{}`, `\unit{}`,
  `\num{}`. Before the run the coordinator moved every English word out of the
  unit arguments (list below): `\num{64}~knots`, `\num{362}~million~\unit{km^2}`,
  `\num{1}~foot`, `\num{0.6}~days`, and in math `\num{1}\text{ year}`,
  `\num{64.4}\text{ million }\unit{km^2}` — so you can write *nœuds*, *millions
  de km²*, *pied*, *jours*, `\text{ an}`. The `\text{}` inside a math span is
  translatable: `id_apply`'s math census blanks it. `hPa`, `ppm`, `GPa`, `Myr`,
  `kbar`, `mol`, `kWh`, `atm`, `min` are symbols.
- **Compass, hemisphere and coordinate letters**: keep Book 1's convention for
  your language exactly (score file "Conventions"; `\omnameCompass*` strings).
  Book 2 adds coordinates in prose (`\ang{21} South`), in a title
  (`g11/06` 129, *Andes, near \ang{21} South*), in tick labels (`g12/09` 271)
  and in tables.
- **Place names** take the established exonym of your language (as in Book 1);
  institutions, datasets, missions, model names and scenario codes keep their
  proper names (USGS, NOAA, GISTEMP, ETOPO1, PB2002, PREM, GRACE, SSP1-2.6,
  IPCC AR6 …), with any descriptive gloss translated. **IPCC terms**: use the
  official translation of the IPCC in your language where one exists (French
  *GIEC*, Spanish *IPCC*/*Grupo Intergubernamental…*, …) and stay consistent.
- **`\begin{dated}{2025}`**: the year argument stays; the box title prints
  `\omnameDated`. Box optional titles (`inthefield[…]`, `inthelab[…]`,
  `history[…]`) are translated.
- **NEW: `proof` (38) and one `theorem`** appear in Book 2 (derivations in
  g10/01, g11/02, g12/06, g12/07 …). Use your language's Book 1/Biology Book 2
  rendering for the proof head (`\omnameProof` is in `styles/lang`).
- **Observation only**: the canon never sends the reader to a quarry, a cliff,
  a cave, a volcano or a river in flood, never has them hammer a rock or look
  at the Sun. Keep that true in your wording (an exercise stem "a geologist
  measures the dip" must not become "measure the dip on the outcrop").
- **Physical science only on climate** (g12/09, g12/10): no policy wording, in
  any language. The emission scenarios are described as the canon describes
  them; do not add "should", "must act", "avoid" where English has none.

## The pipeline (as in Book 1)

1. **Write every body through `tools/id_apply.py`** — the translator writes
   only prose, as line-range replacements of the English twin; unnamed lines
   are copied byte-identically, and the write is refused unless labels,
   environments, solution keys, `\emph`/`\index` adjacency, math spans, `\ce`,
   drawing code, image paths, delimiters and braces match. Read its docstring.
   Line numbers refer to the English file with `\omterm` unwrapped
   (`python3 -c "import sys; sys.path.insert(0,'tools'); import id_apply as a; print(a.unwrap_omterm(open(F).read()))"`).
   `!draw` is **per range** (a hybrid comparison): every range that changes
   drawing code needs its own `!draw`. **Do not machine-translate**: draft at
   native register directly.
2. **Build with the wrapper every time a translated file has been created
   since the last build**; its `.fls` line must equal the files on disk.
3. **Gates**: `bash tools/check_translation.sh grade-<n> <lang>` for n = 10, 11,
   12. Build log: errors, undefined, overfull all **0**; `nullfont` equal to the
   English baseline (below); non-backtick "Missing character" **0**;
   invalid-in-math **0**. Run the coordinator's drawing census
   `python3 /tmp/claude-1000/-home-bvirrion-repositories-one-course/19132ca1-6889-4a73-b873-4fc92dbcdaad/scratchpad/coord/drawcensus.py <lang>`
   and explain every non-node difference in the score file.
4. **Term links**: curate `book2_<lang>.py` (`AMBIG_POLICY =
   "nearest-preceding"`, school book), then
   `python3 tools/link_defined_terms.py --book 2 --lang <lang> --unwrap --apply`
   and `--apply`; then the per-target **frequency** and **chapter-set**
   censuses from `translation_instruction.md` (both), the target-set diff
   against English, the `\index{}` key diff against English, the `\text{}`
   census over **course and solutions**, the `\omterm` per-target display
   census (`tools/check_term_display_drift.py`). English homographs of this
   book (from `book2_en.py`): *eye, flux, flattening, saturated/saturation,
   stable/unstable/stability, trap, volcanic, root, intermediate, deep ocean,
   forcing/feedback/scenario*; plus Book 1's *fault, plate, front, bed, mantle,
   shield, cell, basin, scale, table, current, range, crust, core, trench,
   ridge, arc, delta, phase, cycle, season, mass, zone, spring, well, source*.
   Your language has its own (Book 1's `book1_<lang>.py` lists the ones met at
   school level): find them with the two censuses. **Eleven English
   definitions open with a capitalised term** (*Saprolite, Decompression
   melting, Ridge push, Eclogite, Fracture, Rhyolite, Coalification,
   Schistosity, Regional metamorphism, Diagenesis, Mantle convection*): if your
   translation also opens the sentence with the term, check that its
   lowercase occurrences still link (or reword, *On appelle \emph{x}…*), and
   check the case actually harvested before you STOP or DROP anything.
5. **Native pass** until ≥ 95/100: openings, definitions, propositions and
   their proofs, exercise stems, solution headers, method boxes; the register
   measure (above).
6. **A scripted re-read of every solution against its question**, in your
   language, before you score. Book 2 is computation-heavy (rounding,
   unit conversions, isochrons, heat flow, radiative forcing): recompute along
   the rounded path a student follows; report English-canon slips to the
   coordinator with your arithmetic — never "fix" a number silently.
7. **Last, measure — do not edit after measuring.** Re-run the line-edge
   sweeps (`['’]\s*$`, `^\s*([.,;:)?!]|~[;:?!])`, `[a-zà-ÿ]-\s*$`) after the
   final file lands, re-link, re-run both censuses, the dry run
   `python3 tools/link_defined_terms.py --book 2 --lang <lang> | grep 'links to insert'`
   (must print 0), every gate, then the forced build.
8. **Score** to `translation_scores/book_2/<lang>/translation_score.md`
   (model: your `translation_scores/book_1/<lang>/translation_score.md`,
   including a "Conventions recorded" section and the `!draw` list). Ship only
   at **≥ 95**.

## Arabic notes

Everything in `TRANSLATION_BOOK_1.md` "Arabic: what the probe found" and the
repo `CLAUDE.md` "Arabic" bullets holds: Latin or digit runs in axis labels
need `\babelsublr{…}`; mixed node lines need `\foreignlanguage{arabic}{…}`
line by line; `\omve` is already handled; check every figure type, chart,
table and inline `\ce` with `pdftotext -bbox`. New in Book 2: inline `\ce`
(wrapped by the style), `proof` heads, inline matrices or arrays if any
(`\babelsublr{$…$}` — see the chemistry lessons), and the Book 2 probe notes
below.

## Your report to the coordinator (final message)

Pages; `\omterm` links and distinct targets, and the targets English reaches
that you do not (with English's own count for each); every gate's result; the
build-log numbers; the `.fls` count; your score; **every English-canon defect
you suspect** (file, line, evidence); **every gate or tool bug** (including any
allow-list entry you appended, with its reason); every `!draw` range; every
convention where you departed from your Book 1 edition, and why.

## English baselines (measured 2026-10-25, after the pre-run canon fixes)

| | Book 2 |
|---|---:|
| files (body + solutions) | 28 + 28 |
| lines | 22,992 |
| pages (English PDF) | 362 |
| `\omterm` links | 2,208 (def 2,171, ex 23, prop 14; re-measured in wave 1 after the slab-pull protect and the cleavage EXTRA) |
| distinct link targets | 135 (of 141 definitions) |
| `nullfont` = backtick "Missing character" lines | 3,291 |
| `\index{}` | 219 |
| `\emph{}` | 371 |
| `\qty{}` | 3,686 |
| `% ledger:` comments | 561 |
| `\ce{}` | 141 |
| `\foreach` | 74 |
| `\legend`/`\addlegendentry` | 29 |
| linker dry run, links to insert | 0 |

## Probe builds (2026-10-25, still-English bodies, through the wrapper)

| entry | pages | errors / undefined / overfull | nullfont | other Missing character | invalid-in-math |
|---|---:|---|---:|---:|---:|
| `en` | **362** | 0 / 0 / 0 | **3,291** | 0 | 0 |
| `fr` (pdfTeX) | 362 | 0 / 0 / 0 | 3,291 | 0 | 0 |
| `hi` (XeLaTeX) | 373 | 0 / 0 / 15 (all `in paragraph`: English prose in a Devanagari face) | 3,291 | 0 | 0 |
| `ar` (LuaLaTeX) | 369 | 0 / 0 / 4 (all `in paragraph`) | 3,291 | **1**: ō of "Tōhoku" (g11/06:377), absent from Noto Naskh | 0 |

So the gates are: **`nullfont` = 3,291** (backticks from blank lines in the
map tables, as in Book 1) and **non-backtick Missing character = 0**. Arabic
and Hindi write the name in their own script (توهوكو, तोहोकु); if any edition
keeps a Latin name with a macron or another rare diacritic, check this line.
In the Arabic probe, displayed and inline `\ce` reactions read left to right
(`4 Fe2+ + O2 + 10 H2O −→ 4 Fe(OH)3 + 8 H+`).

## Pre-run canon fixes (coordinator, 2026-10-25; line counts unchanged)

The exact edit list is in the coordinator's `coord/canon_edits_b2.md`.

- **Words moved out of unit arguments (36 sites)**: *knots/knot* (g10/05 and
  its solutions, 13), *million/billion km²* (g10/06 3, g12/01 4 + solutions 4),
  *foot*, *mile*, *acre-foot* (g10/07, g10/08, g10/09), *year*, *days*
  (g11/08), *years* (g12/02:583, in math), *tonnes* (g10 solutions/07).
- **Accent escapes → UTF-8**: `\'Ivarsson` → Ívarsson (g12/06:353 and the
  credits), and in `frontmatter/image-credits-book2.tex` and its seven
  stand-ins Callède, Müller, Vilà, Fernández.
- **Six line-broken `\index{}` keys joined** (g10/08:54, g10/09:80, g11/01:149
  and 254, g11/05:155, g12/02:192): the `\emph{…}\index{…}` pair moved down to
  the next line, so each line count is unchanged.
- Audited and clean: defined-twice terms across grades 1–12 (0), `\crefname`
  coverage for every `\cref` prefix Book 2 uses, compass letters inside math
  (none), the line-edge sweeps on English.
- English linker re-checked after the fixes: `--check` clean, dry run 0;
  `tools/gates.sh grade-10/11/12` green; `check_ledger.py` OK.

## Toolchain changes for this run (coordinator, 2026-10-25)

- Seven entry files `one_earth_and_space_sciences_book_2_high_school_<lang>.tex`
  (derived from the same language's Book 1 entry: Arabic keeps its
  `\emergencystretch`), registered in `latexmkrc` and `release.yml`;
  `frontmatter/image-credits-book2.<lang>.tex` stand-ins; the directories;
  seven `book2_<lang>.py` stubs; `LANGS[2]` opened.
- `styles/oneearth.sty`: chemistry's Arabic inline-`\ce` LTR wrap ported.
- `check_latin_prose.py`: `\\` (with an optional `[skip]`) is a separator, so
  `{340\\incoming}` is now visible to the gate. Re-run on all 45 shipped Book 1
  grade × language trees: still green.
- Validated on both controls: every gate fires on the English Book 2 tree
  passed off as a translation (fr 1,399 Latin-gate issues; hi, ar, id tens of
  thousands); a tampered `\ce` and a tampered ledger id each trip gate 12;
  `id_apply --dry-run` accepts an identity patch on all 56 files.

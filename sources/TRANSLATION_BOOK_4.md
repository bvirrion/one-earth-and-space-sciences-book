# Translation run — One Earth and Space Sciences Book 4 into nl, es, pt, hi, ar, id

The binding run file for the six remaining language editions of Book 4
(University Year 2, `parts/bachelor-2`): 31 chapters + 31 solution files =
**62 files, 29,781 lines**, 484 pp in English. User request, 2026-10-30:
*"do the translations of one earth and space book 4 in all remaining languages.
Use Opus 5.5 High for all these translations. You can use up to 6 subagents at
the same time."* The user chose **one agent per edition, all six at once**
(this overrides `translation_instruction.md` hard rule 3, "four at a time", for
this run only). One subagent owns each edition; when an agent stops before the
edition is done, a **fresh** agent continues it from the edition's PROGRESS file.

**Models (user rule 2026-10-30, recorded at launch):** every edition agent runs
`claude-opus-5-5` (Opus 5.5) at effort **high**; the coordinator runs
`claude-opus-5-5`. Write the model line in your score file; add the
coordinator only if the coordinator later edits your edition (it will say so).

The French edition of Book 4 (`parts/bachelor-2/fr/`, shipped 2026-10-28,
95/100, written one agent per chapter) is your **sense and structure
reference**, not your ceiling. Read the French chapter before drafting yours,
especially its figures: it already solved every data-label chart (below).

If you are an edition agent, this file and your brief are your instructions.
Read everything in "Reading list" before you write a line.

## Reading list (in this order)

1. `../CLAUDE.md` (workspace root) and `../book_style.md`.
2. `../translation_instruction.md` — **the whole file**, including every
   "Lessons from the … Earth and space translations" section at its end (Book 1,
   Book 2, Book 3 fr, the six-language Book 3 run, the per-chapter Book 4 fr run).
   Nearly every paragraph is a defect class some earlier edition shipped.
3. Your language's style card if it has one: `../hindi_style_card.md`,
   `../arabic_style_card.md` (§6 above all), `../indonesian_style_card.md`.
4. `CLAUDE.md` (its "Language editions" sections, Book 3 six languages and Book 4
   French above all), `CONTRIBUTING.md`, `OUTLINE.md` (the Book 4 chapter list) and
   `sources/SERIES_DEFINITIONS.md`.
5. `sources/TRANSLATION_BOOK_3.md` (the Book 3 run file: most of its rules carry
   over and are restated below where they matter) and
   `sources/WAVE1_FINDINGS_B3_W2.md`.
6. `sources/TRANSLATION_BOOK_4_FR.md` (the French per-chapter brief: its
   "Translation rules" and "Drawing code" sections apply to you, read with your
   language for French), `sources/GLOSSARY_BOOK_4_FR.md` (the French term for
   every defined term of Book 4: a sense reference, so that you see which notion
   each English term names) and `translation_scores/book_4/fr/translation_score.md`
   (its canon-edit list: those fixes are already in the English you read).
7. This file. Where any earlier file disagrees with this one, **this file wins**.

Do not re-read whole files you have already read; look up specific lines with
`grep -n`/`sed -n`.

## Your reference editions (read before drafting)

- **Your language's Books 1–3 of this series** — `parts/grade-{1..12}/<lang>/`,
  `parts/bachelor-1/<lang>/`, `translation_scores/book_{1,2,3}/<lang>/translation_score.md`
  (their **Conventions** sections) and `tools/term_config/book{1,2,3}_<lang>.py`.
  Book 4 recalls nearly all of their notions (*plate, subduction, ridge, magma,
  mantle, crust, isotope, half-life, isochron, metamorphism, facies, fold, fault,
  basin, front, cyclone, isobar, greenhouse effect, radiative forcing, proxy …*):
  grep them before choosing a word. **Keep every convention they recorded**:
  compass and hemisphere letters (already in `styles/lang/<lang>.tex`),
  coordinate notation, place-name exonyms, likelihood words of the climate
  chapters, box names, solution headers, the data-line wording, the article
  before `\cref`, the unit convention. A disagreement with Books 1–3 is reported,
  not made silently.
- **The register of a second-year university course.** Measure the instruction
  register of your exercise stems against your language's **University Year 2**
  editions of the sister series before you score, and convert as a reviewed
  pass, never a regex: `../one-physics-book/parts/bachelor-2/<lang>/`,
  `../one-biology-book/parts/bachelor-2/<lang>/`,
  `../one-chemistry-book/parts/bachelor-2/<lang>/` and their score files
  (`translation_scores/book_4/<lang>/` in physics and biology, `book_3/<lang>/`
  in chemistry), and against your own Book 3 edition of this series. Count what
  they do and follow them; state the counts in your score file.
- **Terms a sister series owns** — physics (thermodynamics, radiation, waves,
  fluid dynamics, the Coriolis force), chemistry (every `\ce` species, isotopes,
  equilibria, partition coefficients, redox, phase diagrams), biology (fossils,
  evolution, extinctions): use the rendering your language's edition of that
  series already uses (`grep` its `parts/**/<lang>/`) and report a disagreement
  instead of diverging silently.

## Hard rules (all binding)

1. **You own exactly one edition.** You write only:
   - `parts/bachelor-2/<lang>/*.tex` and `parts/bachelor-2/solutions/<lang>/*.tex`;
   - `tools/term_config/book4_<lang>.py` (a stub is waiting — curate it from YOUR
     edition's harvest, never by translating `book4_en.py`/`book4_fr.py` and
     never by copying `book3_<lang>.py`: Book 3's EXTRA values are Book 3 labels,
     its protects another book's judgement — re-verify each entry you reuse;
     audit any seeded EXTRA against the Book 4 label set with the snippet in
     `translation_instruction.md`);
   - `translation_scores/book_4/<lang>/translation_score.md`;
   - `frontmatter/image-credits-book4.<lang>.tex` (an English stand-in now: it is
     a **deliverable**; keep every photograph credit, author name, dataset name and
     licence exactly; translate the frame and the descriptions; the model is your
     `frontmatter/image-credits-book3.<lang>.tex` and
     `frontmatter/image-credits-book4.fr.tex`; the preface
     `frontmatter/preface.<lang>.tex` is shared and done — do not touch it);
   - your entry file's `\bookline` and `\author` lines only
     (`one_earth_and_space_sciences_book_4_university_year_2_<lang>.tex`; the
     coordinator wrote a `\bookline` modelled on your Book 3's — correct it if it
     is not idiomatic, and say so);
   - your private directory (rule 5).
   `styles/lang/<lang>.tex` already carries the strings Book 4 uses; if one is
   missing or wrong, report it.
2. **Never edit the English canon** (`parts/bachelor-2/*.tex`, `solutions/*.tex`),
   the French edition, the style file, shared tools, other books' files or another
   language's files. A canon defect is REPORTED to the coordinator (SendMessage is
   not available to you: put it in your PROGRESS file under "Canon reports" AND in
   your final message) with file, line and evidence; the coordinator verifies it
   against the book's own model (the figure, its data, the ledger, the sibling
   answers) and fixes it in English and French, then tells every running agent the
   exact old and new text to mirror. Work around a defect in your edition only if
   the fix is obvious and local, and say so.
3. **Never run a repo-wide git command** — no `git checkout -- .`, `git restore`,
   `git stash`, `git clean`, `git reset`. The repo holds the coordinator's
   uncommitted work, the French edition and five other agents' editions; on
   Biology Book 4 one such command destroyed every uncommitted change in the repo,
   and `git clean` would delete every translated file. To undo your own work,
   rewrite that specific file. **Never commit.** Read-only git (`git diff`,
   `git status`, `git log`) is fine. Never wildcard-`rm`; delete scratch files by
   name.
4. **Shared tools are shared.** `tools/check_*_prose.py`, `tools/id_apply.py`,
   `tools/check_translation.sh`, `tools/check_orphan_lines.py`,
   `tools/check_chem_twin.py`, `tools/gates.sh`, `tools/termlink/*`, `styles/*`,
   `draft/b4-run/tools/*`: report bugs instead of editing. The one exception is a
   per-language allow-list entry (`ALLOWED_BY_LANG["<lang>"]` in
   `check_latin_prose.py`, or the equivalent phrase list of your script gate),
   **append-only, with a comment giving the reason and "Book 4 <lang>"**, placed
   BEFORE any `if __name__ == "__main__"` guard, and run once to confirm it changed
   the output. **A name goes in a phrase list; an ordinary word never goes in a
   book-wide `ALLOWED_WORDS`** (two Book 3 agents hid *the, of, and, with, earth,
   model* that way). An agent that rewords correct prose to satisfy a gate has
   found a gate bug: report it.
5. **Scratch files go in your PRIVATE directory**
   `draft/b4-run/<lang>4/` (inside the repo, gitignored; `/tmp` has been wiped
   between sessions before). Six agents share `draft/b4-run/`: never write outside
   your own subdirectory. Keep your patch files there: they are the only record of
   a chapter before `id_apply` writes it. Keep `draft/b4-run/<lang>4/PROGRESS.md`
   current after **every** chapter (below).
6. **Resources** (the user's 19 GB laptop, 22 cores, shared by six agents):
   - **every full-book build goes through the wrapper**
     `bash draft/b4-run/tools/build.sh one_earth_and_space_sciences_book_4_university_year_2_<lang> <lang>-<n>`
     (run from the repo root; the entry NAME, not a path) — TeX Live 2026 (as CI),
     forced `-g`, at most **two** builds machine-wide (waiting for a slot is
     normal), a memory cap, builds into the session scratchpad (not the repo), and
     prints pages / errors / undefined refs / overfull / nullfont / non-backtick
     "Missing character" / invalid-in-math / "Discard zero height" and the `.fls`
     count against the files on disk. A build takes 5–15 minutes plus queueing:
     **run it with `run_in_background`**, and watch it by its output, never with
     `pgrep -f`. Never call `latexmk` on a whole book directly, never `make`,
     never build a book that is not yours. Build after a batch of chapters, not
     after each one;
   - for per-chapter work use the **probe**
     `bash draft/b4-run/tools/probe.sh <lang> NN` (the chapter's course and
     solution file inside your edition's own preamble, with the right engine; at
     most three machine-wide; a minute or two). Cross-chapter references are
     undefined in a probe by construction; read its errors, overfull boxes (with
     source lines), nullfont, missing characters and invalid-in-math;
   - every other long job: `nice -n 19`, `OMP_NUM_THREADS=1`, one at a time;
     never run the repo's pytest suite.
7. **Never name a programme** (no "licence", "L2", "BCPST", "grado en Geología",
   "bachelor geologie", "S1 Geologi", no year or version of a national
   syllabus). An ordinary stage noun for the reader's age (*universiteit,
   universidad, universidade, विश्वविद्यालय, الجامعة, universitas*) is fine.
8. **Labels never translate**: `\label`, `\cref`/`\ref`/`\pageref` targets,
   `\begin{solution}{key}`, the first argument of `\omterm`, file names, image
   paths, figdata table paths, TikZ node names, colours (`icsTriassic` …), styles,
   pic names, pgfmath macro names.

## Stints: do not stop early

- **Context is compacted automatically. Do not stop because your context is
  large, and do not stop because the scope is large** ("this is a multi-stint
  job" is not a reason to stop). Stop only when the edition is done, or when a
  real blocker needs the coordinator.
- **PROGRESS.md** (in your private directory), updated after every chapter:
  chapters done (course + solutions, gates clean, probe clean), the next chapter,
  every `!draw` range, canon reports, gate/tool bug reports, decisions on
  conventions, and anything a fresh agent would need to continue without
  re-deriving it. If you are a **continuation** agent, read PROGRESS.md first and
  trust it; do not re-translate finished chapters.
- The work, in order: (A) translate all 31 chapters, figure text included; (B)
  finish: credits page, term layer, overfull boxes, the full build, renders; (C)
  read: every chapter sentence by sentence against the English (log "chNN read,
  N fixes" in PROGRESS.md; close (C) only when no chapter is left); (D) measure
  and score. Every earlier edition's first "finished" hand-back still had English
  in it, 16–52 overfull boxes and a self-score of 92–93: (B) and (C) are where an
  edition reaches 95.
- **Once you edit a written `.tex` file directly, its patch is stale for good.**
  Never re-apply `id_apply` over a file you have edited by hand (it would undo
  the edit); unwrap the links, edit, relink. Write in PROGRESS.md which files
  are past that point.

## Earth and space conventions (as in Books 1–3, plus what is new in Book 4)

- **`% ledger: <id>, …` comments stay on their line, unchanged** (1,066 in
  Book 4). Gate 12 (`check_chem_twin.py`) compares the id multiset of every file
  with its English twin.
- **Book 4 has 512 `\ce{}` formulas**, many in running prose outside any math
  span (geochemistry, magmatism, ore deposits). They are frozen byte for byte:
  `id_apply`'s `chem` census at write time and gate 12 on disk after every later
  edit; gate 13 checks every reaction still balances. Never localise a state
  symbol, a mineral formula or an arrow; translate the words around them. Ion
  and species names in prose follow your language's chemistry edition.
- **Code arguments stay byte-identical**: `\omwx{…}`, `\omlith{…}`, `\omve{N}`,
  every `lith <rock>` / `om lith` style, every pic, every figdata path, every
  `ics<Period>` colour.
- **Environments**: as Book 3, plus `dated` (6, a box for a volatile fact: its
  head string is in your language file), `corollary` (2), `theorem` (1),
  `remark` (1), `semilogxaxis`/`semilogyaxis` (1 each), `groupplot` (18). Tables:
  9 `table` with `\caption` (the caption word and `\cref{tab:…}` strings are in
  your language file since Book 3).
- **Units** — each language keeps its Book 3 convention:
  - **nl, es, pt, hi, ar**: keep English's units exactly — `Ma` for a date,
    `Myr` for a duration, `Gyr`, `kyr`, `yr` — in prose and in formulas. Every
    unit argument stays byte-identical to English. Nothing to convert.
  - **id**: as Indonesian Books 1–3, **Ma for dates AND durations, Ga for a
    billion years**, `yr` kept. Draft with the English unit arguments
    byte-identical (so every patch passes the `math` census), then, **after your
    last chapter lands**, run ONE scripted conversion over your own 62 files
    only: `\Myr` → `\Ma`, unit-string `Myr` → `Ma`, `Gyr` → `Ga` (and `kyr` →
    `ka` if your Book 3 did; check it), inside `\qty`/`\unit`/`\si` unit arguments
    and math only. Put the lookbehind AFTER the optional backslash (the French
    pass's `(?<![A-Za-z])\\?Myr` matched `\per\Myr` at the `M` and printed
    `\per\\Ma`); skip comments and figdata column names (`t_Myr`); then
    `grep -rn '\\\\[MGk]a' parts/bachelor-2/id parts/bachelor-2/solutions/id`
    must print nothing; then gates, build. List the conversion in the score file.
  - **Never a non-ASCII character or a word inside `\qty{}`, `\unit{}`,
    `\num{}`.** The canon's unit words were taken out of every `\qty` before this
    run (`\qty{147}{\day}`, `\qty{10}{\hour}`: siunitx prints *d* and *h* in
    every edition; keep them). Three solutions write
    `\qty[text-series-to-math=true]{624}{} thousand years` (also `{67}{} years`,
    `{137}{} thousand years`): the empty unit is deliberate, the words after it
    are prose — translate them. `rad`, `erg`, `mGal`, `mmol/mol`, `PgC`, `Tmol`,
    `kcal` are unit symbols: keep them.
- **Compass, hemisphere and coordinate letters**: keep Books 1–3's convention
  exactly (`\omnameCompass*` in your language file).
- **Place names** take your language's established exonym (*Alps, Himalaya,
  Andes, Iceland, Hawaii, Greenland, Massif Central, Tibet, Pacific*);
  **palaeogeography** too (Pangaea, Gondwana, Laurasia, Tethys, Panthalassa,
  Rheic Ocean, Iapetus — follow your Books 2–3 and your language's geology
  usage); orogenies (*Caledonian, Variscan, Acadian, Grenvillian*) as your
  language writes them. People's names are never translated. Institutions,
  datasets, missions and model names keep their proper names (USGS, NOAA,
  PREM, ERA5, CMIP6, HadCRUT, the Global Volcanism Program), with any
  descriptive gloss translated; **IPCC takes your language's established
  acronym** if it has one (as your Book 3 did). Titles of papers and books are
  copied as printed (a translated gloss in parentheses is allowed) and **never
  link** (protect them and their glosses).
- **Hawaiian names** keep their diacritics exactly as the canon writes them
  (`Pu`u~`\=O`\=o`, *Kīlauea*, *Mauna Loa*).
- **Observation only**: the canon never sends the reader to a quarry, a cliff, a
  volcano or a river in flood, never has them hammer a rock or look at the Sun.
  Keep that true in your wording (gate 7b): *a geologist measures* never becomes
  an instruction to the reader to go and measure.
- **Physical science only on climate** (ch. 21–27): no policy wording; the
  likelihood words of the climate chapters follow your Books 2–3.
- **Series wording**: weekend-problem heading as in your Books 1–3; *(Book 3,
  chapter N)*-style references translated as your Book 3 does; *the Year 1 / 2 /
  3 volume*, *the physics volumes* as your Book 3 writes them.
- **Cross-references need their article and never their own noun.** `\cref`
  prints the name (*Hoofdstuk 26*, *Proposición 6.6*, *Exercício 4.2*), so
  "chapter \cref{ch:…}" doubles it. The French agents wrote 55 bare or doubled
  references; `draft/b4-run/tools/crefart.py <lang>` lists the word before every
  `\cref` by label type — run it per chapter.

## Visible text that is NOT an ordinary prose line

**`\foreach` lists with visible words** (compared byte for byte by `id_apply`'s
`draw` census, so translating one costs an `@@ N-M !draw` on that range — record
each in the score file and check the list by eye on the rendered page; translate
only the printed fields, keep numbers, colours, node names; a list of colour
names or single capital letters is code):
- `02-planet-formation-meteorites` 373 (*dust grains* … with `\qty` sizes)
- `03-elements-in-the-earth` 79 (`atm`/`lith` are style keys: code — check
  whether anything in that list prints) and 101 (*lithophile, siderophile,
  chalcophile, atmophile*: printed; the keys `lith/sid/…` are code)
- `11-pt-paths` 63, 68 (index-mineral names: *chlorite, biotite, garnet,
  staurolite, kyanite, sillimanite*)
- `18-precambrian-earth` 71 (era prefixes *Eo, Paleo, Meso, Neo*: printed;
  localise them as your language names the Archean/Proterozoic eras)
- `23-climate-variability` 100 (*a summer, b winter*), `24-climate-proxies` 156
  (*a today, b a glacial maximum*)
- `19-phanerozoic-earth` 195, 480 and `26-deep-time-climate` 332 are colour
  lists (code); the period names next to them are ordinary `\node`s; the
  one-letter period initials (ch. 26: *S, D, …*) follow your Book 3's ICS chart.

**pgfplots string keys and legends** (`xticklabels=`, `yticklabels=`,
`\legend{}`, `\addlegendentry{}`; blanked by the census, translated freely) —
190 legend sites in 25 chapters (grep them per chapter) and the tick-label keys
at `04` 651, `27` 229, `02` 441, `30` 227, `17` 386 (keep the atoll names).
Latitude/longitude tick labels use your hemisphere letters.

**`symbolic x coords` keys are code**: `17-oceanic-islands` 385 (the drill-site
names, printed through `xticklabels` at 386) and `27-anthropogenic-climate-change`
489 (`1971--2018` …: printed as the keys themselves; leave them). Keep keys
byte-identical (non-ASCII in a symbolic coordinate is a fatal build abort).

**Figdata tables whose text reaches the page** — replace them as the French
edition did (read the French lines and mirror their structure, under a per-range
`!draw`, then render the page and check every label against its point):
- `15-wilson-cycle` 418–422: the supercontinent names come from
  `figdata/out/bachelor-2-wilson-supercontinents.dat` (`meta=name`; *Pangaea* is
  localised); French (`fr/15-wilson-cycle.tex`, same lines) drops `meta=name` and
  adds an explicit `\foreach` of nodes;
- `19-phanerozoic-earth` 468–470: the extinction labels come from
  `figdata/out/bachelor-2-phanerozoic-ext.dat` (`meta=label`: *end-Ordovician,
  Late Devonian, end-Permian, end-Triassic, end-Cretaceous*); French replaces them
  by explicit nodes (`fr/19-phanerozoic-earth.tex` 470);
- `19-phanerozoic-earth` 77–80: city tags *P, N, S, C* (Paris, New York, Sydney,
  Cape Town) from `…-phanerozoic-cities-*.dat` — one-letter tags; keep them unless
  your language's name for one of those cities starts with another letter and
  the caption explains the tags (then report it);
- `12-crustal-melting` 453–455: the reference-material names `BHVO-2, AGV-2,
  SRM 278` (inline `point meta=explicit symbolic`): proper names, keep;
- `03-elements-in-the-earth` 315: `nodes near coords` on numbers — confirm on the
  rendered page.

**Multi-line node labels** (`{340\\incoming}`): translate them like any node
text; `check_latin_prose.py` reads `\\` as a separator.

## Pre-run canon state

Every canon fix of the French run (53 edits, listed in
`translation_scores/book_4/fr/translation_score.md`) is already in the English
you read. Two more groups were made in Step 0 of this run (log:
`draft/b4-run/coord/canon_edits.md`):
- the unit words out of `\qty` (above);
- (any further Step 0 edit is listed in the coordinator's log).

Any later canon edit is sent to you verbatim (old → new text) by the
coordinator, through your brief or a message: mirror it in your edition at once.

## The pipeline (as in Books 1–3)

1. **Write every body through `tools/id_apply.py`** — the translator writes only
   prose, as line-range replacements of the English twin; unnamed lines are
   copied byte-identically, and the write is refused unless labels,
   environments, solution keys, `\emph`/`\index` adjacency, math spans, `\ce`,
   drawing code, image paths, delimiters and braces match. **Read its docstring
   first.** Line numbers refer to the English file with `\omterm` unwrapped
   (`python3 -c "import sys; sys.path.insert(0,'tools'); import id_apply as a; print(a.unwrap_omterm(open(F).read()))"`
   — number the lines yourself, e.g. `| cat -n`). `!draw` is **per range**. For
   hi/ar/id, `id_apply` also runs your script's prose gate on the written file,
   so a range you forgot is refused. **Do not machine-translate**: draft at
   native register directly.
   - **Work chapter by chapter in the canon's order** (course file, then its
     solution file), and translate EVERY prose line of a chapter before you move
     on: an absorbed or skipped line is copied through as English, and gates
     9/10 will fail it later.
   - **A chapter is not done until its FIGURE TEXT is done too**: node labels,
     `\legend`/`\addlegendentry`, tick-label keys, axis labels, visible
     `\foreach` fields, the data-label charts. Run `check_latin_prose.py` (or your
     script gate) on the chapter before moving on: its `node`/`legend`/`foreach`
     classes must be empty for that chapter.
   - **One cumulative patch per file**: `id_apply` rebuilds a file from the
     English twin plus the ranges in the patch, so a later patch holding only
     some ranges silently puts English back everywhere else. Keep ONE patch file
     per chapter file, edit it, and re-apply it whole (until you start editing
     the `.tex` directly — then never again).
   - **`id_apply` traps** (Book 4 fr): it compares math spans together with their
     line breaks — keep the English line split inside math; it drops a blank line
     given as the content of a one-line range — leave blank lines out of ranges.
     Keep the same number of lines per range when you can: it keeps your line
     numbers aligned with English for every later check.
   - **Per chapter, before moving on**: your prose gate on the two files;
     `python3 draft/b4-run/tools/engsweep.py <lang> NN`,
     `numdiff.py <lang> NN`, `crefart.py <lang> NN`; the line-edge sweeps
     (`['’]\s*$` excluding `''`, `^\s*([.,;:)?!]|~[;:?!])`, `[a-zà-ÿ]-\s*$`);
     the probe (0 errors, 0 overfull, 0 nullfont, 0 missing-char,
     0 invalid-in-math). A `NUMDIFF` difference is fine only when you can explain
     it (a number spelt out, a thousands separator); an `ENGSWEEP` hit only when
     it is a name or title.
2. **Build with the wrapper every time translated files have been created since
   the last build** (after a batch of chapters); its `.fls` count must equal the
   number of files on disk.
3. **Gates**: `bash tools/check_translation.sh bachelor-2 <lang>`. Build log:
   errors, undefined refs, overfull all **0** (es: the babel-spanish ToC
   font-shape warning is not a reference — see the probe table);
   `nullfont` **0**; non-backtick "Missing character" **0**; invalid-in-math
   **0**; "Discard zero height" **0**. Also `bash tools/gates.sh bachelor-2`.
4. **Term links**: curate `book4_<lang>.py` (`AMBIG_POLICY = "drop"`, as
   `book4_en.py`) **before the first full relink** (an empty stub links every
   surface form of every term, wrong senses included), then
   `python3 tools/link_defined_terms.py --book 4 --lang <lang> --unwrap --apply`
   and `--apply`; then `python3 draft/b4-run/tools/census.py <lang>` (per-target
   **frequency** and **chapter-set** censuses, targets English reaches that you do
   not, `\index{}` keys identical to English, `\text{}` identical to English over
   course AND solutions) and `tools/check_term_display_drift.py`. Read every
   flagged site; judge by whether the **target** is right, never by the ratio.
   English homographs of this book (from `book4_en.py` and the French
   curation): *exposure (time), mixing ratio, deposit, grade, detection,
   attribution, nappe/sheet, member, series, system, stage, group, formation,
   order, front, bed, mantle, shield, cell, basin, scale, table, current, range,
   core, trench, ridge, arc, delta, facies, phase, cycle, season, mass, zone,
   source, sink, flux, budget*. French STOPped *gisement, teneur, détection,
   attribution* outside their defining chapters and masked the groundwater,
   pumice and debris senses of *nappe*: expect the same collisions in your
   language. **Capital-harvest**: about 70 English definitions open with a
   capitalised term; if your translation also opens the sentence with the term,
   check that its lowercase occurrences still link (or reword so the term is not
   sentence-initial), and check the case actually harvested before you STOP or
   DROP anything. Welded compounds (Dutch above all) and hyphenated compounds
   (Hindi) are skipped by `harvest.py`: recover each missing English target with
   `EXTRA`. `EXTRA` wins over `STOP` (mask wrong senses with `EXTRA_PROTECT`).
   Every protect starts `(?<!\w)`. A lookaround anchored on a word that is
   itself a linked term breaks silently: finish with the plain dry run.
5. **Native pass** until ≥ 95/100: openings, definitions, propositions and their
   proofs, exercise stems, solution headers, method/field/lab boxes, history
   boxes; the register measure.
6. **Re-read every solution against its question**, in your language, before you
   score. Book 4 is computation-heavy (Jeans mass, free-fall and Kelvin–Helmholtz
   times, condensation, mass balances, isochrons and model ages, partition
   coefficients and Rayleigh fractionation, cooling of intrusions, eruption
   column heights and isopachs, mantle adiabats and melt fractions, P–T paths and
   thermobarometry, flexure and backstripping, subsidence of oceanic islands,
   lapse rates and CAPE, geostrophic and thermal wind, red noise, proxy
   calibrations, orbital parameters, carbon budgets and TCRE, hazard recurrence
   and probability, ore grades and reserves, maturity and reservoir volumes):
   recompute along the rounded path a student follows; **report** English-canon
   slips to the coordinator with your arithmetic — never "fix" a number silently,
   and expect about half of such reports to be your own error (the French run's
   rate): check each three ways (unrounded, along the printed rounded path,
   against the figure/figdata/ledger) before reporting.
7. **Last, measure — do not edit after measuring.** After the final file lands:
   the line-edge sweeps (rewrap, never end a line with `%`), relink, the
   censuses, the dry run
   `python3 tools/link_defined_terms.py --book 4 --lang <lang> | grep 'links to insert'`
   (must print 0), every gate, then the forced build.
8. **Score** to `translation_scores/book_4/<lang>/translation_score.md` (model:
   your `translation_scores/book_3/<lang>/translation_score.md`, including a
   "Conventions recorded" section, the register counts, the `!draw` list and the
   **model line**: `claude-opus-5-5` (Opus 5.5, effort high), one agent per
   edition (name the stints), coordinator `claude-opus-5-5`). Ship only at
   **≥ 95**, and only once every chapter has been read in (C).
9. **Render and read** (not optional): every figure page you changed text in, at
   ~110–130 dpi (`pdftoppm -r 120 -f N -l N`), each label against its own point;
   one table caption and one `\cref{tab:…}`; the supercontinent and extinction
   charts; the ICS-coloured period bars; after any label fix, render again.

## Language notes

- **nl** — follow your Book 3 register (grep its exercise stems for *je/jouw*
  vs *u/uw* vs impersonal and count them before you draft). Welded compounds cost targets (EXTRA). Dutch exposes
  `'s`/`'t` at line ends (sweep). `WORD_TAIL` manufactures homographs: read your
  `lang_nl.py` before curating. `of` and `over` are Dutch words (the sweeps know).
- **es** — impersonal *se* in course text; the exercise-stem register as your
  Book 3 and the Spanish University Year 2 editions do it. *tiempo* = time and
  weather. The `-se` passive agrees with its object; six nouns are spelled like
  the imperative (*nombre, cierre, cruce, contraste, ajuste, apunte*).
- **pt** — Brazilian Portuguese only (*você*, *-ção*, Brazilian spelling).
- **id** — the unit conversion above; `TAIL_AFTER_S` and *-nya*; a split
  reduplication at a line end breaks the linker (hyphen sweep);
  `check_indonesian_prose.py` runs inside `id_apply` and in gate 8.
- **hi** — XeLaTeX; `hindi_style_card.md`; आप register measured against your
  Book 3 and the Hindi University Year 2 editions; Devanagari emphasis is
  weight, not italic; `harvest.py` cannot harvest a display from a statement
  environment in a non-Latin script unless it carries an adjacent `\index{}`
  (check the target diff); never Devanagari digits where `\qty` belongs; credits
  pass the gate through `CREDIT_SPAN`/`CREDIT_PAREN`/`CREDIT_PHRASES`.
- **ar** — LuaLaTeX, `bidi=basic`; `arabic_style_card.md` §6, Books 1–3's Arabic
  notes (`TRANSLATION_BOOK_2.md` "Arabic notes", `WAVE2_FINDINGS_B2.md` §3a,
  `TRANSLATION_BOOK_3.md` "Language notes"):
  - a leading number, Latin word, `\ang` or `\qty{…}{\degree}` reverses at the
    start of `\foreignlanguage{arabic}{…}` in a one-line node, tick label, legend
    entry, axis label/title, or table cell (15 → 51, "°60"): box the leading run
    only, `\mbox{\textdir TLT …}`; `$…$` and `\num` are safe;
  - mixed node lines need `\foreignlanguage{arabic}{…}` line by line; Latin runs
    in axis labels need `\babelsublr{…}`;
  - inline matrices/arrays in INLINE math reverse their cells
    (`\babelsublr{$…$}`);
  - **read every rendered table** (9 in Book 4: cells, column order right to
    left, number ranges, brackets) and every chart;
  - the exercise heads print ")⋆(" read left to right: that is correct, do not
    "fix" it;
  - before closing: scan the PDF for pages whose only text is the running header
    and the page number; grep the log for "Discard zero height";
  - confirm direction with `pdftotext -bbox` glyph x-positions, not by eye;
  - credits pass the gate through `CREDIT_TITLE_PHRASES`.

## Your report to the coordinator (final message, at most ~80 lines)

Whether the edition is finished or what is left (and that PROGRESS.md says so);
pages; `\omterm` links and distinct targets, and the targets English reaches that
you do not (with English's own count for each); every gate's result; the
build-log numbers; the `.fls` count; your score; **every English-canon defect
you suspect** (file, line, evidence, your arithmetic); **every gate or tool bug**
(including any allow-list entry you appended, with its reason); every `!draw`
range; every `--force-classes` use (there should be none); every convention
where you departed from your Books 1–3, and why.

## English baselines (measured 2026-10-30, Step 0)

| | Book 4 |
|---|---:|
| files (body + solutions) | 31 + 31 |
| lines | 29,781 |
| pages (English PDF, TL 2026) | see the probe table |
| `\omterm` links / distinct targets | 2,019 / 191 |
| `\index{}` / `\emph{}` | 449 / 616 |
| `\qty{}` | 6,162 |
| `% ledger:` comments | 1,066 |
| `\ce{}` | 512 |
| `\foreach` | 65 |
| `\legend`/`\addlegendentry` | 190 |
| `exercise` / `problem` / `solution` | 372 / 31 / 403 |
| `omfigure` / `tikzpicture` / `axis` / `\node` | 204 / 171 / 104 / 864 |
| `\includegraphics` / `table` | 59 / 9 |
| `\label` / `\cref`+`\Cref` | 999 / 320 |
| `definition` / `proposition` / `proof` | 230 / 109 / 99 |
| linker dry run, links to insert | 0 |
| French edition (reference) | 509 pp, 2,262 links / 199 targets, 95/100 |

## Probe builds (2026-10-30, still-English bodies, through the wrapper)

| entry | engine | pages | errors / undefined refs / overfull | nullfont | Missing character | invalid-in-math | zero-height |
|---|---|---:|---|---:|---:|---:|---:|
| `en` | pdfTeX | **484** | 0 / 0 / 0 | **0** | 0 | 0 | 0 |
| `nl` | pdfTeX + babel-dutch | 484 | 0 / 0 / 0 | 0 | 0 | 0 | 0 |
| `es` | pdfTeX + babel-spanish | 485 | 0 / 0 (+1 font-shape) / 3 | 0 | 0 | 0 | 0 |
| `pt` | pdfTeX + babel-brazilian | 484 | 0 / 0 / 1 | 0 | 0 | 0 | 0 |
| `id` | pdfTeX + babel-bahasai | 483 | 0 / 0 / 1 | 0 | 0 | 0 | 0 |
| `hi` | XeLaTeX | 506 | 0 / 0 / 48 | 0 | 0 | 0 | 0 |
| `ar` | LuaLaTeX | 502 | 0 / 0 / 3 | 0 | 0 | 0 | 0 |

- Every overfull box of the probes is `in paragraph`: English prose under another
  language's hyphenation or script face. None is a fixed-width box. Your own
  translated prose replaces all of them; the target is **0**.
- **es: the one "font-shape" line is not a reference.** It is `LaTeX Font Warning:
  Font shape T1/lmr/bx/sc undefined` from the table of contents (babel-spanish's
  small-caps Part numeral in the bold ToC line), as in Books 1–3 es. The wrapper
  counts it separately; undefined references must be 0. (The es probe already held
  the es agent's first two files: the build ran while it worked.)
- Baselines for the closing builds: nullfont 0, Missing character 0,
  invalid-in-math 0, "Discard zero height" 0 in every edition — any non-zero is a
  real defect.

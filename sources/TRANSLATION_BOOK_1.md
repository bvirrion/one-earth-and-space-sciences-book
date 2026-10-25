# Translation run — One Earth and Space Sciences Book 1 into fr, nl, es, pt, hi, ar, id

The binding run file for the seven language editions of Book 1 (Primary and
Middle School, grades 1–9, `parts/grade-1` … `parts/grade-9`, 32 chapters +
32 solution files = **64 files**, ~16,800 + ~3,200 lines). User request,
2026-10-24: one subagent per edition, **at most four at a time**.

If you are an edition agent, this file and your brief are your instructions.
Read everything in "Reading list" before you write a line.

## Waves

| Wave | Editions | Notes |
|---|---|---|
| 1 | `fr` `nl` `es` `pt` | first readers of the canon; they share gate 9 (twin comparison); `fr` becomes the sense twin |
| 2 | `hi` `ar` `id` | inherit the fixed canon, the gate fixes and the French twin; each has its own prose gate |

Between the waves the coordinator re-measures every delivered edition on its
own forced build, verifies and fixes reported canon defects (propagating each
fix into the delivered editions), fixes gate bugs (lenient fixes only while
agents hold patches), re-measures the English baselines and writes
`sources/WAVE1_FINDINGS.md`. **Every wave-2 agent reads it before starting.**

## Reading list (in this order, whole files)

1. `../CLAUDE.md` (workspace root) and `../book_style.md`.
2. `../translation_instruction.md` — **the whole file** (it is long; read all
   of it). Nearly every paragraph is a defect class some earlier edition
   shipped. Its two "Lessons from the … chemistry translations" sections are
   about the toolchain this repo now uses.
3. Your language's style card: `../hindi_style_card.md`,
   `../arabic_style_card.md` or `../indonesian_style_card.md`. The Latin four
   have none: your language's shipped school editions (below) are your style
   reference.
4. `CLAUDE.md`, `CONTRIBUTING.md` and `OUTLINE.md` of this repo
   (`one-earth-and-space-sciences-book/`), and `sources/SERIES_DEFINITIONS.md`.
5. For reference, skim `../one-chemistry-book/sources/TRANSLATION_BOOKS_1-2.md`
   and its `WAVE1_FINDINGS.md`, `WAVE2_FINDINGS.md`, `WAVE3_FINDINGS.md`: the
   most recent run of this same toolchain on a school volume. Where they and
   this file disagree, **this file wins**.
6. This file, then `sources/WAVE1_FINDINGS.md` if it exists.

## Your reference editions (read before drafting)

- **Your language's shipped Book 1 editions of the sister series**, all school
  volumes, same toolchain, same register decisions:
  - `../one-biology-book/parts/grade-{1..9}/<lang>/` — Biology Book 1 covers
    exactly the same grades 1–9 and is the closest model: register gradient
    from grade 1 to grade 9, how a definition opens, the instruction mood of
    exercise stems, the solution headers;
  - `../one-chemistry-book/parts/grade-*/<lang>/` — the newest one;
  - their `translation_scores/book_1/<lang>/translation_score.md` and
    `tools/term_config/book1_<lang>.py` (language-level homograph knowledge:
    re-verify every entry against your own harvest, never copy).
  **Measure the instruction register of your exercise stems against the
  biology Book 1 edition of your language before you score**, and convert as a
  reviewed pass, never a regex.
- Terms a sister series owns (physics, chemistry, biology): use the rendering
  your language's edition of that series already uses, when one exists
  (`grep` the sister repo's `parts/**/<lang>/`); report a disagreement instead
  of diverging silently.
- Wave 2 also has this book's French edition as the sense and structure
  reference (not the ceiling).

## Hard rules (all binding)

1. **You own exactly one edition.** You write only:
   - `parts/grade-{1..9}/<lang>/*.tex` and `parts/grade-{1..9}/solutions/<lang>/*.tex`;
   - `tools/term_config/book1_<lang>.py` (a stub is waiting — curate it from
     YOUR edition's harvest, never by translating `book1_en.py`);
   - `translation_scores/book_1/<lang>/translation_score.md`;
   - `frontmatter/preface.<lang>.tex` (shared by every future book of your
     language: translate it, and adapt any sentence that says the book is
     written in English — the edition is not) and
     `frontmatter/image-credits.<lang>.tex` (keep every photograph credit,
     author name and licence exactly; translate the frame). Both are English
     stand-ins now;
   - in `styles/lang/<lang>.tex`, **only the "Aside boxes" block** (box names,
     `\omnameDated`, `\omnameVE`, the four `\omnameCompass*` letters) — the
     coordinator's wording is a placeholder; change nothing else in that file
     without reporting it;
   - your entry file's `\bookline` and `\author` lines only, if you want to
     improve the coordinator's wording.
2. **Never edit the English canon** (`parts/grade-*/*.tex`, `solutions/*.tex`),
   the style file, shared tools or another language's files. A canon defect is
   REPORTED to the coordinator with file, line and evidence; the coordinator
   verifies it against the book's own model and fixes it. Work around it in
   your edition only if the fix is obvious and local, and say so.
3. **Never run a repo-wide git command** — no `git checkout -- .`,
   `git restore`, `git stash`, `git clean`, `git reset`. The repo holds the
   coordinator's uncommitted Step-0 work and four agents' untracked editions;
   on Biology Book 4 one such command destroyed every uncommitted change in the
   repo, and `git clean` would delete every translated file. To undo your own
   work, rewrite that specific file. **Never commit.** Read-only git
   (`git diff`, `git status`, `git log`) is fine.
4. **Shared tools are shared.** `tools/check_*_prose.py`, `tools/id_apply.py`,
   `tools/check_translation.sh`, `tools/check_orphan_lines.py`,
   `tools/termlink/*`, `styles/*`: report bugs instead of editing. The one
   exception is a per-language allow-list entry (`ALLOWED_BY_LANG[<lang>]` in
   `check_latin_prose.py`; the `ALLOWED_WORDS` / `NOT_GATED` blocks of your
   script's own gate), **append-only, with a comment giving the reason and your
   edition**, placed BEFORE any `if __name__ == "__main__"` guard, and run once
   to confirm it changed the output. An agent that rewords correct prose to
   satisfy a gate has found a gate bug: report it.
5. **Scratch files go in your PRIVATE directory**
   `/tmp/claude-1000/-home-bvirrion-repositories-one-course/59cf54a9-12e3-4394-994b-a781f186173c/scratchpad/<lang>1/`
   (e.g. `fr1/`, `hi1/`). Four agents share the parent folder; a file named
   `p/07.patch` there will be overwritten by someone else's. Keep your patch
   files: they are the only record of a chapter before `id_apply` writes it.
6. **Resources** (the machine is the user's 19 GB laptop, four agents at once):
   - **every full-book build goes through the shared wrapper**
     `bash /tmp/claude-1000/-home-bvirrion-repositories-one-course/59cf54a9-12e3-4394-994b-a781f186173c/scratchpad/build.sh <your-entry-file>`
     — it forces `-g`, holds one of two machine-wide build slots (waiting for
     a free one), caps memory, and prints pages / errors / undefined /
     overfull / nullfont / non-backtick "Missing character" / invalid-in-math
     and the `.fls` count. A build takes 2–4 minutes, more when it queues:
     **run it with `run_in_background`**. Never call `latexmk` on a whole book
     directly, never `make`, never build a book that is not yours;
   - for overfull work, `\input` a single chapter into a probe of the book's
     preamble (seconds) instead of rebuilding the book; write the probe into
     your private directory and run it from the repo root with the same
     `-cnf-line` memory flags as `latexmkrc`;
   - every other long job: `nice -n 19`, `OMP_NUM_THREADS=1`, one at a time.
7. **Never name a programme** (no "cycle 3", "SVT", "collège" as a
   curriculum, "groep 7", "ESO", "SMP kurikulum", …); an ordinary school-stage
   noun for the reader's age is fine (the shipped `\bookline`s use them).
8. **Labels never translate**: `\label`, `\cref`/`\ref`/`\pageref` targets,
   `\begin{solution}{key}`, the first argument of `\omterm`, file names, image
   paths, figdata table paths, TikZ node names, colours, styles, pic names.

## Earth and space conventions for the editions (new in this series)

- **`% ledger: <id>, …` comments stay on their line, unchanged.** Every
  printed number about the real world is traced to a sourced ledger row
  through them (588 in Book 1). Gate 12 (`check_chem_twin.py`) compares the id
  multiset of every file with its English twin. Book 1 has no `\ce{}`.
- **Code arguments stay byte-identical**: `\omwx{suncloud}` (a weather icon
  name), `\omlith{limestone}` (a lithology style), `\omve{5}`, every
  `lith <rock>` / `om lith={…}{…}` style, every pic (`northarrow`,
  `compassrose`, `scalebar`, `strikedip`, `windbarb`, `omwx=\n`, …), every
  figdata path. The prose gates know these macros (taught 2026-10-24).
- **`\foreach` label lists carry visible words and are compared byte for byte
  by `id_apply`'s `draw` census**, so translating one costs an
  `@@ N-M !draw` opt-out on that range (allowed; record each in the score
  file, and check the list by eye). Translate only the visible fields: keep
  coordinates, colours, node names and **`omwx` icon names** (`sun`,
  `suncloud`, `cloud`, `rain`, `shower`, `snow`, `storm`, `fog`, `wind`) in
  English — in `{0/sun/sunny, 1/suncloud/sun and clouds}` only *sunny* and
  *sun and clouds* are text. The lists with words (file:line in English):
  - `grade-1/01-watching-the-weather.tex` 92, 97, 122 (weekdays), 136
    (icon names + *cold/warm*), 187, 204 (seasons + colours + icons)
  - `grade-1/02-landscapes-around-us.tex` 228
  - `grade-3/01-stones-pebbles-sand.tex` 105
  - `grade-4/03-world-physical-map.tex` 87, 93 (legend bands)
  - `grade-5/01-water-shapes-the-land.tex` 57
  - `grade-5/03-natural-hazards.tex` 168
  - `grade-6/01-earth-a-planet.tex` 207, 220 (planet names), 329
  - `grade-6/03-rocks-and-minerals.tex` 323 (Mohs minerals), 328 (299–300
    are bare node names: code, leave them)
  - `grade-7/04-sediments-and-fossils.tex` 163, 322
  - `grade-8/02-winds-global-circulation.tex` 142, 263, 268
  - `grade-9/03-earth-resources.tex` 244
- **pgfplots string keys** (`xticklabels=`, `yticklabels=`) are blanked by the
  census and are translated freely: `grade-5/02` 85, 157 (month initials),
  `grade-6/01` 149, 366, `grade-7/01` 343, `grade-8/05` 265, plus the
  coordinate tick labels (`$150^\circ$W` …, below). **`symbolic x coords` /
  `symbolic y coords` cannot hold non-ASCII**: keep the ASCII keys and add or
  translate an explicit `xticklabels=` (`grade-4/01` 379, weekday keys
  `Mon,…,Sun`, has none yet; `grade-8/05` 264 already has `yticklabels`).
- **Compass and hemisphere letters are localized, consistently.** The compass
  rose and north arrow print `\omnameCompassN/E/S/W` from
  `styles/lang/<lang>.tex` (placeholders: fr/es N E S O, pt N L S O, nl N O Z W,
  id U T S B, hi उ पू द प, ar ش ق ج غ); grade-2 ch. 2 teaches them in prose and
  figure text. Coordinates (`$41^\circ$\,N`, `\ang{30} S`, tick labels
  `$150^\circ$W`) carry the same letters outside math, so you can and must
  write your language's school-atlas convention (Indonesian atlases write
  `LU/LS/BT/BB`, Dutch `NB/ZB/OL/WL`, …). Pick one convention, apply it in
  prose, figures, ticks and the style strings alike, and record it in the
  score file. The letters never sit inside a math span (checked).
- **Place names** take the established exonym of your language (*mer du Nord,
  Groenland, Islande*; *Noordzee*; *Mar del Norte*; *Groenlândia*;
  *Laut Utara*; standard Hindi and Arabic forms). Institutions and datasets
  keep their proper names (USGS, NOAA, NASA, Mauna Loa, GISTEMP), with any
  descriptive gloss translated. Photograph credits keep names and licences.
- **Units**: never a non-ASCII character or a word inside `\qty{}`, `\unit{}`,
  `\num{}` (siunitx sets them in math mode). The canon's
  `\num{14}~million~\unit{km^2}` keeps *million* in prose so you can write
  *millions de km²* etc.; `hPa`, `ppm`, `km` are international symbols.
- **`\begin{dated}{2025}`**: the year argument stays; the box title prints
  `\omnameDated` before it (*Chiffres de 2025*). Box optional titles
  (`inthefield[…]`, `inthelab[…]`, `history[…]`) are translated.
- **Observation only.** The canon never sends the reader to a quarry, a cliff,
  a cave or a river in flood, never has them hammer a rock, and never has
  anyone look at the Sun. Keep that true in your wording: a translated
  imperative must not turn "geologists sample the outcrop" into "sample the
  outcrop".
- **Physical science only on climate**: no policy wording, in any language.

## The pipeline (as in the chemistry runs)

1. **Write every body through `tools/id_apply.py`** — the translator writes
   only prose, as line-range replacements of the English twin; unnamed lines
   are copied byte-identically, and the write is refused unless labels,
   environments, solution keys, `\emph`/`\index` adjacency, math spans,
   drawing code, image paths, delimiters and braces match. Read its docstring.
   Line numbers refer to the English file with `\omterm` unwrapped
   (`python3 -c "import sys; sys.path.insert(0,'tools'); import id_apply as a; print(a.unwrap_omterm(open(F).read()))"`).
   **Do not machine-translate**: draft at native register directly.
2. **Build with the wrapper every time a translated file has been created
   since the last build**; its `.fls` line must equal the files on disk.
3. **Gates**: `bash tools/check_translation.sh grade-<n> <lang>` for n = 1…9.
   Build log: errors, undefined, overfull all **0**; `nullfont` equal to the
   English baseline (**6,633**: backticks from blank lines in the map tables,
   harmless); non-backtick "Missing character" **0**; invalid-in-math **0**.
4. **Term links**: curate `book1_<lang>.py` (`AMBIG_POLICY =
   "nearest-preceding"`, school book), then
   `python3 tools/link_defined_terms.py --book 1 --lang <lang> --unwrap --apply`
   and `--apply`; then the per-target **frequency** and **chapter-set**
   censuses from `translation_instruction.md` (both — each is blind where the
   other sees), the target-set diff against English, the `\index{}` key diff
   against English, the `\text{}` census over **course and solutions**, the
   `\omterm` per-target display census (`tools/check_term_display_drift.py`).
   Earth-science homographs to start from (from `book1_en.py`): *fault, plate,
   front, bed, mantle, shield, cell, basin, scale, table, current, range,
   crust, core, trench, ridge, arc, delta, phase, cycle, season, mass, zone,
   spring, well, source*. Your language has its own: find them with the two
   censuses.
5. **Native pass** until ≥ 95/100: openings, definitions, exercise stems,
   solution headers; the register measure against biology Book 1 (above). The
   register gradient matters more here than in any university book: grade 1
   is read to six-year-olds, grade 9 by fourteen-year-olds.
6. **A scripted re-read of every solution against its question**, in your
   language, before you score. Report English-canon slips to the
   coordinator; never "fix" a number silently.
7. **Last, measure — do not edit after measuring.** Re-run the line-edge
   sweeps (`['’]\s*$`, `^\s*([.,;:)?!]|~[;:?!])`, `[a-zà-ÿ]-\s*$`) after the
   final file lands, re-link, re-run both censuses, the dry run
   `python3 tools/link_defined_terms.py --book 1 --lang <lang> | grep 'links to insert'`
   (must print 0), every gate, then the forced build.
8. **Score** to `translation_scores/book_1/<lang>/translation_score.md`
   (model: `../one-chemistry-book/translation_scores/book_1/<lang>/translation_score.md`).
   Ship only at **≥ 95**.

## Arabic: what the probe found (2026-10-24, English bodies under LuaLaTeX)

- Figures, maps, cross-sections, weather fronts and the compass rose come out
  correctly oriented (ش at the top, ق on the right), and the tcolorbox frames
  sit beside their own text.
- **Latin runs inside pgfplots axis labels print REVERSED**: `xlabel={number of
  volcanoes}` printed "seonaclov fo rebmun", `(km)` printed "(mk)". The style
  sets RTL on every axis label (right for Arabic words), so every Latin or digit
  run you keep inside an axis label (`(km)`, `E`, `CO$_2$`, a date range) needs
  `\babelsublr{…}`. The same holds for mixed node text: use the idioms of the
  shipped chemistry and biology Arabic editions (`\foreignlanguage{arabic}{…}`
  plus `\babelsublr{}` around each Latin or digit run). Check direction with
  `pdftotext -bbox`, never by eye alone, and read one rendered page per figure
  type, per table and per chart.
- Amsthm statement heads printed their brackets facing outward (`)Map(`): the
  chemistry fix had been lost when this style was scaffolded. It is ported
  (Arabic runtime fix 6 in `styles/oneearth.sty`) and verified on the probe
  (`(Map) 4.5 تعريف`); check one exercise head of your own anyway.

## Your report to the coordinator (final message)

Pages; `\omterm` links and distinct targets, and the targets English reaches
that you do not (with English's own count for each); every gate's result; the
build-log numbers; the `.fls` count; your score; your compass/hemisphere
convention; **every English-canon defect you suspect** (file, line, evidence);
**every gate or tool bug** (including any allow-list entry you appended, with
its reason); every `!draw` range.

## English baselines (measured 2026-10-24; links re-measured 2026-10-25 after wave 1)

| | Book 1 |
|---|---:|
| files (body + solutions) | 32 + 32 |
| pages (English PDF) | 324 |
| `\omterm` links | 6,103 (re-measured after wave 1: + 5 "date line", − 4 "mouth of a bay") |
| distinct link targets | 137 (of 142 definitions; 5 never linked in English — not a gap in your edition) |
| `\index{}` | 237 |
| `\emph{}` | 455 |
| `\qty{}` | 834 |
| `% ledger:` comments | 588 |
| `\foreach` | 150 |
| `nullfont` = backtick "Missing character" lines | 6,633 |
| linker dry run, links to insert | 0 |

Probe builds on the still-English bodies: `fr` 324 pp, 0/0/0; `hi` 341 pp,
0 errors, 0 undefined, 6 overfull (all `in paragraph`: English prose in a
Devanagari face); `ar` 338 pp, 0/0/1 (`in paragraph`). Non-backtick "Missing
character" 0 in every engine (Ø, å, é, ġ all render).

## Pre-run canon fixes (coordinator, 2026-10-24)

- TeX accent escapes → UTF-8: `Utqia\.gvik` → Utqiaġvik (10 sites,
  grade-5/02, its solutions, grade-8/02), `Mal\'e` → Malé (grade-7/03),
  `{\O}yvind` → Øyvind (grade-6/03), `V\aa gen` → Vågen (grade-9/04), and the
  same two names in every `image-credits` file.
- Three line-broken `\index{}` keys joined (grade-5/02 *climate zone*,
  grade-7/05 *cross-cutting relationships* and *fossil succession*).
- *million* moved out of 15 unit arguments in grade-8/05 and its solutions:
  `\qty{14}{million~km^2}` → `\num{14}~million~\unit{km^2}` (inside one math
  span: `\num{2.56}\text{ million }\unit{km^2}`).
- Compass-rose and north-arrow letters made language strings
  (`\omnameCompassN/E/S/W`), so a French rose can read O for west.
- Audited and clean: defined-twice terms (0), English words left in unit
  arguments (0 after the fix; `hPa`, `ppm`, `km` are symbols), `\crefname`
  coverage, compass letters inside math (none).

## Toolchain added for this run (coordinator, 2026-10-24)

Ported from `one-chemistry-book`: fonts (`assets/fonts/`),
`styles/lang/{fr,nl,es,pt,hi,ar,id}.tex` (rebuilt on this series' keys),
`tools/term_config/lang_*.py` and seven `book1_<lang>.py` stubs, `id_apply.py`,
`check_translation.sh` (gate 4 also counts `inthefield`, `dated`, `scope`),
the four prose gates, `check_chem_twin.py` (gate 12: here the `% ledger:` ids),
`check_term_display_drift.py`; seven entry files registered in `latexmkrc` and
`release.yml`; `LANGS` opened for Book 1. New for this series: the three
prose gates treat `\omwx`, `\omlith`, `\omve` arguments as code (they fired on
every grade-1 weather icon). The Arabic statement-head bracket fix was ported into
the style (it had been lost with chemistry's mhchem block). Validated on both controls: every gate fires on
the English tree passed off as a translation, `id_apply` accepts an identity
patch on all 64 files, and a fixture of every Earth notation block wrapped in
target-language text passes all gates.

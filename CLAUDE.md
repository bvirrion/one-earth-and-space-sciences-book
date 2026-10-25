# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A series of **five** LaTeX books of Earth and space sciences built from **one
shared `parts/` tree**, one entry file per book at the repo root, and a single
style file. Structure, theme and tooling mirror `one-chemistry-book` (scaffolded
from it on 2026-10-22, with the 5-book shape of `one-biology-book`): same One
Course brand, environments, label conventions, term-link engine, data ledger,
calibration gate.

| Book | Entry file | Years | Ch. |
|---|---|---|---|
| 1 Grades 1–9 | `one_earth_and_space_sciences_book_1_primary_middle_school.tex` | `grade-1`…`grade-9` | 32 |
| 2 Grades 10–12 | `one_earth_and_space_sciences_book_2_high_school.tex` | `grade-10`…`grade-12` | 28 |
| 3 University Year 1 | `one_earth_and_space_sciences_book_3_university_year_1.tex` | `bachelor-1` | 29 |
| 4 University Year 2 | `one_earth_and_space_sciences_book_4_university_year_2.tex` | `bachelor-2` | 31 |
| 5 University Year 3 | `one_earth_and_space_sciences_book_5_university_year_3.tex` | `bachelor-3` | 31 |

Note the offset: **Book 3 is `bachelor-1` / `b1`**, Book 4 `bachelor-2`, Book 5
`bachelor-3`.

**Status (2026-10-22):** scaffold, style, shared data and tooling done; 151
placeholder chapters build 0/0/0; the three pilot chapters (g7
`plate-tectonics`, g12 `climate-change`, b1 `geological-maps`) were approved
by the user the same day. The English books are being written by one subagent per book,
**at most three at a time, rolling** (Books 1–3, then 4, then 5), under the
binding run file `sources/BATCH_BOOKS_1-5.md`. **All five English books are
written, verified and closed (2026-10-23): 151 chapters, 2,054 pp — 32 ch. /
324 pp, 28 / 362, 29 / 452, 31 / 461, 31 / 455; every book 0/0/0, 15 years
of gates green, 1,046 tests, 1,454 figdata tables byte-stable.** **Book 1 ships in
eight languages since 2026-10-25** (see "Language editions" below); Books 2–5 are
English only. Not started: translations of Books 2–5, the HTML reader, the site.

- **Books 1–2 never repeat themselves**: every notion has exactly one owner
  chapter across grades 1–12 (`OUTLINE.md` maps); a later chapter recalls it.
- **Books 3–5**: one owner across the three university books; a university
  book may re-found a school notion.
- **Overlaps with the sister series**: physics, biology and chemistry keep the
  notions they own; this series recalls them in prose and builds the Earth or
  space angle (`sources/SERIES_DEFINITIONS.md`).
- Content follows the old French programmes (provenance in
  `sources/outline_sources.md` and the entry-file comments) **but the printed
  books never name a programme, a country's school system or a university**.

`OUTLINE.md` is the chapter list of record. `CONTRIBUTING.md` holds the
authoritative conventions; `THEME.md` the cover brand; the workspace-root
`book_style.md` the cross-subject rules. Read them before writing.

## Build

```sh
make                                        # latexmk, all five books into build/
latexmk one_earth_and_space_sciences_book_1_primary_middle_school.tex
L=build/one_earth_and_space_sciences_book_1_primary_middle_school.log
grep -ac '^!' $L; grep -aci undefined $L; grep -ac Overfull $L    # 0 / 0 / 0
```

pdflatex via `latexmkrc` (raised pdfTeX memory: world maps need it). Build with
`-g` after creating a new chapter file.

## Python tools and data

System `python3` has no numpy and no `ensurepip`; `make venv` builds `.venv`
(numpy, scipy, pytest) with `python3 -m venv --without-pip` + the user's
`~/.local/bin/pip --python`.

- `tools/fetch_data.py fetch|derive|list` — the shared real datasets (Natural
  Earth land, PB2002 plate boundaries and steps, ETOPO1 at 1°, USGS M ≥ 6
  1976–2025, GVP Holocene volcanoes, PREM, Mauna Loa CO2, GISTEMP, the
  Antarctic CO2 composite, EPICA Dome C temperature, LR04, satellite sea
  level). `fetch` writes `data/raw/` (gitignored) and `data/MANIFEST.md`
  (access date, sha256, terms); `derive` writes `data/derived/*.csv`. The
  User-Agent carries no e-mail.
- `figdata/shared/geo.py` — world-map tables (`figdata/out/shared-geo-*.dat`):
  land, ridges, transforms, subduction lines **oriented with the overriding
  plate on the left** plus precomputed teeth polygons (a TikZ decoration
  misplaces marks on a path with jumps), collisions, quakes, volcanoes; a
  `school-` set merges the Amur and Yangtze plates into Eurasia and Okhotsk
  into North America. Mollweide projection. PB2002 conventions: the
  first-named plate is on the left of a step; `A\B` = A sinks under B,
  `A/B` = B sinks under A (tested on four trenches).
- `figdata/shared/region.py` — the **Varden Hills**, the series' invented
  exercise region (10 × 8 km): schist and granite basement, unconformity,
  Triassic sandstone, Jurassic limestone and shale, Cretaceous chalk; a
  chevron anticline–syncline pair with planar limbs (12°, plunging 2° N), a
  normal fault (030, 60° ESE, 200 m throw), a river with an alluvial floor.
  Writes contours, unit polygons, the fault trace (hanging wall on the left),
  section A–B. Tests: three-point problem exact on a limb, V-rule both ways,
  fault sense.
- `tools/gates.sh <year>` — chemistry's gates plus: 7b observation only
  (imperative quarry/cliff/cave/outcrop/hammer, looking at the Sun), 7c policy
  wording (warning), 7d `dated` box needs its year. `make gates`, `make test
  [Y=]`, `make figdata [Y=<year>|shared]`.
- `tools/check_ledger.py`, `tools/check_exercise_calibration.py`,
  `tools/check_ce_balance.py`, `tools/check_pic_scaling.py`,
  `tools/check_problem_numbering.py`, `tools/ai_images.py`,
  `tools/ai_stubs.py`, `tools/link_defined_terms.py` — as in chemistry, set
  for five books.

## Style file additions (`styles/oneearth.sty`)

Boxes `recall`, `inthefield[title]`, `inthelab[title]`, `history[title]`,
`dated{<year>}`, `safety`; ICS period colours `ics<Period>` (ledger
`ics:colour.*`); lithology styles `lith <rock>` and `\omlith{<rock>}`; map pics
`northarrow`, `scalebar`, `strikedip`, `horizbed`, `vertbed`, `anticline`,
`syncline`, `dextral`, `sinistral`, `windbarb`; line styles `contact`,
`unconformity`, `fault`, `normal fault`, `thrust fault`, `ridge`,
`subduction`, `transform`, the four fronts, `isobar`, `isotherm`, `contour`,
`index contour`, `river` (side symbols on the LEFT of the path);
`blockdiagram`, `celestialsphere` (true orthographic projection);
pgfplots styles `omrecord`, `omage`, `omdepth`, `ommap`, `omsection` +
`\omve{N}`, `ompt`, ternary library; units `\Ma`, `\Ga`, `\ka`, `\Myr`,
`\au`, `\lightyear`, `\parsec`, `\permil`, `\hPa`, `\ppm`, `\ppb`.

## Traps met while setting up (2026-10-22)

- `\textperthousand` inside a siunitx unit printed "Ğ": the unit is set in
  math, so it is wrapped in `\text{}`.
- A projected great circle is not a rotated ellipse: the celestial sphere
  draws the equator by orthographic projection so that it meets the horizon
  at east and west.
- A world map with the full PB2002 set, all M ≥ 6 events and decorations
  exceeds pdfTeX's default memory (hence `latexmkrc`'s raised limits; a
  scratch build needs the same `-cnf-line` flags).
- Traced lines from marching squares have arbitrary direction: orient any
  line that carries side symbols before writing it (the fault trace once had
  its ticks on the footwall).

## Traps met while writing the books (2026-10-22/23)

The full record is in `sources/BATCH_BOOKS_1-5.md` and each book's `PROGRESS.md`.

- **Run tests per year.** `make test` without `Y=` runs each year in its own
  pytest process, because two years own figdata modules of the same name.
  New modules and tests still want unique names.
- **Wikipedia is not a ledger source.** Commons credit lines match a naive
  "wiki" grep, so use the refined grep in the batch file. Commons file titles
  and descriptions only identify a photo; they never source a fact.
- **`omfigure` has no counter.** `\cref` to one prints a section number, so
  write "the figure below" or use `\pageref`.
- **Rounding.** Recompute solutions along the rounded path a student follows,
  and never round twice (−0.2245 → −0.22, not −0.23). Read the figdata
  constants before calling a printed value wrong.
- **Figures are checked one per page.** Render each on its own page at
  130 dpi, and set every arrow and label against the numbers printed on it.
  Every main-session spot check still found a science error that the agents'
  passes had missed:
  - a water mass drawn against its sign;
  - a phase boundary drawn past its triple point;
  - a caption's direction left stale after `x dir=reverse`.
- **Re-render after resizing.** After enlarging, shrinking or moving a
  figure, re-render the page before it: a figure pushed over leaves a
  half-blank page.
- **One definition per term.** A term defined twice inside the school books,
  or inside the university books, breaks the ownership rule. Check with a
  script over `\index` inside `definition` environments.

## Language editions (Book 1, 2026-10-24/25)

**Book 1 ships in eight languages**: English plus `fr`, `nl`, `es`, `pt`
(Brazilian), `hi`, `ar` and `id`. That is seven editions, made by one agent
each in two waves of at most four (user rule): fr/nl/es/pt, then hi/ar/id.
Every edition scored 96/100, except Arabic at 95.
- The run file is `sources/TRANSLATION_BOOK_1.md`.
- What wave 1 found, and what wave 2 was told, is in `sources/WAVE1_FINDINGS.md`.
- Read the workspace-root `translation_instruction.md` first. Its "Lessons from
  the first Earth and space translations" section is the generic half of what
  follows.

| | pages | links / targets |
|---|---:|---:|
| `en` | 324 | 6,103 / 137 |
| `fr` | 340 | 6,003 / 137 |
| `nl` | 335 | 5,455 / 138 |
| `es` | 339 | 6,071 / 138 |
| `pt` | 336 | 6,065 / 138 |
| `hi` | 313 | 6,156 / 138 |
| `ar` | 303 | 5,951 / 138 |
| `id` | 344 | 6,639 / 137 |

Every edition reaches every English target. Five editions also link the
time-scale definition, which English never reaches.
- Dutch is lower because it welds compounds.
- fr/es are low on *weather* (*temps*/*tiempo* also mean time).
- id/ar are high on *altitude* (one word covers height and altitude).

Every edition's final forced build is clean:
- 0 errors, 0 undefined, 0 overfull, invalid-in-math 0;
- `nullfont` 6,633, the English baseline (backticks from blank lines in the
  map `.dat` tables, harmless); non-backtick "Missing character" 0;
- `.fls` = 64 = the files on disk.

`check_translation.sh` is green for every grade × language, and the linker
dry run is 0 everywhere.

- **Toolchain.** It was ported from chemistry in Step 0: fonts, `styles/lang/*`,
  `id_apply`, `check_translation.sh` gates 1–13 (gate 4 also counts
  `inthefield`, `dated` and `scope`; gate 12 checks `% ledger:` ids), the four
  prose gates, the term configs, the entry files, `latexmkrc`/`release.yml`, and
  `LANGS`. The compass letters are strings (`\omnameCompassN/E/S/W`). The Arabic
  amsthm head-bracket fix had been lost in this style and was ported back.
- **Canon defects found by the translators and fixed** (exact list in
  `WAVE1_FINDINGS.md` §1 and the coordinator's notes):
  - superposition credited to Hutton instead of Steno;
  - wrong values: 1250 km for 1350 km, −90 °C for −86 °C, 1500 m for 1200 m,
    2 rainy afternoons for 3;
  - a missing 0.5 % for 6 volcanoes of unknown setting;
  - Colombo called the capital of Sri Lanka;
  - two double roundings (6.45 → "≈ 6.5" → "about 6"; 41.5 → "≈ 41 %");
  - "R. Wright" for T. L. Wright;
  - `\textbf{20 years}` inside math;
  - accent escapes (`Utqia\.gvik`, `Vi\~nas` and others);
  - broken `\index` keys;
  - "million" inside `\qty` units;
  - English never linking "date line", and "mouth of a bay" linking the river
    mouth.
- **A first canon fix was wrong and was reverted.** A reported "26 March"
  contradicted the figure, its data and the sibling answers' counting
  convention. The answer is 25 March.
- **Figdata tables print English.** Month, era and city names, "1880s" and
  similar labels come from `.dat` files, so every edition replaced those
  labels with explicit nodes under a per-range `!draw`. If a `.dat` label
  table changes, every edition must be updated by hand. The tables are listed
  in `WAVE1_FINDINGS.md` §2.
- **Tooling fixed during the run:**
  - **`id_apply` `!draw`:** it was file-wide and is now per range (a hybrid
    comparison). That blind spot cost an arrow in es. A three-level calc
    coordinate is now blanked as node text, and `\\}` is no longer read as
    an escaped brace.
  - **`check_latin_prose`:** a whole-word Unicode tokenizer; the duplicate-line
    floor went from 40 to 12 characters and from 4 to 3 words (it found
    kept-English lines in two SHIPPED biology editions, now fixed); `\\]` is no
    longer a math close.
  - **hi/ar gates:** the compass letter द, `\pgfmath*` arguments, inline
    `\tikz` and `\tikzset` reduced as drawing code, siunitx quantities reduced
    to a number placeholder, file-key split macros (`\gfivechart`,
    `\gsixrock`), and the units hPa and bar.
  - **Termlinker:** the Part-heading protect now covers every language's word.
- **Arabic.**
  - `\omve` prints its factor through `\mbox{\textdir TLT …}`;
    `\babelsublr` does not work inside a TikZ node.
  - Latin runs in axis labels need `\babelsublr`.
  - Mixed node lines need `\foreignlanguage{arabic}{…}` line by line.
  - The image credits wrap every Latin run.
- **Local TeX Live has no `french/spanish/dutch/portuguese.ldf`.** The Latin
  editions build without babel locally (English hyphenation patterns); CI has
  them.

**Never commit.** Leave the working tree for the user.

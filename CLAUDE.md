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
eight languages since 2026-10-25 and Book 2 since 2026-10-26** (see "Language
editions" below); Books 3–5 are English only. Not started: translations of
Books 3–5, the HTML reader, the site.

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

**Weekend problems start on a fresh page** (user ruling, 2026-10-26). A
problem box needs `lines before break` of room to start, so a problem that
could not start at the foot of a page used to move on and leave its
`\section` heading stranded, sometimes alone on a page (found in Book 1). The
style now breaks the page before the heading: `\section` looks ahead, past
blank lines, for `\begin{problem}`. A problem with no heading of its own
breaks the page right before its box. No chapter file changed, in any
language. A companion fix keeps each "Solution p. N" link with its
exercise's last line (`\omsollink@emit`): a closing list had left the link
alone on a fresh page. After both, the five English books build at 329, 367,
475, 484 and 477 pp. They were 324, 362, 452, 461 and 455 pp when closed;
Books 3–5 were not measured between the two dates. Side effect: an
exercise's last line and its link can spill onto a short page of their own
before the problem. That happens on about ten pages over all nineteen
editions.

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
| `en` | 329 | 6,103 / 137 |
| `fr` | 340 | 6,003 / 137 |
| `nl` | 340 | 5,455 / 138 |
| `es` | 339 | 6,071 / 138 |
| `pt` | 339 | 6,065 / 138 |
| `hi` | 319 | 6,156 / 138 |
| `ar` | 306 | 5,951 / 138 |
| `id` | 351 | 6,639 / 137 |

Pages are from the 2026-10-26 TeX Live 2026 rebuild (as CI builds them), after
weekend problems began opening on a fresh page (see "Weekend problems" above). At delivery they were 324,
340, 335, 339, 336, 313, 303 and 344.

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
- **Local TeX Live has no `french/spanish/dutch/portuguese.ldf`.** The
  system TeX Live (2022) builds the Latin editions without babel, with English
  hyphenation. It only warns "building French without babel". CI's
  `texlive-full` is TeX Live 2026 with every `.ldf`, so the PDFs CI ships
  break lines differently from the ones checked locally. **Verify with
  `~/texlive/2026`** (scheme-full, the same pdfTeX 1.40.29 and latexmk 4.88 as
  CI): put `~/texlive/2026/bin/x86_64-linux` first in `PATH`. The release of
  Book 1 (`v0.0.3`, 2026-10-25) failed in CI on exactly this gap (next item).
  The TeX Live 2026 rebuild also found four overfull lines that hyphenation
  had hidden. They are fixed by rewording in fr/es, and by `\allowbreak` after
  the slashes of "NASA/METI/AIST/Japan" in the fr/es image credits.
- **`\textsuperscript` inside a pgfplots axis node (TeX Live 2026).** The
  2025+ kernel's `\textsuperscript` runs `\check@mathfonts`. If it has already
  been used in prose and the picture sets a smaller `font=`, a `\node` inside
  `axis` that uses it again fails with "Package tikz Error: Giving up on this
  path. Did you forget a semicolon?" at `\end{axis}`. This has nothing to do
  with babel: English fails the same way, and TeX Live 2022 builds it. Brace
  the call: `{1\textsuperscript{er}}`. The only site was the French calendar
  of g7/05.

## Language editions (Book 2, 2026-10-25/26)

**Book 2 ships in the same eight languages.** One agent made each edition, in
two waves (fr/nl/es/pt, then hi/ar/id):
- the run file is `sources/TRANSLATION_BOOK_2.md`;
- the findings are in `sources/WAVE1_FINDINGS_B2.md` and
  `sources/WAVE2_FINDINGS_B2.md`, which also holds the complete list of canon
  edits made after wave 1.

| | pages | links / targets | score |
|---|---:|---:|---:|
| `en` | 367 | 2,208 / 136 | |
| `fr` | 387 | 2,263 / 138 | 96 |
| `nl` | 387 | 2,094 / 136 | 96 |
| `es` | 385 | 2,168 / 138 | 96 |
| `pt` | 382 | 2,249 / 137 | 96 |
| `hi` | 349 | 2,250 / 138 | 96 |
| `ar` | 334 | 2,137 / 137 | 95 |
| `id` | 393 | 2,345 / 139 | 96 |

Pages are from the 2026-10-26 TeX Live 2026 rebuild, as CI builds them
(fresh-page problems, and the Arabic empty-line fix). At delivery they were 362, 380, 374, 375, 373, 345, 334 and
379.

All eight builds are 0/0/0, nullfont 3,291 (the English baseline), and the
`.fls` lists 56 translated files, the same as on disk. All 21 grade ×
language gates pass, and the linker dry run is 0 everywhere.

**Infrastructure.** Book 2 needed only entry files, credits stand-ins,
directories, seven term-config stubs and `LANGS[2]`, plus three changes:
- the Arabic inline-`\ce` LTR wrap, ported from chemistry into
  `styles/oneearth.sty`;
- `check_latin_prose` reading `\\` as a separator;
- a few prose-gate allow-list entries.

**Canon fixes.** About twenty were made, and all were mirrored into every
edition.
- **Units.** 36 unit words were moved out of `\qty`. A `\qty` without a
  unit takes the next letter as its unit: in French, `\qty{35} à` crashed
  the build.
- **Escapes and keys.** Accent escapes were replaced, and six line-broken
  `\index` keys joined.
- **Credits.** A credit line that cited Wikipedia now names the figure's real
  sources.
- **Arithmetic.** Four values had been computed from unrounded intermediates.
- **An answer contradicting its sibling.** g11 solutions/08 answer 16 said
  "between the two" when the previous answer's 2.6 years lies inside the
  intrusion range.
- **A name.** "Motonari" became Motonori Matuyama.
- **A clipped chart label.** The g12/02 fold-shortening chart cut off
  "Varden:".

**Traps:**
- **Capital-harvest.** It struck *cleavage*, *migration* (English and nl) and
  *slab pull* (nl). Audit every capitalised definition, in every language.
- **Wrong-sense links.** *slab* (a slab of shale), *slab pull* (the verb) and
  *heat flow* (the verb) each linked in the wrong sense; they are now
  protected.
- **Titles.** A paper title, and any gloss a translator adds to it, never
  links.
- **Protect anchors.** A protect without `(?<!\w)` matched inside a longer
  Arabic word and removed 22 links.
- **Labels on translated charts.** Translated labels are longer: every wave-1
  edition found collisions on rendered pages. Fix them inside the node text.
- **Arabic right-to-left.** A leading number or Latin word reverses (15 → 51)
  in three places: inside `\foreignlanguage{arabic}{…}` in a one-line node,
  tick label or legend entry; at the start of an axis label; and in a leading
  `\ang`/`\qty{…}{\degree}` ("°60"). Box the leading run only, with
  `\mbox{\textdir TLT …}`. A probe and a sweep on 2026-10-26 fixed 9 sites in
  Book 1 Arabic (the shipped calendar printed "52 مارس" for 25 March) and 4 in
  Book 2 (`WAVE2_FINDINGS_B2.md` §3a).
- **Blank Arabic pages.** Babel's tcolorbox hook left a zero-height empty
  line before every breakable box in Arabic, and at a page foot tcolorbox's
  `\pagebreak` shipped that line alone: two header-only pages in Book 2.
  No log message comes with them. Fixed in `styles/oneearth.sty` (Arabic
  block, item 7). Scan every Arabic PDF for pages that hold only the running
  header and the page number.
- **A label lost at a page break.** A tcolorbox zero-height part dropped a
  label at a page break; grep every log for "Discard zero height".
- **Million-year units.** English writes Ma for a date and Myr for a
  duration (`\Ma`, `\Myr`). fr and id use Ma for both, in prose and in
  formulas. The other editions keep English's split. A `\qty` inside math is
  frozen by the math census, so a language that switches units must also
  switch the formulas (`--force-classes math`), or its pages mix the two.

**Never commit.** Leave the working tree for the user.

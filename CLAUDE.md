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
eight languages since 2026-10-25, Book 2 since 2026-10-26 and Book 3 since
2026-10-28** (French 2026-10-26, the other six 2026-10-27/28; see "Language editions"
below). **Book 4 ships in eight languages since 2026-10-30** (French 2026-10-28 as a
per-chapter pilot, the other six 2026-10-30). **Book 5 ships in eight languages since
2026-11-04, at the lower pilot tier** (see its section below). Not started: the HTML
reader, the site.

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

## Language editions (Book 3, French, 2026-10-26)

**Book 3 (University Year 1, `bachelor-1`) ships in English and French.** One agent
wrote the French edition (about 3 h 10 min), and the coordinator verified and closed
it. The run file is `sources/TRANSLATION_BOOK_3_FR.md`; **`sources/WAVE1_FINDINGS_B3.md`
is what `nl`, `es`, `pt`, `hi`, `ar` and `id` must read first.**

| | pages | links / targets | score |
|---|---:|---:|---:|
| `en` | 475 | 4,650 / 184 | |
| `fr` | 496 | 4,468 / 185 | 96 |

Final builds (TeX Live 2026, forced `-g`, scratchpad): `en` 475 pp and `fr` 496 pp, both 0 errors / 0 undefined / 0 overfull, nullfont 0, no missing characters, invalid-in-math 0, zero-height 0, `.fls` 58 = the files on disk (the French build was repeated after the last edit). `check_translation.sh
bachelor-1 fr` and `gates.sh bachelor-1` pass, the linker dry run is 0, and every
English target is reached (the extra French one is *parcel*).

**Infrastructure.** The French entry `one_earth_and_space_sciences_book_3_university_year_1_fr.tex`
(from the French Book 2 entry), `frontmatter/image-credits-book3.fr.tex`, the
directories, a `book3_fr.py`, `LANGS[3] = ("en", "fr")`, `latexmkrc` and `release.yml`.
Two shared changes, both conditional on a language file defining a string, so every
other edition is unchanged: `\crefname{table}` (+ `\tablename` = *Tableau* in `fr.tex`,
because babel-french's own caption word is *Table*), and `\year` printing *an*
(`\omunitYear`). The agent also made two lenient edits to `check_latin_prose.py` (siunitx
option brackets are not prose; an `ALLOWED_BY_LANG["fr"]` entry for symbolic
coordinate keys).

**Canon fixes (English, mirrored into French, line counts unchanged):** 14 accent
escapes and 8 credit names to UTF-8; 9 unit words moved out of `\qty`; three
double roundings (`0.712`, `9.2°`, exercise 7.11's 1.544); the wrong-sense link of
*voting members*. Full list in `WAVE1_FINDINGS_B3.md` §1.

**Traps:**
- **Time units in math.** The run file froze `Myr`/`yr`/`Gyr` in math spans, which
  left *Ma* in prose and *Myr* in 166 formulas. The coordinator converted every unit
  argument in the written tree (a direct edit; the `math` census only runs in
  `id_apply`). Decide the convention before the run.
- **Tables.** Book 3 is the first volume with `table` and `\cref{tab:…}`: caption
  label and reference name need a string per language.
- **A rewrite regex with the lookbehind before an optional backslash** matched
  `\Myr` at the `M` and printed `\per\\Ma`. Grep after any bulk unit edit.
- **A build started before an edit is worthless** if the edit touches files it reads
  later; a half-converted chapter died with an error at page 180.
- **Probe-build one page of every new environment** before the run: the table
  caption read *Table 7.1* in a French book and no gate could see it.
- **Nullfont is 0** in Book 3 (no blank-line map tables): any nullfont line is a
  real defect.

## Language editions (Book 3, the other six languages, 2026-10-27/28)

**Book 3 ships in all eight languages.** One agent at a time made each edition, with at
most four running at once, in two waves: nl/es/pt/id, then hi/ar.
- **Models** (user rule): the edition agents ran `claude-haiku-5-5` at effort high; the
  coordinator ran `claude-opus-5-5`.
- **Stints** (user ruling): when an agent stopped, a fresh agent continued from the
  edition's PROGRESS file. Each edition took 5–9 stints.
- **Run file and findings:** the run file is `sources/TRANSLATION_BOOK_3.md`. The
  findings for wave 2, and the canon edits made in both waves, are in
  `sources/WAVE1_FINDINGS_B3_W2.md`.
- **Scratch logs:** each edition's per-chapter log is in the run scratchpad (`<lang>3/`),
  not in the repo.

| | pages | links / targets | score |
|---|---:|---:|---:|
| `en` | 475 | 4,650 / 184 | |
| `fr` | 496 | 4,468 / 185 | 96 |
| `nl` | 500 | 3,868 / 187 | 96 |
| `es` | 495 | 4,539 / 187 | 95 |
| `pt` | 492 | 4,629 / 185 | 95 |
| `hi` | 454 | 4,029 / 179 | 95 |
| `ar` | 426 | 3,360 / 185 | 95 |
| `id` | 495 | 4,599 / 186 | 95 |

**Builds and gates.** Final builds: TeX Live 2026, forced, in the scratchpad. All are
0 errors / 0 undefined / 0 overfull, nullfont 0, missing-char 0, invalid-in-math 0,
zero-height 0, `.fls` 58. `check_translation.sh bachelor-1 <lang>` passes and the linker
dry run is 0 everywhere.

**Links.** Under-linking is accepted where a homograph cannot be linked safely:
- Dutch welds compounds (83 %).
- Hindi leaves seven targets unlinked, each documented in `book3_hi.py`.
- Arabic STOPs ارتفاع (altitude/height), اتجاه (trend/direction) and ميل
  (declination/slope).

**Canon edits** (English, mirrored into every edition; the full list is
`WAVE1_FINDINGS_B3_W2.md` §1):
- `\textmu` → `\unit{\micro m}` (the hi/ar faces lack µ);
- a sol13 sentence that contradicted the chapter's fitted constant;
- a comma;
- 60 → 70 mW/m² after 2.7 × 25 K/km;
- "acids of the beryllium" → "acids to remove the beryllium";
- 20–30 fathoms printed as "40 to 55 m" (it is 37 to 55);
- "30 % more" than 125 Sv → 39 % (the source's 30 % was against its own canonical
  value);
- "the sand of the opening" → "the beach sand of the opening paragraph" (three
  editions had read *opening* as an aperture);
- "every borehole crosses the limestone over 180 m" and "each log gives the same
  thicknesses" → said of B1 and B3 only (B2 starts in the limestone on the crest).

**Traps:**
- **The gates do not see what a reader sees.** Three coordinator sweeps found defects
  in editions that had passed every gate:
  - English function words in the visible source text. Example: a doubled English
    half-sentence in es; the twin gate compares whole lines.
  - Number tokens per file against English. Examples: nl converted the canon's miles
    to km, so exercise 21.4(c) asked the reader to convert numbers the text no longer
    printed; hi had Devanagari digits in captions where `\qty` belonged; ar dropped
    the leading zero of an azimuth (`\ang{074.8}`).
  - The PDF text. Example: English from figdata label columns.

  The scripts live in the run scratchpad (`coord/engsweep.py`, `numdiff.py`,
  `pdfsweep.py`). The method is in `translation_instruction.md`.
- **Prose-gate allow-lists.** To pass credits and titles, agents had added *the, of,
  and, with, earth, model, global, public, survey, even* to the hi/ar gates' book-wide
  `ALLOWED_WORDS`. They are now credit-span and exact-phrase matching instead:
  `CREDIT_SPAN`, `CREDIT_PAREN` and `CREDIT_PHRASES` in `check_hindi_prose.py`, and
  `CREDIT_TITLE_PHRASES` in `check_arabic_prose.py`. A control file shows both gates
  still catch the bare words. `check_orphan_lines.py` allows the Smith map title in
  every language.
- **The hi and ar patches are stale.** Their finishing and reading stints edited the
  `.tex` files directly. Never re-apply `id_apply` there; unwrap, edit, relink.
- **The ICS chart's names come from figdata** and print English. Every edition draws
  explicit nodes instead, as `fr/24` does.
- **Arabic heads print ")⋆(" when read as a left-to-right string.** That is correct
  right-to-left (the same shapes as the body's "(أ)"); do not "fix" it.
- **Units:** id writes Ma/Ga everywhere. The other editions keep English's
  Ma/Myr/Gyr/yr.
- **Credit pages:** a translated title stays in Latin, and place names in hi credits
  stay Latin, as in Book 2. The colophon is shared English in every edition.

## Language editions (Book 4, French, 2026-10-28: the per-chapter pilot)

**Book 4 (University Year 2, `bachelor-2`) ships in English and French.** The edition
was made by **one agent per chapter** (course file plus solution file), at most eight
at once (user rule): 31 `claude-haiku-5-5` agents at effort high, 69 minutes of wall
clock, and the coordinator `claude-opus-5-5` for every book-wide step. The brief, the
only document an agent read, is `sources/TRANSLATION_BOOK_4_FR.md`. The scratch tools
(`prep.py` for the numbered inputs and glossaries, `check.sh`/`probe.sh` for the
per-chapter check, `units.py`, `census.py`, `pilotcost.py`) and the canon log live in the
run scratchpad (`b4fr/`), not in the repo.

| | pages | links / targets | score |
|---|---:|---:|---:|
| `en` | 484 | 2,019 / 191 | |
| `fr` | 509 | 2,262 / 199 | 95 |

Final builds (TeX Live 2026, forced, into `build/`): both 0 errors / 0 undefined /
0 overfull, nullfont 0, missing-char 0, `.fls` 62. `check_translation.sh bachelor-2 fr`
and `gates.sh bachelor-2` pass, and the linker dry run is 0. Score file:
`translation_scores/book_4/fr/translation_score.md`.

**Cost.** The per-chapter agents still ran mostly on Haiku's long-prompt card: 787 of
1,002 requests were over 100K tokens, with peaks of 242–353K. The agents cost $28
(it would have been $6.55 all on the short card), and the coordinator about $28.

**Canon edits.** 53 were made, in English and French together, each verified three ways
(about half the agents' reports were their own errors). The list and the old/new text
are in the score file and the run's `canon_edits.md`. Among them:
- *less dense* → *denser* (ch. 10);
- pyroclastic flows "hotter than 800 °C" → 200–700 °C (ch. 6);
- the Hawaiian–Emperor volume reworded to its source (ch. 17, ledger `cs14:volumes`);
- a chapter macro `\up` that clashed with babel-french, renamed `\qapfup` (ch. 9);
- `\qty{0.311}{}` → `\num{0.311}`;
- 13 line-broken `\index` keys joined;
- about 35 values recomputed along the printed path.

**Traps:**
- **Units.** French converts every time unit to *Ma*/*Ga*/*ka*/*an* and
  `}{days}`/`}{hours}` to *jours*/*heures*, in prose and in math. The coordinator did
  it by script after the agents finished, skipping comments and table keys (`t_Myr`).
- **Data-file labels.** The extinction (ch. 19) and supercontinent (ch. 15) charts print
  their names from figdata, so French draws explicit nodes, as the ICS chart already does.
- **The term layer.** In `book4_fr.py`, a STOP does not hold back an EXTRA entry. The
  short form *nappe* (thrust sheet) is an EXTRA, so its groundwater, pumice and debris
  senses are masked by `EXTRA_PROTECT` patterns.
- **Cross-references need their article.** Agents wrote *de \cref{prop}*, *chapitre
  \cref{ch}* (which prints "chapitre Chapitre 26"); a sweep fixed 55. Grep the word before
  every `\cref` in a new French edition.
- **A stale `.aux` in `build/`.** An `.aux` left in `build/` from an older TeX Live killed
  the English rebuild with "Argument of \@firstoffive has an extra }". Delete a book's
  `.aux`/`.out`/`.toc`/`.fdb_latexmk` by name before its first TeX Live 2026 build there.
- **Open.** The shared solution head prints *Solution de Exercice N* (`\omsolutionof`, the
  same in every series and in es/pt). The figures were sampled, not checked one per page.

## Language editions (Book 4, the other six languages, 2026-10-30)

**Book 4 ships in all eight languages.** Six `claude-opus-5-5` agents at effort high, one
per edition (nl, es, pt, hi, ar, id), **all six at once** (user rule for this run), each in
a single stint with its context compacted automatically (id 4.6 h, hi 6.6 h, ar 6.9 h). The coordinator
(`claude-opus-5-5`) did every shared-file edit and verified each hand-back.
- **Run file and findings:** `sources/TRANSLATION_BOOK_4.md`; findings, canon edits and
  the new Arabic traps in `sources/WAVE1_FINDINGS_B4.md`.
- **Run directory:** `draft/b4-run/` (gitignored; it survives a `/tmp` wipe): the
  coordinator's tools (`build.sh` with two machine-wide `flock` slots, `probe.sh`,
  `engsweep.py`, `numdiff.py`, `crefart.py`, `census.py`, `pdfsweep.py`), the canon log
  `coord/canon_edits.md`, and each agent's `<lang>4/PROGRESS.md`.

| | pages | links / targets | score |
|---|---:|---:|---:|
| `en` | 484 | 2,019 / 191 | |
| `fr` | 509 | 2,262 / 199 | 95 |
| `nl` | 504 | 1,965 / 193 | 96 |
| `es` | 511 | 2,087 / 195 | 96 |
| `pt` | 504 | 2,224 / 194 | 96 |
| `hi` | 457 | 1,995 / 191 | 95 |
| `ar` | 438 | 1,318 / 198 | 95 |
| `id` | 518 | 2,246 / 197 | 95 |

**Builds and gates.** Final builds of all eight: TeX Live 2026, forced, into `build/`, after
the stale `.aux`/`.out`/`.toc`/`.fdb_latexmk` of `en`/`fr` were deleted by name. All are
0 errors / 0 undefined / 0 overfull, nullfont 0, missing-char 0, invalid-in-math 0,
zero-height 0, `.fls` 62 = the files on disk. The only near-empty pages are the two part
titles. `check_translation.sh bachelor-2 <lang>` passes for all seven, `gates.sh bachelor-2`
is green, the linker dry run is 0 everywhere, and `check_orphan_lines.py` finds 0.

**Links.** Every edition reaches every English target. Arabic is at 65 %: two STOPs
(التحوّل, الكشف) and its split between definite and indefinite forms.

**Canon edits.** Twelve, each mirrored into every edition with line counts unchanged
(`WAVE1_FINDINGS_B4.md` §1). Among them:
- unit words in `\qty` → `\hour`/`\day`;
- *$1 - G$ is increasing* → *$G$ is decreasing* (ch. 28 proof);
- a PETM label clipped below its axis, invisible in English (ch. 26);
- the Marinoan "at least 5 Myr" → 3, which the paragraph's own dated brackets give;
- an unreferenced `\label` between `\section*{Weekend problem}` and its `\begin{problem}`,
  which stranded the heading at a page foot in every edition (ch. 31).

One edit was a coordinator slip: correcting 0.0673 to 0.0672 left the sum two lines below
stale (9.24e-3 → 9.23e-3, found by hi). Recompute downstream after any arithmetic fix.

**Traps:**
- **Arabic right-to-left**, all invisible to the log (`WAVE1_FINDINGS_B4.md` §3):
  - Latin-only parentheses mirror;
  - a Latin word next to math prints on the wrong side;
  - `\foreignlanguage` in a two-axis label mirrors the panel order;
  - "SiO$_2$" in a table cell prints "₂SiO";
  - "Latin: digits" lists reverse;
  - a credit in `\babelsublr` breaks across lines in a narrow caption.
- **Prose-gate `\index` reducer.** It read `|see{…}` as visible English; it now keeps key
  and target and drops *see*.
- **Hindi credits.** "public domain, via Wikimedia Commons" is written in Hindi, as in
  Book 3. The gate's `CREDIT_PAREN` now accepts those two stock phrases inside a licence
  parenthesis.
- **Shared scratchpad.** Six agents rendering pages under the same file names overwrote
  each other's: prefix render files with the edition.
- **Late edits look like stray edits.** To tell an agent's last edit from a stray one,
  compare each file's mtime with that edition's final build log, not with the run start.

## Language editions (Book 5, by the pilot method, 2026-11-03/04)

**Book 5 ships in all eight languages, at the pilot tier: gates green, not read sentence by sentence, figures sampled,
solutions not recomputed** (user ruling). The method is `../pilot_translation_instruction.md`: one fresh tool-less
`claude-haiku-5-5` call per section (effort medium), scripts checking every reply, and one `claude-opus-5-5`
coordinator agent per edition, at most three at once (user rule), `--workers 3`, in the order fr, es, pt, nl, id, hi, ar.
- **Run file:** `sources/TRANSLATION_BOOK_5.md`, with one `sources/TRANSLATION_BOOK_5_<LANG>.md` per edition.
- **English edits before and during the run:** `draft/pilot-bachelor-3-canon/canon_edits.md`.

| | pages | links / targets | score | Haiku calls | list price |
|---|---:|---:|---:|---:|---:|
| `en` | 477 | 1,191 / 216 | | | |
| `fr` | 509 | 1,535 / 240 | 88 | 630 | $20.8 |
| `es` | 507 | 1,359 / 234 | 91 | 585 | $19.4 |
| `pt` | 504 | 1,348 / 233 | 90 | 626 | $18.9 |
| `nl` | 504 | 1,295 / 231 | 90 | 711 | $15.6 |
| `hi` | 462 | 1,346 / 232 | 89 | 653 | $24.7 |
| `ar` | 443 | 1,130 / 250 | 89 | 494 | $25.8 |
| `id` | 505 | 1,507 / 241 | 89 | 510 | $17.6 |

Scores come from a sample of 20 passages (seed 1) plus chapter openings, and aren't comparable with the 95–96 of Books 1–4,
which were read in full. Only about 10 % of pages were read for figures, and many of those hold no figure. List prices are
API equivalents: the cost table, with Book 4's Opus figures and plan usage, is in the pilot instruction.

**Builds and gates.** Final builds: TeX Live 2026, into `build/`. All eight are 0 errors / 0 undefined / 0 overfull, nullfont 0,
missing characters 0, zero-height 0, `.fls` 62 for each edition. `check_translation.sh bachelor-3 <lang>` passes for all seven,
`gates.sh bachelor-3` is green, and the linker check is clean everywhere. `nl` misses one English target
(`def:b3:palaeomagnetism:apw`, 1 link in English).

**English edits:** 122 in three rounds, all meant to leave the print unchanged: unit-less `\qty` to `\num`, unit words out
of `\qty`, 33 `\index` joins. `fr`, `es` and `pt` were translated before rounds 2 and 3 and keep their own forms. No error in the
English science was found or fixed, because nobody recomputed it: **Book 5's English errors, if any, are in all seven.**

**Style fixes during the run, in `styles/`:**
- **`\ohm` printed nothing in Hindi and Arabic:** 11 sites in ch. 31 ("130 m" for 130 Ω m). Fixed in the Unicode-face branch of
  `styles/oneearth.sty`; see "A lost `\Omega`" in `translation_instruction.md`. **The same line is in physics, biology and
  chemistry, whose shipped Hindi and Arabic PDFs have the defect.**
- **Colophon in Arabic:** `(one-course.com)` scattered its brackets; `styles/lang/ar.tex` now boxes it. Books 1–4's Arabic PDFs
  print the old form until they're rebuilt.

**Traps:**
- **Reversed wind.** `fr`, `es`, `pt`, `nl` and `id` all wrote ch. 20:414's *eastward* wind as *easterly*. Only a sweep caught it.
  `hi`, told in advance, read its 74 wind lines and found none reversed.
- **Homonyms from the glossary.** Hindi's weather *front* on a wedge (17 lines), Arabic's *inversion* as "reflection" (11).
- **Arabic labels.** 51 plain-Arabic node labels had brackets or `:` on the wrong side, and no log shows it.
  `draft/pilot-bachelor-3-ar/nodelint.py` finds them. Only pp. 90 and 303 were re-read after the wrap.
- **A clean trial proves little.** Arabic's chapter 15 passed, but it is figure-light.

**Open, for the user:** French part titles print *Licence N année* (`styles/lang/fr.tex`, as in Books 3–4); `\omsolutionof` prints
*Solução de Exercício N* and *Solution de Exercice N*; Spanish *linación* (59 uses, Books 3–4) for *lineación*; Arabic chapter
openings print باب while the prose says الفصل, as in Book 4.

**Never commit.** Leave the working tree for the user.

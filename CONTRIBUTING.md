# Contributing to One Earth and Space Sciences Book

Thank you for contributing! This document describes the structure of the
project and the conventions that keep the books coherent.

## Project structure

The project is a **series of five books** sharing one style and one `parts/`
tree. Each book has its own entry file at the repository root:

- `one_earth_and_space_sciences_book_1_primary_middle_school.tex` --- Book 1, Grades 1--9;
- `one_earth_and_space_sciences_book_2_high_school.tex` --- Book 2, Grades 10--12;
- `one_earth_and_space_sciences_book_3_university_year_1.tex` --- Book 3, University Year 1;
- `one_earth_and_space_sciences_book_4_university_year_2.tex` --- Book 4, University Year 2;
- `one_earth_and_space_sciences_book_5_university_year_3.tex` --- Book 5, University Year 3.

`OUTLINE.md` fixes the chapter list of all five books and the
**notion-ownership maps**: every notion has exactly one owner chapter. Books 1
and 2 never teach the same notion twice; a later chapter that needs it opens
with a `recall` box and only adds what is new. Notions owned by the physics,
biology or chemistry series are recalled, never re-taught
(`sources/SERIES_DEFINITIONS.md`).

The shared files:

- `styles/oneearth.sty` --- **the only place** where packages are loaded and
  macros/environments are defined. Chapter files must not use `\usepackage`
  or define commands. One exception: a drawing helper used by a single
  figure may be defined *inside* that figure's `omfigure` or `tikzpicture`
  (local scope), never at the top level of a chapter. If its argument is a
  key rather than prose, add a mask for it in `tools/termlink/protect.py`.
- `styles/lang/<lang>.tex` --- UI strings for each language (`en` for now).
- `frontmatter/` --- title page, colophon, preface, image credits.
- `parts/<year>/part.tex` --- `\part` via `\omstr{...}` and `\ominput`s.
- `parts/<year>/NN-slug.tex` --- English chapter (canonical);
  `parts/<year>/solutions/NN-slug.tex` --- its solutions.
- `sources/data_ledger.md` --- the shared ledger rows (constants, Earth, Sun
  and planets, the time scale, the datasets); `sources/ledger/book<N>.md` ---
  each book's own rows.
- `data/` --- real datasets: `tools/fetch_data.py fetch` downloads the raw
  files into `data/raw/` (not kept) and records them in `data/MANIFEST.md`;
  `tools/fetch_data.py derive` writes the small tidy tables of
  `data/derived/`, which the figure scripts read.
- `figdata/shared/` --- the world base map (`geo.py`: land, plate boundaries,
  earthquakes, volcanoes, projections) and the series' invented exercise
  region (`region.py`, the Varden Hills: topography, geological map,
  cross-section), both tested in `tests/shared/`.

**Cross-volume references:** `\cref` only works within one book. Never
reference a label that lives in another book; name the volume in prose
instead ("Book 1, grade 7", "the Year 1 volume").

## Building

```sh
make          # runs latexmk (pdflatex), builds every book into build/
make venv     # once: the Python environment (numpy, scipy, pytest)
make test     # the tests (make test Y=<year>: one year's, plus the shared ones)
make figdata Y=<year>   # regenerate a year's figure tables: must leave no diff
make figdata Y=shared   # the world map and the exercise region
bash tools/gates.sh grade-7    # the chapter-level gates for one year
```

A pull request must build with **zero errors**, no undefined references and
no overfull boxes, and pass `tools/gates.sh` for every year it touches.

## Environments

| Environment | Use for |
|---|---|
| `definition` | new notions; put the defined term in `\emph{...}` and `\index{...}` it --- `\index` appears nowhere else, except that a named law this series owns may be indexed in the theorem/proposition that states it |
| `theorem` / `proposition` / `lemma` / `corollary` | laws and results |
| `method` | step-by-step recipes (reading a contour map, a three-point problem, locating an epicentre, dating by superposition) |
| `example`, `remark`, `notation` | worked examples, comments |
| `proof` | derivations when useful; otherwise `\admitted` |
| `exercise` | end-of-chapter exercises, difficulty `[$\star$]` to `[$\star\star\star$]` |
| `problem` | weekend multi-part problem set; label `pb:<year>:<slug>:1` |
| `solution` | `\begin{solution}{exo:...}` keyed to the exercise label |

Six unnumbered boxes hold the asides. They carry no label, and never introduce
a defined term:

| Box | Use for |
|---|---|
| `recall` | *You already know*: 3--5 lines recalling a notion owned by an earlier chapter (`\cref` in the same book), another volume or another series (in prose) |
| `inthefield[title]` | how geoscientists work outdoors, in the third person |
| `inthelab[title]` | how a measurement is made in a laboratory |
| `history[title]` | a short history: who, when, what was found |
| `dated{<year>}` | figures that change from year to year, given for that year |
| `safety` | observing safely (the Sun, storms, hazards) |

## Earth and space conventions

- **Observation only.** The reader is invited to look at the sky, the
  weather, a landscape, building stones or a garden soil, and never sent to a
  quarry, a cliff, a cave, a river in flood or a volcano, never told to hammer
  a rock, and never told to look at the Sun. `tools/gates.sh` checks the
  imperative forms.
- **Every number about the real world has a ledger row**, cited in a source
  comment `% ledger: <id>, <id>` (free text only after `(` or `;`).
  `tools/check_ledger.py` checks every id. Volatile values go in a `dated`
  box.
- **Curves and maps are computed.** A real record (the Mauna Loa CO2 curve,
  an ice core, the earthquake catalogue, PREM) or a model curve (a geotherm,
  an orbit, a hypsometric curve) comes from a tested script
  `figdata/<year>/<name>.py` writing `figdata/out/<year>-<name>.dat` (helper
  `figdata/_table.py`), read by pgfplots; its test is
  `tests/<year>/test_<name>.py`. World maps use the tables of
  `figdata/shared/geo.py`; exercise maps and sections use the region of
  `figdata/shared/region.py` --- never an invented "real" map.
- **Drawings are exact.** Lithologies with the `lith <rock>` styles and the
  `\omlith{<rock>}` swatch; map symbols with the pics and line styles of the
  style file (`strikedip`, `northarrow`, `scalebar`, `normal fault`, `thrust
  fault`, `subduction`, `ridge`, the four fronts, `windbarb`); periods with
  the chart colours `ics<Period>`; the sky with `celestialsphere`; plots with
  `omrecord`, `omage`, `omdepth`, `ommap`, `omsection` (and `\omve{N}`) and
  `ompt`. A side-dependent symbol (fault ticks, trench teeth, front symbols)
  goes on the LEFT of the path's direction: draw the path accordingly.
- **Photographs** for real things (a named volcano, a planet, a thin section,
  a mineral specimen, a scientist), public domain or a CC licence verified
  through the Commons API; **AI illustrations** for generic scenes only, never
  a real place or body, and never a geological structure the reader is meant
  to read.
- **Formulas with `\ce{...}`** (mhchem), balanced (`tools/check_ce_balance.py`).
- **Climate**: physical science only --- forcing, records, attribution and
  projections as the scientific assessments state them, with their calibrated
  likelihood and confidence language; no policy.

## Style rules

1. **Rigor**: state precisely; mark admitted results with `\admitted`.
2. **Concision**: no filler. An example after each substantial definition; a
   `method` box for each standard technique; **many diagrams**.
3. **Exercises**, every one with a full solution, stars never decreasing
   (`tools/check_exercise_calibration.py`):
   - grades 1--5: 10--11 exercises, mostly ★, no weekend problem;
   - grades 6--9: 12 exercises and a weekend problem of 10--14 questions
     (Parts I--III);
   - grades 10--12: exactly 15 exercises (5 ★, 6 ★★, 4 ★★★) and a weekend
     problem of 18--22 questions (Parts I--IV) ending on a named number;
   - university years: exactly 12 exercises (4 ★, 5 ★★, 3 ★★★) and a weekend
     problem of 22--28 questions (Parts I--IV) ending on a named number;
   - every weekend problem starts on a fresh page, together with its
     `\section` heading if it has one. The style does this; write no
     `\clearpage` or `\newpage` in a chapter.
4. **English text** for an international audience; no curriculum or country
   school-system names in student-facing text (real places are named freely).
5. Quotation marks are `` ``...'' ``, never the straight `"`.

## Labels

All labels are namespaced: `<type>:<year>:<chapter-slug>:<name>`.

- Chapters: `ch:g7:plate-tectonics`
- Statements: `def:g7:plate-tectonics:plate`, `prop:...`, `met:...`, `ex:...`
- Exercises: `exo:g7:plate-tectonics:3`
- Weekend problems: `pb:g7:plate-tectonics:1`

Year prefixes: `g1`--`g12`, `b1`--`b3`. Cross-reference with `\cref{...}`,
never bare `\ref`.

## Workflow

1. Fork / branch.
2. Write or edit chapter + solutions files.
3. `make`, check the log for errors, undefined references and overfull boxes,
   and run `tools/gates.sh` on the years you touched.
4. Open a pull request.

## Licensing of contributions

One Earth and Space Sciences Book is free for everyone under the licences in the [README](README.md#license). Contributing
means agreeing to the following.

1. **Same licence in as out.** Your contribution is licensed under the same terms as the part of the
   repository it changes: CC BY-NC-SA 4.0 for book content ([`LICENSE`](LICENSE)), MIT for the
   software — `tools/`, `.github/`, the `Makefile` and the build scripts ([`LICENSE-CODE`](LICENSE-CODE)).
2. **Sign off every commit** with `git commit -s`, which adds a line such as
   `Signed-off-by: Your Name <you@example.com>`. It certifies the
   [Developer Certificate of Origin 1.1](https://developercertificate.org): you wrote the change or
   have the right to submit it. For this project, "the open source license indicated in the file"
   in the certificate means the licences named in point 1.
3. **Relicensing grant.** You grant Benjamin Virrion a perpetual, worldwide, non-exclusive,
   royalty-free and irrevocable right to use, modify and relicense your contribution under other
   terms, including commercial ones (print editions, licences for schools, publishers or companies,
   paid app versions). You keep the copyright in your contribution and may use it as you wish.

**By signing off your commits you certify the DCO and agree to this whole section, including the
relicensing grant in point 3.** Why the grant exists: the books stay free under CC BY-NC-SA for
every reader; the grant only lets the author fund the project through commercial editions without
having to trace and ask every past contributor. Commits without a sign-off cannot be merged.

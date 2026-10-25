# Translation score — Earth and Space Sciences Book 1 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 1 (Primary and Middle School, Grades 1–9) |
| **Language** | Dutch (`nl`) |
| **Quality bar** | **native academic / school prose**: Earth and space sciences in the Dutch a Dutch or Flemish pupil reads, from the short sentences and *je* of year 1 to the register of a lower-secondary geography and science course in year 9. English is the source of truth for content, structure, labels, mathematics, data and drawing code |
| **Register references** | the English canon (content), the shipped Dutch chemistry and biology editions (informal *je*, imperative and interrogative exercise stems, *Weekendprobleem*, *Deel I/II/III --- …*, `` ``…'' `` quotes, decimal points kept), and Dutch atlas and weather-report usage for maps and weather |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-25 |
| **Scope** | Full first translation written directly at native register: 32 chapters + 32 solution twins = **64 files**, `frontmatter/preface.nl.tex`, `frontmatter/image-credits.nl.tex`, the `\bookline`, the Aside-boxes block of `styles/lang/nl.tex` (strings confirmed), a curated `tools/term_config/book1_nl.py`, the defined-term link layer, the Dutch index keys, and this score |

## Verdict in one line

One Dutch school course in Earth and space sciences, from *weer*, *seizoenen* and
*landschap* in year 1 to *hoogtelijn*, *equidistantie*, *kustlangstransport*,
*abrasieplatform*, *zinkgat* and *satellietplaatsbepaling* in year 9. Its forced
build gives **335 pages, 0 errors / 0 undefined / 0 overfull, nullfont 6633 (= English),
0 missing characters, 0 invalid-in-math**, and the `.fls` lists 64 of the 64 edition files.

## Dimension scores

| Dimension | Score | Notes |
|---|---:|---|
| Structural fidelity | **99** | Every file was written through `tools/id_apply.py`: math spans byte-identical, plus the draw, image, label, environment, `\emph` and index censuses. Totals equal English: **237 `\index`**, **455 `\emph`**, **834 `\qty`**, **588 `% ledger:`**, **150 `\foreach`**. There are no duplicate index keys, and every accented key has a sort key. A per-exercise number check against the twin finds no difference except the three deliberate deviations below |
| Terminology | **96** | Standard Dutch atlas and school terms. Examples: *hoogtelijn, equidistantie, hoofdhoogtelijn, schaalbalk, getalschaal, mercatorprojectie, oppervlaktegetrouwe projectie, teledetectie, valse kleuren, tektonische plaat, plaatgrens, diepzeetrog, oceanische rug, seismometer, seismogram, epicentrum, haard, tsunami, pyroclastische stroom, luchtmassa, warmtefront/koufront/occlusie, isobaar, depressie/hogedrukgebied, convectiecel, ijskap, ijsplaat, morene, zwerfsteen, U-dal, opheffing, barchaan, lijzijde/loefzijde, klif, abrasieplatform, landtong, kwelder, karst, stalactiet/stalagmiet, toeslagmateriaal, era/periode, geologische tijdschaal*. The compass reads N O Z W; coordinates are written NB/ZB/OL/WL. Two points are taken off for terms where Dutch and Flemish usage differ and one form had to be chosen (*schaalbalk*), and two for a few compounds (*getijdenzone*, *aardrijkskundige breedte*) that a Flemish reader might phrase differently |
| Register / tone | **97** | Informal *je/jouw/jij* (214 forms) and **0** formal *u/uw*. Exercise stems are imperatives and questions (*Bereken*, *Leg uit*, *Teken*, *Waarom …?*). Grades 1–4 use short, concrete sentences; grades 7–9 use the lower-secondary register. *Weekendprobleem* ×20, matching English |
| Accuracy / sense | **96** | Every chapter was re-read against its twin, and every weekend problem and solution chain was recomputed from the English data and figdata. Three wordings deliberately depart from a defective English sentence (see *Canon findings*); nothing else is added, dropped or softened. All coordinator canon fixes are mirrored |
| Typography / mechanics | **97** | `` ``…'' `` quotes; decimal points kept in prose and maths; times written *6.00~uur*, with *09.00* on figure axes; *miljoen/miljard*; *publiek domein*, *Foto van …*. `\text{}` in maths is translated (14 of 14). Line-edge sweeps are clean outside TikZ code and comments |
| Link layer | **95** | **5,467 links to 137 targets.** All 136 of English's targets are reached, plus one: *geologische tijdschaal* in a g7.5 caption. That is 90 % of English's 6,102 links. The gap is structural: Dutch writes *weerbericht, weerkaart, breedtegraad, zeeniveau* as one word, and `lang_nl` does not link inside a compound (weather 59 vs 99, latitude 39 vs 74). The homographs (*meer, weer, bron, schaal, plaat/plaats, front, afzetting, breuk*) are curated with evidence in `book1_nl.py`. `--unwrap --apply` then `--apply` is idempotent, and the dry run prints **links to insert: 0** |
| Build cleanliness | **99** | Forced `-g` build: 0 `!`, 0 undefined, 0 overfull (the last one, in the image credits, was fixed with `\slash`), nullfont equal to English, 0 missing characters, 0 invalid-in-math |

## Figures

Every translated figure label was rendered on its own page and checked against
its numbers. Collisions were fixed by shortening the Dutch label, never by
moving the geometry; for example, the g9.5 hill profile became *flauwe westflank /
steile oostflank*. Figure text that lives in figdata text columns, which no
gate reads, was translated inline under `!draw` (list below).

## `!draw` ranges (English line numbers)

g1-01 92–93, 97–98, 122–123, 136–138, 187–189, 204–207 · g1-02 228 ·
g3-01 105–109 · g3-02 63–65, 77–79 · g4-01 378–379 · g4-03 87–88, 93–95 ·
g5-01 57–59 · g5-03 168–169 · g6-01 76, 207–208, 219–220, 329–330 ·
g6-02 256 · g6-03 323–324, 328 · g6-05 273 · g7-02 476–477 ·
g7-03 208, 342–343 · g7-04 163, 322 · g7-05 423, 438, 441, 444, 512, 517, 520 ·
g8-01 133, 211 · g8-02 142, 263, 268, 391–392 · g8-03 73–74 ·
g8-04 290–291, 358–359, 504–505 · g8-05 264–266, 269 · g9-01 214 ·
g9-03 77–78, 244–247. No `!math` range remains.

## Canon findings (reported, not fixed in the English)

1. `parts/grade-1/solutions/01-watching-the-weather.tex` 44–46 gives 2 rainy afternoons, but the chart data (`parts/grade-1/01-watching-the-weather.tex` ~136) shows 3. The Dutch edition prints 3.
2. `parts/grade-7/02-volcanoes.tex` 662–663 asks for "four percentages", but the proposition (493–496) prints three. The Dutch edition names the three plus the 0.5 % of unknown setting.
3. The g7-05 solution to problem 6 now reads "26 March", but body line 532 and `figdata/out/grade-7-earth_calendar.dat` give 25 March (day 83.6 from 1 January = day 0). The Dutch edition mirrors the canon.
4. Figdata text columns hold visible English that no gate checks (g3-02 globe; g6 planet sizes, cities map, water-table labels; g7 volcano settings, quake counts, time-scale labels, earth calendar; g8 standard atmosphere; g9 climate-record decades, concentrations). The Dutch edition translates them inline under `!draw`.
5. `parts/grade-7/03-earthquakes.tex` 454 calls Colombo the capital of Sri Lanka. The legislative capital is Sri Jayawardenepura Kotte.
6. English links "mouth" (of a bay) to the river-mouth definition (`parts/grade-9/04-landforms.tex`, 4×) and "weathers" in g1-01:347.

## Coordinator addendum (2026-10-25, after wave 1)

Re-verified by the coordinator after the wave-1 canon fixes and tool changes:
- a forced build: 335 pp, 0 errors / 0 undefined / 0 overfull, nullfont 6,633, `.fls` 64 = 64;
- `check_translation.sh` 9/9 PASSED under the stricter gates (per-range `!draw`, the 12-character dup tier, the whole-word tokenizer);
- relinked with the multilingual Part-heading protect: **5455 links**, 138 targets (English's 137 plus the time-scale definition, which English never links), dry run 0. The date-line EXTRA was added by the coordinator, to match English's new EXTRA (5 links).

The coordinator mirrored the canon fixes listed in `sources/WAVE1_FINDINGS.md` §1 into this edition, among them the problem-6 date (**25** March, which reverts the first fix to 26) and the three rainy afternoons. The score is unchanged.

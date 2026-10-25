# Wave 1 findings — Earth & space Book 1 (fr, nl, es, pt)

These findings bind wave 2 (hi, ar, id), on top of `TRANSLATION_BOOK_1.md`.
The coordinator wrote them from the four wave-1 reports and its own
verification (2026-10-25).

Wave 1 delivered four editions, each at 96/100:

| Edition | Pages | Links | Targets |
|---|---|---|---|
| fr | 340 | 6,003 | 137 |
| es | 339 | 6,071 | 138 |
| pt | 336 | 6,065 | 138 |
| nl | 335 | 5,455 | 138 |

The English source has 324 pages and 6,103 links over 137 targets, now
including the date line. es, pt and nl also link the time-scale definition,
which English never reaches, and each edition's date line has an EXTRA for its
short form (5 links, as in English). Add one for yours. Each edition was verified by the coordinator:
- a forced build at 0/0/0, with nullfont 6,633 (the English baseline) and
  `.fls` = 64 = the files on disk;
- `check_translation.sh` green for all nine grades;
- a linker dry run at 0.

## 1. English-canon fixes made during wave 1

All of these fixes were made in place, with the line count unchanged, and
mirrored into every delivered edition. Your English source already carries
them, so translate the text as it now reads.

| File | Fix |
|---|---|
| grade-1/solutions/01 exo 8 | **3** rainy afternoons (Monday rain, Friday showers, Sunday rain: the chart's `\foreach` data), not 2 |
| grade-7/02 proposition "where" | "For the last 6 (0.5~\%) the setting is not known." Exercise 5(c) and its solution add four percentages |
| grade-7/03 l.454 | Colombo is "the largest city of Sri Lanka", not its capital |
| grade-7/05 l.75–76 | Superposition is credited to Steno (1669), not Hutton: "The first was stated by Nicolas Steno in 1669; Hutton built on it at the end of the eighteenth century." The ledger line is now `% ledger: usgs:hutton-smith, og:stratigraphy-principles` |
| grade-7/05 caption l.28–30 | "Hutton saw each layer as a span of time, with the oldest at the bottom wherever the layers have not been turned over." |
| grade-7/solutions/05 pb 6 | "83.9 days (83.6 with the unrounded 12.44). January and February make 59 days: 24.6 to 24.9 days into March, on **25 March**." This uses solution 7's convention and matches the figure. A first fix to "26 March" (from rounding to 84 first) was wrong and has been reverted |
| grade-8/solutions/03 exo 11(a) | **1350 km**, "four and a half scale bars" (the map's L and H centres are 1352 km apart) |
| grade-8/01 l.292 | The top of the mesosphere is at **−86 °C**, as solution 2(d) and the figure have it |
| grade-8/solutions/04 exo 7(c) | "between **1200** and 2700 m" (3500 − 2300) |
| grade-9/solutions/03 l.111 | `\textbf{20 years}` moved out of math: `= 20$: \textbf{20 years}.` |

Left as they are: grade-9/solutions/04 pb 10 ("2043", defensible), and the
link on "weathers" in g1-01 (the weather-type sense).

## 2. Figdata tables carry English visible labels

The following tables are read by `meta=name`, `nodes near coords`,
`yticklabels from table` or `point meta`, and the text they print is English:

- `grade-3-globe-*-labels`, `grade-6-cities-map`, `grade-6-planets-sizes`,
  `grade-6-water_table-fresh`, `grade-6-water_table-well-labels`;
- `grade-7-volcano_settings`, `grade-7-quake_counts`, `grade-7-time_scale-*`,
  `grade-7-earth_calendar-*` (months and tag);
- `grade-8-standard_atmosphere-*` (levels and layers),
  `grade-9-climate_records-decades` (the "1880s" column),
  `grade-9-concentration` (metal names).

No edition can translate a `.dat` file. Every wave-1 edition replaced the
table-driven label with explicit `\node`s or an explicit `yticklabels={…}`,
copying the coordinates from the `.dat` rows, marked that line range
`!draw`, and then checked the rendered page against the English one, label
by label. The four editions' `!draw` ranges are almost the same list (see
their score files), so start from it. In the census, a drop in `\addplot`
count and a rise in `\node` count are expected. Nothing else is.

## 3. `!draw` is now per range (`id_apply`, installed after wave 1)

Until now, one `!draw` range anywhere in a file disabled the drawing census
**for the whole file**. That is how the Spanish edition silently lost a full
`\draw[arr] (q1) -| node{no} (q3);` arrow in grade-6/03, and how French lost
a leader line in grade-7/02, which the French agent caught itself.

`id_apply` now compares drawing code on a hybrid file in which every `!draw`
range is put back to English and every other range is your translation. So:

- **every range that changes drawing code needs its own `!draw`**. This
  includes a `\foreach` label list, an explicit `yticklabels` list that
  replaces `from table`, a widened node option, or an inline label table;
- a translated `\foreach` list in an unmarked range is now REJECTED, even if
  another range of the same file carries `!draw`.

Node text inside a calc coordinate, `at ($(P)+({sin(40)*1.15},{0})$) {…}`,
is now blanked like any other node text. The coordinate pattern had allowed
only one level of nested parentheses.

As a check of your own, run the coordinator's per-file census

    python3 /tmp/claude-1000/-home-bvirrion-repositories-one-course/59cf54a9-12e3-4394-994b-a781f186173c/scratchpad/coord/drawcensus.py <lang>

and explain every difference that is not a node difference in your score
file. An en dash inside label text ("2020--25", "Peru--Chile") counts as an
extra `--`.

## 4. Gate and tool fixes installed after wave 1

- `id_apply` `brace_balance`: `\\}` (a row separator, then a closing brace)
  used to read as an escaped `\}`. It no longer does, so you do not need the
  `\\ }` workaround.
- `check_latin_prose`:
  - **Whole-word tokenizer.** Words are now bounded by any Unicode letter,
    not just ASCII. "Utqiaġvik" no longer yields the fragment "vik", and
    "Schröder" no longer yields "der". (This matters for `id`: the
    Indonesian gate is separate, but the twin-comparison logic is the same
    idea.)
  - **The dup tier** ("English line kept beside its translation") had a
    40-character, 4-word floor. Two kept English lines slipped under it: nl
    had "even in a moment.", and the shipped biology Book 1 pt edition had
    "And when a scraped knee heals?", now fixed. The floor is now 12
    characters and 3 words.
  - **`MATH_ENV_CLOSE`** no longer matches the `\]` of `row sep=\\]`.
- `check_translation.sh`: the drafty-"..." check exempts
  `\pgfplotsinvokeforeach`.
- Weekend-problem headings: the Part-heading protect knew only "Part", so es
  and nl had linked terms inside their *Parte*/*Deel* headings. It now covers
  `Part|Partie|Parte|Deel|Bagian|भाग|الجزء`, followed by a **Roman numeral**.
  Keep the Roman numeral in your heading (`\textbf{भाग II --- …}`), or add
  your own protect if your heading spells the number out (Arabic الجزء
  الثاني).
- Not fixed: the blocking axisstr tier fires on symbolic coordinates that are
  never printed (g8/05). Rename them to ASCII keys under `!draw`, as pt did,
  or keep the English keys.

## 5. Link layer

- **Run `--unwrap --apply`.** `--unwrap` without `--apply` is a dry run and
  changes nothing. If you then `--apply`, you link on top of stale links.
- **`EXTRA_PROTECT` is one alternation scanned left to right.** Of two
  overlapping patterns, the earlier one hides the later one: pt's
  "própria escala" hid "escala do tempo". Merge overlapping phrases into one
  pattern.
- **`WORD_TAIL` over-reach.** Dutch `(?:e?[ns])?` turned EXTRA "plaat" into
  "plaats" (place), about 50 false links. After every EXTRA, check the
  frequency census for a jump.
- **Morphology.** `WORD_TAIL` cannot generate a plural whose accent shifts
  (es *volcán → volcanes*) or any irregular plural. Add such plurals as EXTRA
  entries.
- **The weather/time homograph.** French *temps* and Spanish *tiempo* mean
  both, so the time sense had to be masked and the weather target ended well
  below English (fr 36, es 77, en 99); nl's 59 comes from compounds. Hindi
  मौसम/समय, Arabic طقس/وقت and Indonesian *cuaca*/*waktu* are separate words,
  so expect to come close to 99. If you fall far short, find out why.
- **Other homographs met.** *scale* (map, Mohs, magnitude, axis); *front*
  (weather, glacier snout, cliff); *plate* (tectonic, ice, glass); *era* (a
  verb form); *longitude*/length; *globe*/balloon; *Ecuador*, the country.
  Find your own with the two censuses.
- **English link changes.** English gained `EXTRA "date line"` (5 links) and
  a protect on "mouth of a bay" (4 links to the river-mouth definition
  removed).

## 6. Build environment

This TeX Live has no `french.ldf`, `spanish.ldf`, `dutch.ldf` or
`portuguese.ldf`, so the Latin-script editions build without babel and
hyphenate with English patterns locally. CI's full TeX Live has them. hi, ar
and id load their own setups and are not affected. Build only through the
shared wrapper.

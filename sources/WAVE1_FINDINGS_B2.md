# Wave 1 findings — Earth & space Book 2 (fr, nl, es, pt)

These findings bind wave 2 (hi, ar, id), on top of `TRANSLATION_BOOK_2.md`
(and, through it, `TRANSLATION_BOOK_1.md` and `WAVE1_FINDINGS.md`). The
coordinator wrote them from the four wave-1 reports and its own verification
(2026-10-25).

Wave 1 delivered four editions at 96/100, each verified by the coordinator on
its own forced build in a fresh output directory (0 errors / 0 undefined /
0 overfull, nullfont 3,291 = English, non-backtick Missing character 0,
invalid-in-math 0, `.fls` = 56 = files on disk), `check_translation.sh` green
for grades 10–12, linker `--check` clean and dry run 0:

| Edition | Pages | Links | Targets |
|---|---:|---:|---:|
| nl | 374 | 2,094 | 135 |
| es | 375 | 2,168 | 138 |
| pt | 373 | 2,249 | 137 |
| fr | 380 | 2,263 | 138 |

**English now: 362 pages, 2,208 links over 136 targets** (it was 2,187 / 135
at the start of the run; the changes are in §2). The editions reach every
English target. fr, es and pt also reach *magnetic anomaly*, which English cannot
link without mislinking a paper title (see §2).

## 1. English-canon fixes made during wave 1

All were made in place, with line counts unchanged, and mirrored into every
delivered edition. Your English source already carries them.

| File | Fix | Found by |
|---|---|---|
| `frontmatter/image-credits-book2.tex` l.76 | "the history of the estimates after Dalrymple, as summarised by Wikipedia" → "from Holmes (1913, 1927), Patterson (1956) and the U.S. Geological Survey" — the figure's real ledger sources. Your stand-in already carries the new English; translate it | nl |
| `grade-12/solutions/04` l.130 | "(144.1 − 143.7) × 86.4 ≈ **35** km" (was 33, from the unrounded 143.72) | pt |
| `grade-12/solutions/05` answer 17 | "29 × ln 10 ≈ **67**" (was 68, from the unrounded 29.33) | pt |
| `grade-12/solutions/06` exo 12 | "Total about **56.7** TW" and "(21.2 + 8.1)/**56.7**" (the four printed terms sum to 56.7) | pt |
| `grade-12/02` l.511 | `\qty{35} to \qty{40}{km}` → `\num{35} to \qty{40}{km}`. A `\qty` with no unit takes the NEXT LETTER as its unit: English printed "35 t" + "o", nl "35 t" + "ot", es/pt "35 a" with a thin space; in French `\qty{35} à` crashed the build (a UTF-8 byte as a unit). The only such site in the canon | fr |
| `grade-12/05` l.102 | stale comment `miss_before_1900_m_per_myr 51.6` → 55.8 (figdata 55.801; nothing printed changes) | pt |

All four numeric fixes are inside math spans: your English twin already has the
new bytes, so `id_apply` will simply expect them.

Checked and left as they are: "the Suiko seamount alone lying 4860 km from
Kilauea" (g11/04:420, correct English).

## 2. The English link layer changed (book2_en.py)

- **Capital-harvest trap, twice.** The definitions of *cleavage* and
  *migration* open on the capitalised display (`\emph{Cleavage}`,
  `\emph{Migration}`), so English linked the lowercase noun 1 time out of ~30
  and 0 out of 4. EXTRA *cleavage(s)* and *migration* were added (cleavage now
  24 links, migration 4). **Check your own definitions of these two**: nl had
  the same trap with *Splijting* and *Migratie* and needed EXTRA entries
  (`splijting`, `splijtrichting(en)`, `migratie`). The other nine capitalised
  English definitions (*Saprolite, Decompression melting, Ridge push, Eclogite,
  Fracture, Rhyolite, Coalification, Schistosity, Regional metamorphism,
  Diagenesis, Mantle convection*) were audited: none leaves a lowercase use
  unlinked outside its own definition, so they need no action unless your
  wording creates one.
- **Wrong-sense links removed by protects**:
  - "its slab pulls it down" (g12/02:33), "the whole slab pulls" (g11
    solutions/06:160) — a noun and a verb, not *slab pull*;
  - "A slab of black shale" and "the slab is about 10 cm across" (g11/09:10, 26)
    — a slab of rock, not the subducting slab;
  - "heat flows out of", "Heat flows from hot to cold" (g12/06:20, 48) — the
    verb, not the measured *heat flow*.
  Your language will have its own versions (*la chaleur s'écoule*, *el calor
  fluye*): read every link to `slab`, `slab-pull` and `heat-flow` once.
- **EXTRA** "pull of the sinking slab" → slab pull (g11 solutions/06:56, the
  defined force in other words).
- Not added: *magnetic anomaly*. English's caption "Magnetic anomalies computed
  across…" (g11/01:369) is the defined sense, but the same capitalised phrase
  is the title of Vine and Matthews's paper in an `\emph` (l.269), which must
  never link. es and pt link the caption; that is correct.

## 3. Figures, labels and the draw census

- **Every wave-1 edition found label collisions on the rendered pages** (pt
  15 figures, es 12), almost all from translated labels being longer than the
  English ones: isochron slope labels (g12/07), the thunderstorm legend
  (g10/05), upwelling labels (g10/06), the oil-system labels (g11/09), the
  Sunda Shelf label (g12/09), dip labels (g11/06). Fix inside the node text
  (shorter wording, or `\shortstack{…\\…}`), which leaves the drawing code
  byte-identical. pt's method is worth copying: list every translated label
  more than ~25 % longer than its twin, then read each of those pages.
- **The draw census's "differences" are English words inside node text that it
  reads as TikZ keywords**: *core--mantle boundary* (`--`), *small circle*,
  *(circle)* (`circle`), *volcanic arc* (`arc`). Your translation removes them,
  so expect 4–6 files to differ in `--`, `circle` or `arc` counts and nothing
  else.
- **The `!draw` ranges were nearly the same in all four editions** (English
  line numbers): g10/02 133–134 (explicit `xticklabels` for the planet
  symbolic coords) and 299; g10/03 226–229; g10/05 58; g11/08 153, 162–169;
  g12/01 122 (the `[about 70]` point meta); g12/05 272; g12/06 286–288; g12/09
  270–271 (the singular `xticklabel` key holding `\textdegree E` is NOT blanked
  by the census, so a localized longitude letter needs `!draw`). pt also used
  `!draw` for several pgfplots label lists (g10/08 329, g10/09 188–191, g11/06
  216, g11/07 634, g11/09 542, g12/01 117, g12/05 85–87, g12/06 170, g12/10
  200–202, 396–397) where nl/es did not need one.
- **`bandB…bandF`**: the two colour `\foreach` lists of the g12/02 fold block
  diagram tripped `check_latin_prose`'s blocking foreach tier in every Latin
  edition (they are colour names, never printed). nl, es and pt each appended
  the same `ALLOWED_BY_LANG` entry. Not relevant to hi/ar; id may need it in
  `check_latin_prose` (gate 9 runs for id too).
- es broke long labels and table headers with `\shortstack` (11 sites); pt and
  nl tightened wording instead. Both are fine.

## 4. Register and terminology decisions worth reusing

- **IPCC calibrated language**: every edition used the IPCC's own published
  terms in its language (*very likely*, *virtually certain*, *high/medium
  confidence*), consistently; nl matched its Book 1 g9 wording. Find the
  official AR6 rendering in your language (the IPCC publishes summaries in
  Arabic; for Hindi and Indonesian use the established national usage) and
  keep it constant.
- **Paleoclimate interval acronyms** (PETM, EECO, MPWP, LIG, LGM, MH) and SSP
  scenario codes stayed in English in es and pt, with a caption note "English
  acronyms of the IPCC" and the full name translated. Do the same.
- **Book 1 cross-references**: es writes «(Libro 1, año N)». Use your Book 1
  part-title wording.
- es and pt kept the decimal point in prose, as in their Book 1 editions.
- Thunderstorm: Spanish *tormenta* is any storm, so only *tormenta eléctrica*
  links (2 against English's 12). Expect similar density shifts where your
  language's word is broader or narrower than English's.

## 5. Tools

- No shared-tool bug was found in wave 1 beyond the pre-run fix
  (`check_latin_prose` reading `\\word` as a macro).
- es found a bug in its own scratch script (a range starting inside math
  joined the next `@@` header): keep every patch range starting and ending
  outside math.

## 6. From the French report (last of wave 1)

- **Exercise register follows the sister series' SAME-GRADE volume, not Book
  1.** French moved from Book 1's collège *tu* imperative to the infinitive
  stems (*Définir, Calculer, Expliquer*) that French Biology Book 2 uses for
  the same three grades. Measure your instruction mood against your language's
  Biology Book 2 (`../one-biology-book/parts/grade-1{0,1,2}/<lang>/`) and its
  score file, and record the choice.
- **Units inside math spans stay as English writes them.** `\unit{cm/yr}`,
  `mm/yr`, `m/Myr` inside `$…$` or a display are frozen by the math census, so
  a French page reads "an"/"Ma" in prose and "yr"/"Myr" in four formulas
  (g11/05 ~376, g12 solutions/02, g12/05 161, g12 solutions/05 94 and 100).
  They are unit symbols and are acceptable; do not spend a `!math` on them.
  hi and ar: they print in Latin script like every other unit.
- **One ambiguous term, two senses by chapter.** French *roche mère* is both
  the soil parent rock (g10/07) and the petroleum source rock (g11/09); with
  `nearest-preceding`, the g12/03 uses would go to the wrong one, so French
  protected them (3 links fewer). If your language uses one word for both
  (check Hindi मूल शैल, Arabic الصخر الأم, Indonesian *batuan induk*), do the
  same.
- **Density above English, each read and correct**: *clivage* 35 against 24,
  *orage* 20 / *éclair* 15 against 12 / 10 (own chapter), *migration* 6
  against 4. fr STOPs *orage* outside its chapter, because it also renders
  English "storm" in g10/07–08.
- **Plurals the morphology cannot form** went into `DERIVED` (*cyclones
  tropicaux, panneaux plongeants, minéraux argileux, phénocristaux*): the same
  lesson as Book 1's *volcán → volcanes*.
- fr cleared 10 overfull boxes on a single-chapter probe (shorter table and
  tick-label wording, one reworded proof sentence) — the probe loop in
  `translation_instruction.md` works here too.


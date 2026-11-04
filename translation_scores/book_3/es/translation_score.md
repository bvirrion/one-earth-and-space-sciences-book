# Translation score — One Earth and Space Sciences Book 3 · Spanish (`es`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 3 (University, Year 1, `bachelor-1`) |
| **Language** | Spanish (`es`), peninsular; impersonal *se* and subjunctive in exercise stems; terms as in the Spanish Book 2 (`parts/grade-1[0-2]/es/`) |
| **Model (drafting)** | claude-haiku-5-5, effort high |
| **Coordinator** | claude-opus-5-5 |
| **Overall score** | **95** |
| **Ship threshold** | ≥ 95: met, with the open items listed below |
| **Scope** | 29 chapters and their 29 solution files (58 files); term layer (4,538 links); image credits; bookline `Libro 3: Universidad -- Primer año` (entry file, unchanged) |

## Build (forced, TeX Live 2026, wrapper, build `es-8`)

- rc 0, **495 pages**; errors 0; undefined 1 (`Font shape T1/lmr/bx/sc undefined`, the font-shape baseline, not a reference); **overfull 0**; nullfont 0; missing characters 0; invalid-in-math 0; zero-height 0.
- `.fls` lists 58 translated files = the 58 on disk.

## Gates

- `tools/check_translation.sh bachelor-1 es`: **PASSED**. Latin prose gate: no multi-word findings; the one-word tier is advisory and was read (`Seeing` ×2 kept as the astronomical term, `Mineral` a cognate, node and legend one-word hits are cognates, proper names or units).
- `tools/gates.sh bachelor-1`: **OK**.
- `tools/check_term_display_drift.py`: 106 targets show more than one display. The tool itself flags most as inflection or as variation the English also has. Not every line was read individually.

## Measured censuses

- **Term links.** English: 4,650 links on 184 targets. Spanish: 4,538 links on 187 targets. Every English target is reached. Three Spanish-only targets, each explained: `parcel` (*partícula de aire*: English uses the bare word "parcel" in its text and the phrase only in its definition); `circumpolar` (*estrella circumpolar* kept in one exercise, where English says "circumpolar"); `ridge-classes` (the English heading "Fast-, slow- and ultraslow-spreading ridges" is not a harvestable term, the Spanish defines three terms).
- **Per-target outliers** (over 1.5× or under 0.5× English), each read in context, all senses correct: cross-bedding 21 vs 8 (*estratificación cruzada* is the translation throughout); facies 2 vs 1; trend-plunge 36 vs 76 (0.47: *dirección* is an ordinary word, so only its trend uses are linked, and *inmersión* carries the plunge); ts-diagram 15 vs 7 (*masa de agua*, 10 uses); detector 10 vs 2 (*relación señal-ruido* throughout); extinction 16 vs 8 (*masa de aire*); moc 3 vs 1; ionic-potential 4 vs 2.
- **Homographs** fixed in `tools/term_config/book3_es.py` (EXTRA_PROTECT, STOP, EXTRA; the file's docstring lists each sense): *longitud* as length (about 120 wrong-sense links removed; geographic uses kept); *estable* (ordinary "steady"); *declinación* magnetic (ch. 1 and ch. 6); *dirección* (ordinary direction, trend kept); *correlación* (ch. 24, generic) and *ambiente de depósito* (not facies) stopped; *grupo* (working group, nanofossil groups) and *miembros* (voting members) protected.
- **Accepted losses** (correct senses no longer linked): the ch. 5 *correlación* link (log correlation); *altura* (altitude) outside ch. 1; the ch. 8 table cell *birrefringencia* (hyphenation hint breaks the match); geographic longitude now 133 links vs 177 English (latitude carries the target).
- **`\index{}` keys:** 449 Spanish = 449 English, equal per file. Line-broken keys: 0 (four joined: *contacto (geológico)*, *unidad cartográfica*, *unión triple estable*, *escala de tiempo de polaridad geomagnética*).
- **`\text{}` census:** course 187 = 187 English; solutions 580 = 580 English.
- **Figure text:** node, legend and axis-label scan finds no English word (only the chron name `C2An`).

## Fixes made in this pass

- **Overfull boxes, 20 → 0.** Body and solutions by rewording before the formula (ch. 1, 4, 6, 12; solutions 4, 7, 9, 10, 11, 12, 15), a hyphenation hint in one table cell (ch. 8), figure labels split or shortened (ch. 21, 22, 29), shorter table headers (ch. 23: *porosidad inicial*, *densidad*), a `\shortstack` header (ch. 24). In ch. 22 the photograph in the es figure is 6.6 cm high (English 6.9 cm), because it overhung by 6.7 pt. Ch. 20 sentence tightened as the coordinator asked: "se limpia con ácidos que eliminan el berilio formado en el aire".
- **English left in the Spanish edition, removed:** the ch. 20 critical-value paragraph (new range); two duplicated English exercise items in ch. 6 (their Spanish versions were already present); the ch. 12 table header; the ch. 4 and ch. 8 weekend-problem part headings; the ch. 22 section title "Evaporites"; the ch. 27 and ch. 29 proposition titles; the ch. 29 foreach labels (`warm`, `cold`).
- **Defined terms restored** so they link: ch. 14 "losa en subducción" (and solution 18), ch. 16 "modelo de Tierra de referencia".
- **Native pass** (ch. 27 course text and solutions of ch. 28): corrected "refleja directamente una fracción de vuelta" → "refleja de vuelta al espacio una fracción"; "El cuadrado de la figura" → "El recuadro de la figura"; solution 28 (6c) "momento angular que sobrante" → "momento angular de sobra". Register consistent with the earlier chapters (impersonal *se*, subjunctive in exercise stems).
- **Figures:** ch. 21 caption node moved clear of the axis label; ch. 29 deep-water label shortened to "agua profunda inferior, hacia el sur" (the two-line version collided with the bottom label). Both checked on rendered pages.
- **Rulings kept:** ch. 26 solution 6's 56010 Pa (0.03 %, rounding); the ch. 27 cap figure drawn for the north cap, with the Spanish caption faithful to English.

## Open items (why the score is 95, not higher)

- The native read covered ch. 27 (course text) and solutions of ch. 28 in full; the other chapters were checked by the gates, the censuses and spot renders (ch. 21 figure, ch. 23 table, ch. 24 ICS chart, ch. 29 figure), not read end to end.
- English bibliographic titles are kept on purpose: ch. 4 (Smith's 1815 map title), ch. 17 (*The Dynamics of Faulting and Dyke Formation*), ch. 22 (*The Structure and Distribution of Coral Reefs*), ch. 28 (*An essay on the winds and currents of the ocean*).
- The 106-target display-drift list was not individually read; most variants mirror English.
- The accepted losses above (one correlation link, altitude outside ch. 1, one table-cell link, part of the geographic-longitude links) are the price of the homograph protection; they are documented in `book3_es.py`.
- Trend-plunge at 0.47 of English: a judgement on an ordinary word, documented above.

## Coordinator verification (claude-opus-5-5, 2026-10-27)

Accepted at 95 after the coordinator's own checks and four fixes the agent's gates could not see:

- `es/09:617`: a doubled clause beginning with the English words "inner-core boundary" removed.
- `es/07:421`: the mineral table's header row was entirely English; now *grupo, términos extremos o ejemplo, clase, densidad, dureza, exfoliación*.
- `es/19:420`: the `inthelab` title "Identifying clay minerals by X-ray diffraction" translated.
- `es/22` and its solutions: the anglicism *ooze(s)* replaced by *fango(s)* (calcáreo, silíceo) throughout, with the plural agreement of "ooze silíceos" fixed; the term layer was regenerated (4,539 links, dry run 0).

Checks: every number token of the 29 solution files matches English (one number spelt out at a sentence start); an English-function-word sweep of the visible source text and two PDF-text sweeps (English figdata labels; English-only words rare in the edition) are clean apart from technical loans (*bias*, *datum*, *const*). Final build (TeX Live 2026, forced): 495 pp | 0 errors | 1 undefined (the babel-spanish font-shape baseline) | 0 overfull | nullfont 0 | missing-char 0 | invalid-in-math 0 | zero-height 0 | `.fls` 58. `check_translation.sh bachelor-1 es` PASSED. Rendered and read: the ICS chart, the heat-flow table, the streamfunction chart.

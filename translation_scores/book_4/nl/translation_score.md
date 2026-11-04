# Translation score — Earth and Space Sciences Book 4 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 4 (University Year 2, `bachelor-2`) |
| **Language** | Dutch (`nl`), Netherlands Dutch (Flemish forms swept out, list below) |
| **Scope** | 31 chapters + 31 solution files = 62 files. Phase A wrote them through `tools/id_apply.py` as line-range patches against the English twin (`draft/b4-run/nl4/p/`). Phase B/C/D edits were made directly in the `.tex` files and logged in `draft/b4-run/nl4/PROGRESS.md`. **The patches are stale and must never be re-applied** |
| **Model** | `claude-opus-5-5` (Opus 5.5, effort high), one agent per edition; coordinator `claude-opus-5-5` |
| **Overall score** | **96 / 100** |
| **Ship status** | Meets the threshold of 95. Every chapter and every solution file was read sentence by sentence against the English (phase C). The mechanical gates pass, and every English link target is reached |
| **Date** | 2026-10-30 |

## Build (forced, TeX Live 2026)

Final forced build `nl-9` (`draft/b4-run/tools/build.sh`, scratchpad), after the last edit:
**504 pages; 0 errors, 0 undefined references, 0 overfull boxes**; nullfont 0; missing characters 0
(backtick 0); invalid-in-math 0; zero-height 0; `.fls` lists 62 translated files = 62 on disk.
English for comparison: 484 pp; French 509 pp.

## What was verified (after the last edit)

- `bash tools/check_translation.sh bachelor-2 nl`: **PASSED**. Latin-prose gate: no multi-word findings.
  The one-word tier is advisory and was read: cognates (*magma*, *pluton*, *hotspot*, *molasse*,
  *thermocline*, *craton*), cloud genera, place names, and unit legends (`\qty{10}{Myr}`).
- `bash tools/gates.sh bachelor-2`: OK.
- Term layer: relinked after the last text edit, **1,965 links across 61 files, 193 targets**
  (English 2,019 / 191). Linker dry run: `links to insert: 0`. Every English target is reached. nl also
  reaches *zeldzame aarde* (b2.03 `ree`) and the tsunami definition (b2.28), which English never reaches.
  Dutch writes compounds as one word, so some English two-word links have no free-standing Dutch
  surface. That accounts for the 2.8 % gap.
- `engsweep.py nl`: 2 lines, both copied titles (*Volcanoes of the World*; *Carbon Dioxide Capture and Storage*).
- `numdiff.py nl`: every difference is deliberate. Cross-volume references (*Year 1 volume* → *Boek~3*,
  *Year 3 volume* → *Boek~5*, *Book 2* → *Boek~2*). Thousands separators in the Enewetak/Funafuti depths
  (4,158 → 4158). The explicit node values of the supercontinent (ch15) and extinction (ch19) charts.
- Census (`census.py nl`): the identical index keys and `\text{}` tokens were all checked. They are
  names (*Lagerstätte*), Dutch cognates (*tonnage*, *placer*, *poikiloblast*, *sediment*, *water*) or
  symbols (*sil*, *and*, *grt*, *liq*, *const*).
- Drift check (`check_term_display_drift.py`): 65 multi-display targets, all inflection or the curated EXTRA forms.

## Dimension scores

| Dimension | /100 | Notes |
|---|---:|---|
| Structural fidelity | 99 | Same line structure, labels, `\cref`s and index keys as the English. Five line-broken `\index` keys were joined at the final gate (msg1 rule). |
| Terminology | 96 | Fixed book-wide during the reading: one spelling each for *rhyoliet*, *Fanerozoïcum* and *craton* (the owner chapter's term; 7 *kraton* changed, which also gave 3 new links). Name compounds take a capital, as in *Köhlerkromme*, *Harkerdiagram* and *Bergeronproces*. Year-volume recall headings use one pattern. |
| Register / tone | 96 | The course text is impersonal (*men*, passive, an occasional *we*) and the exercise stems are imperative, as in Book 3 nl. There is no *je*/*u* (one *Stel je* in ch02 was changed to *Neem*). |
| Fidelity / accuracy | 96 | The arithmetic of every solution file was checked against the English, by script for ch24–31. Seven canon reports, two of them fixed upstream. All coordinator canon edits are mirrored. |
| Figures | 94 | Every figure page was rendered and viewed per chapter in phase A probes. Labels that ran long were shortened inside their nodes (ch22, 26, 28, 29, 30). msg4's ch03 legend now breaks over two lines and was re-rendered. The whole book was not re-rendered page by page after phase C. |
| Typography | 97 | 0/0/0 throughout; `Boek~N` ties; `\cref` without an article and without its own noun. |

Overall: (99 + 96 + 96 + 96 + 94 + 97) / 6 = 96.3 → **96**.

## Conventions

- Cross-volume references: *Year 1 volume* → *Boek~3*, *Year 3 volume* → *Boek~5*, the school
  volumes → *Uit de schoolboeken*. Sister series: *Uit de natuurkundeboeken / scheikundeboeken /
  wiskundeboeken / biologieboeken*. A sister series' year volume: *Uit het scheikundeboek van het
  tweede jaar universiteit*, and in parentheses *(scheikunde, eerste jaar universiteit)*.
- Units are exactly as in the English: Ma for dates, Myr for durations, Gyr, kyr and yr, in prose and in formulas.
- Coordinates are written NB/ZB/OL/WL, and the compass N O Z W, as the recorded convention of Books 1–2 nl.
- *nappe* → *dekblad* (as Book 2 nl); *dyke* → *gang*; *thin/thick-skinned* → *dunhuidig/dikhuidig*;
  the chapter-31 title follows Book 3 nl ch06: *Veldwerk- en laboratoriummethoden II*.
- **Netherlands Dutch, not Flemish.** Swept book-wide:
  - *besluiten (dat)* → *concluderen*;
  - *gelijkaardig* → *soortgelijk*;
  - *vanaf dan* → *vanaf dat moment*;
  - *voorzien* → *voorspellen*;
  - *doorheen* → *gedurende / in de loop van*;
  - *gekend* → *bekend*;
  - *terug op* → *weer op*;
  - *op het einde* → *aan het eind*;
  - *plots(e)* → *plotseling(e)*;
  - *vertrekken van* → *uitgaan van / starten vanuit*;
  - *tegen de wijzers van de klok in* → *tegen de klok in*;
  - *voorbijsteken* → *sneller gaan / inhalen*;
  - *welbepaald* → *welomschreven*;
  - *bijkomend* → *extra*;
  - *labo* → *laboratorium*.
- `%`-joined hyphenated words (sol24 *pro%mille* and the like) are left as they are.
- The `0:` anchor in TikZ `label={[…]0:…}` under a `!draw` range is accepted (coordinator msg1).

## `!draw` ranges

- ch02 course 373–377: the `\foreach` stage labels from dust to planets.
- ch03 course 101–102: the Goldschmidt legend `\foreach`. msg4: "geen stabiele isotoop" is now `\shortstack[l]{geen stabiele\\isotoop}`, rendered clear of the B cell.
- ch11 course 63 and 68.
- ch15 course 416–422: the supercontinent names, as explicit nodes (mirrored from fr).
- ch19 course 468–470: the extinction labels, as explicit nodes (mirrored from fr).
- ch23 course 100 and 206–208: the panel titles.
- ch24 course 156: the panel titles.

`--force-classes` was never used.

## English canon

Fixed upstream and mirrored:

- **sol23 exo 11.** The area is 6.17e12, not 6.18e12, and Q is 5.05e21, not 5.06e21 (my report).
- **ch28 l.493, Weibull proof** (my report, confirmed). With $U = 1 - G(X)$ increasing, the m-th largest peak would map to the m-th *largest* U. The fix is $U = G(X)$ with $G$ decreasing.
- **The other msg3 edits:** ch26 l.533 (node `axis cs:55.52,-2.9`), sol28 l.104–105 (0.0672) and sol31 l.123 (0.36).

Reported and not edited (minor, the "unrounded value" class, kept as English):

- **sol06 pb 7.** The text prints 1.67 + 2.02 = 3.68.
- **ch05/ch06.** One rhyolite saturation pressure is printed as 129 MPa in ch05 and 127 MPa in ch06.
- **sol05 pb 14.** The text prints 58 m; the printed path gives 57 m.

## Tooling

- `tools/check_latin_prose.py`: one append-only entry, `ALLOWED_BY_LANG["nl"]`, "Book 4 nl". It mirrors
  the fr/id/es/pt entries: *daito*, *jima*, the ICS colour keys, *grt*, *cumulo*/*nimbus*, *tonnage* and
  *microcontinent*. This gate has no phrase list, so the two place-name fragments went into the per-language
  set, as every other Book 4 edition did.
- No tool bug found.

## Departures from Books 1–3 nl

- Coordinates use NB/ZB/OL/WL, as Books 1–2 nl. Book 3 nl was mixed.
- *craton* replaces Book 3 nl's single *kratons*, because the owner chapter of this book defines *craton*.

## Limits

This reading is by an AI reader, not a native one. A native reading of the whole book is still the
recommended step before a ship decision.

# Translation score — Earth and Space Sciences Book 3 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 3 (University Year 1, `bachelor-1`) |
| **Language** | Dutch (`nl`) |
| **Overall score** | **96 / 100** (mean of the six translation dimensions; Links not deducted, see below) |
| **Ship threshold** | ≥ 95 — **met** (open items listed below are not deductions except as stated) |
| **Date** | 2026-10-27 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5), effort high; coordinator `claude-opus-5-5` |
| **Scope of this pass** | Last reading stint. Every part of the book has now been read sentence by sentence against the English: course text ch01–29 and solutions sol01–29. ch01–28 course text and sol25–29 were read in earlier passes. **This pass: solutions sol01–24 and the ch29 course text.** Term layer re-run after the last edit; forced build after the relink. |

## Measured numbers

| Measure | Value |
|---|---|
| Forced build (after the last edit and the term layer re-run), `nl-9` | **500 pp**; errors 0; undefined 0; overfull 0; nullfont 0; missing-character 0; invalid-in-math 0; zero-height 0; `.fls` 58. |
| `check_translation.sh bachelor-1 nl` | **TRANSLATION GATE: PASSED** (run after the build). |
| `consist.py` (patches reproduce disk) | patches checked 58; mismatches: none (re-run after the last patch). |
| English-word sweep (`engsweep.py nl`, excluding `[we]`) | empty (re-run after the build). |
| Linker | unwrap removed 3655, apply inserted **3868 links across 58 files**; dry run `links to insert: 0`. |
| Solutions numeric comparison (`numdiff.py nl solutions`) | 2 files differ, both deliberate and no value changed: sol05 explicit "boven 200 m" (the English says "above it"; same value 200 m); sol25 "Koolstof-14" (the isotope's name, English "carbon-14"). |

## Dimension scores

| Dimension | /100 | Notes |
|---|---:|---|
| Structural fidelity | 99 | Consistency and gate checks green after the last edit. Numeric diff explained (above). |
| Terminology | 95 | Closed by ruling: *etage* stays (nl Book 2 never uses *stage*). Fixed this pass: leftover English *hydrogen* (sol19); *achtvlak* (octahedron, false friend) → *octant* (sol01); *mantelsdichtheid* → *dichtheid van de mantel*, the course-text form (sol03). Open: the water-mass names differ between ch26 (*Centraal Water*, *Noord-Atlantisch Diepwater*) and ch29 (*Noord-Atlantisch Diep Water*); see open item 2. |
| Register / tone | 96 | Agreement fixed in ch29 (*warm, meanderend lint*). *Ze tellen zou* → *Ze meetellen zou* (sol20, ungrammatical verb-first infinitive). Gender and calques checked in all solutions read. |
| Fidelity / accuracy | 96 | Every number in sol01–24 and ch29 checked against the English. Added content not in the English removed (sol02 "dat wij vanavond zien"; sol13 "naar binnen gerichte"). A missing "(a)" label restored (sol15). Spot arithmetic in ch29 confirmed (0.92 PW; 9.0e-7 m/s ≈ 28 m/yr). |
| Figures | 94 | Not changed this pass; the figures were not re-rendered. The ch29 figure labels (the `!draw` ranges: Gulf Stream, Stommel gyre, overturning section, Ekman spiral, upwelling schematic) were translated and read in source; the build is clean with no overfull; label collisions were not checked by eye. |
| Typography | 97 | Unchanged. |
| Links | 83 | Reported, **not deducted**: link coverage 83 % is a linker limit, accepted by the coordinator ruling. Excluded from the overall. |

Overall: (99 + 95 + 96 + 96 + 94 + 97) / 6 = 96.2 → **96**.

## Native pass: what was read and fixed

**This pass.** Sentence-by-sentence read of the solutions sol01–24 against the English, and of the ch29 course text against the English. Fixes:

| File | Fixes | What |
|---|---:|---|
| sol01 | 1 | *achtvlak* → *octant* (octahedron is *achtvlak*; the sphere octant is *octant*). |
| sol02 | 1 | Phrase *dat wij vanavond zien* removed (not in English). |
| sol03 | 1 | *mantelsdichtheid* → *dichtheid van de mantel*. |
| sol04 | 0 | — |
| sol05 | 0 | — (heave = *horizontale verplaatsing*, as in ch05). |
| sol06 | 0 | — |
| sol07 | 0 | — |
| sol08 | 0 | — |
| sol09 | 0 | — |
| sol10 | 0 | — |
| sol11 | 0 | — |
| sol12 | 0 | — |
| sol13 | 1 | Phrase *naar binnen gerichte* removed (not in English). |
| sol14 | 0 | — |
| sol15 | 1 | Missing "(a)" label restored before *Tien keer de smelt*. |
| sol16 | 0 | — |
| sol17 | 0 | — (*dompelende plooi* is the course term). |
| sol18 | 0 | — |
| sol19 | 1 | Leftover English *hydrogen* → *waterstof* (balance check). |
| sol20 | 1 | *Ze tellen zou* → *Ze meetellen zou*. |
| sol21 | 0 | — |
| sol22 | 0 | — |
| sol23 | 0 | — (*basement* is the course term in ch23). |
| sol24 | 0 | — |
| ch29 | 1 | *een warme, meanderende lint* → *een warm, meanderend lint* (agreement). |

Total this pass: 8 fixes (sol01–24 and ch29). Solutions sol25–29 were read in an earlier pass and not reread here.

**Earlier passes (kept for reference).** ch01–28 course text sentence by sentence (about 60 fixes in ch01–26 in the previous pass); ch27–28 read in full; sol25–29 read in full; ch06, ch13, ch17, ch19, ch20, ch21 term fixes (*textuurrijpheid*, *halfruimte*, *richting*/*duik*, *laaglading*).

**Limits.** This is a reading pass by an AI reader, not a native reader. A second independent reading by a native speaker remains the recommended step before a ship decision.

## Figure work

Earlier passes only (no figure work this pass): ICS chart (ch24) explicit Dutch nodes under a per-range `!draw`; ch19 clay families caption collision fixed; ch16 label anchor fixed; ch14 English label in a plot translated; ch06, ch02, ch03, ch04, ch07, ch09, ch17, ch21, ch19 figures rendered and read.

## Link layer

- Done: *slijpplaat* (bare thin section), *tweelingvorming* (twinning), *drievoudig knooppunt* (triple junction), added as EXTRA in an earlier pass.
- Term layer re-run after the last edit: unwrap removed 3655, apply inserted 3868 across 58 files; dry run 0.
- **Link coverage 83 %**: ruled a linker limit, not a translation defect. Chapter-restricted surfaces for *attitude (dip)* and *trend-plunge* would be needed to close it; not a translation issue.

## Conventions and open items

- Programme names are not printed; *Boek 2, klas 11* is the book cross-reference the English canon also has.
- Series cross-references: *Boek N* for another series volume; *klas N* for a school grade.
- Loanwords and names kept as in the English canon: *strike-slip*, *dip-slip*, *break-up*, *Basin and Range*, *Red Rock Canyon*, *sills*, *detachments*, *tracers*, bibliography titles.
- `\text{}` census: *rms*, *CMB*, *ICB*, *OLR*, *rad*, *direct*, *transport* kept (accepted).
- Tooling touched (append-only, reported earlier): `tools/check_latin_prose.py` (ALLOWED nl *warm*, *water*), `tools/check_orphan_lines.py` (ALLOWED_ORPHAN_LINES nl, Smith's 1815 map title).

## English canon defects, reported, not fixed

1. ch29 (course text, 2nd Atlantic-to-Pacific overturning paragraph): "173.3 Sv … \qty{30}{\percent} more than that long-used value" — 173.3 / 125 = 1.39, so the excess is about **39 %**, not 30 %. The nl edition keeps the English figure; the English should be corrected by its owner.

Ruled correct in English by the coordinator (no longer open): ch27 cap caption; ch23 430 000 / 140 000; ch15 `\qty{e5}{km^2}` and `\qty{e6}{km^3}`.

## Open before shipping

1. **Figures**: the ch29 figures and the rest of the touched figures were not re-rendered in this pass. A visual check of the ch29 pages (Gulf Stream and overturning figures) is recommended.
2. **Water-mass names across ch26 and ch29**: ch26 uses *Centraal Water* (figure label and text) and *Noord-Atlantisch Diepwater*; ch29 uses *Noord-Atlantisch Diep Water* (7 uses). The series should use one form. Unifying them touches a figure label in ch26, so it needs a rebuild and a check.
3. **A second native reading** of the whole book (solutions included) remains the recommended step before a ship decision.
4. **Link coverage 83 %**: accepted by ruling; not deducted.
5. **Canon defect 1** above: the owner of the English ch29 text should correct the percentage.

Score: **96** (threshold 95 met on the translation dimensions). The figure dimension stays at 94 because the figures were not re-rendered this pass.

## Coordinator verification (claude-opus-5-5, 2026-10-27)

Accepted at 96 after the coordinator's own checks and the fixes below:

- `nl/21`: the Grand Banks history box and the Colorado pebble sentence had converted the English miles to kilometres (770, 640, 240 km), so exercise 21.4(c), "convert 480 and 400 miles", asked about numbers the text no longer printed. The miles are back (480, 400, 150 *mijl*, *binnen enkele mijlen*), and the sentence after the box again gives the conversion, *en 480 mijl is ongeveer 770 km*, as English does. Changed in the file and in `ch21.patch`.
- Earlier coordinator fixes: ch23 *zeven over de laatste 430 000*, ch26 *Centraal Water*. English canon edits 5–8 mirrored (ch20 beryllium, ch22 37–55 m, ch29 39 %, ch23 *strandzand van het begin van dit hoofdstuk* was already right).
- Rulings: link coverage 83 % (the linker cannot restrict a surface form to some chapters) and *etage* (nl Book 2 never prints *stage* as a term) are not deductions.

Checks: `numdiff` over the 29 solution files differs in two places only, both the same value (*boven 200 m*; *koolstof-14*). In the course text it differs in book cross-references (Year 3 volume → *Boek 5*), decades written out, and the ICS chart's explicit nodes. The English-function-word sweep is clean, and the PDF-text sweep shows no word that is not in the verified nl-4 sweep. Final build (TeX Live 2026, forced, `coord-nl-2`): 500 pp | 0 errors | 0 undefined | 0 overfull | nullfont 0 | missing-char 0 | invalid-in-math 0 | zero-height 0 | `.fls` 58. `check_translation.sh bachelor-1 nl` PASSED, linker dry run 0, `consist.py` clean (58 patches).

Coordinator, after the build: ch29 *Noord-Atlantisch Diep Water* (7) unified to ch26's *Noord-Atlantisch Diepwater* (file + patch; dry run 0, gate PASSED).

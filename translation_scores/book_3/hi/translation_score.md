# Translation score — One Earth and Space Sciences Book 3 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 3 (University, Year 1, `bachelor-1`) |
| **Language** | Hindi (`hi`); आप register, danda ।, Latin digits, units kept (Ma, Myr, Gyr, yr); names transliterated |
| **Model (drafting)** | claude-haiku-5-5, effort high |
| **Coordinator** | claude-opus-5-5 |
| **Overall score** | **95** |
| **Ship threshold** | ≥ 95: **met** (see the basis below) |
| **Scope** | 29 chapters and their 29 solution files (58 files); term layer; image credits (29 items) |

## Build (forced, TeX Live 2026, `build.sh`, build `hi-11`, final after the chapter 2–22 reading stint)

- rc 0, **454 pages**; errors 0; undefined 0; **overfull 0**; nullfont 0; missing characters 0; invalid-in-math 0; zero-height 0.
- `.fls` lists 58 translated files = the 58 on disk.
- Build `hi-10` (before the stint) had the same counts: 454 pages, 0/0/0, nullfont 0.
- The overfull boxes of `hi-4` (52) were cleared in the finishing run: the image credits were rewritten, and 14 solution paragraphs and 2 body paragraphs were reflowed (long formulas split at a top-level `=` into `$…$` spans joined by a space, a few formulas moved to `\[…\]`, short Hindi words added before a break). The probe builds are not the gate: the final build is.

## Chapter 2–22 reading stint (sentence-level, every chapter, this session)

- Every course-text sentence of chapters 2–11 and 13–22 was read side by side with the English twin, numbers and cross-references rechecked. Chapters 1, 12, 23–29 had been read sentence-level in earlier stints (see below), so every chapter of the book has now had a sentence-level read.
- Meaning and sense fixes (chapters 2–5, 10, 16–17, 19–21), each in the stint log: a broken CFHT phrase ("मौना के पर स्थित"); "rises" mistranslated as "सूर्योदय के बाद"; "lets sunlight through" written with the wrong sense (निकलने देता → गुज़रने देता); a doubled "से से" in an exercise; the chapter term भौगोलिक मानचित्र for *geological map* (→ भूवैज्ञानिक मानचित्र); potential temperature rendered as क्षमता-तापमान (→ विभव-तापमान); a figure caption that read "सीधे हैं" for *the right way up* (→ सही क्रम में हैं); a reversed sense "छोटे वलनों के वर्जेंस के उलट" (→ the reversals of minor-fold vergence); a triaxial-cell sentence that said "कई गुना" for *many orders of magnitude* (→ कई परिमाण-क्रम); a garbled photo caption (granite grus); a Froude-number transliteration fixed in three places.
- Consistency and typography: मॉडल spelling (ch05); feldspar names aligned with ch07 (एल्बाइट, एनॉर्थाइट); aragonite aligned with ch07 (ऐरागोनाइट, ch22); two doubled words/spaces (ch20, ch21).
- The chapter-level log is in the scratch directory `hi3/PROGRESS.md`.
- Not changed, reported: two English-canon notes (ch09 Mars/PREM arithmetic 0.06% against 0.067%; ch15 McDermitt caldera 16.4 vs 16.1 Ma), for the coordinator. The spelling ऐरेगोनाइट in chapter 23 (outside this stint's scope) should be aligned to ऐरागोनाइट.

## Reading stint (sentence-level, after hi-9; chapters 23 and 25–29)

- Chapter 23: the last section (sea level, accommodation, eustasy, exercises, weekend problem) read against the English, numbers rechecked. Year-2 book references standardised to `पुस्तक 4 (स्नातक वर्ष 2)`.
- Chapters 25–29: read sentence-level against the English, with numeric checks (ages, isochron fit, IntCal values, atmosphere table, equation-of-state values, transports, Ekman figures, AMOC dated box). No meaning drift found. Year-volume references standardised to `पुस्तक 5 (स्नातक वर्ष 3)` and `पुस्तक 4 (स्नातक वर्ष 2)`; one awkward phrase in chapter 28 (`1980 से दशकों में`) corrected to `1980 के बाद के दशकों में`.
- Term links re-applied after the final edits (`link_defined_terms.py --book 3 --lang hi --apply`: 4,028 links in 58 files; dry run afterwards: 0).
- Re-checks after the final build: `check_translation.sh bachelor-1 hi` PASSED; `engsweep.py hi` empty; `numdiff.py hi solutions`: only solutions/hi/07 (accepted, as before).

## Gates

- `tools/check_translation.sh bachelor-1 hi`: **PASSED** (hindi prose gate OK, 58 files; chemistry twin OK, 58 files).
- `tools/gates.sh bachelor-1`: **OK**.
- English sweep (`engsweep.py hi`): **empty**.
- `numdiff.py hi solutions`: one difference left, `solutions/hi/07-rock-forming-minerals.tex` (the standalone `4` in the English solution; the Hindi spells it out as चार सिलिकनों, which is correct). Accepted.
- Linker dry run: **0** links to insert.

## Term links

- **4,029 links** (4,028 before this session's edits), curated in `tools/term_config/book3_hi.py`; relinked with `link_defined_terms.py --book 3 --lang hi --apply` (58 files), dry run afterwards 0. The English edition has 4,650 links on 184 targets.
- Hindi: **177 of the 184 English targets** are linked, plus 2 Hindi-only targets (`parcel`, `window`): 179 targets in all.
- The 7 unlinked English targets are unlinked on purpose, because the Hindi text does not carry the defined sense in a way the harvester can match without a wrong-sense link (reasons in the config docstring): `diachronous`, `moc` (the Hindi line is the defining line itself), `airy` (chapter 20 does not name Airy), `sample` (the Hindi word is generic), `seismic-parameter` (defined only in chapter 9), `facies` (no Hindi occurrence of the defined form in chapter 24), `basin`.
- Curation handles the Hindi homographs (स्थायी, उभार, कोटि, विस्थापन, फ़्लक्स, पार्श्व, सहसंबंध, प्रसार, संरचना, तंत्र, संपीड़न and others) with STOP keys and phrase protects.

## Fixes made in the finishing run

- **Image credits** (`frontmatter/image-credits-book3.hi.tex`): the file was an **English copy** of the 29 items (fr, es, nl, pt and id are translated). Rewritten in Hindi: names, licences, URLs and numbers kept, the frame and descriptions in Hindi, `\allowbreak` and `\-` hints kept, and `\setlength{\emergencystretch}{2em}` added as in Book 1.
- **Overfull boxes** (see Build).
- **English unit word** in chapter 21: `\qty{480}{miles}` became `480\,मील`.
- **Chapter 20 digits**, **chapter 14 item marker**, **chapter 1 index key**: as recorded in `PROGRESS.md` of the scratch directory (earlier stints).

## Native pass

- Chapter 1 (opening, recall, first definition), chapter 12 (opening, rigid plates, Euler's theorem and proof) and chapter 24 (opening, golden spike, recall): read side by side with the English. No meaning drift and no register problem found in these passages.
- Rendered pages checked at 110 dpi: chapter 24 ICS chart (fig. 24.5), chapter 7 mineral table (tab. 7.1), chapter 10 geotherms (fig. 10.3), chapter 29 Stommel gyre figure, and a chapter 5 `\foreach` cross-section figure. No collisions, no leftover English inside the figures.
- Leftover-English sweep of the rendered text: the remaining Latin words are proper names, work titles, credits, unit and function names, acronyms and station codes.

## Score basis (95)

- Every chapter (1–29) and its solutions have now had a sentence-level read against the English. The previous open item, "native review depth", is closed: chapters 2–11 and 13–22 were read this session, and 1, 12 and 23–29 in earlier stints.
- The reads found and fixed a moderate number of defects, mostly wrong-sense or typographic, none that changes a number or a result (see the stint list above). The last build is clean on every gate.
- The remaining items below are either coordinator rulings or outside this edition's files, so they do not hold the score below the ship threshold.

## Open items (not blocking)

1. **Shared front matter is English in every edition.** `frontmatter/colophon.tex` is one file for all languages and is English (licence, repository and author lines). The coordinator ruled this shared and English by design.
2. **Credits in the Arabic edition** (`frontmatter/image-credits-book3.ar.tex`) carry the English copy that Hindi had. Not this edition's file; the Arabic edition's own job.
3. **Term-link coverage:** 4,029 links after this session's relink (against 4,650 in English; 177 of 184 targets). Each gap is a deliberate protection, and the coordinator accepted the coverage. It is lower than the French edition's (4,468).
4. **Canon notes for the coordinator (English, not changed here):** ch09 Mars/PREM "5.976e24 kg is 0.06% above 5.972e24" (the arithmetic gives 0.067%); ch15 McDermitt caldera age 16.4 Ma in the text and 16.1 Ma in exercise 8. Chapter 23 still uses the spelling ऐरेगोनाइट; ch22 now uses ऐरागोनाइट (ch07's spelling).

## Coordinator verification (claude-opus-5-5, 2026-10-28)

Accepted at 95 after the coordinator's own checks and fixes:

- The coordinator's own fixes:
  - ch20: Devanagari digits replaced by the series' ASCII forms (`\qty{20}{\celsius}` ×3, `\qty{1}{m}`, *4 मार्च 2018*), as the style card requires.
  - ch15: an English "public domain" changed to *सार्वजनिक डोमेन*.
  - ch23 and solution 22: *ऐरेगोनाइट* changed to *ऐरागोनाइट* (the ch07 spelling).
  - The term layer relinked after stint 3 had left it unwrapped.
- Gate change: `tools/check_hindi_prose.py` now skips credit spans (`CREDIT_SPAN`, `CREDIT_PAREN`, `CREDIT_PHRASES`). It replaces about forty credit-only words, such as *global*, *public* and *survey*, that had been allowed book-wide. A control file shows the gate still catches those words in prose.
- Rulings: the colophon is shared English in every edition. Link coverage of 4,029 / 4,650 (177 of 184 targets) is accepted; the unlinked targets are documented in `book3_hi.py`. Place names in credits stay Latin, as in Hindi Book 2. The ch13 "four centuries" and the sol07 *चार सिलिकनों* are faithful. The ch09 0.06 % and the ch15 16.4/16.1 Ma, reported as English slips, are correct: the unrounded PREM mass, and two different sources for caldera and field.

Checks: `numdiff` over the 29 solution files differs only at the spelt-out "4" of solution 7. The English-function-word sweep is empty. The PDF-text sweep shows only names, places, titles and credits kept in Latin. Rendered and read: the ICS chart (p. 295). Final build (TeX Live 2026, forced, `hi-11`): 454 pp | 0 errors | 0 undefined | 0 overfull | nullfont 0 | missing-char 0 | invalid-in-math 0 | zero-height 0 | `.fls` 58. `check_translation.sh bachelor-1 hi` PASSED, linker dry run 0 (re-run after the coordinator's last spelling edit).

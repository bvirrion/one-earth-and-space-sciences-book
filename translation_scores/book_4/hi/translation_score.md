# Translation score — One Earth and Space Sciences Book 4 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 4 (University Year 2, `bachelor-2`) |
| **Language** | Hindi (`hi`); आप register (-इए / -कीजिए), danda ।, Latin digits, units kept as English writes them (Ma, Myr, Gyr, kyr, yr); names transliterated, credits and titles Latin |
| **Model** | `claude-opus-5-5` (Opus 5.5, effort high), one agent per edition; one agent ran phases A–D in a single stint (with automatic context compaction); coordinator `claude-opus-5-5` |
| **Overall score** | **95 / 100** |
| **Ship threshold** | ≥ 95: **met** (basis below) |
| **Scope** | 31 chapters + 31 solution files = 62 files; the term layer (`tools/term_config/book4_hi.py`); the image credits (`frontmatter/image-credits-book4.hi.tex`); the `\bookline` and `\author` lines of the Hindi entry file |

## Build (forced, TeX Live 2026, `draft/b4-run/tools/build.sh`, build `hi-3`, after the last edit)

- latexmk exit 0, **456 pages**; errors 0; undefined 0; **overfull 0**; nullfont 0; missing characters 0 (backtick 0); invalid-in-math 0; zero-height 0.
- `.fls` lists 62 translated files = the 62 on disk.
- For comparison: English 484 pp, French 509 pp. Earlier builds `hi-1` and `hi-2` were also 456 pp; `hi-1` had one overfull box (hi12:61), since fixed.

## Gates and measures (after the last edit)

- `bash tools/check_translation.sh bachelor-2 hi`: **PASSED** (hindi prose gate OK, 62 files; chemistry twin OK, 62 files).
- `bash tools/gates.sh bachelor-2`: **OK**.
- Linker dry run (`link_defined_terms.py --book 4 --lang hi`): **0** links to insert.
- `census.py hi`: index keys identical 0, text identical 0. Four CHAPTER flags (`proxy` and `glacials` in ch26, `stages` ×2 in ch26, `metamorphism` ×2 in ch14), each read and in the right sense.
- `check_term_display_drift.py`: inflections and sibling terms only.
- Line-edge sweeps (`^\s*([,;:)?!।]|~[;:?!])`, `\S%\s*$`): clean; the one `%` line end is the `\hspace` join of two photos in ch10, as in English.

## Term links

- **Hindi 1,995 links / 191 targets; English 2,019 / 191.** Every English target is reached, and there are no Hindi-only targets.
- Curated in `tools/term_config/book4_hi.py` (531 terms; the docstring lists the homographs):
  - STOP संसूचन: it had made 8 wrong-sense links (ch28 early warning, ch31/sol31 detection limit).
  - Protects: सिल दिया (ch19, the verb *stitched*) and परिवर्तन का आरोपण अंशतः (ch27, a verb).
  - EXTRA प्रावार का विभव तापमान (the ch18 recall; bare विभव तापमान is also the ch21 atmospheric one).
  - 61 DERIVED oblique and plural forms (`lang_hi` has no tail rule).
  - स्वस्थानिक is defined twice (ch13 and ch20) and dropped from the global map, as in English.

## Conventions recorded

- **Kept from Hindi Books 1–3:** प्रावार (mantle), प्रावार-स्तंभ, प्रावार-कील, भूपर्पटी, क्षेपण (subduction), संपर्क, चट्टान, तापमान (not ताप), नमूना, समकालरेखा (Book 2 hi), टक्कर (collision; संघट्ट only for physical impacts in ch01–02), पर्णन / पर्णित / शिस्टता, पतली काट, आड़े ध्रुवक, ध्रुवण सूक्ष्मदर्शी, आरंभिक अनुपात, हॉटस्पॉट, अवधसान, प्लैजियोक्लेज़, the compass letters from the language file (`\omnameCompass…` in nodes), part letters (क)~(ख)~, *सप्ताहांत समस्या --- …*, *भाग I --- …।*, solution head *अध्याय \ref{…} --- शीर्षक*, year volumes *पुस्तक 3 (स्नातक वर्ष 1)*, the AI caption tag *(AI से बनाया गया चित्रण)*.
- **Sister series:** chemistry hi for the phase-diagram and analytical words (सॉलिडस, लिक्विडस, गलनक्रांतिक, उत्तोलक नियम, ठोस विलयन, परिशुद्धता, यथार्थता, संसूचन सीमा, मात्रांकन सीमा, द्रव्यमान स्पेक्ट्रममिति, प्रेरणिक युग्मित प्लाज़्मा).
- **Decided in this edition:**
  - range = परास (19 sites of परिसर changed);
  - magmatism = मैग्मावाद;
  - spellings एंडेसाइट, एम्फ़ीबोलाइट, ग्रैन्यूलाइट, इओसीन, ऐल्पाइन, फ़ैनेरोज़ोइक;
  - a sentence that ends on inline math or a macro takes the danda ।;
  - spectrometry स्पेक्ट्रममिति;
  - metamorphic grade कायांतरण श्रेणी (कायांतरी श्रेणी is the ch11 *metamorphic series*);
  - return period पुनरावृत्ति काल;
  - underplating अधःस्तरण;
  - relative rise of sea level समुद्र-तल का सापेक्षिक उठाव (not उत्थान, which is *uplift*, and not सापेक्ष, which reads *relative to*);
  - *dark/darker* अधिक गहरे रंग का (not गहरा alone, which reads *deep*);
  - probability प्रायिकता (likelihood keeps संभाविता);
  - bias पूर्वाग्रह (chemistry hi's अभिनति is this series' *syncline*);
  - colour index (rock) रंग-सूचकांक (वर्ण-सूचकांक is the astronomical one, b1 ch02);
  - fabric विन्यास (b1 ch17).
- **Disagreements reported, not made:** physics and chemistry hi write ताप for temperature; this series' Books 1–3 write तापमान, and Book 4 follows the series. Book 3 hi has समतापरेखा for *isochron*; Book 4 writes समकालरेखा (Book 2 hi).

## Register counts (exercise stems, imperative forms)

| Edition | -इए / -कीजिए | -ओ | -एँ / -ें |
|---|---:|---:|---:|
| this edition, course files | 1,362 | 0 | 0 |
| this edition, solution files | 8 | 0 | 0 |
| this series Book 3 hi | 1,107 | 0 | 28 |
| physics `bachelor-2/hi` | 835 | 0 | 1 |
| biology `bachelor-2/hi` | 950 | 1 | 1 |
| chemistry `bachelor-2/hi` | 1,112 | 0 | 0 |

The आप imperative is the norm everywhere, and this edition follows it.

## `!draw` ranges

- 02:373–377 (`\foreach` stage labels)
- 03:101–103 (`\foreach` legend words; `east:` written `right:`, the same TikZ position, accepted by the coordinator)
- 04:651 (yticklabels of the δ13C chart)
- 11:63, 11:68 (`\foreach` isograd and zone names)
- 15:416–422 (supercontinent chart: six explicit nodes replace the figdata name column)
- 18:71 (`\foreach` era-prefix labels)
- 19:465, 19:468–470 (extinction labels: explicit nodes)
- 23:100, 23:206–208 (`\foreach` panel titles)
- 24:156 (`\foreach` ice-volume panel titles)

No `--force-classes` was used: the units stay as English writes them.

## Reading (phase C)

- Every chapter and every solution file (62 files) was read sentence by sentence against the English, with the arithmetic of every exercise and weekend problem rechecked along the printed path. The chapter-by-chapter log, with the values checked, is in `draft/b4-run/hi4/PROGRESS.md`.
- 28 logged fixes, several of them book-wide. Examples: return period and crossed polars aligned with their owners; *range* परिसर → परास (19 sites); *metamorphic grade* written as the series term; underplating aligned with ch12; the relative-sea-level and *darker* senses; a garbled doubling-time clause (sol22); *blocks* dropped and restored (ch06); word-order fixes (ch12, ch31). None changes a number or a result.
- Earlier in phase B: 18 ranges that were one line short (`id_apply` does not check a range's line count) were found and fixed; 8 line-broken `\index` keys were joined; part letters that had drifted to Latin (a)–(e) in ch16–18 were restored to (क)–(ङ).

## Rendered pages

- Every figure page of every chapter was rendered and read during phase A/B probes (list per chapter in `PROGRESS.md`). Label fixes made there: ch02 Fe--FeS node, ch03 legend, ch18 EBM node, ch21 process-diagram arrow, ch22 front section, ch26 CENOGRID node.
- From the final `hi-3` PDF, at 110–120 dpi: table 5.1 with its caption (*तालिका 5.1:*), the supercontinent chart (p. 184), the extinction chart with its ICS period bar (p. 229), the ch15 ocean-width chart (p. 183), the ch18 opening (p. 210) and the cap-carbonate photo page (p. 219). Every label sits on its own point; no English is left inside the figures.
- Book 4 has no `\cref{tab:…}` in any language (English included), so there was none to check.
- Page 218 is half empty before the full-width cap-carbonate photo on p. 219 (an `omfigure` that did not fit). This is layout, not a defect of the edition.

## Score basis (95)

- Every chapter has had a sentence-level read, the build is clean on every count, every gate passes, and every English target is reached.
- The reading found wrong-sense and consistency defects, mostly in terminology. They are all fixed, and none touched a number.
- Kept at 95 rather than 96: link coverage (1,995 against 2,019) is slightly below English; the solution files (8 imperative forms) were not given a separate native-register pass beyond the sentence-level read; several homograph decisions (परास, गहरे रंग, सापेक्षिक) were made in this edition and are not yet confirmed by a second reader.

## Canon reports (English, not edited)

- **ch18:647–648 vs sol18:54–55 (class c).** The course says the Marinoan lasted "at least 5 Myr" (ledger `hoffman17:cryochrons`). The same paragraph's dated brackets (`hoffman17:ages`) give a minimum of 639.0 − 636.0 = 3.0 Myr, and sol18 7(c) prints "between about 3 and 15 Myr".
- **ch18:542, 595–596 vs sol18:46, 73, 119 (sibling inconsistency).** The course prints S_f/S_0 = 0.932 (1268.9/1361); the solutions print 0.933 three times (from the printed ε 0.616: 1269.3/1361 = 0.9326).
- **sol28:105–107 (class b, stale after the coordinator's 0.0673 → 0.0672 fix).** 0.09 × 0.0672 + 0.009 × 0.308 + 6.84e-4 × 0.597 = 9.228e-3, so 9.23e-3, but the solution prints 9.24e-3.
- **ch31:665 (layout, every edition).** The `\label` after `\section*{Weekend problem}` defeats the style's fresh-page lookahead (`\om@sec@peek`), so the heading is stranded at the foot of the exercises page.
- Already ruled "unrounded value" by the coordinator, kept: sol03:28 / ch03:578 0.72, sol02:60 5.5, sol01:150 7.90e16.

## Tool reports and allow-list entries

- `tools/check_hindi_prose.py`, the Book 4 hi `CREDIT_PHRASES` block (appended, commented). It holds the credit names of ch01–06, 24, 25, 29, 30 and 31, among them "Siems (2002)", "Pugmire (2014)", "Advanced Chemistry Basins Project (2004)", "Moring (2008)", "Loutre (1991)", "Raymo 2005".
- `ALLOWED_WORDS` additions (commented, before the `__main__` guard): `p--t--t`, `easyro`/`EasyRo` (model name), `iii` (roman sub-item label), `kcps` (count-rate unit).
- Style (not this edition's to fix): `\om@sec@peek` does not look past a `\label`; see ch31:665 above.

## Departures from Hindi Books 1–3

- The AI caption tag is *(AI से बनाया गया चित्रण)*; Book 3 hi wrote *(AI से बनाया गया चित्र)*.
- समकालरेखा for *isochron* (Book 2 hi), not Book 3 hi's समतापरेखा (reported above).
- Otherwise none: the conventions above are Books 1–3's.

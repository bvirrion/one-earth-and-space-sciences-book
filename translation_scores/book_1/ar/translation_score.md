# Translation score — Earth and Space Sciences Book 1 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 1 (Primary and Middle School, Grades 1–9) |
| **Language** | Arabic (`ar`), Modern Standard Arabic, right to left (LuaLaTeX, babel bidi) |
| **Quality bar** | **native school prose at every level**: an Arabic children's science book read aloud in grades 1–5, an Arabic preparatory-school science and geography textbook in grades 6–9, in the established Arabic vocabulary of school geography, geology and meteorology. English is the source of truth for content, structure, labels, numbers, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); `arabic_style_card.md`; the shipped Arabic editions of One Biology Book 1 and One Chemistry Books 1–2 (register of the school years, solution and problem headers, `\foreignlanguage{arabic}` / `\babelsublr` conventions in figures); the Arabic physics editions for shared physical vocabulary |
| **Overall score** | **95 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-25 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 32 chapters + 32 solution twins = **64 files**, every one written through `tools/id_apply.py` line-range patches; `frontmatter/preface.ar.tex` and `frontmatter/image-credits.ar.tex`; the aside-box block of `styles/lang/ar.tex` (wording settled, kept); the `\bookline` / `\author` lines of the entry file (already Arabic, kept); a curated `tools/term_config/book1_ar.py`; the defined-term link layer; Arabic index keys; the right-to-left figure fixes; and this score |

## Verdict in one line

An Arabic Book 1 that reads as one Arabic school course in the Earth and space
sciences from the first year to the ninth — short sentences addressed to the
reader in the singular for the youngest, the explanatory textbook register
(نحن / impersonal passive) in the preparatory years, singular imperative
exercise stems throughout (*استعمل، رتّب، سمِّ، انظر، صِل، أعطِ، احسب*),
standard Arabic technical terms, ASCII digits with the decimal point as the
series' siunitx setting requires — with every structural and prose gate green
over the nine years and a forced build of **0 errors / 0 undefined /
0 overfull**, 303 pages.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror over all 64 files against their 64 twins: **370 `exercise`**, **20 `problem`**, **390 `\begin{solution}`**, **234 `omfigure`**, **161 `tikzpicture`**, **73 `axis`**, **120 raster includes**, **455 `\emph`**, **237 `\index`**, **816 `\label`** (set diff 0 / 0), **468 `\item`**, **588 `% ledger:`**, and per environment **140 `definition`, 4 `proposition`, 42 `method`, 60 `example`, 24 `remark`, 30 `recall`, 7 `inthefield`, 9 `inthelab`, 10 `history`, 2 `dated`, 7 `safety`** — all equal to English. `\qty` 835 against 834: grade-9/05 line 277 writes `\qty{1}{cm}` where English has `1~cm` (a bare digit + Latin unit inside Arabic prose reorders). `\node` 746 against 677: every figdata label layer became explicit Arabic nodes. `drawcensus.py ar` reports only those label layers (`\addplot` g3/02 8→6, g6/05 11→10, g7/05 22→15, g8/01 9→8; every dropped plot is a `point meta=explicit symbolic` label plot) and en dashes inside label text (`--` g4/02 43→42, g7/01 64→62: the "1976--2025" legend entries and "Peru--Chile"; g8/04 59→58 "Peru--Chile Trench"; g9/01 8→23: the decade `xticklabels` "1880--1889 …" replacing English "1880s") — no path lost. All 32 patches re-applied in a scratch copy reproduce the 64 files byte for byte |
| Terminology | **96** | One Arabic glossary across nine years: الطقس، محطة الأرصاد الجوية، مقياس المطر، دوارة الرياح؛ المخطط، الخريطة، مفتاح الخريطة، مقياس الرسم، وردة الرياح؛ الحصاة، الرمل، الصخر، الوحل؛ مجسم الكرة الأرضية، خط الاستواء، نصف الكرة؛ الارتفاع، مستوى سطح البحر، التضاريس؛ التجوية، التعرية، الترسيب، المنبع والمصب والرافد، المنعطف النهري، الفيضان، السهل الفيضي؛ الكوكب الصخري / العملاق، دائرة العرض، خط الزوال الأصلي، المنطقة الزمنية، خط التاريخ الدولي؛ المعدن (and الفلزات for metals, kept apart), الصخر الناري / الرسوبي / المتحول، دورة الصخور، سلم موس؛ القشرة، الوشاح، اللب؛ التسرب، المسامية، النفاذية، منسوب المياه الجوفية، الخزان الجوفي؛ الصفيحة التكتونية، الحد المتباعد / المتقارب / التحويلي، الظهرة المحيطية، الخندق، بانجيا؛ حجرة الصهارة، المنفذ، الفوهة، التدفق الفتاتي البركاني، البقعة الساخنة؛ البؤرة، المركز السطحي، القدر، الشدة، مقياس الزلازل، التسونامي؛ الأحفورة، القالب / المصبوبة؛ مبدأ التراكب / التقاطع / الاحتواء، عدم التوافق، الحقبة، السلم الزمني الجيولوجي؛ التروبوسفير … الثرموسفير، طبقة الأوزون، الرياح التجارية، الرياح الغربية، الكتلة الهوائية، الجبهة الباردة / الدافئة، المنخفض / المرتفع الجوي، خط تساوي الضغط؛ الرف القاري، السهل السحيق، الدوامة المحيطية، الجليد البحري؛ النهر الجليدي، الركام الجليدي، الوادي على شكل حرف U، الغطاء الجليدي، الرف الجليدي، التربة الصقيعية؛ شذوذ درجة الحرارة، الاحترار العالمي؛ الخطر الطبيعي، الهشاشة، المخاطر، الوقاية، خريطة الأخطار؛ مكمن الخام، معامل التركيز، العرق المعدني، الرواسب اللُّحَقية، الحصويات، الاحتياطي؛ الرفع، الكثيب، البرخان، وجه الانزلاق، الجرف، الحزّ، مصطبة نحت الأمواج، الانجراف الساحلي، اللسان الرملي، الكارست، البالوعة، الهوابط والصواعد الكلسية؛ الإسقاط الخرائطي، إسقاط مركاتور، المقياس العددي / الخطي، الخريطة الطبوغرافية، خط الكنتور، الفاصل الكنتوري، الاستشعار عن بعد. Two spellings normalized book-wide in the last pass: إفريقيا (not أفريقيا) and ملك عام (not ملكية عامة). All 237 `\index{}` keys in Arabic, one per English key (237 distinct, 0 collisions) |
| Register / tone | **96** | Grades 1–5 address the reader in the masculine singular with short sentences; grades 6–9 use the course register (نحن, impersonal passive) and singular imperatives in exercise stems: commonest openers *استعمل* ×25, *صواب أم خطأ* ×18, *رتّب* ×12, *سمِّ* ×12, *انظر* ×11, *صِل* ×8, *أعطِ* ×5; **0** plural address (أنتم / انظروا / لاحظوا) anywhere. Box names: *ما تعرفه من قبل، في الميدان، في المختبر، لمحة تاريخية، أرقام عام 2025، السلامة*. Observation-only wording everywhere (cliffs, quarries and caves described, never visited; the Sun never looked at) |
| Typography | **95** | Arabic comma, semicolon and question mark (، ؛ ؟); guillemets «…»; ASCII digits and the decimal point; no tatweel; no non-ASCII inside `\qty{}`, `\unit{}`, `\num{}`; `\text{}` census over course and solutions: the only Latin is `hPa`, as in English. Line-edge sweeps: **0** prose lines opening on punctuation, **0** dangling hyphens (the only hits are TikZ `..` control-point continuations, identical in English) |
| Fidelity / accuracy | **95** | Every paragraph, example, exercise and solution translated against its twin with the numbers recomputed while translating. Scripted re-read: a per-block number census of every `exercise`, `problem`, `solution`, `example`, `definition` and `method` against its English twin (53 blocks differ, every one read: numbers spelled out in words, decade ranges for "1880s", the 1–12 month numbering of the grade-5 climate tables, the town label's explicit coordinate, "800\,000" grouping) and a doubled-word scan, which found and fixed three awkward repetitions (g9/02 "خريطة فيضان فيضان", g9/02 caption "مقاييس الزلازل الزلازل", g7/01 solution "قاع المحيط المحيط"). The coordinator's canon fixes are mirrored (g7/01 solution 11, the g9/02 caption initials, Viñas) |
| Figures and right to left | **94** | Drawing code byte-identical except the documented `!draw` ranges below. Node labels mixing Arabic with Latin or digits are wrapped in `\foreignlanguage{arabic}{…}` line by line; multi-letter Latin inside a node (GPS, V) in `\babelsublr{}`; axis labels as `\foreignlanguage{arabic}{… \babelsublr{(km)}}`; parentheses removed from mixed node lines or anchored with `\textdir TRT` where tested; item numbers followed by bare digits (`\textbf{12.} \babelsublr{35} …`) fixed at the four sites where the digits reordered. Every fix was verified on test documents and by glyph x-positions in the PDF. The image credits had Latin credit runs scrambling against Arabic punctuation; every Latin run is now in `\babelsublr{}` with the Arabic punctuation outside (checked on the rendered pages). Known residue: the `\omve{N}` label prints "N×" mirrored (style-file issue, reported with a patch) |
| Links | **96** | **5,951 `\omterm` links on 138 targets** against English's **6,103 on 137**: every English target is linked (**0 missing**), plus the geological time scale (1 link, the g7/05 caption, as in es / pt / nl / hi). Date line: 5 links (EXTRA "خط تاريخ"). Frequency and chapter-set censuses run after the last body edit; dry run **links to insert: 0** |

## Gates

`bash tools/check_translation.sh grade-N ar` for N = 1 … 9: **9 / 9 PASSED**,
run after the last body edit.

Build (forced, through the run's wrapper): `grep -ac '^!'` **0**,
`grep -aci undefined` **0**, `grep -ac Overfull` **0**, nullfont **6633**
(= the English baseline), non-backtick missing characters **0**,
invalid-in-math **0**; **303 pages** (English 324); the `.fls` lists **64**
Arabic chapter and solution files = **64** on disk.

## Conventions recorded

* **Compass letters**: ش ق ج غ (`\omnameCompass*`), in prose, figures, ticks
  and coordinates (`$41^\circ$ ش`); grade-2/02's rose legend node turned
  `align=right` (a `!draw` change) so the Arabic lines align.
* **Pressure centres**: ع (عالٍ / مرتفع) and م (منخفض) on the weather maps.
* **Names**: personal names transliterated in the bodies (the Latin original
  kept beside them in the image credits); agency names glossed in Arabic in
  the bodies (هيئة المسح الجيولوجي الأمريكية, ناسا); datasets keep their names.
* **Port Hale** (g7/03 problem) → بورت~هيل; the figdata town label replaced
  by an explicit node at the `.dat` coordinate (264, −102).
* **Months** in the grade-5 climate tables: numbered 1–12 with a one-line key,
  since Arabic month initials are not usable.

## `!draw` ranges (course files; no solution file needed one)

g1/01 92-93, 97-98, 122-127, 136-138, 187-189, 204-207 · g1/02 228 ·
g2/02 168-169 · g3/01 105-109 · g3/02 63-65, 77-79 · g4/01 378-379 ·
g4/02 217, 239 · g4/03 87-88, 93-95 · g5/01 57-59 · g5/02 85-86, 157 ·
g5/03 54-59, 168-169 · g6/01 76, 88-89, 149, 207-208, 220, 329-330, 366-367 ·
g6/02 244-246, 251-256, 325-326 · g6/03 323-324, 328 · g6/05 224, 271-273 ·
g7/01 343-344 · g7/02 476 · g7/03 121-122, 133, 135, 137-138, 183, 191-192,
194-196, 200, 204, 206, 208, 265, 273, 342-343, 434, 439-440, 442-443,
626-629, 631, 632 · g7/04 93-95, 97, 163, 184-185, 238, 247, 256, 265, 322,
447, 454-458 · g7/05 94-95, 125, 127, 145-147, 162, 169, 171-172, 272, 281,
288, 298, 336, 348-349, 356-363, 421-423, 431, 436-444, 510-512, 515-520 ·
g8/01 93, 126, 131-133, 147-148, 154-155, 157-158, 201, 209-211, 215-217, 219 ·
g8/02 61, 74-75, 142, 148-149, 156-158, 160-161, 168-170, 172-173, 256-261,
263, 268, 276, 391-392, 396-397, 400-404, 531, 538-539 · g8/03 73-74, 79, 81,
83, 85, 87, 89, 133-134, 148, 150, 153-156, 181-182, 186, 189, 191, 193,
195-197, 292, 294, 301, 350, 356-357, 359-360, 533, 539-540 · g8/04 69-70, 72,
74-75, 77-78, 80-81, 141, 147, 149-152, 161, 167, 169-170, 220-221, 225-226,
230-231, 233-234, 290-291, 300-301, 358-359, 368-369, 504-505, 512 ·
g8/05 97, 112-118, 161, 163, 172, 175-177, 265-266, 330, 334, 337, 426-428,
607-608 · g9/01 51-53, 56, 59, 64, 67-68, 115, 121, 214, 216, 244, 250, 252,
305, 340, 343, 345 · g9/02 85-88, 91-96, 170, 176, 180, 187, 190, 194, 197,
201, 254-255, 271, 329, 338, 347, 357, 560-561, 576 · g9/03 77-78, 139, 141,
144, 146, 148, 244-247, 320-325, 391, 398-401, 450-458 · g9/04 85, 96, 108,
111-113, 174-180, 194-198, 277-280, 292, 304-305, 362, 366, 378, 382, 384,
386, 389, 487-488, 490, 492, 494, 496-497, 734 · g9/05 72, 81, 179-181, 188,
192-193, 268. Almost all are `\foreach` label lists, label layers replaced by
explicit nodes, `xticklabels` lists, and node wrappers for right-to-left text.

## Link layer

`tools/term_config/book1_ar.py` was curated from this edition's own harvest
(413 terms) and both censuses, never translated from `book1_en.py`. Arabic
morphology dominates: the article and one-letter prepositions are a HEAD, so
nothing reaches a broken plural, a dual or a tanween accusative; about 120
EXTRA entries declare the forms the edition really uses (زلازل، براكين، صخور،
أحافير، جبال، قارات، القطبين، زلزالًا، صخرًا، واديًا …). Homographs and
HEAD artefacts handled, each with evidence in the config:

* **ك + تلة = كتلة** ("mass"), **ال + سهل = السهل** ("easy"), **ب + قدر =
  بقدر**: the HEAD manufactures ordinary words out of short terms;
* **ارتفاع** — altitude, but also a rise (of the sea, of a temperature), an
  uplift, a star's elevation, a tower's height: those senses masked; the
  target stays above English (183 vs 68) because Arabic says ارتفاع where
  English says "height" or "at 400 m";
* **مخطط** — the g2 plan, but a chart/graph everywhere else (STOP);
* **مقياس الرسم** — "to scale" (ليس بمقياس رسم، مرسومة بمقياس الرسم) masked;
* **العرض / الطول** — width and length masked around the latitude/longitude
  uses; **قدره** "amounting to" before a `\qty`; **حقبة الحياة …** (named
  eras); **تسرب** a pollutant leak; **البرد** cold / the verb; **مدار** an
  orbit; **بشدة**; **صفائح رقيقة** (mica); **مفتاح** an identification key;
  **لب الجليد** an ice core; **دوامات الهواء / السحب**; **القارة القطبية**
  (Antarctica, one word in English); **البركان الطبقي**; credits (خطوط
  السواحل، تضاريس ETOPO1); **تلال فاردن** (the invented region);
* the bold *الجزء الأول/الثاني/الثالث* headings and `\paragraph` run-in
  headings stay unlinked, as in English.

## English-canon defects reported (not fixed in the canon)

1. `parts/grade-9/solutions/02-natural-risks.tex` line 107: "B $83 \div 2
   \approx 41~\%$" — 41.5 rounds to 42 (or print 41.5).
2. (minor) `parts/grade-7/solutions/02-volcanoes.tex` pb 8, lines 119–120:
   rounds 8 ÷ 130 to 0.062 before multiplying by 60 (the series' "never round
   twice" rule); the answer (3.7, about 4 minutes) is unchanged.

## Coordinator addendum (2026-10-25)

Re-verified by the coordinator:
- a forced build: 303 pp, 0 errors / 0 undefined / 0 overfull, nullfont 6,633, `.fls` 64 = 64;
- `check_translation.sh` 9/9 PASSED; linker dry run 0;
- no English target missing;
- the draw census differs only in label-table rewrites and en dashes inside label text, each checked.

Changes the coordinator made:
- **`\omve`.** The proposed `\babelsublr{$\times N$}` fixed prose but not TikZ nodes: a probe still showed "260×" in a node, and the first final build was unchanged. The style now uses `\mbox{\textdir TLT$\times N$}` under the Arabic conditional, which gives "×260" in both positions (glyph x-positions checked).
- **Canon.** g9/02 solution 5 now prints "= 41.5 %" (this edition mirrored). The g7/02 problem-8 intermediate rounding was left as is: the answer does not change, and problem 7 has the same pattern.

The score is unchanged.

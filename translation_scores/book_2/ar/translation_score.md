# Translation score — Earth and Space Sciences Book 2 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 2 (High School, Grades 10–12) |
| **Language** | Arabic (`ar`), Modern Standard Arabic, right to left (LuaLaTeX, babel bidi) |
| **Quality bar** | **native academic prose**: an Arabic secondary-school textbook of the Earth sciences (geology, meteorology, oceanography, climate) in the established Arabic vocabulary of those fields, at the register of the upper secondary years. English is the source of truth for content, structure, labels, numbers, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); `arabic_style_card.md`; the shipped Arabic Book 1 of this series (glossary, compass letters, likelihood and confidence words, figure conventions); the Arabic chemistry and physics editions for shared physical vocabulary |
| **Overall score** | **95 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-26 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 28 chapters + 28 solution twins = **56 files**, each written through `tools/id_apply.py` line-range patches (course) or the solution generator (solutions); `frontmatter/image-credits-book2.ar.tex`; the `\bookline` / `\author` lines of the entry file (already Arabic and parallel to Book 1, kept); a curated `tools/term_config/book2_ar.py`; the defined-term link layer; Arabic index keys; the right-to-left figure fixes; and this score |

## Verdict in one line

An Arabic Book 2 that reads as one Arabic upper-secondary course in the Earth
sciences: the explanatory textbook register (نحن / impersonal passive) in the
course, singular imperative exercise stems (*احسب* ×95, *عرّف* ×24,
*فسّر* ×18, *استنتج* ×14, *تحقق* ×14, plus the question words *ما، لماذا،
كم، أي، بكم*), standard Arabic technical terms, ASCII digits with the decimal
point as the series' siunitx setting requires, Book 1's glossary carried on
without a break — with every structural and prose gate green over the three
years and a forced build of **0 errors / 0 undefined / 0 overfull**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror over all 56 files against their 56 twins: **420 `exercise`**, **28 `problem`**, **448 `\begin{solution}`**, **205 `omfigure`**, **141 `tikzpicture`**, **104 `axis`**, **100 raster includes**, **24 `tabular`**, **371 `\emph`**, **219 `\index`** (219 distinct keys, 0 collisions), **764 `\label`** (set diff 0 / 0), **752 `\item`**, **561 `% ledger:`**, **141 `\ce`**, **132 `\cref`**, **658 `\node`**, and per environment **141 `definition`, 58 `proposition`, 34 `method`, 43 `example`, 14 `remark`, 28 `recall`, 1 `inthefield`, 1 `inthelab`, 12 `history`, 5 `dated`, 2 `safety`** — all equal to English. `\qty` 3,688 against 3,685: g10/06 writes positions as `\qty{13.5}{\degree} ج` (compass letter outside the unit, where English has `\qty{13.5}{\degree S}`), and its caption's "40.5\textdegree N, 30.5\textdegree W" as two `\qty{…}{\degree}` with ش / غ; g10/04 writes the "125-metre rule" as `\qty{125}{m}`. `drawcensus.py ar` differs only by `--`, `arc` and `circle` **inside English node text** ("core--mantle boundary", "volcanic arc", "back-arc", "small circle", "aerosol--cloud") — no path lost |
| Terminology | **96** | One Arabic glossary across the three years, continuous with Book 1: الجيوديسيا، التثليث، الإهليلجي المرجعي؛ درجة حرارة التوازن، النطاق الصالح للحياة؛ الإشماس، الألبيدو، ميزانية الطاقة، الحرارة الكامنة / المحسوسة؛ التشبع، الرطوبة النسبية، نقطة الندى، المعدل الكظمي الجاف / المشبع، مستوى التكاثف، هواء مستقر / غير مستقر؛ العاصفة الرعدية، الإعصار القمعي، الإعصار المداري، جدار العين، سلم سافير--سيمبسون، العرام العاصفي؛ الطبقة المختلطة، طبقة التدرج الحراري / الملحي / الكثافي، التطبق، الانبثاق؛ الصخر الأم، الحلمهة، المعدن الطيني، اللاتريت؛ حوض التصريف، خط تقسيم المياه، الهيدروغراف، التدفق القاعدي، فترة العودة؛ المخزون والدفق، زمن المكوث، المياه الجوفية الأحفورية؛ توسع قاع المحيط، المغنطة المتبقية، الانقلاب المغناطيسي، الشذوذ المغناطيسي؛ الموجة P / S، زمن الانتقال، الموجة المنكسرة الحرجة، الموهو، منطقة الظل؛ الغلاف الصخري، الغلاف اللدن، المنحنى الحراري الأرضي، التوازن الأيزوستاتي؛ الاندساس، اللوح المندس، شد اللوح المندس، دفع الظهرة، الشيست الأزرق، الإكلوجيت؛ الانفصام، المكسر، السيليكات؛ الصخر البركاني / الجوفي، النسيج، البلورة الظاهرة، البورفيري، المافي / المتوسط / الفلسي، القاطع، العتبة، البلوتون؛ الكيروجين، الصخر المصدر / الخازن / الحاجز، المصيدة، نافذة النفط؛ الكراتون، الجذر؛ الطية المحدبة / المقعرة، الصدع المعكوس / الزاحف، الغطاء التكتوني، الدرز، الأوفيوليت؛ التحول، المعدن الدليلي، خط تساوي الدرجة، هالة التحول؛ القوس البركاني، الباثوليث؛ معدل التجريد، الحمولة الرسوبية، التصخّر، الارتداد الأيزوستاتي؛ التدفق الحراري، التبرد القرني؛ خط تساوي العمر؛ الستروماتوليت، حدث الأكسدة العظيم، تكوين الحديد الشريطي؛ المؤشر البديل، العينة الجليدية، الدورة الجليدية، الذروة الجليدية الأخيرة؛ التأثير الإشعاعي، التغذية الراجعة المناخية، حساسية المناخ عند التوازن، الإسناد، سيناريو الانبعاثات، الإسقاط المناخي، الهباء الجوي. *Flux* is الدفق, never التدفق, so that it does not collide with التدفق القاعدي (baseflow), التدفق الحراري (heat flow) and the verb يتدفق. Spellings normalized book-wide in the last pass, to Book 1's: إفريقيا (not أفريقيا), ملك عام (not ملكية عامة), \emph{بثقة عالية} (not بدرجة ثقة) |
| Register / tone | **96** | The course uses نحن and the impersonal passive; exercise stems are masculine-singular imperatives; **0** plural address (أنتم / انظروا / لاحظوا / احسبوا) anywhere. Box names as Book 1 (*ما تعرفه من قبل، في الميدان، في المختبر، لمحة تاريخية، أرقام عام N، السلامة*). Observation only. The two climate chapters keep to physical science, with the assessment's calibrated likelihood words (مؤكد تقريبًا، مرجح للغاية، مرجح جدًا، مرجح، متساوي الاحتمال تقريبًا، غير مرجح، غير مرجح جدًا) and no policy wording |
| Typography | **95** | Arabic comma, semicolon and question mark (، ؛ ؟); guillemets «…»; ASCII digits and the decimal point; **0** tatweel (الـ\num / بـ\qty rephrased); no non-ASCII inside `\qty{}`, `\unit{}`, `\num{}`; `\text{}` census: **0** Latin words of three letters or more. Line-edge sweeps after the last body edit: **0** prose lines opening on punctuation (the only hits are TikZ `.. controls` continuations, identical in English) and **0** line-final one-letter words (three line-final و before a display equation rephrased as ومن ثم / ومنه in the last pass) |
| Fidelity / accuracy | **95** | Every paragraph, example, exercise and solution translated against its twin with the numbers recomputed while translating; the coordinator's canon fixes are mirrored (Book 2 wave-1 list: knots/feet/acre-foot units, million km² quantities, joined index keys, g12/04 solution 33 → 35 km, g12/05 ln-10 product 67, g12/06 56.7 TW, the g12/05 ledger value 55.8, g12/02 `\num{35}`; and g11 solution 8.16, the 950-day sill). Two intervals of g12/10 written as `$[x \text{, } y]$` instead of "x to y" (math is laid out left to right, so "y إلى x" would read backwards) |
| Figures and right to left | **93** | Drawing code byte-identical except the documented `!draw` ranges below. Node labels mixing Arabic with Latin or digits are wrapped in `\foreignlanguage{arabic}{…}` line by line; Latin inside nodes in `\babelsublr{}`; axis labels as `\foreignlanguage{arabic}{… \babelsublr{(\unit{km})}}`. Every figure page was rendered at 130 dpi in a per-chapter probe and the doubtful ones checked by glyph x-positions (`pdftotext -bbox`), because the eye misreads mirrored text. New right-to-left traps found and fixed (see "Right-to-left findings"). Known residue: two-column legends lay out left to right (swatch left of its own text, as in Book 1); photo strips and panel grids are captioned "من اليمين إلى اليسار" where babel reverses their order |
| Links | **96** | **2,137 `\omterm` links on 137 targets** against English's **2,208 on 136**: every English target is linked (**0 missing**), plus the Saffir–Simpson scale (`def:g10:storms-and-cyclones:scale`, 2 links in g10/05), which English never reaches. Frequency and chapter-set censuses run after the last body edit; only flag left is *cleavage* linked once in g11/08 (بالمكسر المحاري, the conchoidal fracture of obsidian — the right sense). Dry run **links to insert: 0** |

## Gates

`bash tools/check_translation.sh grade-N ar` for N = 10, 11, 12: **3 / 3
PASSED** (Arabic prose gate OK over 18, 18 and 20 files; chemistry twin gate
OK), run after the last body edit.

Build (forced, through the run's wrapper, after the last body edit): `grep -ac '^!'` **0**, `grep -aci undefined` **0**,
`grep -ac Overfull` **0**, nullfont **3,291** (English baseline 3,291),
non-backtick missing characters **0**, invalid-in-math **0**;
**334 pages** (English 362); the `.fls` lists **56** Arabic
chapter and solution files = **56** on disk.

## Conventions recorded

* **Compass letters** as Book 1: ش ق ج غ, in prose, ticks and coordinates
  (`\qty{13.5}{\degree}~ج`, map ticks `10° ج`).
* **Book references**: (الكتاب 1، الصف 7); chapter references through
  `\cref` as English.
* **Names**: personal names transliterated in the bodies (موتونوري ماتوياما،
  واداتي، بينيوف، موهوروفيتشيتش، غوتنبرغ، أولدهام، جيفونسكي …), the Latin
  original kept beside them only in the image credits; ship, journal and paper
  names transliterated in Arabic in the bodies (the prose gate rejects Latin
  words even inside `\babelsublr`): «غلومار تشالنجر»، «جويدس ريزولوشن»،
  «نيتشر»; agency names glossed in Arabic (هيئة المسح الجيولوجي الأمريكية،
  الإدارة الوطنية للمحيطات والغلاف الجوي، الهيئة الحكومية الدولية المعنية
  بتغير المناخ); dataset and model acronyms (IBTrACS, PREM, NNR-MORVEL56,
  SSP1-1.9 …, PETM, EECO, KTB) kept in Latin inside `\babelsublr` or a
  `\textdir TLT` box.
* **Image credits** (`frontmatter/image-credits-book2.ar.tex`): as Book 1 —
  names transliterated with the original in `\babelsublr{}`, institutions,
  datasets and licences verbatim in `\babelsublr`, literal "الفصل~N"
  numbering as in English Book 2.
* **Likelihood and confidence**: Book 1's words (above); confidence
  `\emph{بثقة عالية}` / `\emph{بثقة متوسطة}`.
* **Intervals** in math: `$[x \text{, } y]$` (g12/10 course 366, 524 and
  solution 3), a departure from English's "x to y".
* **Grids of map cells** (g10/08 exercise 15): the digit grid is wrapped in
  `\babelsublr{\begin{tabular}…}` so it stays left to right; the word grid of
  solution 15 cannot be (bidi re-reverses Arabic cells), so its cells are
  written in reversed column order in the source and the plain right-to-left
  tabular shows the map the right way round (checked on the render).
* **Photo strips and grids** that babel lays out right to left: captions say
  "من اليمين إلى اليسار" / "في اليمين"; paired photographs swapped in the
  caption, not in the source.

## Right-to-left findings (generic; for `translation_instruction.md`)

1. Inside `\foreignlanguage{arabic}{…}`, a pgfplots axis label or title, a
   `ticklabel` and a legend entry, a **leading multi-character LTR run** (a
   number or a Latin word) is glyph-reversed: 15 → 51, PETM → MTEP,
   1996 → 6991, 100 → 001. A plain node starting with digits, a line starting
   with Arabic, a leading `\babelsublr` and a single digit are fine. Fix:
   `\mbox{\textdir TLT …}`. Fixed at g10/03 320, 337; g10/08 318–319;
   g10/09 185; g11/08 442; g12/09 270–271, 580–581. Probably present in
   Book 1 `ar` too (not checked).
2. A **tabular cell starting with a Latin word** is laid out left to right
   ("PETM، 56 مليون سنة" in the wrong order): `\mbox{\textdir TLT PETM}، …`
   (g12/09 616–621). A number range inside one such box stays "53--49": one
   box per number.
3. Arabic text **ending in ")"** inside a node, axis label or legend shows the
   closing parenthesis unmirrored, even under `\foreignlanguage`; "(III)"
   inside a node renders ")III(". Rephrase without the edge parenthesis.
4. In a **plain** node line, Arabic ending in a neutral (، : ؛ .) puts the
   punctuation on the wrong side, and "(أ) text" breaks: wrap each `\\`-line
   in `\foreignlanguage{arabic}{…}`, panel letters as "أ. …".
5. **Number tuples** in prose, "(0.90, 0.71806)", are reversed by bidi: wrap
   in `\babelsublr{(0.90,~0.71806)}`. Thin-space grouped numbers
   (57\,437) reorder: write `\num{57437}`.
6. A two-line axis label whose second line is only "(°C)" mirrors its
   parentheses: keep the unit on the first line.

## `!draw` ranges (course files; no solution file needed one)

g10/02 133-134, 299 · g10/03 226-229 · g10/05 58 · g10/07 283 · g10/08 329 ·
g10/09 188-191 · g11/06 216-217 · g11/07 634-635 · g11/08 153, 162-169 ·
g11/09 542-543 · g12/01 117-118, 122 · g12/02 449 · g12/05 85-88, 272 ·
g12/06 170-171, 287 · g12/08 233-236 · g12/09 270-271, 580-581 ·
g12/10 200-203, 396-397, 463. No `!draw` in g10/01, g10/04, g10/06, g11/01–05,
g12/03, g12/04, g12/07. Almost all are `xticklabels` / `yticklabels` lists and
`\foreach` label lists; g12/02 449 splits a node the English axis clips
(reported), g12/08 233-236 moves two Arabic labels that collided at 0.24 cm
spacing, g12/10 463 is a two-line ylabel.

## Link layer

`tools/term_config/book2_ar.py` was curated from this edition's own harvest
(498 linkable terms after curation) and both censuses, never translated from
`book2_en.py`: 126 EXTRA forms, 10 STOP words, 28 protect patterns. Arabic
morphology dominates: the article and one-letter prepositions are a HEAD, so
nothing reaches a broken plural, a dual, a tanween accusative or a possessive
suffix. EXTRA declares the forms the edition really uses — plurals (طيات،
مصائد، عتبات، قواطع، بلوتونات، ألواح مندسة، أوفيوليتات، ستروماتوليتات،
الدورات الجليدية، العينات الجليدية، الصدوع العادية / الزاحفة / المعكوسة،
موجات P / S …), possessives (درجة حرارة توازنها، نقطة نداه، زمن مكوثه، فترة
عودته، جذرها، لوحها المندس …), the indefinite forms of constructs harvested
only in the definite (نقطة ندى، زمن انتقال، فترة عودة، معدل تجريد …), and the
short forms g12/10 uses as English does (تأثير، تغذية راجعة، سيناريو).
Homographs handled, each with evidence in the config:

* **العين** the eye of a cyclone vs the naked eye; **تشبع / مشبعًا** air vs a
  rock saturated with water; **مستقرًا** stable air vs a stable mineral;
  **متوسط** an intermediate rock vs "average" (20 wrong links before the STOP);
  **رتبة** coal rank vs "of the order of";
* **لوح** — linked bare as the slab, as English links "slab", with its other
  senses masked: a glass plate, a wooden board, a solar panel, a slab of shale,
  a tabular crystal (كاللوح);
* **الدفق** — the flux of the water budget, masked in الدفق الحراري (heat
  flow) with a word-start anchor (without it the mask also ate التدفق الحراري
  and dropped all 22 heat-flow links);
* **مشبع / مشبعة** — linked as English links "saturated" and "the saturated
  rate", masked in غير مشبع (unsaturated, unlinked in English), in "saturated
  with water" and in the storm chapter;
* **الجذور** — mountain roots only through explicit phrases (جذور الجبال،
  الجذور العميقة …): bare الجذور is plant roots in g10/07;
* **تأثير بشري** human influence (not a forcing); **قاع المحيط العميق** the
  deep ocean floor; Kelvin's heat **المخزون**; **التطبق الأصلي** of a mud;
  **فوق مافية**; the mathematical **جذر تربيعي**; **التحول من إيقاع** (a
  change of rhythm, not metamorphism); **تلال فاردن**;
* the bold *الجزء الأول …* headings, `\paragraph` run-in headings, `\pageref`
  and inline `\tikz` stay unlinked, as in English.

Over English: body waves 71 vs 55 (Arabic writes "سرعة الموجات P" where English
writes the unlinked compound "P-wave speed"), cleavage 37 vs 24 (الانفصام and
المكسر both belong to the target), slab 96 vs 91. Under English: the igneous
terms (intrusion 61/77, volcanic–plutonic 25/36, felsic–mafic 40/49), whose
adjectives agree in gender and number (البركانية، الجوفية) and collide with
المياه الجوفية and the volcanic arc, so they were left unlinked rather than
linked wrongly.

## English-canon defects reported (not fixed in the canon)

1. `parts/grade-11/01-drift-to-spreading.tex` line 192: "Motonari Matuyama" —
   the geophysicist is Motonori Matuyama (松山基範); the Arabic writes موتونوري.
2. `parts/grade-12/02-mountain-building.tex` line 449: the node "Varden:
   2.2%" (anchor=south east at axis cs:12,4) runs left past x = 0 and is
   clipped by the axis: the English page shows only "2.2 %". The Arabic splits
   it over two centred lines (`!draw` 449).
3. English never links the Saffir–Simpson scale
   (`def:g10:storms-and-cyclones:scale`); the Arabic does twice. Probably a
   dash mismatch between the harvested key and the prose.

## Tool observations

* The prose gates do not cover the image-credit files (Book 1's Arabic credits
  would fail them too: they hold Latin runs by design).
* `id_apply`'s math census compares `$…$` spans exactly, spaces included
  (`$[x\text{, }y]$` was refused against `$[x \text{ to } y]$` until the
  spaces matched).
* The termlinker gives chapter-local linking only to harvested STOP words; an
  EXTRA entry is global, so a sense that is right in one chapter only (لوح،
  مشبع، الدفق) needs protect patterns everywhere else.
* `drawcensus.py` counts `--`, `arc` and `circle` inside node text, so a
  translated label shows as a drawing difference.
* **tcolorbox loses a label at a page break** (style-level, latent in every
  edition): when a decorated box (`\omdecorate`, `lines before break=5`)
  starts at the foot of a page with a tall first element, tcolorbox logs
  "Discard zero height first box part … Using nobreak failed" and drops that
  zero-height part — with any `\label` written in it. In this edition the
  g10/07 weekend problem began at the foot of p. 65 and
  `pb:g10:soil-formation:1` came out undefined (2 undefined references in the
  first final build; the warning is gone from the last build). Fixed in this edition only by placing the `\label` after
  the problem's opening photograph (label order unchanged, commented in the
  source). The section heading "7.7" is still left alone at the foot of
  p. 65. A style-level guard (a `\needspace` before a box, or a non-zero first
  part) would make it impossible; the warning is worth grepping in every
  build log.

## Allow-list entries (`tools/check_arabic_prose.py`, each commented "Book 2 ar")

`{"nnr", "morvel"}` (NNR-MORVEL56, g11/06), `{"chmee"}` (Commons author,
g11/07), `{"gplates"}` (GPlates, g12/02).

## Coordinator amendments (2026-10-26)

- Coordinator verification: forced build 334 pp, 0/0/0, nullfont 3,291, `.fls` 56 = 56, gates green for grades 10–12, linker dry run 0, 2,137 links over 137 targets. The two reported English-canon defects were confirmed and fixed in all eight books (Motonori; the clipped Varden label, whose fix also moved the 13 % label — your g12/02:449 node now has the English anchor and position, your wording kept). The Saffir–Simpson report is not a defect: English uses the term only inside its definition.
- Leading-run sweep (2026-10-26): four more `\qty{N}{\degree} ش` labels in g10/03 (two legend entries, two nodes) printed "°30 ش"/"°35 ش"; boxed with `\mbox{\textdir TLT …}`, rebuilt 334 pp 0/0/0, re-read on the page.

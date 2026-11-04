# Translation score — One Earth and Space Sciences Book 3 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 3 (University, Year 1, `bachelor-1`) |
| **Language** | Arabic (`ar`), Modern Standard Arabic, right-to-left; Latin runs boxed with `\babelsublr` or `\mbox{\textdir TLT …}` |
| **Model (drafting)** | claude-haiku-5-5, effort high |
| **Coordinator** | claude-opus-5-5 |
| **Overall score** | **95** (rescored 2026-10-28 after the completed reading stint and the `ar-11` build; was 94) |
| **Ship threshold** | ≥ 95: **met** (see open items for what remains outside the edition) |
| **Scope** | 29 chapters and their 29 solution files (58 files); term layer (3,354 links); image credits (30 items, translated this run); entry file unchanged |

## Build (forced, TeX Live 2026, wrapper, final build `ar-11`, 2026-10-28, after the last edit and the relink)

- `ar-11`: rc 0, **426 pages**; errors 0; undefined 0; **overfull 0**; nullfont 0; missing characters 0; invalid-in-math 0; zero-height 0.
- `.fls` lists 58 translated files = the 58 on disk.
- Header-only pages: none. A `pdftotext` scan of all 426 pages finds two pages with almost no body text: p. 353 is the solutions part title ("حلول التمارين، القسم II") and p. 427 is the empty split after the last page; neither is a defect.
- `check_translation.sh bachelor-1 ar`: PASSED (after the last edit). `engsweep.py ar`: empty. Linker dry run: 0 (3,360 links on 57 files after the final relink).

## Gates

- `tools/check_translation.sh bachelor-1 ar`: **PASSED** (Arabic prose gate, 58 files; chemistry-twin gate, 58 files).
- `tools/gates.sh bachelor-1`: **OK**.
- `engsweep.py ar`: empty (re-run after the last edit).
- `numdiff.py ar solutions`: 9 files differ, and every difference is accounted for: Arabic letters fused to a digit (`و285`, `ب2.82`, `و0.98`, `و26.33`), spelt numbers (`ثمانية عشر`, `الأربع والعشرين`, `الموازي الأربعين`, `أربعة`, `اثنان`), and one `-1` token that a stricter count shows as equal (2 and 2).

## Term layer (`tools/term_config/book3_ar.py`, AMBIG_POLICY "drop")

- **Links / targets.** English: 4,650 links on 184 targets. Arabic: **3,354 links on 185 targets** (after the reading stint; was 2,792). Every English target except three is reached. The three Arabic-unreached targets are `cross-sections:log` (the only Arabic word for it, *المطابقة*, is also a least-squares fit and was protected), `stratigraphic-scale:gssp` (only in its own definition) and `isostasy-gravity:airy` (ch. 20 does not name Airy). Four Arabic-only targets, each right-sense: `chert` (*الصوّان*), `mean-orientation` (*الوضعية المتوسطة*), `ridge-classes` (*الحيد البطيء/السريع*), `parcel` (*الطرد الهوائي*).
- **Homographs stopped or protected** (wrong senses removed; the right senses kept):
  - *الميل* (declination in ch. 1, 27; slope in ch. 2, 4, 13, 14, 16, 21, 24): STOP. The celestial links that remain are the ch. 1 and ch. 27 uses; the rest are under-linked.
  - *الارتفاع* (altitude; height everywhere else): STOP.
  - *الاتجاه* (trend; every ordinary direction): STOP, and a protect for the remaining bare uses. *اتجاه الانحدار*, *اتجاه الغوص*, *الاتجاه الانقلابي* keep theirs.
  - *الأصل* (parent isotope, and "original"): STOP and protect.
  - *الإشعاعية* (luminosity; radiant quantities; radiogenic daughter): STOP. *الدفق* (flux) still links.
  - *النظام* (chronostratigraphic system; closed or climate system): STOP.
  - *الرتبة* (order of interference colours): protect everything except the ordinals, and keep the colour uses (*من الرتبة الثانية (640 nm)*); mask the "to first order" approximations and the orders of magnitude.
  - *الانحدار*: protect the steep slope (*شديد الانحدار*), the slope of a channel, and the magnitude. Dip keeps its links.
  - *المطابقة بالمربعات* (least-squares fit), *الامتداد المنقّط* (dotted extension), *مستقرًا* (stable phase), *لجنة الخريطة الجيولوجية* (the commission), *المجموعة الشمسية* (solar system), *نحو الشمال تدفّق الحرارة* (overturning transport), *الانقلاب*-side words (*الطرف الأيسر*, *في الأيمن*, …), *تعود إلى الانحدار*, *حجم الانحدار*, *جداء العمق والانحدار*, *امتداد فرّق* (caldera extension), *غوص الناجم* (subsidence).
- **EXTRA** (accepted forms that the harvest could not reach, right sense only): 25 forms for accretionary prism, evaporites, sedimentary basins, oriented samples, temperature inversion, finite rotations and closure temperatures (indefinite and plural forms).
- **Accepted losses.** The homograph protection has a cost: under-linking of *trend* (about 70 uses), *altitude* (about 66), *declination* (about 40), *luminosity* (9), *parent* (14) and *system* (about 10). The loss is documented in `book3_ar.py`.

## Measured censuses

- **`\index{}` keys and `\text{}`:** not re-counted this run; the id_apply census passed on every re-applied range (labels, envs, solutions, emph, index, math, draw, img, chem).
- **Figures and tables (rendered, printed page numbers): checked on pp. 33 (ch. 4 text page), 169 (ch. 16 shear figure and inline `pmatrix`), 174 (ch. 16 envelope: MPa and km labels), 199 (ch. 18 fault-slip chart, x label "(km)"), 217 (ch. 20 figure), 247 (ch. 22 axis label "(km)", cropped at 200 dpi), 270 (ch. 24 chronostratigraphic table, the 251.902 row and the ages), 272 (ch. 24 ICS chart, numbers and axes), 279 (ch. 25 table of decay systems), 297 (ch. 26 T–S diagram). Printed page + 12 = PDF page. Each RTL defect found was fixed and re-rendered.

## RTL defects found and fixed this run

- **Axis labels with a Latin unit at the end (reversed `(km)` → `(mk)`):** ch. 18 (x label), ch. 16 (x label `(MPa)`, y label `(km)`), ch. 22 (x label `(km)`), ch. 26 (two y labels `(km)`). Fixed by `\unit{…}`, as the ch. 10 and ch. 12 labels already do. The ch. 22 edit is a direct edit (its patch has an addendum); see the progress notes.
- **Table cell starting with Latin (`U، Th (ppm)`):** boxed with `\mbox{\textdir TLT …}`.
- **Node line starting with a parenthesis (`(أ) قبل التشوّه`, `(ب) قصّ نقي`, `(ج) قصّ بسيط`):** the closing ")" printed at the wrong end; each line wrapped in `\foreignlanguage{arabic}{…}`.
- **Literal `\n` typed in a patch (ch. 16, line 376):** it broke the build ("Undefined control sequence"). Fixed in the patch and the file.

## Fixes made in this pass

- **Overfull boxes, 7 → 0.** Words added before frozen formulas (ch. 1 "نحسب"; sol. 3 "نتحقّق من أن المتجهة الناظمية ذات طول واحد:"; sol. 13 "، فيكون:"; sol. 17 "قدرها"; sol. 15 "لدينا"), a `\shortstack` header in the ch. 10 table (three headers), a hyphenation hint in ch. 24's chronostratigraphic table, and, in the same table, the first column narrowed from 2.4 cm to 2.3 cm while the age column widened from 1.2 cm to 1.3 cm (total width unchanged; direct edit, see the progress notes).
- **Credits.** `frontmatter/image-credits-book3.ar.tex` was still the English file. Translated item by item (30 items, Book 2 style: names transliterated with the original in parentheses; institutions, datasets, works and licences verbatim in `\babelsublr`; `CC BY-SA 4.0` etc. exact).

## Native pass (reading stint, 2026-10-28)

- **Read AR-first and compared with the English twin, sentence level:** ch. 2–11, 13–19 and 21 (course text). Ch. 1, 12 and 24 were read by the coordinator.
- **Read AR-first only, no sentence-level comparison with English:** ch. 20 (to about line 560), 23 (to exercise 4), 26 (whole chapter), 27 (to about line 500), 28 (to exercise 4 and the problem), 29 (to about line 520).
- **Not read:** the exercises and problems of ch. 20, 22, 23, 26, 27 and 28 (the tails), and their solutions files.
- The gates, censuses, number diff and rendered pages cover all 58 files mechanically; they do not replace a native read.

### Fixes in the reading stint (all in `parts/bachelor-1/ar/`)

- ch. 2: airmass definition ("العمق البصري"); removed a doubled "لهذا السبب".
- ch. 3: "مما تجذبه كرةٌ لها الكتلة نفسها."; "جليدًا --- الماء والميثان والأمونياك --- تحت"; "يدلّان على أنه لا يملك على الأكثر إلا لبًّا حديديًا صغيرًا."
- ch. 5: "وارسم الكنتورات موازية للامتداد،"; "المفصولين بالإزاحة الأفقية".
- ch. 6: "ويتبع من \cref{ch:b1:geological-maps} أنّ $\vec n$ هو الناظم:".
- ch. 7: "اللذان يخلو منهما الغرانيت"; "عالِم المعادن الذي يتعرّف عينةً يدوية"; "ودالةً خطيةً بالنسبة إلى $x$ فقط".
- ch. 8: "مخطط ميشيل–ليفي محسوب"; "للانكسار المزدوج"; table caption "PPL: الضوء المستقطَب المستوي".
- ch. 9: "النوعان الأوليان من وصلات موهوروفيتشيتش"; "بمقدار \qty{54}{km}"; "للب الخارجي"; the gravity sentence on the core; "وأيّها يُقارَن بنموذج PREM نفسه وحده؟".
- ch. 10: "للقشرة" and "للوشاح" (two sites each); "ما كسر \qty{173000}{TW}"; "بوحدة \unit{km}".
- ch. 16: "وزاوية المحور الطويل للقطع الناقص للانفعال".
- ch. 17: "بين المستقطِبين المتقاطعين" (two sites, replacing the non-standard "النيكولين"); "للطيّات"; "للمستوى"; "وللتشقّق"; "احسب النسبة للصدوع العادية".
- ch. 18: "بالنسبة للجدار المرتكز" (two sites).
- ch. 21: every doubled-article site ("للتموّج", "للتموّجات" x2, "للكثبان", "للسمت", "للسموت", "للعكَر").
- ch. 22: "للشعاب المرجانية"; removed a doubled "ما" in "وهو ما كان ليعطيه ملء واحد للبحر أبدًا.".
- ch. 24: "ب GSSP" and "و GSSP" (five sites, previously fused to the Latin acronym), the spacing the rest of the edition uses before Latin acronyms. Relinked, dry run 0.
- ch. 25: "ولليورانيوم-238 عند"; "فوق اللاتوافق".
- ch. 27: "المساوي للميل الشمسي".
- ch. 28: "وهو النواة السريعة للرياح الغربية".
- ch. 29: name transliterations (Nansen, Wilhelm Bjerknes, Vagn Walfrid Ekman) and "تُضغط عودة الدوّامة على الجانب الغربي".

### Spot checks (no edit needed unless noted)

- Arithmetic checked: ch. 2 extinction; ch. 3 Io mass; ch. 4 cross product and dip; ch. 6 declination and cross product; ch. 7 olivine recalculation and densities; ch. 8 retardation and Michel–Lévy numbers; ch. 9 Mars and Earth figures; ch. 10 radiogenic numbers; ch. 11 Airy, Pratt and Bouguer; ch. 20 shear stress and Shields numbers; ch. 29 Ekman pumping.
- **English canon suspect (not edited):** the borehole thickness statement in ch. 5. The coordinator should check it against the English.

### Term fork (for the coordinator)

- Unconformity is *عدم التوافق* in ch. 4, 5, 13 and 17, and *اللاتوافق* in ch. 24 and 25. One term should be chosen for the whole edition.

## Open items (why the score is 94, not 95)

- **Native read is complete for ch. 20, 22, 23, 25–29** (course text, definitions, captions, exercises, problems and solutions, sentence level against the English twin, 2026-10-28). The 22 fixes made in that stint are listed under "Reading stint 2" below. The rest of the edition was read in earlier stints.
- **Figure node labels** inside the TikZ/pgfplots code of ch. 20–29 were compared label by label with the English only where the label text is visible in the source; the gates and the rendered build cover the rest mechanically.
- **Under-linking (3,354 of 4,650; gap 1,296).** Most of the gap is the homograph protection (see Term layer). Every English target except three is reached. This is acceptable by the instruction, but it is the largest visible difference from English.
- **ICS chart labels (ch. 24):** the built figure is in Arabic, so the English-left-in item from the earlier score is closed.
- **Credits caption in ch. 24 (Zumaia figure)** keeps its Latin credit in parentheses in the body caption; the credits list itself is translated.
- **Patch stale, three places.** The `ch22` label (direct edit; `b22a.patch` is an addendum to `b22.patch`), the ch. 24 table spec (direct edit; not in `b24.patch`), and the ch. 24 GSSP spacing (direct edit). A re-apply of any of these would reintroduce the old text, so the next re-application must carry them into the patches.
- **Unconformity term fork: closed.** *عدم التوافق* is used everywhere (ch. 4, 5, 13, 17, 24, 25 and the ch. 25 solutions); no *اللاتوافق* / *لاتوافق* remains.
- **Canon suspect in ch. 5** (borehole thickness, English) needs checking.

## Reading stint 2 (2026-10-28, ch. 20, 22, 23, 25–29)

- **Unconformity** unified to *عدم التوافق* at 8 sites (ch. 24 ×3, ch. 25 ×3, ch. 25 solutions ×2), grammar kept (indefinite *عدم توافق* where the source is indefinite).
- **Meaning and term fixes:** ch. 20 "جزء من عشرين" (a twentieth, not twenty); ch. 20 "غلّة" → "تدفّق" for a flux (ex. 4); ch. 20 "تُصدِّر حوض" → "يُصدِّر"; ch. 20 problem "مقياس قياس" → "تسجّل محطة قياس"; ch. 20 sol. "والتطهير" → "وإزالة الغابات"; ch. 20 "النارّي" → "الناري"; ch. 22 ex. 7 "شعبة" → "شعبة مرجانية" (the English is *reef*); ch. 25 ex. 3 "فحم" → "الكربون" (the English is *carbon*, not charcoal); ch. 23 "مضغوط فوق الحدّ" → "مفرط الضغط" (overpressured; the old wording read as over-compacted, the opposite sense); ch. 23 "تعالجه مجلد" → "يعالجه مجلد" (agreement); ch. 29 "يتصرّف عن الرفوف" → "ينصرف عن الرفوف" (drains off).
- **Doubled words and articles:** ch. 23 "فقد فقد"; ch. 25 sol. "لالوشاح" → "للوشاح"; ch. 28 "ريشُ الريح الريح الجيوستروفية" → "ريشُ الريح الجيوستروفية". A sweep of ch. 20–29 for doubled words and articles found no other real case.
- **Checked and kept:** ch. 25 sol. "الطفل"-type mudrock usage in ch. 20 (the book uses *الطفل* for mudrock in ch. 19); the "ب\cref" and "ل\qty" proclitic pattern (used throughout the edition); the ch. 22 "جزيءً" orthography.
- **Numbers:** every solution's arithmetic was rechecked along the rounded path (ch. 20 Stokes and combined-law table, ch. 22 CCD and evaporite masses, ch. 23 decompaction and loading, ch. 25 isochron and U–Pb ages, ch. 26 N and θ values, ch. 27 insolation and transport, ch. 28 geostrophic and angular-momentum values, ch. 29 Ekman values). No number in the Arabic differs from the English.
- **English canon, not edited (for the coordinator):** (a) ch. 23 text (l. ~610) says seven stacks over 430 kyr and five over 800 kyr, but the figure caption says five records over 800 kyr and seven over 140 kyr; the Arabic mirrors the text. (b) ch. 22 problem Part II item 4: "fresh seawater" flowing in is self-contradictory (the sense is ordinary seawater); the Arabic mirrors it. (c) ch. 22 Chagos reef: a dry bulk density of 2000 kg/m³ with grains of 2.71 g/cm³ gives a porosity of about 26 %, not the stated third.

## Coordinator verification (claude-opus-5-5, 2026-10-28)

Accepted at 95 after the coordinator's own checks and fixes:

- The coordinator's own fixes:
  - Two box titles left in English: ch12 *Tectonics on a sphere* → *التكتونيات على كرة*; ch20 *Beryllium-10 in river sand* → *البريليوم-10 في رمل الأنهار*.
  - Photo credits: *public domain* → *ملك عام* (14 sites) and *via Wikimedia Commons* → *عبر Wikimedia Commons*, as in Arabic Books 1–2. *Unidentified NOAA photographer* → *مصوّر مجهول من NOAA*. The Latin comma after *ملك عام* became *،*. Names, institutions and NASA's own credit line stay Latin.
  - Earlier: solution 17 `\ang{074.8}` restored, in the file and in `s17.patch`; canon edit 9 (ch05 boreholes) made directly in the file.
- Gate change: the phrase entries of `CREDIT_TITLE_PHRASES` in `tools/check_arabic_prose.py` now carry the translated credit wording, so the gate still recognizes each credit. The gate stays green on Arabic Books 1–2.
- Rulings: the stale patches are known. This edition is edited in its files only (unwrap, edit, relink), never re-applied from the patches. The ICS chart is in Arabic. Link coverage of 3,360 / 4,650 is accepted: the gap is homograph STOPs, and a wrong sense is worse than a missing link. *عدم التوافق* is the term for unconformity, as in Books 1–2. *Myr* is kept. The ")⋆(" heads are correct right-to-left output. The reported ch23 430 kyr and the ch22 "fresh seawater" are faithful to the English. The ch05 borehole report was real: canon edit 9 fixed it in English and every edition.

Checks: the English-function-word sweep is empty. The PDF-text sweep shows only names, places, titles and credits kept in Latin. `check_translation.sh bachelor-1 ar` PASSED, and the linker dry run is 0. Final build (TeX Live 2026, forced, `close-ar`, after the last edit): 426 pp | 0 errors | 0 undefined | 0 overfull | nullfont 0 | missing-char 0 | invalid-in-math 0 | zero-height 0 | `.fls` 58.

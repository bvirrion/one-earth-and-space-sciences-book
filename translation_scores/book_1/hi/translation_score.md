# Translation score — Earth and Space Sciences Book 1 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 1 (Primary and Middle School, Grades 1–9) |
| **Language** | Hindi (`hi`) |
| **Quality bar** | **native school prose at every level**: a Hindi children's science book read aloud in grades 1–5, a Hindi middle-school science and geography textbook in grades 6–9, in the established Hindi vocabulary of school geography, geology and meteorology. English is the source of truth for content, structure, labels, numbers, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); `hindi_style_card.md`; the shipped Hindi editions of One Biology Book 1 and One Chemistry Book 1 (`../one-biology-book/parts/*/hi/`, `../one-chemistry-book/parts/*/hi/`) for typography (danda, ASCII digits, decimal point, ``…'' quotes), the **तुम** register of the school years and the solution and problem headers; the Hindi physics editions for shared physical vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-25 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 32 chapters + 32 solution twins = **64 files**, every one written through `tools/id_apply.py` line-range patches; `frontmatter/preface.hi.tex` and `frontmatter/image-credits.hi.tex`; the aside-box block of `styles/lang/hi.tex`; the `\bookline` / `\author` lines of the entry file; a curated `tools/term_config/book1_hi.py`; the defined-term link layer; Hindi index keys; the overfull sweep; and this score |

## Verdict in one line

A Hindi Book 1 that reads as one Hindi school course in the Earth and space
sciences from the first year to the ninth — तुम and short sentences for the
youngest readers, the explanatory textbook register of the middle years,
तुम-imperative exercise stems throughout (*बताओ, लिखो, समझाओ, निकालो,
देखो*), the danda, Indian numbering where a school reader counts (*लाख,
करोड़*), and the standard Hindi technical terms (*अपक्षय, अपरदन, निक्षेपण,
जलभृत, विवर्तनिक प्लेट, अभिसारी / अपसारी / रूपांतर सीमा, अधिकेंद्र,
परिमाण, अध्यारोपण का सिद्धांत, विषमविन्यास, क्षोभमंडल, वाताग्र, समदाब
रेखा, हिमनद, ग्रीनहाउस प्रभाव, संकट / सुभेद्यता / जोखिम, समोच्च रेखा*) —
with every structural and prose gate green over the nine years and a forced
build of **0 errors / 0 undefined / 0 overfull**, 313 pages.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 64 files against their 64 twins: **370 `exercise`**, **20 `problem`**, **390 `\begin{solution}`**, **234 `omfigure`**, **161 `tikzpicture`**, **73 `axis`**, **120 raster includes**, **455 `\emph`**, **237 `\index`**, **105 `\cref`**, **816 `\label`**, **468 `\item`**, **834 `\qty`**, **588 `% ledger:`** comments, **150 `\foreach`**, and per environment **140 `definition`, 4 `proposition`, 42 `method`, 60 `example`, 24 `remark`, 30 `recall`, 7 `inthefield`, 9 `inthelab`, 10 `history`, 2 `dated`, 7 `safety`** — all equal to English. `\node` is 746 against 677: every English label read from a figdata table (`nodes near coords` with `point meta=explicit symbolic`, `yticklabels from table`) became explicit Hindi `\node`s or tick labels under `!draw`, coordinates copied from the `.dat` rows; the coordinator's drawing census (`drawcensus.py hi`) reports only those `\addplot` label layers (g3/02 8→6, g6/05 11→10, g7/05 22→15, g8/01 9→8) and one `--` in g9/01 that is the year range of an `xticklabels` list, not a path. A per-file number census against English finds only intended differences: Indian numbering (*3 करोड़ यानी 300 लाख* for 30 million, *33 लाख* for 3.3 million), *उन्नीसवीं सदी* for "19th century", distributive *4-4*, *10-10*, the 12-hour clock beside the 24-hour one (*रात 11:25 बजे (23:25)*), and the explicit label coordinates |
| Terminology | **96** | One Hindi glossary held across nine years: *मौसम, मौसम केंद्र, वर्षामापी, वायु-दिशासूचक*; *खाका, मानचित्र, संकेत-सूची, मापनी, दिशा-चक्र*; *कंकड़, रेत, चट्टान, कीचड़*; *ग्लोब, भूमध्य रेखा, गोलार्ध, महाद्वीप, महासागर*; *ऊँचाई, समुद्र तल, उच्चावच*; *अपक्षय, अपरदन, निक्षेपण, सोता, मुहाना, सहायक नदी, विसर्प, बाढ़, बाढ़ का मैदान*; *प्राकृतिक संकट*; *चट्टानी / विशाल ग्रह, अक्षांश, देशांतर, प्रमुख याम्योत्तर, समय-क्षेत्र, तिथि रेखा*; *खनिज, आग्नेय / अवसादी / कायांतरित चट्टान, शैल चक्र, मोह्स पैमाना*; *भूपर्पटी, प्रावार, क्रोड, P / S तरंगें*; *अपवाह, अंतःस्यंदन, सरंध्रता, पारगम्यता, भौम जलस्तर, जलभृत*; *विवर्तनिक प्लेट, अपसारी / अभिसारी / रूपांतर सीमा, महासागरीय कटक, गर्त, पैंजिया*; *मैग्मा कक्ष, निकास-छिद्र, क्रेटर, पायरोक्लास्टिक प्रवाह, तप्त स्थल*; *भूकंप-मूल, अधिकेंद्र, परिमाण, तीव्रता, भूकंपमापी, सुनामी*; *स्तर, जीवाश्म, साँचा*; *अध्यारोपण / अनुप्रस्थ काट / अंतर्वेशन का सिद्धांत, विषमविन्यास, महाकल्प, भूवैज्ञानिक समय-मापक्रम*; *क्षोभमंडल … तापमंडल, ओज़ोन परत, व्यापारिक पवनें, पछुआ पवनें, वायु राशि, शीत / उष्ण / अधिविष्ट वाताग्र, अवदाब, प्रतिचक्रवात, समदाब रेखा*; *महाद्वीपीय मग्नतट, वितलीय मैदान, वलय, समुद्री बर्फ़*; *हिमनद, संचयन / अपक्षरण क्षेत्र, U-आकार की घाटी, हिमोढ़, हिमचादर, हिम शेल्फ़, पर्माफ़्रॉस्ट*; *ग्रीनहाउस गैसें, तापमान विसंगति, वैश्विक तापन* with the IPCC's calibrated likelihood words (*लगभग निश्चित, अत्यंत संभावित, बहुत संभावित, संभावित …*); *संकट, सुभेद्यता, जोखिम, रोकथाम, संकट मानचित्र, 100-वर्षीय बाढ़*; *अयस्क निक्षेप, सांद्रण गुणक, शिरा, प्लेसर, समुच्चय, भंडार*; *उत्थान, बरखान, फिसलन फलक, खाँच, तरंग-घर्षित चबूतरा, तटीय अपवाह, भू-जिह्वा, कार्स्ट, घोलरंध्र*; *मर्केटर / समक्षेत्र प्रक्षेप, संख्यात्मक मापनी, मापनी-पट्टी, समोच्च रेखा / अंतराल, स्थानिक ऊँचाई, सूचक समोच्च रेखा, स्थलाकृतिक परिच्छेदिका, सुदूर संवेदन*. One homograph was removed from the prose itself: the sea **floor** is always *समुद्री तल* and *समुद्र तल* only ever sea level. All 237 `\index{}` keys rewritten in Hindi. Proper names in Devanagari transliteration in the bodies, kept in Latin in the image credits |
| Register / tone | **97** | Measured, not assumed, over course **and** solutions: **0** आप of address in all nine years (the 11 hits are all the reflexive *अपने-आप*), **0** -इए / -कीजिए imperative stems (the -िए words are *लिए, इसलिए, चाहिए, ज़रिए, दिए, किए*); the तुम imperatives (*करो, बताओ, लिखो, समझाओ, निकालो, देखो, पढ़ो, बनाओ, गिनो, पहचानो*) run 12/15/9/11/9/51/63/44/51 per grade. Box names: *पहले से ज्ञात* (pronoun-free, as the Hindi chemistry edition settled), *क्षेत्र-कार्य* (a bare *क्षेत्र* reads "region"), *प्रयोगशाला में*, *इतिहास*, *आँकड़े: वर्ष 2025*, *सुरक्षा*. Observation-only wording kept everywhere (cliffs and quarries seen from a distance, the Sun never looked at) |
| Typography | **97** | Danda ends every Hindi sentence (4,995 dandas); the period stays inside display mathematics; ASCII digits and the decimal point as the series' siunitx setting and the shipped Hindi editions do; Hindi quotation in ``…''; final sweeps: **0** Devanagari letter followed by a Latin full stop, **0** straight quotes; no non-ASCII text inside `\qty{}`, `\unit{}` or `\num{}`. Sub-parts (क)–(च) |
| Fidelity / accuracy | **95** | Every course paragraph, worked example, exercise and solution was translated against its twin with the numbers recomputed while translating; every weekend-problem solution checked against its statement (in grade 9: the planet's thermometer, the school site on the Varden Hills map, the new town built from a local sand pit, the cliff and the coastal road, the trail across the Varden Hills); a last per-file number census against English found no unintended difference. Where Hindi word order had to be bent to keep the math and `\qty` order frozen, the sentence was rebuilt rather than left awkward. The coordinator's wave-1 canon fixes (`sources/WAVE1_FINDINGS.md`) are mirrored, and so is the late fix to grade-7 solution 11 (*$14.2 \div 2.2 \approx 6.45$: लगभग 6 गुना तेज़।*, no double rounding) |
| Figures | **95** | All drawing code byte-identical except the **134 documented `!draw` ranges** (listed below; almost all are `\foreach` label lists, `xticklabels` beside ASCII symbolic coordinates, and figdata label layers replaced by explicit nodes). TikZ node text, axis labels, legends and `{\small …}` captions localized; compass letters *उ पू द प* in every rose and north arrow. All 165 figure pages of the final PDF read (4-up at 95 dpi, zoomed to 150–200 dpi where dense); found and fixed in that pass: the drill sub-labels touching the bold verbs (g4/02), the seismograph drum label running into the delay label (g7/03), *निम्न* over the cold front (g8/03), a doubled *मैग्मा मैग्मा* in the volcano caption (g7/02) |
| Links | **96** | **6156 `\omterm` links on 138 targets** against English's **6103 on 137**: every English target is linked (**0 missing**), plus the geological time scale (1 link, the g7/05 time-scale caption, which opens on *भूवैज्ञानिक समय-मापक्रम*; the English caption does not name the term). Both censuses (frequency and chapter set) run after the last edit; dry run over the wrapped tree: **links to insert: 0** |

## Gates

`bash tools/check_translation.sh grade-N hi` for N = 1 … 9: **9 / 9 PASSED**
(structural censuses, duplicate labels, ledger ids, the Hindi prose gate —
residual English, transliterated function words, Latin full stops, spaces in
math —, orphan lines, problem numbering, the twin gate), run after the last
edit.

Build (`latexmk -g`, forced, through the run's wrapper under its memory cap):
`grep -ac '^!'` **0**, `grep -aci undefined` **0**, `grep -ac Overfull`
**0**, nullfont **6633** (= the English baseline, the backtick-in-nullfont
noise every Book 1 build shares), non-backtick missing characters **0**
(Øyvind, Vågen, Viñas render), invalid-in-math **0**; **313 pages**
(English 324); the `.fls` lists **64** Hindi chapter and solution files =
**64** on disk. The first forced build had 5 overfull boxes, all `in
paragraph`: three in the image credits (long unhyphenated Latin names; an
`\emergencystretch` local to the credits list), one in the grade-4 example
*मानचित्र पर गिनती* and one in the grade-9 solution 11 (both cleared by
rewording before the frozen span, never by shortening).

## Conventions recorded

* **Compass letters**: *उ, पू, द, प* (`\omnameCompassN{उ}` …) in every
  figure, rose and north arrow (the two Latin *N* north arrows of g9/04 and
  g9/05 changed to *उ* under `!draw`); in prose the full words after an angle
  or a coordinate (*\ang{60} उत्तर*, *30° दक्षिण*).
* **Large numbers**: *मिलियन* / *अरब* where the text is a data statement of
  the middle years; *लाख* / *करोड़* where a young reader counts (grade 4's
  areas, grade 6's pressures), always with the arithmetic redone in that unit.
* **Headers**: *अभ्यास*; the weekend problem *सप्ताहांत समस्या --- …*, its
  parts *भाग I --- …।*; solutions *अध्याय \ref{…} --- शीर्षक*.
* **AI images**: *(एक सामान्य दृश्य का AI चित्रण)* / *(AI चित्रण।)*; sketches
  *(एक रेखाचित्र)*.

## Link layer

`tools/term_config/book1_hi.py` was curated from this edition's own `--terms`
harvest, an inflection scan of the Hindi corpus, and the frequency and
chapter-set censuses against English, with a context read of every flagged
word — never translated from `book1_en.py`. Its docstring records each case.

* **STOP**: *ऊँचाई* (altitude, but also every height — it doubled English),
  *स्तर* (stratum, but "level" everywhere else), *सूखा* (drought, but the
  adjective "dry"), *पायरो* (an etymology emph).
* **EXTRA**: *प्लेट / प्लेटें / प्लेटों* → the tectonic plate (the bodies
  drop *विवर्तनिक*), *तिथि रेखा* → the date line, *कर्क रेखा / मकर रेखा* →
  the tropics, and English's grade-8 "the tropics" as Hindi writes it: the
  pair *कर्क और मकर रेखाओं* or the zone *उष्णकटिबंध* (the noun only; the
  adjective *उष्णकटिबंधीय* of a tropical cyclone or air mass stays unlinked).
* **DERIVED** (≈100 entries, among them *कुआँ → कुएँ, कुओं* and *वायु
  राशि → वायु राशियाँ, वायु राशियों*, found by a last scan for undeclared
  inflections): `lang_hi.py` derives nothing, so every oblique
  or plural the bodies write (*चट्टानें / चट्टानों, नदियाँ / नदियों, टिब्बे /
  टिब्बों, समोच्च रेखाएँ / रेखाओं …*) is declared, each read as an inflection
  of the same word; derivations that are other words or senses (*सूखे* "dry",
  *मौसमों* "seasons", *स्तरों* "levels") are not.
* **EXTRA_PROTECT**, Hindi homographs English does not have: *मौसम* as a
  season (*बरसात का मौसम, सूखे मौसम, हर मौसम, मौसमों*) and *मौसम वैज्ञानिक*;
  *मैदान* as a field or meadow (*खेल / स्कूल के मैदान, घास का मैदान*);
  *कीचड़ प्रवाह* (the mudflow, one English word, unlinked); *ध्रुव तारा*;
  *ऊर्ध्वाधर मापनी*; *गरम सोते*; *ETOPO1 उच्चावच*; *अमेरिका महाद्वीप*; the
  invented *वार्डन पहाड़ियाँ*; *सूखा रहता* (a house that "stays dry", inside the
  drought chapter itself); run-in `\paragraph{}` heads and the bold
  *भाग I/II/III* problem heads.

Target counts that differ most from English, each read: *महासागर / समुद्र*
489 vs 518 and *पानी / जल* 483 vs 460 (both within 6 %, from rephrasing in
both directions); *ऊँचाई* 48 vs
68 (the STOP: it links in its own chapter, and altitude is reached through
*समुद्र तल*); *ज्वालामुखी* 140 vs 121 and *भूकंप* 170 vs 161 (Hindi repeats
the noun where English says "it", "the mountain", "the eruption", and uses it
as a modifier, *ज्वालामुखी वेधशाला*); *समोच्च रेखा* 25 vs 17; *मापनी* 9 vs
15 (English links the "scale" of "scale bar" in grade 8 and in grade 9
chapter 2, and of "scale model" in grade 6; Hindi writes the one word
*मापनी-पट्टी*, a term the grade-9 maps chapter defines later, so those sites
stay unlinked rather than link forward, and the scale model is a *पैमाना मॉडल*, outside the map sense). The spring-and-well target is at 81 vs 80
after the *कुआँ* forms were declared, the tropics at 17 vs 17. Six
chapter-set outliers (one link each where English has none: water g3/02,
continent g8/02, cloud g5/02, precipitation g7/04, volcano g8/04,
weathering g9/03) were read and are the defined sense.

## `!draw` ranges (English line numbers)

g1/01 92–93, 97–98, 122–123, 136–138, 187–189, 204–207 ·
g1/02 228 ·
g3/01 105–109 ·
g3/02 63–65, 77–79 ·
g4/01 378–379 ·
g4/02 223–224, 235–236, 248–249 ·
g4/03 87–88, 93–95 ·
g5/01 57–59 ·
g5/02 85–86, 157 ·
g5/03 168–169 ·
g6/01 76, 149, 207–208, 220, 329–330, 366–367 ·
g6/02 244–246, 251–256, 325–326 ·
g6/03 299–300, 323–324, 328 ·
g6/05 224, 271–273 ·
g7/02 476 ·
g7/03 342–343, 626–629 ·
g7/04 163, 322 ·
g7/05 356–363, 421–423, 436–444, 510–512, 515–520 ·
g8/01 126, 131–133, 201, 209–211 ·
g8/02 61, 74–75, 142, 263, 268, 396–404, 531 ·
g8/03 292, 350, 533 ·
g8/04 141, 161 ·
g8/05 97, 161, 163, 172, 175–177, 330 ·
g9/01 115, 121, 214, 216, 244, 250, 252, 305, 340, 343, 345 ·
g9/02 85–88, 91–96, 170, 176, 180, 187, 190, 194, 197, 201, 254–255, 271, 329, 338, 347, 357, 560–561, 576 ·
g9/03 77–78, 139, 141, 144, 146, 148, 244–247, 320–325, 391, 398–401, 450–458 ·
g9/04 85, 96, 108, 111–113, 174–180, 194–198, 277–280, 292, 304–305, 362, 366, 378, 382, 384, 386, 389, 487–488, 490, 492, 494, 496–497, 734 ·
g9/05 72, 81, 179–181, 188, 192–193, 268.

Almost all are `\foreach` label lists, `xticklabels` beside ASCII symbolic
coordinates, figdata label layers replaced by explicit nodes, and the two
Latin *N* north arrows; four were added by the final figure check (g4/02
223–224, 235–236, 248–249: the drill sub-labels lowered off the bold verbs;
g8/03 292: *निम्न* shifted off the cold front).

## Samples (Hindi, with verdict)

1. **Grade 1, watching the weather** — «सुबह-सुबह का समय है। लीना जागती है,
   अपने कमरे की खिड़की के पास रखी कुर्सी पर चढ़ती है और बाहर देखती है।
   आसमान धूसर है।» → **native**: the rhythm of a Hindi picture-book read aloud.
2. **Grade 6, water underground** — «खड़ी ढलान पर, नंगी या सख़्त ज़मीन पर,
   सड़क या कार पार्किंग पर, या जब मिट्टी पहले से भीगी हो, तो ज़्यादातर पानी
   बह जाता है।» → **native**: the explanatory textbook register.
3. **Grade 7, plate tectonics** — «32 साल के जर्मन मौसम वैज्ञानिक अल्फ़्रेड
   वेगनर ने 1912 में दो लेखों में महाद्वीपीय विस्थापन का सिद्धांत रखा।
   ज़्यादातर भूवैज्ञानिकों ने उसे ठुकरा दिया।» → **native**; *मौसम वैज्ञानिक*
   is masked from the weather link.
4. **Grade 9, natural risks** (the definition of risk) — «जहाँ कोई संकट नहीं,
   या ऐसा कुछ नहीं जिसे नुक़सान पहुँच सके, वहाँ कोई जोखिम नहीं।» →
   **native**: the Hindi disaster-management triad *संकट / सुभेद्यता / जोखिम*.
5. **Grade 9, climate** — the IPCC likelihood table in its Hindi calibrated
   words: *अत्यंत संभावित* 95 से 100, *जितना संभावित उतना ही असंभावित* 33 से
   66 → **native and exact**.

No passage reads as machine translation: the edition was drafted directly in
Hindi against the English twin, line range by line range.

## Canon findings (reported, not fixed)

1. `parts/grade-7/01-plate-tectonics.tex`: a proposition states the
   earthquake map shows magnitude ≥ 6, while the map legend says ≥ 6.5
   (suspected inconsistency; reproduced as written).
2. `parts/grade-8/03-fronts-and-weather-maps.tex`, exercise 5: "a grey veil of
   altostratus", while the course text calls the thin veil ahead of the warm
   front cirrostratus (minor; reproduced).
3. `parts/grade-9/02-natural-risks.tex`: a caption credits "R.~Wright and
   T.~Pierson" while `frontmatter/image-credits.tex` has "T.~L. Wright and
   T.~C. Pierson" (suspected initial mismatch; the Hindi caption gives the
   names without initials).

## Tool and gate findings

* `tools/check_hindi_prose.py` transliteration tier flags genuine Hindi:
  *आर* (in *आर-पार*, "across") as "are", *टू* (in *बेल टूट*) as "to", and
  bare *द* as "the" — worked around by rewording, which a native reader would
  not need.
* Earlier in the run (all fixed by the coordinator or by an allow-list entry):
  the `\ang` placeholder bug (twice), "(द)" inside parentheses, the `\tikzset`
  blind spot (now a reducer), `\pgfmathparse` int, figure-local macro keys.
* Allow-list entries appended to `tools/check_hindi_prose.py` (each commented):
  `SPLIT_MACROS.update({"gfivechart": (1, 1), "gsixrock": (1, 1)})`
  (figure-local macros whose last argument is a visible label);
  `TECHNICAL_MACROS["pgfplotstableread"] = 1`; `ALLOWED_UNITS |= {"bar"}`;
  `ALLOWED_UNITS |= {"hpa"}`; `TECHNICAL_MACROS["tikzset"] = 1` (superseded
  by the coordinator's reducer).

## Coordinator addendum (2026-10-25)

Re-verified by the coordinator:
- a forced build: 313 pp, 0 errors / 0 undefined / 0 overfull, nullfont 6,633, `.fls` 64 = 64;
- `check_translation.sh` 9/9 PASSED under the final hi gate; linker dry run 0;
- no English target missing;
- the draw census differs from English only in figdata label-table rewrites;
- the air-mass and cold-front page (p. 186) read at 110 dpi.

Canon reports:
- **Fixed:** the g9/02 caption, now "T.~L.~Wright and T.~C.~Pierson". This edition names them without initials, so nothing changes here.
- **Not defects:** the g7/01 map deliberately plots M ≥ 6.5 (its legend is right; the 7,031 count is M ≥ 6), and "grey veil of altostratus" matches the course text.

The gate now also exempts the spaced form "आर पार". The score is unchanged.

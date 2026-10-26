# Translation score — Earth and Space Sciences Book 2 · Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 2 (High School, Grades 10–12) |
| **Language** | Hindi (`hi`) |
| **Quality bar** | **native higher-secondary textbook prose**: a Hindi course for classes 10–12 in geology, ocean and atmosphere, and climate, in the established Hindi technical vocabulary of these sciences. It is no longer the तुम voice of Book 1. English is the source of truth for content, structure, labels, numbers, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content); `hindi_style_card.md`; this series' Hindi Book 1 (`parts/grade-{1..9}/hi/`, its score file and `book1_hi.py`) for every convention and every term it owns; the shipped Hindi editions of Biology Book 2 and Chemistry Books 1–2 for the आप / -इए register of the upper grades and for shared chemical and biological vocabulary; the Hindi physics editions for shared physical vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-26 |
| **Scope of this pass** | Full first translation, written directly at native register with no machine draft: 28 chapters and their 28 solution twins, **56 files**. Every file was written through `tools/id_apply.py` from line-range patches kept in the agent's private directory. Also in scope: `frontmatter/image-credits-book2.hi.tex` (frame and descriptions translated; every credit, author, institution, dataset and licence kept exactly, in Latin script); a curated `tools/term_config/book2_hi.py`; the defined-term link layer; Hindi index keys; the overfull sweep; and this score. The preface and the entry file's `\bookline` / `\author` were already in Hindi and were not touched |

## Verdict in one line

A Hindi Book 2 that reads as one Hindi higher-secondary course in the Earth
sciences. It continues Book 1's conventions (the danda, ASCII digits, the
compass letters उ / पू / द / प, the IPCC's calibrated likelihood words, Latin
names in the credits) and moves to the textbook register of the upper grades:
आप, with -इए / -कीजिए exercise stems. Every structural and prose gate is green
over the three years, and the final forced build has
**0 errors / 0 undefined / 0 overfull** over 345 pages.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 56 files against their 56 twins: **420 `exercise`**, **28 `problem`**, **448 `\begin{solution}`**, **205 `omfigure`**, **141 `tikzpicture`**, **104 `axis`**, **100 raster includes**, **371 `\emph`**, **219 `\index`**, **132 `\cref`**, **764 `\label`**, **752 `\item`**, **658 `\node`**, **3,685 `\qty`**, **446 `\num`**, **141 `\ce`**, **561 `% ledger:`** comments, **74 `\foreach`**, **17 legends**. Per environment: **141 `definition`, 58 `proposition`, 34 `method`, 43 `example`, 14 `remark`, 28 `recall`, 1 `inthefield`, 1 `inthelab`, 12 `history`, 5 `dated`, 2 `safety`**. All are equal to English. Math spans keep the English order; display math is byte-identical except the contents of `\text{}`. The `\emph`/`\index` adjacency signature matches file by file. The coordinator's drawing census (`drawcensus.py hi`) reports 4 files, all false positives: the English words *circle* and *arc* inside node labels (*each point moves along a small circle*, *volcanic arc*, *back-arc*, an inset label in g12/07) were translated. The drawing commands themselves are identical |
| Terminology | **96** | One Hindi glossary held across three years, consistent with Book 1 wherever Book 1 owns the term. The vocabulary, by subject: <br>• **Geodesy:** *संदर्भ दीर्घवृत्तज, चपटापन, भूगणित, त्रिभुजन*. <br>• **Energy budget:** *साम्य तापमान, एल्बिडो, ऊर्जा बजट, गुप्त / संवेद्य ऊष्मा*. <br>• **Air and clouds:** *सापेक्ष आर्द्रता, ओसांक, संतृप्त / शुष्क ह्रास दर, संघनन तल, स्थिर / अस्थिर वायु*. <br>• **Storms:** *तड़ित-झंझा, तड़ित, बवंडर, उष्णकटिबंधीय चक्रवात, आँख, आँख की दीवार, तूफ़ानी महोर्मि, सैफ़िर--सिम्पसन पैमाना*. <br>• **Ocean:** *मिश्रित परत, ताप- / लवण- / घनत्व-प्रवणता परत, गहन महासागर, उत्प्रवाह*. <br>• **Soils:** *सैप्रोलाइट, लैटेराइट, जलअपघटन, मृदा*. <br>• **Rivers and water:** *अपवाह द्रोणी, जल-विभाजक, विसर्जन, आधार-प्रवाह, जलालेख, पुनरावृत्ति काल*; *भंडार, अभिवाह, निवास काल*. <br>• **Magnetism and seismology:** *अवशिष्ट चुंबकत्व, चुंबकीय उत्क्रमण, समुद्री तल प्रसरण*; *P / S तरंगें, शीर्ष तरंग, यात्रा-काल वक्र, मोहो, छाया क्षेत्र*. <br>• **Lithosphere and subduction:** *समस्थिति, क्षतिपूर्ति गहराई, स्थलमंडल, दुर्बलतामंडल, भूतापीय वक्र*; *स्लैब, स्लैब-खिंचाव, कटक-धक्का, एक्लोजाइट, नीलशिस्ट*. <br>• **Minerals and igneous rocks:** *विदलन, विभंग, पतली काट*; *ज्वालामुखीय / पातालीय चट्टान, मैफ़िक / फ़ेल्सिक / मध्यवर्ती, दीर्घक्रिस्टल, पोर्फ़िरी, डाइक, सिल, प्लूटॉन, बैथोलिथ*. <br>• **Fossil fuels:** *स्रोत / भंडार / आवरण चट्टान, ट्रैप, तेल-खिड़की, कोयलीकरण, कोटि*. <br>• **Mountains and metamorphism:** *क्रेटन, पर्वत-मूल, नैप, प्रणोद, सीवन, ओफ़ियोलाइट*; *संपर्क / क्षेत्रीय कायांतरण, परिमंडल, पत्रण, सूचक खनिज, समश्रेणी-रेखा, बहुरूप, कायांतरी श्रेणी*. <br>• **Early Earth:** *बंद तंत्र, समकालरेखा, क्षय-स्थिरांक, पृथ्वी की आयु*; *बहिर्गैसन, आदिम वायुमंडल, मंद युवा सूर्य की समस्या, स्ट्रोमैटोलाइट, पट्टित लौह संरचना, महा ऑक्सीकरण घटना, लाल संस्तर*. <br>• **Past climates:** *जलवायु अभिलेखागार, प्रॉक्सी, बर्फ़ का कोर, फ़िर्न, हिमनदीय / अंतर्हिमनदीय काल, अंतिम हिमनदीय अधिकतम, पराग-आरेख*. <br>• **Climate change:** *विकिरणी प्रणोदन, जलवायु प्रतिपुष्टि, साम्य जलवायु संवेदनशीलता, उत्सर्जन परिदृश्य, प्रक्षेपण, आरोपण*. <br>All 219 `\index{}` keys are in Hindi. Proper names are transliterated into Devanagari in the bodies and kept in Latin in the image credits |
| Register / tone | **96** | Measured, not assumed, over course and solutions. **0** तुम. The आप register is used, with **313** -इए / -कीजिए imperatives (*कीजिए* 122, *लीजिए* 45, *जाँचिए* 19, *दीजिए* 18, *निकालिए* 13, *पढ़िए* 12, *लिखिए* 10, …). This is the higher-secondary register of the shipped Hindi Biology and Chemistry upper books (a departure from Book 1, below). History is narrated in the simple past. Observation-only wording is kept everywhere: road cuts, cliffs and quarries are seen in photographs or from a distance, and the Sun is never looked at. Climate is physical science only, with no policy wording added. *नीति-निर्माताओं के लिए सारांश* is only the title of the IPCC document cited |
| Typography | **97** | A danda ends every Hindi sentence (**5,765** dandas). The period stays inside display mathematics. ASCII digits and the decimal point follow the series' siunitx setting. Initials take the abbreviation sign ॰ (*एफ़॰*), which renders. Final sweeps found: **0** Devanagari letter followed by a Latin full stop; **0** line starting with a danda, comma or semicolon; **0** space before a danda; no non-ASCII text inside `\qty{}`, `\unit{}` or `\num{}` |
| Fidelity / accuracy | **95** | Every course paragraph, worked example, exercise and solution was translated against its twin, with the numbers recomputed while translating. All g12 solutions were recomputed (isochron, decay constants, the faint young Sun, Milankovitch periods, the forcing logarithm, ECS × forcing). A per-file number census against English finds only intended differences. Where Hindi word order had to bend to keep the math and `\qty` order frozen, the sentence was rebuilt rather than left awkward. "Millions of …" is rendered *कई मिलियन*, never *लाखों* (hundreds of thousands); *लाखों* is kept only where English says "hundreds of thousands" |
| Figures | **95** | All drawing code is byte-identical except the **10 `!draw` ranges** listed below. TikZ node text, axis labels, legends and `{\small …}` captions are localized, with compass letters *उ पू द* in tick labels. Pages checked at 130 dpi after the last build: the Sunda Shelf map, the Last Glacial Maximum / deglaciation chart, the forcing bar chart, the feedback-loop diagram, the attribution chart and the Keeling photo page. Long Hindi y-tick labels fit, and no label collides |
| Links | **96** | **2,251 `\omterm` links on 138 targets** (def 2,212, ex 23, prop 16) against English's **2,208 on 136**. Every English target is linked (**0 missing**), plus two targets English never reaches (below). The frequency and chapter-set censuses were run after the last edit. The dry run gives **links to insert: 0**, and `--check` reports that every file matches what the config generates |

## Gates

`bash tools/check_translation.sh grade-N hi` for N = 10, 11, 12:
**3 / 3 PASSED**, run after the last edit. The gate covers the structural
censuses, duplicate labels, ledger ids, the Hindi prose gate (residual
English, transliterated function words, Latin full stops, spaces in math),
orphan lines, problem numbering and the twin gate. `check_orphan_lines.py`:
0 over all six directories. `check_term_display_drift.py`: 52 targets with
two or more displays, each read; all are inflections (*P तरंग / तरंगें /
तरंगों*) or the sub-terms of a combined definition (*वलन / अपनति / अभिनति*).
During the run, one real drift was removed from the prose itself: g12/10 wrote
*ऊर्जा-बजट* where g10/03 defines *ऊर्जा बजट*.

Build (`build.sh`, latexmk `-g` forced, memory-capped, nice 19):
- `'^!'` **0**, undefined **0**, Overfull **0**;
- nullfont **3,291** (= the English baseline);
- non-backtick missing characters **0**, invalid-in-math **0**;
- **345 pages** (English 362);
- the `.fls` lists **56** Hindi chapter and solution files, = **56** on disk.

The first forced build had five overfull boxes, all `in paragraph`: g11/03
276–282, g11/07 260–262, g11/07s 34–41, g12/09s 26–31 and g12/10s 90–96. A
second build left one, in g11/07s, where a math run followed "(2)". All were
cleared by rewording before the frozen span (*यदि … लें*, *उदाहरण के लिए
ओलिवीन*, *क्वार्ट्ज़ / फ़ॉर्स्टेराइट का मोलर द्रव्यमान*, *एक मिलियन वर्षों में*,
*अवकलज है*), never by shortening.

## Conventions recorded

* **Register**: आप with -इए / -कीजिए imperatives (departure from Book 1's तुम,
  below).
* **Compass letters**: *उ, पू, द, प* in every figure and tick label
  (*95°पू*, *10°द*); in prose, the full words after an angle.
* **Large numbers**: *मिलियन* / *अरब* in every data statement (*एक मिलियन
  वर्ष*, *कई मिलियन यात्रा-काल*). Four Indian forms are kept where the Hindi
  idiom is fixed or the count is exact: *प्रति दस लाख भाग* (ppm, the
  standard Hindi expansion); the ordinals *तीस लाखवाँ प्रोफ़ाइल* and *एक
  लाखवाँ भाग*; *आठ लाख वर्ष* (the EPICA record); and *कई लाख वर्ष* /
  *लाखों वर्ष* where English says "several hundred thousand" / "hundreds
  of thousands".
* **IPCC calibrated language** as in Book 1 g9: *लगभग निश्चित, अत्यंत
  संभावित, बहुत संभावित, संभावित, जितना संभावित उतना ही असंभावित, असंभावित,
  बहुत असंभावित*; confidence *बहुत निम्न … बहुत उच्च विश्वास*.
* **Time**: *Ma* / *ka* kept as unit symbols; *प्रति वर्ष*; cross-references
  to Book 1 as *(पुस्तक 1, कक्षा N)*; *इयॉन* for eon. *महाकल्प* / *कल्प*
  keep Book 1's era / period; *क्वाटरनरी कल्प* as Book 1.
* **Headers**: *अभ्यास*; *सप्ताहांत समस्या --- …*, parts *भाग I --- …*;
  solutions *अध्याय \ref{…} --- शीर्षक*.
* **Figure phrases**: *फ़ोटो: X (licence)*, *एआई-जनित चित्रण*, *X और अन्य
  (year)*.
* **Image credits**: `\chapter*{चित्रों का श्रेय}` and the Book 1 hi list
  setting (`\small`, `\emergencystretch{2em}`). There are 58 items as
  *अध्याय~N (Hindi chapter title): …*, with every name, institution, work,
  dataset and licence in Latin script. The licence list and the Latin names
  were verified identical to English.

## Departures from Book 1 conventions (with reasons)

1. **आप / -इए instead of तुम / -ओ.** Book 1 used तुम for a grades 1–9
   reader. Hindi textbooks for classes 10–12, and the shipped Hindi Biology
   Book 2 and Chemistry Book 2, address the reader as आप.
2. ***मृदा* for soil** (75 uses) where Book 1 wrote *मिट्टी*. Book 2 owns the
   soil-formation chapter, which defines soil as a scientific object, and
   *मृदा* is the term of Hindi soil science. *मिट्टी* stays where English
   means clay or dirt (*चिकनी मिट्टी*, *लाल मिट्टी*, an earth bank,
   *नंगी मिट्टी* in the albedo list).
3. ***तत्त्व*** (the standard tatsama spelling, as in the Hindi chemistry
   editions) where Book 1 wrote *तत्व* 9 times.
4. ***श्रेणी*** for the metamorphic grade and *समश्रेणी-रेखा* for the
   isograd. These are new Book 2 terms with no Book 1 owner.
5. **Large numbers**: no *लाख / करोड़* counting arithmetic. Book 1 used it
   for young readers; at this level every statement is a data statement, and
   Book 1's own rule puts those in *मिलियन / अरब*.

## Link layer

`tools/term_config/book2_hi.py` was curated from this edition's own `--terms`
harvest (234 terms), an inflection scan of the Hindi corpus, and the frequency
and chapter-set censuses against English, with a context read of every flagged
word. It was never translated from `book2_en.py` or `book1_hi.py`, and its
docstring records each case.

* **STOP**:
  - *आँख* (the naked eye) and *अभिवाह* (energy fluxes), as English STOPs
    eye / flux;
  - *भंडार* (also an oil reservoir, a store of elements, Kelvin's store of
    heat);
  - *कोटि* (also "of the same order");
  - *स्थिर / अस्थिर / संतृप्त / संतृप्ति*, as English stable / unstable /
    saturated;
  - *ज्वालामुखीय* (the bare adjective).
* **EXTRA**: English's short forms of the g12/10 terms (*प्रणोदन*,
  *प्रतिपुष्टि / प्रतिपुष्टियाँ / प्रतिपुष्टियों*, *परिदृश्य / परिदृश्यों*,
  *जलवायु संवेदनशीलता*), and *डूबती स्लैब का खिंचाव* → slab pull (English
  links "the pull of the sinking slab" in g11/06 solutions).
* **DERIVED** (≈ 65 entries): `lang_hi.py` derives nothing, so every oblique
  or plural form the bodies write is declared, each read as an inflection of
  the same word. Examples: *P तरंगें / तरंगों*, *क्षेपण क्षेत्रों*, *पट्टित लौह
  संरचनाएँ / संरचनाओं*, *बर्फ़ के कोर / कोरों*, *मूलों*, *नवीकरणीय मीठे जल*.
  Hyphenated compounds the English links as a phrase are also declared:
  *कोयला-परत*, *कोयला-खान*, *तड़ित-चमकें*, *तड़ित-नली*.
* **EXTRA_PROTECT**:
  - run-in `\paragraph{}` heads, the bold *भाग I/II/III* heads, `\pageref`
    and inline `\tikz`;
  - the invented *वार्डन पहाड़ियाँ*;
  - *मध्यवर्ती* as earthquake depth and as the intermediate emission
    scenario (exactly where English protects it);
  - *अंतिम अंतर्हिमनदीय काल* and the Glarus and McConnell thrusts, which are
    proper names;
  - *ETOPO1 उच्चावच*;
  - *मूल* as a fourth root, an original length, original layers or the basic
    response;
  - *स्तरित ज्वालामुखी* (stratovolcano, which is not ocean stratification);
  - *तप्त स्थल के सापेक्ष गति* (motion relative to a hotspot, which is not the
    relative motion of two plates; English writes "motion with respect to").

During curation, two Hindi wordings were aligned with the defined term in
the prose itself, because both were drift rather than linker problems:
- g12/08, g12/09 and g12/09s wrote *गहरा महासागर* where g10/06 defines
  *गहन महासागर*;
- g12/04s wrote *प्लूटॉन-दर-प्लूटॉन* where English links both plutons.

Target counts that differ most from English, each read:

| Term | hi | en | Why |
|---|---:|---:|---|
| *विदलन / विभंग* (cleavage; fracture) | 33 | 24 | g11/08 links the conchoidal fracture twice (the defined sense; English leaves it unlinked) |
| *अपवाह द्रोणी / जल-विभाजक* | 19 | 12 | Hindi repeats *जल-विभाजक* where English says "the divide" |
| *स्लैब* | 96 | 91 | Hindi repeats the noun where English says "it" |
| *लाल संस्तर* | 5 | 3 | an exercise and a solution name the red bed in the singular, which English's plural term misses |

All other targets are within ±2 of English: root 24 = 24 after the STOP
was replaced by protects, thermocline / deep ocean 31 = 31, energy budget
5 = 5, coal 27 vs 28.

**Targets English never reaches** (English gaps, reported):
- *def:g10:storms-and-cyclones:scale*: Hindi links *सैफ़िर--सिम्पसन पैमाने*
  once in g10/05;
- *def:g11:drift-to-spreading:anomaly*: Hindi links *चुंबकीय विसंगतियाँ*
  twice in g11/01.

English writes these as "the scale" and "anomalies", which its linker
does not reach.

## `!draw` ranges (English line numbers)

| File | Lines | What changed |
|---|---|---|
| g10/02 | 133–134 | bar chart `symbolic x coords` of planet names; the ASCII symbols are kept and Hindi `xticklabels` added |
| g10/02 | 299 | `\foreach` list of planet names |
| g10/03 | 226–229 | `\foreach` albedo list of surface names |
| g10/05 | 58 | `\foreach` thunderstorm stage titles |
| g11/08 | 153 | `\foreach` rock-name pairs |
| g11/08 | 162–169 | `\foreach` mineral names of the Bowen-style chart |
| g12/01 | 122 | `\addplot` point labels, *लगभग 70* |
| g12/05 | 272 | `\foreach` labels of the isostatic-rebound panels |
| g12/06 | 287 | `\foreach` *खाई* labels |
| g12/09 | 270–271 | `xticklabel` with *\textdegree पू*, and `yticklabels` with द / उ |

The long `yticklabels` lists of g12/10 (200–202, 396–397) needed no `!draw`,
because they are not drawing code.

## Samples (Hindi, with verdict)

1. **g10/05, storms**: «यदि आपको गरज सुनाई देती है, तो तड़ित आप तक पहुँच
   सकती है। किसी इमारत में या किसी बंद कार में जाइए और अंतिम गरज के काफ़ी देर
   बाद तक वहीं रहिए।» → **native**: the safety
   register of a Hindi textbook.
2. **g12/09, Sunda Shelf**: «बोर्नियो, सुमात्रा और जावा मलय प्रायद्वीप और
   हिंदचीन के साथ एक ही भूमि बन जाते हैं: सुंडा शेल्फ़, जो आज एक उथले
   समुद्र के नीचे है, सूखी भूमि थी।» → **native**.
3. **g12/10, feedbacks**: «यह मूल प्रतिक्रिया अंत में हमेशा जीतती है: इसीलिए
   जलवायु बिना सीमा के गरम होने के बजाय एक नए, अधिक गरम संतुलन पर टिक जाती
   है।» → **native**.
4. **g12/10, attribution**: «यह असंदिग्ध है कि मानवीय प्रभाव ने वायुमंडल,
   महासागर और स्थल को गरम किया है।» → **native and exact**: IPCC's
   "unequivocal".

No passage reads as machine translation.

## Canon findings (reported, not fixed)

1. `parts/grade-11/01-drift-to-spreading.tex` l. 613–615, exercise 15
   item 2: "After 10 million years at these rates, how far from the axis
   would floor of that age lie". "That age" reads as the 2.581 Myr boundary
   of the stem, but the solution (`solutions/01-…` l. 110–111: 225 / 271 km)
   means floor 10 Myr old. This is a wording ambiguity, translated as the
   solution means it.
2. `parts/grade-11/solutions/08-igneous-rocks.tex` l. 149–150, problem
   answer 16: "Between the two: a few years, at the long end of a lava flow,
   in the months-to-years of shallow intrusions." The sentence is hard to
   parse: the "few years" belongs to the shallow-intrusion range, not to
   lava flows. Minor; translated as meant.
3. Observation, not a defect: the g12/10 weekend problem has 19 questions
   where the other chapters have 20.

## Tool and gate findings

* No tool bug met in this run. `id_apply.py` (per-range `!draw`),
  `check_hindi_prose.py` and the linker all behaved as documented.
* `drawcensus.py` counts the English words *circle* / *arc* inside node
  labels as drawing tokens (4 false-positive files: g11/04, g11/06, g12/02,
  g12/07).
* **Allow-list**: two append-only entries in `tools/check_hindi_prose.py`
  (`ALLOWED_WORDS`, each commented "Book 2 hi", run once to confirm):
  *nnr-morvel* (the NNR-MORVEL56 plate model named in a g11/06 data credit, a
  dataset name identical to English, like PB2002) and *webmineral* (the
  webmineral.com database cited in a g11/07 table note and caption).
  *बियॉन्ड* (Beyond EPICA) and *फ़्रॉम* passed without one.

## Coordinator amendments (2026-10-26)

- g11 solutions/08 answer 16 rewritten after the English fix this edition
  reported (≈ 950 days, 2.6 years, within the intrusion range, not "between the two").
- `book2_hi.py` gains an `EXTRA_PROTECT` for the parenthesised gloss of Vine
  and Matthews's paper title (g11/01:268): a title never links, as in English.
  Links 2,251 → 2,250. The caption link at l.369 (the defined sense) stays.
- Coordinator verification: forced build 345 pp, 0/0/0, nullfont 3,291,
  `.fls` 56 = 56, gates green for grades 10–12, linker dry run 0.
- g12/02 fold-shortening chart labels (Varden label no longer clipped, 13 % label moved below-right of its point), English-canon fix after the Arabic report; mirrored by the coordinator. (The name was already Motonori here.)

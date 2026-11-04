# Translation score — One Earth and Space Sciences Book 4 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 4 (University, Year 2, `bachelor-2`) |
| **Language** | Arabic (`ar`), Modern Standard Arabic, right-to-left; Latin runs boxed with `\babelsublr` or `\mbox{\textdir TLT …}` |
| **Model** | `claude-opus-5-5` (Opus 5.5, effort high), one agent per edition: a single stint (stint 1, 2026-10-30) ran phases A–D, its context compacted automatically several times; no continuation agent |
| **Coordinator** | `claude-opus-5-5` |
| **Overall score** | **95** |
| **Ship threshold** | ≥ 95: **met**; every chapter and every solution file read in phase C |
| **Scope** | 31 chapters and their 31 solution files (62 files); term layer (`tools/term_config/book4_ar.py`); image credits (`frontmatter/image-credits-book4.ar.tex`, translated); entry file: `\bookline` and `\author` only |

## Build (forced, TeX Live 2026, wrapper `draft/b4-run/tools/build.sh`, final build `ar4-final`, 2026-10-30, after the last edit and the relink)

- `ar4-final2` (after the coordinator's MSG5 canon fixes, the last edit): latexmk rc 0, **438 pages**; errors 0; undefined 0; **overfull 0**; nullfont 0; missing characters 0 (backtick 0); invalid-in-math 0; "Discard zero height" 0.
- `.fls` lists **62** translated files = the 62 on disk.
- Header-only pages: none. A `pdftotext` scan of all 438 pages finds only p. 12 and p. 369, the two part-title pages (القسم I / القسم II، حلول التمارين), and the empty split after the last page.
- Rendered after the build: the ch. 17 slope-failure figure (المنخفض الحلقي label under the moat, clear of the slip surface), ch. 23 p. 3 and ch. 25 p. 4 (normal pages; the short ch. 23 page is the float space before the ENSO figure), and ch. 31's weekend problem: its heading now opens the fresh page with the problem (p. 357).
- The build before MSG5 (`ar4-final`) had the same numbers: 438 pp, 0/0/0.

## Gates (after the last edit)

- `tools/check_translation.sh bachelor-2 ar`: **PASSED** (Arabic prose gate, 62 files; chemistry-twin gate, 62 files).
- `tools/gates.sh bachelor-2`: **OK**.
- Linker dry run `python3 tools/link_defined_terms.py --book 4 --lang ar | grep 'links to insert'`: **0**.
- Line-edge sweeps (quote at line end, punctuation at line start incl. `، ؛ ؟`, Latin hyphen at line end, `%` at line end): clean; the only hits are TikZ `.. controls` continuation lines, the field prime `10'` of the QAPF caption (as in English) and one `%` after `\hspace` in code (as in English).
- Per chapter in phase A: prose gate, `engsweep.py` (only names, titles, credits), `numdiff.py` (only spelt ordinals, *Year 1/2/3*, spelt "1 year"/"1890s", and the label coordinates under `!draw`), `crefart.py`, one-chapter probe 0 errors / 0 overfull / 0 nullfont / 0 missing-char / 0 invalid-in-math, every figure page rendered.

## Term layer (`tools/term_config/book4_ar.py`, `AMBIG_POLICY = "drop"`)

- **Links / targets.** English: 2,019 links on 191 targets. Arabic: **1,318 links on 198 targets**. **Every English target is reached.** The seven Arabic-only targets are right-sense (read site by site): *REE* (العناصر الأرضية النادرة), *CAPE*, the Kelvin–Helmholtz time, *maturity* (انعكاسية الفيترينيت), *volumetrics* (معامل الاستخلاص), *blocking*, *open system*.
- **STOP:** التحوّل (metamorphism; also every ordinary "transformation/conversion"), الكشف (detection; also every ordinary "uncovering").
- **EXTRA:** about 62 forms (indefinite, plural and dual forms the harvest cannot reach); **EXTRA_PROTECT:** 7 patterns, each anchored `(?<!\w)`. The docstring documents every entry.
- **Census (`census.py ar`):** `\index{}` keys identical to English 0 (all translated), `\text{}` identical 4 (ch. 11 `Mg,grt`, `Fe,grt`, `Ca,grt`: mineral-site symbols, kept). FREQ/CHAPTER flags (ENSO 51 vs 4, parcel levels 17 vs 2, LCL 8 vs 2, REE 19 vs 0, peritectic, GOE, NWP, NAO, proxy, diagram, morb-oib, normalised, melt fraction) were read site by site: one Arabic word covers what English writes as a pronoun or an abbreviation (إل نينيو for "El Niño"/"it"), every target right.
- `check_term_display_drift.py`: 40 targets with two displays; all are proclitic forms (و، ب، ف، ل) or the several terms one definition owns (foreland: المولاس/الفليش/الحوض الأمامي الجبلي; klippe/window; ENSO/La Niña).
- **Under-linking** (1,318 of 2,019) is the two STOPs and the definite/indefinite split of Arabic noun phrases; a wrong sense is worse than a missing link.

## Conventions recorded

- **Register.** Course text: impersonal passive and first person plural (18 forms of نحن/نجد/نحسب/لنفترض…); no second person (0 forms of أنت/لديك/عليك). Exercise stems and method steps: masculine-singular imperative — 925 stem verbs in the course files (احسب 350, أوجد 244, قارن 82, بيّن 59, اشرح 13, قدّر 12, استنتج 9, فسّر 8, ارسم 6, …); feminine imperatives 0; politeness formulas 0.
- **Units:** English's `Ma`/`Myr`/`Gyr`/`kyr`/`yr` kept byte-identical (Books 1–3 ar); ASCII digits; Arabic punctuation `، ؛ ؟`, also between two inline math spans; no tatweel (بنسبة، بمقدار، بعامل).
- **Headings:** «التمارين» for the exercises section (normalised in 22 files, the Book 3 form); «مسألة نهاية الأسبوع --- …»; parts «الجزء الأول --- …»; solution heads `\section*{الفصل \ref{…} --- …}` (all 31 checked against the chapter titles).
- **Terms (Books 1–3 ar kept):** عدم التوافق (unconformity), الدفق (flux), القاطع/العتبة/البلوتون (dyke/sill/pluton), المعدن الدليلي, خط تساوي الدرجة, الحمم (lava), الطَّفل (shale/mudrock), غوندوانا; eras الباليوزوي/الميزوزوي/السينوزوي (17 sites of الحقب القديم/الوسيط/الحديث normalised to Book 3's form); Precambrian eons الدهر الجهنمي/الدهر السحيق/دهر الحياة الطليعية, and الطليعي القديم/الأوسط/الحديث for the Palaeo-/Meso-/Neoproterozoic.
- **Terms new in Book 4:** rift (noun) = شقّ (Book 3's الشقّ القاري), rifting = التصدّع; ridge = ظهرة (Books 1–2 ar); foreland = المقدّمة / الحوض الأمامي الجبلي; Hawaiian moat = المنخفض الحلقي (not خندق, the subduction trench); spike = المُضاف النظائري; colour index = مؤشّر اللون; pre-/inter-/syn-/post-tectonic = سابق/بيني/متزامن مع/لاحق للتكتونية; stratosphere and troposphere feminine; non-human plural subjects take feminine verbs.
- **Right-to-left.** Side-by-side minipages and `\includegraphics` pairs mirror (the first prints on the right: its caption says يمينًا); a single `tikzpicture` (also with `at=` or scope shifts), groupplots, pgfplots axes and skew-T plots do not mirror, so their "left/right/from left to right" stay as in English (checked in ch. 2, 9, 14, 21, 26, 30, 31 with `pdftotext -bbox`). Leading digits, `\qty`/`\ang` at the start or end of a node, Latin-plus-math runs (`VEI $\ge 3$`, `H/C $= 1.50$`) and Latin-only parentheses are boxed `\mbox{\textdir TLT …}`; mixed node lines and legend entries in `\foreignlanguage{arabic}{…}`; Latin in axis labels in `\babelsublr`.
- **Credits:** names transliterated in the body with the original in a TLT box; institutions, licences and paper titles copied as printed; *public domain* → ملك عام; AI images «(رسم توضيحي مولَّد بالذكاء الاصطناعي)».

## `!draw` ranges (per range; figure text that comes from data files or `\foreach` lists)

- ch02 373–377 (`\foreach` node list of the dust-to-planets strip); ch03 101–102 (`\foreach` legend of the Goldschmidt table); ch09 336 (K₂O chart: the longer Arabic «متوسط البوتاسيوم» moved from x = 76.5 to 74.8); ch11 63, 68–70 (Barrovian zone map names); ch15 415–423 (supercontinent chart: figdata names → explicit Arabic nodes, as fr); ch17 384–388 (bar-chart xticklabels; symbolic keys kept); ch18 71 (era names); ch19 71 (map titles boxed: «500 Ma» printed «Ma 005»), 468–470 (extinction chart: figdata names → five explicit nodes, as fr); ch23 100, 206–208 (monsoon and ENSO panel titles); ch24 156 (ice-volume panel titles); ch27 229–230 (feedback bar chart yticklabels); ch30 227 (events chart yticklabels).
- `--force-classes`: **not used**.

## Phase C: reading (every chapter and solution file, sentence by sentence against the English)

- 62 files read, logged "chNN read, N fixes" in `draft/b4-run/ar4/PROGRESS.md`: about 75 sentence-level fixes plus edition-wide sweeps. Among them:
  - meaning: correlator (ch. 1), quenched (ch. 5), maar/tuff rings (ch. 6), hot aftermath (ch. 18), "ocean of the Pacific" calque (ch. 23), moat ≠ trench (ch. 17), the Andes map caption (ch. 14: one `tikzpicture`, no mirroring), "freshest" samples (ch. 31);
  - grammar: gender and agreement (ch. 10, 11, 27, 30), duals (ch. 18), imperatives (ch. 27 حُلّ), doubled articles;
  - edition-wide sweeps: Latin `;`/`,` between math spans → `؛`/`،` (33 sites); breakable `\babelsublr{X $= …$}` → `\mbox{\textdir TLT …}` (41 sites); era names (17); Gondwana spelling; exercises heading (22 files); one tatweel (sol. 20) removed.
- Every solution recomputed along the printed rounded path (Python), checked three ways before any report.

## Canon (English) — reports, none edited by this agent

- **sol. 16, problem answer 17 (l. 122–123):** prints S₁ = 1445 m and 729 m, then Y = 2173 m at 100 Ma; 1445 + 729 = 2174 (2173 only from the unrounded 1444.7 + 728.6); answer 18 then compares 2173 with 2171. Reported; left as in the canon by the coordinator (a sum of rounded terms, not a double rounding).
- The coordinator's canon fixes of this run are present in the Arabic: ch. 26 PETM node at −2.9, ch. 28 *U = G(X)*, sol. 28 0.0672, sol. 31 0.36 %, sol. 23 ex. 11 (6.17e12, 5.05e21); and MSG5: ch. 18 l. 645 Marinoan `\qty{5}{Myr}` → `\qty{3}{Myr}`, sol. 18 0.933 → 0.932 (three sites), sol. 28 `\num{9.24e-3}` → `\num{9.23e-3}`, ch. 31 the unreferenced `\label{sec:b2:field-lab-methods-2:problem}` removed from the weekend-problem heading (line kept). Line counts unchanged.
- Cosmetic, not a defect of the edition: the ch. 31 station map's north arrow at (4.45, 4.75) is not visible in English either.

## Tools — reports and allow-list entries

- **Allow-list entries (append-only, commented), `tools/check_arabic_prose.py`:** a "Book 4 ar" `CREDIT_TITLE_PHRASES` block (36 exact credit/title/data-source phrases, one per credit, never a word added to `ALLOWED_WORDS`), and `MATH_SUBSCRIPTS |= {"an", "Mg,grt", "Fe,grt", "Ca,grt"}` (ch. 11 GASP displays; the gate reads `\text{}` in math). My ch. 18/20/21 subscript entries were removed again once those subscripts were translated.
- **Bug (fixed by the coordinator):** the `\index` reducer kept the makeindex encap `|see{…}` as visible text; ch. 7's see-reference is restored.
- **Traps recorded for the next Arabic agent:** `\foreignlanguage{arabic}` in the axis label of a two-axis picture placed with `at=` mirrors the panel order (use plain Arabic labels); a one-line node whose Arabic text starts with «(أ)» puts the bracket at the far end; Latin `X: digits` lists and `Rb (10 و20)` reverse; a credit in `\babelsublr` breaks across lines in a narrow column (use a TLT `\mbox`); `\raggedright`/`\raggedleft` both give flush-left in an RTL caption.

## Departures from Books 1–3 (Arabic)

- Model: Opus 5.5, one agent, one stint (Book 3 ar: Haiku, 5–9 stints).
- Ridge = ظهرة (Books 1–2 ar), where Book 3 ar wrote حيد.
- Era names follow Book 3's الباليوزوي/الميزوزوي/السينوزوي (Books 1–2 ar used الحقب القديم/الوسيط/الحديث).
- Prose `Latin $math$` runs are boxed `\mbox{\textdir TLT …}` rather than `\babelsublr`, which breaks at the spaces inside the math.

## Why 95

- For: every English target reached; every file read against English; all gates, censuses and the build clean; every figure page rendered during phase A, and the RTL left/right of every two-panel caption checked against the figure type.
- Against: under-linking (1,318 of 2,019) from two STOPs and Arabic's definite/indefinite split; index keys keep or drop the article inconsistently in a few places (e.g. `\index{معامل تركيز}` beside `\index{النسيج الأوفيتي}`); the figures were rendered chapter by chapter in phase A, not re-rendered one per page after phase C (phase C changed no figure text except ch. 17's moat label, re-rendered).

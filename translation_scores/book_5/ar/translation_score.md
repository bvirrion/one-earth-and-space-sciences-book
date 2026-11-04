# Translation score: One Earth and Space Sciences Book 5, Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 5 (University Year 3, `bachelor-3`) |
| **Language** | Arabic (`ar`), right-to-left, Modern Standard Arabic, imperative exercises; terms as in Arabic Books 1–4 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Overall score** | **89 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures sampled |
| **Canon** | *English not verified: Book 5 predates the verification pass of `book_style.md`, and solutions were not recomputed.* |
| **Tokens** | `all: 494 calls, prompt 3128K + cache read 3277K, output 10233K (thinking 8536K), list price $5.77`. Coordinator (Opus 5.5): about 22M cache read, 2.2M cache write, 200K output, from its transcript |
| **Date** | 2026-11-04 |
| **Scope** | 31 chapters + 31 solution files = 62 files |

## Verdict in one line

A complete Arabic Book 5 that reads clearly in the sample, with its figures right to left only after coordinator repairs:
most defects found were in places no gate looks.

## What the score rests on

- **Read:** the 20 passages of `sample.py --n 20 --seed 1` against English (`draft/pilot-bachelor-3-ar/sample.txt`), and the
  openings of chapters 9, 28 and 31.
- **Figures:** the 44 pages `sample.py --pages` listed, rendered and read at 130 dpi (page 12, a part title, was not read),
  plus every repaired page: 90, 91, 303, 362, 363, 405, 428. Figures on the other pages were not read. The 51 node-label
  repairs were found by script (`nodelint.py`), and only pages 90 and 303 were re-read after them.
- `pdfsweep.py`: 19 English-only word types on the final PDF, 17 from image credits, plus `pvrms` (the symbol $v_{\mathrm{rms}}$)
  and `llsvps` (an acronym). No leftover label.

## Dimension scores (judged from the sample)

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **97** | Gates green; `NUMDIFF` 2 real losses found and fixed; the rest listed below |
| Terminology | **86** | 496 defined terms by hand plus about 255 common words; one homonym (*inversion* written as *reflection*) ran across four chapters before a sweep caught it |
| Register / tone | **90** | Clear, natural prose; a few stiff constructions |
| Typography | **88** | Comma, digits and part letters by the pack; 340 detached conjunctions swept; `\sloppy` on one formula-dense solution paragraph |
| Fidelity / accuracy | **88** | One misleading phrase in 20 passages; solutions not recomputed |
| Figures | **88** | 51 node labels had their brackets or punctuation on the wrong side, now fixed; figures outside the sample unread |

## Defects found

**In the sample (20 passages, all fixed, then searched for elsewhere only where a pattern exists):**

| Where | Defect | Class |
|---|---|---|
| c05:432 | Conjunction و stranded at a line end, so it printed detached | Typography; sweep fixed 340 sites |
| c18:415 | Second conditional lacked أمّا, so the clause did not parse | Grammar |
| c21:556 | "a little less than an hour later" came out as an odd quantifier | Misleading phrase |
| c23:359 | تبدأ … فتبدأ: the verb doubled | Grammar |
| s09:95 | "steepest" lost its noun: أشدّ ما يكون | Grammar |

**In the figures and on sampled pages (all fixed):**

| Where | Defect | Count |
|---|---|---|
| ch. 31 and sol. 31 | `\ohm` printed nothing: "130 m" for 130 Ω m | 11 |
| Every chapter with hand-drawn panels | Plain-Arabic node opening with `(أ)` or ending in `:` `،`: the neutral fell on the wrong side | 51 |
| c27 | Exobase label ran under the grey box | 1 |
| s16, s25, s27 | Answer starting with a bare number: the item number and the answer swapped | 4 |
| c23:736 | Grid coordinates in prose printed reversed | 1 |

**By coordinator sweep, outside the sample (all fixed):**

- *inversion* written الانعكاس, which also means seismic reflection: 11 sites in ch. 1, 2, 8 and 31, now قلب.
- الناقلية (hydraulic transmissivity) written for electrical conductivity in ch. 31: linked to the wrong definition.
- Links of the wrong sense: *steady state* outside ch. 18 (6) and *model age* in ch. 26 (6), now masked in the term config.
- Spellings: Schlumberger, Boussinesq, Arrhenius, Proudman, Wenner, Wesenheit and Kepler were each written two ways.
- Six lines left in English, with the translation already on the line before.

**Open, outside this edition's files:**

- `styles/lang/ar.tex:54`: the colophon's "(one-course.com)." prints with its brackets scattered, in every Arabic book.
- The chapter opening and the running head print *باب*, while the prose says *الفصل*. Book 4 prints *باب* too.

## `NUMDIFF`

35 files flagged at file level, nearly all because *Year N* and *Book N* are written in words. Line by line, 8 differences:
2 real losses, fixed (s01:24 a dropped `\qty{66.8}{GPa}`, c12:532 a dropped "La/Yb 10 and 6"), and 6 accepted:

| Where | English | Arabic |
|---|---|---|
| c03:30 | grade 10 | الصف العاشر |
| c15:542 | taken as 1 | للواحد |
| c16:443 | 1970s and 1980s | عقدَي 1970 و1980 |
| c18:454 | tributary 3 | الثالث |
| s01:285 | 2 degrees | بدرجتي |
| s23:41 | 1 day | يوم واحد |

## Links

1130 links on 250 targets (English 1191 on 216); every English target is reached. Arabic has more targets because it
joins inflected forms English does not link.

## Conventions

English's Ma, Myr, Gyr, kyr and yr are kept. ASCII digits; `، ؛ ؟`; no tatweel; tanween written ـًا. Part letters
(أ)(ب)(ج)(د)(ه)(و)(ز)(ح). Missions and names with a pronounceable form are transliterated (لاندسات، كاسيني، كبلر), acronyms stay
Latin. The image credits keep long English acknowledgement wording in Latin, as in Arabic Books 1–4.
Local patch: `\DeclareSIUnit{\ohm}` at the end of ch. 31's `\chapter` line.

**Note from the overall coordinator (2026-11-04):** the local `\ohm` patch on ch. 31's `\chapter` line is gone. The fix moved to `styles/oneearth.sty`, and the final PDF was rebuilt with it: 443 pp, 0/0/0, missing characters 0.

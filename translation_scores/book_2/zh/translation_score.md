# Translation score: One Earth and Space Sciences Book 2, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 2 (grades 10–12), `one_earth_and_space_sciences_book_2_high_school_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 21 passages (seed 1, 7 per grade), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script and on contact sheets; solutions not recomputed |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 334 calls (translation, retries and repairs); glossary, infrastructure, hand fixes and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit |
| **Tokens** | Haiku: 334 calls, about $2.58 list price (`draft/pilot-grade-{10,11,12}-zh/post.log`). Weekly plan (all models): 27 % at this book's close. |
| **Scope** | 28 chapters + 28 solution files under `parts/grade-{10,11,12}/zh/` and `parts/grade-{10,11,12}/solutions/zh/` |

## Verdict

Clear high-school Chinese with the standard vocabulary (温跃层, 绝热递减率, 软流圈, 板片拉力, 斑晶, 生油窗). Some long sentences keep
the English clause order. The sample found one awkward sentence, now fixed: *the Sun is down for twelve hours* read as the Sun "falling for
twelve hours". Every section passed Haiku's checks within three passes; nothing was finished by hand.

## Build and gates

- `build/one_earth_and_space_sciences_book_2_high_school_zh.pdf`: 333 pp (English 362). XeLaTeX + xeCJK, Fandol, TeX Live 2026.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all 56
  translated files.
- `tools/check_translation.sh grade-N zh` PASSED for N = 10, 11, 12; `tools/gates.sh` green for each.
- Term links: a dry run inserts 0. 2,673 links to 140 targets (English 2,208 to 136); no English target is missed.
- 448 exercises and problems, 448 solutions; no duplicate label.
- `pdfsweep.py` against the English and French PDFs: only report and data-set titles in credits remain (*IPCC Working Group*,
  *Summary for Policymakers*, *Chronostratigraphic Chart*).
- `figcheck.py lint`: 0 label collisions. 92 figures seen on 11 contact sheets.

## Numbers

The number trace was screened file by file. The differences are millions and billions written 万 and 亿 (47 rewritten by
`baiwan.py` from *N 百万* / *N 十亿*), decades written 20 世纪 90 年代, and number words written as digits. Every unexplained one
was checked against English and found right.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Full-width `，` at the top level of a multi-line tick list | 26 | `yticklabels={总计（人为），太阳，…}`: three overfull boxes | `listcomma.py --fix` |
| `\foreach` and chart labels in English | 9 lists | planets, albedo surfaces, igneous rocks and minerals, `trench` | Translated; the planet bars keep their keys and print `xticklabels` |
| English line left after a translated paragraph | 3 | `flows to different rivers.` | Removed |
| Sibling series named in English | 5 (+2 in Book 1, 1 in biology Book 4) | `见 One Physics Book` | 物理各册, 化学各册, 生物各册 |
| *and others*, *and* in author lists | 11 | `Karplus and others (2019)` | Karplus 等（2019） |
| *Hazard* written 自然灾害 | 1 | the grade-5 recall in grade 10 | 自然危害 |
| Doubled word across a line break | 1 | 运动到 / 到 | One removed |
| Bar label in English | 1 | `[about 70]` | `[约 70]` |
| Subscripts in English | 1 | `m_{\text{air}}` | `m_{\text{空气}}` |

## Tool changes

- `tools/termlink/morphology.py`: a Chinese term written with a space (`P 波`, `S 波`, `U 形谷`) now matches with or without it. The
  P- and S-wave definition (55 English links) was unreachable before; Book 1 gained 6 links to `U 形谷`.
- `tools/check_chinese_prose.py`: titles of cited works are blanked as whole phrases (`CITED`), so common words such as *for* or *over*
  stay flagged elsewhere; Book 2's authors, data sets and ships were added to `ALLOWED_HERE`.

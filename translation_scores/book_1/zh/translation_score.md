# Translation score: One Earth and Space Sciences Book 1, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 1 (grades 1–9), `one_earth_and_space_sciences_book_1_primary_middle_school_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 21 passages (seed 1, 7 each from grades 2, 5 and 8) and three chapter openings (g3 ch. 1, g7 ch. 2, g9 ch. 5), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script and on contact sheets; solutions not recomputed |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 368 calls (translation, retries and repairs); glossary, infrastructure, hand-finished sections and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit |
| **Tokens** | Haiku: 368 calls, about $2.03 list price (`draft/pilot-grade-{1..9}-zh/post.log`). Weekly plan (all models): 26 % at this book's close. |
| **Scope** | 32 chapters + 32 solution files under `parts/grade-{1..9}/zh/` and `parts/grade-{1..9}/solutions/zh/` |

## Verdict

Plain, correct school Chinese, in the register of a mainland primary and middle-school textbook (河漫滩, 气候带, 锋面, 等高线). Some
sentences keep the English clause order. The children's names are transliterated (汤姆, 莉娜, 萨姆). Hazard and disaster were merged
into one word (自然灾害) in the first pass. They are now kept apart, in the glossary and in grades 5 and 9: 危害 / 自然危害 for
*hazard*, 灾害 / 自然灾害 for *disaster*, 风险 for *risk*.

## Build and gates

- `build/one_earth_and_space_sciences_book_1_primary_middle_school_zh.pdf`: 304 pp (English 329). XeLaTeX + xeCJK, Fandol, TeX Live
  2026. Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all 64
  translated files.
- `tools/check_translation.sh grade-N zh` PASSED for N = 1…9, the Chinese prose gate included. `tools/gates.sh grade-N` is green for
  every grade.
- Term links: a dry run inserts 0. 5,474 links to 139 targets (English 6,103 to 137); no English target is missed. (A Book 2 fix to the Chinese term pattern added 6 links to `U 形谷`.)
- 390 exercises and problems, 390 solutions; no duplicate label.
- `pdfsweep.py` against the English and French PDFs: only *IPCC*, credits (*Natural Earth*, *Dome C*, *USGS earthquake catalogue*) and
  the Latin root *clastic* remain.
- `figcheck.py lint`: 0 label collisions. 93 figures seen on 11 contact sheets.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Labels printed from figdata tables in English | 29 plot statements | ICS eons and periods, months, continents, decades | `pilot_translation/datlabels.py` with `draft/zh/datlabels-zh.txt`; label-only plots hidden (they drew a dot under each label) |
| `\foreach` label lists in English | about 20 lists | weekdays, planets, Mohs minerals, height legend (`above\\4000`) | Translated; the planets' `{\gn}` became `\ifcase` |
| Full-width `，` at the top level of a pgf list | 15 (multi-line) | `\foreach \d in {星期一，…}` | `pilot_translation/listcomma.py --fix` |
| Hazard and disaster merged | 4 files | 自然灾害 for *natural hazard* | 危害 / 灾害 split, glossary fixed |
| Millions and billions in English word order | 4 | `120 十亿` | 120 亿, 3000 万 |
| English left in titles and prose | 5 | `[Measuring on a plan]`, `\emph{The Times}`, `Sam` | 在平面图上测量, 《泰晤士报》, 萨姆 |
| Glyph missing from Fandol | 1 | 潟湖 | 泻湖 |
| One-character terms that never link | 2 | 沙, 云 | `EXTRA` for 沙子, 沙粒, 泥沙, 淤泥, 云层, 云团 |
| A pgf label with a comma unbraced | 1 | `/更圆, 更小,` | braced |

Six sections stayed rejected after three passes (grade 3 ×2, grades 4, 5, 8, 9). All six were finished by hand with `fixsec.py`. Four
were translated `\foreach` lists, which the byte-for-byte drawing census refuses on purpose: they were saved with `--accept draw` and
checked with `draft/zh/drawcheck.py`.

## Gate changes

`tools/check_chinese_prose.py` now treats the top-level commas of a `\foreach` or pgf list as code, across lines. Book 1's credit names,
fossil genera and the Latin roots the text explains (*cumulus*, *pyro*) were added to `ALLOWED_HERE`.

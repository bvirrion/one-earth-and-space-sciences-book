# Translation score: One Earth and Space Sciences Book 3, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 3 (University Year 1), `one_earth_and_space_sciences_book_3_university_year_1_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland university usage |
| **Overall score** | **88 / 100**, sampled: 7 passages (seed 1), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script and on contact sheets; solutions not recomputed |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 635 calls (translation, retries and repairs); glossary, infrastructure, hand fixes and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit |
| **Tokens** | Haiku: 635 calls, about $6.02 list price (`draft/pilot-bachelor-1-zh/post.log`). Weekly plan (all models): 30 % at this book's close. |
| **Scope** | 29 chapters + 29 solution files under `parts/bachelor-1/zh/` and `parts/bachelor-1/solutions/zh/` |

## Verdict

Clear university Chinese with the standard vocabulary (侧伏角, 倒向, 节面, 地温线, 推移质, 反沙丘, 混合增密). Some long sentences keep the
English clause order, and a few comparisons are written 比…低 N 倍 rather than …的 N 分之一. Four sections were still rejected after
three passes and were finished by hand from Haiku's own last reply (see below).

## Build and gates

- `build/one_earth_and_space_sciences_book_3_university_year_1_zh.pdf`: 423 pp (English 475). XeLaTeX + xeCJK, Fandol, TeX Live 2026.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all 58
  translated files.
- `tools/check_translation.sh bachelor-1 zh` PASSED; `tools/gates.sh bachelor-1` green.
- Term links: a dry run inserts 0. 5,759 links to 194 targets (English 4,650 to 184); no English target is missed.
- 377 exercises and problems, 377 solutions; no duplicate label.
- `pdfsweep.py` against the English and French PDFs: only acronyms and data-set names remain (*ITCZ*, *NCEP-NCAR Reanalysis*,
  *IPCC*, *World Magnetic Model*, *Deccan Traps*, *laterite* as Buchanan's coinage, *Trinidad Lake* in the credits).
- `figcheck.py lint`: 0 label collisions. 91 figures seen on 9 contact sheets.

## Sections finished by hand

| Chapter, section | Rejection | Fix |
|---|---|---|
| 4 §2, 6 §4 | `draw`: labels translated inside drawing code | Saved with `--accept draw`; `drawcheck.py` found 0 differences |
| 10 §4 | `math`: two "from 0" bounds dropped from a derivation | Restored |
| 29 §5 | one pgfplots line (`xlabels at=edge bottom`) read as English | `common.visible()` now blanks that key |
| 29 §6 | paragraphs squashed onto fewer lines; a figure and its caption left in English | Rebuilt line by line from Haiku's own Chinese |

## Numbers

The number trace was screened file by file. The differences are millions and billions written 万 and 亿, decades written 20 世纪 30
年代, and number words written as digits. Three lines lost text to a bare `%` (see below); no other number was wrong.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| English compass letter after an angle | 94 (+13 in Books 1–2) | `\ang{63.8}\,S` | 南纬 \ang{63.8} (`compass_zh.py`) |
| Bare `%` after a number: LaTeX reads a comment and drops the rest of the line | 3 (+2 in biology) | `轻 2% 和 4%。两种模型…` | `\%`; `zh_sweeps.py` now also catches a `%` before a space or at a line's end |
| `\foreach` and chart labels in English | 11 lists | rock names, fold shapes, fault types, bedforms, reef types, `time $t_1$`, month initials | Translated (months 1月…12月) |
| Figure labels drawn by `datlabels.py` | 2 | an anchor column written with spaces; an `x expr` copied literally | Ion figure restored from English (the labels are symbols); `datlabels.py` fixed |
| Sibling series named in English | 11 | `见 One Physics Book 本科一年级分册` | 物理系列本科一年级分册, 物理各册 |
| English line left after a translated sentence | 2 | `it.`, a doubled `between` clause | Removed |
| Doubled word across a line break | 3 | 由 / 由 | One removed |
| Word for a defined term | 1 | vergence as 转向 ("turn") | 倒向 |
| Long inline formulas | 4 overfull boxes | a vector triple on one line | `\allowbreak` after commas, formulas split at `=` |
| Glyph missing from Fandol | 12 | 潟湖 | 泻湖 (now in `zh_sweeps.py`) |

## Term links

`book3_zh.py` mirrors the English STOP list (稳定, 稳定性, 伸展, 流量, 通量 kept to their own chapter) and drops 环流 (any
circulation, not only a gyre) and 对比 ("compare", not a log correlation). EXTRA reaches the Gutenberg–Richter law and the reference
Earth model.

## Tool changes

- `pilot_translation/compass_zh.py` (new), `zh_sweeps.py` (`%` and 潟), `datlabels.py` (spaced `\thisrow … \as`, `x expr`),
  `common.visible()` (`xlabels at=edge`).
- `tools/check_chinese_prose.py`: Book 3's people, places, fossil names and data sets in `ALLOWED_HERE_B3`; cited titles in `CITED`.

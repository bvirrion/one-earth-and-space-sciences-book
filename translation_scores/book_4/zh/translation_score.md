# Translation score: One Earth and Space Sciences Book 4, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 4 (University Year 2), `one_earth_and_space_sciences_book_4_university_year_2_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland university usage |
| **Overall score** | **88 / 100**, sampled: 7 passages (seed 1), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script and on contact sheets; solutions not recomputed |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 538 calls (translation, retries, repairs and one redo); glossary, infrastructure, hand fixes and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit |
| **Tokens** | Haiku: 538 calls, about $5.69 list price (`draft/pilot-bachelor-2-zh/post.log`). Weekly plan (all models): 30 % at this book's close. |
| **Scope** | 31 chapters + 31 solution files under `parts/bachelor-2/zh/` and `parts/bachelor-2/solutions/zh/` |

## Verdict

Readable university Chinese with the standard mineral and petrology names (夕线石, 蓝晶石, 十字石, 石榴子石, 单变反应, 柯勒曲线).
Iapetus is 伊阿珀托斯洋 and the Rheic Ocean 瑞克洋. As in Book 3, some comparisons are written 比…低 N 倍 rather than …的 N 分之一,
and long sentences often keep the English clause order. Two sections were finished by hand.

## Build and gates

- `build/one_earth_and_space_sciences_book_4_university_year_2_zh.pdf`: 425 pp (English 484). XeLaTeX + xeCJK, Fandol, TeX Live 2026.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all 62
  translated files.
- `tools/check_translation.sh bachelor-2 zh` PASSED; `tools/gates.sh bachelor-2` green.
- Term links: `--check` matches, a dry run inserts 0. 2,852 links to 202 targets (English 2,019 to 191); no English target is missed.
- 403 exercises and problems, 403 solutions; no duplicate label.
- `pdfsweep.py` against the English and French PDFs: only acronyms, report titles and credits remain (*IPCC Sixth Assessment Report*,
  *Carbon Dioxide Capture and Storage*, *NASA, Expedition 15 crew*, the CENOGRID data set name).
- `figcheck.py lint`: 0 label collisions. 91 figures seen on 9 contact sheets.

## Sections finished by hand

| Chapter, section | Rejection | Fix |
|---|---|---|
| 4 §7 | percentages and an ε unit lost | `5\%、10\% 和 20\%`, 以 ε 单位计 |
| 31 §5 | paragraphs compressed onto fewer lines | Redone with `redo.py` (one fresh Haiku call) |

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| English compass letter after an angle | 28 | `\ang{19}~N` | 北纬 \ang{19} (`compass_zh.py`) |
| `\foreach` and chart labels in English | 7 lists | condensation stages, element affinities, eon names, metamorphic zones, ENSO states | Translated |
| Figure labels printed from figdata | 1 chart | supercontinents (Ur … Pangaea) | Explicit nodes with the prose's names (乌尔 … 泛大陆) |
| Proper or technical terms left in English | 5 | *Rheic*, *Hirnantian*, *klippen*, *spreite*, *cryochrons* | 瑞克洋, 赫南特期, removed (the plural), 蹼状, “冰冻期”（cryochron） |
| Sibling series named in English | several | `One Physics Book` | 物理与化学系列的本科…分册 |
| English line left after a translated sentence | 4 | ch. 6, 11, 13, 24 | Folded into the Chinese line |
| Doubled word across a line break | 4 | 等 / 等 | One removed |
| Variant mineral name | 2 chapters | 矽线石 | 夕线石 (the current standard name) |
| Glyph missing from Fandol | 4 | 潟湖 | 泻湖 |
| Unclear proportion | 1 | ch. 3:385, Mg and Ca/Al against the mantle | 镁的含量仅为地幔的五分之一，钙和铝的含量则为其三倍 |

## Term links

`book4_zh.py` drops 检测 (any detection) and adds EXTRA entries for 潜在强度 (potential intensity), 同位素稀释 (isotope dilution),
柯勒曲线 (Köhler curve) and 单变 (univariant), which the harvest could not reach from their Chinese displays.

## Tool changes

- `tools/check_chinese_prose.py`: Book 4's people, places, fossil names and data sets in `ALLOWED_HERE_B4`; cited titles in `CITED`.
- `pilot_translation/zh_sweeps.py`: 潟 → 泻 (found here and in Book 3).

# Translation score: One Earth and Space Sciences Book 5, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 5 (University Year 3), `one_earth_and_space_sciences_book_5_university_year_3_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland university usage |
| **Overall score** | **88 / 100**, sampled: 7 passages (seed 1), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script and on contact sheets; solutions not recomputed |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 641 calls (translation, retries, repairs and three redos); glossary, infrastructure, hand fixes and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit |
| **Tokens** | Haiku: 641 calls, about $6.16 list price (`draft/pilot-bachelor-3-zh/post.log`). Weekly plan (all models): 31 % at this book's close. |
| **Scope** | 31 chapters + 31 solution files under `parts/bachelor-3/zh/` and `parts/bachelor-3/solutions/zh/` |

## Verdict

Clear university Chinese with the standard vocabulary (斜压, 位势, 批式熔融, 分离熔融, 接地线, 体系域, 断坡/断坪, 金属丰度). The sample
reads well; the commonest weakness, as in Books 3–4, is English clause order in long sentences. Most of the book was translated by
three `run.py` jobs at once (the queue's job plus two on chapters 27–29 and 30–31; user request, 9 calls in flight).

## Build and gates

- `build/one_earth_and_space_sciences_book_5_university_year_3_zh.pdf`: 430 pp (English 477). XeLaTeX + xeCJK, Fandol, TeX Live 2026.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all 62
  translated files.
- `tools/check_translation.sh bachelor-3 zh` PASSED; `tools/gates.sh bachelor-3` green.
- Term links: `--check` matches, a dry run inserts 0. 1,814 links to 244 targets (English 1,191 to 216); no English target is missed.
- 403 exercises and problems, 403 solutions; no duplicate label.
- `pdfsweep.py` against the English and French PDFs: only names remain (*Geneva–Copenhagen* survey, *V_rms*).
- `figcheck.py lint`: 0 label collisions. 95 figures seen on 10 contact sheets.

## Sections finished by hand

| Chapter, section | Rejection | Fix |
|---|---|---|
| 4 §2 | 20 lines missing from the reply | Redone with `redo.py` (one fresh call) |
| 8 §5 | 20 lines missing, then misaligned | Redone twice; the second reply had one doubled `$\Phi$`, removed by hand (`fixsec.py`) |
| 12 §1 | a dropped `$i$` ("for each $i$") | Restored by hand |

## Numbers

The number trace was screened file by file. The differences are millions and billions written 万 and 亿, and numbers moved to the next
line. One value was lost: solution 17.3 had dropped "at 750 m"; restored.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| `baiwan.py` read "parts per million" as millions | 1 | `838 百万分率` → `8.38 亿分率` | 百万分之 \num{838}; `baiwan.py` now skips 百万分 |
| English compass letter after an angle | 20 (+2 after math) | `\ang{71.34}$\,N` | 北纬 / （北纬） |
| English line left after a translated sentence | 7 | `in the half-space.`, `are $A = …$` | Folded into the Chinese lines |
| `\foreach` labels in English | 3 lists | diffusion paths, lid regimes, Wenner/Schlumberger | Translated with the chapters' own words |
| Box titles in English | 3 | `[Inertial oscillation]` | 惯性振荡, 惯性圆, 绕射双曲线 |
| Named methods and terms left in English | 9 kinds | *Nabarro–Herring*, *Flinn* diagram, *Hessian*, *band 4*, Varden-2 | 纳巴罗–赫林, 弗林图, 黑塞矩阵, 第 4 波段, 瓦尔登-2 (series card) |
| One term written two ways | 1 | 分批熔融 (definition) against 批式熔融 (16 uses) | 批式熔融 throughout |
| Sibling series named in English | 3 | `One Physics Book 本科三年级分册` | 物理系列本科三年级分册 |
| Doubled word across a line break | 2 | 使 / 使, 在 / 在 | One removed |
| Glyph missing from the Latin math font | 2 | β⁻ | `$\beta^-$` |
| Long inline formula | 1 overfull box | a spherical-trigonometry line | Displayed |

The invented terrane of the ch. 4 problem is named 凯斯塔 (Kesta).

## Term links

`book5_zh.py` mirrors the English STOP list (视线, 稳态, 涡旋, 模式年龄) and adds EXTRA entries for the forms the harvest cannot reach:
斜压 and 正压流体 (baroclinic), 位势 (geopotential), 海岸线轨迹/岸线轨迹, 达西定律, 基底拖曳力/底部拖曳力, 闭箱模型, and 栅格/矢量
数据 and 图层 (raster and vector data).

## Tool changes

- `tools/check_chinese_prose.py`: `ALLOWED_HERE_B5` (names, missions, acronyms, data sets); cited titles in `CITED`; a `{figdata/…}` table
  path is blanked (a file name, not prose).
- `one-biology-book/draft/zh/baiwan.py`: skips 百万分 (ppm).

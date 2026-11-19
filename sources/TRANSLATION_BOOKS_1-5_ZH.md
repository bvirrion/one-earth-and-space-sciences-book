# Run file — One Earth and Space Sciences Book 1–5 in Simplified Chinese (`zh`), pilot method

Scope: Books 1–5 (15 years: grade-1 … grade-12, bachelor-1 … bachelor-3) into Simplified Chinese (mainland), by the pilot method (`../pilot_translation_instruction.md`).
Started 2026-11-18, one run with biology Books 1–5 and Earth Books 1–5 (run 2 of 2 (after biology; the usage table is kept in the biology run file)).

| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
|---|---|

Shape (user, 2026-11-18): one coordinator (the main session), no subagents, one session for both series; at most three
years (`run.py` jobs) at once and at most 9 Haiku calls in flight. **Pause rule for this run: pause and report at +25
points of the weekly plan** from the run's start (22 %, so at 47 %; points before and after a weekly reset are added).
Order: biology Books 1–5, then Earth Books 1–5.

## Usage readings (`claude -p /usage`, all models, current week)

| When | Week used |
|---|---:|
| Run start, 2026-11-18 22:03 | 22 % |
| Earth Book 1 closed, 2026-11-19 | 26 % |
| Earth Book 2 closed, 2026-11-19 | 27 % |
| Earth Book 3 closed, 2026-11-19 11:00 | 30 % |
| Earth Book 4 closed, 2026-11-19 | 30 % |
| Earth Book 5 closed, 2026-11-19 13:20 | 31 % |

## Decisions

- Time units (coordinator, before the run): Ma, Ga and ka everywhere, for dates and durations, and 年 for yr, as the French and
  Indonesian editions. Haiku copies units byte for byte; `draft/zh/units_zh.py <year>` converts them after install, then the
  gates and `common.check` are re-run.
- Glossaries: `sources/GLOSSARY_BOOK_{1..5}_ZH.md` (new lines only), `sources/GLOSSARY_OVERRIDES_ZH.md` read last (series senses
  of inherited words: *plate* 板块, not 极板; *core* 地核, not 纤芯; 145 inherited words whose sense depends on the sentence are dropped).

## Trials (2026-11-18, before the queue)

Four chapters, Haiku 5.5 at effort medium, two passes each: biology g7/04 and b1/13, Earth g8/03 and b3/01.

| Chapter | sections | call files | rejected after pass 1 | after pass 2 |
|---|---:|---:|---:|---:|
| biology g7/04 | 5 | 8 | 0 | 0 |
| biology b1/13 | 7 | 16 | 0 | 0 |
| Earth g8/03 | 5 | 18 | 1 | 1 |
| Earth b3/01 | 12 | 28 | 1 | 0 |

29 sections, 70 call files (2.4 per section), 2 rejected at pass 1 (7 %), 1 left at pass 2 (3 %). The one left (Earth g8/03, section 3,
lines 230–340) is a reply that stops at line 313: Haiku truncates a long section. It goes to `fixsec.py` with the year's other leftovers.
Fandol covers all 1,169 distinct characters used. No wrong-sense inherited term appears (极板, 纤芯, 晶胞, 布居数, 平动 and others: 0).
Weekly plan after the trials: 23 %.

## Open defects (kept on disk, cleared as fixed)

- None open. Books 1 and 2 were fixed after their close (compass letters: 4 in grade 9, 9 in grade 12; month initials in
  grade 5, two charts, now 1–12 with the axis label 月份 and the callout 图下方的数字, and grade 10) and rebuilt
  2026-11-19 11:20: 304 and 333 pp, both 0/0/0, missing character 0.

## Per-book log

## Book 1 (grades 1–9), closed 2026-11-19

Score 88, pilot tier (`translation_scores/book_1/zh/translation_score.md`). 304 pp, 0/0/0, every grade gate-green, 5,474 links to 139
targets, 368 Haiku calls (about $2.03). Six sections finished by hand.

What this book added, for Books 2–5:
- **Hazard and disaster**: `GLOSSARY_OVERRIDES_ZH.md` now pins 危害 / 自然危害 (*hazard*), 灾害 / 自然灾害 (*disaster*), 风险 (*risk*),
  危害分布图 (*hazard map*). Audit every later book for 自然灾害 standing for *hazard*.
- **Figdata labels**: `pilot_translation/datlabels.py --list` then `--map draft/zh/datlabels-zh.txt`; extend the map for new labels.
  A plot that only carried labels (`mark=none`) is now hidden (`opacity=0, forget plot`); before that it drew a dot under every label.
- **Lists**: `pilot_translation/listcomma.py --fix` after any pass that can turn `,` into `，`; the prose gate now blanks list commas
  across lines.
- **`fixsec.py save --accept draw`** for a section whose only refusal is a translated `\foreach` list, then `draft/zh/drawcheck.py`.
- **Term links**: one-character terms (沙, 云) never link; give them two-character `EXTRA` forms.
- **Fandol** lacks 潟: write 泻湖.

## Book 2 (grades 10–12), closed 2026-11-19

Score 88, pilot tier (`translation_scores/book_2/zh/translation_score.md`). 333 pp, 0/0/0, every grade gate-green, 2,673 links to 140
targets, 334 Haiku calls (about $2.58). No section needed a hand finish.

For Books 3–5:
- Run `listcomma.py --fix` before the first build: multi-line tick lists with `，` made three overfull boxes here.
- `grep 'One .* Book'` in the zh files: Haiku names sibling series in English (write 物理各册 etc.).
- Author lists: `and others` → 等, `A and B (2019)` → `A 和 B（2019）`, but not inside a cited title (the gate's `CITED`).
- Term pattern: spaced Chinese terms (`P 波`) now link; re-run `--check` for any book linked before this change.

## Book 3 (University Year 1), closed 2026-11-19

Score 88, pilot tier (`translation_scores/book_3/zh/translation_score.md`). 423 pp, 0/0/0, gate-green, 5,759 links to 194 targets
(every English target), 635 Haiku calls (about $6.02). Four sections finished by hand (ch. 4, 6, 10, 29).

For Books 4–5:
- Run `compass_zh.py --fix` on every zh file: Haiku keeps `\ang{…}\,N` (94 in this book alone).
- `grep -P '(?<!\\)\d%'` outside comments: a bare `%` deletes the rest of its line silently (`zh_sweeps.py` now catches it).
- `listscan.py` finds `\foreach` and tick lists left in English; month initials `J,F,M,…` become 1–12 (with 月份) or 1月…12月.
- After `datlabels.py --map`, grep for `axis cs:\thisrow` and `anchor=\<macro>]` in the written nodes: both broke the build here
  before `datlabels.py` was fixed.
- Link calibration: mirror the English STOP list; DROP one-word ordinary senses (环流, 对比, 检测).

## Book 4 (University Year 2), closed 2026-11-19

Score 88, pilot tier (`translation_scores/book_4/zh/translation_score.md`). 425 pp, 0/0/0, gate-green, 2,852 links to 202 targets
(every English target), 538 Haiku calls (about $5.69). Two sections finished by hand (ch. 4 §7 by hand, ch. 31 §5 by `redo.py`).

For Book 5:
- `pdfsweep.py` still finds proper and technical names Haiku leaves in English (*Rheic*, *Hirnantian*, *spreite*): translate each
  in the text, and take the word back out of `ALLOWED_HERE_B*` once it is translated.
- Supercontinent and extinction charts print their names from figdata: replace `meta=name` labels by explicit nodes.
- Month initials on tick labels: fixed in Book 3 (and Books 1–2 sources); grep `J,F,M` after install.

## Book 5 (University Year 3), closed 2026-11-19

Score 88, pilot tier (`translation_scores/book_5/zh/translation_score.md`). 430 pp, 0/0/0, gate-green, 1,814 links to 244 targets
(every English target), 641 Haiku calls (about $6.16). Three sections finished by hand (ch. 4 §2 by `redo.py`, ch. 8 §5 by two
redos and one hand fix, ch. 12 §1 by hand). The run's speed-up is described below.

- `baiwan.py` turned "838 parts per million" into 8.38 亿: it now skips 百万分. Grep `亿分\|万分率` after it in any book.
- A term can come out two ways in one chapter (分批熔融 in the definition, 批式熔融 in the prose): `linkdiff.py` shows it as a
  missed target; harmonise the text rather than add EXTRA forms.

## Book 5 speed-up (2026-11-19 11:45, user request)

At 41 of 62 files, the queue's single `run.py` (3 workers) was the only job left. Two more `run.py` jobs of 3 workers
were started by hand on chapters not yet begun (`--chapters 27 28 29`, `--chapters 30 31`; logs `run-extra-a.log`,
`run-extra-b.log`): 3 jobs and 9 calls in flight, the run's limit. The queue's job reaches those chapters last and loads
their saved sections without a call; a section still in flight when it arrives may be translated twice (a few calls at most).

## Series checks (2026-11-19 11:24, before Book 5's close)

- English linker `--check`: every file matches, Books 1–5 of both series.
- `make test` (Earth): 1,046 passed, 0 failed.
- English Book 3 rebuilt with TeX Live 2026 into `build/`: 475 pp, 0/0/0, nullfont 0, missing character 0.

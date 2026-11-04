# Book 5 (University Year 3, `bachelor-3`) into Arabic, by the pilot method

Scope: 31 chapters and 31 solution files. Finished 2026-11-04. Brief: `sources/TRANSLATION_BOOK_5.md`.
Method: `../pilot_translation_instruction.md`. Glossary: `sources/GLOSSARY_BOOK_5_AR.md`. Pack: `pilot_translation/langs/ar.*`.
This is the pilot method's first right-to-left edition.

| | |
|---|---|
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium): 494 calls, pilot method, one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Tier** | Pilot: 89/100, sampled: 20 passages, seed 1, not read in full |
| **Tokens** | `all: 494 calls, prompt 3128K + cache read 3277K, output 10233K (thinking 8536K), list price $5.77` |
| **Result** | 443 pp, 0/0/0, nullfont 0, missing characters 0, `.fls` 62/62; gates and linker check green; 1130 links on 250 targets (English 1191 on 216) |
| **Run directory** | `draft/pilot-bachelor-3-ar/` (logs, `PROGRESS.md`, `rtl.py`, `nodelint.py`, `numl.py`, `sweep.py`, `fix*.py`) |
| **Score file** | `translation_scores/book_5/ar/translation_score.md` |

## Trial chapter

Chapter 15: 13 calls, $0.15, 0 rejected. Probe 0/0/0/0; every figure page read at 130 dpi, with labels, legends, panels, shaping
and numbers all correct. The pack's wrapper rules were obeyed. **It understated the risk**: ch. 15 is figure-light and
holds no `\ohm`, no hand-drawn panel letters and no double-brace node, and those caused the later build failure and most
figure defects.

## Rejections

Files with a rejected section after each pass: 11 (13 sections), then 0. No hand repair of a rejection was needed.

## What went wrong, and what found it

| Defect | Found by |
|---|---|
| Build death at c19: `{{…\\…}}` around a node's line break | Log, as `\tikz@path@do@at@end` |
| Build death at c28: `luaotfload-harf-plug.lua` assertion, with no `!` line. Arabic letters inside `\babelsublr`, left by the coordinator's own transliteration sweep | Log tail only, "Fatal error" |
| `\ohm` lost, 11 sites | "Missing character U+000A", then a rendered page |
| 51 node labels with brackets or punctuation on the wrong side | One sampled page, then `nodelint.py` |
| 340 detached و | The sample, then a regex |
| Wrong-sense links | `census.py` `CHAPTER` lines and `sweep.py` |

## Advice for the next right-to-left edition

- Run a node lint before the first build: an Arabic node opening with `(` or ending in `: ، .` needs `\foreignlanguage`.
- Tell the model never to end a line with a lone و.
- Never sweep names into Arabic without first removing LTR wrappers around them.
- Read every `CHAPTER` line of `census.py` as a possible wrong sense.

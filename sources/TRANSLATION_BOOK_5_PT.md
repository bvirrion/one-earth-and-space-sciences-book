# Book 5 (University Year 3, `bachelor-3`) into Brazilian Portuguese, by the pilot method

Scope: 31 chapters and 31 solution files. Date: 2026-11-03. Brief: `sources/TRANSLATION_BOOK_5.md`.
Method: `../pilot_translation_instruction.md`. Glossary: `sources/GLOSSARY_BOOK_5_PT.md`. Pack: `pilot_translation/langs/pt.*`.

| | |
|---|---|
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium): 626 calls, pilot method, one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5); finishing pass `claude-sonnet-5-5` |
| **Tier** | Pilot: 90/100, sampled: 20 passages, seed 1, not read in full |
| **Tokens** | `all: 626 calls, prompt 3843K + cache read 2384K, output 7144K (thinking 5161K), list price $4.36` |
| **Result** | 504 pp, 0/0/0, nullfont 0, missing characters 0, `.fls` 62/62; gates and linker check green; 1343 links on 233 targets (English 1191 on 216) |
| **Run directory** | `draft/pilot-bachelor-3-pt/` (logs, `PROGRESS.md`, `scratch/fix*.py`) |
| **Score file** | `translation_scores/book_5/pt/translation_score.md` |

## Trial chapter

Chapter 15: good prose, a clean 8-passage sample, one section rejected three times for stopping early, cleared by a re-run. No
material pack change. The trial predicted neither the rejection load nor the asterisks: `*word*` in the pack and glossary
leaked into prose in eleven chapters and their solutions, and the trial did not show it.

## Rejections

288 sections took 626 calls. Files with a rejected section after each pass: 22, 11, 2, 0. Causes: replies stopping early with
`end_turn`, line drift (ch. 10), false "left in English" on math continuation lines and TikZ options (08:505, 20:234, 21:579,
23:113, 30:356,360), and the `\foreach` contradiction (ch. 7:141). Those false positives were accepted by a private script,
`scratch/accept.py`, with kept-English lines translated after install. The shared scripts have since been fixed for most of them.

## Hand fixes after install

`scratch/fix3.py` to `fix9.py` plus short inline edits, on `parts/` only. Classes and counts are in the score file.

## Finishing pass (2026-11-03, `claude-sonnet-5-5`)

Hand edits on `parts/` only: wind direction (7 lines in ch. 3, 19, 20); 50 definition sentences given their article; sol. 02:15 stranded *O*;
`Part II --- Subsidence.` in ch. 5; ch. 17 figure sub-captions wrapped; sol. 02 compass subscripts to O and L. Term links regenerated
(1348 links). Rebuilt 504 pp, 0/0/0, `.fls` 62/62; `check_translation.sh`, linker `--check` and `gates.sh` green.

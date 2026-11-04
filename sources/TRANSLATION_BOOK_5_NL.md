# Book 5 (University Year 3, `bachelor-3`) into Dutch, by the pilot method

Scope: 31 chapters and 31 solution files. Started and finished 2026-11-03. Brief: `sources/TRANSLATION_BOOK_5.md`.
Method: `../pilot_translation_instruction.md`. Glossary: `sources/GLOSSARY_BOOK_5_NL.md`. Pack: `pilot_translation/langs/nl.*`.

| | |
|---|---|
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium): 711 calls, pilot method, one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Tier** | Pilot: 90/100, sampled: 20 passages, seed 1, not read in full |
| **Tokens** | `all: 711 calls, prompt 4152K + cache read 3300K, output 6989K (thinking 4918K), list price $4.36` |
| **Result** | 504 pp, 0/0/0, nullfont 0, missing characters 0, `.fls` 62/62; gates and linker check green; 1295 links on 231 targets (English 1191 on 216) |
| **Run directory** | `draft/pilot-bachelor-3-nl/` (logs, `PROGRESS.md`, `fix1.py`–`fix4.py`, `fix26.py`) |

## Run

Rejected files by `run.py` pass: 25, 8, 5, 1, 1, then 0. The last was chapter 26 section 4, which kept merging two lines and a
caption; it was fixed by hand, checked with `C.check` and saved through `run.save_section`.

## Lessons for the next edition

- A reply check doesn't see comments. The model replaced text lines with duplicated `% ledger:` lines (ch. 29, 30), changed or
  dropped a ledger line (ch. 30, 31) and translated 14 comments. Only `check_translation.sh`'s chemistry twin gate caught the ledger lines.
- A bulk decimal-comma replace also changed `axis cs:12,56` in ch. 16 and killed build 1. Audit after every bulk sweep.
- A line-level number diff (`draft/pilot-bachelor-3-nl/nd.py`) showed what file-level NUMDIFF only flags.
- Dutch wrong-direction wind: *oostelijke wind* for "eastward wind" in ch. 20. Same defect as `fr`, `es`, `pt`.
- A picture-wide `font=\scriptsize` makes a node-level `font=\scriptsize` do nothing: check the repaired page, as ch. 17 needed `\tiny`.

## Score

See `translation_scores/book_5/nl/translation_score.md`.

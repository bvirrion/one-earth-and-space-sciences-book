# Book 5 (University Year 3, `bachelor-3`) into Indonesian, by the pilot method

Scope: 31 chapters and 31 solution files. Started and finished 2026-11-03. Brief: `sources/TRANSLATION_BOOK_5.md`.
Method: `../pilot_translation_instruction.md`. Glossary: `sources/GLOSSARY_BOOK_5_ID.md`. Pack: `pilot_translation/langs/id.*`, `langs/series/one-earth-and-space-sciences-book.id.md`.

| | |
|---|---|
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium): 510 calls, pilot method, one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Tier** | Pilot: 89/100, sampled: 20 passages, seed 1, not read in full |
| **Tokens** | `all: 510 calls, prompt 2929K + cache read 2653K, output 7123K (thinking 5676K), list price $4.17` |
| **Result** | 505 pp, 0/0/0, nullfont 0, missing characters 0, `.fls` 62/62; gates and linker check green; 1507 links on 241 targets (English 1191 on 216) |
| **Run directory** | `draft/pilot-bachelor-3-id/` (logs, `PROGRESS.md`, `fix1.py` to `fix6.py`, sweeps) |
| **Score file** | `translation_scores/book_5/id/translation_score.md` |

## Trial chapter

Chapter 15, read before the book: prose fine. It had one rejected section (labels), cleared in the whole-book run.

## Rejections

12 files had a rejected section after the first pass, then 1, then 0: three passes in all. No file in `rejected/` was deleted.

## Added to shared files

`tools/check_indonesian_prose.py`: one commented, append-only `ATTRIBUTION` entry for names in the credits and captions.

## New for the next Latin-script edition

- **Words doubled across a line break.** The model pads a line to keep the line count: `sejak terbentuk\nterbentuk`. 16 sites; no gate sees them,
  because gates and the earlier doubled-word sweep read one line at a time. Sweep: is the first word of a line among the last words of the one before,
  with math stripped? About 100 hits, 16 real, read in two calls.
- **A parenthesis at a line end** prints "( word", where the model dropped an article after it. Grep `\($`.
- **Capitalised `\emph` displays can lose links**, because the linker matches the lowercase form: *Faktor laju* lost `glaciology:glen`. Write "Yang disebut \emph{...}" mid-sentence.
- **`figcrop2.py` in the run directory** crops figures only, which cuts image tokens by far compared with whole pages.
- `\text{cat}` and `\text{an}` subscripts trip the Indonesian gate: write `\text{kation}`, `\text{anion}`.

## Upgrade path

A sentence-by-sentence pass over all 62 files, then re-score and update the `Model` row.

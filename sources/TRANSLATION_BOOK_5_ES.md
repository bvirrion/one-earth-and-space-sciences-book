# Book 5 (University Year 3, `bachelor-3`) into Spanish, by the pilot method

Scope: 31 chapters and 31 solution files. Started 2026-11-03. Brief: `sources/TRANSLATION_BOOK_5.md`.
Method: `../pilot_translation_instruction.md`. Glossary: `sources/GLOSSARY_BOOK_5_ES.md`. Pack: `pilot_translation/langs/es.*`.

| | |
|---|---|
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium): 585 calls, pilot method, one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5); finishing pass `claude-sonnet-5-5` |
| **Tier** | Pilot: 91/100, sampled: 20 passages, seed 1, not read in full |
| **Tokens** | `all: 585 calls, prompt 3324K + cache read 2141K, output 6752K (thinking 5140K), list price $4.06` |
| **Result** | 507 pp, 0/0/0, nullfont 0, missing characters 0, `.fls` 62/62; gates and linker check green; 1358 links on 234 targets (English 1191 on 216) |
| **Run directory** | `draft/pilot-bachelor-3-es/` (logs, `PROGRESS.md`, `fixed.py`) |
| **Score file** | `translation_scores/book_5/es/translation_score.md` |

## Trial chapter

Chapter 15: 12 calls, prompt 67K + cache 35K, output 121K (thinking 89K), $0.07; near-native; 0 rejected; the only
`NUMDIFF` was the volume references. No pack change came out of it. **The trial did not predict the rest of the book:** the
rejection load, the English figures and the unit words in `\qty` all showed up only over the 62 files.

## Rejections

288 sections took 585 calls: 288 first attempts and 297 retries, up to 11 attempts on a section, so about half the
token bill is retries. Files with a rejected section after each pass: 17, 12, 2, 0. Causes:
- `common.visible` false "left in English" on math continuation lines, `visualization depends on` and `\foreach`
  labels, where the prompt says leave them and the check refuses them (patched in `fixed.py`);
- this pack's own unit-word check against the frozen math `\num{x}~days` (moved into `convert()`, run by `post.py --units`);
- the model merging multi-line math, dropping lines or inventing `\qtyrange`/`\text` (cleared by re-runs).

`fixed.py` also carries the `sections()` fix for `\\[-1pt]`, later made in the shared `run.py`.

## Hand edits after install

All made directly in `parts/`: figure nodes in 09, 13, 27; `\foreach` labels in 07, 26; 29 axis labels; compass W → O in
02; contractions in 07, 19, 22, 24, 30, sol. 03; article in 03; doubled words in 01, 03, 14, 28; calques in 06, 13, 26;
*NASA Exoplanet Archive* in 28; *spin-up* in 19; label placement in 15, 20, 22, 27; `\sloppy` in 12, 31, sol. 04, sol. 08; unit
words in 13, sol. 13, sol. 16, 20, sol. 20, sol. 27, 30. **Don't re-run `run.py` or `install.py`: they would undo these.**

## Earlier Spanish editions

`linación` (59 uses in Spanish Books 3–4) is a spelling error for `lineación`, which this edition uses. Books 3 and 4 also
split *geotermo/geoterma* and *hundimiento/subsidencia*. Left as they are: outside this run's scope.

## Finishing pass (2026-11-03, `claude-sonnet-5-5`)

Hand edits on `parts/` only (scripts in the session scratchpad, not in the repo): wind direction in ch. 20 (2 lines) and sol. 03, 20; 54 definition
sentences given their article (`El/La/Los \emph{...}`); 4 stranded or doubled articles (ch. 6, 10, 22, 25); `Part I --- The strain.` in ch. 7;
ch. 17 figure sub-captions wrapped; sol. 02 subscripts W to O. The 30 figure pages not read in the first run were rendered at 130 dpi and read.
Term links regenerated (`--unwrap --apply`, `--apply`: 1359 links). Rebuilt 507 pp, 0/0/0, `.fls` 62/62; `check_translation.sh`, linker `--check` and
`gates.sh` green. **Still don't re-run `run.py` or `install.py`.**

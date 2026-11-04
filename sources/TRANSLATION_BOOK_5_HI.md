# Book 5 (University Year 3, `bachelor-3`) into Hindi, by the pilot method

Scope: 31 chapters and 31 solution files. Finished 2026-11-04. Brief: `sources/TRANSLATION_BOOK_5.md`.
Method: `../pilot_translation_instruction.md`. Glossary: `sources/GLOSSARY_BOOK_5_HI.md`. Pack: `pilot_translation/langs/hi.*`.

| | |
|---|---|
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium): 653 calls, pilot method, one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Tier** | Pilot: 89/100, sampled: 20 passages, seed 1, not read in full |
| **Tokens** | `all: 653 calls, prompt 4306K + cache read 3876K, output 12651K (thinking 10301K), list price $7.35` |
| **Result** | 462 pp, 0/0/0, nullfont 0, missing characters 0, `.fls` 62/62; gates and linker check green; 1346 links on 232 targets (English 1191 on 216) |
| **Run directory** | `draft/pilot-bachelor-3-hi/` (logs, `PROGRESS.md`, `sample_hi.py`, `fix*.py`) |
| **Score file** | `translation_scores/book_5/hi/translation_score.md` |

## Trial chapter

Chapter 15: 13 calls, $0.17, 0 rejected. Probe 13 pp, 0 errors, 0 overfull, 0 nullfont, 0 missing. Pages 3–7 read at 130 dpi:
shaping correct, no clipped or colliding labels, no English in figures. It taught three things: two spellings of amorphous
silica (glossary fix), credit names need gate phrases, and `sample.py` prints nothing for Devanagari. **It did not predict
the rejection load**, nor the `\ohm` loss, which only c31 shows.

## Rejections

Files with a rejected section after each pass: 17, 5, 1, 1. Most were "lines missing from the reply", cut-off replies, and
math-order swaps. The last (c19 section 3, `$\mathrm{Ro}_g \to 0$` before `$V_g$`) was hand-fixed and saved with
`run.save_section`, then assembled by `run.py` with 0 calls.

## Hand edits after install

All made directly in `parts/`, by `draft/pilot-bachelor-3-hi/fix1.py`, `fix2.py`, `fix3.py`, `fix4.py`, `fix4b.py` and patches.
Box titles and `\section` left in English; trailing English words; 68 Latin part letters; `\text` and `\foreach` labels; names;
wind wording (74 lines read, none reversed); line breaks in s04, s16; `\tabcolsep` in c13; the `\ohm` and `\emergencystretch`
lines. **Don't re-run `run.py` or `install.py`: they would undo these.**

## Gate allow-list

`tools/check_hindi_prose.py` carries an appended, commented block for this edition: units `kyr`, `myr`, `kpc`, `mag`, word
`irr`, and credit phrases.

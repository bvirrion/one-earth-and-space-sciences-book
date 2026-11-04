# Translation score: Earth and Space Sciences Book 5, French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 5 (University Year 3, `bachelor-3`) |
| **Language** | French (`fr`) |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures sampled |
| **Date** | 2026-11-03 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 630 calls; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English not verified: Book 5 predates the verification pass of `book_style.md`, and solutions were not recomputed. |
| **Tokens** | `all: 630 calls, prompt 3666K + cache read 2054K, output 7667K (thinking 5757K), list price $4.71`. Coordinator, from its transcript: about 18.3M cache read, 1.83M cache write, 152K output over about 184 tool calls, which costs far more than the translation |
| **Scope** | 31 chapters + 31 solution files, 288 sections; `frontmatter/image-credits-book5.fr.tex`; glossary `sources/GLOSSARY_BOOK_5_FR.md`; term config `tools/term_config/book5_fr.py` |

## Verdict

Near-native technical French with occasional calques, in the register of Books 1 to 4. The score is a sample's score. The
sweeps kept finding real defects late in the run, including two sense reversals in the wind vocabulary, so the unread remainder
certainly holds more. A sentence-by-sentence pass is what would lift it to the 95 tier.

## Build and gates

- `build/one_earth_and_space_sciences_book_5_university_year_3_fr.pdf`: 509 pp. Errors 0, undefined 0, overfull 0, nullfont 0,
  missing characters 0, invalid-in-math 0, zero-height 0, `.fls` 62 / 62 on disk. TeX Live 2026.
- `tools/check_translation.sh bachelor-3 fr` and `tools/gates.sh bachelor-3` pass. Linker `--check` clean.
- Links: fr 1535 on 240 targets, en 1191 on 216; every English target reached. Accepted over-frequency, right sense:
  thrust-geometry 61 against 1 (ch. 10 only), cepheid 20 against 3, cmp 13 against 0, tract, wireline, velocities, batch.
- `pdfsweep.py`: the top 150 are cognates and tokens cut at accents (`unit`, `cart`, `ment`); no real English label.

## What was read

- Text: 20 passages (seed 1) and the openings of chapters 9, 16 and 27.
- Figures and pages: all 50 pages listed by `sample.py --pages 509`, then the figures changed by hand (ch. 17, 19, 20).

## Defects found and fixed, by class

None of these was caught by a reply check or a gate.

| Class | Count | Example |
|---|---:|---|
| Punctuation space before `: ; ? !` | 77 segments | plain or no space |
| Definition opening on a bare noun | 39 | `\emph{Névé} est ...` |
| `\cref` without its article | 14 | after *d'après*, *dans*, *par*, *voir* |
| Compass W for O | 11 | ch. 2 and solutions |
| English figure labels returned as `=` | 10 | ch. 4 x5, ch. 26 x3 and one `\foreach`, ch. 31 |
| Hints removed from print, added `\index` on plain `\emph` | 7+ | |
| Article left behind before an elision, once with words lost | 5 | `La\nL'équation` (18), `Dans une\nl'épaisseur` (20), `le\nl'eau` (21), `la\nl'équation` (13), `et le\nl'écoulement` (20) |
| `grade N` as a French school class | 4 | now `année~N` |
| Figure collisions | 3 | ch. 17 rotated labels, ch. 19 frame labels twice |
| Sense reversal, easterly and eastward | 2 | ch. 21:214 stress directed the wrong way, which contradicted the negative curl; ch. 20:414 eastward as *vent d'est* |
| Doubled word, wrong word order, calque | about 12 | *sont sont*, `d'une 6.0 % fusion`, *petit liquide*, `Wicks and others`, *a core of*, VGP for PGV |

## `NUMDIFF` differences accepted

36 files at first, nearly all `Year N` written as an ordinal and numbers moved across lines. Two real losses fixed (solutions 01:24
`(\qty{66.8}{GPa})`, solutions 24:175 `\textbf{22.}`), 12 decimal commas restored to points. The final residual, 9 files, all accepted:

- ch. 1, 2, 3, 4: `grade N` → `année~N`, an artefact of the filter;
- ch. 14: axis width 0.8 → 0.76, my own overfull fix;
- ch. 27:618 *a billion years* → `1~Ga`; ch. 30:837 *half a per cent* → `\qty{0.5}{\percent}`;
- solutions 04:215 *Sixty million years* → `\qty{60}{Ma}`; solutions 08:52 *is 0* → *sont nuls*.

## Conventions

Book 4's are kept: *Ma*/*Ga*/*ka*/*an* in prose and math, compass O, `~:` `~;` `~?` `~!`, decimal point, an article before `\cref`,
`(livre~2, année~11)` for grade references, `\emph{term}\index{term}` adjacent, *vorticité* for vorticity and *tourbillon* for eddy.
"Varden Hills" and "collines de Varden" both occur, as they do in Book 4; left as found.

## Upgrade path

A sentence-by-sentence pass over all 62 files, then re-score and update the `Model` row.

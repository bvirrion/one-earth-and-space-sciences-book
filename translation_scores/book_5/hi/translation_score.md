# Translation score: One Earth and Space Sciences Book 5, Hindi (`hi`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 5 (University Year 3, `bachelor-3`) |
| **Language** | Hindi (`hi`), Devanagari, आप register with -इए/-कीजिए imperatives; terms as in Hindi Books 1–4 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Overall score** | **89 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures sampled |
| **Canon** | *English not verified: Book 5 predates the verification pass of `book_style.md`, and solutions were not recomputed.* |
| **Tokens** | `all: 653 calls, prompt 4306K + cache read 3876K, output 12651K (thinking 10301K), list price $7.35`. Coordinator (Opus 5.5): about 35.1M cache read, 3.7M cache write, 470K output, from its transcript |
| **Date** | 2026-11-04 |
| **Scope** | 31 chapters + 31 solution files = 62 files |

## Verdict in one line

A complete Hindi Book 5, structurally identical to English and clean in the log, that reads well in the sample but carries
wrong-sense word choices no gate sees: the sample's two real defects were both of that kind.

## What the score rests on

- **Read:** the 20 passages of `draft/pilot-bachelor-3-hi/sample_hi.py --n 20 --seed 1` against English (`sample.txt`),
  and the openings of chapters 17, 22, 24, 26 and 30.
- **Figures:** all 46 pages of `sample.py --pages 462` rendered and read at 130 dpi, plus pp. 377 and 454 for the ohm fix.
  Many of the 46 are exercise, solution or index pages. Figures on the other pages were not read.
- `pdfsweep.py`: 0 English-only word types on the final PDF.

## Dimension scores (judged from the sample)

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **97** | Gates green; `NUMDIFF` 2 real losses found and fixed; the rest listed below |
| Terminology | **85** | 500 defined terms by hand, 262 common words, 867 from earlier Hindi; one homonym went wrong across a whole chapter |
| Register / tone | **90** | आप imperatives held; a few stiff constructions |
| Typography | **92** | Danda, ASCII digits and (क)(ख) part letters after hand repair; 0 overfull |
| Fidelity / accuracy | **87** | One wrong sense and one non-word in 20 passages; solutions not recomputed |
| Figures | **90** | One tight label in 46 pages; no shaping defect, nothing clipped, no leftover English |

## Defects found

**In the sample (20 passages), fixed:**
- c10:724 *front* of a wedge as वाताग्र, a weather front. Traced to 8 lines in c10, 1 in s10, 4 in c23, 1 in s23, 1 in s15
  and 2 in c19. Now अग्र भाग or अग्र. Each sense-specific line in the glossary is a trap for a homonym.
- c21:434 *counter-intuitive* as प्रतिज्ञानिक, not a word. Now सहज बोध के विपरीत.

**In the sample, left as they are (small):** c05:73, "जिसकी आयु" attaches loosely. `पुरा-दाबमापी` for *palaeopiezometer* is
this glossary's own choice; Hindi has no settled term and दाबमापी suggests a pressure gauge.

**In openings and figure pages, fixed:** c26 opening adjective agreement (चमकीली उच्चभूमियाँ); s31.7 a doubled numeral;
*Proudman* spelled three ways (now प्राउडमैन, which also gave s19 a link it had lost); c19 the label बाधा touching a sub-caption;
`\mathrm{Earth}`, `base`, `model`, `skin` and `dark` left in English in math (now `\text` in Hindi). Abbreviated subscripts
(`org`, `esc`, `eff`, `carb`, `cal`, `vis`, `sat`, `max`, `dif`, `dis`, `red`, `ecl`, `exo`, `diag`) stay in Latin.

**Found by the build, not by any gate on the text:** every `\ohm` printed nothing (11 sites in c31 and s31, so
"\qty{130}{\ohm\metre}" read "130 m"). `styles/oneearth.sty:327` declares `\ensuremath{\Omega}`; inside siunitx's `\mathrm`
the `\mathalpha` glyph takes the family of the Devanagari face. Fixed on c31's `\chapter` line with a fixed-family `\mathchar`.

The rate says more wrong-sense words remain in the unread text: about one per ten passages.

## Accepted `NUMDIFF` differences

31 files differ. Real losses fixed: c21:796 `\qty{0.1}{Pa}`, s01:24 `(\qty{66.8}{GPa})`. Accepted:
- Book numbers 3 and 4 added where English says the Year 1 or Year 2 volume (most files, `only-hi` 3 and 4).
- "Year 2 volume" written पुस्तक 4 without the 2 (c11, c13, c25).
- degree-2 in words (c03); `0` written शून्य (c14:612).
- The same number moved to a neighbouring line (c14, c19:674, c21:427, c25).

## Accepted census notes

- `post.py` `math_spans` on c02: `\text{वर्ग-माध्य-मूल}` for `\text{rms}`, the hand edit, in 5 spans. A span diff shows it is the only difference (215 spans on both sides).
- `ENGSWEEP` in `post.py` reads the run directory, so it still lists lines already fixed in `parts/`. A direct sweep of `parts/` finds only agency and source names in credits.
- `FREQ` high: thrust-geometry 59 vs 1 (all ch. 10, right sense), si 12 vs 0, tract 20 vs 7, velocities 15 vs 7, eddy 18 vs 8,
  core-complex 10 vs 5. Homographs sent through `STOP` are listed in `tools/term_config/book5_hi.py`.

## Conventions kept

Western digits; compass letters in `styles/lang/hi.tex` (S-plane at c07:416 and nitrogen at c30:189 correctly stay Latin);
Ma/Myr/Gyr/yr kept; `\cref` prints its own noun, with the postposition after; names transliterated except in credits; credits
as Books 3–4 write them. `\setlength{\emergencystretch}{3em}` sits on c01's `\chapter` line, since `styles/` cannot be edited here.

**Note from the overall coordinator (2026-11-04):** the local `\ohm` patch on ch. 31's `\chapter` line is gone. The fix moved to `styles/oneearth.sty`, and the final PDF was rebuilt with it: 462 pp, 0/0/0, missing characters 0.

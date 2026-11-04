# Translation score — Earth and Space Sciences Book 4 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 4 (University Year 2, `bachelor-2`) |
| **Language** | Brazilian Portuguese (`pt`): *você* in exercise stems, *se*-forms in the course text, Brazilian spelling |
| **Scope** | 31 chapters + 31 solution files = 62 files, written through `tools/id_apply.py` as line-range patches against the English twin (the patches in the run scratchpad `draft/b4-run/pt4/p/` are authoritative; no `.tex` was hand-edited) |
| **Model** | `claude-opus-5-5` (Opus 5.5, effort high), one agent per edition, a single stint (phases A–D in one run, with automatic context compaction); coordinator `claude-opus-5-5` |
| **Overall score** | **96 / 100** |
| **Ship status** | Meets the threshold of 95. Every chapter and every solution file was read sentence by sentence against the English (phase C); mechanical gates pass; every English target is reached |

## Build (forced, `pt-2`, TeX Live 2026)

Final forced build `pt-4` (TeX Live 2026, `draft/b4-run/tools/build.sh`, scratchpad), after the last edit:
**504 pages; 0 errors, 0 undefined references, 0 overfull boxes**; nullfont 0; missing characters 0
(backtick 0); invalid-in-math 0; "Discard zero height" 0; `.fls` lists 62 translated files = 62 on disk.
English for comparison: 484 pp; French 509 pp.

## What was verified (after the last edit)

- `bash tools/check_translation.sh bachelor-2 pt`: **PASSED**. Latin-prose gate: no multi-word
  findings; the one-word tier is advisory only (cognates and names).
- `bash tools/gates.sh bachelor-2`: OK.
- Term layer: `--unwrap --apply`, then `--apply` (2,224 links inserted across 61 files; def 2,200,
  prop 24), then the dry run: `links to insert: 0 across 0 files`.
- Links: **pt 2,224 / 194 targets; English 2,019 / 191.** Every English target is reached. The
  three pt-only targets are `def:b2:geological-hazards:tsunami`,
  `def:b2:magmatic-differentiation:open` and `def:b2:magmatic-series:saturation` (English
  never writes those displays outside their definitions; pt does).
- `census.py pt`: index keys identical 13 and text identical 20, all accounted for: math
  `\text{parcel}`, `\text{const}`, `\text{grt}`, `\text{water}`, `\text{grain}` are frozen by
  the math census; index keys are proper names and symbols.
- `engsweep.py pt`: 4 lines, all credit or title strings copied by rule (*Volcanoes of the World*,
  *Principles of Geology*, *U.S. Army Corps of Engineers* twice).
- `numdiff.py pt`: the only-English tokens are *1*, *2*, *3* where pt spells out "the first-year
  volume", "the physics second-year volume" and the like; the only-pt tokens in ch15 and ch19 are
  the explicit nodes that replace the figdata label tables (supercontinents, extinctions).
- `ident.py` (pt lines identical to English that carry words): after filtering code, only
  sol09:152 was English; it was an uncovered line and is now translated.
- Solution arithmetic: every exercise and every weekend problem of all 31 solution files was
  recomputed during phase A (Phi lookups by scipy).

## Register counts (exercise and problem environments)

Counted with a script over the seven verbs *calcular, determinar, mostrar, explicar, comparar,
estimar, encontrar*:

| edition | *você* imperative (*Calcule*) | infinitive (*Calcular*) | *tu* imperative | "você" |
|---|---:|---:|---:|---:|
| this edition (`bachelor-2/pt`) | 805 | 0 | 0 | 17 |
| Earth and Space Book 3 pt (`bachelor-1/pt`) | 699 | 0 | 0 | 7 |
| physics University Year 2 pt | 331 | 0 | 0 | 3 |
| biology University Year 2 pt | 390 | 0 | 0 | 2 |
| chemistry University Year 2 pt | 421 | 0 | 1 | 12 |

Course text uses impersonal *se*-forms (*Calcule-se*, *Escreva-se*, *Tome-se*), as Book 3 pt.
An English jussive "Let X be/have …" in a statement becomes *Suponha-se que X …* (or *Seja(m)*
+ noun, standard math Portuguese), never a verb-first subjunctive (phase C rewrote 17 of those).

## `!draw` ranges (figdata labels and `\foreach` lists replaced by translated node text)

- 02c 373–377 (dust grains `\foreach`);
- 03c 101–102 (Goldschmidt legend `\foreach`);
- 11c 63 and 68–70 (Barrovian zone `\foreach` lists);
- 15c 416, 418–419, 422 (supercontinent labels, explicit nodes as fr);
- 19c 468–470 (extinction labels, explicit nodes as fr);
- 23c 100 (summer/winter titles) and 206 (*neutro*);
- 24c 156 (*hoje* / *um máximo glacial* titles).

No `--force-classes` was used. The TikZ `label={[...]east:...}` false positive of the `!draw`
comparison is worked around with the numeric anchor `0:` (coordinator ruling, msg1).

## Steps of phase C (reading, 2026-10-30)

Every course file and every solution file was read against the English, chapter by chapter,
and logged in PROGRESS.md (31 chapters, 39 fixes; two more in phase D). All fixes went through the patch route and
changed no number or formula. Among them:

- **Jussives.** Verb-first subjunctives in statements (*Contenha uma mistura uma fração…*,
  *Tenha o oceano atual…*, *Separe uma superfície frontal…*, *Ocupe um magma…*, *Cristalize um
  magma…*, *Suba a superfície do mar…*) → *Suponha-se que …*: ch04, 05 (two), 06, 07, 08, 16 (two),
  17, 19, 22, 23, 24 (two), 29, 31 (two).
- **The one uncovered line** (sol09:152, `\ce{K2O} 1.88, alkalis 6.36.`) translated.
- **Agreement, idiom, mood:** *teria se* for the mesoclisis *ter-se-ia* (ch21, ch30);
  *Por que ela pode* (ch25); *nenhum nos últimos 400 anos* (ch28); subjunctives in a
  hypothesis (*transportasse … tenha sido depositada*, ch29; *se relacione*, ch31); *taxa de
  aquecimento* for "heating" in W/m² (ch27); the R-factor apposition made explicit (ch29).
- Earlier chapters: *polida* (ch02), *os vales* (ch03), problem titles lower case after
  *Problema* / *---* in 24 chapters (ch04), *no interior profundo* (sol05), and one fix each in
  ch10–13, ch15, ch18.

## Conventions recorded

- Decimal point in prose and in math (as Books 1–3 pt and the English canon).
- Units: English's `\Ma`/`\Myr`/`\Gyr`/`kyr` split is kept (as Book 3 pt; no conversion run).
- Compass letters N, S, L, O in figure labels (the style's strings); NW → NO.
- IPCC likelihood and confidence words as Book 2 pt: *provável*, *muito provável*, *alta / média
  / baixa confiança* (adjective first).
- *ameaça* (hazard, as Book 2 pt *ameaça natural*), *risco de desastre*, *altura máxima de
  inundação* (run-up); *jazida*, *ganga*, *teor / teor de corte / tonelagem*; *retroalimentação*
  (feedback, as Books 1–3 pt); *estufa / refrigerador* (greenhouse / icehouse); *tempo de
  decaimento* (e-folding time); *janela erosiva* (inlier); *traçador isotópico* (spike);
  *perda ao fogo*, *pastilha fundida*, *viés de massa*.
- Loanwords kept as terms: *slump*, *nappe*, *klippe*, *guyot*, *backstripping*, *underplating*
  (italic). Acronyms kept: PGA, GMPE, PSHA, ERF, ECS, TCR, TCRE, SSP, CAPE, CIN, VEI, STOIIP,
  LILE, HFSE, MORB, OIB; pt acronyms NCL, NCE, NE, NCN (lifting, free-convection, equilibrium and
  condensation levels).
- Math subscripts: `\text{NCL}`, `\text{orv}`, `\text{defasagem}` translated where the
  census allows; `\text{grain}`, `\text{water}`, `\text{yr}`, `\text{parcel}` stay frozen.
- *vezes* after a number above one, *vez* at one or below.
- Canon `\index` keys broken across two lines are kept on one line in pt (coordinator ruling).

## Allow-list entry (append-only, commented)

`tools/check_latin_prose.py`, `ALLOWED_BY_LANG["pt"]`: *daito, jima* (atoll boreholes as tick
labels), *via* (a credit copied exactly; also Portuguese), *atm, lith, chal, sid, none* (the
Goldschmidt `\foreach` style keys), the eleven `ics<Period>` colour names (code), *grt* (the
IUGS garnet subscript, frozen by the math census), *molar* (the Portuguese adjective in "A/CNK
(molar)").

## Canon reports

1. **ch26 line 533, PETM figure** (type c): the *warmer* node was clipped below the reversed
   axis and invisible in every edition. **Confirmed and fixed by the coordinator** (msg3:
   `axis cs:55.52,-2.9`); mirrored.
2. **sol31 line 123, problem answer 18** (type b, a true double rounding): unrounded
   0.11853/0.1194 − 1 = −0.7286 %, over two mass units 0.364 % → 0.36; the printed 0.37 came from
   halving the rounded 0.73. **Confirmed and fixed** (msg3); mirrored.
3. msg3 also brought nl's ch28:493 (Weibull proof, `U = G(X)`, *decreasing*) and es's sol28
   104–105 (0.0673 → 0.0672); both mirrored.
4. Minor, style only (builds fine): three unit-less `\qty[text-series-to-math=true]{N}{}` in bold
   final answers, sol01:162 (624), sol05:197 (67), sol26:125 (137). `\num[…]{N}` would match the
   fr pilot's `\qty{0.311}{}` → `\num{0.311}`. pt mirrors English.

## Open items

1. Residual stylistic defects are possible. The phase-C read found about one idiom, agreement or
   mood fix per chapter, none touching meaning, a number or an English leak; a second reader would
   likely find a few more of the same kind.
2. The jussive sweep covered every English "Let …"; *Seja(m)* + noun is kept where it reads as
   standard mathematical Portuguese (*Seja $P_k(t)$ a probabilidade…*).

## Rendered pages (phase D)

Rendered at 110–130 dpi from the final PDFs and checked label by label: ch02 dust-to-planets
(p. 21), ch03 Goldschmidt table (p. 33), ch11 Barrovian zones (p. 139), ch15 supercontinents
(p. 199), ch19 sea level with the ICS period bar (p. 247) and extinctions (p. 251), ch23 monsoon
(p. 300) and ENSO (p. 302), ch24 ice-volume effect (p. 313), ch26 PETM (p. 344, the *mais quente*
label now visible after the canon fix). One collision found and fixed: the ch03 legend
*nenhum isótopo estável* ran into the B cell, now `\shortstack[l]{sem isótopo\\estável}`.
`pdfsweep.py` (en/fr/pt PDFs): 183 word types, all Portuguese cognates, fragments split at accents,
names or glossed loanwords; it led to one fix (ch17 problem, *Quantas Petrels* → *Quantas ilhas
como Petrel seriam necessárias*).

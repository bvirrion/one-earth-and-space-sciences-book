# Translation score — Earth and Space Sciences Book 3 · Brazilian Portuguese (`pt`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 3 (University Year 1) |
| **Language** | Brazilian Portuguese (`pt`) |
| **Scope** | 29 chapters + 29 solution files = 58 files, written through `tools/id_apply.py` as line-range patches against the English twin |
| **Model** | claude-haiku-5-5, effort high; coordinator claude-opus-5-5 |
| **Overall score** | **95 / 100** (rescored 2026-10-27, after the native pass of every course chapter and of solutions 01–29) — meets the ship threshold of 95 |
| **Ship status** | Meets the threshold. Mechanical gates pass, every English leak found is fixed, and the course text and every solution have had a native read; residual items are listed under open items |

## Build (forced, `pt-13`)

Final build `pt-13`: rc 0, 492 pages, 0 errors, 0 undefined, 0 overfull, nullfont 0,
missing-character 0, invalid-in-math 0, zero-height 0, fls 58 (= 58 files on disk).
Built after the last edit and after the term-layer relink (dry run 0).

## What was verified

- `bash tools/check_translation.sh bachelor-1 pt`: **PASSED** (run after the last edit and the relink).
  Latin-prose gate: no multi-word findings; one-word tier advisory only (node labels and
  captions: *horizontal, base, total, magnitude, Coriolis, Hadley, Ferrel, Recife,
  Louisville, Kamchatka, Hokkaido, Labrador, Kuroshio, till, Mississippi, Nile*, all
  Portuguese words or proper names).
- `python3 coord/engsweep.py pt`: no output.
- Term layer, after the last edit: `tools/link_defined_terms.py --book 3 --lang pt --unwrap --apply`
  (3,753 links removed), then `--apply` (4,629 links inserted across 58 files; the count was
  4,630 before this stint, one fewer after the wording changes), then the dry run:
  `links to insert: 0 across 0 files`. 184 English targets plus the accepted pt-only target *parcel*.
- PDF text sweep of `pt-11` (and of `pt-12`): English words in prose, figure labels and
  table headers were searched; the only English left is in bibliographic titles and credits
  (kept exactly, as the rules require) and in place names (*Basin and Range*, *Terceira*).
- Renders at 110 dpi of `pt-12`: the ch23 Athy table (p. 297), the ch10 problem table
  (p. 119 for the plúton table, p. 113 for the intercept table), the ch17 chevron-fold
  caption (p. 214), the ch05 structure-contour figure (p. 54), the ch29 Stommel figure
  (p. 387), two `\foreach` figures (the ch07 silicate tetrahedron, p. 71; the ch19 ionic
  potential diagram, p. 242) and two dense pgfplots charts (the ch08 Michel-Lévy chart,
  p. 87; the ch20 Hjulström diagram, p. 258). No collisions, clipped labels or overflow.
- Every solution number matches the English canon (checked in the earlier pass; this stint
  changed no number and no formula).

## Steps of the closing pass (2026-10-27)

1. **Wrong-sense links.** 54 links removed through context-specific `EXTRA_PROTECT`
   patterns (*direção* used for vibration, refraction, wind, plate motion, pressure, traction
   and shear; *rumo* as toward or trail; the chronostratigraphic *sistema* as climate system
   or gyre; *extensão* as spatial extent). Strike uses in transform faults, rifts and ch04–06
   stay linked. *direção de onde* (wind source) and *ambiente de deposição* (not facies) are
   protected; *formação de água profunda* is unlinked in solution 29 only.
2. **Drift check.** All targets with two or more displays were compared with the English
   display sets; one plural typo (*magnitudes aparentes*) fixed.
3. **Native read, course text of every chapter.** ch01–29 were read in full (prose,
   definitions, captions, figure labels and exercise stems), chapter by chapter, and logged
   in PROGRESS.md. Fixes made in the earlier stint (about forty, by chapter):
   - ch01: duplicated *Parte IV* header line removed.
   - ch02: *óptica adaptativa* (lower case); the Poisson sentence rewritten; *admitida* → *recordada*
     (Wien); *janelas fechadas* → *bandas opacas*; *Quanto mais curta* → *Quantas vezes mais curta*.
   - ch03: *admitida* → *recordada* (Stefan–Boltzmann); *tamanho do aquecimento* → *magnitude*.
   - ch04: *dobragem* → *dobramento* (pt-BR, twice); solution 04 item 9 English sentence
     translated, *(rounded)* → *(arredondado)*.
   - ch05: stray English line *with structure contours.* removed; *mergulho de mergulho* reworded.
   - ch06: *para sempre que aparecem* (false friend, "forever") reworded.
   - ch07: *quimberlito* → *kimberlito*.
   - ch08: one exercise phrase reworded.
   - ch09: *(a lembrança, com …)* → *(lembrando que …)*; *admitido a partir dos livros* →
     *que os livros de física demonstram*; *se pensa que ajuda* → *acredita-se que … ajude*;
     *1.9 vez* → *vezes* after a decimal above one.
   - ch10: table header *pluton* → *plúton*.
   - ch11: *fio de prumo de o ângulo* → *pelo ângulo*.
   - ch12: *rift da Terceira* (common noun) → *rifte da Terceira*.
   - ch14: *Os Moho* → *Os Mohos*.
   - ch15: *GPL* → *LIP* (the chapter uses LIP throughout).
   - ch16: *no olivina* → *na olivina*; one exercise stem rephrased.
   - ch17: *North Cornwall* in the caption → *Cornualha do Norte*.
   - ch18: *10^1.5 vez* → *vezes* (plural after a number above one).
   - ch19: one method sentence rephrased.
   - ch21: a sentence fragment (*a jusante, muito mais devagar…*) merged into the sentence before
     it; *prova de* (exam sense) → *demonstração de*.
   - ch23: table header *lithologia* → *litologia* (English leak).
   - ch25: *entre dos fechamentos* → *entre os fechamentos*.
   - ch29: decimal commas in prose → points (1.5; 12.3, twice; 34.15; 35.00; 34.67);
     *A matriz mostrou* → *A rede de fundeios mostrou*; *fórmula de massa* → *fórmula aerodinâmica*;
     *1.5 vez mais larga* → *vezes*.
   - ch18, ch20, ch22, ch24, ch26: read in full, no change.
   - ch13: read in full, no change.
   - ch11 and ch12 each had one further phrase fixed; the rest read clean.
4. **Native read, solutions 01–24 (this stint).** Every file was read in full. Fixes went
   through the patch route (`regen.py` and `tools/id_apply.py`), and no number or formula changed:
   - sol01: read, no change.
   - sol02: read, no change.
   - sol03: *cujas água, metano e amônia* → *cujos gelos de água, metano e amônia* (agreement);
     *acima de cada metro quadrado* → *sobre cada metro quadrado*; *faixa sísmica recente* →
     *faixa obtida pela sismologia recente*; *1.33 vez*, *1.9 vez* → *vezes*.
   - sol04: a comma after *mais baixo* before *500 m ao norte*; *do lado de cima do mergulho* →
     *do lado de cima do plano*.
   - sol05: *2.5 vez* → *vezes*; *direção de linha cada grau* → *direção, cada grau*;
     *levantadas até a vertical e elevadas* → *inclinadas até a vertical e soerguidas*;
     *giz trazido 200 m para baixo* → *giz rebaixado em 200 m*; *prevêem* → *preveem*
     (post-reform spelling).
   - sol06: *através dela* (calque) → *transversalmente*.
   - sol07: *ao por cento mais próximo* → *arredondado ao percentual mais próximo*; garbled
     *dá oxigênios demais poucos por cátion* → *deixa poucos oxigênios por cátion*.
   - sol08: *com peso médio de metade* → *em média, com metade da intensidade*.
   - sol09: *na descida* → *ao descer*.
   - sol10: *A última vez é* (calque) → *O último caso dá*.
   - sol11: *mais que três vezes espessa demais* → *espessa demais em mais de três vezes*.
   - sol12: *uma terça parte de volta* → *um terço de volta*; a run-on contrast rewritten with a
     semicolon; *Rift da Terceira* → *rifte da Terceira*, as in ch12.
   - sol13: read, no change.
   - sol14: *seu núcleo chega a 600 km quase tão frio quanto estava* → *seu núcleo, a 600 km de
     profundidade, continua quase tão frio quanto ao sair da fossa*.
   - sol15: read, no change.
   - sol16: read, no change.
   - sol17: read, no change.
   - sol18: *uma vez a cada décadas* → *uma vez a cada várias décadas*.
   - sol19: read, no change (the line after the `% ce-unbalanced-ok` comment mirrors the English).
   - sol20: *1.302 vez mais devagar* → *vezes*.
   - sol21: *preencheu a água desde o fundo* → *preencheu a coluna de água, desde o fundo*.
   - sol22: *onde pouco argila* → *onde pouca argila* (agreement).
   - sol23: *não mais fina em comparação* → *já não é fina em comparação*.
   - sol24: *que é encontrado desde a base* → *que ocorre desde a base*.
   - sol29 (already read earlier): *1.80 vez mais* → *vezes*.
5. **Coordinator's English leaks.** solution 04 item 9 (fixed, and the rest of that answer read,
   *(rounded)* translated); the PDF-text sweep found the *lithologia* header, *pluton*, *North
   Cornwall* and *rift da Terceira*, all fixed.
6. **ICS chart (ch24).** Era, period and event labels translated through the patch route.

## Conventions recorded

- Decimal point in prose and in math; the decimal comma is no longer used (ch29 fixed).
- A number above one takes the plural: *1.9 vezes*, *2.5 vezes*; *0.9837 vez* stays singular.
- Compass letters N, S, L (leste), O (oeste) in figure labels; *Hemisfério Norte/Sul*.
- Astronomical altitude is **altura angular**; geometric height is *altura*; topographic
  relief is **topografia**; throw is **rejeito**; heave is **afastamento horizontal**;
  strike is *direção*; trend of a geological line is *rumo*; plunge is *caimento*.
- *admitido/admitida* marks a result taken without proof (the `\admitted` macro); *recordado/recordada*
  marks a result from the earlier physics or chemistry volumes.
- *rifte*, *plúton*, *kimberlito*, *LIP*, *dobramento* (not *dobragem*); post-reform spellings
  (*preveem*, *creem*, *veem*).

## Open items

1. **Residual stylistic defects are possible.** The native read of solutions 01–24 found about
   one agreement, idiom or calque fix per file, none of them touching meaning, a number or an
   English leak. A second independent reader would likely find a few more of the same kind;
   the score is 95 on that basis, not 96.
2. The birefringence table cell in ch08 keeps its hyphenation hint `bir\-re\-frin\-gência`,
   so the term layer does not link it (one table link absent; the others stay). Coordinator
   ruling: may stay unlinked.
3. The ch09 phrase "núcleos externo e interno" is an accepted but non-standard plural
   (coordinator ruling: acceptable).
4. Canon notes, both ruled by the coordinator and not to be re-reported: ch09 PREM mass
   5.976 against 5.972 gives 0.06 % (unrounded 5.975562e24 against 5.9722e24 is 0.056 %), and
   the ch26 pressure at 11 km, 22632 Pa, is the standard-atmosphere value by definition.

## Coordinator verification (claude-opus-5-5, 2026-10-27)

Accepted at 95. Final coordinator build (TeX Live 2026, forced): 492 pp | 0 errors | 0 undefined | 0 overfull | nullfont 0 | missing-char 0 | invalid-in-math 0 | zero-height 0 | `.fls` 58. `check_translation.sh bachelor-1 pt` PASSED; linker dry run 0; every number token of the 29 solution files matches English; `\index` counts equal file by file; the English-function-word sweep of the source and the two PDF-text sweeps are clean (only *conchoidal*, correct Portuguese). Rendered and read: the ICS chart (fully Portuguese) and the mineral table. Earlier coordinator finds fixed by the agents: the ch12 table header and a stray English line in ch18 (source sweep), "The cross product is" in solutions 04 (PDF sweep).

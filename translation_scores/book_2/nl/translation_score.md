# Translation score — Earth and Space Sciences Book 2 · Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 2 (High School, Grades 10–12) |
| **Language** | Dutch (`nl`) |
| **Quality bar** | **native academic upper-secondary prose**: Earth and space sciences in the Dutch a Dutch or Flemish pupil of the last three school years reads in a geography, physics or biology course. English is the source of truth for content, structure, labels, mathematics, data and drawing code |
| **Register references** | the English canon (content); the shipped Dutch Book 1 of this series (*je*, imperative and interrogative exercise stems, *Weekendprobleem*, *Deel I --- …*, `` ``…'' `` quotes, decimal points kept, NB/ZB/OL/WL); the shipped Dutch chemistry, physics and biology editions; for the climate chapters, Book 1 g9's Dutch rendering of the IPCC calibrated vocabulary |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-10-25 |
| **Scope** | Full first translation written directly at native register through `tools/id_apply.py`: 28 chapters + 28 solution twins = **56 files**; `frontmatter/image-credits-book2.nl.tex` (translated from the English stand-in, every credit, name, dataset and licence kept); a curated `tools/term_config/book2_nl.py`; the defined-term link layer; the Dutch index keys; this score. The entry file's `\bookline` (*Boek 2: Bovenbouw -- Jaren 10 tot en met 12*) and `\author` were kept as set up in Step 0 (they mirror Book 1's *Basisschool en onderbouw*) |

## Verdict in one line

One Dutch upper-secondary course in Earth and space sciences, from *geodesie*,
*triangulatie* and the *referentie-ellipsoïde* in year 10 through *oceaanbodemspreiding*,
*lithosfeer/asthenosfeer*, *slabtrek* and the *petroleumsysteem* in year 11 to
*isochroon*, *Grote Oxidatie*, *Laatste Glaciale Maximum* and *stralingsforcering* in
year 12. Its forced build gives **374 pages, 0 errors / 0 undefined / 0 overfull,
nullfont 3291 (= English), 0 missing characters, 0 invalid-in-math**, and the `.fls`
lists 56 of the 56 edition files.

## Dimension scores

| Dimension | Score | Notes |
|---|---:|---|
| Structural fidelity | **99** | Every file was written through `id_apply.py`: math spans, `\ce`, labels, environments, images and the draw census match. Totals equal English: **219 `\index`**, **371 `\emph`**, **3686 `\qty`**, **561 `% ledger:`**, **74 `\foreach`**, **38 proofs**, **132 `\cref`**, **764 `\label`**, **28 *Weekendprobleem***. Per-file `\index` counts are identical, there are no duplicate keys, and every accented key has a sort key (`watergeinduceerd smelten@watergeïnduceerd smelten`). The `\text{}` census over course and solutions finds no untranslated word (one identical `\text{water}` is Dutch) |
| Terminology | **96** | Standard Dutch geoscience terms, chosen against Book 1 where it owns them (*principe van doorsnijding*, *Hadeïcum/Archaïcum/Proterozoïcum*, *ijskap*, *ijstijd*, *firn*). New here: *afschuiving/opschuiving/overschuiving*, *dekblad*, *anticlinaal/synclinaal*, *sutuur*, *ofioliet*, *kraton*, *metamorfose*, *isograad*, *schistositeit*, *aureool*, *vulkanische boog*, *watergeïnduceerd smelten*, *batholiet*, *denudatiesnelheid*, *bodemvracht/zwevende vracht/opgeloste vracht*, *diagenese*, *isostatisch herstel*, *warmtestroom*, *seculaire afkoeling*, *isochroon*, *beginverhouding*, *oeratmosfeer*, *gebande ijzerformatie*, *rode lagen*, *klimaatarchief*, *proxy*, *glaciaal/interglaciaal*, *stralingsforcering*, *klimaatterugkoppeling*, *evenwichtsklimaatgevoeligheid*, *toeschrijving*, *emissiescenario*. The IPCC vocabulary follows Book 1 g9 (*vrijwel zeker … zeer onwaarschijnlijk*; *(zeer) hoge / gemiddelde mate van vertrouwen*). Points off for terms where Dutch usage is split (*Grote Oxidatie* against the English loan *Great Oxidation Event*; *rode lagen* against *red beds*; *chert* kept beside *hoornsteen*; *bitumineuze kool*) |
| Register / tone | **96** | Informal *je/jouw/jij* (91 forms), **0** formal *u/uw*. Exercise stems are imperatives and questions (*Bereken*, *Leg uit*, *Toon aan*, *Waarom …?*). Upper-secondary register throughout; the climate chapters keep the canon's physical-science-only wording (no *moeten*, *vermijden* added) |
| Accuracy / sense | **96** | Every solution was re-read against its question and recomputed along the rounded path a student follows (isochrons, Patterson's lead slope, faint young Sun, 1 kg of iron, LR04 periods, pollen ages, Sunda areas, forcing law, doubling year). No number differs from English. No wording departs from the canon |
| Typography / mechanics | **97** | `` ``…'' `` quotes; decimal points kept in prose and maths; *miljoen/miljard*; *Foto …* / *foto van …* / *(publiek domein)* / *AI-illustratie*; coordinates *NB/ZB/OL/WL* also in tick labels; ranges *50 à 60* or *x tot y*. The line-edge sweeps are clean outside TikZ code |
| Link layer | **95** | **2068 links to 134 targets** (English 2187 / 135, 95 %). The only target English reaches and nl does not is `def:g11:subduction-zones:slab-pull` (English 2): English links the verb phrase *its slab pulls it down* (g11.06 solutions 160, g12.02 33), which Dutch writes *haar slab trekt haar omlaag*. nl reaches no target English does not. Homographs are curated in `book2_nl.py` (*breuk* fault/fracture, *val* trap/fall/*vals*, *gang* dyke/*aan de gang*, *voorraad* stock of water/store of heat, *gelaagdheid* of the ocean/of a mud, *Glarus-/McConnell-overschuiving*, *laatste interglaciaal*), with English's own STOPs (*oog, flux, afplatting, verzadigd, stabiel, vulkanisch*). The only per-target ratio outside 0.6–1.3 is *stroomgebied* (67 vs 12): Dutch has one unambiguous word where English mostly writes the unlinked short form *basin*. `--unwrap --apply` then `--apply`; the dry run prints **links to insert: 0** |
| Build cleanliness | **99** | Forced build: 0 `!`, 0 undefined, 0 overfull (two fixed during the run: the g12.09 problem table, by giving its first column the header *tijdstip (jaar geleden)*; a g12.10 solution, reworded around an unhyphenable compound), nullfont equal to English, 0 missing characters, 0 invalid-in-math |

## Figures

Every translated figure label of grade 12 chapters 7–10 was rendered and checked against its
numbers (estimates chart, Varden isochron, Patterson lead isochron, faint young Sun,
banded-iron schematic, oxygen timeline, Dome C records, Sunda map, pollen diagram, LR04,
feedback loops, forcing bars, attribution, projections); grades 10–12 chapters 1–6 were
checked the same way earlier in the run. No collision; the pollen titles (*kruiden, berk,
den, hazelaar, eik*) fit their columns.

The drawing census (`drawcensus.py nl`) shows six non-node differences, all English words
inside node text that the census reads as TikZ keywords: *core--mantle boundary* →
*kern-mantelgrens* (g11.02, g12.06: `--`), *small circle* → *kleine cirkel* (g11.04:
`circle`), *volcanic arc* → *vulkanische boog* (g11.06, g12.02: `arc`), *(circle)* →
*(cirkel)* (g12.07).

## `!draw` ranges (English line numbers)

g10-02 133–134 (explicit `xticklabels`), 299 (planet `\foreach`) · g10-03 226–229 (albedo
`\foreach`) · g10-05 58 (`\foreach \dx/\title`) · g11-08 153 (rock names), 162–169 (mineral
`\m` list) · g12-01 122 (`[about 70]` point meta) · g12-05 272 (`\lab` list) · g12-06
286–287 (`\lab` *trench* → *trog*) · g12-09 270–271 (`xticklabel` *°E* → *°OL*; the singular
key is not blanked by the census). No `!math` range.

## Shared-tool entry

`tools/check_latin_prose.py`: one append-only `ALLOWED_BY_LANG["nl"]` entry
(`bandB … bandF`) for the two colour-name `\foreach` lists of the g12.02 fold block diagram,
as es/pt/fr did. Run once: grade-12 went from FAIL (blocking foreach tier) to PASSED.

## Conventions recorded

- *je* with imperatives; *Weekendprobleem*; `\textbf{Deel I --- …}`; `\section{Oefeningen}`;
  `\section{Probleem: …}`; solution headers `\section*{Hoofdstuk \ref{…} --- Titel}`.
- De Aarde, de Zon, de Maan capitalised; *Boek 1, jaar N*; sister series as *(de
  natuurkundeboeken)*, *(de scheikundeboeken)*, *(de biologieboeken)*, *(de wiskundeboeken)*.
- Coordinates *NB/ZB/OL/WL* in prose, tables and tick labels; compass N O Z W.
- Decimal point kept; *miljoen/miljard*; *per jaar*; percentages as in English.
- Proof heads: bare `proof` as English; *[Gedeeltelijk bewijs]*, *[Verantwoording]*,
  *[Controle]*, *[Hoe het wordt berekend]* where English titles one.
- Credits: *Foto …*, *Foto's …*, *foto van …*, *(publiek domein)*, *Gegevens: …*,
  *X en anderen (2020)*, *AI-illustratie*.
- Accented index keys carry a sort key; math `\text{}` subscripts translated (*nu*, *lucht*,
  *vast*, *boven*, *onder*, *ijs*).
- Genders: *het graniet* (*een graniet dat*), *de polymorf*, *de isochroon* (*haar helling*),
  *het glaciaal/interglaciaal* (plural *glacialen*).
- Proper names kept: Varden Hills, Hamersley Ranges, Dome C, Beyond EPICA, SSP codes, IPCC.

## Canon findings (reported, not fixed in the English)

1. `frontmatter/image-credits-book2.tex` 76: "the history of the estimates after Dalrymple,
   as summarised by Wikipedia" cites Wikipedia as a source, which the repo's own rule
   ("Wikipedia is not a ledger source") forbids. Kept verbatim in nl.
2. `parts/grade-12/02-mountain-building.tex` 33 and `parts/grade-11/solutions/06-subduction-zones.tex`
   160: English links the subject + verb *slab pulls* ("its slab pulls it down") to the
   *slab pull* definition, a noun–verb homograph match.

## Coordinator amendment (2026-10-25, after the es report)

The definition of cleavage opens on the capitalised display *Splijting*, so the
lowercase noun never linked (English had the same gap: 1 link out of ~30 uses).
`book2_nl.py` gained EXTRA *splijting*, *splijtrichting(en)*; English gained
EXTRA *cleavage(s)*. Relinked: **2,090 links** (was 2,068); the cleavage target
now has 23 links (English 24). Linker dry run 0, `--check` clean, grade-11 gate
green. English baseline is now 2,208 links / 135 targets.
Second amendment (after the pt report): EXTRA *migratie* (the same capitalised
opening, *Migratie*): migration target 1 → 5 links; total **2,094 links**.
Four canon number fixes mirrored into this edition's g12 solutions 04, 05, 06
and the g12/05 comment (see `sources/WAVE1_FINDINGS_B2.md`). English baseline
now 2,208 links / 136 targets.

## Coordinator amendments

- 2026-10-26: g11 solutions/08 answer 16 rewritten by the coordinator after an English canon fix (reported by hi): ≈ 950 days, 2.6 years, within the intrusion range, not "between the two". Gates for grade 11 re-run, green; linker dry run 0.
- 2026-10-26: `book2_nl.py` EXTRA "trek van de wegzakkende slab" (and "slabtrek") → slab pull, the capital-harvest trap again (`\emph{Slabtrek}`); g11 solutions/06 now links the defined force, as English does. Links stay 2,094 (that phrase linked to *slab* before); targets 135 → 136, every English target reached.
- 2026-10-26: g11/01 "Motonari" → "Motonori" Matuyama, and the g12/02 fold-shortening chart labels (Varden label no longer clipped, 13 % label moved below-right of its point), both after the Arabic report; mirrored by the coordinator.

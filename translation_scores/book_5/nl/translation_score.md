# Translation score: One Earth and Space Sciences Book 5, Dutch (`nl`)

| Field | Value |
|-------|--------|
| **Book** | One Earth and Space Sciences Book 5 (University Year 3, `bachelor-3`) |
| **Language** | Dutch (`nl`), Netherlands usage; `Ma`/`Myr`/`Gyr`/`yr` as English; NB/ZB/OL/WL; terms as in Dutch Books 1–4 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium): 711 calls, pilot method, one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Overall score** | **90 / 100**, sampled: 20 passages, seed 1, not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures sampled |
| **Canon** | English not verified: Book 5 predates the verification pass of `book_style.md`, and solutions were not recomputed. |
| **Tokens** | `all: 711 calls, prompt 4152K + cache read 3300K, output 6989K (thinking 4918K), list price $4.36`. Coordinator (Opus 5.5), from its transcript: 13.3M cache read, 1.17M cache write, 120K output, measured before the last few calls; likely the larger share of the cost |
| **Date** | 2026-11-03 |
| **Scope** | 31 chapters + 31 solution files = 62 files, 288 sections |

## Verdict in one line

A complete Dutch Book 5 that reads as near-native in the sample and is structurally identical to English, all gates green
and clean in the log. It was not read sentence by sentence, and it still carries small language defects at about the rate
the reading found: one per five pages or so, none changing the science.

## What the score rests on

- **Read against English:** the 20 passages of `sample.py --n 20 --seed 1` (`draft/pilot-bachelor-3-nl/sample.txt`) and the
  openings of chapters 3, 19 and 29.
- **Pages:** `sample.py --pages` listed 50 pages. **39 were read at 130 dpi:** 14, 15, 16, 33, 49, 53, 61, 69, 108, 111, 118,
  131, 137, 163, 195, 196, 200, 217, 222, 229, 231, 242, 250, 254, 278, 292, 303, 312, 352, 357, 370, 390, 393, 404, 411, 428,
  434, 452, 484. **The other 11 were not read:** 2, 5, 12, 458, 462 gave `crop.py` no figure region; 333, 334, 391, 392, 481, 497 have
  at most 3 drawing strokes, boxes only. Pages 200 and 217 were re-read after their figures were repaired.
- `pdfsweep.py`'s top words over the whole book; a line-level number diff (`nd.py`) over all 62 files.

## Defects found, all fixed

| Where found | Defect | Examples |
|---|---|---|
| Sample (3) | Gender; doubled phrase; calque | *het geopotentiaal*; *in rust* twice in ch. 20; *Schalie breekt beide* in ch. 17 |
| Pages, language (8) | Doubled or stray word; wrong article; broken compound; missing full stop | *reproduceert* twice (ch. 3), *wordt* twice (ch. 30), *van de dezelfde* (ch. 17), *de bronpunt* (ch. 18), *breukgliding- inversie* (ch. 8), a caption without its full stop (ch. 7), *Walther's wet* and *onderwateroeversand* with English *-sand* (ch. 17) |
| Pages, figures (2) | Label over a box edge or over its neighbour | Facies strip in ch. 17; box label in ch. 15 |
| Sweeps | Backwards wind phrase | ch. 20: *voor een oostelijke wind* where $u$ blows towards the east; two more stream phrases in ch. 19–20 |
| Sweeps | Number form | Decimal commas in ch. 16 and 29; thousands in ch. 25–26; unit-less `\qty` in ch. 7 |
| Gates | English left in figures and titles; comment damage | About 20 titles and labels; five `% ledger` defects and 14 translated comments |
| `pdfsweep.py` | Residual English | *assessment* throughout ch. 22, now *rapport* / *beoordelingsrapport* |

## Known weaknesses that remain

- A section nobody read carries the same defect rate: expect about a hundred small language defects in the book.
- The invented names *Lake Ardo* and *Lake Orrin* stay in English form, like *Varden Hills*.
- Terminology can vary between sections, because each call sees one section. Fixed where found: *afvoergebied*,
  *drainagegebied* and *afwateringsgebied* in ch. 18. Other such pairs are probably still there.

## NUMDIFF

30 files flagged. Most are `Year N`/`Book N` becoming `Boek~N` and numbers moved between lines. Real losses fixed: 3 classes
(decimal commas, thousands, unit-less `\qty`); lines not counted. **Accepted differences:** cross-volume references, word forms
such as *acht dagen later* for 8 days (solution 25, line 12), and hyphen forms such as 20-s. No lost number otherwise.

## Numbers

504 pp; 0 errors, 0 undefined, 0 overfull, nullfont 0, missing characters 0, `.fls` 62/62. `check_translation.sh` passed,
`gates.sh` OK, linker check OK, orphan lines 0, Latin prose gate no multi-word findings. 1295 links on 231 targets (English
1191 on 216). One target not reached: `def:b3:palaeomagnetism:apw`, English 1 link.

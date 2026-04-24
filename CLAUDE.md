# LUCIA — LUCY's House Rules

You're in LUCY's house now. Read these before you touch anything.

LUCIA is The Human Chronicle — a narrative encyclopedia of human civilization.
Every culture told from inside their own worldview. Named after LUCY, a German
Shorthaired Pointer, 10 years old, who watches rabbits all day with more patience
than most historians and always goes through the gate first.

Sibling projects: MAXIM (C:\src\reference), FELIX/RMM (C:\src\rmm). Fully
independent — own rules, own voice, own scoring. Borrows patterns, not authority.

---

## Editorial Philosophy — 4 Rules

1. **Present from within.** Tell each culture's story from inside their worldview.
   The text never steps outside to judge. The Aztecs tell the Aztec story.
2. **No historical judgment.** Don't pre- or post-judge against different standards.
   Periodization belongs to the culture — their era names, not Western academic labels.
3. **Story-first.** Each chapter opens with a scene: a real person, a real moment.
   Context emerges from narrative, not the other way around.
4. **Evolving quality.** The scoring rubric is a learning system. When something
   exceptional appears, capture it, update the rubric, raise the bar.

---

## LUCY's Personality

**Where LUCY lives:** Preface, tools, scoring, CLAUDE.md, style guide — the
infrastructure that holds the project together.

**Where LUCY is silent:** Culture chapters. Cultures speak for themselves.

| Trait | How It Shows Up |
|-------|----------------|
| Patient, observant (watches rabbits all day) | Thorough review process, no rushing |
| Not shy to say when she's hungry | Direct feedback, no-nonsense scoring |
| Nice cuddles | Warm, approachable guides and preface |
| Goes through gates first | Quality gates, pipeline discipline |

---

## The 5-Level Tree

```
L1  Region          26 geographic/cultural areas
L2  People          Named civilizations (~250-300)
L3  Era             Period as the culture defined it, in their terms
L4  Chapter files   opening.md (~800w), chapter.md (~5000w), notes.md, figures.md
L5  Review rounds   reviews/R1-*.md, R2-*.md, BOARD-*.md
```

---

## The 26 Regions

### Ancient & Living World (1-22)

| #  | Region |
|----|--------|
| 1  | Mesoamerica |
| 2  | Andes & Western South America |
| 3  | Amazonia, Caribbean & Lowland South America |
| 4  | North America |
| 5  | Mediterranean Classical World |
| 6  | Fertile Crescent & Mesopotamia |
| 7  | Iran & the Persianate World |
| 8  | The Islamic Heartlands |
| 9  | Egypt & the Nile Valley |
| 10 | West African Sahel & Savanna |
| 11 | West African Forest & Guinea Coast |
| 12 | Central Africa & Kongo World |
| 13 | East Africa, Horn & Swahili World |
| 14 | Southern Africa |
| 15 | South Asia (Indic World) |
| 16 | Tibet & the Himalayan World |
| 17 | East Asia (Sinographic Sphere) |
| 18 | Southeast Asia |
| 19 | Central & Inner Asia (Steppe World) |
| 20 | Western Christendom |
| 21 | Northern & Eastern Europe |
| 22 | Oceania & the Pacific World |

### The Crossroads (23-26)

| #  | Region |
|----|--------|
| 23 | The Americas Reborn |
| 24 | Colonial Empires & Systems |
| 25 | Diasporas & Dispersed Peoples |
| 26 | The Pacific Century (Modern East Asia) |

---

## Forbidden Words & Framings

**Never use in culture chapters:**
- primitive, advanced, tribe, Dark Ages, "discovered by [Europeans]", "the New World"

**Never frame as:**
- "While Europe was doing X, these people were doing Y"
- "Before contact with the West, they had already..."
- "They were remarkably sophisticated for..."

**The Achebe Test:** Could a thoughtful member of this culture read this and feel
their story was told with dignity — from inside — regardless of whether they
agreed with every detail?

---

## Scoring

**The Gate** (openings): 30 points across 6 dimensions — Scene, World, Honesty,
Texture, Voice, Pull. 5 points each.

**The Chronicle** (chapters): 60 points across 6 dimensions — Immersion, Evidence,
Progression, Figures, Voice, Landing. 10 points each.

**Total: 90 points per era.**

| Target | Score |
|--------|-------|
| Opening (The Gate) | 24+ / 30 |
| Chapter (The Chronicle) | 48+ / 60 |
| Manuscript mean | 75+ / 90 |

The rubric evolves. Innovations get logged, and after 2+ in the same category,
the rubric version increments. New bar applies forward only.

---

## Pipeline — 11 Stages

```
OPENING → GATE-1 → PANEL-1 → NOTES → PANEL-2 → FIXES → WRITE → GATE-2 → CLEAN → BOARD → FINAL
```

1. **OPENING** — Write opening.md (~800w). Hook scene.
2. **GATE-1** — Score against The Gate. Target: 24+/30.
3. **PANEL-1** — All 5 panel voices review the opening.
4. **NOTES** — Write notes.md (production bible).
5. **PANEL-2** — Panel reviews notes, targets weak areas.
6. **FIXES** — Apply feedback, revise opening if needed.
7. **WRITE** — Write chapter.md (~5000w) + figures.md.
8. **GATE-2** — Score against The Chronicle. Target: 48+/60.
9. **CLEAN** — Judgment check, voice consistency, em-dash audit, sources.
10. **BOARD** — Domain experts give final assessment.
11. **FINAL** — Apply board fixes, lock chapter. Log innovations.

**Anchor rule:** 1 region, 1 people, 1 era — through all 11 stages before scaling.

---

## The Panel — 5 Voices

| Voice | Lens |
|-------|------|
| **Barbara Tuchman** | Narrative craft — pacing, scene construction, arc |
| **Ibn Khaldun** | Historical systems — patterns, causation, cycles |
| **Chinua Achebe** | Cultural voice — dignity, authenticity, ownership |
| **Wade Davis** | Anthropological wonder — hidden condescension, worldview depth |
| **Ryszard Kapuscinski** | Sensory immersion — heat, smell, sound, texture |

Role definitions at `.roles/panel/`

Editorial roles (Judgment Auditor, Voice Keeper, Compression Editor) at
`.roles/editorial/`

Board role template at `.roles/board/`

---

## Source Tiers

| Tier | Type | Use |
|------|------|-----|
| 1 | Primary sources | Gold standard. Original texts, inscriptions, oral traditions. |
| 2 | Academic | Peer-reviewed journals, university press monographs. |
| 3 | Scholarly secondary | Historian books, museum publications. MAXIM/FELIX are Tier 3. |
| 4 | Reference | Wikipedia for dates/facts only. Prefer underlying papers. |
| 5 | Do not use | Grokipedia, mirrors, pop YouTube, unsourced blogs, unverified AI. |

---

## Safety Rules

- **Never delete files by regex.** Always verify what you're deleting.
- **Protect structural files:** CLAUDE.md, TRACKER.md, 00-LANDSCAPE.md, 00-OVERVIEW.md.
  Never overwrite these without explicit confirmation.
- **Never glob outside project scope.** Stay in C:\src\chronicle.
- **Always verify before destructive operations.** Read before you write.

---

## Directory Conventions

- Regions numbered `01` through `26` (zero-padded).
- People directories: lowercase, hyphenated (e.g., `aztec-mexica`).
- Standard files per region: `00-LANDSCAPE.md`, `SOURCES.md`
- Standard files per people: `00-OVERVIEW.md`, `SOURCES.md`
- Standard files per era: `opening.md`, `chapter.md`, `notes.md`, `figures.md`
- Reviews in: `reviews/R1-*.md`, `R2-*.md`, `BOARD-*.md`

---

## Key Files

| What | Where |
|------|-------|
| Design spec | `docs/superpowers/specs/2026-04-14-lucia-design.md` |
| Roles | `.roles/` (panel, editorial, board) |
| Style guide | `guides/STYLE-GUIDE.md` |
| Pipeline | `guides/PIPELINE.md` |
| Scoring rubric | `scoring/RUBRIC.md` |
| Tracker | `TRACKER.md` |
| Innovation log | `scoring/INNOVATIONS.md` |
| Source registry | `sources/MASTER.md` |

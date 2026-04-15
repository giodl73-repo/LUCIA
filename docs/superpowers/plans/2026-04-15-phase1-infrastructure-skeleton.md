# Phase 1: Infrastructure + Skeleton — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bootstrap the LUCIA Chronicle project with all infrastructure files and build the full 26-region skeleton at 3 levels deep (Region → People → Eras listed).

**Architecture:** Content-first Markdown project rendered via MkDocs + Material theme. 26 region directories, each containing people subdirectories with overview files that enumerate eras. Infrastructure includes CLAUDE.md, style guide, pipeline guide, scoring rubric, source management, and a status tracker.

**Tech Stack:** MkDocs + Material theme, Markdown, Python (MkDocs), Bash (serve script)

**Spec:** `docs/superpowers/specs/2026-04-14-lucia-design.md`
**Roles:** `.craft/roles/` (panel, editorial, board)

---

## File Map

```
chronicle/
├── CLAUDE.md                              ← Task 1
├── README.md                              ← Task 1
├── index.md                               ← Task 1
├── .gitignore                             ← Task 1
├── TRACKER.md                             ← Task 7
├── .mkdocs/
│   ├── mkdocs.yml                         ← Task 2
│   └── serve.sh                           ← Task 2
├── guides/
│   ├── STYLE-GUIDE.md                     ← Task 3
│   ├── PIPELINE.md                        ← Task 4
│   ├── TEMPLATES.md                       ← Task 4
│   └── HOW-TO-WRITE-A-CHAPTER.md          ← Task 4
├── scoring/
│   ├── RUBRIC.md                          ← Task 5
│   ├── INNOVATIONS.md                     ← Task 5
│   └── TARGETS.md                         ← Task 5
├── sources/
│   ├── MASTER.md                          ← Task 6
│   ├── ACQUISITION.md                     ← Task 6
│   └── by-region/                         ← Task 6
│       └── (26 region source files)
├── panel/                                 ← already done (.craft/roles/)
├── regions/
│   ├── 01-mesoamerica/                    ← Tasks 8-13 (LANDSCAPE.md)
│   │   ├── 00-LANDSCAPE.md               ← Tasks 14-19 (peoples + OVERVIEW.md)
│   │   ├── olmec/00-OVERVIEW.md
│   │   ├── maya/00-OVERVIEW.md
│   │   └── ...
│   ├── 02-andes/
│   ├── ...
│   └── 26-pacific-century/
└── docs/superpowers/
    ├── specs/2026-04-14-lucia-design.md   ← already done
    └── plans/2026-04-15-phase1-*.md       ← this file
```

Regions are numbered 01-26 in directory names for sort order, matching the
canonical list in the spec (Section 5).

---

## Task 1: Project Scaffold

**Files:**
- Create: `CLAUDE.md`
- Create: `README.md`
- Create: `index.md`
- Create: `.gitignore`

- [ ] **Step 1: Create .gitignore**

```
# MkDocs build output
site/

# Superpowers brainstorm sessions
.superpowers/

# OS files
.DS_Store
Thumbs.db

# Python
__pycache__/
*.pyc
.venv/

# Editor
*.swp
*.swo
*~
```

- [ ] **Step 2: Create CLAUDE.md**

This is LUCY's house rules — the most important file in the project. It must contain:

1. **Project identity** — LUCIA, The Human Chronicle, codename after LUCY the GSP
2. **Editorial philosophy** — present from within, no judgment, story-first, evolving quality
3. **LUCY's personality** — where it lives (infrastructure) and where it's silent (chapters)
4. **The 5-level tree** — L1 Region → L2 People → L3 Era → L4 Chapter files → L5 Reviews
5. **The 26 regions** — canonical numbered list from spec Section 5
6. **Key rules** — forbidden words, forbidden framings, the Achebe Test
7. **Scoring** — The Gate (30pts) + The Chronicle (60pts), targets
8. **Pipeline** — 11 stages, anchor rule
9. **Panel** — 5 voices with one-line descriptions
10. **Source tiers** — what to use, what not to
11. **Safety rules** — never delete by regex, protect structural files, never glob outside scope
12. **Directory conventions** — numbering (01-26 for regions), file naming (00-LANDSCAPE.md, 00-OVERVIEW.md, opening.md, chapter.md, notes.md, figures.md)

Reference the full spec at `docs/superpowers/specs/2026-04-14-lucia-design.md` and the roles at `.craft/roles/ROLE.md`. Do NOT duplicate the full spec — CLAUDE.md is the session startup guide, not the archive.

Tone: LUCY's voice — observant, direct, warm, disciplined. Not corporate. Not cute. The voice of a smart dog who runs a tight ship.

- [ ] **Step 3: Create README.md**

```markdown
# LUCIA — The Human Chronicle

The story of every human culture, told from inside their own worldview.

26 regions. ~250-300 peoples. Thousands of eras.
Each one told the way they would tell it themselves.

## What This Is

LUCIA is a narrative encyclopedia of human civilization. Every culture gets
its own book — structured as a region containing peoples, each with chapters
covering their eras. The writing is story-first: each chapter opens with a
real person in a real moment, and the era's context emerges from narrative.

## The Rule

The text never steps outside a culture's worldview to judge. No culture is
measured against another's standards. The reader stands inside, not above.

## Named After

LUCY — a German Shorthaired Pointer, 10 years old, who watches rabbits
with the patience of a historian and goes through every gate first.

## Project

- **Spec:** docs/superpowers/specs/2026-04-14-lucia-design.md
- **Roles:** .craft/roles/
- **Style:** guides/STYLE-GUIDE.md
- **Pipeline:** guides/PIPELINE.md
- **Scoring:** scoring/RUBRIC.md

Built with MkDocs + Material theme.
```

- [ ] **Step 4: Create index.md**

The MkDocs landing page. Should contain:
- Project title and one-line description
- ASCII art showing the 5-level tree structure
- Navigation links to the 26 regions (grouped as "Ancient & Living World" + "Crossroads")
- Links to guides, scoring, sources

- [ ] **Step 5: Commit**

```bash
git add CLAUDE.md README.md index.md .gitignore
git commit -m "Bootstrap project scaffold — CLAUDE.md, README, index, gitignore"
```

---

## Task 2: MkDocs Configuration

**Files:**
- Create: `.mkdocs/mkdocs.yml`
- Create: `.mkdocs/serve.sh`

- [ ] **Step 1: Create mkdocs.yml**

Model after MAXIM's `.mkdocs/mkdocs.yml` (at `C:\src\reference\.mkdocs\mkdocs.yml`) but adapted for LUCIA:

Key settings:
- `site_name: LUCIA — The Human Chronicle`
- `theme: material` with custom palette (different from MAXIM — LUCIA should have its own identity)
- Font: EB Garamond for body (same as MAXIM — good for long reading), JetBrains Mono for code
- Extensions: tables, admonitions, attr_list, def_list, toc with permalinks, superfences
- `docs_dir: ..` (project root, since content lives at root level)
- `site_dir: ../../chronicle-site` (output alongside project, not inside it)
- Navigation: build initial nav with guides, scoring, sources, and placeholder for regions

The nav structure should be:

```yaml
nav:
  - Home: index.md
  - Guides:
    - Style Guide: guides/STYLE-GUIDE.md
    - Pipeline: guides/PIPELINE.md
    - Templates: guides/TEMPLATES.md
    - How to Write a Chapter: guides/HOW-TO-WRITE-A-CHAPTER.md
  - Scoring:
    - Rubric: scoring/RUBRIC.md
    - Innovations: scoring/INNOVATIONS.md
    - Targets: scoring/TARGETS.md
  - Sources:
    - Master Registry: sources/MASTER.md
    - Acquisition: sources/ACQUISITION.md
  - The Ancient & Living World:
    - Mesoamerica: regions/01-mesoamerica/00-LANDSCAPE.md
    - Andes & Western South America: regions/02-andes/00-LANDSCAPE.md
    # ... all 22 regions
  - The Crossroads:
    - The Americas Reborn: regions/23-americas-reborn/00-LANDSCAPE.md
    - Colonial Empires & Systems: regions/24-colonial-empires/00-LANDSCAPE.md
    - Diasporas & Dispersed Peoples: regions/25-diasporas/00-LANDSCAPE.md
    - The Pacific Century: regions/26-pacific-century/00-LANDSCAPE.md
```

- [ ] **Step 2: Create serve.sh**

```bash
#!/usr/bin/env bash
cd "$(dirname "$0")"
python -m mkdocs serve -f mkdocs.yml
```

- [ ] **Step 3: Verify MkDocs serves**

```bash
cd .mkdocs && bash serve.sh
```

Open `http://127.0.0.1:8000` — confirm the site loads with the landing page. Stop the server.

- [ ] **Step 4: Commit**

```bash
git add .mkdocs/
git commit -m "Add MkDocs configuration with Material theme"
```

---

## Task 3: Style Guide

**Files:**
- Create: `guides/STYLE-GUIDE.md`

- [ ] **Step 1: Write STYLE-GUIDE.md**

Pull content from the spec Section 7 (Style Guide). This is not a copy — it's the full, authoritative style guide for chapter authors. Must include:

1. **The Achebe Test** — the core rule, prominently placed
2. **The 13 Principles** — with before/after examples for each. For every principle, show a BAD example and a GOOD example drawn from historical writing. These examples must be original (written for LUCIA), not quoted from published works.
3. **Mechanical Rules** — chapter lengths, em-dash limits
4. **Forbidden Words** — table with word, why, use-instead
5. **Forbidden Framings** — table with framing, why
6. **The Voice Spectrum** — guidance on how prose rhythm should vary by culture type (steppe cultures vs. court cultures vs. maritime cultures vs. oral traditions)

Example before/after for Principle #2 (The World Before the Label):

```
BAD:  The potlatch ceremony was a practice of competitive gift-giving
      among the Kwakwaka'wakw people of the Pacific Northwest.

GOOD: The chief stood before the assembled guests and began to give
      away everything he owned. Blankets first — stacked higher than
      a man could reach. Then copper shields, each worth a canoe.
      Then the canoes themselves. The guests watched, calculating.
      Every gift was a challenge: match this, or admit you cannot.
      The Kwakwaka'wakw called it potlatch.
```

- [ ] **Step 2: Commit**

```bash
git add guides/STYLE-GUIDE.md
git commit -m "Add LUCIA style guide — 13 principles with before/after examples"
```

---

## Task 4: Pipeline & Template Guides

**Files:**
- Create: `guides/PIPELINE.md`
- Create: `guides/TEMPLATES.md`
- Create: `guides/HOW-TO-WRITE-A-CHAPTER.md`

- [ ] **Step 1: Write PIPELINE.md**

The 11-stage pipeline from spec Section 6.6, expanded with:
- Clear entry/exit criteria for each stage
- Who does what (which roles fire at which stage)
- What artifacts are produced
- ASCII flow diagram showing the full pipeline
- The Anchor Rule explained

- [ ] **Step 2: Write TEMPLATES.md**

The LANDSCAPE template (L1) and OVERVIEW template (L2) from spec Section 7.6-7.7, expanded with:
- Annotated examples (not just the template skeleton — show a filled-in example)
- A LANDSCAPE example for a fictional region
- An OVERVIEW example for a fictional people
- The chapter file templates (opening.md, chapter.md, notes.md, figures.md) with structure guidance

- [ ] **Step 3: Write HOW-TO-WRITE-A-CHAPTER.md**

End-to-end guide for a chapter author (agent or human). Walk through the process from "you've been assigned an era" to "the chapter is locked." Include:
- How to research the era (source tiers, what to look for)
- How to write the opening (scene selection, the 800-word constraint)
- How to write the production bible (notes.md structure)
- How to write the full chapter (5000-word structure, section pacing)
- How to write figures.md (key leaders and people)
- Common mistakes and how to avoid them (drawn from the forbidden words/framings)
- What to expect from the panel and how to use their feedback

- [ ] **Step 4: Commit**

```bash
git add guides/
git commit -m "Add pipeline, templates, and chapter-writing guides"
```

---

## Task 5: Scoring System

**Files:**
- Create: `scoring/RUBRIC.md`
- Create: `scoring/INNOVATIONS.md`
- Create: `scoring/TARGETS.md`

- [ ] **Step 1: Write RUBRIC.md**

The Gate (30pts) + The Chronicle (60pts) from spec Section 6.2-6.3, expanded with:
- Version header: `## Rubric v1.0 — Established 2026-04-15`
- Detailed scoring guidance for each dimension (what does a 1 look like? A 3? A 5?)
- Per-dimension anchor examples: a score-1 sentence vs. a score-5 sentence
- Scoring worksheet template that reviewers fill out per chapter:

```markdown
## Scoring Worksheet — The Gate

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Scene     | /5    |          |
| World     | /5    |          |
| Honesty   | /5    |          |
| Texture   | /5    |          |
| Voice     | /5    |          |
| Pull      | /5    |          |
| **Total** | /30   |          |
```

- [ ] **Step 2: Write INNOVATIONS.md**

```markdown
# Innovation Log

Innovations are exceptional techniques discovered during chapter writing that
the rubric did not anticipate. When 2+ innovations emerge in the same category,
they trigger a rubric amendment.

## Log

*(No innovations yet — this log will grow as chapters are written.)*

## Amendment History

| Version | Date | Amendment | Source | Dimension |
|---------|------|-----------|--------|-----------|
| v1.0    | 2026-04-15 | Initial rubric | — | — |
```

- [ ] **Step 3: Write TARGETS.md**

```markdown
# Scoring Targets

## Per-Chapter Targets

| Metric | Target | Minimum |
|--------|--------|---------|
| Opening (The Gate) | 24+ / 30 (80%) | 21 / 30 (70%) |
| Full Chapter (The Chronicle) | 48+ / 60 (80%) | 42 / 60 (70%) |
| Combined | 72+ / 90 (80%) | 63 / 90 (70%) |

## Manuscript Targets

| Metric | Target |
|--------|--------|
| Manuscript mean | 75+ / 90 (83%) |
| No chapter below | 63 / 90 (70%) |

## How Targets Evolve

Targets may increase as innovations are adopted and the rubric matures.
Targets never decrease. When a rubric amendment raises the bar, the target
for that dimension is reviewed and may be adjusted upward.
```

- [ ] **Step 4: Commit**

```bash
git add scoring/
git commit -m "Add scoring system — rubric v1.0, innovation log, targets"
```

---

## Task 6: Source Management

**Files:**
- Create: `sources/MASTER.md`
- Create: `sources/ACQUISITION.md`
- Create: `sources/by-region/.gitkeep`

- [ ] **Step 1: Write MASTER.md**

```markdown
# Source Master Registry

Global registry of all sources used across the Chronicle.

## Source Tiers

| Tier | Type | Use |
|------|------|-----|
| 1 | Primary sources | Original texts, inscriptions, oral traditions. Gold standard. |
| 2 | Academic sources | Peer-reviewed journals, university press monographs. |
| 3 | Scholarly secondary | Well-sourced books by recognized historians, museum publications. |
| 4 | Reference | Wikipedia (dates/facts only, not interpretive claims). |
| 5 | Do not use | Grokipedia, Wikipedia mirrors, pop YouTube, unsourced blogs. |

## Cross-Project References

| Source | Tier | Location | Use |
|--------|------|----------|-----|
| MAXIM | 3 | C:\src\reference | Background context, verify independently |
| FELIX/RMM | 3 | C:\src\rmm | Comparative mythology, verify independently |

## Registry

*(Sources will be registered here as chapters are written.
Format: Author, Title, Year, Tier, Regions Used In.)*
```

- [ ] **Step 2: Write ACQUISITION.md**

```markdown
# Source Acquisition Punchlist

Sources needed but not yet acquired or consulted. Fed by `NEEDED` entries
in individual chapter notes.md files.

## Punchlist

*(Empty — will be populated as chapters enter the NOTES stage.)*
```

- [ ] **Step 3: Create by-region directory**

```bash
touch sources/by-region/.gitkeep
```

Region-specific source bibliographies will be created alongside their LANDSCAPE.md files in Tasks 8-13.

- [ ] **Step 4: Commit**

```bash
git add sources/
git commit -m "Add source management — master registry, acquisition punchlist"
```

---

## Task 7: Status Tracker

**Files:**
- Create: `TRACKER.md`

- [ ] **Step 1: Write TRACKER.md**

A status dashboard for the entire project, modeled on MAXIM's `TRACKER.md`. Must include:

1. **Phase status** — which phase we're in (Phase 1: Skeleton)
2. **Region status table** — all 26 regions with columns:
   - Region name
   - LANDSCAPE.md status (none / stub / draft / complete)
   - Peoples count (how many L2 entries)
   - Overviews status (none / stub / draft / complete)
   - Chapters started (count)
   - Chapters locked (count)
3. **Totals row** — aggregate counts
4. **Last updated date**

Initial state: all regions at "none" for everything.

```markdown
# LUCIA Chronicle — Status Tracker

**Phase:** 1 — Skeleton (3 levels deep)
**Last updated:** 2026-04-15

## Region Status

| # | Region | Landscape | Peoples | Overviews | Chapters | Locked |
|---|--------|-----------|---------|-----------|----------|--------|
| 1 | Mesoamerica | — | 0 | — | 0 | 0 |
| 2 | Andes & Western SA | — | 0 | — | 0 | 0 |
...all 26 rows...
| **Total** | | **0/26** | **0** | **0** | **0** | **0** |
```

- [ ] **Step 2: Commit**

```bash
git add TRACKER.md
git commit -m "Add status tracker — all regions at initial state"
```

---

## Task 8: Skeleton L1 — Americas Landscapes (Regions 1-4)

**Files:**
- Create: `regions/01-mesoamerica/00-LANDSCAPE.md`
- Create: `regions/02-andes/00-LANDSCAPE.md`
- Create: `regions/03-amazonia-caribbean/00-LANDSCAPE.md`
- Create: `regions/04-north-america/00-LANDSCAPE.md`
- Create: `sources/by-region/mesoamerica.md`
- Create: `sources/by-region/andes.md`
- Create: `sources/by-region/amazonia-caribbean.md`
- Create: `sources/by-region/north-america.md`

- [ ] **Step 1: Create region directories**

```bash
mkdir -p regions/01-mesoamerica regions/02-andes regions/03-amazonia-caribbean regions/04-north-america
```

- [ ] **Step 2: Write 00-LANDSCAPE.md for each region**

Follow the LANDSCAPE template from `guides/TEMPLATES.md`. Each must contain:

1. **Region name and introduction** (1-2 paragraphs: what makes this a region)
2. **The Land** — ASCII map showing peoples' locations, major geographic features (rivers, mountains, coastlines). Use the culture's own place names where known.
3. **The Peoples** — table with: People name, approximate span, key theme (1 sentence)
4. **How They Connect** — trade, war, cultural exchange, migration that binds this region
5. **Cross-References** — links to cultures in other regions that interact significantly

The peoples listed MUST match the spec (Section 5) and include the full set identified in the stress test. For Region 1 (Mesoamerica), the peoples are:
- Olmec, Maya, Teotihuacan, Zapotec, Mixtec, Toltec, Aztec/Mexica, Purépecha, Totonac

For Region 2 (Andes):
- Chavín, Moche, Nazca, Tiwanaku, Wari, Chimú, Inca, Muisca, Mapuche

For Region 3 (Amazonia/Caribbean):
- Taino, Carib, Arawak, Tupí-Guaraní, Marajoara, Kuikuro, Yanomami
- Plus any additional significant peoples identified during research

For Region 4 (North America):
- Mississippian/Cahokia, Haudenosaunee, Cherokee, Creek, Comanche, Lakota, Pueblo, Navajo, Haida/Tlingit, Cree, Anishinaabe, Inuit

- [ ] **Step 3: Create source stubs for each region**

Each `sources/by-region/<region>.md` should have:
- Region name header
- Empty table structure for sources (Author, Title, Year, Tier)
- Note: "Sources will be populated as chapters are written"

- [ ] **Step 4: Update TRACKER.md**

Set Landscape status to "draft" for regions 1-4. Set Peoples count.

- [ ] **Step 5: Commit**

```bash
git add regions/01-* regions/02-* regions/03-* regions/04-* sources/by-region/ TRACKER.md
git commit -m "Add Americas landscapes — Mesoamerica, Andes, Amazonia, North America"
```

---

## Task 9: Skeleton L1 — Mediterranean & Middle East Landscapes (Regions 5-8)

**Files:**
- Create: `regions/05-mediterranean/00-LANDSCAPE.md`
- Create: `regions/06-fertile-crescent/00-LANDSCAPE.md`
- Create: `regions/07-iran-persianate/00-LANDSCAPE.md`
- Create: `regions/08-islamic-heartlands/00-LANDSCAPE.md`
- Create: `sources/by-region/` entries for each

- [ ] **Step 1: Create region directories**

```bash
mkdir -p regions/05-mediterranean regions/06-fertile-crescent regions/07-iran-persianate regions/08-islamic-heartlands
```

- [ ] **Step 2: Write 00-LANDSCAPE.md for each region**

Same template as Task 8. Peoples from the spec:

Region 5 (Mediterranean): Minoan, Mycenaean, Phoenician, Greek city-states, Etruscan, Roman Republic/Empire, Carthage, Byzantine Empire

Region 6 (Fertile Crescent): Sumer, Akkad, Babylon, Assyria, Mitanni, Hittites, Urartu, Arameans

Region 7 (Iran/Persianate): Elam, Achaemenid Persia, Parthia, Sassanid Empire, Samanids, Safavids, Qajar, Kurdish dynasties, Durrani/Afghan

Region 8 (Islamic Heartlands): Pre-Islamic Arabian tribes, Rashidun, Umayyad, Abbasid, Fatimid, Ayyubid, Mamluk, Seljuks of Rum, Ottoman Empire, Berber/Amazigh, Almoravids, Almohads, Barbary States

- [ ] **Step 3: Create source stubs and update TRACKER.md**

- [ ] **Step 4: Commit**

```bash
git add regions/05-* regions/06-* regions/07-* regions/08-* sources/by-region/ TRACKER.md
git commit -m "Add Mediterranean & Middle East landscapes — 4 regions"
```

---

## Task 10: Skeleton L1 — Africa Landscapes (Regions 9-14)

**Files:**
- Create: `regions/09-egypt-nile/00-LANDSCAPE.md`
- Create: `regions/10-west-africa-sahel/00-LANDSCAPE.md`
- Create: `regions/11-west-africa-forest/00-LANDSCAPE.md`
- Create: `regions/12-central-africa/00-LANDSCAPE.md`
- Create: `regions/13-east-africa-horn/00-LANDSCAPE.md`
- Create: `regions/14-southern-africa/00-LANDSCAPE.md`
- Create: `sources/by-region/` entries for each

- [ ] **Step 1: Create region directories**

```bash
mkdir -p regions/09-egypt-nile regions/10-west-africa-sahel regions/11-west-africa-forest regions/12-central-africa regions/13-east-africa-horn regions/14-southern-africa
```

- [ ] **Step 2: Write 00-LANDSCAPE.md for each region**

Same template. Peoples from the spec:

Region 9 (Egypt/Nile): Predynastic, Old Kingdom, Middle Kingdom, New Kingdom, Ptolemaic, Roman Egypt, Coptic, Kush, Meroe

Region 10 (W. Africa Sahel): Ghana Empire, Mali, Songhai, Kanem-Bornu, Hausa city-states, Fulani, Wolof, Soninke

Region 11 (W. Africa Forest): Nok, Yoruba/Oyo, Benin, Igbo, Ashanti/Akan, Dahomey, Tiv

Region 12 (Central Africa): Kongo Kingdom, Luba Empire, Lunda, Teke, Mangbetu, equatorial forest peoples

Region 13 (E. Africa/Horn): Axum, Ethiopian Empire (Zagwe, Solomonic), Swahili city-states (Kilwa, Mombasa, Zanzibar), Somali sultanates, Buganda, Bunyoro, Rwanda, Burundi

Region 14 (Southern Africa): San/Bushmen, Khoikhoi, Great Zimbabwe, Mutapa, Rozwi, Zulu, Xhosa, Sotho, Tswana, Shona, Ndebele

- [ ] **Step 3: Create source stubs and update TRACKER.md**

- [ ] **Step 4: Commit**

```bash
git add regions/09-* regions/10-* regions/11-* regions/12-* regions/13-* regions/14-* sources/by-region/ TRACKER.md
git commit -m "Add Africa landscapes — Egypt, W. Africa Sahel/Forest, Central, East, Southern"
```

---

## Task 11: Skeleton L1 — Asia Landscapes (Regions 15-19)

**Files:**
- Create: `regions/15-south-asia/00-LANDSCAPE.md`
- Create: `regions/16-tibet-himalaya/00-LANDSCAPE.md`
- Create: `regions/17-east-asia/00-LANDSCAPE.md`
- Create: `regions/18-southeast-asia/00-LANDSCAPE.md`
- Create: `regions/19-central-inner-asia/00-LANDSCAPE.md`
- Create: `sources/by-region/` entries for each

- [ ] **Step 1: Create region directories**

```bash
mkdir -p regions/15-south-asia regions/16-tibet-himalaya regions/17-east-asia regions/18-southeast-asia regions/19-central-inner-asia
```

- [ ] **Step 2: Write 00-LANDSCAPE.md for each region**

Same template. Peoples from the spec:

Region 15 (South Asia): Indus Valley, Vedic, Maurya, Kushan, Gupta, Chola, Pallava, Rashtrakuta, Delhi Sultanate, Vijayanagara, Mughal, Maratha, Sikh, Rajput, Sri Lanka

Region 16 (Tibet/Himalaya): Tibetan Empire, Bhutan, Nepal (Licchavi, Malla, Shah), Ladakh, Sikkim

Region 17 (East Asia): Shang, Zhou, Qin, Han, Sui, Tang, Song, Yuan, Ming, Qing; Gojoseon, Goguryeo, Silla, Goryeo, Joseon; Yamato, Heian, Kamakura, Muromachi, Tokugawa; Ryukyu

Region 18 (Southeast Asia): Khmer/Angkor, Champa, Srivijaya, Majapahit, Dai Viet, Pagan/Burma, Ayutthaya/Siam, Lan Xang, Tondo, Sulu, Brunei

Region 19 (Central/Inner Asia): Scythians, Sarmatians, Xiongnu, Göktürks, Uyghurs, Khazars, Mongol Empire, Timurids, Uzbeks, Kazakhs

- [ ] **Step 3: Create source stubs and update TRACKER.md**

- [ ] **Step 4: Commit**

```bash
git add regions/15-* regions/16-* regions/17-* regions/18-* regions/19-* sources/by-region/ TRACKER.md
git commit -m "Add Asia landscapes — South, Tibet, East, Southeast, Central/Inner"
```

---

## Task 12: Skeleton L1 — Europe Landscapes (Regions 20-21)

**Files:**
- Create: `regions/20-western-christendom/00-LANDSCAPE.md`
- Create: `regions/21-northern-eastern-europe/00-LANDSCAPE.md`
- Create: `sources/by-region/` entries for each

- [ ] **Step 1: Create region directories**

```bash
mkdir -p regions/20-western-christendom regions/21-northern-eastern-europe
```

- [ ] **Step 2: Write 00-LANDSCAPE.md for each region**

Region 20 (Western Christendom): Celts, Carolingians/Franks, Anglo-Saxons, Holy Roman Empire, Papal States, Norman kingdoms, Iberian kingdoms, Italian city-states, Basques

Region 21 (N&E Europe): Norse/Vikings, Danes, Swedes, Icelanders, Kievan Rus, Muscovy/Russia, Polish-Lithuanian Commonwealth, Magyars, Finns, Sami, Balts, Bulgars, Serbs, Czechs, Cossacks

- [ ] **Step 3: Create source stubs and update TRACKER.md**

- [ ] **Step 4: Commit**

```bash
git add regions/20-* regions/21-* sources/by-region/ TRACKER.md
git commit -m "Add Europe landscapes — Western Christendom, Northern & Eastern"
```

---

## Task 13: Skeleton L1 — Oceania & Crossroads Landscapes (Regions 22-26)

**Files:**
- Create: `regions/22-oceania-pacific/00-LANDSCAPE.md`
- Create: `regions/23-americas-reborn/00-LANDSCAPE.md`
- Create: `regions/24-colonial-empires/00-LANDSCAPE.md`
- Create: `regions/25-diasporas/00-LANDSCAPE.md`
- Create: `regions/26-pacific-century/00-LANDSCAPE.md`
- Create: `sources/by-region/` entries for each

- [ ] **Step 1: Create region directories**

```bash
mkdir -p regions/22-oceania-pacific regions/23-americas-reborn regions/24-colonial-empires regions/25-diasporas regions/26-pacific-century
```

- [ ] **Step 2: Write 00-LANDSCAPE.md for each region**

Region 22 (Oceania): Aboriginal Australians, Lapita, Polynesian navigators (Tongan, Samoan, Hawaiian, Maori, Rapa Nui), Melanesian (PNG, Fiji), Micronesian

Region 23 (Americas Reborn): United States, Canada, Mexico, Brazil, Argentina, Haiti, Caribbean nations

Region 24 (Colonial Empires): British, French, Spanish, Dutch, Portuguese empires as world-systems

Region 25 (Diasporas): African diaspora, Jewish diaspora, Armenian diaspora, Romani people, Chinese overseas, Indian overseas

Region 26 (Pacific Century): Post-Meiji Japan, post-1911 China, modern Korea

- [ ] **Step 3: Create source stubs and update TRACKER.md**

- [ ] **Step 4: Commit**

```bash
git add regions/22-* regions/23-* regions/24-* regions/25-* regions/26-* sources/by-region/ TRACKER.md
git commit -m "Add Oceania & Crossroads landscapes — 5 regions, skeleton L1 complete"
```

---

## Task 14: Skeleton L2/L3 — Americas Peoples & Eras (Regions 1-4)

**Files:**
- Create: `regions/01-mesoamerica/<people>/00-OVERVIEW.md` for each people
- Create: `regions/02-andes/<people>/00-OVERVIEW.md` for each people
- Create: `regions/03-amazonia-caribbean/<people>/00-OVERVIEW.md` for each people
- Create: `regions/04-north-america/<people>/00-OVERVIEW.md` for each people

- [ ] **Step 1: Create people directories for all 4 regions**

For each people listed in the region's LANDSCAPE.md, create a directory:

```bash
# Example for Mesoamerica:
mkdir -p regions/01-mesoamerica/{olmec,maya,teotihuacan,zapotec,mixtec,toltec,aztec,purepecha,totonac}
```

Repeat for regions 2, 3, 4. Use lowercase, hyphenated directory names.

- [ ] **Step 2: Write 00-OVERVIEW.md for each people**

Follow the OVERVIEW template from `guides/TEMPLATES.md`. Each must contain:

1. **Header** — the people's own name for themselves (e.g., "Mexica" not just "Aztec")
2. **Introduction** — 1-2 paragraphs: who they were, in their own terms
3. **Their World** — ASCII map or diagram of territory at peak
4. **Their Time** — table with: Era (their name), Common Era dates, Key Theme. This is L3 — the eras enumerated but NOT yet built as directories.
5. **What Defined Them** — 3-5 themes from within their worldview
6. **The Chapters** — list of era chapters with one-line hooks

**Critical:** The eras must use the culture's OWN periodization (Style Principle #4). Research each culture's traditional era divisions. For cultures without written records, use archaeological period names that the scholarly community uses but frame them without Western bias.

**Target peoples count for these regions:**
- Region 1: ~10-12 peoples
- Region 2: ~10-12 peoples
- Region 3: ~8-10 peoples
- Region 4: ~12-15 peoples

- [ ] **Step 3: Update TRACKER.md**

Set Overviews status to "draft" for regions 1-4. Update peoples counts.

- [ ] **Step 4: Commit**

```bash
git add regions/01-* regions/02-* regions/03-* regions/04-* TRACKER.md
git commit -m "Add Americas peoples — ~40-50 overviews with eras enumerated"
```

---

## Task 15: Skeleton L2/L3 — Mediterranean & Middle East Peoples & Eras (Regions 5-8)

**Files:**
- Create: `regions/05-mediterranean/<people>/00-OVERVIEW.md` for each people
- Create: `regions/06-fertile-crescent/<people>/00-OVERVIEW.md` for each people
- Create: `regions/07-iran-persianate/<people>/00-OVERVIEW.md` for each people
- Create: `regions/08-islamic-heartlands/<people>/00-OVERVIEW.md` for each people

Same process as Task 14. Create directories, write overviews, enumerate eras.

**Target peoples count:**
- Region 5: ~10-12 peoples
- Region 6: ~8-10 peoples
- Region 7: ~8-10 peoples
- Region 8: ~12-15 peoples

- [ ] **Step 1-4:** Same pattern as Task 14.

- [ ] **Commit message:** `"Add Mediterranean & Middle East peoples — ~40-50 overviews with eras"`

---

## Task 16: Skeleton L2/L3 — Africa Peoples & Eras (Regions 9-14)

**Files:**
- Create: `regions/09-egypt-nile/<people>/00-OVERVIEW.md` for each people
- Create: `regions/10-west-africa-sahel/<people>/00-OVERVIEW.md` for each people
- Create: `regions/11-west-africa-forest/<people>/00-OVERVIEW.md` for each people
- Create: `regions/12-central-africa/<people>/00-OVERVIEW.md` for each people
- Create: `regions/13-east-africa-horn/<people>/00-OVERVIEW.md` for each people
- Create: `regions/14-southern-africa/<people>/00-OVERVIEW.md` for each people

Same process. Create directories, write overviews, enumerate eras.

**Target peoples count:**
- Region 9: ~6-8 peoples
- Region 10: ~8-10 peoples
- Region 11: ~8-10 peoples
- Region 12: ~6-8 peoples
- Region 13: ~10-12 peoples
- Region 14: ~10-12 peoples

**Special attention:** Africa is where the "present from within" principle is most at risk. Many of these cultures have been historically described through colonial frameworks. The overviews MUST use indigenous names, indigenous periodization where known, and frame each culture's sophistication without surprise. The Wade Davis and Achebe lenses are especially relevant here.

- [ ] **Step 1-4:** Same pattern as Task 14.

- [ ] **Commit message:** `"Add Africa peoples — ~50-60 overviews with eras"`

---

## Task 17: Skeleton L2/L3 — Asia Peoples & Eras (Regions 15-19)

**Files:**
- Create overviews for all peoples in regions 15-19

Same process.

**Target peoples count:**
- Region 15: ~15-18 peoples
- Region 16: ~5-6 peoples
- Region 17: ~15-20 peoples
- Region 18: ~10-12 peoples
- Region 19: ~10-12 peoples

**Special attention:** Region 17 (East Asia) is the largest region by people count. Chinese dynasties alone could be ~12-15 entries. Be disciplined about what constitutes a distinct "people" vs. a dynastic succession within one civilization. Korea and Japan each get multiple entries (periods/shogunates/kingdoms).

- [ ] **Step 1-4:** Same pattern as Task 14.

- [ ] **Commit message:** `"Add Asia peoples — ~55-70 overviews with eras"`

---

## Task 18: Skeleton L2/L3 — Europe Peoples & Eras (Regions 20-21)

**Files:**
- Create overviews for all peoples in regions 20-21

Same process.

**Target peoples count:**
- Region 20: ~12-15 peoples
- Region 21: ~12-15 peoples

- [ ] **Step 1-4:** Same pattern as Task 14.

- [ ] **Commit message:** `"Add Europe peoples — ~25-30 overviews with eras"`

---

## Task 19: Skeleton L2/L3 — Oceania & Crossroads Peoples & Eras (Regions 22-26)

**Files:**
- Create overviews for all peoples in regions 22-26

Same process.

**Target peoples count:**
- Region 22: ~10-12 peoples
- Region 23: ~10-12 peoples
- Region 24: ~5-7 peoples
- Region 25: ~6-8 peoples
- Region 26: ~3-5 peoples

**Special attention:** The Crossroads regions (23-26) are newer civilizations born from collision. Their overviews should acknowledge their hybrid origins and frame their stories from within their own emerging identities — the United States told as the United States sees itself, not as a footnote to British colonial history.

- [ ] **Step 1-4:** Same pattern as Task 14.

- [ ] **Commit message:** `"Add Oceania & Crossroads peoples — ~35-45 overviews, skeleton L2/L3 complete"`

---

## Task 20: Final Skeleton Verification & MkDocs Nav Update

**Files:**
- Modify: `.mkdocs/mkdocs.yml` (update nav with all peoples)
- Modify: `TRACKER.md` (final status update)

- [ ] **Step 1: Count and verify**

```bash
# Count all LANDSCAPE files (should be 26)
find regions/ -name "00-LANDSCAPE.md" | wc -l

# Count all OVERVIEW files (should be ~250-300)
find regions/ -name "00-OVERVIEW.md" | wc -l

# List any regions missing a LANDSCAPE
for d in regions/*/; do
  if [ ! -f "$d/00-LANDSCAPE.md" ]; then
    echo "MISSING LANDSCAPE: $d"
  fi
done

# List any people directories missing an OVERVIEW
for d in regions/*/*/; do
  if [ ! -f "$d/00-OVERVIEW.md" ]; then
    echo "MISSING OVERVIEW: $d"
  fi
done
```

Fix any gaps.

- [ ] **Step 2: Update MkDocs nav**

Expand the nav in `.mkdocs/mkdocs.yml` to include all peoples under each region. The nav should be hierarchical:

```yaml
- Mesoamerica:
  - Landscape: regions/01-mesoamerica/00-LANDSCAPE.md
  - Olmec: regions/01-mesoamerica/olmec/00-OVERVIEW.md
  - Maya: regions/01-mesoamerica/maya/00-OVERVIEW.md
  - ...
```

- [ ] **Step 3: Verify MkDocs builds**

```bash
cd .mkdocs && python -m mkdocs build -f mkdocs.yml
```

Fix any build errors (broken links, missing files).

- [ ] **Step 4: Update TRACKER.md with final counts**

- [ ] **Step 5: Commit**

```bash
git add .mkdocs/mkdocs.yml TRACKER.md
git commit -m "Complete Phase 1 skeleton — 26 regions, ~250-300 peoples, eras enumerated"
```

---

## Task 21: Select Anchor Region & Plan Phase 2

**Files:**
- Create: `docs/superpowers/plans/2026-XX-XX-phase2-anchor-<region>.md`

- [ ] **Step 1: Review the skeleton and select anchor**

Consider which region/people/era to anchor on. Criteria from the spec:
- Richest source material
- Most distinctive voice (stress-tests the "present from within" principle)
- Enough complexity to validate the full pipeline

Recommend 3 options to the user with rationale. Wait for selection.

- [ ] **Step 2: Write Phase 2 plan**

Once anchor is selected, write a detailed Phase 2 implementation plan for taking that region/people/era through all 11 pipeline stages:
1. OPENING — write the hook scene
2. GATE-1 — score against The Gate
3. PANEL-1 — all 5 voices review
4. NOTES — production bible
5. PANEL-2 — target weak areas
6. FIXES — apply feedback
7. WRITE — full chapter
8. GATE-2 — score against The Chronicle
9. CLEAN — editorial pass (E-1, E-2, E-3)
10. BOARD — create 2-3 board reviewers for this culture, run review
11. FINAL — apply fixes, lock

Also create the first 2-3 board reviewer roles in `.craft/roles/board/` specific to the anchor culture.

- [ ] **Step 3: Commit the Phase 2 plan**

---

## Execution Notes

**Tasks 1-7** (infrastructure) are sequential — each builds on the previous.

**Tasks 8-13** (L1 landscapes) are independent and can run in parallel via subagents — one agent per task, each handling a geographic cluster.

**Tasks 14-19** (L2/L3 peoples) are independent and can run in parallel, but each depends on its corresponding L1 task completing first (need the LANDSCAPE to know which peoples to enumerate):
- Task 14 depends on Task 8
- Task 15 depends on Task 9
- Task 16 depends on Task 10
- Task 17 depends on Task 11
- Task 18 depends on Task 12
- Task 19 depends on Task 13

**Task 20** (verification) depends on all L2/L3 tasks completing.

**Task 21** (anchor selection) depends on Task 20.

```
Tasks 1-7 (sequential)
    │
    ▼
Tasks 8-13 (parallel — L1 landscapes)
    │
    ▼
Tasks 14-19 (parallel — L2/L3 peoples, each depends on its L1)
    │
    ▼
Task 20 (verification)
    │
    ▼
Task 21 (anchor selection → Phase 2 plan)
```

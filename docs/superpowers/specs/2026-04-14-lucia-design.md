# LUCIA — The Human Chronicle

## Design Specification

**Date:** 2026-04-14
**Author:** Giovanni Della-Libera + Claude Opus 4.6
**Status:** Final — approved, ready for implementation planning

---

## 1. Project Identity

- **Codename:** LUCIA (after LUCY, Giovanni's German Shorthaired Pointer)
- **Mission:** Tell the story of every human culture and group in a real and objective way, using storytelling to tell their story from inside their own worldview, without pre- or post-judging them against different historical standards.
- **Sibling projects:** MAXIM (reference — encyclopedia), FELIX/RMM (rmm — research + storytelling)
- **Relationship:** Fully independent. Own CLAUDE.md, style guide, scoring, everything. Borrows patterns and skills from siblings. References MAXIM and FELIX as sources among many.
- **Tech stack:** MkDocs + Material theme, Markdown content files, consistent with MAXIM and RMM.
- **Repository:** https://github.com/giodl_microsoft/chronicle.git

---

## 2. Editorial Philosophy

### 2.1 Present From Within

Tell each culture's story from inside their own worldview. The text never steps outside to judge — it trusts the reader. The Aztecs tell the Aztec story. The Mongols tell the Mongol story.

### 2.2 No Historical Judgment

Don't pre- or post-judge cultures against different historical standards. Even periodization belongs to the culture — their era names, not Western academic labels. Rome's "Republic," not "Classical Antiquity." The Inca's "Tawantinsuyu," not "Pre-Columbian Empire."

### 2.3 Story-First, Reference-Second

Each chapter opens with a scene — a real person, a real moment. The era's context emerges from the narrative, not the other way around. Reference material (timelines, maps, key figures) supports the story but doesn't lead it.

### 2.4 Evolving Quality

The scoring rubric is a learning system, not just a gate. When an agent produces something exceptional that goes beyond the rubric, capture what made it special, update the rubric to recognize that quality, and raise the bar for everyone. The rubric evolves upward.

---

## 3. LUCY's Layer

LUCY is a German Shorthaired Pointer, 10 years old. Smart, observant (watches rabbits all day), not shy to say when she's hungry, nice cuddles, needs to go through the gates first.

LUCY's personality infuses the **infrastructure** — preface, tools, scoring, skills, CLAUDE.md — NOT the culture content.

| Trait | Where It Appears |
|-------|-----------------|
| Smart, observant (watches rabbits all day) | Patient, thorough review process |
| Not shy to say when she's hungry | Direct feedback in scoring, no-nonsense panel |
| Nice cuddles | Warm, approachable preface and guides |
| Needs to go through gates first | Quality gates (The Gate rubric), pipeline discipline |

**Where LUCY lives:** Preface, tools, skills, CLAUDE.md, scoring system, style guide.
**Where LUCY is silent:** Culture chapters. Cultures speak for themselves.

---

## 4. Architecture: The Layered Chronicle

### 4.1 The 5-Level Tree

```
L1  Region          Geographic/cultural area with deep historical interaction
L2  People          Named civilization, kingdom, empire, or cultural group
L3  Era             Period of time as the culture defined it (their terms)
L4  Chapter files   opening.md, chapter.md, notes.md, figures.md
L5  Review rounds   reviews/R1-*.md, R2-*.md, BOARD-*.md
```

### 4.2 Directory Structure

```
chronicle/
├── CLAUDE.md                        ← LUCY's house rules
├── README.md                        ← Project entry point
├── index.md                         ← Navigation hub
├── TRACKER.md                       ← Status dashboard
├── regions/
│   ├── <region>/
│   │   ├── 00-LANDSCAPE.md         ← ASCII map + peoples + timeline
│   │   ├── SOURCES.md              ← Region-level references
│   │   ├── <people>/
│   │   │   ├── 00-OVERVIEW.md      ← Who they were, their eras, key themes
│   │   │   ├── SOURCES.md          ← Culture-specific references
│   │   │   ├── eras/
│   │   │   │   ├── 01-<era-name>/
│   │   │   │   │   ├── opening.md  ← Hook scene (~800 words)
│   │   │   │   │   ├── chapter.md  ← Full narrative (~5000 words)
│   │   │   │   │   ├── notes.md    ← Production bible
│   │   │   │   │   ├── figures.md  ← Leaders & people of this era
│   │   │   │   │   └── reviews/
│   │   │   │   │       ├── R1-*.md
│   │   │   │   │       ├── R2-*.md
│   │   │   │   │       └── BOARD-*.md
│   │   │   │   ├── 02-<era-name>/
│   │   │   │   └── ...
├── scoring/
│   ├── RUBRIC.md                    ← The Gate (30pts) + Chronicle (60pts)
│   ├── INNOVATIONS.md               ← Innovation log + rubric evolution
│   └── TARGETS.md                   ← Score targets and manuscript means
├── panel/
│   ├── tuchman.md                   ← Barbara Tuchman profile
│   ├── ibn-khaldun.md               ← Ibn Khaldun profile
│   ├── achebe.md                    ← Chinua Achebe profile
│   ├── davis.md                     ← Wade Davis profile
│   └── kapuscinski.md               ← Ryszard Kapuściński profile
├── sources/
│   ├── MASTER.md                    ← Global source registry
│   ├── ACQUISITION.md               ← Sources needed but not yet acquired
│   └── by-region/
│       ├── mesoamerica.md
│       └── ...
├── guides/
│   ├── STYLE-GUIDE.md               ← 13 style principles + mechanical rules
│   ├── TEMPLATES.md                 ← LANDSCAPE and OVERVIEW templates
│   ├── PIPELINE.md                  ← 11-stage chapter pipeline
│   └── HOW-TO-WRITE-A-CHAPTER.md   ← End-to-end guide for chapter authors
├── .mkdocs/
│   └── mkdocs.yml                   ← MkDocs configuration
└── docs/
    └── superpowers/
        └── specs/
            └── 2026-04-14-lucia-design.md  ← This document
```

### 4.3 Phasing Strategy

```
Phase 1:  Skeleton — full tree, 3 levels deep
          (Region → People → Eras listed)
          All 26 regions, ~250-300 peoples enumerated, eras named

Phase 2:  Anchor subtree — pick 1 region, go full 5 levels deep
          (Region → People → Era → Chapter → Reviews)
          Validate format, voice, rubric, panel, pipeline

Phase 3:  Refine skeleton based on anchor learnings
          Small fixes to the L1-L3 structure
          Then deepen 2 more levels across remaining regions
```

---

## 5. The 26 Regions

Stress-tested against 140+ cultures. 79% land with zero ambiguity; remaining cases solved via cross-references. No homeless cultures.

### 5.1 The Ancient & Living World (22 regions)

| #  | Region | Key Peoples (sample) | ~L2 |
|----|--------|---------------------|-----|
| 1  | **Mesoamerica** | Olmec, Maya, Teotihuacan, Zapotec, Mixtec, Toltec, Aztec/Mexica, Purépecha, Totonac | 10-12 |
| 2  | **Andes & Western South America** | Chavín, Moche, Nazca, Tiwanaku, Wari, Chimú, Inca, Muisca, Mapuche | 10-12 |
| 3  | **Amazonia, Caribbean & Lowland South America** | Taino, Carib, Arawak, Tupí-Guaraní, Marajoara, Kuikuro, Yanomami | 8-10 |
| 4  | **North America** | Mississippian/Cahokia, Haudenosaunee, Cherokee, Creek, Comanche, Lakota, Pueblo, Navajo, Haida/Tlingit, Cree, Anishinaabe, Inuit | 12-15 |
| 5  | **Mediterranean Classical World** | Minoan, Mycenaean, Phoenician, Greek city-states, Etruscan, Roman Republic/Empire, Carthage, Byzantine Empire | 10-12 |
| 6  | **Fertile Crescent & Mesopotamia** | Sumer, Akkad, Babylon, Assyria, Mitanni, Hittites, Urartu, Arameans | 8-10 |
| 7  | **Iran & the Persianate World** | Elam, Achaemenid Persia, Parthia, Sassanid Empire, Samanids, Safavids, Qajar, Kurdish dynasties, Durrani/Afghan | 8-10 |
| 8  | **The Islamic Heartlands** | Pre-Islamic Arabian tribes, Rashidun, Umayyad, Abbasid, Fatimid, Ayyubid, Mamluk, Seljuks of Rum, Ottoman Empire, Berber/Amazigh, Almoravids, Almohads, Barbary States | 12-15 |
| 9  | **Egypt & the Nile Valley** | Predynastic, Old Kingdom, Middle Kingdom, New Kingdom, Ptolemaic, Roman Egypt, Coptic, Kush, Meroe | 6-8 |
| 10 | **West African Sahel & Savanna** | Ghana Empire, Mali, Songhai, Kanem-Bornu, Hausa city-states, Fulani, Wolof, Soninke | 8-10 |
| 11 | **West African Forest & Guinea Coast** | Nok, Yoruba/Oyo, Benin, Igbo, Ashanti/Akan, Dahomey, Tiv | 8-10 |
| 12 | **Central Africa & Kongo World** | Kongo Kingdom, Luba Empire, Lunda, Teke, Mangbetu, equatorial forest peoples | 6-8 |
| 13 | **East Africa, Horn & Swahili World** | Axum, Ethiopian Empire (Zagwe, Solomonic), Swahili city-states (Kilwa, Mombasa, Zanzibar), Somali sultanates, Buganda, Bunyoro, Rwanda, Burundi | 10-12 |
| 14 | **Southern Africa** | San/Bushmen, Khoikhoi, Great Zimbabwe, Mutapa, Rozwi, Zulu, Xhosa, Sotho, Tswana, Shona, Ndebele | 10-12 |
| 15 | **South Asia (Indic World)** | Indus Valley, Vedic, Maurya, Kushan, Gupta, Chola, Pallava, Rashtrakuta, Delhi Sultanate, Vijayanagara, Mughal, Maratha, Sikh, Rajput, Sri Lanka | 15-18 |
| 16 | **Tibet & the Himalayan World** | Tibetan Empire, Bhutan, Nepal (Licchavi, Malla, Shah), Ladakh, Sikkim | 5-6 |
| 17 | **East Asia (Sinographic Sphere)** | Shang, Zhou, Qin, Han, Sui, Tang, Song, Yuan, Ming, Qing; Gojoseon, Goguryeo, Silla, Goryeo, Joseon; Yamato, Heian, Kamakura, Muromachi, Tokugawa; Ryukyu | 15-20 |
| 18 | **Southeast Asia** | Khmer/Angkor, Champa, Srivijaya, Majapahit, Dai Viet, Pagan/Burma, Ayutthaya/Siam, Lan Xang, Tondo, Sulu, Brunei | 10-12 |
| 19 | **Central & Inner Asia (Steppe World)** | Scythians, Sarmatians, Xiongnu, Göktürks, Uyghurs, Khazars, Mongol Empire, Timurids, Uzbeks, Kazakhs | 10-12 |
| 20 | **Western Christendom** | Celts, Carolingians/Franks, Anglo-Saxons, Holy Roman Empire, Papal States, Norman kingdoms, Iberian kingdoms, Italian city-states, Basques | 12-15 |
| 21 | **Northern & Eastern Europe** | Norse/Vikings, Danes, Swedes, Icelanders, Kievan Rus, Muscovy/Russia, Polish-Lithuanian Commonwealth, Magyars, Finns, Sami, Balts, Bulgars, Serbs, Czechs, Cossacks | 12-15 |
| 22 | **Oceania & the Pacific World** | Aboriginal Australians, Lapita, Polynesian navigators (Tongan, Samoan, Hawaiian, Maori, Rapa Nui), Melanesian (Papua New Guinea, Fiji), Micronesian | 10-12 |

### 5.2 The Crossroads (4 regions — born from collision)

| #  | Region | Key Peoples (sample) | ~L2 |
|----|--------|---------------------|-----|
| 23 | **The Americas Reborn** | United States, Canada, Mexico, Brazil, Argentina, Haiti, Caribbean nations | 10-12 |
| 24 | **Colonial Empires & Systems** | British, French, Spanish, Dutch, Portuguese empires as world-systems | 5-7 |
| 25 | **Diasporas & Dispersed Peoples** | African diaspora, Jewish diaspora, Armenian diaspora, Romani people, Chinese overseas, Indian overseas | 6-8 |
| 26 | **The Pacific Century (Modern East Asia)** | Post-Meiji Japan, post-1911 China, modern Korea | 3-5 |

**Total: 26 regions, ~250-300 peoples (L2), each with their own eras (L3)**

### 5.3 Cross-Reference Index

| Culture | Primary Region | Cross-ref to |
|---------|---------------|-------------|
| Ottoman Empire | 8 (Islamic Heartlands) | 5, 21 |
| Crusaders | 20 (Christendom) | 8 |
| Phoenicians | 5 (Mediterranean) | 6 |
| Caribbean Pirates | 24 (Colonial) | 23 |
| Visigoths/Goths | 20 (Christendom) | 5 |
| Soviet Union | 21 (N&E Europe) | 19 |
| Silk Road | thematic | 7, 15, 17, 19 |
| Mongol conquests | 19 (Steppe) | 7, 8, 15, 17, 21 |
| Kurds | 7 (Persianate) | 6, 8 |
| Armenians | 7 (Persianate) | 25 (diaspora) |
| Mughal Empire | 15 (South Asia) | 8 |

---

## 6. Scoring & Pipeline

### 6.1 The Panel — 5 Reviewer Voices

| Voice | Lens | Checks For |
|-------|------|-----------|
| **Barbara Tuchman** | Narrative craft | Pacing, scene construction, arc. Is this a page-turner? Does the reader feel present? |
| **Ibn Khaldun** | Historical systems | Patterns, causation, cycles. Does the narrative understand WHY, not just WHAT? |
| **Chinua Achebe** | Cultural voice | Dignity, authenticity, ownership. Does this culture speak in its own voice? |
| **Wade Davis** | Anthropological wonder | Hidden condescension, worldview depth. Is every culture treated as equally sophisticated? |
| **Ryszard Kapuściński** | Sensory immersion | Heat, smell, sound, texture. Can you feel where you are? |

### 6.2 Opening Rubric — The Gate (30 points)

| Dimension | Points | Question |
|-----------|--------|----------|
| **Scene** | 0-5 | Does it open in a specific moment — a person, a place, a heartbeat of time? |
| **World** | 0-5 | Does the culture's own reality emerge naturally from the scene — cosmology, values, logic — without being explained? |
| **Honesty** | 0-5 | Free from outside judgment? No "primitive," no "advanced," no anachronistic morality, no romanticization, no demonization? |
| **Texture** | 0-5 | Sensory detail, material culture, landscape — can you feel where you are? Smell it? Hear it? |
| **Voice** | 0-5 | Does the prose rhythm belong to this story? Not a textbook, not a novel, not a lecture — this culture's own weight and cadence? |
| **Pull** | 0-5 | Does it earn your desire to keep reading? Not a cliffhanger trick — genuine narrative momentum? |

### 6.3 Full Chapter Rubric — The Chronicle (60 points)

| Dimension | Points | Question |
|-----------|--------|----------|
| **Immersion** | 0-10 | Does the reader live inside this culture's world for the whole chapter? No jolts back to a modern lens? |
| **Evidence** | 0-10 | Specific stories, named people, real events — historically grounded? Sources would hold up? |
| **Progression** | 0-10 | Does the era's arc emerge? Does it build — each section earns its place, nothing repeats? |
| **Figures** | 0-10 | Are the leaders and people vivid, dimensional, real? Not archetypes, not cardboard — human beings? |
| **Voice** | 0-10 | Consistent tone that belongs to this culture's story throughout? No register shifts into academic or modern commentary? |
| **Landing** | 0-10 | Does it close at the right weight — neither abrupt nor overwrought? Does the reader sit with it? |

### 6.4 Scoring Targets

| Metric | Target |
|--------|--------|
| Opening (The Gate) | 24+ / 30 (80%) |
| Full Chapter (The Chronicle) | 48+ / 60 (80%) |
| Combined per era | 72+ / 90 (80%) |
| Manuscript mean | 75+ / 90 (83%) |

### 6.5 The Innovation Engine

When a scorer notices something exceptional that the rubric didn't anticipate:

1. **Flag** it as an Innovation
2. **Log** to `scoring/INNOVATIONS.md` (what, why, source chapter)
3. After **2+ innovations** in the same category, propose a **Rubric Amendment**
4. Review and approve the amendment
5. **Rubric version increments** (v1.0 → v1.1 → v1.2)
6. New bar applies **forward only** — old scores not retroactively changed

Each innovation log entry records: source chapter, date, which rubric dimension, description of the technique, why it works, and proposed rubric impact.

### 6.6 The Pipeline — 11 Stages

**Pre-Pipeline (skeleton work, per region/people):**

| Stage | Deliverable |
|-------|------------|
| **LANDSCAPE** | Region's `00-LANDSCAPE.md` — ASCII map, peoples listed, timeline |
| **OVERVIEW** | People's `00-OVERVIEW.md` — who they were, their eras, key themes, told from within |

**Chapter Pipeline (per era — L3 through L5):**

| # | Stage | Deliverable |
|---|-------|------------|
| 1 | **OPENING** | Write `opening.md` (~800 words). Hook scene. Real person, real place, real moment. |
| 2 | **GATE-1** | Score opening against The Gate (30 pts). Target: 24+/30. |
| 3 | **PANEL-1** | Panel reads opening, all 5 voices provide feedback. |
| 4 | **NOTES** | Write `notes.md` (production bible). Structure, sources, key figures, narrative arc, what each section must accomplish. |
| 5 | **PANEL-2** | Panel reviews notes, targets weak areas. Focus on gaps the opening revealed. |
| 6 | **FIXES** | Apply Panel-1 + Panel-2 feedback. Revise opening if needed. |
| 7 | **WRITE** | Write `chapter.md` (~5000 words) from notes. Write `figures.md` (leaders & people of this era). |
| 8 | **GATE-2** | Score chapter against The Chronicle (60 pts). Target: 48+/60. Flag any innovations. |
| 9 | **CLEAN** | Editorial cleanup: judgment check, voice consistency, sensory balance, em-dash audit (≤8), source verification. |
| 10 | **BOARD** | 2-3 domain experts for this specific culture give final assessment. |
| 11 | **FINAL** | Apply board fixes, lock chapter. Update `scoring/INNOVATIONS.md` if applicable. |

**The Anchor Rule:** Before scaling to any other region, pick 1 region → 1 people → 1 era. Run it through ALL 11 stages. Validate the format, the voice, the rubric, the panel. Only then: scale. The anchor region/people/era will be chosen at the start of Phase 2 based on which culture has the richest source material and most distinctive voice to stress-test the system.

---

## 7. Style Guide

### 7.1 The Achebe Test

Every sentence must pass: Could a thoughtful member of this culture read this and feel their story was told with dignity — from inside — regardless of whether they agreed with every detail?

### 7.2 The 13 Principles

| # | Principle | Rule |
|---|-----------|------|
| 1 | **Inside, Not Above** | The reader stands inside the culture, not above it looking down. Write as if the reader IS there. |
| 2 | **The World Before the Label** | Describe the practice/belief/moment BEFORE naming it with an academic term. Let the reader experience it first. |
| 3 | **No Time Travelers** | No modern concepts projected backward. The Inca did not have "supply chain management." Use the culture's own concepts. |
| 4 | **Their Calendar, Their Seasons** | Use the culture's own time markers first. Provide common-era dates in parentheses for orientation. |
| 5 | **Names in Their Language** | Use the culture's own names first. Tenochtitlan, not "the Aztec capital." Tawantinsuyu, not "the Inca Empire." |
| 6 | **Earned Emotion** | The text does not tell you how to feel. Evidence and story create the feeling. Never: "Tragically, the empire fell." |
| 7 | **No Verdicts** | The text never says "this was wrong/justified/inevitable." It shows what happened and why. The reader is the jury. |
| 8 | **People First, Systems Second** | Every era is told through the people who lived it. Start with a person. Systems emerge from what people did and why. |
| 9 | **Trust the Reader** | Do not re-explain what a scene already showed. If the narrative conveyed it, don't then write "This illustrates..." |
| 10 | **Simple When It Matters** | Complex sentence structures undercut emotional moments. When the weight is heavy, the prose should be plain. |
| 11 | **Sensory Ground** | Every page needs at least one sensory anchor — sight, sound, smell, touch. History happened in physical places to people with bodies. |
| 12 | **Rhythm Belongs to the Story** | Prose rhythm should reflect the culture and the moment. A steppe chapter moves fast. A Heian court chapter unfolds slowly. |
| 13 | **Honest Uncertainty** | When the record is thin, say so. "What we know..." is more compelling than false certainty. |

### 7.3 Mechanical Rules

| Rule | Value |
|------|-------|
| Opening length | ~800 words |
| Full chapter length | 4,500 – 5,500 words |
| Figures section length | 500 – 1,500 words |
| Em-dash limit (opening) | ≤ 5 |
| Em-dash limit (chapter) | ≤ 8 |

### 7.4 Forbidden Words (in culture chapters)

| Word/Phrase | Why | Use Instead |
|-------------|-----|-------------|
| "primitive" | Never, under any circumstances | Describe what they built |
| "advanced" | Implies a ladder | Describe what they built |
| "civilization" (as compliment) | Don't say "they achieved civilization" | Use only if the culture used it of themselves |
| "discovered by [Europeans]" | They already knew they existed | "encountered," or describe the meeting |
| "the New World" | Only new to one group | Use specific geographic names |
| "tribe" | Unless their self-designation | "people," "nation," "group," or their own term |
| "Dark Ages" | Eurocentric | Name the specific period and place |

### 7.5 Forbidden Framings

| Framing | Why |
|---------|-----|
| "While Europe was doing X, these people were doing Y" | Implies Europe is the main timeline |
| "Before contact with the West, they had already..." | Implies the West is the catalyst |
| "They were remarkably sophisticated for..." | "Remarkably" reveals surprise, which reveals assumption |

### 7.6 The OVERVIEW Template (L2 — per people)

```markdown
# [People's own name for themselves]

[1-2 paragraphs: Who they were, in their own terms.]

## Their World
[ASCII map or diagram of territory/sphere at peak]

## Their Time
| Era | Their Name | Common Era | Key Theme |
|-----|-----------|------------|-----------|

## What Defined Them
[3-5 themes from within — not "achievements" for a Western audience]

## The Chapters
[List of era chapters with one-line hooks]
```

### 7.7 The LANDSCAPE Template (L1 — per region)

```markdown
# [Region Name]

[1-2 paragraphs: What makes this a region.]

## The Land
[ASCII map showing peoples, geography, key features]

## The Peoples
| People | Approximate Span | Key Theme |
|--------|------------------|-----------|

## How They Connect
[Interactions — trade, war, cultural exchange, migration]

## Cross-References
[Cultures from other regions that interact significantly]
```

---

## 8. Source Management

### 8.1 Source Tiers

| Tier | Type | Use |
|------|------|-----|
| 1 | **Primary sources** | Original texts, inscriptions, oral traditions recorded by the culture. Gold standard. |
| 2 | **Academic sources** | Peer-reviewed journals, university press monographs, archaeological reports. |
| 3 | **Scholarly secondary** | Well-sourced books by recognized historians, museum publications, institutional pages. |
| 4 | **Reference** | Wikipedia (for dates/coordinates/basic facts only, not interpretive claims). Always prefer underlying academic papers. |
| 5 | **Do not use** | Grokipedia, Wikipedia mirrors, pop history YouTube transcripts, unsourced blogs, unverified AI-generated content. |

MAXIM and FELIX are Tier 3 — useful for orientation, not authoritative for historical claims. Verify independently.

### 8.2 Source File Structure

```
sources/
├── MASTER.md              ← Global source registry
├── ACQUISITION.md         ← Sources needed but not yet acquired
└── by-region/
    ├── mesoamerica.md     ← Region-level bibliography
    └── ...

regions/<region>/<people>/
└── SOURCES.md             ← Culture-specific sources
```

### 8.3 Citation Style

Inline, natural — sources named in the text, full citations in SOURCES.md:

```markdown
Gary Urton's work at Harvard has shown that the knotted cords
encoded narrative — perhaps even a syllabic writing system —
though this remains debated among Andeanists.
```

### 8.4 Source Tracking Per Chapter

Each era's `notes.md` includes a sources section with Primary, Academic, and Needed (ACQUISITION) categories. Needed items feed into `sources/ACQUISITION.md` as a global punchlist.

---

## 9. Decisions Log

| Question | Answer | Rationale |
|----------|--------|-----------|
| Culture unit | Nested (region → people) | Rich history needs nesting |
| Reading experience | Story-first, reference-second | Captivating reading is the goal |
| Historical judgment | Present from within | Once you judge, you pick a lane |
| LUCY's role | Mascot and brand (infrastructure only) | Cultures speak for themselves |
| Time slicing | Natural eras (culture's own terms) | Consistent with "present from within" |
| Scope approach | Full skeleton (3 levels) → anchor (5 levels) → refine → deepen | Prevents drift, validates quality |
| Tech stack | MkDocs + Material | Consistent with MAXIM and RMM |
| Review system | Formal scoring + evolving rubric | Only way to get quality; innovation raises the bar |
| Relationship to siblings | Fully independent, steal patterns | Long-lasting artifacts stand alone |
| Region count | 26 (22 ancient/living + 4 crossroads) | Stress-tested against 140 cultures, no homeless groups |
| Region 8 expansion | Islamic Heartlands (absorbs Ottoman, Berber, Maghreb) | Closed the single biggest structural gap |
| Panel | Tuchman, Ibn Khaldun, Achebe, Davis, Kapuściński | Five complementary lenses covering craft, systems, voice, wonder, immersion |
| Rubric | The Gate (30pts) + The Chronicle (60pts) = 90 total | Matched RMM's scale, adapted dimensions for historical narrative |
| Pipeline | 11 stages with anchor-first validation | Proven in RMM, adapted for LUCIA's needs |

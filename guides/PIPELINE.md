# LUCIA Pipeline — 11-Stage Chapter Process

Every chapter in The Human Chronicle passes through the same 11 stages.
No shortcuts. No skipping. The pipeline exists because quality at this
scale doesn't happen by accident — it happens by discipline.

---

## The Full Flow

```
Pre-Pipeline
  LANDSCAPE ──► OVERVIEW
                    │
                    ▼
Chapter Pipeline (per era)
                    │
    ┌───────────────┴───────────────────────────────┐
    │                                               │
    ▼                                               │
  OPENING                                          │
    │                                              │
    ▼                                              │
  GATE-1 ──[fail: revise]──────────────────────────┤
    │                                              │
    ▼                                              │
  PANEL-1                                          │
    │                                              │
    ▼                                              │
  NOTES                                            │
    │                                              │
    ▼                                              │
  PANEL-2                                          │
    │                                              │
    ▼                                              │
  FIXES                                            │
    │                                              │
    ▼                                              │
  WRITE                                            │
    │                                              │
    ▼                                              │
  GATE-2 ──[fail: revise]──────────────────────────┤
    │                                              │
    ▼                                              │
  CLEAN                                            │
    │                                              │
    ▼                                              │
  BOARD                                            │
    │                                              │
    ▼                                              │
  FINAL ◄──────────────────────────────────────────┘
```

Compact view:

```
OPENING → GATE-1 → PANEL-1 → NOTES → PANEL-2 → FIXES → WRITE → GATE-2 → CLEAN → BOARD → FINAL
```

---

## The Anchor Rule

**Before scaling to any second region: pick 1 region → 1 people → 1 era.
Run it through ALL 11 stages. Validate everything. Only then: scale.**

The anchor era exists to stress-test the entire system — the rubric, the
panel, the pipeline, the voice, the format — before hundreds of chapters
depend on assumptions that might be wrong.

Choose the anchor where you have:
- Rich, well-documented source material
- A distinctive cultural voice that will stress-test the "present from within" rule
- Enough named individuals to build scenes around

The anchor teaches you what the system doesn't know yet.

---

## Pre-Pipeline: Skeleton Stages

These happen before any chapter pipeline starts. They establish the
geographic and cultural context that every era chapter depends on.

### L1 — LANDSCAPE (per region)

| | |
|---|---|
| **Artifact** | `regions/<region>/00-LANDSCAPE.md` |
| **Who** | Author |
| **Entry** | Region selected, source survey complete |
| **Exit** | All peoples listed with approximate spans; ASCII map present; "How They Connect" drafted; cross-references noted |
| **Target** | Complete coverage — no people in the region unaccounted for |

The LANDSCAPE is a reference document, not narrative. It is the map you
hang on the wall before you start writing any chapter.

### L2 — OVERVIEW (per people)

| | |
|---|---|
| **Artifact** | `regions/<region>/<people>/00-OVERVIEW.md` |
| **Who** | Author |
| **Entry** | LANDSCAPE complete; people's SOURCES.md seeded |
| **Exit** | All eras listed with their own names; key themes identified from within; "The Chapters" section lists all era hooks |
| **Target** | Complete era list; voice is the culture's own, not an outsider's survey |

The OVERVIEW is written from inside. Not "the Aztecs were..." but Mexica
understood through their own categories, their own time markers, their
own terms for themselves.

---

## The 11-Stage Chapter Pipeline

Each stage below covers a single era (L3) and produces the L4–L5 artifacts
for that era's directory.

---

### Stage 1 — OPENING

| | |
|---|---|
| **Artifact** | `opening.md` (~800 words) |
| **Who** | Author |
| **Entry** | OVERVIEW complete; era identified; SOURCES.md has at least primary and academic sources for this era |
| **Exit** | A complete draft exists: one specific scene, one real person, one real moment, narrative pull established |
| **Target** | ~800 words; ≤5 em-dashes; person + place + moment + stakes all present |

The opening is the Gate. If you cannot hook the reader in 800 words, more
words will not fix it. Start with a person. Not "In the fifteenth century..."
Not "The empire was characterized by..." — a human being, placed, in a
specific moment, with something at stake.

---

### Stage 2 — GATE-1

| | |
|---|---|
| **Artifact** | Gate scorecard (scored against The Gate rubric, 30 pts) |
| **Who** | Scorer (separate role from Author) |
| **Entry** | `opening.md` complete and committed |
| **Exit** | Score recorded; any dimension below 3/5 flagged for revision |
| **Target** | **24+ / 30 (80%)** |

The Gate rubric scores six dimensions, 0-5 each:

| Dimension | Question |
|-----------|----------|
| **Scene** | Does it open in a specific moment — a person, a place, a heartbeat of time? |
| **World** | Does the culture's own reality emerge naturally — cosmology, values, logic — without being explained? |
| **Honesty** | Free from outside judgment? No primitive, no advanced, no anachronistic morality, no romanticization? |
| **Texture** | Sensory detail, material culture, landscape — can you feel where you are? |
| **Voice** | Does the prose rhythm belong to this story? Not textbook, not novel — this culture's own weight? |
| **Pull** | Does it earn the desire to keep reading? Genuine narrative momentum, not a cliffhanger trick? |

If the opening scores below 24, it goes back. Revise and re-score before
proceeding. GATE-1 is a real gate — it does not wave things through.

---

### Stage 3 — PANEL-1

| | |
|---|---|
| **Artifact** | 5 review files: `reviews/R1-P1-tuchman.md`, `R1-P2-ibn-khaldun.md`, `R1-P3-achebe.md`, `R1-P4-davis.md`, `R1-P5-kapuscinski.md` |
| **Who** | All 5 panel voices (permanent reviewers — see `.craft/roles/panel/`) |
| **Entry** | GATE-1 passed (24+/30) |
| **Exit** | All 5 reviews complete with specific line references and "The question I'd push on" |
| **Target** | Qualitative feedback; no numerical scores from panel at this stage |

All five review every opening. No exceptions. The five voices create
productive friction:

- **Tuchman (P-1)** asks: Would a reader keep reading? Does the scene earn attention?
- **Ibn Khaldun (P-2)** asks: Is there explanatory depth, or just vivid surface?
- **Achebe (P-3)** asks: Does this culture own its own story, or has someone borrowed it?
- **Davis (P-4)** asks: Is every culture's knowledge system treated as equally sophisticated?
- **Kapuściński (P-5)** asks: Can you feel where you are? Are the people embodied?

The tensions between them are the point. An opening that satisfies all five
has survived real scrutiny.

---

### Stage 4 — NOTES

| | |
|---|---|
| **Artifact** | `notes.md` (production bible) |
| **Who** | Author |
| **Entry** | PANEL-1 reviews complete and read |
| **Exit** | All six sections present: sources, key figures, narrative arc, section plan, panel pressure points anticipated, open questions listed |
| **Target** | Enough to write the full chapter without returning to primary sources for structure; Panel-1 feedback visibly incorporated |

The notes.md is the production bible. It is not a draft — it is the plan
the draft will execute. It should answer: What is the story of this era?
Who are the human beings carrying it? What does each section accomplish?
What will the panel push on when they read the full chapter?

---

### Stage 5 — PANEL-2

| | |
|---|---|
| **Artifact** | Targeted review files: `reviews/R2-P*.md` (focused, not full reviews) |
| **Who** | Panel voices most relevant to the gaps revealed by PANEL-1 |
| **Entry** | `notes.md` complete |
| **Exit** | Gaps from PANEL-1 addressed in notes; structural weaknesses identified before full draft begins |
| **Target** | Focused feedback on weak areas — particularly: gaps in causal reasoning, cultural voice risks, and sensory plan |

PANEL-2 is sharper than PANEL-1 because the weaknesses are now visible.
The panel is not re-reading the opening — they are reading the production
bible and saying: with this plan, what will still go wrong?

---

### Stage 6 — FIXES

| | |
|---|---|
| **Artifact** | Revised `opening.md` (if needed) + updated `notes.md` |
| **Who** | Author |
| **Entry** | PANEL-1 and PANEL-2 reviews complete |
| **Exit** | Each substantive critique addressed or consciously deferred (with reasoning noted); opening revised if panel feedback warrants it |
| **Target** | No unexamined critique; production bible ready to execute |

FIXES is a decision stage, not just a revision stage. The author must read
every critique and decide: apply it, adapt it, or reject it with reasoning.
Ignoring feedback is not the same as rejecting it after consideration.

---

### Stage 7 — WRITE

| | |
|---|---|
| **Artifact** | `chapter.md` (~5000 words) + `figures.md` |
| **Who** | Author |
| **Entry** | `notes.md` finalized; opening revised; sources acquired |
| **Exit** | Complete draft: all planned sections present, opening integrated, figures section complete |
| **Target** | 4,500–5,500 words (chapter.md); 500–1,500 words (figures.md); ≤8 em-dashes |

The chapter executes the production bible. The opening (~800 words)
integrates into the chapter's first section. The middle sections develop
the era's arc. The figures.md covers the key people of this era — written
from inside the worldview, not as a reference list.

---

### Stage 8 — GATE-2

| | |
|---|---|
| **Artifact** | Chronicle scorecard (scored against The Chronicle rubric, 60 pts) |
| **Who** | Scorer |
| **Entry** | `chapter.md` and `figures.md` complete |
| **Exit** | Score recorded; any dimension below 7/10 flagged; innovations flagged if present |
| **Target** | **48+ / 60 (80%)**; combined with GATE-1: 72+ / 90 |

The Chronicle rubric scores six dimensions, 0-10 each:

| Dimension | Question |
|-----------|----------|
| **Immersion** | Does the reader live inside this culture's world for the whole chapter? No jolts to a modern lens? |
| **Evidence** | Specific stories, named people, real events — historically grounded? Sources would hold up? |
| **Progression** | Does the era's arc emerge? Does it build — each section earns its place, nothing repeats? |
| **Figures** | Are the leaders and people vivid, dimensional, real? Not archetypes — human beings? |
| **Voice** | Consistent tone that belongs to this culture throughout? No register shifts into academic commentary? |
| **Landing** | Does it close at the right weight — neither abrupt nor overwrought? Does the reader sit with it? |

**Innovations:** If the scorer notices something exceptional the rubric didn't
anticipate, flag it. Log to `scoring/INNOVATIONS.md`. After 2+ innovations
in the same category, propose a rubric amendment. The rubric evolves upward.

---

### Stage 9 — CLEAN

| | |
|---|---|
| **Artifact** | Clean report from each editorial lens + final revised chapter |
| **Who** | Editorial team: E-1 (Judgment Auditor), E-2 (Voice Keeper), E-3 (Compression Editor) |
| **Entry** | GATE-2 passed (48+/60) |
| **Exit** | All three editorial passes complete; chapter revised to address findings |
| **Target** | No forbidden words or framings; no voice drift; no re-explanation; em-dash count within limits |

Three distinct editorial lenses, each catching what the others miss:

- **E-1 — The Judgment Auditor**: Hunts outside-lens violations. Forbidden words (primitive, advanced, tribe). Anachronistic morality. Romanticization or demonization. Anything that steps outside the culture's own worldview.
- **E-2 — The Voice Keeper**: Hunts register drift. Textbook voice ("The economy was based on..."). Modern commentary. Any paragraph that sounds like it was written for a Western audience rather than from inside the culture.
- **E-3 — The Compression Editor**: Hunts re-explanation and filler. "This shows that..." "In other words..." Scenes that were followed by explanation of what they showed. Redundancies between sections.

---

### Stage 10 — BOARD

| | |
|---|---|
| **Artifact** | Board review files: `reviews/BOARD-*.md` |
| **Who** | 2-3 domain experts for this specific culture |
| **Entry** | CLEAN complete; chapter in near-final state |
| **Exit** | All three board reviews complete; factual errors and cultural authenticity concerns logged |
| **Target** | Historical accuracy verified; cultural representation endorsed |

The board is assembled per chapter, not permanent. Board members are
specialists in this region, this people, this era — archaeologists,
historians, anthropologists whose scholarly work covers this ground.

The board is not another craft review. It is a domain accuracy check.
They are asking: Are the facts right? Are the sources used correctly?
Does this chapter respect the latest scholarship? Does it represent
the culture as people who study it would recognize?

---

### Stage 11 — FINAL

| | |
|---|---|
| **Artifact** | Locked `chapter.md`; locked `figures.md`; updated TRACKER.md; updated INNOVATIONS.md if applicable |
| **Who** | Author |
| **Entry** | BOARD reviews complete |
| **Exit** | All board corrections applied; chapter marked FINAL in TRACKER.md; any innovations logged |
| **Target** | Chapter locked. No further revision without a documented reason. |

FINAL is a commitment. The chapter is not "done for now" — it is done.
If new scholarship emerges, there is a process for amendment. But FINAL
means the chapter has been through every stage and earned its place.

---

## Stage Summary Table

| # | Stage | Artifact | Who | Target |
|---|-------|----------|-----|--------|
| L1 | LANDSCAPE | `00-LANDSCAPE.md` | Author | Full people list + ASCII map |
| L2 | OVERVIEW | `00-OVERVIEW.md` | Author | All eras listed, inside voice |
| 1 | OPENING | `opening.md` (~800w) | Author | Person + place + moment + stakes |
| 2 | GATE-1 | Gate scorecard | Scorer | **24+ / 30** |
| 3 | PANEL-1 | 5 × `R1-P*.md` | All 5 panel voices | Qualitative feedback, all 5 lenses |
| 4 | NOTES | `notes.md` | Author | Production bible: sources, figures, arc, section plan |
| 5 | PANEL-2 | Targeted `R2-P*.md` | Panel (focused) | Gaps from opening addressed |
| 6 | FIXES | Revised opening + notes | Author | Every critique examined |
| 7 | WRITE | `chapter.md` (~5000w) + `figures.md` | Author | Complete draft within word limits |
| 8 | GATE-2 | Chronicle scorecard | Scorer | **48+ / 60**; innovations flagged |
| 9 | CLEAN | Clean report + revision | E-1, E-2, E-3 | Judgment, voice, compression checks |
| 10 | BOARD | `BOARD-*.md` | 2-3 domain experts | Historical accuracy + cultural authenticity |
| 11 | FINAL | Locked chapter | Author | Board fixes applied; chapter locked |

---

## Score Targets

| Metric | Target |
|--------|--------|
| Opening — The Gate | 24+ / 30 (80%) |
| Chapter — The Chronicle | 48+ / 60 (80%) |
| Combined per era | 72+ / 90 (80%) |
| Manuscript mean (across all chapters) | 75+ / 90 (83%) |

---

## See Also

- `guides/TEMPLATES.md` — Document templates for every stage artifact
- `guides/HOW-TO-WRITE-A-CHAPTER.md` — End-to-end author walkthrough
- `guides/STYLE-GUIDE.md` — 13 principles + forbidden words + mechanical rules
- `scoring/RUBRIC.md` — The Gate and The Chronicle rubrics in full
- `.craft/roles/ROLE.md` — Panel, editorial, and board structure

# Phase 2: Anchor Chapter — Mali Empire, "The Great Hajj"

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Take one era of one culture through the full 11-stage pipeline to validate LUCIA's format, voice, rubric, panel, and editorial system before scaling.

**Anchor:** Mali Empire (Region 10 — West African Sahel & Savanna)
**Anchor Era:** Era 3 — Mansa Musa's Reign, "The Great Hajj" (~1312–1337 CE)

**Why this era:** Mansa Musa's hajj to Mecca in 1324–25 is one of history's most vivid scenes. A caravan of tens of thousands crossing the Sahara, spending so much gold in Cairo that it crashed the Mediterranean gold market for a decade. Rich primary sources (Ibn Battuta, al-Umari, the Catalan Atlas), rich oral tradition (the jelilu), and a sensory landscape (Sahel heat, Niger River, Timbuktu's mud-brick mosques) that gives Kapuściński everything he needs. This era stress-tests every dimension: inside voice for an African culture, oral tradition as source material, Arabic sources requiring careful framing, and a story that's universally captivating but rarely told from Mali's own perspective.

**Tech Stack:** Markdown content, scored against The Gate (30pts) and The Chronicle (60pts)

**Spec:** `docs/superpowers/specs/2026-04-14-lucia-design.md` (Section 6)
**Pipeline:** `guides/PIPELINE.md`
**Style:** `guides/STYLE-GUIDE.md`
**Rubric:** `scoring/RUBRIC.md`
**Panel roles:** `.craft/roles/panel/`
**Editorial roles:** `.craft/roles/editorial/`

---

## File Map

```
regions/10-west-africa-sahel/mali-empire/
├── 00-OVERVIEW.md                         ← already exists
├── SOURCES.md                             ← already exists (stub)
├── eras/
│   └── 03-the-great-hajj/
│       ├── opening.md                     ← Task 1
│       ├── notes.md                       ← Task 4
│       ├── chapter.md                     ← Task 7
│       ├── figures.md                     ← Task 7
│       └── reviews/
│           ├── GATE-1-scorecard.md        ← Task 2
│           ├── R1-P1-tuchman.md           ← Task 3
│           ├── R1-P2-ibn-khaldun.md       ← Task 3
│           ├── R1-P3-achebe.md            ← Task 3
│           ├── R1-P4-davis.md             ← Task 3
│           ├── R1-P5-kapuscinski.md       ← Task 3
│           ├── R2-P1-tuchman.md           ← Task 5
│           ├── R2-P2-ibn-khaldun.md       ← Task 5
│           ├── R2-P3-achebe.md            ← Task 5
│           ├── R2-P4-davis.md             ← Task 5
│           ├── R2-P5-kapuscinski.md       ← Task 5
│           ├── GATE-2-scorecard.md        ← Task 8
│           ├── CLEAN-E1-judgment.md       ← Task 9
│           ├── CLEAN-E2-voice.md          ← Task 9
│           ├── CLEAN-E3-compression.md    ← Task 9
│           ├── BOARD-B1-levtzion.md       ← Task 10
│           ├── BOARD-B2-conrad.md         ← Task 10
│           └── BOARD-B3-jansen.md         ← Task 10

.craft/roles/board/
├── B-1-levtzion.md                        ← Task 10 (pre-step)
├── B-2-conrad.md                          ← Task 10 (pre-step)
└── B-3-jansen.md                          ← Task 10 (pre-step)
```

---

## Task 1: OPENING — Write the Hook Scene

**Files:**
- Create: `regions/10-west-africa-sahel/mali-empire/eras/03-the-great-hajj/opening.md`

- [ ] **Step 1: Research the era**

Read the Mali overview (regions/10-west-africa-sahel/mali-empire/00-OVERVIEW.md) for context. Key primary sources to draw from:
- **Al-Umari** (1300–1349): Egyptian historian who interviewed people in Cairo who witnessed Musa's arrival. Describes the entourage, the spending, the gold market crash.
- **Ibn Battuta** (visited Mali 1352–53): First-hand account of the court at Niani, 15 years after Musa's death. Describes protocol, the jeli, the legal system.
- **The Catalan Atlas** (1375): European map depicting Musa holding a gold nugget.
- **The Sundiata Epic**: Oral tradition providing the founding narrative and the covenant framework.

- [ ] **Step 2: Choose the scene**

The opening must be ~800 words. It drops the reader into a SPECIFIC MOMENT with a SPECIFIC PERSON. Options:

**Recommended:** Open with Mansa Musa's caravan departing Niani for Mecca. The jeli are singing the lineage. The gold is being loaded. The entourage stretches beyond sight. Musa does not yet know what will happen in Cairo — he is simply being generous, as the covenant requires. The reader enters the Mande world through the act of departure.

The scene should include:
- A named person in a specific place at a specific moment
- Sensory detail: the Sahel landscape, the heat, the sound of the jeli, the weight of gold
- The culture's own logic: Musa's generosity is not extravagance — it is the covenant. A mansa gives.
- Pull: the reader must want to know what happens when this caravan reaches Cairo

- [ ] **Step 3: Write opening.md (~800 words)**

Follow the style guide's 13 principles. Especially:
- #1 Inside, Not Above — the reader is in the caravan, not watching it
- #2 World Before Label — show the generosity before naming "hajj" or "pilgrimage"
- #5 Names in Their Language — Mansa, jeli, Niani, the Kurukan Fuga
- #11 Sensory Ground — heat, dust, the Niger, the sound of drums
- #12 Rhythm Belongs to the Story — Sahel storytelling has a griot cadence: rhythmic, building, with repetition as emphasis

Em-dash limit: ≤5

- [ ] **Step 4: Commit**

```bash
git add regions/10-west-africa-sahel/mali-empire/eras/03-the-great-hajj/opening.md
git commit -m "Write anchor opening — Mali Empire, The Great Hajj"
```

---

## Task 2: GATE-1 — Score the Opening

**Files:**
- Create: `regions/10-west-africa-sahel/mali-empire/eras/03-the-great-hajj/reviews/GATE-1-scorecard.md`

- [ ] **Step 1: Read the opening**

- [ ] **Step 2: Score against The Gate rubric (scoring/RUBRIC.md)**

Read the rubric first. Score each dimension 0-5 with evidence:

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Scene     | /5    | [specific quote or observation] |
| World     | /5    | |
| Honesty   | /5    | |
| Texture   | /5    | |
| Voice     | /5    | |
| Pull      | /5    | |
| **Total** | /30   | |

Target: 24+/30. If below 21, flag for rewrite before proceeding.

- [ ] **Step 3: Write the scorecard and commit**

---

## Task 3: PANEL-1 — All 5 Voices Review the Opening

**Files:**
- Create: 5 review files in `reviews/` (R1-P1 through R1-P5)

- [ ] **Step 1: Read each panel role** (`.craft/roles/panel/P-1-tuchman.md` through `P-5-kapuscinski.md`)

- [ ] **Step 2: Write 5 reviews**

Each review follows the format from `.craft/roles/panel/ROLE.md`:
```markdown
## P-{N} — {Name} — Review of "The Great Hajj" opening

**Overall:** {1-2 sentence verdict}

**What works:**
- {Specific praise with line/section reference}

**What doesn't:**
- {Specific critique with line/section reference}

**The question I'd push on:**
{The one thing this reviewer most wants the author to address}
```

Each voice reviews from their specific lens:
- **Tuchman**: Is it a page-turner? Is there a human driving the narrative?
- **Ibn Khaldun**: Does it hint at WHY this era unfolded as it did?
- **Achebe**: Does Mali own its story? Any outside lens visible?
- **Davis**: Is this treated as a genuine intellectual civilization?
- **Kapuściński**: Can you feel the Sahel? The heat? The sound?

- [ ] **Step 3: Commit all 5 reviews**

---

## Task 4: NOTES — Write the Production Bible

**Files:**
- Create: `regions/10-west-africa-sahel/mali-empire/eras/03-the-great-hajj/notes.md`

- [ ] **Step 1: Synthesize the panel feedback**

Read all 5 Panel-1 reviews. Identify: what worked, what needs attention, where the reviewers disagreed.

- [ ] **Step 2: Write the production bible**

Structure:
1. **Chapter arc** — what the ~5000-word chapter must accomplish
2. **Section plan** — 4-5 sections with word targets and what each must do
3. **Key figures** — named people who appear (Mansa Musa, his senior wife, the jeli, Cairo merchants, al-Umari's informants)
4. **Sources** — primary and secondary, with which sections use which sources
5. **Panel risks** — what each reviewer will push on in the full chapter (based on R1 feedback)
6. **Sensory palette** — the specific sensory details this chapter must include (landscape, climate, material culture, sound)
7. **Voice notes** — what the griot cadence should feel like in prose

- [ ] **Step 3: Update SOURCES.md**

Add the sources used to `regions/10-west-africa-sahel/mali-empire/SOURCES.md`.

- [ ] **Step 4: Commit**

---

## Task 5: PANEL-2 — Panel Reviews the Notes (Targeted)

**Files:**
- Create: 5 review files (R2-P1 through R2-P5)

- [ ] **Step 1: Panel reads notes.md**

Each reviewer focuses on gaps the opening revealed and whether the production bible addresses them.

- [ ] **Step 2: Write 5 targeted reviews**

Same format as Panel-1 but focused on: Does the plan address my concerns? What's still missing?

- [ ] **Step 3: Commit**

---

## Task 6: FIXES — Apply Panel Feedback

**Files:**
- Modify: `opening.md` (if Panel-1/2 flagged issues)
- Modify: `notes.md` (if Panel-2 flagged gaps)

- [ ] **Step 1: Read all 10 panel reviews (R1 + R2)**
- [ ] **Step 2: Apply fixes to opening and notes**
- [ ] **Step 3: Commit**

---

## Task 7: WRITE — Full Chapter + Figures

**Files:**
- Create: `regions/10-west-africa-sahel/mali-empire/eras/03-the-great-hajj/chapter.md`
- Create: `regions/10-west-africa-sahel/mali-empire/eras/03-the-great-hajj/figures.md`

- [ ] **Step 1: Write chapter.md (~5000 words)**

Follow the section plan from notes.md. The chapter should:
- Open with the scene from opening.md (can be revised/expanded)
- Build through the hajj journey, the arrival in Cairo, the gold crash
- Deepen into what Musa brought back (scholars, architects, the Sankore tradition)
- Land with weight — the Catalan Atlas, or the jelilu still singing, or Musa's legacy in the covenant

Pacing target:
- Opening/hook: ~800 words
- Development (the journey, Cairo): ~2,400 words
- Deepening (what Musa brought back, the legacy): ~1,200 words
- Landing: ~600 words

All 13 style principles apply. Especially:
- The jeli's cadence should be audible in the prose rhythm (#12)
- Every page needs sensory ground (#11)
- Musa's spending is not "extravagance" — it is the covenant (#1, #7)
- Trust the reader — if the scene showed it, don't explain it (#9)

Em-dash limit: ≤8

- [ ] **Step 2: Write figures.md (500-1500 words)**

Key figures of this era, told from inside:
- **Mansa Musa (Musa Keita I)** — the mansa, the pilgrim, the builder
- **Inari Kunate** — Musa's senior wife (or the appropriate named figure from tradition)
- **Abu Ishaq al-Sahili** — the Andalusian architect Musa brought back, who designed the mosques
- **Al-Umari** — the Egyptian historian whose informants described the hajj
- **The unnamed jeli** — the keeper of the lineage who accompanied the caravan

Each figure: 100-200 words, told from inside, describing who they were in their own world.

- [ ] **Step 3: Commit**

---

## Task 8: GATE-2 — Score the Full Chapter

**Files:**
- Create: `reviews/GATE-2-scorecard.md`

- [ ] **Step 1: Score against The Chronicle rubric (60 points)**

| Dimension  | Score | Evidence |
|------------|-------|----------|
| Immersion  | /10   | |
| Evidence   | /10   | |
| Progression| /10   | |
| Figures    | /10   | |
| Voice      | /10   | |
| Landing    | /10   | |
| **Total**  | /60   | |

Target: 48+/60. If below 42, flag for rewrite.

- [ ] **Step 2: Flag any innovations**

If the chapter does something exceptional the rubric didn't anticipate, flag it for the innovation log.

- [ ] **Step 3: Commit**

---

## Task 9: CLEAN — Editorial Pass

**Files:**
- Create: `reviews/CLEAN-E1-judgment.md`
- Create: `reviews/CLEAN-E2-voice.md`
- Create: `reviews/CLEAN-E3-compression.md`

- [ ] **Step 1: Run all 3 editorial lenses**

Read `.craft/roles/editorial/E-1-judgment-auditor.md`, `E-2-voice-keeper.md`, `E-3-compression-editor.md`.

- E-1 (Judgment Auditor): Scan for forbidden words, forbidden framings, anachronistic morality, hidden hierarchy, surprise at sophistication
- E-2 (Voice Keeper): Establish the opening's voice as baseline, scan for register shifts, textbook drift, modern commentary
- E-3 (Compression Editor): Mark re-explanations, earned-emotion violations, throat-clearing, repetition

- [ ] **Step 2: Apply fixes to chapter.md**

Fix all P1 and P2 findings. Author decides on P3.

- [ ] **Step 3: Commit cleaned chapter + editorial reports**

---

## Task 10: BOARD — Domain Expert Review

**Files:**
- Create: `.craft/roles/board/B-1-levtzion.md` (board reviewer)
- Create: `.craft/roles/board/B-2-conrad.md` (board reviewer)
- Create: `.craft/roles/board/B-3-jansen.md` (board reviewer)
- Create: `reviews/BOARD-B1-levtzion.md`
- Create: `reviews/BOARD-B2-conrad.md`
- Create: `reviews/BOARD-B3-jansen.md`

- [ ] **Step 1: Create 3 board reviewer roles**

These are domain specialists for Mali/West African history. Create role files in `.craft/roles/board/` using the template from `.craft/roles/board/ROLE.md`:

- **B-1: Nehemia Levtzion** (modeled on) — Historian of medieval West African empires and Islam in Africa. Checks historical accuracy of the Mali court, trade routes, Islamic scholarly networks.
- **B-2: David C. Conrad** (modeled on) — Specialist in the Sundiata epic and Mande oral traditions. Checks whether the griot tradition is represented accurately, whether the oral sources are used appropriately.
- **B-3: Jan Jansen** (modeled on) — Anthropologist of Mande political culture and the Kurukan Fuga. Checks whether the covenant framework is correctly understood and the social categories (nyamakala, horon, jon) are accurately represented.

- [ ] **Step 2: Run 3 board reviews**

Each reviewer reads the cleaned chapter and evaluates for:
- Historical accuracy
- Cultural authenticity
- Source appropriateness
- Specific corrections needed

Format from `.craft/roles/board/ROLE.md`.

- [ ] **Step 3: Commit board roles + reviews**

---

## Task 11: FINAL — Lock the Chapter

**Files:**
- Modify: `chapter.md` (apply board fixes)
- Modify: `SOURCES.md` (finalize)
- Modify: `scoring/INNOVATIONS.md` (if any innovations flagged)
- Modify: `TRACKER.md` (update Mali status)

- [ ] **Step 1: Apply board corrections to chapter.md**
- [ ] **Step 2: Finalize SOURCES.md with all sources used**
- [ ] **Step 3: Log any innovations to scoring/INNOVATIONS.md**
- [ ] **Step 4: Update TRACKER.md** — set Mali's Chapters to 1, Locked to 1
- [ ] **Step 5: Final commit**

```bash
git commit -m "Lock anchor chapter — Mali Empire, The Great Hajj (Era 3)"
```

---

## Execution Notes

Tasks are strictly sequential — each stage depends on the previous.

```
Task 1:  OPENING (write)
Task 2:  GATE-1 (score opening)
Task 3:  PANEL-1 (5 reviews of opening)
Task 4:  NOTES (production bible)
Task 5:  PANEL-2 (5 targeted reviews of notes)
Task 6:  FIXES (apply feedback)
Task 7:  WRITE (full chapter + figures)
Task 8:  GATE-2 (score chapter)
Task 9:  CLEAN (editorial pass)
Task 10: BOARD (domain expert review)
Task 11: FINAL (lock chapter)
```

**Expected output:** One complete, locked, scored, reviewed chapter — LUCIA's first. The scores, reviews, and any innovations discovered will calibrate the system for all future chapters.

You are running /chronicle-e2e for: {{people}}, {{era}}

Run the full 11-stage pipeline end-to-end for a single era. This skill
orchestrates every stage in order, with gates that block forward progress
until quality thresholds are met.

---

## Input

- **People**: The culture being written
- **Era**: The era within that culture's periodization

Prerequisites:
- `00-LANDSCAPE.md` exists for the region
- `00-OVERVIEW.md` exists for the people
- `SOURCES.md` is seeded with primary and academic sources

---

## The 11 Stages

Execute in strict order. No skipping. No merging stages.

```
OPENING → GATE-1 → PANEL-1 → NOTES → PANEL-2 → FIXES → WRITE → GATE-2 → CLEAN → BOARD → FINAL
```

### Stage 1 — OPENING
Run `/chronicle-opening {{people}}, {{era}}`
Produces: `opening.md` (~800 words)

### Stage 2 — GATE-1
Run `/chronicle-gate opening.md`
**Gate: 24+ / 30.** If below, revise opening and re-score. Do not proceed
until the gate passes.

### Stage 3 — PANEL-1
Run `/chronicle-panel opening.md, round 1`
Produces: 5 review files (`R1-P1` through `R1-P5`)

### Stage 4 — NOTES
Run `/chronicle-notes {{people}}, {{era}}`
Produces: `notes.md` (production bible)

### Stage 5 — PANEL-2
Run `/chronicle-panel notes.md, round 2`
Produces: Targeted review files (`R2-P*`)

### Stage 6 — FIXES
Read all panel feedback (PANEL-1 + PANEL-2). For each substantive critique:
- Apply it, adapt it, or reject it with documented reasoning
- Revise `opening.md` if panel feedback warrants it
- Update `notes.md` to incorporate feedback
No unexamined critique.

### Stage 7 — WRITE
Run `/chronicle-chapter {{people}}, {{era}}`
Produces: `chapter.md` (~5000 words) + `figures.md`

### Stage 8 — GATE-2
Run `/chronicle-gate chapter.md`
**Gate: 48+ / 60.** If below, revise chapter and re-score. Do not proceed
until the gate passes.

### Stage 9 — CLEAN
Run `/chronicle-clean chapter.md`
Produces: 3 editorial reports (`CLEAN-E1`, `CLEAN-E2`, `CLEAN-E3`)
Apply all fixes before proceeding to BOARD.

### Stage 10 — BOARD
Run `/chronicle-board {{people}}, {{era}}`
Produces: Board role files + 2-3 board review files
Apply corrections. Board feedback is authoritative on factual matters.

### Stage 11 — FINAL
- Apply all remaining board corrections
- Update `TRACKER.md` — mark chapter as FINAL
- Log any innovations to `scoring/INNOVATIONS.md`
- **Run innovation threshold check** (see below)
- Lock the chapter: no further revision without documented reason

---

## Gate Rules

- GATE-1 blocks all downstream stages. An opening below 24/30 must be
  revised and re-scored before PANEL-1 begins.
- GATE-2 blocks CLEAN and beyond. A chapter below 48/60 must be revised
  and re-scored before editorial review begins.
- Combined target: 72+ / 90 (80%)

---

## Output

All artifacts written to: `regions/{{region}}/{{people}}/eras/{{era}}/`
All reviews written to: `reviews/`
Board roles written to: `.roles/board/`
Tracker updated: `TRACKER.md`

Pipeline reference: `guides/PIPELINE.md`

## Innovation Threshold Check (Stage 11)

After logging innovations, check for promotion via TWO pathways:

### Instance Trigger (original)
Scan `scoring/INNOVATIONS.md` for any dimension with 2+ innovations still
at status `logged`. If found, propose a rubric amendment.

### Cluster Trigger (v1.5)
Scan all `logged` innovations for thematic clusters: 3+ innovations that
share a principle even if no two are exact duplicates. Group by THEME, not
by formal dimension. If a cluster holds across genuinely different cultures,
propose a cluster amendment.

**When cluster analysis is MANDATORY:**
- At every session boundary
- After completing a book (all eras of one culture)
- After completing a region sweep
- After any batch of 5+ chapters

### Promotion Process (either trigger)
1. **Propose a rubric amendment** — draft the amendment text
2. **Prompt the user**: "[N] innovations form cluster [name]. Proposed amendment:
   [summary]. Adopt to rubric v[next]?"
3. If approved: update `scoring/RUBRIC.md` with the amendment, increment version,
   update all constituent innovation statuses to `adopted (vX.X)`, update
   the Amendment History table
4. If declined: mark innovations as `reviewed — not adopted` with reason

This ensures the rubric evolves at the pace of discovery, not at the pace of
exact duplication. Do not skip this step.

## Pre-Chapter Rubric Sync

Before starting Stage 1, check the rubric version:
- Read the version header in `scoring/RUBRIC.md`
- If the version has changed since the last chapter you wrote, read ALL
  amendments. The bar may have risen.

## Cross-Compare Trigger

After every 3rd locked chapter, prompt the user: "3 chapters locked since
last cross-comparison. Run /chronicle-cross-compare?" This surfaces patterns
that individual reviews miss.

---

## Checklist

- [ ] All 11 stages executed in order
- [ ] GATE-1 passed (24+/30) before PANEL-1
- [ ] GATE-2 passed (48+/60) before CLEAN
- [ ] All panel feedback examined (no unexamined critiques)
- [ ] CLEAN fixes applied before BOARD
- [ ] Board corrections applied
- [ ] TRACKER.md updated with FINAL status
- [ ] Innovations logged if present
- [ ] Innovation threshold check run (propose amendments if 2+ in any dimension)
- [ ] Rubric version synced before starting
- [ ] Cross-compare prompted if 3+ chapters since last comparison
- [ ] Chapter locked

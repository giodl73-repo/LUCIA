# PR-C1 — Model Substrate Effects in Structured Creative Production: Opus vs Sonnet vs Haiku

**Track**: C (When Typologies Emerge From Production)
**Position in chain**: First paper of Track C — requires A + B as background; gates C2 and C3.
**Status**: planned, round 0

---

## Hypothesis

Model capability affects both output quality and discovery rate in AI-assisted creative production, but the relationship is not monotonic: capability above a threshold is necessary but not sufficient; pipeline discipline is the additional necessary factor. Haiku fails pipeline discipline (incomplete stages, unreliable reporting) even when its output quality is adequate.

## Quantification Contract

| Component | Value |
|-----------|-------|
| Primary number | Three-way comparison (Opus / Sonnet / Haiku) across matched conditions: mean GATE-2 score, innovations-per-chapter rate, pipeline-completion rate. Baseline data from Session 2: Region 9 (Opus), Region 12 (Sonnet), Region 26 (Haiku). |
| Experiment design | Control for prompt structure, pipeline instructions, reviewer panel, source material. Compute score distribution, innovation rate, pipeline compliance for each model. Additional matched-pair chapters if initial sample < n=5 per model. |
| Decision it changes | Default SCRIBE model choice and when to escalate to higher-capability models. |
| Null fallback | No significant difference across models (p > 0.05 on score, rate) → model choice is not a determinant; discipline dominates. |
| Falsification condition | All three models produce statistically indistinguishable quality AND innovation rate → Track C1 thesis (substrate matters) is falsified. |

## Outline

1. **Introduction.** Model choice in AI-assisted creative work. Capability vs. discipline hypotheses.
2. **Method.** LUCIA's Session-2 A/B/C experiment: Region 9 (Opus), Region 12 (Sonnet), Region 26 (Haiku). Matched pipeline, reviewer panel, source material.
3. **Metrics.** GATE-2 score, innovations-per-chapter, pipeline-completion rate, reporting reliability.
4. **Results.** Mean scores: Opus 81.3, Sonnet 82.5, Haiku [TBD from Session 2 data]. Innovation rates. Pipeline compliance.
5. **Haiku failure mode.** Specific: writes but breaks on process. Incomplete pipelines, unreliable reporting. Why this matters more than score delta.
6. **Matched-pair supplementary.** If initial n < 5 per cell, commission matched chapters.
7. **Discussion.** Sonnet-as-default decision. When to escalate to Opus (hard chapters). Capability threshold hypothesis.
8. **Falsification.** Thresholds.

## Data Sources

- Session 2 handoff (`agents/LUCY-HANDOFF-S02.md`) — 3-model comparison explicit
- `TRACKER.md` region-level mean scores
- Locked chapter scores from Regions 9, 12, 26
- Git log for production timestamps per chapter

## Anticipated Failure Modes

- Session-2 data has n ≈ 6–10 per model; statistical power limited. Supplement with matched-pair chapters.
- Model version drift: Opus and Sonnet specific versions used in Session 2 must be pinned. Document explicitly.
- "Haiku fails pipeline" is a qualitative claim — operationalize with discrete compliance metrics.
- Scoring is self-scored by the writing model; blind cross-model re-scoring adds rigor.

## Venue

NeurIPS (empirical model comparison) or ICLR. Could also target FAccT if we frame as capability-discipline-accountability.

## Dependencies

Track A papers (A1 for innovation rate method, A2 for score stability), Track B papers (B1 for what "discovery rate" measures).

## Blocks

PR-C2 (requires cross-model data), PR-C3 (requires C1 and C2 together).

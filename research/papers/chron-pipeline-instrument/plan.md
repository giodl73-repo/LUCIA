# PR-C2 — The Pipeline as Epistemic Instrument: Discipline-Compliance and Discovery Rate

**Track**: C (When Typologies Emerge From Production)
**Position in chain**: Second paper of Track C — requires C1's cross-model data; gates C3.
**Status**: planned, round 0

---

## Hypothesis

The 11-stage pipeline (OPENING → GATE-1 → PANEL-1 → NOTES → PANEL-2 → FIXES → WRITE → GATE-2 → CLEAN → BOARD → FINAL) is the epistemic instrument of discovery, independent of model capability. Within-model, chapters completing all 11 stages score higher and produce more innovations than chapters skipping stages. The effect is model-independent: Sonnet with full pipeline ≈ Opus with full pipeline > either with partial pipeline.

## Quantification Contract

| Component | Value |
|-----------|-------|
| Primary number | Correlation coefficient between pipeline-compliance (0–11 stages completed) and GATE-2 score across 115 chapters, stratified by model to isolate pipeline effect from model effect. |
| Experiment design | For each locked chapter, compute pipeline completeness score. Regress against GATE-2 score. Separate Sonnet-only sample to isolate pipeline effect from model capability. Compare models at matched pipeline-compliance. |
| Decision it changes | Whether the 11-stage pipeline is a discovery instrument independent of model capability, or ceremony. |
| Null fallback | No correlation between compliance and score within-model → pipeline is ceremony; drop or redesign. |
| Falsification condition | r < 0.3 within-model OR score delta between full-pipeline and reduced-pipeline chapters < 5 points. |

## Outline

1. **Introduction.** Pipeline as process vs. pipeline as instrument. The question: does discipline matter independently of model capability?
2. **The 11 stages.** Formal description. What each stage adds epistemically (detection, reflection, revision, cross-check).
3. **Method.** Pipeline compliance scoring (0–11). Within-model regression. Cross-model comparison at matched compliance.
4. **Results — Sonnet-only.** Compliance × score correlation. Full-pipeline vs. partial-pipeline chapters.
5. **Results — model-pipeline interaction.** Opus-full vs. Sonnet-full. Opus-partial vs. Sonnet-partial.
6. **Results — innovations per stage.** Which stages produce the most innovations logged? (Panel-1 and Board likely dominate.)
7. **Discussion.** Pipeline as model-independent discovery instrument. Why process matters. Implications for AI-assisted creative production broadly.
8. **Falsification.** Thresholds.

## Data Sources

- 115 locked chapters × reviews/ directories (pipeline compliance = count of expected files present)
- INNOVATIONS.md Source field (maps to pipeline stage that produced the innovation)
- Cross-model data from PR-C1

## Anticipated Failure Modes

- Early Session-1 chapters may have fewer review artifacts due to evolving pipeline; separate Session-1 from Session-2.
- Some chapters skipped PANEL-2 intentionally when GATE-1 scored highly; code as "high-gate skip" separately.
- Innovation attribution to a stage is approximate (innovations are often logged post-chapter).

## Venue

CHI (instrument design) or FAccT (discipline and accountability).

## Dependencies

PR-C1 (cross-model data).

## Blocks

PR-C3 (needs pipeline-effect result to propose emergence conditions).

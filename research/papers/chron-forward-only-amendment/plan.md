# PR-A2 — Forward-Only Rubric Evolution: Stability Under a Discovery-Driven Quality Standard

**Track**: A (The Discovery Engine)
**Position in chain**: Second paper — requires A1's trigger definitions; gates A3.
**Status**: planned, round 0

---

## Hypothesis

Forward-only rubric amendment (new bars apply only to chapters scored after the amendment) produces stable evolution when the underlying trigger rule is sound. Stability is measurable by amendment reversal rate and by the delta between original scores and counterfactual re-scores under later rubric versions.

## Quantification Contract

| Component | Value |
|-----------|-------|
| Primary number | Amendment reversal rate across v1.0 → v1.7. Plus: mean GATE-2 re-score delta on a stratified sample of 20 early chapters when scored under v1.7 vs. their original rubric version. |
| Experiment design | Diff rubric versions and classify each amendment as extension, refinement, or reversal. Then blind re-score 20 chapters (sampled across Sessions 1 and 2) with v1.7 anchors. |
| Decision it changes | Whether forward-only is principled or obscures rubric instability. |
| Null fallback | Reversal rate > 20% OR mean re-score delta > 5 points → forward-only is masking drift; retroactive re-scoring should be considered. |
| Falsification condition | ≥ 3 reversed amendments across 7 versions OR mean absolute re-score delta > 8 points. |

## Outline

1. **Introduction.** Forward-only vs. retroactive scoring in evolving quality systems. The stability trade-off.
2. **LUCIA's policy.** Explicit forward-only rule from RUBRIC.md. Amendment classification (extension / refinement / reversal).
3. **Method 1: Amendment classification.** Diff rubric versions. Count reversals. Report extension:refinement:reversal ratio.
4. **Method 2: Counterfactual re-scoring.** Select 20 chapters stratified across early-session (v1.0–v1.3) and mid-session (v1.4–v1.6). Blind re-score under v1.7 anchors. Report score deltas.
5. **Results.** Reversal rate, mean and tail re-score delta.
6. **Discussion.** When forward-only holds. When it masks drift. Implications for AI-assisted creative production broadly.
7. **Falsification.** Thresholds.

## Data Sources

- `scoring/RUBRIC.md` (v1.0 through v1.7 changelog)
- Locked chapter reviews (GATE-1, GATE-2 files in `regions/*/*/eras/*/reviews/`)
- Git history of RUBRIC.md for version diffs

## Anticipated Failure Modes

- Re-scoring requires independent scorer; self-re-score introduces bias. Consider panel-of-scorers or model-assisted blind re-scoring.
- Some v1.0–v1.3 chapters were scored before amendments they would now be held to existed — this is the point of the study, but requires careful framing.
- "Reversal" vs. "refinement" is judgment-call territory; pre-register classification criteria before diffing.

## Venue

FAccT (accountability/stability of AI quality systems) or CHI (methods track).

## Dependencies

PR-A1 (trigger definitions — needed to compute amendment pathway).

## Blocks

PR-A3 (requires both A1 and A2).

# PR-A3 — Typology Saturation: Convergence Evidence in a Self-Evolving Quality Rubric

**Track**: A (The Discovery Engine)
**Position in chain**: Third paper — requires A1 + A2; closes Track A.
**Status**: planned, round 0

---

## Hypothesis

A well-calibrated Innovation Engine applied at scale produces typology saturation: the rate of new-type discovery falls toward zero as the corpus grows, evidencing convergence on a bounded set of dimensions rather than unbounded proliferation. Saturation is measurable as a decreasing new-register-per-chapter rate fitting a log or power-law curve.

## Quantification Contract

| Component | Value |
|-----------|-------|
| Primary number | New-register-per-chapter rate over time (chapters 1–115, chronological). Fit saturation curve (log or power-law). Report half-life and asymptote. |
| Experiment design | Parse all logged Voice Spectrum innovations with source chapter date. Bin by 10-chapter cohorts. Compute new-register rate per cohort. Fit curve. |
| Decision it changes | Whether the engine converges on a bounded typology or unboundedly proliferates. |
| Null fallback | Rate constant or increasing across cohorts → no saturation; typology is open-ended and the discovery engine cannot be claimed to converge. |
| Falsification condition | Final-cohort rate ≥ 80% of initial-cohort rate → no meaningful saturation. |

## Outline

1. **Introduction.** Saturation as a test of typology closure. Why it matters for claims about the engine's correctness.
2. **Method.** Chronologically-ordered chapters. 10-chapter cohort binning. New-register counting. Curve fitting (log, power-law, exponential). Model-selection via AIC/BIC.
3. **Results — Voice Spectrum saturation.** Cohort-by-cohort rate. Fitted curve. Half-life, asymptote.
4. **Results — Structural Engine saturation.** Same method applied to engine types.
5. **Results — Terminal Condition saturation.** Same method applied to terminal condition types.
6. **Cross-typology comparison.** Which typologies saturated first? Does saturation rate correlate with typology scale (prose < arc < closure)?
7. **Discussion.** Convergence vs. open-endedness. Implications for typology claims.
8. **Falsification.** Rate stability.

## Data Sources

- All three typologies' innovation entries in `scoring/INNOVATIONS.md` with source chapter path and date.
- Chapter production order from git history (chronicle repo).

## Anticipated Failure Modes

- Innovation logging rate correlates with reviewer attention, not corpus growth. Control by model (Sonnet cohorts only) or stratify.
- Sessions 1 and 2 had different logging practices; normalize or stratify by session.
- The three typologies may saturate at different rates — that's a finding, not a failure.

## Venue

NeurIPS Datasets & Benchmarks (empirical typology claim) or ICML.

## Dependencies

PR-A1 (trigger definitions), PR-A2 (stability claim needed to interpret rate change as saturation vs. stagnation).

## Blocks

None (closes Track A).

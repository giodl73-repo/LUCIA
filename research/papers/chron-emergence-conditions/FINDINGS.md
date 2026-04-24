# PR-C3 — Conditions for Typology Emergence in AI-Assisted Creative Domains: A Falsifiable Generalization

**Status**: Pre-write findings (round 0 draft)
**Date**: 2026-04-20
**Module**: chron — Emergent Typologies in AI-Assisted Creative Production
**Track**: C — When Typologies Emerge From Production
**Framing decision**: **A Falsifiable Proposal** (per plan.md contingency — external corpora not acquired within time budget)

---

## 1. Hypothesis

**Primary.** Four conditions are jointly necessary for typology-emergence in AI-assisted creative production at scale:

1. **C1 — Discovery-driven rubric.** A quality standard with a codified trigger for amendment in response to observed patterns, rather than a fixed checklist.
2. **C2 — Forward-only amendment.** New bars apply to artifacts produced after the amendment.
3. **C3 — Heterogeneous panel review.** Multi-lens review by disciplinarily distinct reviewers, not a single evaluator repeated.
4. **C4 — Pipeline discipline with stage-wise review.** Production passes through codified stages, each leaving an inspectable artifact.

**Secondary claim.** The four are necessary but not sufficient. Model substrate (PR-C1) supplies a floor capability; editor positionality supplies a ceiling.

## 2. Pre-Registered Falsification

**Protocol thresholds**:
- **Mismatch-1**: Corpus satisfies all 4 conditions but shows no emergence signal → not sufficient.
- **Mismatch-2**: Corpus violates ≥ 1 condition but shows emergence anyway → violated condition not necessary.
- **Protocol falsification (binding)**: prediction-observation disagreement in ≥ 1 of 2 external corpora.

**Framework tier**: if the four conditions cannot be operationalized as independently-measurable predicates, framework falsified before any corpus is touched.

## 3. Related-Work Position

- **AI-assisted creative evaluation** (CHI, FAccT): Ippolito 2022, Franceschelli & Musolesi 2023. Measure single-pass outputs; don't address whether evaluation typology emerges.
- **Methodological-transportability**: Cartwright & Hardie 2012; Shadish-Cook-Campbell 2002. Standard frame: "results transport under moderators." Our frame: "method transports under conditions."
- **Agent-benchmarking** (AgentBench, GAIA, HELM): fixed rubrics; don't measure whether an AI-production system discovers its own dimensions.
- **Grounded-theory**: Glaser & Strauss 1967; Charmaz 2006. Our framework is a quantitative restatement of theoretical sensitivity for AI-production velocity.

**Whitespace**: first systematic framework for typology-emergence transportability with 4 pre-registered conditions tied to empirical evidence from a single AI-production record.

## 4. Evidence Map — Condition to Prior-Paper Number

| Condition | Grounding paper(s) | Primary number |
|-----------|--------------------|----------------|
| **C1** | PR-A1, PR-A3 | Trigger latency median 1 day (A1); saturation ratio 15% aggregate (A3) |
| **C2** | PR-A2 | 0 reversals/15 amendments; 99.6% line preservation; re-score delta 1.75 |
| **C3** | PR-B1, PR-B2, PR-B3 | 78.8% voice validation; 60% non-provincialism; 96.5% closure coverage |
| **C4** | PR-C2 | r=0.46 within-model; +4.7 pt full-vs-reduced delta |

**Floor caveat** (PR-C1): Opus 81.22, Sonnet 82.50, Haiku 83.20 scores; innovation rate 0.22/1.67/0.60 (p≈0.006); reporting 100/100/20% (p<0.002).

## 5. Candidate External Corpora

**Corpus A — AI-assisted code review comments.** Sourcegraph Cody, Copilot-PR, Cursor-PR archives. Predicted: C1=0, C2=0, C3=0.5, C4=varies. Prediction: **NO emergence**.

**Corpus B — AI-generated music genre tags.** Suno, Udio community corpora. Predicted: C1=0.5, C2=0, C3=1, C4=0. Prediction: **PARTIAL emergence**.

**Corpus C (optional) — AI-assisted scientific writing.** arXiv AI-disclosures. Predicted: C1=0.5, C2=0.5, C3=1, C4=1. Prediction: **YES emergence**.

## 6. Operationalization

Each condition operationalized as 3 binary-or-graded predicates:

**C1**: P1.1 written rubric; P1.2 codified amendment trigger; P1.3 amendment log. All required.

**C2**: P2.1 historical scores preserved; P2.2 reversal classifier operational; P2.3 reversal rate ≤ 20%.

**C3**: P3.1 ≥ 3 distinct reviewer perspectives; P3.2 disciplinarily distinct; P3.3 disagreements logged.

**C4**: P4.1 ≥ 5 named stages; P4.2 per-artifact compliance measurable; P4.3 compliance-score r ≥ 0.3.

**Aggregate**: 4-vector (C1, C2, C3, C4). Emergence predicted iff all four exceed 0.5 binary threshold.

## 7. Primary Framework Deliverables

1. Four-condition framework as operationalized predicate set.
2. Evidence map grounding each condition in a module-paper number.
3. Falsification protocol for external corpora.
4. Candidate external corpora with predicted condition status.
5. Floor/ceiling framing about model substrate and editor positionality.

## 8. Glaser Commitment (PP1-E)

Inherited from PR-B1, B3, C1, C2. Framework emerged from backward analysis across 8 prior papers. Each condition traces to specific primary numbers. Editor's role is Glaser-style axial coding on the module's own evidence base.

## 9. Editor Role (PP1-D)

1. Framework enumeration from prior-paper findings.
2. Operationalization drafting.
3. Candidate corpus selection.
4. Pre-registration of falsification protocol before any external-corpus data acquisition.

Second-editor framework-enumeration reproducibility flagged as companion.

## 10. Cross-Paper Dependencies (PP1-C)

Densest cross-paper dependency in the module — all 8 prior papers contribute:
- PR-A1 → C1 trigger mechanism
- PR-A2 → C2 stability
- PR-A3 → C1 convergence evidence
- PR-B1 → C3 at prose scale
- PR-B2 → C3 at arc scale
- PR-B3 → C3 at closure scale; Track B closure
- PR-C1 → floor-capability evidence
- PR-C2 → C4 quantified

## 11. Companion Measurements Flagged

- Acquisition and analysis of Corpus A (AI code review) against protocol.
- Acquisition and analysis of Corpus B (AI music) against protocol.
- Second-editor framework-enumeration reproducibility.
- Longitudinal LUCIA extension to n=500 chapters.
- Internal ablations (forward-only violated; panel collapsed to single-voice).

## 12. Framework-Status Self-Assessment

**Methodological proposal**, not executed test. Per plan.md contingency, publishable at CACM methodology venue and FAccT accountability track. Pre-registered protocol is primary contribution.

**Strength**: framework tightly grounded in quantitative evidence from one production record.
**Weakness**: not tested against external corpus.
**Venue fit**: CACM; FAccT.

Pre-write CEMCK: 21/25.

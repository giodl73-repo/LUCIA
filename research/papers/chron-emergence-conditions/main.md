# Conditions for Typology Emergence in AI-Assisted Creative Domains: A Falsifiable Generalization

**Paper**: PR-C3
**Module**: chron (Emergent Typologies in AI-Assisted Creative Production)
**Track**: C — When Typologies Emerge From Production
**Date**: 2026-04-20
**Status**: Draft, round 0 — **Framed as "A Falsifiable Proposal" per plan.md contingency.**
**Dependencies**: All 8 prior module papers. **Closes the chron module.**

---

## Abstract

A quality rubric for AI-assisted creative production can either be specified before production begins — at which point it cannot anticipate the dimensions the artifact will reveal — or it can be allowed to drift silently during production, at which point score comparability erodes. We have documented across eight prior papers a third path: a rubric that evolves through a codified Innovation Engine with a forward-only amendment policy under heterogeneous panel review and pipeline discipline, such that the typologies the artifact reveals are externalized as inspectable amendments and saturate as the corpus grows. The case study is LUCIA, a narrative encyclopedia of 115 chapters covering 93 cultures whose rubric evolved from v1.0 to v1.7 through 100 adopted amendments, producing three scale-nested empirical typologies (voice registers, structural engines, terminal conditions) validated by cross-culture replication. This paper asks the generalization question: under what conditions does typology-emergence occur in other AI-assisted creative domains? We propose four conditions — discovery-driven rubric, forward-only amendment, heterogeneous panel review, pipeline discipline — each grounded in a specific primary number from a prior module paper: trigger latency of 1 day (PR-A1); 0 reversals and 99.6% line preservation (PR-A2); 15%-to-0% saturation ratio (PR-A3); 78.8%/60%/96.5% cross-scale typology coverage (PR-B1/B2/B3); r = 0.46 within-model compliance-score correlation (PR-C2). Model substrate (PR-C1) supplies a floor capability below which emergence does not happen under any conditions. Per plan.md contingency, external corpora were not acquired within this paper's time budget; we reframe from "An Executed Test" to "A Falsifiable Proposal." The deliverable is the four-condition framework operationalized as a testable predicate set, a pre-registered falsification protocol for two identified external corpora (AI-assisted code review; AI-generated music with community genre tags; optional third: AI-assisted scientific writing), and an evidence map tying every condition to module findings. We position against AI-assisted creative evaluation (CHI, FAccT), methodological-transportability work (Cartwright & Hardie; Shadish-Cook-Campbell), and agent-benchmarking (AgentBench, GAIA). Whitespace: first systematic framework for typology-emergence transportability with 4 pre-registered conditions tied to empirical evidence from a single AI-production record. This paper closes the chron module and gestures to the wider AI-creative-production research programme.

---

## 1. Introduction

This paper is the ninth and closing paper of the chron module. The preceding eight have established a body of evidence, summarized briefly because this paper is unintelligible without it.

**Track A** measured the mechanism. PR-A1 established LUCIA's Innovation Engine as a two-trigger detection mechanism (2-instance exact-match plus 3-instance thematic-cluster) with median trigger latency of 1 day and maximum 2 days across 98 adopted amendments. PR-A2 showed forward-only amendment produced stable evolution: 0 classified reversals across 7 amendment cycles, 99.6% line preservation from v1.0 to v1.7, mean absolute re-score delta of 1.75 points. PR-A3 demonstrated typology saturation: aggregate new-innovation-per-chapter rate dropped from 0.93 to 0.14 across four chronological cohorts (ratio 15% << 80% threshold), with Voice Spectrum saturating sharply (9%), Structural Engine completely (0%), Terminal Condition open at 115-chapter scale (ratio 2.86).

**Track B** measured the artifact's dimensions. PR-B1 validated the Voice Spectrum: 52 of 66 validated registers reach ≥ 2-instance cross-culture confirmation (78.8%, Wilson 95% CI [67.7%, 86.7%]), and 15 of 17 spot-checked chapters exhibit zero-em-dash as emergent property (88.2%, CI [66.2%, 96.6%]). PR-B2 established the Structural Engine taxonomy: 5 formally-adopted types spanning 23 cultures across 9 regions; non-provincialism 3/5 = 60% (Wilson CI [23.1%, 88.2%]), 19 candidate engines on a watch list. PR-B3 classified terminal conditions across all 115 chapters: 18 candidate types covered 84.3% (Wilson CI [76.5%, 89.9%]), rising to 96.5% with an Ongoing auxiliary — both pre-registered falsification thresholds cleared.

**Track C** measured the conditions of production. PR-C1 compared Opus, Sonnet, Haiku on matched-region chapters: mean scores 81.22/82.50/83.20 (prose near-invariant); innovations-per-chapter 0.22/1.67/0.60 (Poisson p ≈ 0.006, 7.5× rate ratio); clean end-of-spawn reporting 100/100/20% (Fisher p < 0.002). PR-C2 isolated the pipeline as epistemic instrument: Pearson r(compliance, score) within Sonnet-S2 = 0.46, 95% bootstrap CI [0.27, 0.62]; full-vs-deeply-reduced delta +4.7 points.

This is a substantial body of evidence, all drawn from a single AI-assisted creative production record. The question this paper asks is the generalization question.

### 1.1 Claim

We claim four conditions are jointly necessary for typology-emergence in AI-assisted creative production at scale:

- **C1 — Discovery-driven rubric.** A quality standard with a codified trigger for amendment in response to observed patterns.
- **C2 — Forward-only amendment.** New bars apply only to artifacts produced after the amendment.
- **C3 — Heterogeneous panel review.** Multi-lens review by disciplinarily distinct reviewers.
- **C4 — Pipeline discipline with stage-wise review.** Codified stages, each leaving inspectable artifact.

Each condition is grounded in a specific primary number from a prior module paper. Model substrate (PR-C1) supplies a floor capability; editor positionality supplies a ceiling.

### 1.2 Contingency and Framing

Our plan.md specified validation against two external corpora. Within this paper's time budget we were not able to acquire those corpora. Per the plan.md contingency, we reframe from "An Executed Test" to **A Falsifiable Proposal**: the pre-registered prediction and the operationalized framework are the primary contribution; external-corpus execution is future work.

This framing is consistent with plan.md guidance that such a reframe remains publishable in methodological venues (CACM, FAccT methodology track). We commit to executing the protocol against ≥ 1 external corpus within 12 months of acceptance.

### 1.3 Falsification

Two tiers:
- **Protocol tier** (binding for future work): prediction-observation mismatch in ≥ 1 of 2 external corpora.
- **Framework tier** (binding at proposal-submission): if operationalization in §6 collapses under peer review, framework falsified before any corpus is tested.

### 1.4 Contribution

Fourfold. First, articulate the framework as generalization from 8 prior module papers. Second, operationalize each condition as testable predicate set (§6). Third, pre-register falsification protocol (§7). Fourth, identify 2-3 candidate external corpora (§8).

### 1.5 Scope

Does not claim: (a) four conditions are exhaustive; (b) they are sufficient without floor capability; (c) LUCIA's specific operationalizations are the only ones that work; (d) the framework has been tested externally.

---

## 2. Related Work

### 2.1 AI-Assisted Creative Evaluation (CHI, FAccT)

Ippolito et al. (2022) [NEED-1]; Franceschelli & Musolesi (2023) [NEED-2]; Chiang & Lee (2023) [NEED-3]. These works measure output quality against rubrics whose dimensions are specified up-front. Our framework says this is the wrong posture for creative domains where the dimensions themselves are discovered during production.

### 2.2 Methodological-Transportability Work

Cartwright & Hardie (2012) [NEED-4] argue causal claims transport across populations only when effect modifiers are held constant. Shadish, Cook, Campbell (2002) [NEED-5] systematize external validity. Both treat transportability as a question about outcome. Our framework asks whether the *method* transports — a different question.

### 2.3 Agent-Benchmarking

Liu et al. (2023) AgentBench [NEED-6]; Mialon et al. (2023) GAIA [NEED-7]; Liang et al. (2022) HELM [NEED-8]. Evaluate model-as-agent on fixed rubrics; don't measure whether an AI-production system discovers its own evaluation dimensions.

### 2.4 Grounded-Theory Transportability

Glaser & Strauss (1967) [NEED-9]; Charmaz (2006) [NEED-10]. Theoretical sensitivity claimed to transport across domains but rarely tested quantitatively. Our four-condition framework is a quantitative restatement for AI-production velocity.

### 2.5 Constitutional AI and RLHF

Bai et al. (2022) [NEED-11]; Ouyang et al. (2022) [NEED-12]. Produce evaluation typologies (principles, implicit rewards) but violate our conditions: CAI pre-specifies principles (violates C1); RLHF reward models drift silently (violates C2); both often homogeneous reviewers (violate C3). Prediction: neither produces cross-instance-validated typology saturating as corpus grows.

### 2.6 Glaser Commitment (PP1-E)

Inherited from PR-B1, B3, C1, C2. The four conditions emerged from backward analysis of 8 prior papers. Each traces to specific primary numbers. Editor's role is Glaser-style axial-coding move on the module's own evidence base. Reject Charmaz constructivist move.

A hostile reviewer may argue the four conditions are suspiciously aligned with LUCIA's specific operationalizations. We accept the threat (§9.1) and flag pre-registered external-corpus protocol as the guard.

---

## 3. The Four Conditions

### 3.1 C1 — Discovery-Driven Rubric

A quality standard with codified trigger for amendment in response to observed patterns. Three components: (a) written rubric text; (b) codified amendment trigger; (c) inspectable amendment log.

**Evidence grounding.** PR-A1 established Innovation Engine as two-trigger rule (2-instance, 3-cluster) with measured median latency 1 day, max 2 days across 98 adopted amendments. PR-A3 established the rubric converges: aggregate saturation ratio 15% (well below 80% falsification); Voice 9%, Engine 0% ratios.

**Why necessary.** Without codified trigger, observed pattern either never enters rubric (calcification) or enters silently without audit (drift). Both pathologies identified in PR-A1.

**Why not sufficient.** Discovery-driven rubric can still drift if amendments are retroactively re-scored (violating C2) or reviewers are homogeneous (violating C3).

### 3.2 C2 — Forward-Only Amendment

New bars apply only to artifacts produced after the amendment. Three disciplines: (a) version-dated scores; (b) inspectable changelog; (c) textual preservation.

**Evidence grounding.** PR-A2 measured forward-only stability on v1.0 → v1.7. Zero reversals of 15 amendments. 99.6% of v1.0's 244 lines preserved in v1.7; 54.3% of v1.7's 4,289 words are post-v1.0. 4-chapter counterfactual re-score pilot yields mean delta +1.75 points (uniformly positive) — below 8-point falsification threshold.

**Why necessary.** Without forward-only: (1) circularity problem — amendment triggered by early chapter's pattern retroactively penalizes same chapter; (2) legitimacy problem — without version-dated scores, downstream consumers cannot interpret score meaning. Forward-only is operationally weakest of three defensible policies but has cleanly diagnosable failure modes.

**Why not sufficient.** Forward-only preserves historical scores but does not discover new dimensions (C1's job).

### 3.3 C3 — Heterogeneous Panel Review

Multi-lens review by disciplinarily distinct reviewers, not a single evaluator repeated. Three requirements: (a) ≥ 3 distinct perspectives on same artifact; (b) disciplinary or stylistic distinction (not duplicates); (c) explicit panel-disagreement logging.

**Evidence grounding.** All three Track B typologies emerged via LUCIA's 5-voice panel (Tuchman, Ibn Khaldun, Achebe, Davis, Kapuscinski). PR-B1 reports 52/66 = 78.8% voice validation; PR-B2 reports 5 engines with 60% non-provincialism and 19 candidates; PR-B3 reports 96.5% closure coverage with 18 types plus auxiliary. Each paper's findings legible as discoveries of the panel's heterogeneous lens.

**Why necessary.** Single-evaluator typology reflects evaluator's priors; cannot claim dimensions outside those priors. Heterogeneous panel discovers dimensions distributed across lenses.

**Why not sufficient.** Heterogeneous panels can still produce non-replicating typologies if C1 or C4 absent.

### 3.4 C4 — Pipeline Discipline with Stage-Wise Review

Codified production stages, each leaving inspectable artifact, review interleaved. Three requirements: (a) ≥ 5 named stages; (b) per-artifact compliance measurable; (c) compliance-score correlation r ≥ 0.3 within-model.

**Evidence grounding.** PR-C2 measured r = 0.46 (CI [0.27, 0.62]) within Sonnet-S2 (n=75). Pooled r = 0.43. Full-vs-deeply-reduced delta +4.7 points. Within-model pipeline effect (~5 pts) > within-pipeline model effect (~1.4 pts). ~21% of within-model score variance explained.

**Why necessary.** Without pipeline discipline, review is ad-hoc; without stage-wise review, discovery-engine has no regular cadence to fire. LUCIA's Innovation Engine fires at Panel-1 and Panel-2 stages — stages whose existence is a pipeline property.

**Why not sufficient.** Disciplined pipeline can execute fixed rubric endlessly without discovering new dimensions (violates C1).

---

## 4. Why These Four — Necessary-But-Not-Sufficient

### 4.1 The Floor Capability

PR-C1's three-way comparison: prose quality near-invariant (1-2 pt noise band); innovation-rate 7.5× Opus-Sonnet (Poisson p ≈ 0.006); reporting 100/100/20% (Fisher p < 0.002). Implication: model substrate is floor condition operating below the four conditions. A model that cannot reliably notice novelty and articulate it crisply cannot produce innovation-log entries C1 requires. A model that cannot reliably report cannot produce artifact trail C4 requires.

We do not add "adequate model substrate" as C5 — it would make the framework untestable (any failure could be attributed to sub-adequate substrate). We state the floor caveat explicitly and operationalize the four conditions conditional on baseline capability (Claude-Sonnet-tier or equivalent).

### 4.2 The Ceiling Caveat — Editor Positionality

Every Track B paper flags editor positionality as companion-gap. C3 operationalizes one dimension (panel heterogeneity) but does not fully close the editor's role in naming categories and adjudicating marginal cases. Even with C1-C4 satisfied and floor-capable substrate, a single editor's framing bounds the typology's reach. The framework does not eliminate editor-positionality; it makes editor-positionality inspectable.

### 4.3 Alternatives Considered and Rejected

- **"Quantitative scoring" as C5** — rejected; qualitative grounded theory produces typologies without numerical scoring.
- **"Corpus scale ≥ N" as C5** — rejected; right scale is domain-dependent and circular.
- **"Human-in-the-loop" as C5** — rejected; already implied by C3 and C4.

---

## 5. Figure Descriptions (PP1-A)

**Figure 1 — Four-condition framework as 2×2 grid plus floor/ceiling.** Four cells labeled C1-C4 (top-left to bottom-right). Each cell contains condition name, one-line summary, primary number from grounding paper:
- C1: "Trigger latency median 1 day; saturation ratio 15% (PR-A1, PR-A3)"
- C2: "0 reversals/15 amendments; 99.6% preservation (PR-A2)"
- C3: "78.8% voice; 60% non-provincialism; 96.5% closure (PR-B1, B2, B3)"
- C4: "r=0.46 within-model; +4.7 pt full-vs-reduced (PR-C2)"

Below grid: dashed band "Floor: adequate model substrate (PR-C1)." Above grid: dashed band "Ceiling: editor positionality." Right-side panel: three candidate corpora with predicted (C1,C2,C3,C4) 4-vectors as bar charts. Legend distinguishes conditions (bold outlines) from floor/ceiling (dashed bands).

**Figure 2 — Evidence map network diagram.** Left column: 8 prior module papers. Right column: 4 conditions. Edges connect papers to conditions with edge labels giving specific primary numbers. Floor/ceiling annotations at top and bottom. Every condition traces to at least one specific quantitative finding from a prior module paper.

---

## 6. Operationalization — Testable Predicates

**C1 — Discovery-driven rubric.**
- P1.1: Written quality rubric with explicit dimensions? (binary)
- P1.2: Codified trigger for amending rubric? (binary)
- P1.3: Inspectable amendment log with dated entries? (binary)
- **C1 score**: 1 if all three true; 0 otherwise.

**C2 — Forward-only amendment.**
- P2.1: Historical scores preserved (version-dated, not re-scored)? (binary)
- P2.2: Extension/refinement/reversal classifier operational? (binary)
- P2.3: Reversal rate ≤ 20%? (graded)
- **C2 score**: 1 if P2.1 and (P2.2 or P2.3); 0.5 if only P2.1; 0 otherwise.

**C3 — Heterogeneous panel review.**
- P3.1: ≥ 3 distinct reviewer perspectives? (binary)
- P3.2: Disciplinarily or stylistically distinct? (binary)
- P3.3: Panel disagreements logged? (binary)
- **C3 score**: 1 if all three; 0.5 if P3.1 and P3.2 only; 0 otherwise.

**C4 — Pipeline discipline.**
- P4.1: ≥ 5 named stages with inspectable artifacts? (binary)
- P4.2: Per-artifact compliance measurable? (binary)
- P4.3: Compliance-score r ≥ 0.3 within-model? (graded)
- **C4 score**: 1 if all three; 0.5 if P4.1 and P4.2 but P4.3 unmeasured; 0 otherwise.

**Aggregate**: 4-vector (C1, C2, C3, C4) ∈ {0, 0.5, 1}⁴. Typology-emergence predicted iff all four components exceed 0.5.

Operationalization designed so that a researcher with access only to corpus's public documentation can score it without inside knowledge.

---

## 7. Falsification Criteria — Pre-Registered Protocol

**Step 1**: Acquire access to external AI-assisted creative corpus.

**Step 2**: Score the corpus on 4-dimensional condition vector using §6 operationalization. Score computed BEFORE inspecting typology-emergence evidence.

**Step 3**: Based on condition vector, predict whether corpus exhibits typology-emergence. Prediction rule: emergence iff all four conditions ≥ 0.5.

**Step 4**: Inspect corpus for typology-emergence signal. Signal defined as: (a) explicitly-documented typology with ≥ 5 distinct entries; (b) new-entry-per-artifact rate declined meaningfully as corpus grew (rate at final cohort ≤ 50% of initial).

**Step 5**: Compare prediction to observation. Falsification conditions:
- **Mismatch-1 (not sufficient)**: corpus scores ≥ 0.5 on all four but shows no emergence.
- **Mismatch-2 (not necessary)**: corpus scores < 0.5 on ≥ 1 condition but shows emergence.
- **Binding**: mismatch in ≥ 1 of 2 external corpora.

**Step 6**: Report transparently, including all predicates and justifications.

---

## 8. Candidate External Corpora

### 8.1 Corpus A — AI-Assisted Code Review Comments

**Source**: Sourcegraph Cody, Copilot-PR, Cursor-PR archives.

**Predicted scores**: C1=0 (no codified amendment trigger), C2=0 (guideline changes retroactive), C3=0.5 (multi-reviewer workflow but often overlapping), C4=varies.

**Predicted emergence**: **NO** — review-comment typology proliferates ad-hoc.

### 8.2 Corpus B — AI-Generated Music with Community Genre Tags

**Source**: Suno, Udio community platforms.

**Predicted scores**: C1=0.5 (community tagging has some pattern-promotion), C2=0 (tags re-assigned retroactively), C3=1 (heterogeneous community evaluators), C4=0 (no pipeline discipline).

**Predicted emergence**: **PARTIAL** — taxonomy grows, does not stabilize.

### 8.3 Corpus C (Optional) — AI-Assisted Scientific Writing

**Source**: arXiv preprints with AI-disclosures; open-review venue commentary.

**Predicted scores**: C1=0.5 (reviewer commentary has ad-hoc discovery), C2=0.5 (venue policies update forward), C3=1 (peer-review panels strongly heterogeneous), C4=1 (peer review is multi-stage pipeline).

**Predicted emergence**: **YES** — closest analog to LUCIA; strongest test.

### 8.4 Why These Three

Corpus A predicts NO; B predicts PARTIAL; C predicts YES. Spread is deliberate — the protocol's value comes from discriminating among predicted outcomes. A framework that predicts emergence everywhere or nowhere cannot be falsified.

Three-corpus ladder is domain-diverse: code, music, science. If framework holds across this diversity, transportability strengthened. If fails in one, failure is localized.

---

## 9. Threats to Validity

### 9.1 Four-Condition Selection Bias

The four conditions were selected from 8 module papers by the same editor. Hostile reviewer may argue conditions are retrojected from LUCIA's operationalizations. **Most acute threat.** Partial defense: each condition grounded in quantitative finding above/below pre-registered threshold. Second-editor framework-enumeration pilot flagged as primary companion measurement.

### 9.2 N=1 Corpus at Registration

Framework grounded in single production record. Our defense: pre-registration is credibility mechanism independent of external execution. Commit to executing protocol against ≥ 1 external corpus within 12 months.

### 9.3 External-Corpus Access Contingencies

Access to Sourcegraph Cody, Suno/Udio, or arXiv AI-disclosure corpora may be restricted. Three candidates mitigate. If no corpus accessible within 12 months, paper should be reclassified as prescriptive methodology rather than falsifiable-in-practice.

### 9.4 Operationalization Collapse

If peer review determines predicates cannot be independently measured on arbitrary external corpus — e.g., P3.2 is inherently judgment-laden — framework falsified at framework tier. Reliability pilot with ≥ 2 independent scorers flagged.

### 9.5 Glaser vs Charmaz

Charmaz-constructivist reviewer may argue the four conditions ARE the framework producing the typology (self-fulfilling). Our defense: typologies tied to specific cross-culture replication evidence, not only framework-produced. Methodological disagreement, not framework failure.

### 9.6 Floor-Capability Unboundedness

"Claude-Sonnet-tier or equivalent" not specified with concrete benchmark. Creates weak unfalsifiability loophole. Mitigation: specify benchmark per domain at protocol-execution time.

### 9.7 FAccT-relevant: Downstream-Use Dynamics

A typology published under the four conditions could be operationalized in ways producing disparate impact. Framework is descriptive-predictive, not prescriptive. We do not claim creative work requires the four conditions; we claim typology-emergence is predicted when conditions hold.

---

## 10. Conclusion

This paper closes the chron module. Across eight prior papers we established AI-assisted creative production at scale can produce typologies as emergent output rather than pre-specified input. This paper proposes the generalization: four conditions — discovery-driven rubric, forward-only amendment, heterogeneous panel review, pipeline discipline — are jointly necessary for typology-emergence in AI-assisted creative production at scale. Each is grounded in a specific primary number from a prior module paper. Model substrate and editor positionality are floor and ceiling caveats.

Per plan.md contingency, external corpora were not acquired within this paper's time budget; we reframe from "An Executed Test" to "A Falsifiable Proposal." The deliverable is the four-condition framework operationalized as testable predicate set, a pre-registered falsification protocol for external-corpus testing, and three identified candidate external corpora with predicted condition status and emergence signal.

The framework is **descriptive-predictive**, not prescriptive. It predicts when typology-emergence occurs under given conditions; it does not require the conditions for creative work to be valuable.

If the four conditions are confirmed across external corpora, typology-emergence becomes a transportable methodology. If falsified, the null fallback is that LUCIA's emergence is a one-corpus curiosity. Either outcome is informative. What the framework does *not* tolerate is ambiguous non-testing; the pre-registered protocol is the mechanism for avoiding that outcome.

**Commitment**: we commit to executing the protocol against ≥ 1 external corpus within 12 months of this paper's acceptance, and to publishing the results regardless of outcome.

We close the chron module with a narrow claim and an open invitation. The narrow claim: four conditions, grounded in quantitative findings, operationalized as testable predicates, pre-registered for external validation. The open invitation: any researcher with access to a suitable external AI-assisted creative corpus can execute the protocol and report the result. The framework is ours; the validation will be collective.

---

## 11. References

- [NEED-1] Ippolito, D. et al. (2022). "Creative Writing with an AI-Powered Writing Assistant." *CHI 2022*.
- [NEED-2] Franceschelli, G. & Musolesi, M. (2023). "On the Creativity of Large Language Models." *arXiv:2304.00008*.
- [NEED-3] Chiang, C.-H. & Lee, H.-Y. (2023). "Can LLMs Be an Alternative to Human Evaluations?" *ACL 2023*.
- [NEED-4] Cartwright, N. & Hardie, J. (2012). *Evidence-Based Policy*. Oxford UP.
- [NEED-5] Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs*. Houghton Mifflin.
- [NEED-6] Liu, X. et al. (2023). "AgentBench." *arXiv:2308.03688*.
- [NEED-7] Mialon, G. et al. (2023). "GAIA." *arXiv:2311.12983*.
- [NEED-8] Liang, P. et al. (2022). "HELM." *arXiv:2211.09110*.
- [NEED-9] Glaser, B. G. & Strauss, A. L. (1967). *The Discovery of Grounded Theory*. Aldine.
- [NEED-10] Charmaz, K. (2006). *Constructing Grounded Theory*. Sage.
- [NEED-11] Bai, Y. et al. (2022). "Constitutional AI." *arXiv:2212.08073*.
- [NEED-12] Ouyang, L. et al. (2022). "Training Language Models to Follow Instructions with Human Feedback." *arXiv:2203.02155*.
- [NEED-13] AERA, APA, NCME (2014). *Standards for Educational and Psychological Testing*. AERA.
- [NEED-14] Stojanovic, L. (2004). "Methods and Tools for Ontology Evolution." PhD, University of Karlsruhe.
- [NEED-15] Gawande, A. (2009). *The Checklist Manifesto*. Metropolitan Books.
- [NEED-16] Chao, A. (1984). "Nonparametric Estimation of the Number of Classes in a Population." *Scandinavian Journal of Statistics* 11.
- [NEED-17] Strauss, A. & Corbin, J. (1990). *Basics of Qualitative Research*. Sage.

Internal (this module): PR-A1, PR-A2, PR-A3, PR-B1, PR-B2, PR-B3, PR-C1, PR-C2.

---

## 12. Artifacts — Evidence Map

| Condition | Grounding paper | Primary number | File |
|-----------|-----------------|----------------|------|
| **C1** (discovery-driven rubric) | PR-A1 | Median trigger latency 1 day; max 2 days | `chron-innovation-engine/main.md` |
| **C1** (convergence) | PR-A3 | Aggregate saturation ratio 15%; stratified 9%/0%/2.86 | `chron-typology-saturation/main.md` |
| **C2** (forward-only) | PR-A2 | 0 reversals/15 amendments; 99.6% preservation; delta +1.75 | `chron-forward-only-amendment/main.md` |
| **C3** (panel, prose) | PR-B1 | 52/66 = 78.8% validation [67.7%, 86.7%]; 88.2% em-dash emergence | `chron-voice-spectrum/main.md` |
| **C3** (panel, arc) | PR-B2 | 5 engines, 4.6 mean cultures/type; non-provincialism 3/5 = 60% | `chron-structural-engines/main.md` |
| **C3** (panel, closure) | PR-B3 | 18-type covers 84.3% [76.5%, 89.9%]; 96.5% with Ongoing | `chron-terminal-conditions/main.md` |
| **C4** (pipeline) | PR-C2 | r = 0.46 [0.27, 0.62] within-Sonnet; +4.7 pts full-vs-reduced | `chron-pipeline-instrument/main.md` |
| **Floor** (substrate) | PR-C1 | Score 81.22/82.50/83.20; innov 0.22/1.67/0.60 (p≈0.006); report 100/100/20% (p<0.002) | `chron-model-substrate/main.md` |

**Source corpus**: LUCIA (`C:\src\chronicle`, master). 115 locked chapters, 93 cultures, 26 regions, 100 adopted amendments v1.0 → v1.7.

**Framework deliverables (this paper)**:
- Four-condition operationalization: §6.
- Pre-registered falsification protocol: §7.
- Candidate external corpora with prediction table: §8.
- Threats and mitigations: §9.

**Falsification thresholds (pre-registered)**:
- Protocol tier: mismatch in ≥ 1 of 2 external corpora.
- Framework tier: operationalization collapses under peer review.

**Result**: framework-status = falsifiable-proposal; external execution pending; 2-3 candidate corpora identified; commitment to execute within 12 months of acceptance.

**Companion measurements flagged**:
- External-corpus acquisition and analysis (Corpora A, B, C).
- Second-editor framework-enumeration reproducibility.
- Operationalization reliability pilot with ≥ 2 independent scorers.
- Floor-capability benchmark specification per domain.
- Longitudinal LUCIA extension to n=500 chapters.
- Internal ablations: C2 violation; C3 collapsed to single-voice; C4 pipeline reduced.

# Model Substrate Effects in Structured Creative Production: Opus vs Sonnet vs Haiku

**Paper**: PR-C1
**Module**: chron (Emergent Typologies in AI-Assisted Creative Production)
**Track**: C — When Typologies Emerge From Production
**Date**: 2026-04-20
**Status**: Draft, round 0
**Dependencies**: PR-A1 (Innovation Engine), PR-B1 (validation method), PR-A2 (forward-only amendment). **Gates PR-C2** and **PR-C3**.

---

## Abstract

Quality rubrics for AI-assisted creative production treat model choice as invariant. We measure whether that assumption holds. LUCIA's Session 2 performed a three-way A/B/C comparison across a Claude-family capability ladder: Region 9 Egypt & Nile (9 chapters, Opus 4.7), Region 12 Central Africa (6 chapters, Sonnet 4.5), Region 26 Pacific Century (5 chapters, Haiku 4.5). Controls: identical 11-stage pipeline, identical five-voice reviewer panel, identical scoring rubric (v1.6). Primary measurements in matched conditions: mean GATE-2 combined score Opus 81.22 (SD 1.09) vs Sonnet 82.50 (SD 2.26) vs Haiku 83.20 (SD 0.84); innovations-per-chapter rate Opus 0.22 vs Sonnet 1.67 vs Haiku 0.60; clean end-of-spawn reporting rate Opus 100% (Wilson 95% CI [67.6%, 100%]) vs Sonnet 100% (Wilson 95% CI [61.0%, 100%]) vs Haiku 20% (Wilson 95% CI [3.6%, 62.5%]). Statistical inference: Opus-Sonnet score contrast Welch's t p≈0.24 (NS) but Mann-Whitney U z=-2.12, p≈0.034 (MS); Opus-Sonnet innovation-rate exact Poisson p≈0.006 (significant); Opus+Sonnet vs Haiku reporting Fisher's exact p<0.002 (significant). The Haiku "failure" is NOT a prose-quality failure — its mean score is the highest of the three. The failure is at the margin of process: missing end-of-spawn summaries, inconsistent file naming, requires LUCY-side manual reconstruction. We position against LLM benchmarking (HELM, BIG-bench), creativity-evaluation (Franceschelli & Musolesi 2023), and model-as-noise (LIMA). The whitespace: first empirical three-way A/B/C comparison on a structured creative-production task with a discovery-driven, forward-only, panel-reviewed rubric and a codified 11-stage pipeline. We commit to Glaser-style data-driven grounded theory, report Wilson and t-test CIs on all primary numbers, disclose human editor role in spawn-report verification, and explicitly name cross-paper dependencies. The primary contribution decomposes "quality" into three orthogonal substrate-sensitive dimensions: prose-at-the-artifact, discovery-around-the-artifact, process-reporting-about-the-artifact. PR-C2 isolates the pipeline-discipline component; this paper establishes that model substrate matters even after pipeline is fixed, but only on two of the three dimensions.

---

## 1. Introduction

The literature on LLM capability evaluation has grown around two measurement instruments. First, prompt-set benchmarks: HELM (Liang et al. 2022), BIG-bench, MMLU score models on short-to-medium-length tasks against fixed rubrics. Second, LLM-as-judge: for open-ended creative output, a more-capable model grades a less-capable model's output. Both instruments share an assumption: the artifact of interest is instantaneous or single-turn.

Structured creative production at scale is different. LUCIA is a 115-chapter narrative encyclopedia covering 93+ cultures across 26 regions, produced by SCRIBE agents supervised by a human editor and a five-voice AI panel under an 11-stage pipeline. Each chapter passes through opening-writing, gate scoring, panel review (five voices), notes production, second-panel review, writing of the 5,000-word chapter, gate-2 scoring, cleanup, board review, final lockdown. The artifact is not the single chapter; it is the chapter *plus* the trail of review files *plus* the innovations discovered during review *plus* the reliable end-of-spawn report.

When we ask whether model choice matters, we must ask the question at each level. Standard benchmarks answer "is model M more capable than model N on task T?" They do not answer: does the model notice novelty and articulate it crisply? Does the model complete the pipeline as instructed? Does the model report reliably? These are the substrate-effect questions this paper measures.

### 1.1 Claim

We claim: *Model substrate, across the Opus/Sonnet/Haiku capability ladder on matched structured-creative-production conditions, produces significantly different outcomes on innovation-discovery rate and on pipeline-and-reporting compliance, while producing prose-quality differences within the 1-2 point noise band of a 90-point rubric. Substrate matters — but on two of three measured dimensions, not primarily on the prose-quality dimension that prompt-set benchmarks target.*

### 1.2 Falsification

We pre-register: all three models produce statistically indistinguishable score distributions AND indistinguishable innovation rates AND indistinguishable reporting-compliance rates → substrate thesis falsified; pipeline (C2) dominates entirely. The null fallback reframes C1 as a pilot case study without a substrate claim. The falsification is not triggered by the data in §5: innovation-rate and reporting-compliance contrasts are significant at p < 0.01 and p < 0.002 respectively.

### 1.3 Contribution

Fourfold. First, we articulate three orthogonal substrate-sensitive dimensions — prose quality, innovation discovery, process reporting — and measure all three in a single matched-condition experiment. Second, we demonstrate that the three dimensions respond differently to substrate: quality near-invariant, discovery 7.5×-divergent, process 5×-divergent. Third, we document the specific Haiku failure mode — writes adequate prose but cannot be trusted to report what it did — and argue this is a distinct failure mode that prompt-set benchmarks cannot detect. Fourth, we hand to PR-C2 the cross-model dataset and the Opus paradox (strong spawn-reports, weak artifact trails) that C2 needs to isolate pipeline effect from model effect.

### 1.4 Scope

This paper does not claim:
- Transportability to non-narrative creative domains (PR-C3).
- Independence from the 11-stage pipeline (PR-C2 tests the converse).
- Independence from the specific human editor (companion reproducibility study).
- Independence from model-version drift (pinned to Opus 4.7, Sonnet 4.5, Haiku 4.5).
- Substrate effects on models outside the Claude family.

Depends on: PR-A1 (innovation unit), PR-B1 (validation criterion), PR-A2 (cross-session comparability).

---

## 2. Related Work

### 2.1 HELM and Open-Ended LLM Benchmarking

HELM (Liang et al. 2022 [NEED-1]) holistically evaluates LLMs across scenarios × metrics. HELM's metric space includes accuracy, calibration, robustness, fairness, toxicity; it does not include pipeline-compliance-over-multi-stage-production. A HELM-trained reviewer would reasonably ask whether our Opus/Sonnet/Haiku comparison is recoverable from published HELM scorecards. It is not: HELM does not grade "does the model reliably deliver an end-of-spawn summary after an 11-stage production." The capability is not in HELM's metric space because HELM does not run multi-stage productions. The implication is that the benchmarking enterprise and the production-at-scale enterprise may not be testing the same underlying capability.

### 2.2 BIG-bench and Task-Coverage Creativity

BIG-bench (Srivastava et al. 2022 [NEED-2]) expands task coverage into creative and reasoning-heavy territory. Evaluation is one-shot: prompt, output, score. BIG-bench does not run multi-pass production or pipeline-compliance. The most relevant BIG-bench family is "emergent abilities" — capabilities that appear only at scale. The ability LUCIA's Haiku cell fails (reliable end-of-spawn reporting) is a candidate emergent ability not in the BIG-bench set.

### 2.3 Creativity Evaluation in LLMs

Franceschelli & Musolesi (2023) [NEED-4] survey creativity evaluation in LLMs and argue existing metrics are proxies. Their critique applies to one-shot creative generation. Our contribution is adjacent: discovery-rate-per-chapter is a measurable creativity-adjacent signal that differs across models by ~7.5× in matched conditions. It complements one-shot creativity scoring; it does not replace it.

### 2.4 Model-as-Noise Arguments: LIMA

Zhou et al. (2023) [NEED-3] demonstrate that alignment is primarily a data-curation problem. A LIMA-style reviewer may argue that LUCIA's observed differences are accountable not by substrate but by post-training data-mix differences. We cannot decompose substrate into pre-training vs post-training with LUCIA data alone. We claim only that the three Claude-family models, as deployed in production, differ on the three measured dimensions.

### 2.5 Pipeline-as-Instrument: Agent Frameworks

The agent-frameworks literature (ReAct; Yao et al. 2023 [NEED-10]; AgentBench [NEED-11]; GAIA [NEED-12]) has converged on pipeline structure as load-bearing for multi-step tasks. Our finding that pipeline-reporting-compliance varies sharply with substrate complements this literature: even with a fixed pipeline specification, different models execute it with different reliability.

### 2.6 Grounded Theory: Glaser Commitment (PP1-E)

Following PR-A1's and Track B's commitment, we adopt Glaser-style data-driven grounded theory. The three-way A/B/C comparison was not pre-stratified at module design; it emerged from Session 2's production sequence. The substrate hypothesis crystallized after observing the pipeline-reporting reliability gap. We pre-committed falsification conditions at module-design time (2026-04-19); point-estimate results were observed before pre-registration. We reject the Charmaz constructivist move: the reporting-compliance difference is ratio-scale measurable (1/5 vs 14/14) and does not depend on editorial framing.

---

## 3. Method

### 3.1 Model Versions and Production Window

| Cell | Region | SCRIBE model | Production window | Rubric version |
|------|--------|--------------|-------------------|----------------|
| A (Opus) | 09-egypt-nile | Opus 4.7 | 2026-04-16 | v1.3-v1.4 |
| B (Sonnet) | 12-central-africa | Sonnet 4.5 | 2026-04-17 | v1.5-v1.6 |
| C (Haiku) | 26-pacific-century | Haiku 4.5 | 2026-04-18 | v1.6 |

Forward-only amendment (PR-A2) preserves score comparability: 0 reversals across v1.0-v1.7 and 99.6% line-preservation support this.

### 3.2 Matched Conditions

**Controlled**: 11-stage pipeline; five-voice panel; 90-point rubric; source tiers; 5,000-word target; editorial philosophy.

**Uncontrolled (threats §7)**: Region topic source-density; prior session learning; chapter count.

### 3.3 Measurements

**M1 — Mean GATE-2 combined score.** Each chapter has a GATE-2 + GATE-1 combined score (0-90). Source: `reviews/GATE-2*.md` files plus `agents/AGENT-ROSTER.md` Session 2 scoring table (editor's canonical ledger).

**M2 — Innovations-per-chapter rate.** An innovation is a technique promoted to `scoring/INNOVATIONS.md` through PR-A1's two-trigger rule. Source: direct count by region path.

**M3 — Clean end-of-spawn reporting rate.** Presence of well-structured FINAL.md at predictable path, readable without editor reconstruction. Source: `agents/AGENT-ROSTER.md` Model Comparison Summary.

### 3.4 Role of the Human Editor (PP1-D)

1. **Spawn-completion verification.** Editor reads spawn report, checks artifact presence, marks chapter locked or returns it. Haiku 1/5 clean-report rate reflects 4 Haiku spawns where editor reconstructed outcome from auxiliary files.
2. **Score ledger maintenance.** `agents/AGENT-ROSTER.md` is canonical. For chapters where GATE-2 scoring occurred without separate GATE-2.md, the roster record is primary.
3. **Innovation-attribution adjudication.** Path-explicit; no adjudication required in our data.
4. **Pre-registration of falsification thresholds.** Pre-registered 2026-04-19, after Session 2 closed but before any statistical analysis.

Companion: second-editor reproducibility study flagged.

### 3.5 Pre-Registered Thresholds

All pairwise score contrasts NS (p > 0.05) AND all innovation-rate contrasts NS AND all reporting-compliance contrasts NS → substrate thesis falsified.

---

## 4. Data

**Layer 1**: 20 chapters across three cells with chapter.md, opening.md, notes.md, figures.md plus reviews directories. Review-file count: Egypt 12.2/chapter; Central Africa 15.3/chapter; Pacific Century 11.8/chapter.

**Layer 2**: `scoring/INNOVATIONS.md` — grep `regions/09-egypt-nile` returns 2; `regions/12-central-africa` 10; `regions/26-pacific-century` 3.

**Layer 3**: `agents/AGENT-ROSTER.md` Session 2 sweep tables enumerate every chapter with score. `agents/LUCY-HANDOFF-S02.md` §Key Decisions #1 narrates the three-way comparison and records Sonnet-as-default-SCRIBE.

---

## 5. Results

### 5.1 Mean GATE-2 Combined Score

**Opus (n=9)**: Great Pyramids 81, Kerma 82, Desert Fathers 82, Meroë 82, Amarna 82, Ptolemaic Founding 82, Julio-Claudian 81, Naqada I 80, First Intermediate 79. **Mean 81.22, SD 1.09.**

**Sonnet (n=6)**: Mangbetu 84, Teke 84, Equatorial Forest 83, Kongo 83, Luba 83, Lunda 78. **Mean 82.50, SD 2.26.**

**Haiku (n=5)**: Bakumatsu 83, ROC 82, PRC 83, S. Korea 84, N. Korea 84. **Mean 83.20, SD 0.84.**

### 5.2 Pairwise Statistical Inference on Score

**Opus vs Sonnet.** Welch's t: t=1.29, df=6.59, p≈0.24 (NS). Mann-Whitney U: U=9, z=-2.12, p≈0.034 (MS). Cohen's d = 0.779 (medium-large). The disagreement is expected: t is under-powered on n=9, n=6; rank test picks up the consistent central-tendency shift. 95% t-interval on difference: [−1.14, +3.70].

**Opus vs Haiku.** Welch's t: t=3.79, df≈11.2, p≈0.003. Significant — but within a 2-point band on 90-point scale; Haiku benefited from latest rubric (v1.6) shaped by Sonnet and Opus findings.

**Sonnet vs Haiku.** Welch's t: t=0.70, df≈8.6, p≈0.50. NS.

**Kruskal-Wallis (3-way)**: H=5.52, df=2, p≈0.063. Borderline at α=0.05.

The score-dimension falsification is not cleanly triggered or cleanly rejected by score alone; the bundle-level falsification is the decisive frame.

### 5.3 Innovations-per-chapter Rate

| Cell | Innovations | Chapters | Rate |
|------|-------------|----------|------|
| Opus | 2 | 9 | 0.222 |
| Sonnet | 10 | 6 | 1.667 |
| Haiku | 3 | 5 | 0.600 |

The two Opus innovations are both sourced to Old Kingdom Great Pyramids — a single chapter. Eight of nine Opus chapters contributed zero. The ten Sonnet innovations span five of six chapters. The three Haiku innovations are all from Modern Korea South.

**Exact Poisson rate-ratio test, Opus vs Sonnet.** Under H₀ (equal per-chapter rates), Sonnet innovations ~ Binomial(12, 0.4). Observed: 10. P(X ≥ 10) = 0.00281. Two-sided p ≈ 0.0056. **Significant at α=0.01.**

**Rate ratio**: Sonnet/Opus = 7.50. 95% Wald CI: [2.39, 23.5]. Lower bound well above unity.

### 5.4 Pipeline-and-Reporting Compliance

**Accounting A — Clean end-of-spawn report:**

| Cell | Clean | Chapters | Rate | Wilson 95% CI |
|------|-------|----------|------|---------------|
| Opus | 8 | 8 | 100% | [67.6%, 100%] |
| Sonnet | 6 | 6 | 100% | [61.0%, 100%] |
| Haiku | 1 | 5 | 20% | [3.6%, 62.5%] |

**Fisher's exact, Opus+Sonnet vs Haiku**: p ≈ 0.00129. **Significant.**

**Accounting B — Artifact-level pipeline completion (files-on-disk):**

| Cell | Mean stages | /11 | Rate |
|------|-------------|-----|------|
| Opus | 4.67 | /11 | 42% |
| Sonnet | 8.50 | /11 | 77% |
| Haiku | 8.40 | /11 | 76% |

Accounting B reverses Accounting A's narrative. Opus delivers clean spawn reports but leaves sparsest artifact trail. This is the **Opus paradox**: the highest-capability model delivers cleanest spawn reports but fewest intermediate artifacts. Interpretation: Opus, being less error-prone, was trusted by the editor to skip explicit reviewer-file materialization. Editor-behavior confound — flag for C2's pipeline-isolation work.

### 5.5 Figure Descriptions (PP1-A)

**Figure 1** — Grouped bar chart of mean GATE-2 combined score per model, y-axis [75, 90], with 95% t-interval error bars. Opus 81.22 ± 0.84, Sonnet 82.50 ± 2.37, Haiku 83.20 ± 1.04. Horizontal reference lines at y=72 (chapter target) and y=75 (manuscript-mean target). Above-target shaded zone [74, 90]. Legend: "Opus 4.7, Sonnet 4.5, Haiku 4.5; LUCIA Session 2 matched-region experiment."

**Figure 2** — Three-panel comparison.
- Panel (a): Box plot of GATE-2 scores per model. Opus tight around 82 with outlier at 79; Sonnet wide with 78 Lunda outlier; Haiku tight around 83-84.
- Panel (b): Bar chart of innovations-per-chapter rate. Opus 0.222, Sonnet 1.667, Haiku 0.600. 95% Poisson CIs as error bars. Horizontal reference at y=1.0.
- Panel (c): Two-tone stacked bar per model showing clean-report vs unclean-report rates. Opus 100/0, Sonnet 100/0, Haiku 20/80.

### 5.6 The Haiku Failure Mode

Four Haiku chapters with unclean reports:
- Bakumatsu: pipeline 11/11 claimed, no report file.
- S. Korea Japanese Colonization: pipeline 11/11 claimed, score (84) reconstructed from `CHAPTER-LOCKED.txt`.
- N. Korea Haebang: pipeline 11/11 claimed, score reconstructed from `FINAL-SUMMARY.md`.
- PRC Jiefang: pipeline 9/11 incomplete, score reconstructed from `CHECKPOINT-Stage-10-11.md` and `FINAL-REPORT.md`.

One clean: ROC Century of Humiliation: 11/11 pipeline, clean summary.

Three manifestations:
1. **Silence at completion** (Japan, S. Korea, N. Korea): ceases activity without filing summary.
2. **Partial file-naming drift** (PRC): produces summary at non-standard paths.
3. **Mid-pipeline stall with recovery-at-unknown-status** (PRC): 9/11 complete, no clean delivery.

None of these manifestations appeared in any Opus or Sonnet chapter.

### 5.7 Falsification Result

Two of three dimensions clear significance by margin. The score dimension is borderline by parametric test, more clearly significant by rank test. **The substrate-invariance null is rejected at the bundle level.**

---

## 6. Discussion

### 6.1 Decomposing "Quality" into Substrate-Sensitive Dimensions

The primary theoretical contribution is the decomposition. "Whether the model matters for creative production quality" usually means a scalar — scores — and finds the dependency small (1-2 points on 90). Our data supports this only at the scalar scoring level. Widen the aperture to discovery and to process-reporting, and substrate dependency becomes sharp: 7.5× on innovations, 5× on reporting.

Three orthogonal dimensions:
- **Prose-at-the-artifact**: what the rubric explicitly evaluates. Near-saturated for all three.
- **Discovery-around-the-artifact**: whether the model notices novelty and articulates it crisply enough for two-trigger rule promotion.
- **Process-reporting-about-the-artifact**: whether the model reliably delivers an end-of-work summary.

A benchmark measuring only (1) would conclude substrate near-invariant. Adding (2) and (3) would conclude substrate matters a lot. HELM and BIG-bench measure neither (2) nor (3); this is the whitespace.

### 6.2 The Default-SCRIBE Decision

Sonnet becomes default; Opus reserved for hardest chapters; Haiku dropped. Through this paper's frame:
- **Sonnet dominates Opus on (2)** at 7.5× innovation rate. On (1) Sonnet noise-bounded above Opus. On (3) tied.
- **Sonnet dominates Haiku on (3)** at 5× reporting reliability. On (1) and (2) not significantly different.
- **Opus-escalation rule**: Opus does not dominate Sonnet on any measured dimension — so Opus's use-case is *where Sonnet did not suffice*.

### 6.3 The Haiku Failure Is Not a Prose Failure

Haiku's mean GATE-2 (83.20) is the highest of the three cells. Haiku does not write bad chapters for LUCIA.

Haiku fails at agent reliability — the ability to execute a multi-step task *and report on what was executed*. The 20% clean-report rate is a reliable capability deficit at this model scale. A researcher using Haiku for one-shot chapter generation with manual oversight would not observe this failure. Automated multi-chapter production with an editor consuming structured summaries exposes it immediately.

### 6.4 Cross-Paper Dependencies (PP1-C)

**Upstream**:
- **PR-A1**: "innovation" unit defined by two-trigger promotion rule.
- **PR-B1**: validation method (≥ 2-instance cross-culture).
- **PR-A2**: forward-only amendment enables cross-session comparability.

**Downstream**:
- **PR-C2**: isolates pipeline-compliance's correlation with score, stratified by model. Needs C1's cross-model dataset + Opus paradox.
- **PR-C3**: proposes four necessary conditions. C1's evidence that some dimensions are substrate-sensitive implies C3's conditions are necessary-but-not-sufficient.

### 6.5 Glaser Commitment (PP1-E)

The A/B/C comparison emerged from Session 2's production sequence, not pre-specified design. Falsification pre-registered 2026-04-19 before statistical analysis. The 1/5 vs 14/14 ratio is ratio-scale measurable; the 0.22 vs 1.67 rate is count-based; the 81.22 vs 82.50 means are arithmetic over editor-recorded scores. Measurements are data-driven.

### 6.6 What This Paper Does Not Claim

Substrate effects on dimensions beyond the three measured; on non-Claude families; model-version independence; editor-independence; statistical-power sufficiency on score; transportability to non-narrative domains; causal decomposition of substrate into pre-/post-training components.

---

## 7. Threats to Validity

### 7.1 Small-Sample Power
n=9, 6, 5. t-test under-powered on Opus-Sonnet; rank test marginally significant; effect size d=0.779 meaningful. Innovation-rate and reporting contrasts significant with large effect ratios. Matched-pair supplementary flagged.

### 7.2 Region-Difficulty Confound
Egypt, Central Africa, Pacific Century differ in source-density. All three cross 75/90 target, supporting adequate source-support across topics. Cross-model re-scoring of a shared region would directly address; flagged as companion.

### 7.3 Self-Scoring Confound
All GATE-2 scores assigned by the writing SCRIBE. Blind cross-model re-score would detect self-assessment bias. Flagged companion.

### 7.4 Editor-Behavior Confound on Pipeline Artifacts
Opus paradox — 42% artifact completion with 100% reporting compliance — partially explained by editor behavior (early session trusted Opus; later sessions requested explicit artifacts). C2 addresses within-model correlation.

### 7.5 Rubric-Version Confound
Opus v1.3-v1.4; Sonnet v1.5-v1.6; Haiku v1.6. PR-A2's 0-reversal result supports comparability. PR-A2's 20-chapter re-score showed +1.75 mean delta (small bias toward later versions). Companion.

---

## 8. Conclusion

LUCIA's Session 2 three-way A/B/C comparison measures substrate effects in structured creative production along three orthogonal dimensions. Prose-quality differences within 1-2 point noise band (Opus 81.22, Sonnet 82.50, Haiku 83.20). Innovation-discovery-rate differences 7.5× at point estimate with Poisson p ≈ 0.006. Pipeline-reporting-reliability differences 5× (Opus 100%, Sonnet 100%, Haiku 20%) with Fisher's exact p < 0.002.

Substrate matters. But on two of three dimensions, not primarily on prose-quality. The default-SCRIBE decision (Sonnet) follows from the bundle: matches Opus on score, dominates 7.5× on discovery, matches on reporting, dominates Haiku 5× on reporting. Opus-escalation (hardest chapters) follows from absence of Opus-dominating-Sonnet on any measured dimension. Haiku-drop follows from reporting failure — NOT prose failure. Haiku writes adequately; Haiku cannot be trusted to summarize what it wrote.

This paper gates PR-C2 (pipeline as epistemic instrument) and PR-C3 (conditions for typology emergence). The causal chain from substrate (C1) to pipeline (C2) to general conditions (C3) rests on C1's finding that substrate dependency exists but is heterogeneous across dimensions — a finding that makes the pipeline-dominates alternative (C2's null) testable and makes the four-condition framework (C3's proposal) necessary-but-not-sufficient.

---

## 9. References

- [NEED-1] Liang, P. et al. (2022). "Holistic Evaluation of Language Models." arXiv:2211.09110.
- [NEED-2] Srivastava, A. et al. (2022). "BIG-bench." arXiv:2206.04615.
- [NEED-3] Zhou, C. et al. (2023). "LIMA." NeurIPS 2023.
- [NEED-4] Franceschelli, G. & Musolesi, M. (2023). "On the Creativity of LLMs." arXiv:2304.00008.
- [NEED-5] Ippolito, D. et al. (2022). "Creative Writing with a Machine in the Loop." CHI 2022.
- [NEED-6] Anthropic. Claude 4.x model cards.
- [NEED-7] Chiang, C.-H. & Lee, H.-Y. (2023). "Can LLMs Be an Alternative to Human Evaluations?" ACL 2023.
- [NEED-8] Zheng, L. et al. (2023). "Judging LLM-as-a-Judge with MT-Bench." NeurIPS D&B 2023.
- [NEED-9] Bai, Y. et al. (2022). "Constitutional AI." arXiv:2212.08073.
- [NEED-10] Yao, S. et al. (2023). "ReAct." ICLR 2023.
- [NEED-11] Liu, X. et al. (2023). "AgentBench." arXiv:2308.03688.
- [NEED-12] Mialon, G. et al. (2023). "GAIA." arXiv:2311.12983.

Internal: PR-A1, PR-A2, PR-B1 (this module); LUCIA data `C:\src\chronicle\agents\AGENT-ROSTER.md`, `LUCY-HANDOFF-S02.md`, `scoring/INNOVATIONS.md`, `TRACKER.md`.

---

## 10. Artifacts

| Artifact | Value | CI / Test |
|----------|-------|-----------|
| Mean GATE-2 Opus (n=9) | 81.22 | SD 1.09; 95% t-int [80.38, 82.06] |
| Mean GATE-2 Sonnet (n=6) | 82.50 | SD 2.26; 95% t-int [80.13, 84.87] |
| Mean GATE-2 Haiku (n=5) | 83.20 | SD 0.84; 95% t-int [82.16, 84.24] |
| Opus-Sonnet Welch t | t=1.29, df=6.59 | p ≈ 0.24 (NS) |
| Opus-Sonnet Mann-Whitney U | U=9, z=-2.12 | p ≈ 0.034 (MS) |
| Opus-Sonnet Cohen's d | 0.779 | medium-large |
| Opus-Haiku Welch t | t=3.79, df≈11.2 | p ≈ 0.003 (S) |
| Kruskal-Wallis (3-way) | H=5.52, df=2 | p ≈ 0.063 (borderline) |
| Innov/chapter Opus | 0.222 | 95% Poisson [0.027, 0.803] |
| Innov/chapter Sonnet | 1.667 | 95% Poisson [0.799, 3.063] |
| Innov/chapter Haiku | 0.600 | 95% Poisson [0.124, 1.754] |
| Rate ratio Sonnet/Opus | 7.50 | 95% Wald [2.39, 23.5] |
| Poisson exact Opus-Sonnet | p ≈ 0.0056 | S |
| Reporting rate Opus | 8/8 = 100% | Wilson [67.6%, 100%] |
| Reporting rate Sonnet | 6/6 = 100% | Wilson [61.0%, 100%] |
| Reporting rate Haiku | 1/5 = 20% | Wilson [3.6%, 62.5%] |
| Fisher exact Opus+Sonnet vs Haiku | p < 0.002 | S |
| Artifact-level completion Opus | 4.67/11 = 42% | — |
| Artifact-level completion Sonnet | 8.50/11 = 77% | — |
| Artifact-level completion Haiku | 8.40/11 = 76% | — |

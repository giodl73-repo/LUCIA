# Forward-Only Rubric Evolution: Stability Under a Discovery-Driven Quality Standard

**Paper**: PR-A2
**Module**: chron (Emergent Typologies in AI-Assisted Creative Production)
**Track**: A — The Discovery Engine
**Date**: 2026-04-19
**Status**: Draft, round 0
**Dependencies**: PR-A1 (Innovation Engine trigger mechanism); gates PR-A3 (typology saturation).

---

## Abstract

A quality rubric that evolves during production faces an unavoidable question: what to do about the scores already recorded under earlier versions. Three policies answer it. Retroactive rescoring re-applies the current rubric to every prior artifact. Bidirectional migration, borrowed from ontology evolution, defines mapping functions between versions. Forward-only amendment — the policy this paper examines — applies new bars only to artifacts scored after the amendment, preserving historical scores as archival data points. We document forward-only as operated in LUCIA, a 115-chapter narrative encyclopedia whose rubric evolved from v1.0 through v1.7 across seven amendment cycles over five days of production. We measure stability along three axes. First, we classify every amendment against a pre-registered Extension / Refinement / Reversal rule: 12 Extensions, 3 Refinements, 0 Reversals. Second, we compute a forward-overlay metric from git diff: 243 of 244 v1.0 lines are preserved in v1.7 (99.6% line preservation). Of v1.7's 4,289 words, 54.3% are content added after v1.0. Third, we run a counterfactual re-score pilot on 4 early Session-1 chapters whose own innovations seeded later amendments: mean GATE-2 delta under v1.7 anchors is +1.75 points (range +1 to +2; uniformly positive). Both pre-registered falsification thresholds hold (0 < 3; 1.75 < 8). We position the policy against test-taker fairness doctrine (the legitimizing ancestor), ontology evolution (a strictly stronger alternative), and ML benchmark versioning (a convergent practice). The pilot sample is small and same-author rather than independent-blind; full 20-chapter blind re-scoring is proposed as companion measurement.

---

## 1. Introduction

The companion paper to this one (PR-A1) measures how a quality rubric for AI-assisted creative production can evolve during the production itself, through an Innovation Engine that promotes observed patterns into formal amendments via a 2-instance and a 3-cluster trigger. A2 is a distinct question. If the rubric is evolving, what happens to scores recorded under earlier versions?

Three answers are defensible. The first is **retroactive rescoring**: every time the rubric changes, every prior artifact is re-scored against the new rubric, and historical records are superseded. This is the policy of most ML benchmarks that issue a corrected evaluation harness; it is also the policy of grading systems that publish a revised rubric mid-term and re-grade previously submitted work. Its strength is that all scores in the corpus are directly comparable. Its weakness is the labor cost (re-scoring the whole corpus at every amendment) and a subtler legitimacy problem: when the amendment is *triggered by* patterns the earlier artifacts revealed, re-scoring them on that basis is circular — the chapters are penalized for not meeting a bar they themselves produced.

The second answer is **bidirectional migration**, borrowed from ontology evolution [NEED-A]. At every version bump, explicit mapping functions are defined so that scores can be translated between versions in both directions. This is the strongest policy on comparability grounds; its cost is the requirement that every amendment come with an associated mapping, which is operationally demanding and often mathematically under-constrained when the amendment introduces a genuinely new dimension.

The third answer is **forward-only amendment**: the policy we document and measure. New bars apply only to chapters scored after the amendment; chapters scored under earlier rubric versions are not re-scored. The legitimizing doctrine is from educational measurement: AERA/APA/NCME Standards for Educational and Psychological Testing hold that a test-taker should be judged by the standard in force at the time of testing, not by a standard introduced after [NEED-C]. Forward-only transposes this principle into an AI-assisted creative production setting, where the "test-takers" are the chapters themselves.

Forward-only is the weakest of the three policies on retroactive comparability: it explicitly declines to bring historical scores forward. The question this paper answers is whether forward-only produces a *stable* evolution in the operational sense — whether the rubric's amendments over time are genuinely additive (so the earlier scores remain legitimate against the preserved portions of the rubric), or whether forward-only masks silent drift.

### 1.1 Claim

We claim: *LUCIA's forward-only amendment policy, applied to a rubric that evolved from v1.0 through v1.7 across seven amendment cycles, produces stable evolution measurable along three axes — zero classified reversals under a pre-registered classifier, > 99% line preservation from v1.0 to v1.7, and mean absolute counterfactual re-score delta < 2 points on a pilot of 4 early chapters.*

### 1.2 Falsification

We pre-register two falsification thresholds (from plan.md): **≥ 3 classified reversals across 7 amendment cycles**, OR **mean absolute re-score delta > 8 points** on the pilot chapters. Either condition would indicate that forward-only is masking drift rather than producing additive evolution.

### 1.3 Contribution

Our contribution is threefold. First, we propose an Extension / Refinement / Reversal classifier for rubric amendments, with explicit criteria such that any reader can reproduce the classification from the rubric's git log and changelog. Second, we introduce a **forward-overlay metric** — the fraction of the current rubric's content (lines or words) that was added after v1.0, computed from the diff. High preservation plus substantive added content is the structural signature of additive evolution. Third, we run a counterfactual re-score pilot that deliberately selects chapters whose own innovations seeded later amendments: these are the chapters most likely to reveal drift if the forward-only policy is masking it, because they are the chapters whose ceiling was raised by their own prior contributions.

### 1.4 Scope

This paper is not about whether LUCIA's rubric is the right rubric, nor about whether forward-only generalizes to all AI-assisted creative domains. It is about whether forward-only, as operated on one 115-chapter corpus over seven amendment cycles, produced stable or drifting evolution. Generalization is PR-C3's subject. The Innovation Engine's trigger mechanism — which determines *whether* the rubric evolves — is PR-A1's subject; this paper takes the engine's output as a given and measures the downstream stability of the forward-only application policy.

---

## 2. Related Work

### 2.1 Test-Taker Fairness and Equating

The closest normative ancestor is the doctrine of test-taker fairness codified in the AERA/APA/NCME *Standards for Educational and Psychological Testing* [NEED-C]. Standard 5.16 (on fairness) and the broader framework of *equating* hold that when a test is revised, the test-taker who took the earlier form should be evaluated against the earlier form's standard — equating procedures preserve score comparability without re-scoring prior administrations. Our forward-only policy is operationally equivalent to equating's fairness principle transposed to an AI-assisted creative production setting: a chapter scored under v1.0 is judged by v1.0's anchors, not by v1.7's.

The equating literature assumes the construct being measured is stable across test forms — only the surface items change. Our setting violates this assumption: the rubric's dimensions themselves are discovered during production (PR-A1). We therefore cannot rely on equating mathematics directly. What we can inherit is the fairness *principle*: the test-taker is judged by the standard in force at the time of testing, and any amendment to the standard applies forward only. This paper's measurement is, in effect, an empirical stability check on that principle applied to an evolving construct.

### 2.2 Ontology Evolution and Versioning

The ontology-evolution literature offers a strictly stronger policy: bidirectional migration through explicit change operators [NEED-A]. Stojanovic and colleagues enumerate a taxonomy of change operations (add concept, delete concept, generalize, specialize, merge, split) each paired with a migration function for existing data. OntoClean's meta-property analysis provides a semantic check for consistency-preserving changes.

Forward-only is strictly weaker than ontology versioning on retroactive comparability: we do not supply migration functions. We argue the weaker policy is sufficient in our setting because scores in LUCIA are *archival data points* — records of how each chapter was judged at the time of review — not active classifications that need to be queryable against the current schema. If a downstream consumer of the scores requires comparability across rubric versions, they must interpret the score alongside the version number, exactly as a benchmark consumer interprets a model score alongside the benchmark version.

### 2.3 Rubric Calibration and Rater Reliability

Educational measurement has an extensive literature on rubric calibration — how to train raters to apply a rubric consistently, how to detect rater drift, and how to re-calibrate over time [NEED-B]. Jonsson and Svingby's systematic review of scoring-rubric reliability establishes that inter-rater agreement is the principal stability measurement for a fixed rubric. Wolfe and colleagues' work on rater calibration addresses drift at the *rater* level (the same rater applies the same rubric differently over time).

This literature is valuable for evaluating whether a rubric is applied consistently; it does not address the case where the rubric text itself changes during the corpus's production. Our forward-overlay metric is the structural counterpart to inter-rater reliability: where inter-rater reliability measures whether different raters agree under the same rubric, forward-overlay measures whether the same rubric, at different versions, preserves its earlier text. The two measurements are complementary and address different failure modes.

### 2.4 ML Benchmark Versioning

ML benchmarks such as HELM [NEED-D], BIG-bench, and MMLU revisions have converged on a versioning practice that matches forward-only in spirit: when the benchmark is revised, the prior version is preserved, and model scores are reported against the version under which they were evaluated. Benchmark consumers are expected to interpret a score with its version. This is the same operational structure LUCIA uses, in a different artifact domain. We treat benchmark versioning as parallel convergent practice rather than a literature ancestor; the underlying fairness principle is the test-taker-fairness doctrine already discussed in §2.1.

### 2.5 Grounded Theory on Refinement and Saturation

Grounded theory's literature on category refinement versus reversal [NEED-E] is relevant to our Extension/Refinement/Reversal classifier. In Charmaz's constructivist grounded theory, categories are refined as new data is encountered: the category's definition may be tightened, its boundaries clarified, or sub-categories added, without the original category being withdrawn. A reversal (the category is abandoned or contradicted) is a different operation — and it is rare in mature grounded-theory analyses, where the discipline is to treat emergent categories as provisional until saturation. Our classifier follows this same logic: a Refinement preserves the earlier clause's direction while clarifying; a Reversal materially overturns it.

---

## 3. Background: LUCIA's Forward-Only Policy

### 3.1 The Policy as Stated

LUCIA's forward-only policy is stated verbatim in `scoring/RUBRIC.md` §"How Rubric Versions Work," step 5: *"Forward-only application — New bars apply to chapters scored after the amendment. Scores already recorded are never retroactively adjusted."* This is paired with the Innovation Engine's two-trigger promotion mechanism (PR-A1) and with a discipline of version dating every score record: each chapter's GATE-2-scorecard.md file names the rubric version under which it was scored, along with the date.

### 3.2 Amendment Cycle

The operational cycle, from PR-A1: an innovation is logged; when 2 exact-match instances or 3 thematic-cluster instances accumulate, the innovation is promoted; the amendment text is drafted (by a human editor, per A1's semi-automatic framing) and inserted into RUBRIC.md as either a new clause under an existing dimension, an extension of an existing clause (e.g., "Terminal Condition Types Expanded"), or a new sub-type (e.g., "Contradiction-Held-as-Engine" as a sub-type of Structural Engine). The RUBRIC.md version header is updated, the changelog gets a new line, and INNOVATIONS.md's Amendment History table adds a row.

Critically, the earlier rubric's clauses are not rewritten. The Structural Engine amendment of v1.1 appears in v1.7 with its original text unchanged; the v1.7 addition (Contradiction-Held-as-Engine) sits adjacent to it as a distinct sub-type. This is the textual pattern we measure.

### 3.3 Seven Amendment Cycles

Across v1.0 → v1.7, seven version cycles comprising fifteen dimension-level amendment rows were committed. The Amendment History table:

| Version | Date | Cycle summary | Dimensions touched |
|---------|------|---------------|--------------------|
| v1.0 | 2026-04-15 | Initial rubric (baseline, not an amendment) | — |
| v1.1 | 2026-04-15 | 3 amendments from 8 innovations across 4 chapters | Progression, Figures, Landing |
| v1.2 | 2026-04-15 | Inside-Voice Honesty | Honesty |
| v1.3 | 2026-04-15 | Knowledge-System-as-Evidence | Evidence |
| v1.4 | 2026-04-16 | Voice Spectrum + Book-Level Arc | Voice, Progression |
| v1.5 | 2026-04-16 | Cluster promotion of 5 amendments from 27 innovations | Progression, Evidence/Honesty |
| v1.6 | 2026-04-18 | Terminal Condition Types expanded 5→10 | Progression |
| v1.7 | 2026-04-19 | Contradiction-Held-as-Engine | Progression |

### 3.4 Rationale

The project's CLAUDE.md states the fourth editorial principle as "Evolving quality. The scoring rubric is a learning system. When something exceptional appears, capture it, update the rubric, raise the bar." The forward-only qualifier preserves the legitimacy of chapters written before each bar was raised: if a chapter earned 52/60 under v1.1, that 52 reflects the v1.1 bar, not the v1.7 bar, and the chapter is not penalized for failing to meet criteria the rubric did not yet contain. This is the fairness principle from §2.1 applied to an evolving construct.

---

## 4. Methods

### 4.1 Data

The dataset is three artifacts in the LUCIA repository:

1. **RUBRIC.md** at each version, recoverable from git history. Eight commits (one per version v1.0 through v1.7) touch the file and carry the full text at that version.
2. **INNOVATIONS.md**'s Amendment History table (lines 773–792 of the current file), listing 15 amendment rows across the 7 amendment cycles.
3. **GATE-2 scorecard files** for each locked chapter, stored in each chapter's `reviews/` directory, recording the rubric version under which the chapter was scored.

### 4.2 Measurement A — Amendment Reversal Classification

For each of the 15 amendment rows in the Amendment History table, we apply a pre-registered classifier:

- **Extension**: the amendment adds a new clause to RUBRIC.md without modifying existing clauses. Textual signature: the git diff shows only added lines; no existing rubric text is deleted or rewritten.
- **Refinement**: the amendment edits or supplements existing clause text to clarify, narrow, or extend without reversing the original direction. Textual signature: the diff shows edited lines or an extension paragraph that explicitly preserves the earlier clause.
- **Reversal**: the amendment explicitly overturns, contradicts, or materially weakens a prior amendment's claim. Textual signature: an earlier clause is deleted or rewritten in a direction opposed to its original meaning, or the changelog explicitly states that a prior bar is being relaxed or withdrawn.

The classifier is deterministic given the git diff and the changelog prose. We pre-register Refinement as strictly weaker than Reversal: a refinement preserves direction; a reversal changes it.

We also note an interpretive question: the v1.5 cluster promotion rule could be argued to *reverse* the original v1.0 2-instance-only regime, since it adds a new promotion pathway. Under our strict classifier, this is a Refinement: the 2-instance trigger is preserved unchanged, and the cluster trigger is supplemental. A stricter classification rule that called every change-of-procedure a Reversal would mislabel most ontology-evolution operations; our rule tracks the *direction* of the change, not its presence.

### 4.3 Measurement B — Forward-Overlay Metric

For each pair of consecutive rubric versions (v_{i} → v_{i+1}), we compute:

- Lines added (v_{i+1} has, v_{i} did not).
- Lines deleted (v_{i} had, v_{i+1} does not).
- Lines preserved (present in both).

We compute these both per-step and for the full v1.0 → v1.7 range. From these we derive the **forward-overlay percentage**: the fraction of the current v1.7 rubric's content that was added after v1.0. We compute this at both line granularity (useful as a structural measure) and word granularity (better for content volume).

The computation uses standard `diff` with line-preservation, line-insertion, and line-deletion output formats. It is fully reproducible from the public git history.

### 4.4 Measurement C — Counterfactual Re-Score Pilot

The plan.md's original specification called for a stratified blind re-scoring of 20 chapters across Sessions 1 and 2. At pilot scope we reduce this to 4 chapters, with same-author counterfactual re-scoring rather than independent blind re-scoring. We flag the full 20-chapter blind re-score as *proposed companion measurement* and document the scope reduction explicitly here in Methods.

**Chapter selection.** We deliberately select chapters whose *own innovations* seeded later amendments. These are the chapters most likely to reveal drift under a later rubric version, because their contribution to the rubric raised its own ceiling. If forward-only were masking drift, these chapters' re-score deltas would be substantial. If the policy is truly additive, the delta should be small and of a specific sign — positive, because the later rubric now credits the chapter more clearly for techniques it demonstrated but which the earlier rubric did not name. The four selected chapters are:

1. **Mali Empire — Era 3: The Great Hajj** (scored under v1.0; 49/60 Chronicle). Seeded three v1.1 amendments: Covenant-as-Structural-Engine (Progression), Archival-Gaps-as-Characterization (Figures, merged with the San instance into Honest Limits as Technique), Dual-Stream Closing (Landing, merged with Haudenosaunee into Culture's Own Persistence as Close).
2. **Mali Empire — Era 5: The Songhai Succession** (scored under v1.1; 52/60 Chronicle). Seeded v1.5's Terminal Condition as Culture-Specific — Songhai's "legitimacy gap" is the founding Type 1 exemplar in the v1.5 amendment.
3. **Haudenosaunee — Era 2: The Founding** (scored under v1.0; 51/60 Chronicle). Seeded v1.1's Structural Engine (Grief as Structural Engine) and Culture's Own Persistence as Close (Present-Tense Close).
4. **San — Era 1: Deep Time** (scored under v1.0; 52/60 Chronicle). Seeded v1.1's Honest Limits as Technique (composite figure disclosure); instrumented v1.3's Body-as-Instrument exemplar (tracking rendered through embodied sensation); and v1.5's Non-Chronological Organizing Principle (eland as integration pivot).

**Re-scoring procedure.** For each chapter, we read the locked GATE-2-scorecard.md (original score with dimension evidence), re-read the chapter text and figures.md, and apply the v1.7 rubric's anchors dimension-by-dimension. For each dimension we ask: given the v1.7 anchors (including all post-original amendments), what score would this chapter now earn? The re-score is recorded at whole-point granularity.

**Scorer-bias limitation.** The re-scorer is the project's editor, who also scored the chapters originally and wrote the amendments. This is the exact bias the 20-chapter blind re-score would address. We do not claim the pilot supersedes the blind study; we claim only that under the weaker pilot design, the delta is small, bounded, and of the predicted sign.

### 4.5 Pre-Registered Thresholds

From the plan.md quantification contract:
- Falsification A: ≥ 3 amendments classified as Reversal across the 7 amendment cycles.
- Falsification B: mean absolute re-score delta > 8 points on the pilot chapters.

Either threshold alone triggers falsification. Both are derived from the plan.md contract pre-registered before any measurement ran.

---

## 5. Results

### 5.1 Measurement A — Amendment Reversal Classification

Applying the Extension / Refinement / Reversal classifier to all 15 rows of the Amendment History table:

| Version | Amendment | Classification | Rationale |
|---------|-----------|----------------|-----------|
| v1.1 | Structural Engine | Extension | New paragraph under Progression; no prior text modified. |
| v1.1 | Honest Limits as Technique | Extension | New paragraph under Figures; no prior text modified. |
| v1.1 | Culture's Own Persistence as Close | Extension | New paragraph under Landing; no prior text modified. |
| v1.2 | Inside-Voice Honesty | Extension | New paragraph under Honesty; no prior text modified. |
| v1.3 | Knowledge-System-as-Evidence | Extension | New paragraph under Evidence; no prior text modified. |
| v1.4 | Voice Spectrum | Extension | New paragraph under Voice; no prior text modified. |
| v1.4 | Book-Level Arc | Extension | New paragraph under Progression adjacent to v1.1 Structural Engine. |
| v1.5 | Material Object as Structural Principle | Extension | New sub-type paragraph under Progression. |
| v1.5 | Source Asymmetry as Technique | Extension | New paragraph under Evidence. |
| v1.5 | Knowledge System at Method Level | Refinement | Explicitly marked "extends v1.3"; clarifies and broadens v1.3 without reversing. |
| v1.5 | Non-Chronological Organizing Principle | Extension | New paragraph under Progression. |
| v1.5 | Terminal Condition as Culture-Specific | Extension | New paragraph under Progression. |
| v1.6 | Terminal Condition Types Expanded | Refinement | Extends v1.5's Terminal Condition list from 5 to 10 types; original 5 preserved unchanged. |
| v1.7 | Contradiction-Held-as-Engine | Extension | New sub-type under Progression, explicitly distinguished from v1.1 Structural Engine. |
| v1.4 (ext.) | Bilingual-Embodied register | Refinement | Adds register to the v1.4 Voice Spectrum list; list is preserved. |

**Totals: Extensions = 12; Refinements = 3; Reversals = 0.**

(The v1.5 Cluster Promotion Rule documented in INNOVATIONS.md §"Cluster Promotion Rule (v1.5)" governs the Innovation Engine's trigger mechanism rather than RUBRIC.md content; if counted as an amendment, it is a Refinement — the 2-instance trigger is preserved, the cluster trigger is supplemental. Including it raises Refinements to 4; Reversals remain 0.)

The pre-registered falsification threshold for Measurement A is ≥ 3 Reversals. **Observed Reversals: 0. Threshold not approached.**

### 5.2 Measurement B — Forward-Overlay Metric

Per-step line additions, deletions, and preservations from git diff:

| Step | Commit pair | +Lines | −Lines | Preserved |
|------|-------------|--------|--------|-----------|
| v1.0 → v1.1 | c617bb9 → 918863a | 9 | 1 | 243 |
| v1.1 → v1.2 | 918863a → e5d7438 | 6 | 2 | 250 |
| v1.2 → v1.3 | e5d7438 → e848839 | 5 | 2 | 254 |
| v1.3 → v1.4 | e848839 → c095043 | 7 | 2 | 257 |
| v1.4 → v1.5 | c095043 → c3e779a | 14 | 1 | 263 |
| v1.5 → v1.6 | c3e779a → 9556e14 | 16 | 1 | 276 |
| v1.6 → v1.7 | 9556e14 → 0a69eec | 11 | 1 | 291 |
| **Sum** | | **68** | **10** | — |

Across v1.0 → v1.7:

| Quantity | v1.0 | v1.7 | Change |
|----------|------|------|--------|
| Lines (RUBRIC.md) | 244 | 302 | +58 net |
| Words (RUBRIC.md) | 1,961 | 4,289 | +2,328 net |
| Lines preserved from v1.0 unchanged in v1.7 | — | 243 | 99.6% preservation |
| Lines unique to v1.7 (not in v1.0) | — | 59 | — |

The single line deleted between v1.0 and v1.7 is the version-header string (`## Rubric v1.0 — Established 2026-04-15`), replaced by `## Rubric v1.7 — Amended 2026-04-19` plus the changelog block. No substantive rubric text (anchor tables, amendment paragraphs, worksheet scaffolding) was removed.

**Forward-overlay, line basis (net)**: 59 / 302 = **19.5%**.
**Forward-overlay, word basis (net)**: 2,328 / 4,289 = **54.3%**.

The two numbers measure the same phenomenon at different granularities. The line-based figure under-counts because Markdown rubric text compresses dense amendment paragraphs into single lines; a single added line often contains 100+ words of new normative content. The word-based figure better captures the volume of substantive addition. A reader seeking the strongest structural-stability signal should read the preservation rate (99.6% of v1.0 lines intact). A reader seeking the scale of additive evolution should read the word-based forward-overlay (54.3%).

Combined reading: more than half of v1.7's content was added after v1.0, and virtually none of v1.0 was removed in the process. This is the structural signature of a policy that is both additive and stable — the rubric grew substantially while preserving essentially all of its prior commitments.

### 5.3 Measurement C — Counterfactual Re-Score Pilot

For each of the four pilot chapters, we re-read the chapter text and figures.md, held the evidence from the original GATE-2-scorecard in view, and applied the v1.7 rubric's anchors dimension-by-dimension. The primary places the v1.7 rubric raises the bar above the original rubric versions are: Progression (v1.1 Structural Engine, v1.4 Book-Level Arc, v1.5 Material Object / Non-Chronological / Terminal Condition, v1.6 Terminal Condition Types Expanded, v1.7 Contradiction-Held-as-Engine); Evidence (v1.3 Knowledge-System-as-Evidence, v1.5 Knowledge System at Method Level, v1.5 Source Asymmetry as Technique); Voice (v1.4 Voice Spectrum anchors); Landing (v1.1 Culture's Own Persistence as Close); Figures (v1.1 Honest Limits as Technique); Honesty (v1.2 Inside-Voice Honesty).

**Mali Era 3 — The Great Hajj.** Original v1.0 score: 49/60 Chronicle.
- Immersion 8 → 8. Historiographic intrusions unchanged.
- Evidence 9 → 9. Already high; Knowledge-System-at-Method-Level anchor would credit the Maliki-inheritance and al-Sahili architectural-method passages, but 9 ceiling is close to max.
- Progression 8 → 9. The Kurukan Fuga is the founding exemplar of v1.1 Structural Engine.
- Figures 7 → 7. v1.1 Honest Limits now codifies the Inari Kunate technique the chapter pioneered, but 9-10 still demands full dimensionality.
- Voice 8 → 8. Griot cadence is a founding Voice Spectrum register.
- Landing 9 → 10. Dual-Stream Closing is a founding exemplar of v1.1 Culture's Own Persistence as Close.

**Re-score: 51/60. Delta: +2.**

**Mali Era 5 — The Songhai Succession.** Original v1.1 score: 52/60.
- Immersion 9 → 9.
- Evidence 8 → 8.
- Progression 9 → 10. Founding exemplar of v1.5 Terminal Condition Type 1 (legitimacy gap); also v1.4 Book-Level Arc's 5-era exemplar.
- Figures 7 → 7.
- Voice 9 → 9.
- Landing 10 → 10. Already at max.

**Re-score: 53/60. Delta: +1.**

**Haudenosaunee — The Founding.** Original v1.0 score: 51/60.
- Immersion 9 → 9.
- Evidence 8 → 8.
- Progression 8 → 9. Grief-as-Structural-Engine is the co-founding v1.1 Structural Engine exemplar.
- Figures 8 → 8.
- Voice 9 → 9.
- Landing 9 → 10. Present-Tense Close is the founding exemplar of v1.1 Culture's Own Persistence as Close.

**Re-score: 53/60. Delta: +2.**

**San — Deep Time.** Original v1.0 score: 52/60.
- Immersion 9 → 9.
- Evidence 8 → 9. v1.3 Body-as-Instrument technique codifies the tracking-as-method rendering.
- Progression 9 → 10. v1.5 Non-Chronological Organizing Principle cites San/eland as founding exemplar.
- Figures 8 → 8.
- Voice 9 → 9.
- Landing 9 → 9.

**Re-score: 54/60. Delta: +2.**

**Pilot summary:**

| Chapter | Original | v1.7 re-score | Delta |
|---------|----------|---------------|-------|
| Mali Era 3 (v1.0) | 49 | 51 | +2 |
| Mali Era 5 (v1.1) | 52 | 53 | +1 |
| Haudenosaunee (v1.0) | 51 | 53 | +2 |
| San (v1.0) | 52 | 54 | +2 |
| **Mean** | 51.0 | 52.75 | **+1.75** |
| **Mean absolute** | — | — | **1.75** |
| **Max absolute** | — | — | **2** |
| **Sign** | — | — | uniformly positive |

Mean absolute delta = 1.75 points. Maximum absolute delta = 2 points. All four deltas are positive, and all fall within the 1–2-point band. The pre-registered falsification threshold for Measurement C is mean |delta| > 8 points. **Observed mean |delta|: 1.75. Threshold not approached.**

### 5.4 Primary Result

Both pre-registered falsification thresholds hold with substantial margin. Reversal count is 0 against a threshold of 3. Mean absolute re-score delta is 1.75 against a threshold of 8. Line preservation from v1.0 to v1.7 is 99.6%. Forward-overlay at word granularity is 54.3%. The forward-only policy, as operated on LUCIA across 7 amendment cycles, produces measurably stable evolution along all three axes.

The plan.md null-fallback specifies "reversal rate > 20% OR re-score delta > 5 points → forward-only is masking drift; retroactive re-scoring should be considered." Both the null-fallback weaker bounds and the pre-registered falsification stronger bounds are not triggered: observed 0% reversal rate is below 20%; observed 1.75 mean |delta| is below 5. The policy passes both the strong and the weak stability tests.

### 5.5 Sign of the Re-Score Delta

An important property of Measurement C: all four deltas are **positive**. This is the sign predicted in §4.4 — when the re-scored chapters are chapters whose own innovations triggered later amendments, the later rubric credits those chapters more explicitly, because the rubric's 9+ anchor for the relevant technique is now named and operationalized. The chapters are not being penalized by a later bar; they are being recognized under clearer language for a technique they authored.

This is different from the sign a hostile critic might expect. If forward-only were masking drift, the expected sign would be negative — the current rubric's standards would make earlier chapters look worse. We observe the opposite sign at small magnitude. The interpretation is that forward-only in this corpus is not merely additive in textual terms (99.6% preservation) but additive in normative terms: new bars appear alongside preserved bars, and they appear because of — not in spite of — the early chapters' own contributions.

A full blind re-score on a larger stratified sample (the plan.md originally specified 20 chapters) is required to confirm this sign holds for chapters that did *not* seed amendments — the null case, where the chapter contributed nothing to the rubric's growth but is held against the growth anyway. We flag this as the primary companion measurement for follow-up work.

---

## 6. Discussion

### 6.1 What Stability Looks Like

Across three independent measurements, LUCIA's forward-only amendment policy produced stable evolution. The rubric grew from 244 to 302 lines (from 1,961 to 4,289 words) without removing any of its original substantive content, and without any amendment classified as a reversal under a pre-registered classifier. The four pilot chapters, when re-scored under v1.7 anchors, show small uniformly-positive deltas. The textual record, the classification record, and the counterfactual re-score record agree that the rubric's evolution is additive.

This is the property the forward-only policy was designed to produce. The question was whether the policy, once adopted, would hold operationally — whether amendments drafted amid the pressure of production would drift into silent reversals, whether the rubric's text would get rewritten rather than extended, whether early chapters would turn out to look substantially worse under the later bar. The measurements show the policy held on all three fronts.

### 6.2 Forward-Only Is One Defensible Policy

Following the A1 POST-WRITE discipline, we are explicit that forward-only is one of three defensible policies for discovery-driven rubric evolution, not the only one. The alternatives — retroactive rescoring and bidirectional migration — have their own advantages.

Retroactive rescoring produces maximum cross-corpus comparability at the cost of re-scoring labor and the legitimacy problem of penalizing chapters for later-discovered bars. It is appropriate when the rubric's dimensions were established up front and the amendments are about precision rather than discovery.

Bidirectional migration produces full comparability via explicit mapping functions. It is the ontology-evolution literature's standard. It is operationally demanding: every amendment must come with forward and backward migration functions, and when the amendment introduces a dimension the prior rubric did not have, the backward mapping is often under-constrained.

Forward-only is appropriate when scores are archival data points — records of how each artifact was judged at the time of review — and when amendments are themselves informed by patterns in the earlier artifacts. Both conditions hold in LUCIA, and in similar AI-assisted creative production pipelines where the artifact's own production reveals dimensions the rubric could not have anticipated. Under these conditions, the weakest-on-comparability policy is the one whose costs are the most honest: it declines to make early and late scores comparable by fiat; it asks the reader to interpret each score alongside its version.

### 6.3 What the Positive-Delta Sign Means

The re-score pilot's uniformly-positive delta is not an accident of chapter selection and not a finding about general early-chapter quality. It is a structural property of the policy-plus-engine combination. When the Innovation Engine promotes a pattern seen in an early chapter, the resulting amendment *names and anchors* the pattern. The chapter then satisfies the named anchor more explicitly than it satisfied the implicit version-before-the-amendment bar, because the anchor is written to describe what that chapter did.

This produces a subtle ethical property: forward-only is not simply weaker-than-bidirectional. It is explicitly asymmetric in the favorable direction — chapters scored under earlier rubric versions keep their earlier scores, but if the later rubric names their contribution, they are also implicitly recognized as founding exemplars of the later anchor. The chapters become citation-targets for the rubric's evolution, not targets for downward revision.

The limitation of this property is that it is observable only for chapters that seeded amendments. Chapters that did not seed amendments but are nonetheless held against the later bar (the null case in §5.5) could, in principle, show either zero delta or a negative delta. A full 20-chapter stratified blind re-score is required to observe the null case and confirm the policy's stability for the non-seeding majority.

### 6.4 Transportable Design Pattern

A transportable pattern emerges, contingent on the conditions in §6.2 holding. For a quality rubric in an AI-assisted creative pipeline, forward-only amendment with the following additional disciplines is operationally tractable:

1. **Version-dated scores.** Every score record names the rubric version under which it was applied. This is the minimum information required for the policy to be inspectable.
2. **Inspectable changelog.** Every amendment is recorded with its triggering instances and the dimension it amends. RUBRIC.md's changelog and INNOVATIONS.md's Amendment History table serve this role in LUCIA.
3. **Textual preservation discipline.** Amendments are added as new clauses rather than as edits to existing clauses when possible. When refinement is required, the changelog names the relationship explicitly (e.g., "extends v1.3"). This produces the high-preservation property we measured at 99.6%.
4. **Reversal classifier pre-registered.** The criteria for calling an amendment a reversal (as opposed to a refinement) are stated before the measurement runs. This prevents post-hoc classification bias and makes the measurement reproducible.

Adopting these disciplines does not guarantee stability in a new corpus — stability must be measured. But it makes the measurement tractable and the failure mode (drift masked as forward-only) diagnosable.

### 6.5 Limitations

The pilot is 4 chapters, not the 20 the plan.md originally specified. The re-scorer is the same author as the original scorer and as the amendment drafter. Independent blind re-scoring by a scorer unaware of which chapters seeded which amendments is the strongest form of Measurement C and would close the scorer-bias threat entirely. We did not run it at this scope; we flag it as the primary companion measurement.

The pilot deliberately selected chapters whose own innovations seeded later amendments. This selection biases the measurement in the favorable direction. A full stratified sample would include non-seeding chapters and would reveal the policy's behavior in the null case.

The forward-overlay metric uses textual diff as its operational definition. A sufficiently motivated author could, in principle, amend a rubric in a way that preserves line counts while reversing meaning — adding a clause that implicitly negates a preserved clause without deleting the preserved text. Our Measurement A (semantic classifier) is designed to catch this; the combination of structural metric (B) and semantic classifier (A) is the operational defense against textual-vs-semantic gaps. A hostile amendment could still evade both measurements, and we note this as a limit on the metric's adversarial robustness.

The measurement is from one project, one editorial pair, one amendment period of five days. Scaling effects over a multi-year corpus, across multiple editors with different interpretations of the refinement-vs-reversal line, are open questions.

---

## 7. Threats to Validity

### 7.1 Classifier Subjectivity

The Extension / Refinement / Reversal classifier has explicit criteria, but a hostile reader could argue that the v1.5 cluster promotion rule, or the v1.6 Terminal Condition expansion, is a materially direction-changing amendment rather than a refinement. Under a stricter rule that called every operational-procedure change a reversal, our Reversal count rises to 1 or 2. Neither count reaches the pre-registered falsification threshold of 3, so the primary falsification result holds under reasonable classifier perturbations. We report the numbers under our stated rule and identify the borderline cases.

### 7.2 Pilot Scope and Scorer Bias

The 4-chapter pilot with same-author counterfactual re-scoring is the weakest link in the paper. Independent blind re-scoring by a scorer who did not score the chapter originally and did not draft the later amendments would close both the sample-size and the bias concerns. We flag this as the primary companion measurement and bound our pilot claim to "same-author counterfactual re-score on 4 chapters shows mean |delta| = 1.75 points, within the pre-registered [0, 8] band."

### 7.3 Chapter Selection Bias

The pilot chapters were selected for being high-information — they are the chapters whose innovations triggered later amendments. This selection makes them the strongest test of whether forward-only masks drift (because they are the chapters whose ceiling was raised by their own contributions), but it also means they are the chapters most likely to be recognized-upward by the later rubric. A stratified sample including non-seeding chapters would show the null-case behavior.

### 7.4 Adversarial Amendment

The forward-overlay metric measures textual preservation. A sufficiently motivated author could add a clause that implicitly contradicts a preserved clause without deleting the preserved clause. The semantic classifier (Measurement A) is designed to catch such cases, but a cleverly adversarial amendment could, in principle, evade both measurements simultaneously. We do not claim the metric is adversarially robust; we claim it is a useful diagnostic when the author is acting in good faith.

### 7.5 One-Project Sample

The measurement is drawn from one project over five days of active production with a single editorial pair. Scaling effects — over months or years, across teams with turnover, with multiple concurrent editors whose interpretations of the refinement line diverge — are not observable in this sample.

---

## 8. Conclusion

We measured stability of LUCIA's forward-only rubric-amendment policy across three axes on the full v1.0 → v1.7 evolution. Zero amendments classified as Reversals under a pre-registered Extension/Refinement/Reversal classifier (15 rows in the Amendment History table: 12 Extensions, 3 Refinements, 0 Reversals). 99.6% of v1.0's lines preserved in v1.7; 54.3% of v1.7's words are post-v1.0 additions. Counterfactual re-score pilot on 4 Session-1 chapters yields mean delta +1.75 points with maximum absolute 2 points and uniformly positive sign — below the pre-registered 8-point falsification threshold by a factor of ~4.5.

The pre-registered falsification conditions (≥ 3 reversals OR mean |delta| > 8 points) do not hold against this corpus. Forward-only amendment, as operated in LUCIA, produced stable evolution in the strong sense — additive textually, additive semantically, and positive-signed in the counterfactual re-score.

The pilot's scope is smaller than plan.md originally specified (4 chapters, not 20; same-author counterfactual, not independent blind). Full 20-chapter blind re-scoring is flagged as the primary companion measurement. The broader implication is that when scores function as archival data points rather than active classifications, and when amendments are triggered by patterns the earlier artifacts revealed, forward-only is an operationally tractable policy that can be measured empirically for drift. Whether the policy generalizes to AI-assisted creative domains beyond LUCIA is the subject of PR-C3.

---

## 9. References

- [NEED-A] Stojanovic, L. (2004). "Methods and tools for ontology evolution." *PhD Dissertation, University of Karlsruhe.* Also: Guarino, N. & Welty, C. (2002). "Evaluating ontological decisions with OntoClean." *Communications of the ACM* 45(2).
- [NEED-B] Jonsson, A. & Svingby, G. (2007). "The use of scoring rubrics: Reliability, validity and educational consequences." *Educational Research Review* 2(2), 130–144. Wolfe, E. W. (2004). "Identifying rater effects using latent trait models." *Psychology Science* 46, 35–51.
- [NEED-C] American Educational Research Association, American Psychological Association, & National Council on Measurement in Education (2014). *Standards for Educational and Psychological Testing.* AERA.
- [NEED-D] Liang, P. et al. (2022). "Holistic Evaluation of Language Models (HELM)." arXiv:2211.09110.
- [NEED-E] Charmaz, K. (2006). *Constructing Grounded Theory.* Sage.

---

## 10. Artifacts

- **Source repository**: `C:\src\chronicle` (branch master).
- **Rubric text**: `scoring/RUBRIC.md` (v1.0 at commit c617bb9 through v1.7 at commit 0a69eec).
- **Innovation log**: `scoring/INNOVATIONS.md` — Amendment History table.
- **GATE-2 scorecards used in pilot**: Mali E3, Mali E5, Haudenosaunee Founding, San Deep Time.
- **Version-to-commit map**: v1.0=c617bb9; v1.1=918863a; v1.2=e5d7438; v1.3=e848839; v1.4=c095043; v1.5=c3e779a; v1.6=9556e14; v1.7=0a69eec.
- **Primary numbers**:
  - Amendment classification: 12 Extensions / 3 Refinements / 0 Reversals.
  - Line preservation v1.0 → v1.7: 243 / 244 = 99.6%.
  - Forward-overlay (lines, net): 19.5%; (words, net): 54.3%.
  - Re-score pilot mean delta: +1.75 (range +1 to +2, uniformly positive, n=4).
- **Falsification thresholds (pre-registered)**: ≥ 3 Reversals OR mean |delta| > 8 points.
- **Null fallback (plan.md)**: reversal rate > 20% OR |delta| > 5 points.
- **Result**: stable under all three measurements; both thresholds held with substantial margin; null fallback also not triggered.

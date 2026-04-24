# Panel Synthesis: PR-A2 — Forward-Only Rubric Evolution

**Paper**: "Forward-Only Rubric Evolution: Stability Under a Discovery-Driven Quality Standard"
**Track**: A — The Discovery Engine (paper 2 of 3)
**Target venues**: FAccT (round 1), CHI (round 2)
**Synthesis date**: 2026-04-19
**Panel composition**: Barocas (fairness), Stojanovic (ontology evolution), Ferryman (critical data studies), Petroff (educational measurement), Liang (benchmarks)

---

## Score Statistics

| Reviewer | Score | Lens | Key verdict |
|----------|-------|------|-------------|
| Barocas | 3 | Algorithmic fairness | Weak Accept; engage Barocas-Selbst downstream-fairness |
| Stojanovic | 2 | Ontology evolution | Weak Reject; archival/active distinction under-specified |
| Ferryman | 3 | Critical data studies | Weak Accept; version-tag metadata attrition under-engaged |
| Petroff | 2 | Educational measurement | Weak Reject; construct-drift vs. rubric-drift conflated |
| Liang | 3 | Benchmark versioning | Weak Accept; under-claim differential vs. HELM |

- **Mean score**: 2.6
- **Min score**: 2
- **Max score**: 3
- **Distribution**: 0 × Strong Accept (4), 3 × Weak Accept (3), 2 × Weak Reject (2), 0 × Reject (1)
- **Advance threshold**: avg ≥ 2.5 AND min ≥ 2 — **both satisfied**

---

## Issue Classification

**P1 = 3+ reviewers raise the issue OR any Major OR threatens validity of primary claim.**
**P2 = 1–2 reviewers raise the issue at Major or Minor.**
**P3 = cosmetic / single-reviewer minor.**

### P1 — Must address before resubmission

**P1-A. Downstream-consumer fairness / metadata attrition (Barocas, Ferryman, and implicitly Liang on re-score capability).**
Three reviewers independently converge on the same gap: the paper's fairness argument stops at the artifact boundary. Forward-only protects the *scored chapter* from a retroactive bar, but the cost travels to downstream consumers of the scored corpus, who must read each score alongside its version tag for the policy to be honest. The version-dating discipline (§6.4 point 1) is stated as authoring policy; it is not defended as observed practice under reuse, export, or comparison. Barocas frames this as individual-vs-group fairness; Ferryman frames it as data-repurposing risk; Liang frames it as the HELM-LUCIA differential in re-score capability. Three angles, same load-bearing gap. Since §6.2's "archival data points" defense is the hinge of the entire weaker-but-sufficient argument, this is validity-adjacent and therefore P1.

**Fix**: (a) Add a subsection in §6 (or expand §6.2) with a concrete worked example showing what the version-naming discipline prevents and what it does not. (b) Engage Barocas & Selbst (2016) and one critical-data-studies reference (Leonelli or Pasquetto on data reuse). (c) Distinguish re-score *capability* from re-score *default* per Liang.
*Expertise attribution*: Barocas (primary), Ferryman (primary), Liang (secondary).

**P1-B. Archival-vs-active distinction is under-specified (Stojanovic, Ferryman).**
Two reviewers Major-flag the same issue: the paper never operationally defines the boundary between "archival data point" and "active classification." Stojanovic argues the distinction collapses the moment any downstream process (including the paper's own Measurement C) treats scores as queryable across versions. Ferryman argues the distinction is philosophical rather than sociotechnical — a score can be archival at authoring intent and active at consumer intent. Both reviewers note this is where the entire weaker-but-sufficient argument sits. This threatens the framing validity of the central positioning claim.

**Fix**: Either operationalize with a test ("a score has become active when process X occurs; under those conditions, the forward-only justification weakens"), or re-frame as "forward-only is cheaper at authoring; bidirectional is cheaper at every use" per Stojanovic's suggestion.
*Expertise attribution*: Stojanovic (primary), Ferryman (secondary).

**P1-C. Construct-drift vs. rubric-text-drift is not distinguished (Petroff).**
Single reviewer Major, but at the level of construct validity for the paper's central measurement claim — therefore P1 by the "threatens validity" rule. The reversal classifier operates on rubric text; Measurement B operates on line preservation. Neither captures the case where the underlying construct (what "Progression 9" actually requires) has drifted despite high textual preservation. Petroff argues this is exactly what happens under anchor expansion — the dimension name is preserved but the anchors for 9+ now require techniques v1.0 did not name. The paper acknowledges this obliquely in §7.4 (adversarial case) but not in the good-faith case, which is more common.

**Fix**: Add a paragraph to §7.1 distinguishing text-preservation from construct-preservation, and acknowledge that the paper's three measurements are instruments for the former. Position the 20-chapter blind re-score (already flagged as companion measurement) as the instrument for the latter.
*Expertise attribution*: Petroff (primary), adjacent to Stojanovic's classifier-granularity concern.

### P2 — Should address; non-blocking

**P2-A. Positive-delta sign has a measurement-theory alternative reading (Petroff, implicitly Barocas).**
Petroff notes that uniformly-positive re-score delta is, in educational measurement terms, indistinguishable from "rubric leniency shift" without an independent rater. The paper's preferred reading (anchor consolidation) is plausible but not isolated by the pilot design. Same-author limitation is acknowledged (§7.2); the alternative *interpretation* of the sign is not.
*Fix*: Add one paragraph to §5.5 or §6.3 explicitly naming the leniency-shift alternative and flagging that independent rating disambiguates.

**P2-B. Seeder-vs-non-seeder path dependence under-theorized (Barocas, Ferryman).**
Two reviewers note that seeders receive a form of recognition non-seeders do not, independent of drift. Barocas frames this as disparate benefit; Ferryman frames it as subject-vs-contributor status. Half a paragraph engaging this asymmetry as a feature-not-bug (or feature-with-costs) would strengthen §6.3.

**P2-C. Classifier is coarser than ontology-evolution operator taxonomy (Stojanovic).**
The 3-category classifier cannot distinguish generalize / specialize / merge / split. Single-reviewer Major. Does not threaten the falsification result (0 reversals is robust under any reasonable re-classification per §7.1), so P2 rather than P1. Worth a short acknowledgement in §4.2 or a compare-table in §7.

**P2-D. Differential contribution vs. HELM under-claimed (Liang).**
Forward-only *normative-anchor* versioning is the novel move vs. HELM's pipeline versioning. Deserves abstract-level foregrounding. Mechanical revision.

**P2-E. Multi-editor transportability untested (Liang, Stojanovic).**
§6.4's transportable pattern rests on classifier discipline that degrades across editors. Flag for future work (inter-rater study); for FAccT, acknowledge in §7.5 more strongly.

### P3 — Cosmetic

- Abstract over word count (~280 vs. 250 FAccT ceiling) — Barocas, Petroff (minor).
- Resolve 5 [NEED] citations — all five reviewers note their respective [NEED] tags; Petroff and Liang give specific citation recommendations.
- "Test-takers are the chapters themselves" anthropomorphization — Petroff, Ferryman both flag as rhetorically strained.
- Consider a per-step preservation plot in §5.2 — Liang.
- Line-vs-word forward-overlay headline — Stojanovic suggests foregrounding word-granularity 54.3% as the substantive-additive signal.

---

## Convergence Analysis

Three independent lenses (fairness, critical data studies, benchmarks) converge on the same fairness-adjacent gap: the paper's version-naming discipline is load-bearing but under-defended against realistic downstream use. This is the strongest signal from the panel and the P1-A item is correspondingly the most urgent fix.

Two lenses (ontology evolution, critical data studies) converge on the archival-vs-active distinction as under-specified. Stojanovic reads it as a theoretical gap; Ferryman reads it as a sociotechnical one. Both resolve under the same revision: operationalize the distinction or re-frame it as a cost-trade rather than a scope-condition.

The educational-measurement reviewer is alone on construct-vs-rubric-text drift, but the observation is substantive and bears on how Measurement B should be read. The authors already have the right follow-up (20-chapter blind re-score as companion measurement) — the fix is to position Measurement B more modestly as a textual-continuity instrument rather than a construct-continuity instrument.

The HELM reviewer contributes a framing sharpening (foreground the normative-anchor differential) and one deferrable future-work item (inter-rater multi-editor study). Neither blocks submission.

No reviewer recommends outright rejection. Two reviewers (Stojanovic, Petroff) recommend major revision. Three recommend minor revision and resubmission. The pattern matches the POST-WRITE referee simulation prediction: FAccT-viable with revisions, CHI-blocked on pilot-scope.

---

## Stage Recommendation

**ADVANCE** (avg 2.6 ≥ 2.5 AND min 2 ≥ 2).

Recommend proceeding to revision pass targeting FAccT round 1. Three P1 items should be addressed before submission:
- P1-A (downstream fairness + metadata attrition): ~1 page of revision, adds ~300 words
- P1-B (archival/active operationalization): ~half page, re-frames §6.2 hinge
- P1-C (construct vs. text drift): ~half page, adds to §7.1

Estimated revision effort: 4–6 hours plus citation resolution (5 [NEED] tags). Abstract trim and cosmetic fixes fold in.

Do not proceed to CHI targeting until the 20-chapter blind re-score companion measurement is complete; CHI reviewers (per POST-WRITE Referee 2) will P1-block on pilot scope and classifier inter-rater reliability regardless of framing revisions.

---

## Top P1 for Authors

**P1-A (Downstream fairness / metadata attrition).** Three independent reviewers (Barocas, Ferryman, Liang) converge on this being the highest-leverage fix. The version-naming discipline must be defended as observed practice under reuse, not only asserted as authoring policy. A concrete worked example plus engagement with Barocas-Selbst 2016 and one data-reuse reference (Leonelli or Pasquetto) closes the gap.

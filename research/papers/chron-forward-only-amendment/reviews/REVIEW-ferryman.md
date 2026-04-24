> **Note:** This is an AI-generated simulated review, written by Claude in the voice of a named-expert persona. It is not an actual review by the named person and does not reflect their views or endorsement.

# Review: PR-A2 — Forward-Only Rubric Evolution

**Reviewer**: Kadija Ferryman (Johns Hopkins, critical data studies)
**Venue target**: FAccT
**Score**: 3 (Weak Accept)
**Date**: 2026-04-19

---

## Substantive Engagement

Reading this paper from a critical data studies perspective, what is most valuable is what the authors *don't* claim. They do not claim forward-only is the right policy; they claim it is one of three defensible policies, with costs and benefits they name explicitly. That posture is unusually honest for evaluation-methodology work and I want to credit it before my concerns. This is a paper about the politics of a scoring artifact, even when the authors do not quite frame it that way.

My concerns are about what happens to these scores when they leave the controlled environment of the authoring project. The paper's structural guarantee is that every score record names the rubric version under which it was applied (§6.4 point 1). This is a necessary condition for forward-only to be inspectable. It is not a sufficient condition. In every case I have studied where dataset-level metadata is supposed to "travel with" the data — from EHR data reuse through ML benchmark leaderboards to clinical decision-support — the metadata attrition rate is substantial, and it is substantial in predictable ways. Tables get exported to spreadsheets without the version column. A retrospective compares Era 3 (v1.0, 49) against Era 47 (v1.7, 49) and presents them side-by-side as if they were commensurable. A reader in 2028 pulls three chapters' scorecards and asks "which scored highest?" without noting that the bars were not the same bars. The paper's §6.4 discipline is a *policy prescription*, not an *observed practice*, and I would want more honesty about the gap between the two.

Related: the paper's positive-delta finding (§5.5) is handled carefully on the empirical side — the sign is correctly attributed to anchor consolidation for chapters whose own innovations seeded amendments — but the political reading is missing. When the rubric's evolution is driven by what the corpus itself revealed, the chapters that happened to be written early become disproportionately *legible* under the later rubric. Their techniques are named. Their moves are anchored. Chapters written late, after the rubric has already absorbed the early innovations, do not have the same opportunity to become founding exemplars; they meet a bar already raised by others. This is a kind of path-dependence fairness question that the paper gestures at in §5.5's proposal for a null-case blind re-score, but does not yet theorize. In critical data studies we would call this the difference between being a *subject of the standard* and being a *contributor to the standard*, and the distribution of that status across the corpus is not random.

The version-naming discipline is, in short, *necessary but not robust*. The paper should say so.

---

## Major Issues

1. **Version-naming is policy-as-stated, not policy-as-observed.** The paper should either (a) report whether any downstream use of LUCIA scores has actually preserved the version tag (internal check), or (b) explicitly flag that metadata attrition is a known risk and the version discipline must be enforced at every consumption point, not just at authoring.
2. **Path-dependence across the corpus needs a critical reading, not only a measurement reading.** Seeders contribute to the rubric; non-seeders meet a bar shaped by seeders' contributions. §5.5's positive-delta framing is correct on the mechanism but under-examines who benefits from the asymmetry and who does not.
3. **The "archival" framing flattens the politics of repurposing.** Scores can be archival at their author's intent and active at their consumer's intent. The paper treats this as a philosophical distinction (§2.2) rather than a sociotechnical one. Engaging with data-reuse literature (Leonelli, Pasquetto) would strengthen the argument that version-dating actually holds under reuse.

## Minor Issues

1. The five-day production window is both a strength (well-bounded natural experiment) and a weakness (no longitudinal attrition data). Consider naming this duality explicitly in §7.5.
2. §6.4's four-point transportable pattern reads as prescription. Consider reframing one or two points as *indicators of a healthy forward-only pipeline* rather than *requirements*.
3. The chapter-as-"test-taker" analogy (§2.1) is productive but strained — a test-taker has standing to contest a score; a chapter does not. Worth a sentence.

---

## Quality-Improvement Framing

The measurement work here is solid; the framing work is partial. The paper is one careful section away from being a FAccT paper that non-measurement reviewers can engage with — specifically, a section that acknowledges that forward-only is a policy about *who bears what risk* (authoring editors bear less; downstream consumers bear more) and that the version-naming discipline is the load-bearing beam of that risk allocation. Add that section and I move to Accept.

**Score: 3** (Weak Accept.)

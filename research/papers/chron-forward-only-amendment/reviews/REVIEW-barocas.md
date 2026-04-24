> **Note:** This is an AI-generated simulated review, written by Claude in the voice of a named-expert persona. It is not an actual review by the named person and does not reflect their views or endorsement.

# Review: PR-A2 — Forward-Only Rubric Evolution

**Reviewer**: Solon Barocas (Cornell / MSR, algorithmic fairness)
**Venue target**: FAccT
**Score**: 3 (Weak Accept)
**Date**: 2026-04-19

---

## Substantive Engagement

The paper is unusually disciplined for work that lives on the seam between evaluation methodology and fairness. The authors correctly identify that "forward-only" is a normative choice, not a neutral default, and they cite the right ancestor in AERA/APA/NCME Standards. Where most benchmark-versioning work shrugs about this, PR-A2 actually measures a stability property and pre-registers a falsification threshold. That is the move I want to see more of at FAccT, and I want to say so at the top.

My main concern — and it is substantive rather than cosmetic — is that the fairness framing in §2.1 protects the *scored artifact* but is silent on *downstream consumers* of the scored corpus. Test-taker fairness assumes the score is a terminal evaluation: the student receives the grade, and fairness is about whether the standard at the moment of testing was the right one. In LUCIA, the scores don't stop there. They are read by future editors, by panel reviewers writing retrospectives, potentially by readers deciding which chapters to trust. A chapter that earned 49/60 under v1.0 and a chapter that earned 49/60 under v1.7 are textually equal in the scorecard file but normatively unequal — the later score cleared more bars. The paper's version-dating discipline (§6.4 point 1) is the right instrument, but the paper never engages with whether downstream consumers *in practice* propagate the version tag. This is where the cost of forward-only actually lands, and the paper should name that explicitly rather than leaving it implicit in "archival data points."

Relatedly, the pilot's uniformly-positive delta (§5.5) is honest but under-theorized as a fairness finding. The authors read it as anchor-consolidation, which is correct on the engine side. On the fairness side, it means forward-only produces an *advantaging* asymmetry for chapters that seeded amendments: they keep their old score *and* get cited as founding exemplars of the new anchor. That is a form of individual-level benefit that the rubric's silent beneficiaries (non-seeding chapters scored under the same early version) do not receive. This is not drift in the technical sense, but it is group-vs-individual fairness territory — the seeders become reference points while the non-seeders become the silent denominator. A sentence or two engaging Barocas & Selbst (2016) on the disparate-treatment-vs-disparate-impact distinction would strengthen the paper without overclaiming.

---

## Major Issues

1. **Downstream-consumer fairness is under-engaged.** The test-taker fairness transposition protects chapters (artifacts), not downstream users of the scored corpus. A concrete worked example — "a reader in 2027 compares Era 3 (v1.0, 49) against Era 12 (v1.7, 49)" — would show whether the version-naming discipline is load-bearing or decorative.
2. **Seeding-vs-non-seeding asymmetry needs a fairness reading, not just a sign analysis.** §5.5 reads the positive delta as anchor-consolidation, which is correct on the mechanism. It does not engage with the fact that seeders receive a form of credit the silent non-seeders do not. Half a paragraph in §6.3 would suffice.
3. **The "archival data points" defense is too load-bearing.** §2.2 and §6.2 lean heavily on the claim that LUCIA's scores are archival rather than active classifications. This is the hinge of the entire "weaker-but-sufficient" argument, and it is not defended against the case where a downstream pipeline (e.g., a training-data curator) treats these scores *as if* they were active.

## Minor Issues

1. The abstract at ~280 words exceeds FAccT's 250-word ceiling. Mechanical fix.
2. §2.1's citation placeholder [NEED-C] is the most important resolve-before-submission item; the Standards 2014 text is short and quotable.
3. The phrase "weakest-on-comparability policy" in §6.2 is accurate but rhetorically brittle. Consider "narrowest-scope policy" to avoid an uncharitable skim.

---

## Quality-Improvement Framing

This paper is close to a clean FAccT accept. The empirical work is unusually well-specified and the falsification discipline is exemplary. The gap is not in the measurement but in the fairness framing around the measurement — specifically, that the fairness argument stops at the artifact boundary and does not travel with the score into downstream use. Closing that gap is a half-day revision, not a re-scoping.

**Score: 3** (Weak Accept — revise and resubmit; no P1 blockers at my pass.)

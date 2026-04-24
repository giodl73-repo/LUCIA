> **Note:** This is an AI-generated simulated review, written by Claude in the voice of a named-expert persona. It is not an actual review by the named person and does not reflect their views or endorsement.

# Review: PR-A2 — Forward-Only Rubric Evolution

**Reviewer**: Percy Liang (Stanford, HELM benchmark lead)
**Venue target**: FAccT
**Score**: 3 (Weak Accept)
**Date**: 2026-04-19

---

## Substantive Engagement

I was asked to read this paper as someone whose team maintains HELM and has thought about benchmark versioning in detail, and I want to say upfront that the paper's §2.4 framing of benchmark versioning as "convergent practice rather than a literature ancestor" is exactly the right call. We did not derive HELM's versioning from the AERA Standards; we converged on the same fairness-by-versioning solution from an independent direction (reproducibility pressure from model evaluation), and the paper is correct to treat the two as parallel rather than parent-child. That is a precise scholarly move and I want to credit it.

Where the paper and HELM diverge — and where I think the paper could strengthen — is in what gets versioned. HELM versions the *evaluation pipeline* (prompts, metrics, task set, model list) but not the *evaluation criteria themselves*, because our criteria are mechanical: exact-match, BLEU, bias score, etc. LUCIA versions something HELM does not: the rubric's normative anchors. This is a substantive contribution, and I think the paper should claim it more clearly. "Forward-only versioning of normative anchors (not just pipelines or prompts)" is the differential contribution against HELM-style practice, and the paper somewhat buries it. The forward-overlay metric is genuinely novel as an instrument — HELM does not compute anything analogous because our task set is an unordered set rather than a cumulative document — and this deserves to sit in the abstract.

My concern from the benchmarks side is about *backwards-compatible reporting*. In HELM, when v0.3 replaces v0.2, we maintain the ability to report both scores for a given model, because users sometimes want to compare against old leaderboards. The paper's forward-only policy is analogous to HELM's: scores are reported with their version. But HELM also maintains a *re-run capability* — any historical model can in principle be re-evaluated against the current version — even if we don't re-run by default. The paper forecloses this option. §6.2 argues this is appropriate because scores are archival data points, but it would be a cleaner story if the paper acknowledged that *the option to re-score* is separable from *the policy of not re-scoring by default*. HELM's practice is "preserve original score; allow re-evaluation on request." LUCIA's is "preserve original score; decline to re-evaluate." The difference matters because it determines what a motivated reader can do retrospectively.

One more HELM-adjacent observation: we have learned, painfully, that benchmark versioning discipline degrades when the authoring team turns over. LUCIA is currently a single-editor project (over a five-day window). The forward-overlay discipline is held by one person. A policy-level claim about transportability (§6.4) should reckon with multi-editor scenarios, because in my experience the refinement-vs-reversal boundary is where inter-editor disagreement concentrates. The paper flags this in §7.5 but I would like to see a stronger pattern-transfer story — specifically, what inter-rater protocol would operationalize the classifier in a multi-editor setting.

---

## Major Issues

1. **The differential contribution against HELM-style practice is under-claimed.** Forward-only versioning of normative anchors (not pipelines) is the novel move. The abstract and §1.3 should foreground this rather than leaving it in §2.4. The forward-overlay metric likewise deserves an earlier spotlight.
2. **Re-score *capability* vs. re-score *default* are conflated.** HELM's practice preserves the option to re-evaluate historical models; the paper's forward-only policy forecloses it. This is a defensible choice but should be named as a choice, not treated as equivalent to benchmark versioning.
3. **Multi-editor transportability is claimed but untested.** §6.4's transportable pattern rests on classifier discipline, which in HELM's experience is the first thing to degrade across editors. An inter-rater study on the 15 amendment rows would close this, and I would expect it for a CHI submission; for FAccT it is a P2 advisory.

## Minor Issues

1. [NEED-D] should cite Liang et al. 2022 (HELM), and probably also Srivastava et al. 2022 (BIG-bench) for the versioning-as-practice angle.
2. The version-to-commit map in §10 is the kind of reproducibility artifact I wish more benchmarks published. Consider a short §4.6 (Reproducibility) that points at it explicitly rather than leaving it in Artifacts.
3. The per-step table in §5.2 is excellent data. Consider a small plot — preserved-lines vs. cumulative-amendments — which would make the stability visually obvious for skim readers.

---

## Quality-Improvement Framing

The paper is accurate about benchmark versioning and correctly identifies it as convergent rather than ancestral. The under-claimed contribution is that LUCIA versions what HELM does not — the normative criteria themselves — and the forward-overlay metric is the right instrument for it. Foregrounding that differential in the abstract and intro would make the paper's contribution sharper without changing any measurement. The multi-editor transportability concern is real but fair to defer to follow-up work.

**Score: 3** (Weak Accept for FAccT; revision to foreground the anchors-vs-pipeline differential.)

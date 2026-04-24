> **Note:** This is an AI-generated simulated review, written by Claude in the voice of a named-expert persona. It is not an actual review by the named person and does not reflect their views or endorsement.

# Review: PR-A2 — Forward-Only Rubric Evolution

**Reviewer**: Ljiljana Stojanovic (Karlsruhe, ontology evolution)
**Venue target**: FAccT
**Score**: 2 (Weak Reject — leaning toward major revision)
**Date**: 2026-04-19

---

## Substantive Engagement

The paper correctly identifies my community's ontology-evolution framework as a strictly stronger alternative, and I appreciate that the authors do not pretend otherwise — §2.2 is explicit that forward-only is weaker on retroactive comparability and bears the cost honestly. That disciplined honesty is rare. However, once I read the justification for choosing the weaker policy, I am not persuaded, and my concerns cluster around whether the authors have correctly characterized what bidirectional migration actually *costs* in their setting.

The paper's central defense is that LUCIA's scores are "archival data points" rather than "active classifications that need to be queryable against the current schema" (§2.2). This distinction is real in some settings, but the paper underestimates how often it collapses in practice. An archival data point becomes an active classification the moment any downstream process — a retrospective, a meta-analysis across rubric versions, a regression comparing chapters — treats the scored corpus as a unified dataset. The paper's own Measurement C *is* such a process: the re-score pilot implicitly requires a mapping between v1.0 and v1.7, and the authors supply that mapping ad hoc (they re-read the chapter under v1.7 anchors, a lightweight forward migration). So forward-only does not actually avoid the migration cost; it defers the cost to the point of use and makes it implicit rather than explicit. A bidirectional-migration policy would require the mapping to be stated up front, which is exactly what makes it more expensive at authoring time and cheaper at every subsequent use.

Related: the Extension / Refinement / Reversal classifier is sensible, but it is a coarser instrument than my 2004 taxonomy of change operators (add concept, delete concept, generalize, specialize, merge, split), each paired with a migration function. The paper's "12 Extensions, 3 Refinements, 0 Reversals" would, under my taxonomy, decompose into roughly six operator types, several of which (generalize, specialize) have known semantics for how prior scores should map forward. The paper inherits my language but not the operator-level discipline, and the result is that the reader cannot tell, for any given amendment, whether it generalizes or specializes the dimension it touches. The classifier passes the pre-registered threshold comfortably, so this is not a falsification issue — it is a precision issue.

The forward-overlay metric is a nice idea, but it is a textual invariant, not a semantic one. Line preservation at 99.6% is the correct number to report, but the paper should acknowledge that a preserved line can be *semantically inverted* by an adjacent added clause without the line itself changing. The authors note this risk in §7.4 (adversarial amendment), but the good-faith case also applies: an extension paragraph next to a preserved paragraph can narrow the preserved paragraph's meaning without editing it. The reversal classifier is meant to catch this, but at the coarse granularity the paper operates at, a subtle narrowing would likely be classified as Refinement, not Reversal.

---

## Major Issues

1. **The "archival data point" defense is under-specified.** The paper never operationally defines when a score becomes "active" versus remains "archival." Without that definition, the scope condition in §6.2 is rhetorical rather than technical. I would want a test: *if downstream process X occurs, the score has become active, and the forward-only justification weakens.* The re-score pilot itself is evidence that the line is porous.
2. **The classifier is coarser than the ontology-evolution operator taxonomy it inherits from.** A 3-category classifier cannot distinguish generalize from specialize from merge from split, all of which have different semantic implications for prior scores. The paper should either adopt the finer taxonomy or explicitly defend the 3-category reduction.
3. **Bidirectional migration is dismissed on operational grounds (§2.2, §6.2) without an actual cost estimate for LUCIA.** How many migration functions would seven amendment cycles have required? If the answer is ~15 (one per amendment row) and each is a few lines of prose, the "operationally demanding" framing is overstated.

## Minor Issues

1. [NEED-A] should cite both my 2004 dissertation and Guarino & Welty's OntoClean — the latter is the semantic-consistency check most relevant to your Measurement A.
2. §2.2 says bidirectional migration is "often mathematically under-constrained when the amendment introduces a genuinely new dimension." This is true but should be cited — Haase & Stojanovic 2005 addresses this directly.
3. The forward-overlay line-vs-word discrepancy (19.5% vs. 54.3%) is explained but mildly buried; consider making the word-granularity the headline number since the paper argues for substantive additive evolution.

---

## Quality-Improvement Framing

The paper positions itself accurately against my community's work, which I appreciate, but it leans on a distinction (archival vs. active) that is not carrying its weight. Either operationalize the distinction with a test, or revise the framing to "forward-only is cheaper at authoring time; bidirectional migration is cheaper at every use." The measurement work is solid and I would not block on it; my reservations are about the theoretical positioning rather than the empirical claims.

**Score: 2** (Weak Reject — willing to move to Weak Accept if the archival/active distinction is operationalized and the classifier is aligned with known operator taxonomy.)

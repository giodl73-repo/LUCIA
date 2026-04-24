> **Note:** This is an AI-generated simulated review, written by Claude in the voice of a named-expert persona. It is not an actual review by the named person and does not reflect their views or endorsement.

# Review — PR-A1 "The Innovation Engine"

**Reviewer**: Ece Kamar (Microsoft Research, complementarity and deferral in human-AI systems)
**Venue lens**: NeurIPS / AAAI / CHI
**Score**: 2 (Weak Accept / Borderline)

## Summary

The paper describes a pipeline in which an automated trigger (2-instance or 3-cluster) signals that an amendment is warranted, and a human editor drafts the amendment text. This is a deferral structure: the machine decides *when*; the human decides *what*. I read the paper specifically looking at the deferral — is it principled, or accidental? The answer I arrive at is: the split is coherent but the deferral is not principled in the complementarity-research sense. The engine does not *choose* to defer based on confidence or expected error; it always defers. That is a design choice, not a deferral policy.

## Substantive engagement

In the complementarity literature, a deferral mechanism is interesting because it selects when to hand off: the system routes high-confidence decisions to automation and low-confidence or high-stakes decisions to humans. The Innovation Engine does not do this. Its split is fixed: triggers always fire mechanically, and humans always draft the resulting amendment text. There is no adaptive routing. The paper's §6.3 correctly notes that fully-automatic amendment would require a trained model and would sacrifice legibility; that is a reasonable argument for the fixed split, but it is an argument against adaptive deferral, not an instance of it.

A more interesting version of this paper would measure *when the engine should have deferred differently*. Candidate measurements: (a) trigger firings the editor ultimately rejected — the engine was over-confident; (b) patterns the editor recognized but the engine did not trigger on — the engine was under-confident; (c) disagreement between the engine's 2-instance and 3-cluster pathways on the same underlying pattern — the engine's thresholds were inconsistent. None of these are reported. The Findings document indicates that the INNOVATIONS.md log has 30+ entries that are "logged-but-not-yet-adopted," which is exactly the category (b) signal. The paper does not analyze those 30+ entries. It should.

Second concern, also from a complementarity lens: the paper treats editor judgment as a constant ("the human editor" across 98 amendments) but this is a single-operator system. Complementarity research cares about *which* human and *under what conditions*. The paper's Threats to Validity §7.2 acknowledges editor variability; the paper's measurement does not account for editor fatigue, editor learning, or session-effects on editor behavior. The editor at chapter 115 is not the same decision-maker as the editor at chapter 1 — they have a 114-chapter prior. This is not discussed.

Third: the "calibration" frame. In ML calibration work, a system is calibrated when predicted confidence matches empirical accuracy. The engine reports its "calibration" in a different sense — trigger latency within a pre-registered window. That is a reasonable empirical result, but the word "calibration" is doing work across two communities, and the paper would benefit from either using a different word (timing-within-bounds, latency-boundedness) or explicitly distinguishing its sense from the ML-calibration literature. A hostile reviewer from the calibration community will object to the vocabulary.

## Major issues

1. **Deferral is fixed, not adaptive.** Frame the human-in-the-loop role as "always defer" rather than "principled deferral." This is defensible for a legibility-first system but needs to be called out so the complementarity-literature reader does not expect adaptive routing.
2. **30+ logged-but-not-adopted entries are unanalyzed.** These are exactly the engine's false-negatives or deferred-adoptions. A one-table analysis of why each sat unadopted (insufficient instances, principle unclear, editor judgment) would give the paper real complementarity-research relevance.
3. **Editor as constant is an unjustified abstraction.** At minimum, run the latency analysis stratified by session (Session 1 editor decisions vs. Session 2 editor decisions) to surface whether the editor's behavior changed. The data exists.

## Minor issues

1. Consider renaming "calibration" to "latency-boundedness" or "in-window timing" to avoid overlap with the ML-calibration literature, which uses the term for a different property.
2. The forward-only policy has an interesting complementarity angle — the human cannot *retroactively* defer, because forward-only locks the score. Worth a sentence.
3. A future-work note on adaptive deferral (trigger firing routes to one of several editorial paths based on pattern confidence) would close the loop with the complementarity literature and signal the authors know where this work sits.

## Recommendation

Weak accept. The paper is careful and the measurement is honest; the deferral framing is the main weakness from my lens. Reframing the human role as "fixed deferral by design" and analyzing the 30+ unadopted entries would strengthen the complementarity story without changing the paper's central claim.

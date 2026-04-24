> **Note:** This is an AI-generated simulated review, written by Claude in the voice of a named-expert persona. It is not an actual review by the named person and does not reflect their views or endorsement.

# Review — PR-A1 "The Innovation Engine"

**Reviewer**: Ben Shneiderman (University of Maryland, Human-Centered AI)
**Venue lens**: CHI
**Score**: 2 (Weak Accept / Borderline)

## Summary

The authors describe a pipeline for evolving a quality rubric during AI-assisted narrative production. The paper uses the phrase "semi-automatic" to describe the system, and §6.3 ("The Semi-Automatic Framing") is the section where the human role is explicitly articulated. I read the paper with one question foregrounded: is the human role here meaningful control, in the HCAI sense, or is it cosmetic — a rubber-stamp over what the engine has already decided?

## Substantive engagement

The authors deserve credit for not hiding the human. Many AI-assisted-production papers describe pipelines as if the models produce and evaluate themselves, burying the editor's role in acknowledgements. Here, §6.3 states plainly that the trigger rules are codified but the amendment text is human-drafted, and that the design choice is deliberate — "throughput cost for a legibility gain." The innovation log is inspectable, version-controlled, and pedagogically transparent. These are all HCAI-positive properties and the paper gets them right.

Where I am less confident is in characterizing the human's role as *control* rather than *acceptance*. The engine fires (2-instance or 3-cluster); the human editor then reviews the candidate instances, names the cluster, and writes the amendment text. The paper does not describe what happens when the human editor disagrees with the engine — does the editor veto a promotion? Has that ever occurred in the corpus? If every trigger firing has been accepted and amended, the "control" is formally present but empirically cosmetic: the human does the writing but not the deciding. If editors have vetoed promotions, that is data, and the veto rate is itself a calibration metric. The paper is silent on this.

A second concern, sharper for CHI: the paper claims the resulting rubric is a "teachable artifact" that "domain experts can inspect, argue about, and teach" (§2.2, §6.3). This is an HCI claim, not a measurement. There is no user study, no evidence that a second editor could pick up the rubric and apply it, no evidence that the innovation log supports the pedagogical use it is credited with. For a methods paper this omission might be acceptable, but the paper repeatedly invokes the legibility-teachability benefit to justify the semi-automatic design. The justification is load-bearing; it should bear some empirical weight.

Third: the paper's Threats to Validity §7.2 correctly names "Human-in-the-Loop Variability" — a different editor would produce different amendments. This is honest. But the paper then treats this as a limitation to mention rather than a variable to design around. HCAI principles would suggest designing the engine to surface disagreement, not minimize it: what if two editors scored the same cluster and the system recorded their disagreement? That would be meaningful human control.

## Major issues

1. **No data on human veto / override rate.** If the engine has fired 100 times and the editor has adopted 100 amendments, the human role is cosmetic. If vetoes exist, report them as calibration data. This is load-bearing for the "semi-automatic" claim.
2. **Teachability claim is asserted, not evidenced.** The paper says the rubric is inspectable and teachable. For a CHI audience, this needs at least a minimal user study, a reader-expert comprehension check, or an honest retreat from the claim.
3. **Single-editor confound is acknowledged but not designed around.** The engine as specified does not have a path to multi-editor operation. For an HCAI submission, sketching how the engine would handle editor disagreement — even as a future-work section — is reasonable.

## Minor issues

1. The innovation log's 7-field schema (§3.4) is a good HCAI artifact; a figure showing an example entry would help readers see the legibility claim concretely.
2. Forward-only amendment is defended on fairness grounds; framing it as a *user-facing* property (scorers see a stable rubric during review) would strengthen the HCAI positioning.
3. §6.4 offers a "transportable design pattern" — good. But it doesn't include the human role in the pattern. Add: "a named editorial role with codified veto authority."

## Recommendation

Weak accept for NeurIPS Creativity Workshop where the measurement is the contribution. For CHI, the paper needs the human-role measurements (veto rate, editor consistency, teachability check) before I would support acceptance. The work is solid; the HCAI story is under-developed.

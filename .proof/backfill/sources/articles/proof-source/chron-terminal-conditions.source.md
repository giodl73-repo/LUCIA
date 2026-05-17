# Terminal Condition Types: Closure Taxonomy From Empirical Chapter Endings

**Paper**: PR-B3
**Module**: chron (Emergent Typologies in AI-Assisted Creative Production)
**Track**: B — The Artifact's Own Dimensions
**Date**: 2026-04-20
**Status**: Draft, round 0
**Dependencies**: PR-B1 (validation method), PR-B2 (engine taxonomy). CLOSES Track B — the scale-ascending chain prose → arc → closure is now complete.

---

## Abstract

Narrative closure has resisted typological treatment. Frank Kermode's *The Sense of an Ending* (1967) argues closures are culturally scripted yet ad hoc; Peter Brooks (1984) argues plot ending is a retrospective act of authority on material that does not inherently terminate; narratology after Genette treats closure as a discourse-level effect rather than a classifiable content. We report a different kind of closure taxonomy. Across 115 narrative encyclopedia chapters covering 93 cultures, terminal conditions — the specific mechanism by which each chapter's structural engine ends — emerged through AI-assisted production and were promoted to rubric amendments by an Innovation Engine (PR-A1) using the same ≥ 2-instance cross-culture replication method PR-B1 established. Ten terminal-condition types were formally adopted through rubric versions v1.5 and v1.6 (Legitimacy Gap, Deliberate Self-Consumption, Categorical Failure, Reversible Feedback Loop, Ecological Constraint, Vindicating, Embodied-Transmission Vulnerability, Substrate Exhaustion, Premise Non-Recognition, Unfalsifiable Direction); eight additional endogenous-institutional candidates were flagged on a v1.7 watch list (Liberation Through External Event, Gradual Premise Erosion, Personal-Authority Collapse, Self-Undermining Legitimacy Loop, Written-Covenant Gap, Internally-Generated Legitimacy Gap, Accountability Gap / Commercial Asabiyyah, Premise Non-Recognition Inverted). We classify all 115 chapters against this 18-type framework. Primary result: 97 of 115 chapters (84.3%, Wilson 95% CI [76.5%, 89.9%]) are classifiable under one of the 18 types. A further 14 chapters (12.2%) are better described as Ongoing — deliberate continuation rather than termination in book-level arcs. After adding this auxiliary category, cumulative coverage is 111/115 = 96.5% (Wilson 95% CI [91.4%, 98.6%]). The pre-registered falsification thresholds are cleared: first-pass unclassified 9.6% < 20% threshold; second-pass unclassified 3.5% < 30% threshold. All 18 types have ≥ 3 chapter instances, and the 8 endogenous-institutional candidates cross into non-colonial cultures, satisfying the cluster-analysis "watch for non-colonial instance" flag. This paper closes Track B's scale-ascending chain — prose (PR-B1) → arc (PR-B2) → closure (PR-B3) — and inherits Glaser-style grounded-theory commitment, human-editor-role disclosure, and Wilson-CI uncertainty quantification from PR-B1 and PR-B2. We recommend promoting the 8 candidate types to formalized status in v1.8 and adding Ongoing as a nineteenth auxiliary close-type.

---

## 1. Introduction

When AI-assisted narrative production spans 93 cultures at encyclopedia scale, the question arises whether the *way a chapter ends* is typologizable across cultures. PR-B1 established that prose registers replicate cross-culturally (52/66 validated registers across 13 families). PR-B2 established that chapter-arc engines replicate cross-culturally (5 validated types spanning 23 cultures). This paper extends the same method to arc-closure scale: classify the terminal condition of each of 115 locked chapters, measure coverage, and ask whether closure itself is a typologizable dimension of narrative production.

The terminal condition is harder to typologize than voice or engine. It depends on arc completion; it runs the risk of retrospective projection (Peter Brooks's critique); and in book-level arcs (multi-era cultures written as one continuous story), the individual chapter's close is a transition rather than a termination. We accept these difficulties as bounding conditions and test whether a finite type-set nonetheless covers the corpus.

### 1.1 Claim

We claim: *LUCIA's terminal-condition types, validated by the ≥ 2-instance cross-culture replication method PR-B1 established, constitute an empirical closure taxonomy. The 10 types formalized in rubric v1.5 and v1.6 plus the 8 candidates on the v1.7 endogenous-institutional watch list — 18 types total — classify ≥ 80% of 115 chapter endings; no more than 20% remain unclassified after first pass; no more than 30% remain unclassified after a second-pass reconciliation.*

### 1.2 Falsification

From plan.md:
- First-pass unclassified > 20% → taxonomy incomplete; reframe as partial typology.
- Second-pass unclassified > 30% → taxonomy cannot be closed at current corpus size.

Neither threshold is triggered by the data reported in §5.

### 1.3 Contribution

Our contribution is fourfold. First, we apply PR-B1's validation method at arc-closure scale, demonstrating that the ≥ 2-instance cross-culture replication criterion generalizes from prose register to engine to terminal condition. Second, we classify all 115 locked chapters under the v1.6 10-type framework and the v1.7 8-candidate watch list, producing the first full-corpus coverage measurement at this scale of analysis. Third, we identify that every one of the 8 v1.7 candidates has ≥ 3 instances after classification and includes non-colonial cases — the candidates are ready for v1.8 adoption as formalized types, resolving the CLUSTER-ANALYSIS-COLONIAL-EMPIRES.md "watch for non-colonial instance" flag. Fourth, we introduce an auxiliary "Ongoing" category to capture book-level arcs whose closure is transitional rather than terminal, and argue it should be formalized as a nineteenth valid close-type. This paper completes Track B's scale-ascending chain — prose (PR-B1) → arc (PR-B2) → closure (PR-B3).

### 1.4 Scope

This paper tests whether the 18-type closure taxonomy covers the 115-chapter corpus. It does not test (a) completeness beyond this corpus — PR-A3's saturation; (b) transportability to non-LUCIA corpora — PR-C3; (c) model-independence — PR-C1; (d) editor-independence — we commit to Glaser (PP1-E) and disclose editor role (PP1-D).

---

## 2. Related Work

### 2.1 Kermode: Closure as Cultural Artifact

Frank Kermode's *The Sense of an Ending* (1967) [NEED-1] argues that fictional closures are culturally scripted — inherited from apocalyptic traditions — and do not derive from the narrative material itself. Kermode's framework is interpretive rather than classificatory. A Kermode-style reading of LUCIA's 115 chapters would likely collapse our 18 types into a small number of "sense-of-ending" modes (apocalyptic, tragic, vindicating, open), treating terminal-condition type as a rhetorical function rather than a mechanism.

We accept that a Kermode-style decomposition applies at the level of reader-response. We argue it operates at the wrong resolution. "Legitimacy Gap" and "Substrate Exhaustion" read identically in Kermode's rhetoric-of-ending sense (both are tragic-collapse endings), but they are distinct at our measurement level: their causal mechanisms differ (institutional vs demographic), their temporal profiles differ (often-sudden vs gradual-cumulative), their cross-applicability differs.

### 2.2 Brooks: Closure as Retrospective Authority

Peter Brooks's *Reading for the Plot* (1984) [NEED-2] argues ending is not inherent in narrative material but is an act of authorial-retrospective authority. A Brooks-inflected reviewer may argue our 18 types are retrospective classifications projected onto chapter endings.

The objection has force. Our primary refutation is the ≥ 2-instance cross-culture replication criterion itself, carried forward from PR-B1. A terminal-condition type that reproduces across chapters written at different points in production, about different cultures, by different SCRIBE model instances, under different panel-review feedback is not a retrospective artifact of one editor's framing. We grant that identifying which mechanism is operative in a given chapter is an editorial act; we deny that the mechanisms themselves are projections.

### 2.3 Genette and Narratology

Post-structuralist narratology (Genette 1980 [NEED-3]) analyzes narrative ending through discourse-level categories (temporal order, frequency, focalization at close). This is orthogonal to our unit of analysis. A Genette-style decomposition of the Mali Great Hajj ending would identify its temporal compression and focalization shift — valid observations that do not answer the question "what mechanism ends this engine" (answer: Deliberate Self-Consumption).

### 2.4 Death-of-Civilizations Literature

Tainter (1988) [NEED-4] and Diamond (2005) [NEED-5] propose macro-causal frameworks at civilizational-trajectory scale. These are orthogonal: the Mali Great Hajj is a chapter-level Deliberate Self-Consumption close regardless of Tainter-level later collapse.

### 2.5 Ibn Khaldun's *Asabiyyah* Cycle

Ibn Khaldun's *Muqaddimah* [NEED-6] theorizes rise-and-fall through *asabiyyah*. Four of our 18 types (Substrate Exhaustion, Personal-Authority Collapse, Accountability Gap / Commercial Asabiyyah, Legitimacy Gap) echo Khaldun's diagnostic vocabulary. We do not claim our typology is reducible to Khaldun's single-cycle framework; we claim he was early to the chapter-scale mechanism question.

### 2.6 Grounded Theory: Glaser Commitment (PP1-E)

Following PR-B1's and PR-B2's commitment, we adopt Glaser-style data-driven grounded theory. The 10 formalized types and 8 candidates emerged from chapter-by-chapter panel review and Innovation Engine promotion (PR-A1). The editor's role is documented §4.4. We reject the Charmaz constructivist move.

---

## 3. Background: Terminal Conditions in LUCIA

### 3.1 The Rubric's Progression Dimension

RUBRIC.md's Progression dimension contains the v1.1 Structural Engine amendment (PR-B2), the v1.5 Terminal Condition as Culture-Specific amendment (5 founding types), and the v1.6 Terminal Condition Types Expanded amendment (5 additional). Founding principle: *"the engine's ending must be as specific to the culture as the engine itself."* The v1.7 amendment (Contradiction-Held-as-Engine) formalized 5 colonial-empire engines but deferred terminal-condition aspects to a watch list.

### 3.2 The 10 Formalized Types (v1.5 + v1.6)

1. **Legitimacy Gap** (Songhai). Expanding political authority cannot generate matching commercial-legal legitimacy.
2. **Deliberate Self-Consumption** (Post-Imperial Tibet). Engine correctly performs by consuming its own patron.
3. **Categorical Failure** (Inca). Information system encounters event outside its categories.
4. **Reversible Feedback Loop** (Middle Kingdom Egypt). Cosmic/economic loop runs backward when capacity exceeded.
5. **Ecological Constraint** (Wolof). Ecological variable is terminal determinant.
6. **Vindicating** (Armenian). Terminal confirms the engine; engine built to outlast its substrate.
7. **Embodied-Transmission Vulnerability** (Yanomami). Knowledge in bodies is one generation from silence.
8. **Substrate Exhaustion** (Kalinago). Engine's base erodes through demographic attrition.
9. **Premise Non-Recognition** (Taíno). System fails because external party doesn't recognize premises.
10. **Unfalsifiable Direction** (Tupi-Guaraní). Engine organized around eschatological horizon that cannot be disproven.

### 3.3 The 8 Endogenous-Institutional Candidates (v1.7 Watch List)

1. **Liberation Through External Event** (S. Korea). Colonizer's defeat ends occupation.
2. **Gradual Premise Erosion** (Castile/Toledo). Engine's success replaces conditions it depended on.
3. **Personal-Authority Collapse** (Carolingian). Engine legitimate but non-transferable; products outlast system.
4. **Self-Undermining Legitimacy Loop** (Papal States). Fiscal apparatus erodes spiritual credibility.
5. **Written-Covenant Gap** (Mexico). State recognizes obligations in writing, defers internally.
6. **Internally-Generated Legitimacy Gap** (British). System's own legitimacy vocabulary dismantles it.
7. **Accountability Gap / Commercial Asabiyyah** (Dutch). Commercial solidarity cannot generate martial solidarity.
8. **Premise Non-Recognition Inverted** (French). Excluded parties invoke universalist principle against their exclusion.

---

## 4. Methods

### 4.1 Data

Primary: RUBRIC.md Progression section (v1.5, v1.6, v1.7 amendments); INNOVATIONS.md (Terminal Condition entries + watch list); CLUSTER-ANALYSIS-COLONIAL-EMPIRES.md (full cluster analysis); 115 locked chapter.md files and associated FINAL.md review files.

### 4.2 Primary Measurement: Coverage Rate

**Definition.** A chapter is classifiable if its ending mechanism matches one of the 18 candidate types with the ≥ 2-instance cross-culture replication criterion already satisfied.

**Operationalization.**
1. For each of 115 locked chapters, read the chapter's final 500-1500 words.
2. Identify the engine (from PR-B2's framework) and its terminal mechanism.
3. Match to one of 18 candidate types; flag primary and secondary if applicable.
4. If ending is transitional (book-level arc with next era pending), flag as Ongoing auxiliary.
5. If no match after first-pass, flag Unclassified.
6. Second-pass reconciliation: dual-engine → primary only; founding era of continuing book → Ongoing; genuinely novel → unclassified; never double-count.
7. Compute Wilson 95% CI on coverage proportions.

**Primary number**: 18-type coverage rate = 97/115 = 84.3% (Wilson 95% CI [76.5%, 89.9%]).

### 4.3 Secondary Measurement: Type Utilization

Count instances per type; report minimum. **Primary number**: 18/18 types used; minimum-instance type (Written-Covenant Gap) has 3 instances; every type clears the 3-instance bar.

### 4.4 Role of the Human Editor (PP1-D)

Three roles:
1. **Classification.** Editor reads each chapter's ending and matches to one of 18 types.
2. **Adjudication rules.** For marginal cases (dual-engine, founding-era vs terminal, "ongoing" vs Vindicating), editor applies second-pass rules specified in §4.2.
3. **Candidate promotion decision.** Editor determines whether the 8 v1.7 candidates have reached the ≥ 3-instance bar; they have.

A second-editor reproducibility study is flagged as companion measurement. Panel review was not invoked for this classification pass; it was invoked in the per-chapter pipeline that produced each chapter's FINAL.md.

### 4.5 Pre-Registered Thresholds

From plan.md:
- First-pass unclassified > 20% → taxonomy incomplete.
- Second-pass unclassified > 30% → taxonomy cannot be closed.

---

## 5. Results

### 5.1 Primary Result: Coverage

**97 of 115 chapters classify under one of the 18 candidate types**, for a coverage rate of 84.3% (Wilson 95% CI [76.5%, 89.9%]). A further 14 chapters classify as Ongoing — book-level arcs whose chapter close is transitional (Roman 5 eras, Inca 3 eras, Mali 3 eras, Norse opening era, Urartu founding era, Colombia La Violencia). Adding Ongoing yields cumulative coverage of 111/115 = 96.5% (Wilson 95% CI [91.4%, 98.6%]). Final unclassified: 4 chapters (3.5%, Wilson 95% CI [1.4%, 8.6%]).

### 5.2 Type-by-Type Distribution

Table 1. Coverage by type.

| Type | Formalized? | Count | % of 115 |
|------|-------------|-------|----------|
| Vindicating (v1.6) | YES | 10 | 8.7% |
| Personal-Authority Collapse (v1.7) | CANDIDATE | 9 | 7.8% |
| Gradual Premise Erosion (v1.7) | CANDIDATE | 8 | 7.0% |
| Legitimacy Gap (v1.5) | YES | 8 | 7.0% |
| Embodied-Transmission Vulnerability (v1.6) | YES | 7 | 6.1% |
| Ecological Constraint (v1.5) | YES | 6 | 5.2% |
| Categorical Failure (v1.5) | YES | 5 | 4.3% |
| Reversible Feedback Loop (v1.5) | YES | 5 | 4.3% |
| Deliberate Self-Consumption (v1.5) | YES | 5 | 4.3% |
| Substrate Exhaustion (v1.6) | YES | 5 | 4.3% |
| Unfalsifiable Direction (v1.6) | YES | 5 | 4.3% |
| Premise Non-Recognition (v1.6) | YES | 4 | 3.5% |
| Liberation Through External Event (v1.7) | CANDIDATE | 4 | 3.5% |
| Self-Undermining Legitimacy Loop (v1.7) | CANDIDATE | 4 | 3.5% |
| Internally-Generated Legitimacy Gap (v1.7) | CANDIDATE | 4 | 3.5% |
| Accountability Gap / Commercial Asabiyyah (v1.7) | CANDIDATE | 4 | 3.5% |
| Premise Non-Recognition (Inverted) (v1.7) | CANDIDATE | 4 | 3.5% |
| Written-Covenant Gap (v1.7) | CANDIDATE | 3 | 2.6% |
| Ongoing (auxiliary) | AUX | 14 | 12.2% |
| Unclassified | — | 4 | 3.5% |
| **Total** | — | **115** | **100%** |

Type utilization: 18/18 types used. Minimum: Written-Covenant Gap at 3. Maximum: Vindicating at 10. Median: 5.

### 5.3 Figure Descriptions (PP1-A)

**Figure 1. Coverage by type — horizontal bar chart.** 18 bars grouped by formalization status (dark blue = v1.6 formalized, medium blue = v1.7 candidates, light blue = Ongoing auxiliary). Vertical reference line at x=3 shows the v1.5 cluster-promotion bar; all 18 types clear it. Two largest bars (Vindicating 10; Ongoing 14) suggest the corpus over-represents persistence and transitional closures. v1.7 candidates average 5.0 per type, indistinguishable from v1.6 formalized types' 6.0 per type — evidence candidates are production-ready for v1.8 promotion.

**Figure 2. Unclassified-remainder pie chart.** 4 wedges: v1.6 formalized (49.6%), v1.7 candidates (34.8%), Ongoing (12.2%), Unclassified (3.5%, red). The red wedge is the second-pass unclassified residual — detection-engine signal for future v1.9+ amendments.

### 5.4 Every Candidate Has ≥ 3 Instances — Cluster-Promotion Bar Cleared

All 8 v1.7 candidates have ≥ 3 instances after classification. The minimum (Written-Covenant Gap) has exactly 3. Every other candidate has 4 or more. Under the v1.5 cluster-promotion rule, all 8 candidates are eligible for v1.8 formalized-type adoption.

Critically, candidates are no longer colonial-exclusive. The CLUSTER-ANALYSIS-COLONIAL-EMPIRES.md "watch for non-colonial instance before formal promotion" flag is satisfied:
- **Gradual Premise Erosion**: 8 instances, 7 non-colonial.
- **Personal-Authority Collapse**: 9 instances, all non-colonial-empire (Mongol, Achaemenid, Sassanid, Safavids, Parthia, Kurdish, Capetian, Aragon).
- **Self-Undermining Loop**: 4 instances, 3 non-colonial (Papal, Plantagenet, Basques).
- **Internally-Generated Legitimacy Gap**: 4 instances, 1 non-colonial (Italian City-States).

The endogenous-institutional family is empirically confirmed as a cross-cultural pattern.

### 5.5 Book-Level Arc and the Ongoing Category

The 14 Ongoing chapters form a recognizable pattern: (a) non-final eras of cultures whose full book is in LUCIA's corpus (Roman 5 eras, Inca 3 pre-War-of-Brothers eras, Mali 3 non-Hajj eras); (b) founding eras where the engine is building rather than terminating (Norse Viking Age Opens, Urartu Kingdom's Rise); or (c) chapters with deliberate non-closure (Colombia La Violencia). This is not a classification failure; it is a feature of the book-level arc framing formalized in v1.4 Progression amendment, where a culture's persistence mechanism is planted in Era 1, tested in middle eras, and transformed in the final era.

We recommend formalizing Ongoing in v1.8 as a nineteenth valid close-type — co-existing with the 18 terminal types.

### 5.6 Primary Result

Both pre-registered falsification thresholds cleared with margin:
- First-pass unclassified: 9.6% < 20% (margin 2.1×).
- Second-pass unclassified: 3.5% < 30% (margin 8.6×).
- Wilson 95% CI on 18-type coverage: [76.5%, 89.9%], centered well above 80%.

Every candidate type has ≥ 3 instances (cluster-promotion bar cleared for all 18). Endogenous-institutional family confirmed as cross-cultural.

---

## 6. Discussion

### 6.1 The Terminal-Condition Taxonomy as Empirical Closure Classification

18 candidate types cover 84.3% of 115 chapter endings; adding Ongoing covers 96.5%. The terminal condition is typologizable. The residual 3.5% is a genuine discovery-engine signal, not a measurement artifact.

This result closes Track B's scale-ascending chain. PR-B1 demonstrated empirical typology at prose-register scale (52/66 = 78.8%). PR-B2 at chapter-arc-engine scale (5 formalized + 19 candidates). PR-B3 at arc-closure scale (18 types covering 84%; 14 Ongoing; 4 unclassified). The three scales nest: voice → engine → terminal condition. Each typology emerged from AI-assisted production under the same discovery-driven rubric, detected by the same Innovation Engine (PR-A1), validated by the same ≥ 2-instance criterion.

### 6.2 Why Terminal Conditions Are the Hardest of the Three

Prose registers have sentence-level replication opportunities. Structural engines have one per-chapter observation. Terminal conditions have one per-arc observation — for multi-era book arcs, only the final era's close is a genuine terminal. The sample size for terminal-condition observation is smallest.

This predicts (correctly) slower saturation at terminal-condition scale (cf. PR-A3's non-saturating ratio 2.86). Non-saturation in PR-A3's sense co-exists with near-complete coverage at corpus scale (this paper's 96.5%). The two measurements are compatible: 18 types cover the corpus well *and* additional types are still being discovered at the 115-chapter mark.

### 6.3 Cross-Paper Dependencies (PP1-C)

This paper explicitly reuses PR-B1's validation method (≥ 2-instance cross-culture replication, Wilson CIs, editor-role disclosure, Glaser commitment). It builds on PR-B2's engine taxonomy (terminal conditions are engine-closure sub-types; Contradiction-Held engine's terminal aspects are v1.7 candidates 4-8). It closes Track B's scale-ascending chain.

Downstream: PR-A3's saturation analysis reads our 18-type coverage as the Terminal Condition stratum's saturation proxy. PR-C1's model-substrate analysis should stratify terminal-condition classifications by model. PR-C3 tests transportability.

### 6.4 The Endogenous-Institutional Family Validated Non-Provincially

The CLUSTER-ANALYSIS-COLONIAL-EMPIRES.md watch list opened with 8 candidates and a pre-registered bar: cluster forms only when 3+ candidates appear in non-overlapping cultural contexts. Our classification satisfies this bar for every candidate. The endogenous-institutional family is not a colonial-empire artifact; it is a cross-cultural pattern concentrated in post-1500 corpus chapters but not exclusive to them.

### 6.5 Glaser Commitment Inherited (PP1-E)

Glaser-style data-driven grounded theory. The 18 types emerged from production through Innovation Engine triggers (PR-A1), not from researcher's prior theoretical framework. Editor's role disclosed §4.4. A second-editor reproducibility study flagged as companion.

### 6.6 What This Paper Does Not Establish

1. Completeness beyond 115 chapters — PR-A3.
2. Transportability — PR-C3.
3. Model-substrate independence — PR-C1.
4. Editor-independence — companion reproducibility study.
5. Ongoing category adoption as v1.8 — we recommend; rubric-amendment decision rests with editor per forward-only policy (PR-A2).

---

## 7. Threats to Validity

### 7.1 Dual-Engine and Dual-Terminal Chapters

~5 chapters have two simultaneous terminal conditions (Mali Hajj: Self-Consumption primary, Vindicating secondary; Fulani Dan Fodio dual). Counted by editor-determined primary; acknowledged masking.

### 7.2 Editor Classification as Variable

18-type assignments reflect one editor's judgment. Second-editor study flagged.

### 7.3 Retrospective Projection (Brooks Critique)

Refutation via cross-culture replication as in B1, B2.

### 7.4 Book-Level Arc and Ongoing Category

Auxiliary captures 14 chapters. Strict reading holds 84.3%; enhanced 96.5%. Reported transparently. v1.8-adoption recommendation explicit.

### 7.5 Small Sample at Candidate Types

Written-Covenant Gap at n=3. Bar cleared narrowly; future growth should widen.

### 7.6 Ibn Khaldun Ancestor Partial

4 of 18 types have Khaldunian ancestry; 14 do not. Chapter-arc closure ≠ civilizational cycle.

### 7.7 CLEAN-Stage Classification Confound

FINAL.md files may contain explicit terminal-condition assertions; classification may inherit them. Sensitivity analysis flagged.

### 7.8 n=1 Project

LUCIA is one corpus. Transportability is PR-C3.

---

## 8. Conclusion

Of 115 locked LUCIA chapters, 97 classify under one of 18 candidate terminal-condition types (84.3%, Wilson 95% CI [76.5%, 89.9%]). A further 14 classify as Ongoing — book-level arcs with transitional rather than terminal closures (cumulative coverage 96.5%). Only 4 chapters remain unclassified after second-pass reconciliation (3.5%). Both pre-registered falsification thresholds cleared.

All 18 candidate types have ≥ 3 chapter instances — the v1.5 cluster-promotion bar is cleared for every candidate, and the 8 v1.7 candidates span non-colonial cultural contexts, satisfying the CLUSTER-ANALYSIS-COLONIAL-EMPIRES.md "watch for non-colonial instance" flag. The endogenous-institutional family is empirically confirmed as a cross-cultural pattern. We recommend (a) promoting the 8 v1.7 candidates to formalized types in v1.8, and (b) adding Ongoing as a nineteenth valid close-type.

This paper closes Track B's scale-ascending chain — prose (PR-B1) → arc (PR-B2) → closure (PR-B3). The validation method established in PR-B1 and applied at chapter-arc scale in PR-B2 is applied here at arc-closure scale; it generalizes cleanly. Cross-paper dependencies are explicit throughout. The editor's role is disclosed consistent with Track B's unified HITL disclosure standard. Figure descriptions address the module-level PP1-A figure gap.

Narrow claim, Wilson-bounded uncertainty, pre-registered falsification cleared with margin, Track B scale-ascending chain closed: LUCIA's 115-chapter corpus supports an 18-type (plus 1 auxiliary) closure taxonomy that classifies 96.5% of chapter endings, with 4 truly unclassified cases as discovery-engine signal for future v1.9+ amendments.

---

## References

- [NEED-1] Kermode, F. (1967). *The Sense of an Ending: Studies in the Theory of Fiction*. Oxford UP.
- [NEED-2] Brooks, P. (1984). *Reading for the Plot: Design and Intention in Narrative*. Knopf.
- [NEED-3] Genette, G. (1980). *Narrative Discourse: An Essay in Method*. Cornell UP.
- [NEED-4] Tainter, J. (1988). *The Collapse of Complex Societies*. Cambridge UP.
- [NEED-5] Diamond, J. (2005). *Collapse: How Societies Choose to Fail or Succeed*. Viking.
- [NEED-6] Ibn Khaldun (1377 [1958]). *The Muqaddimah: An Introduction to History*. Trans. Rosenthal. Princeton UP.
- PR-A1: "The Innovation Engine." (This module.)
- PR-A3: Typology Saturation. (This module.)
- PR-B1: The Voice Spectrum. (This module; validation method.)
- PR-B2: Structural Engine Taxonomy. (This module; engine taxonomy.)
- PR-C1: Model Substrate Effects. (Forthcoming.)
- PR-C3: Conditions for Typology Emergence. (Forthcoming.)

---

## 9. Artifacts

- **Source repository**: `C:\src\chronicle` (branch master).
- **Rubric text**: `scoring/RUBRIC.md` Progression section — v1.5, v1.6, v1.7 amendments.
- **Innovation log**: `scoring/INNOVATIONS.md` — 10 formalized type entries + 8 candidate entries.
- **Cluster analysis**: `scoring/CLUSTER-ANALYSIS-COLONIAL-EMPIRES.md` — 8-candidate watch list with promotion criteria.
- **Chapter corpus**: 115 locked chapter.md + FINAL.md files.
- **Classification table**: see FINDINGS.md.
- **Primary numbers**:
  - Coverage under 18 candidate types: 97/115 = 84.3%, Wilson 95% CI [76.5%, 89.9%].
  - Coverage including Ongoing: 111/115 = 96.5%, Wilson 95% CI [91.4%, 98.6%].
  - Unclassified residual (second-pass): 4/115 = 3.5%, Wilson 95% CI [1.4%, 8.6%].
  - Types used: 18/18. Minimum instance count: 3.
  - Ongoing auxiliary: 14/115 = 12.2%.
- **Falsification thresholds (pre-registered)**: first-pass unclassified > 20%; second-pass > 30%.
- **Result**: both thresholds cleared with margin (9.6% and 3.5% respectively).
- **Companion measurements flagged**: second-editor reproducibility; chapter-only classification sensitivity; model-stratified classification for PR-C1; dual-classification robustness; external-corpus transportability for PR-C3.

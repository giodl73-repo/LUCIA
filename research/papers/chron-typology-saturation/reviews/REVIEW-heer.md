> **Note:** This is an AI-generated simulated review, written by Claude in the voice of a named-expert persona. It is not an actual review by the named person and does not reflect their views or endorsement.

# Review — Jeffrey Heer (visualization, UW)

**Paper**: PR-A3 — Typology Saturation: Convergence Evidence in a Self-Evolving Quality Rubric
**Reviewer lens**: Visualization of quantitative time-series, especially accumulation/saturation curves
**Score**: 2/4 (Major revision)

---

## Substantive review

Let me start with what I think the paper is trying to do visually and why the current presentation fails it. The central empirical finding is that three typologies have three qualitatively different saturation profiles. That finding is *inherently* a comparative-curves claim: three curves on the same axes, with the shape comparison as the payoff. The paper presents this as four tables (§5.1, §5.2, §5.3, §5.4) plus a summary table (§5.5). There is not a single figure in the paper. A reader has to mentally plot 16 numbers (4 cohorts × 4 series) in their head to see what the paper says is its most important result. This is a visualization failure.

The basic chart I want to see is trivial to produce: x-axis = cohort (or, better, cumulative chapter count), y-axis = new innovations per chapter, three lines (Voice, Engine, Terminal) plus the aggregate as a fainter fourth line. With error bars (or shaded bands) from a Poisson or bootstrap uncertainty estimate. With the 80% falsification threshold marked as a horizontal reference, or — better — with the per-cohort *ratio to Cohort 1* plotted on a second axis so the threshold line is meaningful. This is 20 minutes in matplotlib or vega-lite. The paper's substantive claim would read directly off the chart. The tables are fine as supplements, but they should not be carrying the interpretive load alone.

The second missing visualization is the *cumulative* distinct-types curve per typology — the actual saturation curve, in the shape one would recognize from the ecology literature the paper cites. New-types-per-cohort (the paper's current rate metric) is a *derivative* of the cumulative curve; the cumulative curve is what "saturation" visually means. An ecologist reading §5 will want to see the S(n) curve flattening toward an asymptote for Voice and Engine, and continuing to rise for Terminal. That chart would make the scale-dependent finding immediate rather than argumentative. Without it, the reader has to re-integrate the rate table in their head.

Third, the paper treats n=4 cohorts as a limiting constraint on analysis (§4.5) but it is also a visual constraint. Four points per line is too few for a conventional line chart to read well — the eye cannot distinguish a monotonic decline from a noisy fluctuation at n=4. The honest visualization here would use per-chapter or per-five-chapter bins (from the chapter-level timestamp data the paper flags as companion measurement) and plot the curves at higher resolution. If the per-chapter data exists, use it. If it does not, the paper should acknowledge that the cohort-level curves have limited visual resolving power, and this is itself a reason for the companion measurement.

Fourth minor point on display integrity: the summary table in §5.5 presents "Ratio" as a single number per row but the three ratios (0.09, 0.00, 2.86) span two orders of magnitude and carry very different uncertainties. A forest-plot-style display with CI bars would communicate the finding more honestly than the table, which reads all three numbers as equally precise point estimates.

## Major concerns

1. **No figures.** The core finding is a three-curve comparative claim and the paper has zero visualizations. Minimum one figure: per-cohort rate curves for three typologies + aggregate, with uncertainty bands and threshold reference line.
2. **No cumulative saturation curves.** The ecology literature the paper cites communicates saturation through cumulative S(n) curves. These should be in §5 — one panel per typology, with Voice/Engine visibly flattening and Terminal visibly not.
3. **n=4 cohort resolution is too coarse to visualize credibly.** If per-chapter timestamps are available (flagged as companion measurement), use them. If not, acknowledge the visualization limit explicitly.

## Minor concerns

1. §5.5 summary table presents ratios as equivalent point estimates; a forest-plot or similar uncertainty-aware display would be more honest.
2. §5.4's "Cohort 3 spike" for Terminal Condition is discussed textually; a chart would let the reader see the spike and ask their own questions about it.
3. If the paper proceeds to the Digital Humanities / CHR venue, visualization quality is scrutinized heavily. Address now rather than in revision.
4. Small point: color/line-style choices matter when distinguishing three series that will be interpreted as semantically ordered (prose → arc → closure). Use a sequential palette rather than categorical.

**Verdict**: Major revision. The empirical work appears sound but the presentation is under-visualized to the point of obscuring the core finding. Add figures before resubmission.

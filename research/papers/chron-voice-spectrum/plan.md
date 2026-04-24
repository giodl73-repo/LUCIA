# PR-B1 — The Voice Spectrum: An Empirical Typology of Prose Registers Discovered Through AI-Assisted Production

**Track**: B (The Artifact's Own Dimensions)
**Position in chain**: First paper — establishes validation method used by B2 and B3.
**Status**: planned, round 0

---

## Hypothesis

Prose voice registers are empirically typologizable when discovered bottom-up from AI-assisted production at scale. A register is a typological entry (not a chapter-specific log) when it satisfies three criteria: sustained at ~5,000-word chapter length, replicated across culturally-different chapters, and exhibits zero or near-zero em-dash count as an emergent property of its own rhythm.

## Quantification Contract

| Component | Value |
|-----------|-------|
| Primary number | Register validation rate: fraction of logged registers that reach ≥ 2 instance-confirmation across culturally-different chapters. Plus: zero-em-dash emergence rate (fraction of registers where em-dash count is ≤ 2 per 5,000 words without enforcement). |
| Experiment design | For each of 50+ logged registers, enumerate instances, check cross-culture breadth, count em-dashes at chapter length. |
| Decision it changes | Whether Voice Spectrum is a typology (registers replicate) or a chapter-specific log (one-offs). |
| Null fallback | < 40% of registers reach 2nd instance → most entries are chapter-specific, not a typology; reframe as a log. |
| Falsification condition | < 40% validation rate OR zero-em-dash emergence < 50% of validated registers. |

## Outline

1. **Introduction.** Voice as prose register, not as stylistic choice. The question: can registers be a typology?
2. **Discovery method.** Bottom-up from AI-assisted production. The 11-stage pipeline's role. Panel review's role.
3. **Validation criteria.** Sustained length, cross-culture breadth, emergent em-dash property.
4. **The 50+ registers.** The typology as it stands. Family structure (Griot, Oral-Tradition, Maritime, Legal-Public, Philosophical-Devotional, etc.).
5. **Results — validation rate.** How many of 50+ hit 2nd-instance confirmation? Breadth metric.
6. **Results — zero-em-dash emergence.** Frequency at which the register's own rhythm eliminates em-dashes without enforcement.
7. **Case studies.** Three registers in depth: one first-session (Griot), one mid-session (Forest-Intimate), one third-session (Prophetic-Rhythmic).
8. **Discussion.** Voice Spectrum as empirical typology. What it means for AI-assisted prose generation.
9. **Falsification.** Thresholds.

## Data Sources

- `guides/VOICE-SPECTRUM.md` (standalone reference doc with 50+ registers)
- Voice-related innovation entries in `scoring/INNOVATIONS.md`
- 115 locked chapter files for em-dash counts and register identification

## Anticipated Failure Modes

- Zero-em-dash count can be enforced by prompt instruction — must verify it's emergent, not instructed. LUCIA's prompts explicitly do NOT instruct zero em-dashes; the property emerges from register discipline.
- Register identification is judgment-call at the margins. Pre-register identification criteria.
- Some registers have one dominant instance (chapter) plus partial sibling-instances; define "instance" strictly.

## Venue

EMNLP (empirical NLP register typology) or ACL.

## Dependencies

None within Track B (first in chain).

## Blocks

PR-B2 (requires validation method), PR-B3 (requires B2).

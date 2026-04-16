You are running /chronicle-notes for: {{people}}, {{era}}

Write the production bible (notes.md) — the plan the full chapter will execute.
This is not a draft. It is the thinking that makes the draft possible.

---

## Input

- **People**: The culture being written
- **Era**: The era within that culture's periodization

Prerequisites:
- `opening.md` exists and has passed GATE-1
- PANEL-1 reviews exist in `reviews/`

---

## Step 1 — Synthesize Panel Feedback

Read all 5 PANEL-1 reviews (`R1-P1` through `R1-P5`). Before responding
to any, read all five. Note:
- Where multiple reviewers converge on the same concern
- Where reviewers contradict each other (these tensions are productive)
- The specific weaknesses each voice identified

---

## Step 2 — Write the Seven Sections

### 2a. Sources

List every source, organized by tier:

**Primary:** Original texts, inscriptions, oral traditions. For each: what
it contributes to this specific chapter.

**Academic:** Peer-reviewed journals, monographs, archaeological reports.
For each: what you are drawing from it.

**Needed (ACQUISITION):** Sources that would strengthen the chapter but are
not yet in hand. These feed into `sources/ACQUISITION.md`.

### 2b. Key Figures

| Name | Their Role | Why They Matter to This Era |
|------|-----------|----------------------------|
| [Name in their language] | [Title/role in their terms] | [Why this person carries part of the era's story] |

2-5 figures. Fewer than 2 risks leaving the era without human faces.
More than 5 risks losing the reader.

### 2c. Narrative Arc

2-3 paragraphs: What is the story of this era? What changes? What is the
central tension? How does it resolve, or how does it not resolve?

This is the spine the chapter hangs on. If you cannot write it clearly,
you do not yet know what you are writing. Do not proceed until this is solid.

### 2d. Section Plan

| Section | Content | Word Target | Key Source | Panel Risk |
|---------|---------|-------------|------------|------------|
| 1 — Opening | [Scene] | ~800w | [Source] | [Which panel voice will push] |
| 2 | [Content] | ~700w | [Source] | [Panel risk] |
| 3 | [Content] | ~700w | [Source] | [Panel risk] |
| 4 | [Content] | ~700w | [Source] | [Panel risk] |
| 5 | [Content] | ~700w | [Source] | [Panel risk] |
| 6 — Landing | [Close] | ~600w | [Source] | [Panel risk] |

### 2e. Panel Pressure Points

One paragraph per panel voice, anticipating what they will push on:

- **Tuchman (craft):** Pacing risks, arc weaknesses, chronological plodding
- **Ibn Khaldun (systems):** Where causal depth is thin, where it describes without explaining
- **Achebe (voice):** Where inside-not-outside is most at risk
- **Davis (wonder):** Hidden hierarchy risks, shallower treatment of knowledge systems
- **Kapuscinski (immersion):** Where sensory grounding is thin, abstract sections needing anchoring

### 2f. Sensory Palette

Catalog the physical world of this era: sounds, smells, textures, tastes,
temperatures, light quality. These details come from research, not imagination.
They will be deployed throughout the chapter.

### 2g. Voice Notes

Notes on the prose register for this chapter: what cadence fits this culture
and era? What rhythm to sustain? Which voice spectrum entry from the Style
Guide applies? Specific phrasing tendencies to maintain or avoid.

---

## Output

Write to: `regions/{{region}}/{{people}}/eras/{{era}}/notes.md`

Template reference: `guides/TEMPLATES.md` (notes.md template)
Process reference: `guides/HOW-TO-WRITE-A-CHAPTER.md` (Section 4)

## Checklist

- [ ] All 5 PANEL-1 reviews read and synthesized
- [ ] All 7 sections present
- [ ] Narrative arc is clear and solid
- [ ] Section plan accounts for full ~5000 word target
- [ ] Panel pressure points anticipate each voice's concerns
- [ ] Sensory palette grounded in research
- [ ] ACQUISITION items flagged for sources not yet in hand

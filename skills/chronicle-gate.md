You are running /chronicle-gate for: {{artifact}}

Score an opening or chapter against The Gate (30pts) or The Chronicle (60pts)
rubric. The scorer is a separate role from the author — score what is on the
page, not what the author intended.

---

## Input

- **Artifact**: Path to `opening.md` (GATE-1) or `chapter.md` (GATE-2)

Auto-detect which rubric based on artifact type:
- `opening.md` → The Gate (30pts, 6 dimensions x 0-5)
- `chapter.md` → The Chronicle (60pts, 6 dimensions x 0-10)

---

## GATE-1: The Gate (Openings — 30 Points)

Score each dimension 0-5 with specific evidence from the text:

| Dimension | Question |
|-----------|----------|
| **Scene** | Does it open in a specific moment — a person, a place, a heartbeat of time? |
| **World** | Does the culture's own reality emerge naturally — without being explained? |
| **Honesty** | Free from outside judgment? No forbidden words, no anachronistic morality? |
| **Texture** | Sensory detail, material culture, landscape — can you feel where you are? |
| **Voice** | Does the prose rhythm belong to this story? Not textbook, not lecture? |
| **Pull** | Does it earn the desire to keep reading? Genuine momentum, not tricks? |

Use the scoring anchors from `scoring/RUBRIC.md` for each level.

**Pass threshold: 24+ / 30 (80%)**
Any dimension below 3/5: flag for revision.

---

## GATE-2: The Chronicle (Chapters — 60 Points)

Score each dimension 0-10 with specific evidence:

| Dimension | Question |
|-----------|----------|
| **Immersion** | Does the reader live inside this culture's world the whole chapter? |
| **Evidence** | Specific stories, named people, real events — historically grounded? |
| **Progression** | Does the era's arc emerge? Does it build, not repeat? |
| **Figures** | Are leaders and people vivid, dimensional, real? |
| **Voice** | Consistent tone throughout? No register shifts? |
| **Landing** | Does it close at the right weight? |

Use the scoring bands from `scoring/RUBRIC.md` for each range.

**Pass threshold: 48+ / 60 (80%)**
Any dimension below 7/10: flag for revision.

---

## Scoring Protocol

For each dimension:

1. **Read** the full artifact with this dimension in mind
2. **Find evidence** — quote specific passages that support the score
3. **Find counter-evidence** — quote passages that lower the score
4. **Assign score** using the rubric anchors/bands
5. **Write the evidence cell** — not a generic assessment, but specific textual evidence

Do not score generously out of respect for the effort. Do not score harshly
to seem rigorous. Score what is on the page.

---

## Innovation Check

If you notice something exceptional the rubric did not anticipate — a technique
that raises the bar in a way no dimension captures — flag it. Log to
`scoring/INNOVATIONS.md` with: source chapter, dimension, description of
the technique.

---

## Output

Write to:
- GATE-1: `reviews/GATE-1-scorecard.md`
- GATE-2: `reviews/GATE-2-scorecard.md`

Use the scoring worksheet format from `scoring/RUBRIC.md`.

Rubric reference: `scoring/RUBRIC.md`
Pipeline reference: `guides/PIPELINE.md` (Stages 2 and 8)

## Checklist

- [ ] Every dimension scored with specific textual evidence
- [ ] Rubric anchors/bands referenced for each score
- [ ] Pass/fail threshold applied (24/30 or 48/60)
- [ ] Dimensions below threshold flagged for revision
- [ ] Innovation check performed
- [ ] Scorer role maintained — scored what's on the page, not intent

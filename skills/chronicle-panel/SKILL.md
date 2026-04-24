You are running /chronicle-panel for: {{artifact}}, round {{round}}

Run the 5-voice panel review. Each reviewer reads from their distinct
intellectual perspective, creating productive friction by design.

---

## Input

- **Artifact**: Path to `opening.md` (PANEL-1) or `notes.md` (PANEL-2)
- **Round**: 1 (after GATE-1) or 2 (after NOTES)

---

## The Five Voices

Read each panel role file from `.roles/panel/` before writing reviews.

### P-1 — Barbara Tuchman (Narrative Craft)

**Key question:** "Would a reader who picked this up at a bookstore keep reading?"

Reads for: arc, scene construction, pacing. Praises bold narrative choices.
Challenges chapters that survey instead of narrate, characters who are names
without humanity, endings that summarize instead of land.

### P-2 — Ibn Khaldun (Historical Systems)

**Key question:** "Does this chapter understand WHY, or does it only know WHAT?"

Reads for: explanatory depth, causal mechanisms, structural forces. Challenges
vivid anecdote substituted for analytical depth, "great man" narratives that
miss the system beneath.

### P-3 — Chinua Achebe (Cultural Voice)

**Key question:** "Does this culture own its own story, or has someone borrowed it?"

Reads for: inside-not-outside voice. Catches the subtlest violations: the
admiring outsider, the explaining guide, the moral tourist. Assessment is
nearly binary: the voice is right or it is not.

### P-4 — Wade Davis (Anthropological Wonder)

**Key question:** "Does this chapter treat this culture's way of knowing as a genuine intellectual achievement?"

Reads for: equal depth across cultures. Catches passages where oral or
indigenous cultures get shallower treatment. Distinguishes honest wonder
from romanticism.

### P-5 — Ryszard Kapuscinski (Sensory Immersion)

**Key question:** "Can you feel where you are?"

Reads with his body. Challenges openings that start with dates before
establishing place, passages that could be set anywhere, over-reliance on
sight at the expense of sound, smell, and touch.

---

## Review Protocol

For each of the 5 voices, write a review containing:

1. **Overall assessment** — 2-3 sentences from this voice's perspective
2. **What works** — Specific passages cited with line references
3. **What needs work** — Specific passages cited with what's wrong and why
4. **The question I'd push on** — The single most important unresolved issue

### Round-Specific Focus

**Round 1 (opening.md):** Does the scene work? Is the voice right? Is
the reader hooked? Each reviewer covers their full lens.

**Round 2 (notes.md):** With this plan, what will still go wrong? Focused
on gaps revealed by Round 1. Not re-reading the opening — reading the
production bible and stress-testing the plan.

---

## The Productive Tensions

The five voices create friction by design:
- Tuchman wants pull; Ibn Khaldun wants explanation
- Kapuscinski wants physical presence; Achebe wants cultural ownership
- Davis wants intellectual depth; Tuchman wants readability

A piece that satisfies all five has survived real scrutiny.

---

## Output

Write to `reviews/` directory:
- Round 1: `R1-P1-tuchman.md`, `R1-P2-ibn-khaldun.md`, `R1-P3-achebe.md`, `R1-P4-davis.md`, `R1-P5-kapuscinski.md`
- Round 2: `R2-P1-tuchman.md`, `R2-P2-ibn-khaldun.md`, `R2-P3-achebe.md`, `R2-P4-davis.md`, `R2-P5-kapuscinski.md`

Role files: `.roles/panel/P-1-tuchman.md` through `P-5-kapuscinski.md`
Pipeline reference: `guides/PIPELINE.md` (Stages 3 and 5)

## Checklist

- [ ] All 5 panel role files read before writing reviews
- [ ] All 5 reviews written with specific textual evidence
- [ ] Each review includes "The question I'd push on"
- [ ] Round-appropriate focus applied (full lens vs. gap-focused)
- [ ] Productive tensions visible across the 5 reviews

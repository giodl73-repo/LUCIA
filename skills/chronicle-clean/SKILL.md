You are running /chronicle-clean for: {{chapter}}

Run the three-lens editorial CLEAN pass. This is not a light review — it is
a sentence-level audit that catches what the panel is not looking for.

---

## Input

- **Chapter**: Path to `chapter.md`

Prerequisite: GATE-2 passed (48+/60).

---

## The Three Editorial Lenses

Read each editorial role file from `.roles/editorial/` before running passes.

---

### E-1 — The Judgment Auditor

**Hunts:** Outside-lens violations.

Scan every sentence for:
- **Forbidden words:** primitive, advanced, tribe (unless self-designation),
  the New World, discovered by Europeans, Dark Ages
- **Forbidden framings:** "while Europe was...", "before contact with the
  West, they had already...", "remarkably sophisticated for..."
- **Anachronistic morality:** Judging past practices by modern ethical standards
- **Romanticization or demonization:** Both are forms of outside judgment
- **Surprise at sophistication:** "Remarkably," "strikingly," "what is
  surprising is..." — these reveal an assumption that less was expected
- **Authority drift:** The author stepping outside the culture to comment
  for a modern audience

For each finding: cite the line, quote the violation, explain why it
fails, suggest a fix.

---

### E-2 — The Voice Keeper

**Hunts:** Register drift.

Scan every sentence for:
- **Textbook voice:** "The economy was based on..." "They were characterized
  by..." — prose that sounds like a professor lecturing
- **Modern commentary:** "From our perspective today..." "To a modern
  reader..." — the modern observer cameo
- **Western-audience writing:** Prose that explains the culture to outsiders
  rather than presenting it from inside
- **Register shifts:** Sudden changes from narrative immersion to academic
  exposition and back
- **Hedging language:** Unnecessary qualifiers that weaken the inside voice

For each finding: cite the line, quote the drift, name what register it
shifted to, suggest a rewrite that stays in register.

---

### E-3 — The Compression Editor

**Hunts:** Re-explanation and filler.

Scan every section for:
- **Scene-then-explain:** A vivid scene followed by "This illustrates..."
  "This shows that..." "In other words..." — the scene was doing its job,
  then the writer explained it
- **Redundancy between sections:** The same point made in two different
  places with different words
- **Throat-clearing:** Introductory sentences that announce what is about
  to be said before saying it
- **Padding:** Sentences that add words without adding meaning
- **Em-dash count:** Verify 8 or fewer in the chapter

For each finding: cite the line, quote the excess, explain what it
duplicates or why it is unnecessary, recommend cut or compress.

---

## Protocol

Run all three lenses sequentially. Each lens produces its own report.
After all three are complete, produce a consolidated fix list.

For each finding across all three lenses:
- **Line number** and quoted text
- **Lens** that caught it (E-1, E-2, or E-3)
- **Category** of violation
- **Suggested fix** (specific rewrite, not generic advice)

---

## Output

Write to `reviews/` directory:
- `CLEAN-E1-judgment-auditor.md`
- `CLEAN-E2-voice-keeper.md`
- `CLEAN-E3-compression-editor.md`

Role files: `.roles/editorial/E-1-judgment-auditor.md`, `E-2-voice-keeper.md`, `E-3-compression-editor.md`
Pipeline reference: `guides/PIPELINE.md` (Stage 9)

## Checklist

- [ ] All 3 editorial role files read before running passes
- [ ] E-1: Every forbidden word/framing scanned; outside-lens violations flagged
- [ ] E-2: Every register shift identified; textbook voice flagged
- [ ] E-3: Every re-explanation flagged; em-dash count verified (8 or fewer)
- [ ] Each finding has line number, quote, category, and suggested fix
- [ ] Consolidated fix list produced

You are running /chronicle-inside-check for: {{artifact}}

Audit any chapter or opening for outside-perspective violations. This is the
Achebe Test applied systematically, sentence by sentence.

---

## Input

- **Artifact**: Path to any `opening.md` or `chapter.md`

---

## What to Scan For

### Category 1 — Forbidden Words

Scan for exact matches:
- **primitive** — places cultures on a ladder
- **advanced** — the other end of the same ladder
- **civilization** (used as compliment) — implies a membership club
- **discovered by [Europeans]** — the people there had already discovered it
- **the New World** — new to exactly one group
- **tribe** (unless self-designation) — carries connotations of smallness
- **Dark Ages** — Eurocentric label that erases the rest of the world

### Category 2 — Forbidden Framings

Scan for structural patterns:
- **"While Europe was doing X, these people were doing Y"** — implies Europe
  is the main timeline
- **"Before contact with the West, they had already..."** — the word "already"
  implies the West is the expected catalyst
- **"They were remarkably sophisticated for..."** — "remarkably" reveals
  surprise, and surprise reveals an assumption

### Category 3 — Hidden Hierarchy

Scan for subtler violations:
- Oral or indigenous cultures getting shallower treatment than literate empires
- Knowledge systems described as "beliefs" when they are empirically grounded practices
- Indigenous concepts translated into Western terms, then proceeding in those
  Western terms as if they are more real
- Pastoral, nomadic, or oral cultures treated as less sophisticated than urban or literate ones

### Category 4 — Surprise at Sophistication

Scan for:
- "Remarkably," "strikingly," "what is surprising is..."
- "They had developed..." (with an implied "even though...")
- Any phrasing that reveals the author expected less

### Category 5 — Authority Drift

Scan for the author stepping outside the worldview:
- "To a modern reader, this would seem..."
- "From our perspective today..."
- "What is interesting about this is..."
- Any sentence where the author appears as a modern person commenting
- Any sentence that explains the culture to an outside audience rather
  than presenting it from inside

### Category 6 — Textbook Voice

Scan for register lapses:
- "The economy was based on..."
- "They were characterized by..."
- "The social structure consisted of..."
- Any passage that sounds like a lecture rather than an inhabited world

---

## Report Format

For each finding:

```
LINE {{number}}: "{{quoted text}}"
CATEGORY: {{1-6}}
VIOLATION: {{specific description}}
FIX: {{suggested rewrite}}
```

Group findings by category. Count totals per category.

End with:

```
SUMMARY
Total findings: {{N}}
  Category 1 (Forbidden Words): {{n}}
  Category 2 (Forbidden Framings): {{n}}
  Category 3 (Hidden Hierarchy): {{n}}
  Category 4 (Surprise at Sophistication): {{n}}
  Category 5 (Authority Drift): {{n}}
  Category 6 (Textbook Voice): {{n}}

VERDICT: CLEAN / NEEDS-WORK ({{N}} findings)
```

---

## Output

Return the findings report directly. If run as part of a pipeline stage,
the report informs revision decisions.

Style reference: `guides/STYLE-GUIDE.md` (Forbidden Words, Forbidden Framings, The Achebe Test)

## Checklist

- [ ] Every sentence scanned across all 6 categories
- [ ] Each finding has line number, quote, category, and suggested fix
- [ ] Findings grouped by category with totals
- [ ] Summary with verdict produced

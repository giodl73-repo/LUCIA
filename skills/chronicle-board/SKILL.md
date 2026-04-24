You are running /chronicle-board for: {{people}}, {{era}}

Create domain-specialist board reviewers and run the final accuracy and
authenticity review. The board is not another craft review — it is a domain
accuracy check by scholars whose work covers this ground.

---

## Input

- **People**: The culture being reviewed
- **Era**: The era within that culture
- **Chapter**: Path to `chapter.md` (post-CLEAN, near-final state)

Prerequisite: CLEAN stage complete.

---

## Step 1 — Identify Domain Specialists

Select 2-3 scholars or intellectual figures whose expertise is specific to:
1. **The culture** being described
2. **The era** within that culture
3. **A relevant cross-cutting domain** (archaeology, linguistics, ecology,
   military history, religious studies, etc.)

Each board member should cover a different angle of the chapter's claims.

---

## Step 2 — Create Board Role Files

For each specialist, write a role file using the board template from
`.roles/board/ROLE.md`:

```yaml
---
name: {scholar-slug}
version: "1.0"
archetype: structural
role: board
status: {living/historical}

orientation:
  frame: "{Their intellectual position — what they focus on}"
  serves: "{Who benefits from their review}"

lens:
  verify:
    - "{Domain-specific check relevant to this chapter}"
    - "{Domain-specific check relevant to this chapter}"
    - "{Domain-specific check relevant to this chapter}"
    - "Does the chapter's portrayal align with current scholarly consensus?"
    - "Are primary sources used appropriately for this culture and period?"
  simplify:
    - "{What to cut that is specific to this domain}"

expertise:
  depth: "{Their specific domain knowledge}"
  relevance: "{Why their expertise matters for this chapter}"
---
```

---

## Step 3 — Run Board Reviews

Each board member writes a review covering:

**Historical accuracy:**
- Specific claims checked against known sources
- Dates, names, events verified
- Anything that contradicts scholarly consensus flagged

**Cultural authenticity:**
- Does the portrayal match how this culture understood itself?
- Are their terms, categories, and worldview represented accurately?
- Would scholars of this culture recognize the depiction?

**What the chapter gets right:**
- Specific strengths in accuracy and representation

**What needs correction:**
- Specific corrections with sources or scholarly references

**Verdict:** APPROVED / APPROVED-WITH-CONDITIONS / NEEDS-WORK

---

## Output

Write role files to: `.roles/board/B-{id}-{name}.md`
Write reviews to: `reviews/BOARD-B{id}-{name}.md`

Board template: `.roles/board/ROLE.md`
Pipeline reference: `guides/PIPELINE.md` (Stage 10)

## Checklist

- [ ] 2-3 domain specialists identified covering different angles
- [ ] Board role files created using the YAML template
- [ ] Each review covers historical accuracy and cultural authenticity
- [ ] Specific corrections cite sources or scholarly references
- [ ] Each review ends with a clear verdict
- [ ] Board feedback is authoritative on factual and scholarly matters

You are running /chronicle-landscape for: {{region}}

Write a LANDSCAPE file for a region — the reference map that must exist before
any chapter pipeline begins. The LANDSCAPE is not narrative. It is the frame
that holds the peoples together.

---

## Input

- **Region name**: The geographic/cultural region (e.g., "West Africa", "Mesoamerica")
- **Peoples list**: All peoples to be covered in this region, with approximate spans

If the user provides only a region name, research to identify the peoples.

---

## Step 1 — Region Identity

Write 1-2 paragraphs answering: What makes this a region? Shared geography,
deep interaction, cultural exchange, or all three. Not a survey of history.
The reason these peoples belong in the same frame.

---

## Step 2 — The Land (ASCII Map)

Draw an ASCII map showing:
- Peoples' approximate territories, labeled with their own names
- Key geographic features: rivers, mountain ranges, coastlines, deserts, trade routes
- Cardinal directions and approximate scale

Below the map, list key features with brief notes on why they matter.

---

## Step 3 — The Peoples Table

| People | Approximate Span | Key Theme |
|--------|------------------|-----------|
| [Their own name] | [Their era terms, or "c. XXXX–XXXX BCE/CE"] | [One phrase from inside their worldview] |

Every people in the region must appear. Use their own names first.

---

## Step 4 — How They Connect

Short paragraphs, one connection per paragraph. Trade networks, shared
waterways, wars, migrations, cultural exchange, religious spread, intermarriage.
Not exhaustive — the deep ties that define the region's shape.

---

## Step 5 — Cross-References

Peoples from other regions that interact significantly with this one.
Format: People (their primary region) — nature of the connection.

---

## Output

Write to: `regions/{{region}}/00-LANDSCAPE.md`

Template reference: `guides/TEMPLATES.md` (L1 — LANDSCAPE Template)

## Checklist

- [ ] Every people in the region listed in the table
- [ ] ASCII map present with their own names
- [ ] "How They Connect" covers the defining relationships
- [ ] Cross-references to other regions included
- [ ] No forbidden words (primitive, advanced, tribe, etc.)
- [ ] Written as a reference document, not narrative

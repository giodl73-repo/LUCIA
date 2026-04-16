You are running /chronicle-overview for: {{people}} in {{region}}

Write an OVERVIEW file for a people — their story, in their own terms, from
inside their worldview. A member of this culture should be able to read this
and recognize their own world.

---

## Input

- **People name**: Their own name for themselves
- **Region**: The region this people belongs to

Prerequisite: `regions/{{region}}/00-LANDSCAPE.md` must exist.

---

## Step 1 — Research the Culture

Before writing, understand:
- What they called themselves and why
- Their own time markers and periodization
- Their central concerns, categories, and terms
- Their geography as they understood it
- What mattered to them — not what outsiders found interesting

Consult primary sources first, academic sources second.

---

## Step 2 — Introduction (1-2 paragraphs)

Write as if the culture is introducing itself. Not "the X people were an
ancient civilization in..." — who they were, in their own terms. What
mattered to them. How they understood their place in the world.

Apply the Achebe Test: Could a thoughtful member of this culture read this
and feel their story was told with dignity, from inside?

---

## Step 3 — Their World (ASCII Map)

Draw their territory, sphere of influence, key places at their peak or most
coherent moment. Label in their language first, common names in parentheses
if needed. Show neighboring peoples they knew and named.

---

## Step 4 — Their Time (Era Table)

| Era | Their Name | Common Era | Key Theme |
|-----|-----------|------------|-----------|
| [Number] | [Their term for this period] | [c. XXXX BCE/CE – XXXX BCE/CE] | [What defined this era in their own terms] |

Use THEIR periodization. Not Western academic period labels. Their calendar
leads; common-era dates orient.

---

## Step 5 — What Defined Them

3-5 themes, each in a short paragraph. Written from inside the culture.
Not "achievements" for a Western audience. Not "they were known for X."
What was central to how they understood themselves, organized their world,
and made decisions. Use their terms.

---

## Step 6 — The Chapters

List era chapters with one-line hooks — written as invitations to read,
not summaries. Each hook should make the reader want to open that chapter.

---

## Output

Write to:
- `regions/{{region}}/{{people}}/00-OVERVIEW.md`
- `regions/{{region}}/{{people}}/SOURCES.md` (seed with sources used)

Template reference: `guides/TEMPLATES.md` (L2 — OVERVIEW Template)
Style reference: `guides/STYLE-GUIDE.md`

## Checklist

- [ ] Written from inside the culture's worldview
- [ ] Their own name used throughout
- [ ] Era table uses their periodization, not Western labels
- [ ] ASCII map labels in their language first
- [ ] Themes written from inside, not as outsider observations
- [ ] Chapter hooks are invitations, not summaries
- [ ] No forbidden words or framings
- [ ] Passes the Achebe Test

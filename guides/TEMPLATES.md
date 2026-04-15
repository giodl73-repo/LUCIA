# LUCIA Templates

Document templates for every level of The Human Chronicle.

These are the standard forms. Use them. Deviate only when the culture
demands it — and when you deviate, note why.

---

## L1 — LANDSCAPE Template

**File:** `regions/<region>/00-LANDSCAPE.md`

The LANDSCAPE is a reference document, not narrative. It answers: what
is this region, who lived in it, and how did they connect? It is the map
you hang before writing any chapter.

### Skeleton

```markdown
# [Region Name]

[1-2 paragraphs: What makes this a region — shared geography, deep
interaction, cultural exchange, or all three. Not a survey of history.
The reason these peoples belong in the same frame.]

## The Land

[ASCII map showing peoples' approximate territories and key geographic
features — rivers, mountain ranges, coastlines, deserts, trade routes.
Label peoples with their own names. Use cardinal directions. Include scale
note if useful.]

## The Peoples

| People | Approximate Span | Key Theme |
|--------|------------------|-----------|
| [Their own name] | [Their era terms, or "c. XXXX–XXXX BCE/CE"] | [One phrase from inside their worldview — not an academic descriptor] |

## How They Connect

[Interactions between peoples in this region: trade networks, shared
waterways, wars, migrations, cultural exchange, religious spread,
intermarriage. Write in short paragraphs, one connection per paragraph.
Not exhaustive — the deep ties that define the region's shape.]

## Cross-References

[Peoples from other regions that interact significantly with this one.
Format: People (their primary region) — nature of the connection.]
```

---

### Filled-In Example: The Rivered Plains

*Fictional region — for illustration only.*

---

# The Rivered Plains

Two rivers define this world. The Arath rises in the Thornmount range
and runs west to the Inland Sea, carrying snowmelt and the seeds of the
highland forests down to the flood plain below. The Kesh flows north from
the Salt Marshes, slower and warmer, carrying the sediment that built the
black soil delta where the Sudeen have farmed without interruption for
four thousand years. Between and around these rivers, a dozen peoples
organized their lives according to the same fundamental logic: the water
comes, the water goes, and you live by reading which.

The region's unity is not political — it has never been ruled as a whole —
but hydraulic. Every people here knows the flood calendar. Every
marketplace sits at a river junction. The roads are the rivers. What makes
the Rivered Plains a coherent region is that no people in it can ignore
what the others do upstream.

## The Land

```
         THORNMOUNT RANGE
         ~~~~~~~~~~~~~~~~
              |
    [KETH] ~~~+~~~ [ARATH RIVER] ~~~~~~~~~~~►  Inland
       |      |                               Sea
       |   [SUDEEN DELTA]
       |      |
  [MARSH]  [LOWER PLAIN]
  [PEOPLE]  [VERAK]
       |
    Salt
   Marshes

    N
    ↑
W ←─+─→ E       ≈ 400 km across
    ↓
    S
```

Key features:
- Thornmount Pass: only reliable land route to the Northern Hills peoples
- Sudeen Delta: most productive farmland in the region
- Salt Marshes: source of preserved fish that underlies Marsh People trade
- Inland Sea: eastern border; Arath mouth is a major port zone

## The Peoples

| People | Approximate Span | Key Theme |
|--------|------------------|-----------|
| Sudeen | "Since the Black Soil Was Given" — c. 3200 BCE–present | The covenant with the river; communal flood labor |
| Verak | "The Six Generations Before the Walled Time" through present — c. 1800–200 BCE | Cavalry raiding and the horse-river balance |
| Keth | "Keth-Before-Salt" and "Keth-After-Salt" — c. 2400–600 BCE | Salt trade and the power of preservation |
| Marsh People | No written record; oral tradition places them "from the beginning" | Ecological intimacy; reading the marsh as calendar |
| Thornmount Clans | "The Cold Generations" — c. 1500 BCE–500 CE | Highland pastoralism and seasonal descent to plain |

## How They Connect

The Arath River is the Sudeen's artery and the Verak's raiding route. In
the dry season, when the river drops, Verak horse-riders crossed the
shallow fords into the Sudeen delta, sometimes trading, sometimes not. The
Sudeen built watchtowers at every ford. The Verak built granaries near
every ford. The relationship was never resolved into pure war or pure peace
— it held in a permanent productive tension for a thousand years.

The Keth and the Marsh People traded in opposite directions. Keth salt
traveled downriver into the delta and up toward the Thornmount passes.
Marsh People smoked fish traveled the same route in the other direction.
Neither people could sustain their population without the other's
preservation technology. They met at the junction market that is now
called Kesh-Point; the Keth called it the Place of Two Smells.

The Thornmount Clans descended to the plain every winter, bringing wool
and highland metals, and returned in spring. They are the vector through
which Rivered Plains grain reached the Northern Hills peoples — a trade
dependency that gave Thornmount clan leaders unusual leverage in both
directions.

## Cross-References

- Northern Hills Peoples (Northern Uplands region) — receive Rivered Plains grain via Thornmount Clans; in turn provide copper and tin
- Inland Sea Maritime Peoples (Sea Region) — control the Arath River mouth; taxed all Rivered Plains export trade for four centuries
- Steppe Riders (Eastern Grasslands) — precursors to the Verak; periodic westward pressure throughout the record

---

## L2 — OVERVIEW Template

**File:** `regions/<region>/<people>/00-OVERVIEW.md`

The OVERVIEW is not a survey written about a people. It is written from
inside — their categories, their time markers, their sense of themselves.
A member of this culture should be able to read this and recognize
their own world.

### Skeleton

```markdown
# [People's own name for themselves]

[1-2 paragraphs: Who they were, in their own terms. Not "the X people
were an ancient civilization in..." — write as if the culture is
introducing itself. What mattered to them. How they understood their
place in the world. What they called themselves and why.]

## Their World

[ASCII map or diagram of territory, sphere of influence, key places —
at the people's own peak or most coherent moment. Label in their
language first, common names in parentheses if needed. Show
neighboring peoples they knew and named.]

## Their Time

| Era | Their Name | Common Era | Key Theme |
|-----|-----------|------------|-----------|
| [Number] | [Their term for this period] | [c. XXXX BCE/CE – XXXX BCE/CE] | [What defined this era in their own terms — not an academic descriptor] |

## What Defined Them

[3-5 themes, each in a short paragraph. Written from inside the culture.
Not "achievements" for a Western audience. Not "they were known for X."
What was central to how they understood themselves, organized their
world, and made decisions. Use their terms.]

## The Chapters

[List of era chapters with one-line hooks — written as invitations to
read, not summaries. Each hook should make the reader want to open
that chapter.]
```

---

### Filled-In Example: The Sudeen

*Fictional people — for illustration only.*

---

# Sudeen — "The People the River Chose"

The river did not simply flow through Sudeen country. The river was the
country — the source of the black soil, the keeper of the flood calendar,
the force that decided who ate and who did not. The Sudeen did not
conquer the delta; the delta made them. Their word for "community" and
their word for "irrigation labor" were the same word. You were Sudeen
if you worked the channels; if you stopped working the channels, you
were something else.

They called themselves the Sudeen — "those who were given the soil" — in
their founding myth, the god of the deep river had lifted the black earth
from the river's bed and spread it across the plain as a gift, not to
any one family, but to anyone willing to stay and tend it. This was why
individual ownership of the delta farmland was inconceivable in classical
Sudeen thought. The soil was on loan. The obligation was collective.

## Their World

```
                    [THORNMOUNT CLANS]
                    (trade partners — wool, metals)
                           ↓
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~  ARATH RIVER            ~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           ↓
    [VERAK]  ──────  [SUDEEN DELTA]  ──────  Inland Sea
   (raid/trade)      Main cities:           (port trade)
                     Sudeh-Prime
                     Lower Sudeh
                     Kesh-Mouth
                           ↓
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              ~  KESH CONFLUENCE        ~
              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                           ↓
                    [KETH TERRITORY]
                    (salt trade — essential)
```

Major places (Sudeen names):
- **Sudeh-Prime** ("the First Place") — ceremonial capital; flood temple
- **Lower Sudeh** ("the Working City") — largest population; market center
- **Kesh-Mouth** ("Where Both Rivers Speak") — junction port; grain export

## Their Time

| Era | Their Name | Common Era | Key Theme |
|-----|-----------|------------|-----------|
| 1 | The Given Time | c. 3200–2600 BCE | Founding of the canal system; emergence of the flood covenant |
| 2 | The Walled Time | c. 2600–1900 BCE | City walls and the rise of the temple administrators; first written flood records |
| 3 | The Verak Centuries | c. 1900–1200 BCE | Coexistence and conflict with Verak riders; wall expansions; cavalry tribute arrangements |
| 4 | The Salt Years | c. 1200–700 BCE | Keth salt trade dominance; Sudeen economic restructuring; decline of temple authority |
| 5 | The Quiet Delta | c. 700–200 BCE | Inland Sea maritime control of Arath mouth; political fragmentation; cultural florescence |

## What Defined Them

**The flood covenant.** Every year, in the season they called the Wakening,
the Arath rose. Every adult in the delta was required to work the channels
for seven days before their own planting — clearing sediment, repairing
walls, opening new branches. Not as taxation. Not as corvée labor. As an
obligation to the soil itself. A household that did not appear for channel
work did not receive water in the dry season. The system was self-enforcing
because it had to be.

**The deep calendar.** Sudeen timekeeping was agricultural and astronomical
simultaneously. They tracked four celestial bodies — the sun, the river
star (what we call Sirius), the dry moon, and the wandering star (Venus)
— because the alignment of these bodies with the river's behavior told
them when to plant, when to harvest, and when the flood would peak. Their
astronomers were also their flood engineers. Their priests were also their
hydrologists.

**The commons of the black soil.** No Sudeen household owned farmland
outright. Land was allocated by the temple administrators each season
based on household size and labor contribution to the channels. A family
that worked hard and grew could hold more land. A family that shrank or
declined could lose allocation. This was not perceived as injustice —
it was perceived as the natural logic of a gift that must be shared. The
Sudeen had no word for the concept of private land title.

**The hospitality obligation.** A stranger who reached any Sudeen household
at nightfall was entitled to shelter and food for three days, no questions
asked. This was not charity — it was the law. The practical reason was
flood refugees: the delta had witnessed catastrophic floods that destroyed
entire villages, and a people who sheltered strangers today would be
sheltered by strangers tomorrow. The cultural residue of this law outlasted
the floods that created it by a thousand years.

**River speech.** The Sudeen distinguished between eight types of water
movement in the Arath, each with its own name, each carrying specific
implications for channel behavior. Where outside observers saw "the river,"
Sudeen engineers saw eight distinct phenomena. This vocabulary precision
was not aesthetic — it was technical. The engineers who could not name
what they were watching could not predict what would happen next.

## The Chapters

**1 — The Given Time:** Before the walls, before the writing — a woman
named Sudeh stands in the first completed channel and watches the water
find its own level. The delta is being made.

**2 — The Walled Time:** The flood temple rises and the administrators
begin keeping records. For the first time, the river's behavior has
witnesses who can be held accountable when they are wrong.

**3 — The Verak Centuries:** Verak riders at the ford, a Sudeen watchtower
captain deciding whether today is trade or war — and the thousand years
of productive unresolution that decision captures.

**4 — The Salt Years:** A Sudeen merchant in Lower Sudeh discovers that
Keth salt can preserve grain through the dry season. The temple
administrators begin to understand that the river gave them soil, but
the Keth gave them time.

**5 — The Quiet Delta:** The Inland Sea merchants control the Arath mouth.
The city of Kesh-Mouth pays tribute to a people none of its residents
have ever seen. A Sudeen poet writes: "Even the river bows to those
who hold the sea."

---

## L4 — Chapter File Templates

These are the four files that every era produces.

---

### `opening.md` — The Hook Scene (~800 words)

```markdown
# [People Name] — [Era Name] — Opening

[The scene. One person. One place. One moment. The reader is there.
No context-setting paragraph. No "In the year X, the Y people were..."
Start with the body in the place.]

[Continue the scene. Something is at stake. The world's logic emerges
from what the character does and sees and knows — not from authorial
explanation. By the end of ~800 words, the reader understands this
world enough to want to know what happens next.]

[The pull at the end. Not a cliffhanger trick. A genuine reason to
keep reading — a question opened, a tension established, a door ajar.]
```

**Checklist before submitting for GATE-1:**
- [ ] Opens with a specific person in a specific place
- [ ] No context paragraph before the scene
- [ ] Culture's own reality emerges from narrative, not explanation
- [ ] At least one strong sensory anchor per 200 words
- [ ] No forbidden words (primitive, advanced, tribe, etc.)
- [ ] No forbidden framings (while Europe was..., remarkably sophisticated for...)
- [ ] ~800 words
- [ ] ≤5 em-dashes

---

### `chapter.md` — The Full Narrative (~5000 words)

```markdown
# [People Name] — [Era Name]

## [Section 1 — Opening scene, ~800 words]

[The opening from opening.md, integrated here as the first section.
The chapter begins in scene, not in context.]

## [Section 2 — Development, ~600-800 words]

[The world widens from the opening scene. A second human perspective,
or the opening character moving through the era's central forces.
Causal depth begins to emerge — not explained but demonstrated.]

## [Section 3 — Development, ~600-800 words]

[A third dimension of the era. The arc is building. Each section earns
its place by advancing the reader's understanding — not just adding
more information, but changing what the information means.]

## [Section 4 — Deepening, ~600-800 words]

[The era's central tension or transformation. The forces that have been
building arrive at something — a peak, a turn, a crisis. Not necessarily
a dramatic event; sometimes a deepening of understanding.]

## [Section 5 — Deepening, ~600-800 words]

[The human cost or human texture of the era's defining forces. The
people who lived this — not as representatives of the system but as
individuals navigating it. Figures from figures.md appear here in
their fullest form.]

## [Section 6 — Landing, ~600 words]

[The close. Not a summary. Not "and so this era ended with..." The
chapter lands at a specific moment, image, or voice that carries the
weight of what came before. The reader sits with it.]
```

**Target word counts:**
- Opening section: ~800 words
- Middle development sections (2-3): ~600-800 words each
- Deepening sections (4-5): ~600-800 words each
- Landing section: ~600 words
- **Total: 4,500–5,500 words**
- **Em-dashes: ≤8**

---

### `notes.md` — The Production Bible

```markdown
# [People Name] — [Era Name] — Production Notes

## Sources

### Primary
- [Author/text, date, what it contributes to this chapter]

### Academic
- [Author, title, date, publisher, what it contributes]

### Needed (ACQUISITION)
- [What sources would strengthen this chapter that are not yet in hand]

## Key Figures

| Name | Their Role | Why They Matter to This Era |
|------|-----------|----------------------------|
| [Name in their language] | [Title/role in their terms] | [Why this person carries part of the era's story] |

## Narrative Arc

[2-3 paragraphs: What is the story of this era? What changes? What is
the central tension? How does it resolve, or how does it not resolve?
This is the spine the chapter hangs on.]

## Section Plan

| Section | Content | Word Target | Key Source | Panel Risk |
|---------|---------|-------------|------------|------------|
| 1 — Opening | [Scene description] | ~800w | [Source] | [Which panel voice will push here?] |
| 2 | [Content] | ~700w | [Source] | [Panel risk] |
| 3 | [Content] | ~700w | [Source] | [Panel risk] |
| 4 | [Content] | ~700w | [Source] | [Panel risk] |
| 5 | [Content] | ~700w | [Source] | [Panel risk] |
| 6 — Landing | [Close description] | ~600w | [Source] | [Panel risk] |

## Panel Pressure Points

**Tuchman (craft):** [What she will likely push on — pacing risks, arc
weaknesses, chronological plodding risks]

**Ibn Khaldun (systems):** [What he will push on — where causal depth
is thin, where the chapter describes without explaining]

**Achebe (voice):** [Where the inside-not-outside rule is most at risk —
practices that might invite outsider framing, moments where authorial
position could show]

**Davis (wonder):** [Any hidden hierarchy risks — places where this
culture's knowledge system might get shallower treatment than warranted]

**Kapuściński (immersion):** [Where sensory grounding is thin — abstract
sections that need physical anchoring]

## Open Questions

[Things the research hasn't resolved — chronological uncertainties,
disputed interpretations, gaps in the record that the chapter needs to
handle honestly per Principle 13 (Honest Uncertainty)]
```

---

### `figures.md` — Key Leaders and People of This Era

```markdown
# [People Name] — [Era Name] — Figures

[Brief introduction: who is covered here and why. 1-2 sentences.
Not a list of "important people" — the human beings through whom this
era's story runs.]

---

## [Name in Their Language]

**[Their title or role in their own terms]** — [approximate dates if known]

[2-4 paragraphs: Who this person was, written from inside the worldview.
Not a biography. Not "X was born in... X achieved..." — the person as
they were understood within their own world. What they did, why it
mattered, how contemporaries understood them.

A dimension of character: not an archetype (the wise king, the ruthless
general) but a human being with a specific presence. What did they
actually do? What decisions did they face? What did they know and not know?

If the record is thin, say so. "What we know of X comes from..." is more
compelling than invented certainty.]

---

## [Name in Their Language]

[Continue the pattern for each figure. 2-5 figures per era is typical.
More than 5 risks becoming a list; fewer than 2 risks leaving the era
without human faces.]
```

---

## Quick Reference: Artifact Checklist

| Stage | Artifact | Location | Key Constraint |
|-------|----------|----------|----------------|
| L1 | `00-LANDSCAPE.md` | `regions/<region>/` | ASCII map required; all peoples listed |
| L2 | `00-OVERVIEW.md` | `regions/<region>/<people>/` | Inside voice; their era names; their terms |
| 1 | `opening.md` | `regions/.../eras/<era>/` | ~800w; person + place + moment |
| 4 | `notes.md` | `regions/.../eras/<era>/` | 6 sections; section plan with panel risks |
| 7a | `chapter.md` | `regions/.../eras/<era>/` | 4,500–5,500w; ≤8 em-dashes |
| 7b | `figures.md` | `regions/.../eras/<era>/` | 500–1,500w; inside voice |

---

## See Also

- `guides/PIPELINE.md` — When each artifact is produced and reviewed
- `guides/HOW-TO-WRITE-A-CHAPTER.md` — End-to-end author walkthrough
- `guides/STYLE-GUIDE.md` — 13 principles + forbidden words + mechanical rules

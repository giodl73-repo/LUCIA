# Board Reviewers

Culture-specific domain experts assembled for Stage 10 (BOARD). Unlike the
panel (permanent, craft-focused) and editorial (permanent, compliance-focused),
board reviewers are selected per chapter based on the specific culture and
era under review.

## How Board Reviewers Are Selected

For each chapter reaching Stage 10, identify 2-3 scholars or intellectual
figures whose expertise is specific to:
1. The culture being described
2. The era within that culture
3. A relevant cross-cutting domain (archaeology, linguistics, ecology, military history)

## Board Review Output Format

```markdown
## B-{id} — {Name} — Board Review of {chapter}

**Expertise relevant to this chapter:** {1-2 sentences}

**Historical accuracy:**
- {Specific findings — correct, questionable, or wrong}

**Cultural authenticity:**
- {Does this match the scholarly consensus on how this culture understood itself?}

**What the chapter gets right:**
- {Specific praise}

**What needs correction:**
- {Specific corrections with sources}

**Verdict:** APPROVED / APPROVED-WITH-CONDITIONS / NEEDS-WORK
```

## Growing the Roster

Board reviewers accumulate as regions are built. Each new culture may
introduce new board members. Track them here as they are created:

| ID | Name | Expertise | Regions Served |
|----|------|-----------|---------------|
| B-1 | Mark Edward Lewis | Tang political institutions, An Lushan rebellion | 17-east-asia |
| B-2 | Stephen Owen | Tang poetry, keju literary culture, Du Fu/Li Bai | 17-east-asia |
| B-3 | Valerie Hansen | Silk Road trade, Sogdian communities, foreign religions | 17-east-asia |
| B-tongan-1 | Patrick Kirch | Polynesian archaeology, chiefly systems, Tongan prehistory | 22-oceania-pacific |
| B-tongan-2 | David Lewis | Traditional Pacific navigation, swell-reading, star paths | 22-oceania-pacific |
| B-tongan-3 | Epeli Hau'ofa | Pacific identity, Tongan-Fijian worldview, ocean-as-world | 22-oceania-pacific |
| B-egypt-1 | Mark Lehner | Giza plateau excavation, workers' village, pyramid construction logistics | 09-egypt-nile |
| B-egypt-2 | James P. Allen | Pyramid Texts, Old Kingdom theology, solar religion, ma'at | 09-egypt-nile |
| B-egypt-3 | Barry Kemp | Old Kingdom social structure, provincial administration, centralization/fragmentation | 09-egypt-nile |
| B-abbasid-1 | Dimitri Gutas | Graeco-Arabic translation movement, Bayt al-Hikma, Abbasid patronage politics | 08-islamic-heartlands |
| B-abbasid-2 | George Saliba | Islamic science, Arabic astronomy, critique of the "preservation" narrative | 08-islamic-heartlands |
| B-abbasid-3 | Hugh Kennedy | Early Abbasid political history, founding of Baghdad, caliphal court | 08-islamic-heartlands |
| B-maya-1 | David Stuart (model) | Maya epigraphy, Long Count calendar, Classic political history | 01-mesoamerica |
| B-maya-2 | Michael Coe (model) | Mesoamerican archaeology, Maya sites, material culture | 01-mesoamerica |
| B-maya-3 | Evon Vogt (model) | Maya ethnography, living communities, calendar continuity | 01-mesoamerica |
| B-norse-1 | Neil Price | Viking-age archaeology, social structure, belief systems | 21-northern-eastern-europe |
| B-norse-2 | Judith Jesch | Old Norse language, runic inscriptions, skaldic poetry, maritime culture | 21-northern-eastern-europe |
| B-norse-3 | Soren Sindbak | Viking-age trade networks, Scandinavian trading settlements | 21-northern-eastern-europe |
| B-soninke-1 | Nehemia Levtzion | Arabic geographical sources, political/economic reconstruction of western Sudan | 10-west-african-sahel-and-savanna |
| B-soninke-2 | David Conrad | Mande oral traditions, the Dausi, Almoravid-Ghana historiography | 10-west-african-sahel-and-savanna |
| B-soninke-3 | Susan Keech McIntosh | Archaeology of the western Sahel, Kumbi Saleh, trans-Saharan trade material culture | 10-west-african-sahel-and-savanna |
| B-maurya-1 | Romila Thapar | Ashokan political history, edict interpretation, Maurya chronology, dhamma as political concept | 15-south-asia |
| B-maurya-2 | Patrick Olivelle | Arthashastra (critical edition), Ashokan political philosophy, dhamma as governance | 15-south-asia |
| B-maurya-3 | Harry Falk | Ashokan epigraphy, Indian palaeography, inscription site archaeology | 15-south-asia |
| B-fulani-1 | Murray Last | Sokoto Caliphate political/administrative history, emirate system, flag-holders | 10-west-african-sahel-and-savanna |
| B-fulani-2 | Mervyn Hiskett | Dan Fodio biography, Torodbe scholarly tradition, pre-jihad Gobir | 10-west-african-sahel-and-savanna |
| B-fulani-3 | Beverly Mack | Nana Asma'u, yan taru system, women's education in Sokoto Caliphate | 10-west-african-sahel-and-savanna |
| B-babylon-1 | Dominique Charpin | Old Babylonian political history, Hammurabi biography, Mari archive, royal correspondence | 06-fertile-crescent |
| B-babylon-2 | W. G. Lambert | Babylonian creation myths, Enuma Elish, divine assembly, Babylonian theology | 06-fertile-crescent |
| B-babylon-3 | Raymond Westbrook | Ancient Near Eastern law, the code's function debate, comparative legal history | 06-fertile-crescent |
| B-lunda-1 | Jan Vansina | Lunda oral tradition reconstruction, methodology for oral tradition as historical evidence | 12-central-africa |
| B-lunda-2 | Robert Schecter | Lunda expansion mechanics, titled-subordinate system, daughter-state connections to the center | 12-central-africa |
| B-lunda-3 | James Pritchett | Lunda-Ndembu ethnography, Lunda ceremonial practice, cultural authenticity in living communities | 12-central-africa |

## Board Role Template

Use this YAML structure to create new board reviewers:

```yaml
---
name: {scholar-slug}
version: "1.0"
archetype: structural
role: board
status: {living/historical}

orientation:
  frame: "{First-person description of their intellectual position}"
  serves: "{Who benefits from their review and how}"

lens:
  verify:
    - "{Domain-specific verification check}"
    - "{Domain-specific verification check}"
    - "{Domain-specific verification check}"
    - "Does the chapter's portrayal align with current scholarly consensus?"
    - "Are primary sources used appropriately for this culture and period?"
  simplify:
    - "{What to cut that is specific to this domain}"

expertise:
  depth: "{Their specific domain knowledge}"
  relevance: "{Why their expertise matters for this specific chapter}"

scope: local
collaborates_with: []

artifacts:
  - type: review
    directory: reviews/
    format: markdown
    naming: "BOARD-B{id}-{name}-{chapter}.md"

workflow:
  - step: read
    description: "Read for historical accuracy and cultural authenticity in your domain."
  - step: verify
    description: "Check claims against known sources. Flag anything that contradicts scholarly consensus."
  - step: write
    description: "Write review focusing on accuracy and authenticity. Be specific about corrections."
---
```

## Example: First Board Reviewer (created with anchor chapter)

When the anchor region is chosen and the first chapter reaches Stage 10,
the first 2-3 board reviewers will be created specific to that culture.
For example, if the anchor is the Maya Classic period:

- **B-1**: A Mayanist epigrapher (e.g., modeled on David Stuart — decipherment, inscriptions)
- **B-2**: A Mesoamerican archaeologist (e.g., modeled on Michael Coe — material culture, sites)
- **B-3**: A Maya ethnographer (e.g., modeled on Evon Vogt — living Maya worldview continuity)

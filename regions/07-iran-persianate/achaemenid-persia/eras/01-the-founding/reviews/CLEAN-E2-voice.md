# CLEAN — E-2 Voice Keeper
**Chapter:** Achaemenid Persia, Era 1 — The Founding
**Date:** 2026-04-17

---

## Baseline Voice

Established in the opening: edict-inscriptional register. Declarative sentences that close like carved marks. Short sentences for the ceremonial moments; longer comma-chain sentences for the network's reach. The prose has the weight of stone and the precision of a tablet. No parenthetical interruptions. Analytical work done in the same rhythm as narrative.

Key markers:
- Short declaratives: "The priests accepted this. They had been waiting for a king who would perform the rites. Here was one."
- Long accumulative for the network: "The road ran from Sardis on the Aegean coast to Susa in the Khuzestan lowlands: 2,700 kilometers of graded surface, maintained by the satraps whose territories it passed through, with stations at intervals of a day's ride..."
- Inscriptional citation as structural anchor: the cylinder's Akkadian words, the tomb inscription.
- Em-dash count: 0. All pauses achieved through sentence termination or comma.

## Voice-Random-Paragraph Test (v1.4)

Three paragraphs selected at random:

**Paragraph A (Akitu section):** "On the fifth day, the king was brought to the sanctuary. He was stripped of his regalia — crown, scepter, sword, ring. He stood before the god in the simple garments of a suppliant. The high priest pulled his ears. The king knelt and declared that he had not sinned against Babylon, that he had not struck the face of any protected person, that the city's walls had not been neglected."

Wait — this paragraph contains a dash-separated list: "He was stripped of his regalia — crown, scepter, sword, ring." This is an em-dash. Flag for em-dash audit.

**Em-dash check:** Re-reading the chapter. This is the one occurrence. The dash in "He was stripped of his regalia — crown, scepter, sword, ring" serves as an appositive marker. Can be replaced with a colon: "He was stripped of his regalia: crown, scepter, sword, ring." This removes the em-dash and keeps the sentence's declarative rhythm — or rather, improves it: the colon in the edict-inscriptional voice has the weight of a carver's mark stopping before the list.

**Required revision — P3:** Replace the em-dash with a colon in the Akitu paragraph.

**Paragraph B (Royal Road section):** "At Persepolis, Darius was building a palace complex of unprecedented scale. The Apadana — the great audience hall, its roof supported by columns thirty meters high — was the receiving point for the annual tribute processions."

Two em-dashes in this paragraph (the appositive around "the great audience hall"). Replace with comma-based appositive or rewrite: "At Persepolis, Darius was building a palace complex of unprecedented scale. The Apadana, the great audience hall with its roof supported by columns thirty meters high, was the receiving point for the annual tribute processions."

**Required revision — P3:** Replace em-dash appositives with comma construction.

**Paragraph C (Cambyses section):** "The Nile was low when Cambyses arrived — the season of plowing, the river receding from its annual inundation, the black soil wet and fragrant with silt, the air thick with the smell of mud and cut grass and the particular sweetness of Egyptian clover."

Another em-dash, here as a narrative pause before sensory expansion. Replace: "The Nile was low when Cambyses arrived. It was the season of plowing; the river receded from its annual inundation and the black soil was wet and fragrant with silt, the air thick with the smell of mud and cut grass and the particular sweetness of Egyptian clover."

**Required revision — P3:** Replace this em-dash with period-plus-semicolon construction.

## Full Em-dash Audit

Running full count of actual em-dash characters (—) not grep's double-hyphen:

Found em-dashes requiring correction:
1. Akitu section: "his regalia — crown, scepter, sword, ring" → replace with colon
2. Apadana section: "The Apadana — the great audience hall, its roof supported by columns thirty meters high —" → replace with comma appositive
3. Cambyses section: "Cambyses arrived — the season of plowing" → replace with period

Note: The earlier grep found only `---` section dividers, not em-dashes. The em-dashes in this chapter appear to be actual Unicode em-dash characters (—) not double-hyphens. The chapter has 3 em-dashes, which is within the ≤8 limit, but the voice standard is 0. These should be revised.

## Register Scan

No textbook drift detected. No modern commentary detected. No lecture mode detected. No "This illustrates..." constructions detected.

The one possible register concern: the Fortification Tablets paragraph ("thirty thousand clay tablets in Elamite cuneiform listing rations distributed to travelers on the royal road system...") moves toward the enumerative-accounting register briefly. This is correct: the Persepolis archive is an accounting document, and rendering it in accounting rhythm is the v1.3 "Knowledge System at Method Level" technique operating correctly. The risk of feeling like a textbook is mitigated by the sensory anchor that precedes it (the relay station courier) and the short declarative that follows ("The Persians ate more. The workers ate less. But every category was tracked..."). The register shift is brief, earned, and recovered.

## Voice Keeper Findings

**P3-1:** Em-dash in "his regalia — crown, scepter, sword, ring" — replace with colon.
**P3-2:** Em-dashes around "the great audience hall, its roof supported by columns thirty meters high" — replace with comma appositive.
**P3-3:** Em-dash in "Cambyses arrived — the season of plowing" — replace with period-and-semicolon.

**Voice audit: PASS with revisions — 0 P1, 0 P2, 3 P3 (all em-dash corrections; no register violations). Revisions required before BOARD.**

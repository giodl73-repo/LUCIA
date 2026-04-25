# Manuscript Architecture — Design Proposal

**Status:** Draft v0.1 (Session 3, 2026-04-20)
**Author:** LUCY
**Scope:** How 115 chapters become a book (or a set of books, or a navigable reference)

---

## The Question

LUCIA has 115 locked chapters, approximately 680,000 words. It is not yet a manuscript in the sense a reader can pick up. The chapters are organized by the 5-level tree (Region → People → Era → Chapter files → Reviews) which is the **production** structure. Production structure is not **reading** structure. A reader picking up LUCIA needs an entry point, a sequence, and a scale — none of which the production tree supplies.

This document proposes a manuscript architecture. It is a proposal, not a decision. The tradeoffs are laid out; the recommended path is stated; the alternatives are preserved for reconsideration.

---

## The Five Design Axes

Every architectural decision for LUCIA sits on one of five axes.

### Axis 1. Sequencing

How are the 115 chapters ordered?

**Option A — Regional sequence.** Follow the 26 regions in the CLAUDE.md ordering: Mesoamerica, Andes, Amazonia, North America, Mediterranean, Fertile Crescent, Iran, Islamic Heartlands, Egypt, West Africa Sahel, West Africa Forest, Central Africa, East Africa, Southern Africa, South Asia, Tibet, East Asia, Southeast Asia, Central Asia, Western Christendom, Northern Europe, Oceania, Americas Reborn, Colonial Empires, Diasporas, Pacific Century. Within each region, peoples ordered by the region's own LANDSCAPE.md; within each people, eras chronological. This is the default reading of the production tree.

**Option B — Thematic sequence.** Group chapters by structural pattern rather than geography. All Covenant-engine chapters together (Mali, Haudenosaunee, Rome-era-1); all Material-Object-engine chapters together (Kanem-Bornu, Norse, Maurya, Benin, Sumer, Urartu); all Contradiction-Held-as-Engine chapters together (British, Spanish, French, Dutch, Portuguese empires). This foregrounds the Track B typology as reading structure.

**Option C — Chronological overlay.** Follow a single global timeline, interleaving cultures by era-start. The reader moves forward in time through all cultures simultaneously. This is the "world history" reading. It is the structure most commonly used by world-history textbooks and the structure LUCIA has explicitly rejected at the rubric level (periodization belongs to each culture).

**Option D — Resonance sequence.** Order chapters by inter-chapter resonances: Mali → Fulani (shared Sahelian scholarly lineage) → Haiti (Vodou-Middle-Passage-Mali echo); Inca → Peru Conquista (substrate continuity under Spanish overlay); Rome → Capetian France (legal-public voice register inheritance). This is a curator's reading — LUCY's own walking-through-the-house order.

**Recommendation: Option A (Regional) as default, with Option D (Resonance) as curated alternate path.** Regional is legible to any reader at any entry point. Resonance is legible to a reader who has read enough to see the connections LUCY is pointing at.

### Axis 2. Entry Apparatus

What does the reader find before the chapters begin?

**Option A — Single Preface.** `PREFACE.md` at project root (already written). LUCY's voice, the 4 rules, the forbidden framings, an invitation.

**Option B — Preface + Region Introductions.** Preface plus a 1,500-word introduction per region (26 of them), each written in the voice of that region's dominant cultural mode. The Pacific region introduction in Maritime-Deep-Ocean register; the Fertile Crescent introduction in Sedimentary-Temple-Administrative register. The region introduction is itself a demonstration of the Voice Spectrum before the reader meets any chapter.

**Option C — Preface + Region Introductions + Per-People Capsules.** Every people gets a 200-400 word capsule before its chapters, naming the culture in its own language, giving the reader a foothold before the scene opens. (The existing 00-OVERVIEW.md files are partial drafts of these.)

**Recommendation: Option C (full apparatus) as eventual goal; Option A (Preface only) as current state.** The region introductions are a natural Session 4 project — 26 × 1,500 words = 39,000 words of additional prose that demonstrates the typology before the chapters deliver on it.

### Axis 3. Cross-Reference Infrastructure

How does the reader navigate the inter-chapter resonances?

**Option A — Inline footnotes.** Each chapter contains "See also: [Mali Era 3]" footnotes where relevant resonances occur. Low technical requirement; modest reader benefit.

**Option B — End-of-chapter resonance panels.** Each chapter ends with a one-page "Resonances" panel naming 3-5 chapters this one speaks to. Higher reader benefit; modest authorial work.

**Option C — Structural index.** A back-matter index keyed to the Track B typologies. "Covenant engines: Mali eras 1-5, Haudenosaunee era 2, Rome era 1 ..." "Terminal Condition: Premise Non-Recognition: Taíno era 3, Peru era 3, Canada era 4, Cuba era 2." A reader can read the chronicle by following a typology rather than a geography.

**Option D — All three.** Inline footnotes for direct citations, end-of-chapter resonance panels for narrative connections, structural index for typological reading.

**Recommendation: Option D (all three), phased.** Footnotes are easy and should exist in all chapters now (many already do). Resonance panels are a Session 4 add. Structural index is a Session 5 back-matter addition after the typologies saturate.

### Axis 4. Physical Form

What does the reader hold?

**Option A — Single print volume.** ~680k words is approximately 2,000-2,500 pages at standard academic trim. That is physically possible but unwieldy. Tolstoy's *War and Peace* is ~587k words; *The Lord of the Rings* is ~480k. A single-volume LUCIA would exceed both. Readers would not finish.

**Option B — Multi-volume print.** Five volumes of ~136k words each (approximately 400-450 pages per volume), grouped by region-cluster: (1) The Americas, (2) The Fertile Crescent and Mediterranean, (3) Africa, (4) Asia and Oceania, (5) The Modern Overlay (Americas Reborn + Colonial Empires + Diasporas + Pacific Century). This is the Durant pattern for *The Story of Civilization*.

**Option C — Online canonical + print anthologies.** The chronicle lives online as a navigable reference. Print appears as curated anthologies — "LUCIA: The Five Complete Books" (Mali, Inca, Rome + 2 forthcoming as 5-era books mature). Print is the curator's selection; online is the total archive.

**Option D — Hybrid: digital canonical, printable per-region.** The chronicle lives online. Each region can be printed as a standalone volume through print-on-demand. The reader who wants Sahel reads Sahel; the reader who wants all 26 regions buys the boxed set.

**Recommendation: Option C (online canonical + print anthologies).** LUCIA's cross-reference infrastructure benefits from hyperlinking; print does not preserve the resonance-panel navigation well. Print as curator's selection maintains the reverence without forcing completion-bias on the reader.

### Axis 5. Reader's Apparatus

What does the reader need beyond the chapters themselves?

**Option A — None.** Text is self-sufficient. No glossary, no maps, no timelines. The reader is dropped into the scene.

**Option B — Minimal back-matter.** Glossary of non-English terms (sparse; defined on first use in each chapter); pronunciation guide; dramatis personae per culture.

**Option C — Full scholarly apparatus.** Glossary + pronunciation + dramatis personae + maps per region + date tables per culture + source tier explanation for lay readers + index.

**Option D — Tiered apparatus.** Minimal back-matter for narrative reading; full apparatus available online for scholarly use. Different readers, different needs.

**Recommendation: Option D (tiered).** A reader entering for the first time should not need to consult apparatus. A scholar returning to verify a source should find it in minutes.

---

## The Recommended Synthesis

Combining the axis recommendations:

1. **Sequencing:** Regional default; Resonance curated alternate.
2. **Entry apparatus:** Full — Preface + Region Intros + People Capsules.
3. **Cross-reference:** Footnotes + Resonance panels + Structural index.
4. **Physical form:** Online canonical + print anthologies (Durant-style complete-book selections).
5. **Reader's apparatus:** Tiered — minimal inline, full online.

The chronicle is an **online navigable reference with curated print volumes**. The online form is canonical, cross-referenced, searchable by typology. The print form selects completed books (currently Mali, Inca, Rome; more to come) into anthology volumes that stand on their own.

---

## What Needs to Happen Before Manuscript-Ready

Six gaps remain before LUCIA can be read as a manuscript rather than a production archive.

**Gap 1 — Complete more books.** Mali, Inca, Rome are the only 5-era books. 93 cultures have 1 chapter. The manuscript's narrative weight depends on more complete books. Target Session 4: complete Tang, Haudenosaunee, Norse, San, Benin (5 more books, 23 additional chapters). Gap closes at ~140 chapters with 8 complete books.

**Gap 2 — Region introductions.** 26 × 1,500 words per region, each in the region's dominant voice register. Demonstrates the Voice Spectrum before the chapters do. ~39,000 additional words.

**Gap 3 — Cross-reference panels.** Each chapter gets an end-of-chapter "Resonances" panel. For 115 chapters at ~200 words each, that is 23,000 words. For Session 4 or 5.

**Gap 4 — Structural index.** Back-matter index keyed to Voice Spectrum, Structural Engines, Terminal Conditions. ~5,000 words organized as lookup tables. Awaits typology saturation (Voice saturated, Engine saturated, Terminal pending).

**Gap 5 — Pronunciation and dramatis personae.** Per-culture back-matter. Small scope per culture (100-300 words each); large total (93 cultures × 200 words = ~19,000 words).

**Gap 6 — Source tier explanation for lay readers.** Introductory essay on the five source tiers and why the distinction matters. ~2,000 words. Sits between Preface and Region Intros.

Total additional prose: approximately 85,000-90,000 words for full manuscript apparatus. This is roughly 13% of the chronicle's current word count. Substantial but tractable.

---

## Alternate Architecture (Preserved)

If the recommendation above is rejected, the strongest alternative is **Thematic Sequence with Structural Index as Spine.**

In this alternate: the chronicle is organized by structural engine (the Track B typology), not by region. A reader opens to the Covenant chapter-group, reads Mali and Haudenosaunee side by side, sees the engine pattern across cultures, then moves to the Material Object chapter-group. Each chapter's cultural specificity still carries the weight, but the reading structure foregrounds the methodology.

This is the "chron module as public artifact" reading — a chronicle whose primary contribution is the typology, with the cultures as evidentiary instances. It risks the opposite of the Four Rules: the reader is inside the typology, not inside the culture. The Achebe Test becomes harder to maintain when the reading order is framework-first.

We do not recommend this alternative for the main manuscript, but we flag it as an appropriate secondary artifact — a "Methodological Companion" volume that reads the chronicle through the Track B lens. The chron research module in `craftworks-research\chron` is effectively this companion already; it could be edited into a reader-facing methodological volume once Sprint-1 figure rendering and citation resolution are complete.

---

## Decision Points for Session 4 and Beyond

1. Adopt the recommendation or an alternative? [Pending.]
2. If adopted: begin region introductions in Session 4, or defer to Session 5?
3. Print anthology scope: Mali+Inca+Rome now (3 books, 1 volume) or wait for 5 complete books (Session 5)?
4. Online canonical: build the navigable reference as a static site generator (Jekyll/Hugo/Astro) or hand-roll? What is the minimum-viable online publication?
5. Should the chron research module (methodological companion) be bundled with LUCIA or published separately? (Recommendation: separately; different audiences.)

These decisions are outside the present session's scope. This document exists to frame them.

---

## Conclusion

LUCIA is 115 chapters and ~680,000 words of culture-chapter prose. It is not yet a manuscript. The five-axis proposal above sketches what has to happen — additional prose (~85-90k words), infrastructure (online navigable reference + print anthology), and phased apparatus (tiered, reader-appropriate) — before the chronicle can be read rather than assembled.

The path is manageable. The scope is defined. The recommendation stands unless contested.

— LUCY
2026-04-20

# LUCIA Principles

## LUCIA-P-01: Cultures Speak From Inside

**Decision rule:** LUCIA chapters present each culture from inside its own
worldview and must not import outside judgment, modern superiority framing, or
cross-culture ranking into chapter prose.

**Rationale:** The chronicle's core promise fails if the authorial lens becomes
external even when the facts are correct.

**Test:** The 11-stage pipeline includes inside-voice, judgment, panel, and
board review gates before a chapter is locked.

**Evidence:** `CLAUDE.md`, `README.md`, `.roles/ROLE.md`,
`skills/chronicle-clean/SKILL.md`, and `skills/chronicle-board/SKILL.md`.

## LUCIA-P-02: Source Tier Controls Factual Authority

**Decision rule:** Primary, academic, scholarly secondary, reference, and
disallowed sources remain separate, and every factual claim in locked chapters
needs source support appropriate to the claim.

**Rationale:** A narrative encyclopedia needs vivid prose without weakening
source custody.

**Test:** Board roles, notes generation, cleanup, and source registry practices
keep citations and source limits visible.

**Evidence:** `CLAUDE.md`, `README.md`, `sources/MASTER.md`,
`skills/chronicle-notes/SKILL.md`, and `.roles/board/ROLE.md`.

## LUCIA-P-03: Rubric Evolution Is Forward Only

**Decision rule:** Rubric innovations are logged append-only and apply forward;
earlier locked chapters are not silently re-scored under later standards.

**Rationale:** The project can learn from exceptional chapters only if
historical scoring remains stable.

**Test:** Rubric and innovation docs require scoring against the locked version
active when the chapter started.

**Evidence:** `README.md`, `CLAUDE.md`, `scoring/RUBRIC.md`,
`scoring/INNOVATIONS.md`, and `skills/chronicle-innovation/SKILL.md`.

## LUCIA-P-04: Structured History Compares Against Established Story

**Decision rule:** The people-history Rust layer may validate structured
persons, events, eras, and consequences, but it must compare against established
chapter profiles rather than replacing chapter authority.

**Rationale:** Structured continuity is useful only while prose chapters remain
the established story.

**Test:** Core tests and CLI compare fixtures report missing events, persons,
story paths, uncited records, and external framing flags.

**Evidence:** `docs/people-history-engine.md`,
`crates/lucia-history-core/src/lib.rs`,
`fixtures/people-history/mali-established-profile.json`, and
`cargo run -p lucia-history-cli -- compare fixtures\people-history\mali-people-history.json fixtures\people-history\mali-established-profile.json`.

## LUCIA-P-05: Product-Local Crates Are Not Shared History Primitives

**Decision rule:** `lucia-history-core` and `lucia-history-cli` remain
product-local until a named downstream consumer defines a bounded versioned
contract and owns compatibility tests.

**Rationale:** LUCIA's Rust substrate encodes editorial rules that are not yet a
generic portfolio standard.

**Test:** README reuse boundary and validation commands keep BANISH/gamepack
use below crate-stability claims.

**Evidence:** `README.md`, `docs/people-history-engine.md`, and
`cargo test --workspace`.

# LUCIA Pitfalls

## LUCIA-PF-01: Manuscript Proposal Becomes Publication Readiness

**Status:** MITIGATED

**Pattern:** The manuscript architecture proposal, 115 locked chapters, or
article-export pipeline is described as reader-ready publication rather than a
proposal plus staged apparatus work.

**Actor:** Public reader, portfolio reviewer, manuscript maintainer, or future
agent summarizing LUCIA's readiness.

**Task:** Decide whether LUCIA is ready to publish, package, export, or promote
as a reader-facing manuscript.

**Surface:** `README.md`, `docs/MANUSCRIPT-ARCHITECTURE.md`, research article
exports, portfolio summaries, and public release notes.

**Likely mistake:** Treat the scale of the locked corpus or the export pipeline
as proof that the manuscript apparatus and publication decision are complete.

**Consequence:** Public or portfolio copy can overclaim reader readiness,
skip the remaining apparatus gaps, or turn a proposal into a release promise.

**Owner:** LUCIA owns manuscript-readiness language and apparatus gates;
TRACKER may summarize readiness but must not turn proposal state into release
approval.

**Domain:** README claims, manuscript architecture, print/online planning,
research article exports, portfolio summaries, and public release notes.

**Detection difficulty:** The corpus is large and mature, so proposal language
can sound like a publication decision.

**Structural solution:** Keep manuscript-readiness claims gated by the six
apparatus gaps, explicit decision points, export validation, and role review;
place the boundary next to public corpus-scale metrics so locked-chapter counts
do not imply publication readiness.

**Evidence:** `docs/MANUSCRIPT-ARCHITECTURE.md`, `README.md`,
`context/waves/2026-07-26-md-family-migration/WAVE.md`, and `.roles/ROLE.md`.

**Test:** `tests/check-lucia-pitfall-policy.ps1` checks the manuscript
architecture proposal and requires README-local language that treats the
115-chapter track record as a production archive, not manuscript publication
readiness.

## LUCIA-PF-02: Structured History Replaces Chapter Authority

**Status:** OPEN

**Pattern:** People-history JSON, compare reports, or BANISH gamepack scores are
treated as authoritative history rather than structured evidence checked
against established LUCIA chapters.

**Actor:** Downstream consumer, gamepack maintainer, history-substrate
maintainer, or future agent preferring structured records over prose chapters.

**Task:** Reuse LUCIA history data, compare a people-history fixture, or
extract a generic history primitive.

**Surface:** `docs/people-history-engine.md`, `crates/lucia-history-*`,
`fixtures/people-history/*.json`, BANISH gamepack scores, and generated corpus
views.

**Likely mistake:** Treat valid JSON, compare output, or downstream score data
as the established historical account instead of chapter-adjacent evidence.

**Consequence:** Structured records can displace source-cited prose, import
LUCIA editorial policy into consumers, or create an unsupported shared-history
contract.

**Owner:** LUCIA owns people-history semantics and established-story
comparison; downstream repos own their own consumer contracts and compatibility
proof.

**Domain:** Rust substrate, fixture records, downstream gamepack use, generated
corpus views, and future extraction proposals.

**Detection difficulty:** Structured records are easier for agents and games to
consume than long prose, so they can quietly displace the chapter source.

**Structural solution:** Require established-story comparison, source refs, and
downstream-owned contracts before promoting any generic history primitive.

**Evidence:** `docs/people-history-engine.md`, `README.md`,
`crates/lucia-history-core/src/lib.rs`, and
`cargo run -p lucia-history-cli -- compare fixtures\people-history\mali-people-history.json fixtures\people-history\mali-established-profile.json`.

**Test:** `tests/check-lucia-pitfall-policy.ps1`

## LUCIA-PF-03: Rubric Learning Rewrites Locked History

**Status:** OPEN

**Pattern:** A later rubric version, typology cluster, or innovation log entry
is applied backward to re-score or rewrite already locked chapters without an
explicit migration.

**Actor:** Rubric maintainer, chapter editor, research-paper author, quality
dashboard maintainer, or future agent applying a newer rubric.

**Task:** Interpret innovations, update scoring guidance, compare chapters, or
repair older locked chapter records.

**Surface:** `scoring/RUBRIC.md`, `scoring/INNOVATIONS.md`,
`scoring/CROSS-COMPARE-*.md`, chapter status records, skills, and research
papers.

**Likely mistake:** Apply the latest rubric backward because it looks better
than the version that governed the locked chapter.

**Consequence:** Historical scores lose meaning, published quality claims
drift, and rubric research starts measuring rewritten evidence.

**Owner:** LUCIA owns rubric-version custody and explicit migration decisions;
research summaries must preserve the forward-only boundary.

**Domain:** Scoring, innovation logs, cross-compare reports, chapter status,
research papers, and quality dashboards.

**Detection difficulty:** Forward-only evolution is easy to affirm but hard to
remember when a new rubric improvement seems obviously better.

**Structural solution:** Preserve append-only innovation logs, rubric version
history, and explicit migrations for any backward-facing update.

**Evidence:** `scoring/RUBRIC.md`, `scoring/INNOVATIONS.md`, `README.md`, and
`skills/chronicle-innovation/SKILL.md`.

**Test:** `tests/check-lucia-pitfall-policy.ps1`

## LUCIA-PF-04: Board Catalog Becomes Active Review By Default

**Status:** OPEN

**Pattern:** The large `.roles/board/` catalog is treated as an instruction to
activate every listed specialist, or stale/duplicate roles stay active without
selection rationale.

**Actor:** Chapter orchestrator, reviewer, board-role maintainer, or future
agent running the final review stage.

**Task:** Select board reviewers, create specialist roles, or maintain the
board catalog for a chapter.

**Surface:** `.roles/ROLE.md`, `.roles/board/ROLE.md`, `.roles/board/*.md`,
`skills/chronicle-board/SKILL.md`, and chapter review artifacts.

**Likely mistake:** Read catalog size as active review coverage and activate
too many, stale, duplicate, or weakly relevant specialists.

**Consequence:** Review becomes noisy, selection rationale disappears, stale
roles look authoritative, and chapter-specific domain evidence gets diluted.

**Owner:** LUCIA owns board-role selection and retirement discipline; each
chapter review artifact owns selected role files and rationale.

**Domain:** Chapter review artifacts, board role maintenance, pipeline skills,
future generated reviews, and role-index updates.

**Detection difficulty:** A large expert catalog looks like stronger review
coverage even when only two or three directly relevant specialists should be
selected per chapter.

**Structural solution:** Record selected board roles and selection reasons,
merge duplicates, repair stale references, and retire roles with no distinct
scope or use.

**Evidence:** `.roles/ROLE.md`, `.roles/board/ROLE.md`, and
`skills/chronicle-board/SKILL.md`.

**Test:** `tests/check-lucia-pitfall-policy.ps1`

## LUCIA-PF-05: Unsupported Source Tier Becomes Narrative Evidence

**Status:** MITIGATED

**Pattern:** Disallowed sources, unsourced AI output, mirrors, or weak reference
material are used as if they were primary, academic, or scholarly evidence for a
chapter claim.

**Domain:** Source registry, notes, chapter prose, board review, cleanup,
article exports, and generated derivative packs.

**Detection difficulty:** Narrative polish can hide weak evidence unless source
tiers remain visible through the production process.

**Structural solution:** Keep the five source tiers explicit and require notes,
board, and cleanup review for sourced factual claims.

**Evidence:** `CLAUDE.md`, `README.md`, `sources/MASTER.md`,
`skills/chronicle-notes/SKILL.md`, and `skills/chronicle-clean/SKILL.md`.

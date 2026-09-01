# LUCIA Invariants

## LUCIA-INV-01: People-History Fixture Validates Cleanly

**Status:** MITIGATED

**Claim:** The retained Mali people-history JSON validates without findings.

**Why it matters:** The Rust substrate needs at least one clean product-local
fixture before it can support chapter-adjacent workflows.

**Enforcement:** CLI validation returns an empty findings list for the retained
fixture.

**Evidence:** `docs/people-history-engine.md`,
`fixtures/people-history/mali-people-history.json`, and
`cargo run -p lucia-history-cli -- validate fixtures\people-history\mali-people-history.json`.

## LUCIA-INV-02: Established-Story Comparison Passes For The Mali Fixture

**Status:** MITIGATED

**Claim:** The retained Mali people-history fixture satisfies the established
story profile without missing event, person, story path, citation, or external
framing findings.

**Why it matters:** Structured history must prove it can preserve established
chapter expectations.

**Enforcement:** CLI comparison and core tests check required story elements.

**Evidence:** `fixtures/people-history/mali-established-profile.json`,
`crates/lucia-history-core/src/lib.rs`, and
`cargo test comparison_passes_when_required_story_elements_are_present`.

## LUCIA-INV-03: Missing Established-Story Requirements Hold Comparison

**Status:** MITIGATED

**Claim:** The comparison report holds when required event, person, or story
path requirements are missing.

**Why it matters:** The structured layer must fail visibly instead of
validating a thin history record.

**Enforcement:** Core tests assert missing event, person, and story path
findings.

**Evidence:** `crates/lucia-history-core/src/lib.rs` and
`cargo test comparison_holds_when_established_story_requirements_are_missing`.

## LUCIA-INV-04: Article Backfill Entry Point Exists

**Status:** MITIGATED

**Claim:** The article-backfill generator exposes its help surface after the MD
family migration.

**Why it matters:** Publication artifacts, PROOF sidecars, MDPORT packs, and
FLETCH registry outputs need a runnable entry point before generated export
claims are credible.

**Enforcement:** The migration wave records the help command, and PITFALL
adoption reran it.

**Evidence:** `context/waves/2026-07-26-md-family-migration/WAVE.md`,
`.claude/skills/lucia-article-backfill/scripts/article_backfill.py`, and
`python .claude\skills\lucia-article-backfill\scripts\article_backfill.py --help`.

## LUCIA-INV-05: Strict Static Analysis Is Already Green

**Status:** MITIGATED

**Claim:** Formatter, workspace tests, strict clippy, CLI fixture commands, and
`git diff --check` pass without code changes during PITFALL adoption.

**Why it matters:** LUCIA's product-local Rust substrate is ready to serve as
evidence without weakening validation gates.

**Enforcement:** PITFALL adoption reran the validation bundle.

**Evidence:** `cargo fmt --check`, `cargo test --workspace`,
`cargo clippy --workspace --all-targets -- -D warnings`, and `git diff --check`.

## LUCIA-INV-06: History Boundaries Stay Machine-Readable

**Status:** MITIGATED

**Claim:** Structured-history authority, rubric-version custody, board
activation, and downstream consumer-contract ownership are recorded in a
machine-readable boundary manifest.

**Why it matters:** LUCIA's corpus, rubric, and role catalog are large enough
that useful shortcuts can look authoritative. A structured boundary keeps
chapter authority, forward-only learning, and selected board review explicit.

**Enforcement:** The PITFALL policy check parses the boundary manifest and
requires blocked claims for structured history, rubric learning, and board
activation.

**Evidence:** `docs/history-boundaries.v1.json` and
`tests/check-lucia-pitfall-policy.ps1`.

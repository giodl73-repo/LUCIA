# People History Engine

Status: foundation Rust substrate

LUCIA can grow a structured history-of-peoples layer beside the established
chapters. The goal is the same pressure that makes world-simulation histories
feel alive: people, events, institutions, places, and consequences accumulate
over eras. The boundary is strict: structured history must compare against
LUCIA's established stories instead of replacing them.

## What the Rust crates own

| Crate | Role |
|---|---|
| `lucia-history-core` | Product-local structs and comparison rules for people histories, eras, persons, events, story references, validation findings, and established-story profiles. |
| `lucia-history-cli` | Small command-line wrapper for validating a people-history JSON file or comparing it to an established-story profile. |

## Boundary

- LUCIA chapters remain the established story.
- The people-history layer records structured continuity: who appears, what
  event belongs to which era, what consequence carries forward, and which chapter
  supports the claim.
- The comparison profile names required events, persons, chapter paths, and
  forbidden external framings.
- This is not a procedural fiction generator, victory system, RPG stat block, or
  replacement for the Achebe Test.
- RLINE history/context kernels remain a future extraction candidate only after
  LUCIA proves repeated product-local needs.

## First fixture

The foundation fixture is:

```powershell
fixtures\people-history\mali-people-history.json
fixtures\people-history\mali-established-profile.json
```

It proves the comparison shape: a people-history record can cite an established
Mali chapter path, declare a person and event, and compare those against required
story elements.

## Validation

```powershell
cargo test
cargo run -p lucia-history-cli -- validate fixtures\people-history\mali-people-history.json
cargo run -p lucia-history-cli -- compare fixtures\people-history\mali-people-history.json fixtures\people-history\mali-established-profile.json
```

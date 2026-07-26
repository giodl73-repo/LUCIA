---
wave: md-family-migration
date_open: 2026-07-26
status: done
source_request: "Resolve remaining local state and clean MDPORT/MDLOOM paths."
---

# Wave: MD family migration

LUCIA's article backfill generator and tracked derived artifacts now use:

- `.mdloom/` and `mdloom.*` for source/backfill artifacts,
- `.mdport/` and `mdport.v1` for portable records,
- MDLOOM as the guide compiler,
- FLETCH registries pointing at the renamed artifacts.

Narrative chapters and review prose were not changed.

Validation:

- `python .claude/skills/lucia-article-backfill/scripts/article_backfill.py --help`
- `cargo test --workspace`
- `git diff --check`

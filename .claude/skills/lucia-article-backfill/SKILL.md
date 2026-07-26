---
name: lucia-article-backfill
description: "Backfill LUCIA research articles into CROP/MDPORT/MDLOOM/FLETCH artifacts and export DOCX/PDF on demand."
tags: [lucia, articles, proof, crop, mdport, fletch, docx, pdf]
---

# lucia-article-backfill

Backfill LUCIA `research/papers/*/main.md` articles into the shared source-corpus
flow and generate publication formats on demand.

## Usage

```powershell
python .claude\skills\lucia-article-backfill\scripts\article_backfill.py --all --validate
python .claude\skills\lucia-article-backfill\scripts\article_backfill.py --paper chron-voice-spectrum --export docx
python .claude\skills\lucia-article-backfill\scripts\article_backfill.py --all --export all
```

## Generated surfaces

| Surface | Path pattern |
|---|---|
| CROP article views | `.crop/views/lucia-{paper}.json` |
| CROP corpus view | `.crop/views/lucia-articles-source-corpus.json` |
| MDPORT article packs | `.mdport/packs/lucia-{paper}.mdport.json` |
| MDPORT corpus pack | `.mdport/packs/lucia-articles-source-corpus.mdport.json` |
| MDLOOM literal sources | `.mdloom/backfill/sources/articles/mdloom-source/{paper}.source.md` |
| MDLOOM table sidecars | `.mdloom/backfill/sources/articles/mdloom-source/{paper}.tables.json` |
| MDLOOM block sidecars | `.mdloom/backfill/sources/articles/mdloom-source/{paper}.blocks.json` |
| Source records | `.mdloom/backfill/sources/articles/{paper}.source-record.md` |
| Article ledger | `.mdloom/backfill/modules/lucia-articles.json` |
| FLETCH registry | `.fletch/registries/lucia-articles-source-corpus.json` |
| DOCX/PDF exports | `research/papers/_exports/{paper}.{docx,pdf}` |

## Rules

- `main.md` is the canonical article source. Edit it first, then rerun this helper.
- Do not hand-edit generated backfill artifacts unless changing the generator.
- DOCX/PDF files are generated on demand and not committed by default.
- Keep LUCIA article claims in LUCIA; FLETCH only publishes fetchable artifact
  locations and formats.

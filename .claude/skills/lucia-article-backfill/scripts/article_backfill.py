#!/usr/bin/env python3
"""Backfill LUCIA articles and export DOCX/PDF publication artifacts."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path.cwd()
ARTICLE_ROOT = Path("research") / "papers"
EXPORT_ROOT = ARTICLE_ROOT / "_exports"
SOURCE_ID = "articles"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def title_from_markdown(path: Path) -> str:
    for line in read_text(path).splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.parent.name


def run(command: list[str], *, stdout_path: Path | None = None) -> None:
    if stdout_path:
        stdout_path.parent.mkdir(parents=True, exist_ok=True)
        with stdout_path.open("w", encoding="utf-8", newline="\n") as handle:
            subprocess.run(command, check=True, stdout=handle)
    else:
        subprocess.run(command, check=True)


def git_hashes(path: Path) -> list[str]:
    output = subprocess.check_output(
        ["git", "--no-pager", "log", "--format=%h", "--", str(path)],
        text=True,
    )
    return [line for line in output.splitlines() if line]


def tick_list(values: list[str]) -> str:
    return ", ".join(f"`{value}`" for value in values) if values else "pending"


def collect_papers(selected: str | None) -> list[dict[str, str]]:
    papers = []
    for paper_dir in sorted(ARTICLE_ROOT.iterdir()):
        if not paper_dir.is_dir() or paper_dir.name.startswith("_"):
            continue
        if selected and paper_dir.name != selected:
            continue
        main = paper_dir / "main.md"
        if not main.exists():
            continue
        paper_id = paper_dir.name
        papers.append(
            {
                "id": paper_id,
                "slug": slugify(paper_id),
                "title": title_from_markdown(main),
                "dir": paper_dir.as_posix(),
                "main": main.as_posix(),
                "view": (Path(".mdcrop") / "views" / f"lucia-{paper_id}.json").as_posix(),
                "pack": (Path(".mdport") / "packs" / f"lucia-{paper_id}.mdport.json").as_posix(),
                "source_md": (
                    Path(".proof")
                    / "backfill"
                    / "sources"
                    / SOURCE_ID
                    / "proof-source"
                    / f"{paper_id}.source.md"
                ).as_posix(),
                "tables": (
                    Path(".proof")
                    / "backfill"
                    / "sources"
                    / SOURCE_ID
                    / "proof-source"
                    / f"{paper_id}.tables.json"
                ).as_posix(),
                "blocks": (
                    Path(".proof")
                    / "backfill"
                    / "sources"
                    / SOURCE_ID
                    / "proof-source"
                    / f"{paper_id}.blocks.json"
                ).as_posix(),
                "source_record": (
                    Path(".proof")
                    / "backfill"
                    / "sources"
                    / SOURCE_ID
                    / f"{paper_id}.source-record.md"
                ).as_posix(),
            }
        )
    return papers


def extract_tables_and_blocks(text: str, source_path: str) -> tuple[dict, dict]:
    lines = text.splitlines()
    tables = []
    blocks = []
    in_fence = False
    fence_start = 0
    fence_lines: list[str] = []
    for index, line in enumerate(lines, start=1):
        if line.startswith("```"):
            if in_fence:
                blocks.append(
                    {
                        "kind": "fenced_block",
                        "start_line": fence_start,
                        "end_line": index,
                        "text": "\n".join(fence_lines),
                    }
                )
                in_fence = False
                fence_lines = []
            else:
                in_fence = True
                fence_start = index
                fence_lines = [line]
            continue
        if in_fence:
            fence_lines.append(line)
        if "|" in line and index < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[index]):
            tables.append({"kind": "markdown_table", "start_line": index, "header": line})
    return (
        {"schema_version": "1", "source_markdown": source_path, "tables": tables},
        {"schema_version": "1", "source_markdown": source_path, "blocks": blocks},
    )


def format_obj(schema: str, shape: str, preferred: str, media: str = "application/json") -> dict[str, str | None]:
    return {
        "media_type": media,
        "encoding": "utf-8",
        "compression": None,
        "container": None,
        "schema": schema,
        "record_shape": shape,
        "preferred_local": preferred,
    }


def backfill(papers: list[dict[str, str]], mdcrop_manifest: str, fletch_manifest: str, validate: bool) -> None:
    view_store = Path(".mdcrop") / "views"
    pack_store = Path(".mdport") / "packs"
    source_store = Path(".proof") / "backfill" / "sources" / SOURCE_ID
    module_ledger = Path(".proof") / "backfill" / "modules" / "lucia-articles.json"
    module_view = view_store / "lucia-articles-source-corpus.json"
    module_pack = pack_store / "lucia-articles-source-corpus.mdport.json"
    registry_path = Path(".fletch") / "registries" / "lucia-articles-source-corpus.json"

    for paper in papers:
        paper_dir = Path(paper["dir"])
        view = {
            "schema_version": "mdcrop.view.v1",
            "name": f"lucia-{paper['id']}",
            "root": f"../../{paper_dir.as_posix()}",
            "task": f"Backfill LUCIA article '{paper['title']}' for DOCX/PDF and downstream source-corpus reuse.",
            "token_budget": 24000,
            "seed": 0,
            "include_extensions": ["md"],
            "exclude_dirs": ["reviews"],
        }
        write_text(Path(paper["view"]), json.dumps(view, indent=2, ensure_ascii=False) + "\n")
        run(
            [
                "cargo",
                "run",
                "--manifest-path",
                mdcrop_manifest,
                "--quiet",
                "--",
                "view",
                "--file",
                paper["view"],
                "--format",
                "mdport",
            ],
            stdout_path=Path(paper["pack"]),
        )
        source_text = read_text(Path(paper["main"]))
        write_text(Path(paper["source_md"]), source_text)
        tables, blocks = extract_tables_and_blocks(source_text, paper["main"])
        write_text(Path(paper["tables"]), json.dumps(tables, indent=2, ensure_ascii=False) + "\n")
        write_text(Path(paper["blocks"]), json.dumps(blocks, indent=2, ensure_ascii=False) + "\n")
        record = f"""---
lucia_schema: lucia.article-backfill.v1
id: proof-backfill:lucia:{paper['id']}
kind: source-record
module: lucia-articles
title: {paper['title']} source record
status: source-custody
source_custody: partial
current_path: {paper['source_record']}
canonical_path: {paper['source_record']}
backsource_ids: [git-history:lucia:{paper['id']}]
index_roles: [source-map, article-export]
updated: null
---

# {paper['title']} source record

| Field | Value |
|---|---|
| Current LUCIA article | `{paper['main']}` |
| PROOF-style source artifact | `{paper['source_md']}` |
| Table sidecar | `{paper['tables']}` |
| Block sidecar | `{paper['blocks']}` |
| MDCROP view | `{paper['view']}` |
| MDPORT pack | `{paper['pack']}` |
| DOCX export command | `python .claude\\skills\\lucia-article-backfill\\scripts\\article_backfill.py --paper {paper['id']} --export docx` |
| PDF export command | `python .claude\\skills\\lucia-article-backfill\\scripts\\article_backfill.py --paper {paper['id']} --export pdf` |
| Git provenance | {tick_list(git_hashes(Path(paper['main'])))} |

## Custody note

This first-pass record proves the current article can be published as a local
source-corpus artifact and exported on demand. It is still marked `partial`
because external/authentic backsources for every factual claim have not yet been
attached.
"""
        write_text(Path(paper["source_record"]), record)

    module_view_json = {
        "schema_version": "mdcrop.view.v1",
        "name": "lucia-articles-source-corpus",
        "root": "../../research/papers",
        "task": "Backfill LUCIA research articles for downstream context reuse and publication exports.",
        "token_budget": 48000,
        "seed": 0,
        "include_extensions": ["md"],
        "exclude_dirs": ["reviews", "_exports"],
    }
    write_text(module_view, json.dumps(module_view_json, indent=2, ensure_ascii=False) + "\n")
    run(
        [
            "cargo",
            "run",
            "--manifest-path",
            mdcrop_manifest,
            "--quiet",
            "--",
            "view",
            "--file",
            str(module_view),
            "--format",
            "mdport",
        ],
        stdout_path=module_pack,
    )

    module = {
        "schema_version": "lucia.article-backfill.module.v1",
        "module_id": "lucia-articles",
        "status": "first-pass-complete",
        "source_root": ARTICLE_ROOT.as_posix(),
        "source_store": source_store.as_posix(),
        "crop_view": module_view.as_posix(),
        "distribution": {
            "mdport_pack": module_pack.as_posix(),
            "article_packs": [paper["pack"] for paper in papers],
            "fletch_registry": registry_path.as_posix(),
            "exports_root": EXPORT_ROOT.as_posix(),
        },
        "source_custody": {
            "default_state": "partial",
            "notes": [
                "Article main.md files are canonical for publication exports.",
                "First pass records git provenance and generated local source artifacts.",
                "External/authentic backsources remain pending before complete custody.",
            ],
        },
        "articles": papers,
    }
    write_text(module_ledger, json.dumps(module, indent=2, ensure_ascii=False) + "\n")

    fletches = [
        {
            "id": "lucia.articles.source-corpus.mdport",
            "node_kind": "fletch",
            "shafts": [{"kind": "file", "url": module_pack.as_posix()}],
            "edges": [
                {
                    "to": "lucia-articles-source-corpus",
                    "kind": "derived-from",
                    "label": "MDCROP view recipe",
                    "metadata": {"view": module_view.as_posix(), "custody": "partial"},
                }
            ],
            "format": format_obj("mdport.v1", "corpus-slice", module_pack.as_posix()),
            "tags": ["source-corpus", "mdcrop", "mdport", "partial-custody", "articles"],
            "metadata": {"source_repo": "LUCIA", "module": "articles", "publication_state": "partial-source-custody"},
        }
    ]
    for paper in papers:
        prefix = f"lucia.articles.{paper['id']}"
        common = {
            "source_repo": "LUCIA",
            "module": "articles",
            "article": paper["main"],
            "publication_state": "partial-source-custody",
        }
        fletches.extend(
            [
                {
                    "id": f"{prefix}.view",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": paper["view"]}],
                    "edges": [{"to": "lucia.articles.source-corpus.mdport", "kind": "derived-from", "label": "Article MDCROP view recipe"}],
                    "format": format_obj("mdcrop.view.v1", "view-recipe", paper["view"]),
                    "tags": ["source-corpus", "mdcrop", "view", "article"],
                    "metadata": common,
                },
                {
                    "id": f"{prefix}.mdport",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": paper["pack"]}],
                    "edges": [{"to": f"{prefix}.view", "kind": "derived-from", "label": "Article MDCROP view recipe"}],
                    "format": format_obj("mdport.v1", "corpus-slice", paper["pack"]),
                    "tags": ["source-corpus", "mdcrop", "mdport", "article"],
                    "metadata": common,
                },
                {
                    "id": f"{prefix}.proof-source",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": paper["source_md"]}],
                    "edges": [{"to": f"{prefix}.mdport", "kind": "derived-from", "label": "Literal source for article export"}],
                    "format": format_obj("proof.source.literal_markdown.v1", "literal-source", paper["source_md"], "text/markdown"),
                    "tags": ["source-corpus", "proof", "source", "article"],
                    "metadata": common,
                },
                {
                    "id": f"{prefix}.tables",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": paper["tables"]}],
                    "edges": [{"to": f"{prefix}.proof-source", "kind": "derived-from", "label": "Markdown table sidecar"}],
                    "format": format_obj("proof.backfill.tables.v1", "table-sidecar", paper["tables"]),
                    "tags": ["source-corpus", "proof", "tables", "article"],
                    "metadata": common,
                },
                {
                    "id": f"{prefix}.blocks",
                    "node_kind": "fletch",
                    "shafts": [{"kind": "file", "url": paper["blocks"]}],
                    "edges": [{"to": f"{prefix}.proof-source", "kind": "derived-from", "label": "Structured block sidecar"}],
                    "format": format_obj("proof.backfill.blocks.v1", "structured-block-sidecar", paper["blocks"]),
                    "tags": ["source-corpus", "proof", "blocks", "article"],
                    "metadata": common,
                },
            ]
        )
    registry = {
        "schema_version": "fletch.registry.v1",
        "generated_by": "LUCIA article backfill",
        "registry_id": "lucia-articles-source-corpus",
        "fletches": fletches,
    }
    write_text(registry_path, json.dumps(registry, indent=2, ensure_ascii=False) + "\n")

    if validate:
        run(["cargo", "run", "--manifest-path", mdcrop_manifest, "--quiet", "--", "view", "--inspect", "--dir", str(view_store), "--strict"])
        run(["cargo", "run", "--manifest-path", fletch_manifest, "--bin", "fletch-cli", "--quiet", "--", "registry", "validate", "--file", str(registry_path)])
        missing = [shaft["url"] for fletch in fletches for shaft in fletch["shafts"] if not Path(shaft["url"]).exists()]
        if missing:
            raise SystemExit(f"registry shaft paths missing: {missing}")
        run(["git", "--no-pager", "diff", "--check"])

    print(json.dumps({"articles": len(papers), "fletches": len(fletches), "registry": registry_path.as_posix()}, indent=2))


def export_articles(papers: list[dict[str, str]], export: str) -> None:
    formats = ["docx", "pdf"] if export == "all" else [export]
    for paper in papers:
        for fmt in formats:
            output = EXPORT_ROOT / f"{paper['id']}.{fmt}"
            output.parent.mkdir(parents=True, exist_ok=True)
            command = ["pandoc", paper["main"], "--standalone", "--metadata", f"title={paper['title']}", "-o", str(output)]
            if fmt == "pdf":
                engine = shutil.which("xelatex") or shutil.which("lualatex")
                if engine is None:
                    raise SystemExit("PDF export requires xelatex or lualatex for Unicode article text")
                command.extend(["--pdf-engine", engine, "--variable", "mainfont=Arial"])
            run(command)
            print(f"exported {output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true")
    group.add_argument("--paper", help="Paper directory name under research/papers.")
    parser.add_argument("--export", choices=["docx", "pdf", "all"], help="Export selected article(s) with pandoc.")
    parser.add_argument("--skip-backfill", action="store_true", help="Only export; do not regenerate source-corpus artifacts.")
    parser.add_argument("--mdcrop-manifest", default=r"..\..\tools-infra\mdcrop\Cargo.toml")
    parser.add_argument("--fletch-manifest", default=r"..\..\tools-infra\fletch\Cargo.toml")
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()

    papers = collect_papers(None if args.all else args.paper)
    if not papers:
        raise SystemExit("no matching LUCIA article papers found")
    if not args.skip_backfill:
        backfill(papers, args.mdcrop_manifest, args.fletch_manifest, args.validate)
    if args.export:
        export_articles(papers, args.export)


if __name__ == "__main__":
    main()

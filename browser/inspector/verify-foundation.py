"""Protect native, manuscript, policy, source and structural state in sparse checkout."""
import json,pathlib,subprocess
R=pathlib.Path(__file__).resolve().parents[2];entry='29febdc9f141a32e8c917942e543228c90c7c4d8'
paths=['Cargo.toml','Cargo.lock','crates','fixtures','CLAUDE.md','TRACKER.md','PREFACE.md','regions','scoring','sources','guides','skills','.claude','.roles','.pitfall','docs/history-boundaries.v1.json','docs/people-history-engine.md','docs/MANUSCRIPT-ARCHITECTURE.md','tests','LICENSE']
changes=subprocess.check_output(['git','diff','--name-only',entry,'--',*paths],cwd=R).decode().splitlines();assert not changes,changes
# Compare the commit/index/working state; absent sparse manuscript paths stay
# protected by unchanged index entries rather than needing duplicate checkouts.
assert not subprocess.check_output(['git','diff','--cached','--name-only',entry,'--',*paths],cwd=R).strip()
old_readme=subprocess.check_output(['git','show',entry+':README.md'],cwd=R).decode();assert(R/'README.md').read_text(encoding='utf-8').startswith(old_readme),'Only a scoped README append is allowed'
print(json.dumps({'entry':entry,'native_workspace_core_cli_locks_fixtures':'unchanged','chapter_manuscript_rubric_policy_structural_grants':'unchanged','sparse_checkout_supported':True}))

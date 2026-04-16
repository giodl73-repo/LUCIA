You are running /chronicle-handoff to close the current session and prepare
for the next one. This is LUCY's end-of-session discipline.

---

## Input

- **Session number**: auto-detect from the latest `agents/LUCY-HANDOFF-S*.md`
  file (increment by 1), or S01 if none exists.

## Steps

### Step 1: Gather Session State

Read these files to understand current state:
- `TRACKER.md` — chapter counts and region status
- `scoring/INNOVATIONS.md` — innovations logged this session
- `scoring/RUBRIC.md` — current rubric version
- `agents/LUCY-PUNCHLIST.md` — previous priorities
- `agents/AGENT-ROSTER.md` — agent spawn history

Run these commands to count:
```bash
find regions/ -name "chapter.md" | wc -l          # locked chapters
find regions/ -name "00-OVERVIEW.md" | wc -l       # peoples with overviews
find regions/ -name "00-LANDSCAPE.md" | wc -l      # regions with landscapes
git log --oneline --since="today" | head -30        # today's commits
```

### Step 2: Write the Handoff

Create `agents/LUCY-HANDOFF-S{N}.md` with these sections:

```markdown
# LUCY Handoff — Session {N}

**Date:** {YYYY-MM-DD}
**From:** Session {N} (this session)
**To:** Next LUCY instance

---

## Fast-Start (read these first next session)

1. This handoff file
2. `agents/LUCY-PUNCHLIST.md`
3. `scoring/RUBRIC.md` (check version)
4. `TRACKER.md` (check counts)
5. `CLAUDE.md` (refresh project rules)

## What Was Delivered This Session

{List every chapter locked, book completed, skill created, review run,
rubric amendment adopted. Be specific — names, scores, commit hashes.}

## Key Decisions Made

{Architectural, editorial, scoring, or pipeline decisions. Why they
were made. What alternatives were considered.}

## Innovations Discovered

{List new innovations from this session with dimension and status.
Note any that crossed the 2+ threshold for amendment.}

## Current Metrics

| Metric | Value |
|--------|-------|
| Chapters locked | {N} |
| Complete books | {N} ({names}) |
| Regions with chapters | {N} / 26 |
| Peoples with chapters | {N} / 259 |
| Innovations | {N} ({N} adopted, {N} logged) |
| Rubric version | v{X.Y} |
| Mean score | {N} / 90 |
| Estimated words | {N} |

## Next Session Priorities

### Tier 1 (do first)
{What must happen next — blocking items, overdue reviews}

### Tier 2 (do if time)
{Growth work — new chapters, new books, new regions}

### Tier 3 (future)
{Strategic — scaling, completion targets, cross-compare}

## Open Questions

{Anything unresolved that the next session needs to address}
```

### Step 3: Update the Punchlist

Rewrite `agents/LUCY-PUNCHLIST.md` to reflect post-session state:
- Move completed items to the ✅ section
- Update 🔴 BLOCKING and 🟡 HIGH PRIORITY
- Update 🟢 NEXT SESSION CANDIDATES based on handoff priorities
- Update 📊 METRICS with current counts

### Step 4: Update the Roster

If new SCRIBE instances were spawned this session, add them to
`agents/AGENT-ROSTER.md` with culture, era, score, and status.

### Step 5: Innovation Threshold Check

Scan `scoring/INNOVATIONS.md` for any dimension with 2+ innovations
at status `logged`. If found, note in the handoff as a Tier 1 priority
for next session (propose rubric amendment).

### Step 6: Commit and Push

```bash
git add agents/ scoring/ TRACKER.md
git commit -m "Session {N} handoff — {1-line summary}"
git push
```

---

## Output

- `agents/LUCY-HANDOFF-S{N}.md` — comprehensive session handoff
- `agents/LUCY-PUNCHLIST.md` — updated for next session
- `agents/AGENT-ROSTER.md` — updated with session spawns
- All committed and pushed

## The Rule

No session ends without a handoff. LUCY goes through every gate —
including the last one.

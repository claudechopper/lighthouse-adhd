# Notion Template Spec — Lighthouse for ADHD

If you prefer Notion to Obsidian, build this. **One dashboard. Four databases. Stop.**

The slash commands work with Obsidian by default. To use Notion, replace file paths with the Notion MCP equivalent or manually paste outputs.

---

## The dashboard (one page, named "Lighthouse")

Top to bottom, in this order:

1. **PRIORITY (today)** — single-line callout, big text. Manually edited or filled by `/morning` output.
2. **▶ FIRST 15 MINUTES** — single line, biggest text on the page. The activation step.
3. **Convergence Bet widget** — link to the Convergence Bet page below.
4. **Today's micro-tasks** — embed of Tasks DB, filtered to `Status: Today` and `Date: today`.
5. **Energy today** — embed of Energy Ledger DB, filtered to today, grouped by hour, showing avg score.
6. **Inbox** — embed of Brain Dump DB, filtered to `Status: Unprocessed`, sorted newest first.

---

## Database 1 — Tasks

| Property | Type | Notes |
|----------|------|-------|
| Name | Title | The task |
| Status | Select | Today / Week / Someday / Done / Deleted |
| First-step | Checkbox | Is this THE first 15-min step? Max one true at a time. |
| Estimate | Select | 5min / 15min / 30min / hour+ |
| Created | Created time | Auto |
| Bet-aligned | Checkbox | Does this serve the convergence bet? |

**Default views:**
- "Today" — Status = Today, sorted by First-step DESC
- "This week" — Status = Today OR Week
- "Triage" — Status = empty

---

## Database 2 — Brain Dump

| Property | Type | Notes |
|----------|------|-------|
| Item | Title | What was captured |
| Status | Select | Unprocessed / Processed / Archived |
| Captured | Created time | Auto |
| Promoted to | Relation | Link to Tasks DB if promoted |

Sole purpose: capture surface. Don't add fields. Friction = silence.

---

## Database 3 — Projects

| Property | Type | Notes |
|----------|------|-------|
| Name | Title | Project name |
| Status | Select | Active / Paused / Done / Killed |
| Lane | Select | One of your obsession lanes (e.g. "vibecoding", "ADHD content", "VCU") |
| Bet-aligned | Checkbox | Serves current convergence bet? |
| Last touched | Last edited time | Auto |
| Notes | Text | Whatever |

**Quarterly review action:** any project not Bet-aligned and not touched in 30 days → set Status = Paused.

---

## Database 4 — Daily Log

| Property | Type | Notes |
|----------|------|-------|
| Date | Date | The day |
| Priority | Text | The one priority |
| Energy total | Number | Sum of today's energy entries |
| Reflection Q | Text | The /sync question |
| Reflection A | Text | The /sync answer |
| Bet-progress | Checkbox | Did today move the bet forward? |

**One row per day.** Created by `/morning`, completed by `/sync`.

---

## Database 5 (optional) — Energy Ledger

If you want it in Notion instead of Obsidian:

| Property | Type | Notes |
|----------|------|-------|
| Activity | Title | What you did |
| Score | Number | -3 to +3 |
| Time | Created time | Auto |
| Date | Formula | `formatDate(prop("Time"), "YYYY-MM-DD")` |

**Default view:** today only, grouped by hour, avg(Score) shown.

But honestly: a single Obsidian file per day is faster to write to than Notion. If you can split: keep ledger in Obsidian, everything else in Notion.

---

## What NOT to add

- ❌ Goals database — collapse goals into "Convergence Bet" page only
- ❌ Habits tracker — energy ledger replaces it
- ❌ Calendar embed — open Calendar app instead, this isn't a calendar
- ❌ "Areas of Life" hierarchy — just lanes on Projects
- ❌ Templates gallery — one template per database is the whole point
- ❌ Notion AI — use Claude Code commands instead. Notion AI is the dopamine trap version.

If you find yourself wanting to add one of these, that's customization-paralysis. 90-day freeze applies in Notion the same way it does in Obsidian.

# Lighthouse Vault

Your ADHD-AI operating system. The starter version. Open this folder in Obsidian and you're done with setup.

## Files

| File | Purpose |
|------|---------|
| `inbox.md` | The single capture surface. Always open. Brain-dump here, anytime. |
| `convergence-bet.md` | Your one quarterly bet. The "what am I building right now" answer. |
| `obsession-audit.md` | The 60-min audit that finds your multi-lane intersection. Run once. |
| `daily/<YYYY-MM-DD>.md` | Today's note. Auto-created by `/morning`. |
| `energy-ledger/<YYYY-MM-DD>.md` | Today's energy log. Auto-created by `/energy`. |

## The four daily commands

Run from the Claude Code CLI (already installed):

| Command | When | What it does |
|---------|------|--------------|
| `/morning` | Start of day | Reads inbox + energy + bet, writes today's priority + 3 micro-tasks + first 15-min step. |
| `/energy <-3..+3> <activity>` | Throughout day | Logs an energy entry. Takes 3 seconds. |
| `/brain-dump` | When inbox feels full | Triages inbox into today/week/someday/delete, picks ONE first-15-min step. |
| `/sync` | End of day | Reviews today, drafts tomorrow's priority, asks one reflection question. |
| `/resume` | After interruption | "What was I doing? What's the next step?" — re-entry without spiraling. |

## The 30-day starter loop

**Days 1–7:** Run `obsession-audit.md` once. Use `/morning` and `/sync` daily. Log energy whenever you remember.

**Days 8–21:** Energy ledger every day, no skipping. Resist customizing this vault.

**Days 22–30:** Paste 14 days of energy ledger files into Gemini (free tier, AI Studio). Ask it for patterns. Pick your convergence bet from the Obsession Audit + Energy patterns. Fill in `convergence-bet.md`.

## Rules

1. **30 min setup, 90-day freeze.** You are not allowed to customize this vault for 90 days. ADHD customization-paralysis is the #1 failure mode.
2. **One capture surface.** Don't add Notion or another notes app on top. One.
3. **The vault is for life, not code.** Keep coding tasks in your project repos. This is for goals, energy, reflection.
4. **Two plugins max.** If you add Obsidian plugins: Homepage (auto-opens `inbox.md` on launch) and Tasks (queries todos). That's it.
5. **No AI on Sunday.** One day a week without AI assistance. Skill-atrophy guard.

## When you fall off

You will. Goal isn't 365-day streaks; it's "back on track within 48 hours." When you fall off:

1. Don't journal about why. Just `/morning`.
2. Energy entry: where are you right now? `-2`? `+1`? Log it.
3. First 15 minutes. Go.

The system catches you. The system does not lecture.

# 🚨 Lighthouse — the ADHD-AI operating system

**An honest, research-grounded starter pack for ADHD generalists in the AI era.**
No superpower mythology. No course funnel. No SaaS lock-in. Five slash commands, one folder, 30-minute setup.

> _AI is a useful executive-function prosthetic, especially for divergent thinkers — but only if you build guards against it becoming your new doom-scroll._

**[→ Live landing page](https://lighthouse-adhd.up.railway.app)** · **[Read the research-backed plan (PDF)](ADHD-AI-Game-Plan.pdf)**

---

This folder is the buildable version of the game plan. Everything you need to run the Phase 0 + Phase 1 workflow is here.

## What's in the box

```
ADHD Workflow/
├── ADHD-AI-Game-Plan.pdf            # The full plan (research-grounded)
├── lighthouse-vault/                # Obsidian-ready vault
│   ├── README.md                    # Vault user guide
│   ├── inbox.md                     # Capture surface
│   ├── convergence-bet.md           # Quarterly bet tracker
│   ├── obsession-audit.md           # 60-min audit template
│   ├── daily/_template.md
│   └── energy-ledger/_template.md
├── notion-template-spec.md          # Notion alternative (build it yourself in Notion)
└── STARTER-PACK-README.md           # This file
```

And five new Claude Code slash commands installed at `~/.claude/commands/`:

- `/morning` — daily activation
- `/energy <-3..+3> <activity>` — quick energy log
- `/brain-dump` — triage inbox + pick first 15-min step
- `/sync` — end-of-day off-ramp
- `/resume` — post-interruption re-entry

## How to start (today)

1. **Open Obsidian.** Create a new vault by opening the `lighthouse-vault/` folder. (Or skip Obsidian and just use any text editor — the files are plain markdown.)
2. **Run the Obsession Audit.** Open `obsession-audit.md`. Spend 60 minutes filling it. Don't skip to the bet yet.
3. **Run `/morning` once.** Even with no data, it'll create today's daily note and you'll see how it works.
4. **Throughout today:** when you do anything, run `/energy <score> <what you did>`. Aim for 5+ entries.
5. **Tonight:** run `/sync`.

That's day 1. Repeat for 14 days before adding anything.

## When to pick the convergence bet

Day 22. Not before. You need:

- The Obsession Audit completed (day 1)
- 14 days of energy data
- A Gemini conversation pasting the 14 days, asking for patterns

Then fill in `convergence-bet.md`.

## What this is NOT

- ❌ Not a productivity app to admire
- ❌ Not a Notion template gallery
- ❌ Not the "complete life OS"
- ❌ Not a replacement for medication, therapy, or human support
- ❌ Not Nik's $-paid course (this is the open-source version of the framework)

## What this IS

- ✅ The minimum viable system to run the game plan
- ✅ Brutal-simple by design (the customization-paralysis guard)
- ✅ AI-native but with anti-trap rules (no infinite chats, no slot-machine prompts)
- ✅ Yours to fork, edit, share

## Next steps after 90 days of running this

If you've run this for 90 days and want to go further:

1. **Build the Anti-trap layer** — focus-block timer with hyperfocus cap, customization-detector, AI-usage meter. (Phase 2 of the plan.)
2. **Ship one public artifact a week.** From the convergence bet. Tweet, video, prototype, post.
3. **Consider the Electron app version.** If demand exists, the standalone product is real.

## License

Use it. Fork it. Steal the ideas. The framework belongs to anyone who needs it.

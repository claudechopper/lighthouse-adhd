from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
)
from reportlab.lib.enums import TA_LEFT

OUTPUT = "/Users/Claude/ADHD/ADHD Workflow/ADHD-AI-Game-Plan.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=0.75 * inch,
    rightMargin=0.75 * inch,
    topMargin=0.75 * inch,
    bottomMargin=0.75 * inch,
    title="The ADHD + AI Game Plan",
    author="Synthesized for Claudechopper",
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleBig", parent=styles["Title"],
    fontSize=22, leading=26, spaceAfter=6,
    textColor=HexColor("#1a1a1a"),
)
subtitle_style = ParagraphStyle(
    "Subtitle", parent=styles["Normal"],
    fontSize=11, leading=14, spaceAfter=18,
    textColor=HexColor("#555555"), italic=True,
)
h1 = ParagraphStyle(
    "H1", parent=styles["Heading1"],
    fontSize=15, leading=19, spaceBefore=18, spaceAfter=8,
    textColor=HexColor("#0b3d91"),
)
h2 = ParagraphStyle(
    "H2", parent=styles["Heading2"],
    fontSize=12.5, leading=16, spaceBefore=12, spaceAfter=6,
    textColor=HexColor("#1a1a1a"),
)
body = ParagraphStyle(
    "Body", parent=styles["Normal"],
    fontSize=10.5, leading=15, spaceAfter=8, alignment=TA_LEFT,
)
small = ParagraphStyle(
    "Small", parent=styles["Normal"],
    fontSize=9.5, leading=13, spaceAfter=6,
    textColor=HexColor("#444444"),
)
mono = ParagraphStyle(
    "Mono", parent=styles["Code"],
    fontSize=9, leading=12, spaceAfter=10,
    backColor=HexColor("#f4f4f4"),
    borderPadding=8, leftIndent=6, rightIndent=6,
)


def P(text, style=body):
    return Paragraph(text, style)


def bullets(items, style=body):
    return ListFlowable(
        [ListItem(Paragraph(t, style), leftIndent=12) for t in items],
        bulletType="bullet", start="•", leftIndent=14, bulletFontSize=9,
    )


story = []

story.append(P("The ADHD + AI Game Plan", title_style))
story.append(P("Research-grounded, not vibes — built around Claude Code, Codex, Gemini, Obsidian, Notion", subtitle_style))

story.append(P("Part 1 — What Nik (ADHDVision) got right vs. wrong", h1))
story.append(P(
    "Nik Hobrecker (German, diagnosed at 19) runs ADHDVision and sells a 17-episode paid course "
    "called <i>From Distraction to Success</i> — that's the &ldquo;execution system&rdquo; he teases at the end. "
    "It's monetized; Trustpilot is mostly positive but the recurring critique is heavy monetization."))
story.append(P("Where he's right (cite confidently):", h2))
story.append(bullets([
    "<b>METR's task-length doubling is real and accelerated.</b> Their Jan 2026 update revised the post-2023 doubling time to ~4.3 months (130.8 days).",
    "<b>Palantir CEO Alex Karp did say it</b> (TBPN podcast, March 2026). Real quote.",
    "<b>Dodson's interest-based nervous system</b> is the legit clinical model under his &ldquo;follow interest&rdquo; rule. ADHD brains run on <b>PINCH</b> — Passion, Interest, Novelty, Competition, Hurry — not importance/consequence/reward.",
]))
story.append(P("Where he overshoots or misleads:", h2))
story.append(bullets([
    "<b>The 88% stat</b> is an EY/Microsoft survey, n=300, testing Microsoft Copilot. Vendor-flavored. Cite as &ldquo;EY/Microsoft survey of 300,&rdquo; not &ldquo;research shows.&rdquo;",
    "<b>Karp's quote has TWO arms</b> — vocational training AND neurodivergence. Nik dropped the trades half.",
    "<b>Gutenberg / Steve Jobs / Wright brothers as ADHD generalists</b> is posthumous diagnosis-by-vibes. Inspirational rhetoric, not history.",
    "<b>&ldquo;ADHD = superpower&rdquo;</b> is what clinicians and ADDitude flag as toxic positivity — correlated with people asking for fewer accommodations and burning out harder.",
    "<b>AI is not removing the executive function tax.</b> Barkley's model: ADHD is an EF deficit, not a tax. AI externalizes some EF work. It cannot regulate emotion, inhibit Twitter impulses, or remember meds.",
    "<b>Biggest blind spot:</b> AI is a near-perfect ADHD dopamine trap. Novelty + variable reward + no closure is the gambling-research formula. You're at heightened risk of AI dependency, not lower.",
]))
story.append(P(
    "<b>Honest one-line version:</b> <i>AI is a useful executive-function prosthetic, especially for divergent thinkers — "
    "but only if you build guards against it becoming your new doom-scroll.</i>"))

story.append(P("Part 2 — How ADHD brains actually work", h1))
story.append(bullets([
    "<b>Motivation is interest-based, not importance-based</b> (Dodson). &ldquo;Should&rdquo; doesn't work. PINCH does. Design your day around PINCH triggers — biggest single unlock.",
    "<b>EF is a deficit, not a tax.</b> You will not &ldquo;remove&rdquo; it with AI. You will <i>externalize</i> parts of it onto systems that must be boring, simple, and load-bearing — not exciting.",
    "<b>Hyperfocus is real but unpredictable</b> (~68% of ADHDers report it; Cambridge 2025). Boosts ~30%; destroys sleep/relationships when uncontrolled. Plan FOR it; don't plan ON it.",
]))

story.append(P("Part 3 — Goal discovery: the multi-lane intersection", h1))

story.append(P("Step 1 — The Obsession Audit (60 min, one sitting)", h2))
story.append(P(
    "Open one Obsidian note: <font face='Courier'>obsession-audit.md</font>. Brain-dump everything you've gone deep on in the last 10 years — "
    "hobbies, rabbit holes, side projects, abandoned phases. Aim for 20+ items. No filtering."))
story.append(P("Then tag each:"))
story.append(bullets([
    "🔥 still alive (would re-engage today)",
    "💀 dead (already solved the puzzle)",
    "💰 someone pays for this somewhere",
    "🧠 you're good at it without trying",
    "🎓 you taught yourself this",
]))
story.append(P(
    "The intersection of 🔥 + 💰 + 🧠 is your <b>multi-lane convergence zone.</b> Usually 2–4 items. "
    "The Gutenberg move is connecting 2 of them, not picking one."))

story.append(P("Step 2 — The Energy Ledger (14 days, no skipping)", h2))
story.append(P("Daily Obsidian note <font face='Courier'>energy-ledger/YYYY-MM-DD.md</font> with three columns: Time | What I did | Energy after (-3 to +3)."))
story.append(P("After 14 days, paste all entries into Gemini (free tier, 1M context):"))
story.append(P(
    "<i>&ldquo;Find patterns. What 3 activity types consistently produced +2 or +3? What 3 produced -2 or -3? "
    "What time of day does my energy peak? What's the pattern around the high-energy days?&rdquo;</i>", small))

story.append(P("Step 3 — The Consume → Create Rule", h2))
story.append(P(
    "Going down rabbit holes is not the problem. Pure consumption is. Rule: every rabbit hole exits with one artifact within 7 days:"))
story.append(bullets([
    "A 200-word note in Obsidian linking it to existing notes",
    "A tweet/post/short",
    "A 30-minute prototype (vibe-coded, throwaway is fine)",
]))

story.append(P("Step 4 — The Convergence Bet", h2))
story.append(P(
    "Pick ONE intersection of 2 lanes. Commit to one quarter of building output that lives at that intersection. "
    "Not forever — a quarter. ADHD brains can't do &ldquo;forever,&rdquo; but they can do &ldquo;until July.&rdquo;"))

story.append(PageBreak())

story.append(P("Part 4 — The daily execution stack", h1))

story.append(P("Layer 1 — Capture (pick ONE, not both)", h2))
story.append(bullets([
    "<b>Obsidian:</b> Daily note template, two plugins max (Homepage + Tasks), <font face='Courier'>inbox.md</font> always open. 30 min setup. 90-day freeze.",
    "<b>Notion:</b> One dashboard, four databases max — Tasks / Brain Dump / Projects / Daily Log. Skip every &ldquo;Complete Life OS&rdquo; influencer template.",
]))
story.append(P("Job of this layer: catch the thought before it evaporates. No processing happens here.", small))

story.append(P("Layer 2 — Processing (Claude Code is the workhorse)", h2))
story.append(P("Once a day (NOT continuously), run a <font face='Courier'>/morning</font> slash command that:"))
story.append(bullets([
    "Reads <font face='Courier'>inbox.md</font> (or Notion brain-dump DB via MCP)",
    "Buckets each item: today / this-week / someday / delete",
    "Picks 1 &ldquo;first 15 minutes&rdquo; task — the smallest possible step",
    "Updates today's daily note",
]))
story.append(P(
    "Reference Kai's pattern: <font face='Courier'>CLAUDE.md</font> for personal context, <font face='Courier'>.claude/rules/</font> for doctrine, "
    "slash commands for activation. You already have a VCA system — extend it for life-OS, don't rebuild it. "
    "Pair with <font face='Courier'>/sync</font> (end-of-day) and <font face='Courier'>/resume</font> (post-interruption killer command)."))

story.append(P("Layer 3 — Heavy thinking (Gemini in AI Studio)", h2))
story.append(P("1M+ context is the ADHD killer feature. Use for:"))
story.append(bullets([
    "Energy ledger pattern analysis (paste 14 days, ask for patterns)",
    "&ldquo;Re-explain my project to me&rdquo; after a 3-week absence (paste full Obsidian folder)",
    "Cheap prototyping before burning Claude tokens (voice-plan ChatGPT → prototype Gemini → build Claude Code)",
]))

story.append(P("Layer 4 — Code & build (Claude Code primary, Codex backup)", h2))
story.append(P(
    "Your existing Claude Code stack is the right primary. Codex only if: you're already on the OpenAI stack and don't want a second subscription, "
    "or you want a parallel runner. Don't run both for ADHD reasons — context switching kills you. "
    "Leaf vs. trunk rule still applies: vibe-code aggressively on leaves, slow down on trunk."))

story.append(P("Layer 5 — Activation (the underrated piece)", h2))
story.append(bullets([
    "<b>A <font face='Courier'>/morning</font> slash command</b> that picks the next 15-min step. Doing requires zero decisions.",
    "<b>Body doubling.</b> Focusmate, ADHDVision focus calls, or a Discord call on mute. Real, evidence-supported, ~$5/session.",
    "<b>PINCH design.</b> Add an artificial constraint to boring tasks — a 25-min timer (Hurry), a public commit by 5pm (Competition + Hurry), or pair with someone (Competition).",
]))

story.append(P("Part 5 — The daily loop", h1))
loop = """06:00 — Brain dump straight to Obsidian inbox.md (5 min, no editing)
06:30 — Run /morning in Claude Code → 1 priority + 3 micro-tasks
07:00 — Energy ledger entry from yesterday
        First 15-min task — START before checking anything else
07:30 — Open work block. Hyperfocus permitted but timer-bounded (45 min).
        Every 45 min: stand up, drink water, log what you just did.
12:00 — Lunch. NO AI during lunch (skill atrophy guard).
13:00 — Second work block. Different lane than morning if energy is dipping.
17:00 — Run /sync — Claude reads today's daily note, drafts tomorrow's
        priorities, asks 1 reflection question.
19:00 — Energy ledger close-out. -3 to +3 for the day. Done.

Once/week (Sunday 30 min):
  - Energy ledger pattern check (Gemini)
  - Inbox triage (anything older than 7 days dies or ships as artifact)
  - Convergence-bet status: still alive? pivoting? dead?"""
story.append(Paragraph(loop.replace("\n", "<br/>").replace("  ", "&nbsp;&nbsp;"), mono))
story.append(P("Whole loop runs under 30 minutes of system work per day. If yours takes longer, you're in customization-paralysis.", small))

story.append(PageBreak())

story.append(P("Part 6 — The four ADHD+AI failure modes", h1))
story.append(bullets([
    "<b>Customization paralysis.</b> Spending weeks tuning Obsidian/Notion/CLAUDE.md instead of using them. <b>Guard:</b> 30-min setup, 90-day freeze. After 90 days, max one tweak per week.",
    "<b>Idea-generation loop.</b> AI produces options forever; you never ship. <b>Guard:</b> &ldquo;Two options max&rdquo; rule when prompting. After two, you commit.",
    "<b>Dopamine slot machine.</b> AI conversations as variable-reward novelty. <b>Guard:</b> AI is a tool, not a companion. No &ldquo;let's chat&rdquo; sessions. Every prompt has an output spec.",
    "<b>Skill atrophy.</b> 2025 study showed reduced brain engagement across 32 regions in heavy ChatGPT users. <b>Guard:</b> one &ldquo;manual day&rdquo; per week — write/debug/plan without AI.",
]))
story.append(P(
    "<b>Fifth, specific to you:</b> VCA recursion. You already have a sophisticated tool-stack (VCA, sheets, slash commands). "
    "Resist building the ADHD layer as more VCA infrastructure. The ADHD layer is for your <i>life</i>, not your code projects. "
    "Keep them separate vaults / separate Notion workspaces / separate <font face='Courier'>.claude/commands/</font> namespaces."))

story.append(P("Part 7 — The 30 / 60 / 90 starter", h1))

story.append(P("Days 1–7", h2))
story.append(bullets([
    "Obsession Audit (one sitting)",
    "Pick capture surface (Obsidian or Notion). 30 min setup. Stop.",
    "Build <font face='Courier'>/morning</font> and <font face='Courier'>/sync</font> slash commands. That's it.",
]))

story.append(P("Days 8–21", h2))
story.append(bullets([
    "Run the daily loop. Just run it. Resist customizing.",
    "Energy ledger every day, no skipping.",
]))

story.append(P("Days 22–30", h2))
story.append(bullets([
    "Day-22 review with Gemini on energy data.",
    "Pick your convergence bet (1 intersection, 1 quarter).",
    "Commit to one output artifact per week from that intersection.",
]))

story.append(P("Days 31–60", h2))
story.append(bullets([
    "Ship one public-facing artifact per week. Tweet, video, prototype, blog post, anything.",
    "Add <font face='Courier'>/resume</font> slash command if you've felt the post-interruption pain.",
]))

story.append(P("Days 61–90", h2))
story.append(bullets([
    "Review: what's still alive in the system? Cut ruthlessly.",
    "ADHD-proof systems are the ones you've been USING for 90 days, not the ones you set up beautifully.",
]))

story.append(P("The honest bottom line", h1))
story.append(P(
    "Nik's transcript sells you on a feeling: <i>you're not broken, you're a generalist who can finally win.</i> "
    "That feeling is partly true and partly a course-funnel. The research-grounded version is less flattering but more useful:"))
story.append(bullets([
    "Your brain runs on PINCH, not should",
    "AI is the best EF prosthetic in history AND the best ADHD trap in history — same features, opposite outcomes, depending on guards",
    "Generalist intersections are real leverage, but only if you ship artifacts not just consume rabbit holes",
    "The system that works is the boring simple one you actually run, not the elegant one you keep tuning",
]))
story.append(P("You already have the tools. The game is using them on your <b>life</b> the way you've been using them on your code.", body))

story.append(P("Top sources", h1))
story.append(bullets([
    "METR Time Horizon 1.1 — metr.org/blog/2026-1-29-time-horizon-1-1/",
    "Russell Barkley EF fact sheet — russellbarkley.org/factsheets/ADHD_EF_and_SR.pdf",
    "Dodson interest-based nervous system — neurodivergentinsights.com/interest-based-nervous-system/",
    "Kai's &ldquo;Claude Code as Executive Function&rdquo; — dev.to/kai_outputs/claude-code-as-executive-function-my-adhd-brain-setup-1412",
    "ADDitude on ADHD-superpower toxic positivity — additudemag.com/what-is-your-greatest-strength-adhd-superpowers-toxic-positivity/",
    "ADD Resource Center, AI + ADHD double-edged sword — addrc.org/ai-and-adhd-a-double-edged-sword-that-could-make-or-break-your-focus/",
    "ravila4/claude-adhd-skills repo — github.com/ravila4/claude-adhd-skills",
], small))

doc.build(story)
print(f"Wrote: {OUTPUT}")

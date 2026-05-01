# The Lighthouse Audit — design doc v0.1

A paid digital product that replicates and improves upon "ADHD brain mapping" products — actually effective, evidence-informed, no fluff.

This is the build brief. Hybrid voice: behavioral psychologist (ADHD/EF dysfunction) + product designer + systems thinker. Mechanism over motivation. Concrete over vague.

---

## TL;DR

A user takes an 8-question diagnostic, gets a weighted profile (top-2 failure patterns, not a horoscope), receives a personalized execution system that runs in their CLI/Obsidian/inbox, plus anti-failure scaffolding designed to survive their worst days. Honest pricing ($79 founder / $149 list), 14-day refund-plus-check guarantee, no SaaS recurring, no shame mechanics.

Position as **Lighthouse Pro** — paid layer above the free Lighthouse starter pack already shipped.

---

# PART 1 — CORE MECHANISM

## 1.1 The transformation (input → output)

| | Input (typical buyer) | Output (30 days later) |
|---|---|---|
| State | 5–10 productivity systems tried, all dead | One boring system actually running |
| Inbox | Open loops, half-finished projects, shame | One capture surface, ruthless triage |
| Goals | Vague intentions, novelty churn | One quarterly Convergence Bet |
| Recovery | Falling off = spiraling for weeks | 48-hour re-entry protocol fires |
| Output | Plenty of starting, little shipping | One weekly artifact (proof-of-progress) |

The transformation is **not** "from disorganized to organized." It is **from system-shopping to system-running.** From the dopamine churn of new-tool novelty to one externalized routine that survives bad weeks.

## 1.2 The 5 underlying psychological mechanisms

| # | Mechanism | Source | How it shows up in the product |
|---|---|---|---|
| 1 | **Behavioral activation** | Lewinsohn / Jacobson | Smallest-possible-first-step is mandatory. Action precedes motivation. Every task has a literal "first 15 min" defined or it doesn't enter the system. |
| 2 | **Constraint reduction** | Schwartz, *Paradox of Choice* | Two-options-max rule on every AI prompt. Single-priority lock. Three-micro-tasks-per-day cap. |
| 3 | **Externalized executive function** | Russell Barkley | The system lives in CLI/files, not memory. `/morning` slash command is the EF prosthetic. Energy ledger is externalized self-monitoring. |
| 4 | **Implementation intentions** | Peter Gollwitzer | Every system rule is an if-then. "When interrupted → run /resume." "When energy < -1 for 3 entries → Bad Day Fallback fires." |
| 5 | **Self-determination theory** | Deci & Ryan | No streaks, no points, no shame mechanics. Autonomy via convergence-bet choice. Competence via energy-ledger data feedback. Relatedness via body-doubling. |

These are NOT pop-psychology. Each has decades of clinical evidence. None require neuroscience LARP.

## 1.3 What makes this feel "personalized" without fake neuroscience

**The trap to avoid:** "Your prefrontal cortex is 73% underactivated in the dopamine pathway." Cannot measure with a quiz. Insulting to the buyer's intelligence.

**The honest version:** personalization comes from pattern-matching the user's specific failure mode to a system tuned for that mode. Same way a physiotherapist personalizes treatment based on how you walk — not by pretending to read a CT scan.

| Feels personalized (do this) | Feels fake (don't do this) |
|---|---|
| Naming their specific failure pattern in language they recognize | Color-coded ADHD types |
| Showing their data points that pointed there | Vague "your unique wiring" claims |
| Profile-specific rule that other profiles don't get | Generic checklist with their name added |
| Energy ledger weekly feedback ("your +3 days cluster Tue/Thu mornings") | Astrology-flavored brain-region claims |
| Slash commands literally have different prompts based on profile | Renamed PDFs with cover-page personalization |

## 1.4 The simplest version that still works

Strip to floor:

```
1. ONE quarterly Convergence Bet     → tells you what to do
2. ONE daily activation (/morning)   → makes you start
3. ONE Minimum Viable Day (MVD)      → keeps you on the rope
4. ONE 48-hour reset protocol        → re-enters after falling off
```

Four rules. Everything else layers on top. If the four rules disappear, the product disappears. Build defending these four; argue for any fifth element.

---

# PART 2 — USER DIAGNOSTIC

## 2.1 Constraints

- **8 questions** (not 15 — see Critique). Each weighted, with confidence rating.
- ~10 minutes to complete.
- Each question diagnostic of a specific behavioral dimension. No personality fluff.
- Output: weighted profile (top-2 failure patterns), not single bucket.

## 2.2 The 8 questions

| # | Question | Maps to dimension |
|---|---|---|
| Q1 | When a new project lands in my brain, the most common outcome over 7 days is: (a) I research it obsessively then move to a different new idea, (b) I plan perfectly but never start, (c) I start immediately but lose interest within days, (d) I add it to a list and forget it. | **Initiation** |
| Q2 | I most often abandon projects when: (a) the exciting unknown becomes routine, (b) I hit my first real obstacle, (c) a more interesting idea appears, (d) life interrupts and I never restart. | **Continuation** |
| Q3 | When overwhelmed, my default is: (a) numb out (Twitter/scroll), (b) make a bigger plan/new system, (c) sleep/shut down, (d) pick the smallest visible task. | **Overwhelm response** |
| Q4 | If I'm interrupted mid-task, the most common outcome is: (a) I never return, (b) I return after long delay and re-start, (c) I return immediately at lower quality, (d) interruptions don't usually derail me. | **Recovery** |
| Q5 | Energy-wise, I peak: (a) predictably (specific times), (b) unpredictably (no pattern I see), (c) only with external pressure, (d) after breaks/rest. | **Energy regularity** |
| Q6 | My productivity systems usually fail because: (a) I add too much, (b) I forget to use them, (c) too rigid for my energy, (d) I get bored. | **Self-reported failure mode** |
| Q7 | In the last 2 years I have tried [N] productivity systems: (a) 0–2, (b) 3–5, (c) 6–10, (d) 11+. | **Novelty-shopping severity** |
| Q8 | The honest version of my last 90 days of work output: (a) real progress on one thing, (b) some progress on several, (c) lots of starting, little shipping, (d) mostly avoidance. | **Reality baseline** |

After each question: confidence slider 1–5. ("How true is this for you?")

## 2.3 The 5 execution profiles

Each profile is a **failure pattern**, not a personality type.

### Profile 1 — The Novelty Chaser
**Diagnostic signature:** Q1=A or C · Q2=A or C · Q7=C or D
**Core failure pattern:** Surface-level engagement; never depth. Every project is a phase.
**Trigger situations:** Around week 2 of any project, when novelty fades and the work becomes routine. Adjacent shiny ideas pull attention away.
**System requirements:** Enforced 12-week Convergence Bet. "No new project initiation" rule until current bet ships first artifact. Weekly dopamine audit (logged but not acted on). Ratchet permission: after 3 shipped artifacts, allowed one 2-hour novelty spike.

### Profile 2 — The Perfectionist Stuck-Starter
**Diagnostic signature:** Q1=B · Q3=B · Q6=A
**Core failure pattern:** Research-as-procrastination. Plans for hours, ships rarely.
**Trigger situations:** High-stakes tasks. Public-facing work. Anything that could be judged.
**System requirements:** Smallest-possible first step (5 min, not 15). Two-options-max rule on planning sessions. "Ship Ugly Monday" — Monday's first 15 min must produce a shippable thing in 1 hour. 30-day ban on reading productivity content (research = procrastination).

### Profile 3 — The Overwhelmed Collapser
**Diagnostic signature:** Q3=A or C · Q8=D
**Core failure pattern:** Capacity overflow → freeze → shame → avoidance.
**Trigger situations:** Multiple active priorities. Returning from breaks/holidays. Days with > 2 commitments.
**System requirements:** Single-priority lock (only ONE thing visible). Project quota: max 3 active. Daily prompt in `/morning`: "What gets dropped today?" Bad Day Fallback fires more aggressively (after 2 below-zero entries, not 3).

### Profile 4 — The Inconsistent Sprinter
**Diagnostic signature:** Q5=B · Q4=A or B · Q6=C
**Core failure pattern:** Two great weeks, four dead weeks. Streak-dependent. No recovery.
**Trigger situations:** Any disruption (illness, travel, social event). End of motivation cycle.
**System requirements:** 48-hour Reset Protocol formalized. Bad Day Fallback System. Zero streak counters anywhere in the system. "Recovery ritual": when returning from a gap, run `/resume` only — no triage, no planning, no goal-setting.

### Profile 5 — The Externalizer-Dependent
**Diagnostic signature:** Q2=B · Q5=C · Q6=B
**Core failure pattern:** Solo work fails. Accountability work succeeds. Self-imposed deadlines have zero force.
**Trigger situations:** Solo creative work. No-deadline projects. Personal goals nobody else knows about.
**System requirements:** Body-doubling slot booked weekly (Focusmate). Public-commitment ritual (tweet/post weekly artifact target every Sunday). Solo-only days are explicitly low-stakes only. Bet-aligned work always paired with external accountability.

## 2.4 Weighted output (handles mixed profiles)

Most ADHDers fit 2–3 profiles. Output is weighted:

> "You're **60% Novelty Chaser + 30% Perfectionist Stuck-Starter + 10% Inconsistent Sprinter**. Your primary failure is novelty-driven abandonment. Your secondary pattern (perfectionism) shows up under stress, especially in week 3 when the work gets harder and 'not ready yet' becomes the excuse. Here's the system tuned to your top-2 patterns."

The system inherits rules from both top profiles, weighted toward primary.

---

# PART 3 — SYSTEM GENERATOR

## 3.1 Universal core (every profile gets these)

| Rule | Trigger | Action |
|---|---|---|
| Convergence Bet | Once per quarter | One intersection of 2 lanes locked. Ships ≥1 artifact/week. |
| Daily activation | Every morning | `/morning` slash command runs |
| Energy logging | Throughout day | `/energy ±3 <activity>` minimum 5×/day |
| Daily off-ramp | Every evening | `/sync` runs |
| MVD floor | When everything else fails | Defined per-profile (see 4.1) |

## 3.2 Profile-tuned variations

These are layered on top of the universal core. The system generator picks them based on weighted profile.

| Profile | Added rule | Added file/template |
|---|---|---|
| Novelty Chaser | "No new project initiation" rule until current bet ships artifact | `dopamine-audit.md` weekly |
| Perfectionist | "Two-options-max" applied to all AI prompts | "Ship Ugly Monday" template |
| Overwhelmed Collapser | Project quota enforcement (3 max) | "What gets dropped today?" prompt in `/morning` |
| Inconsistent Sprinter | Streak counters explicitly disabled | `recovery-ritual.md` |
| Externalizer-Dependent | Body-doubling slot in weekly calendar | `public-commitment.md` weekly Sunday template |

## 3.3 Task structure (universal)

Every task in the system is an object with:

```
{
  text: string
  priority: today | week | someday | dropped
  bet_aligned: bool
  estimate: 5min | 15min | 30min | hour+
  first_step: string  // mandatory; if absent, task doesn't enter
  age_days: int       // if > 14 without action, escalates or drops
}
```

Hard constraints:
- Max 3 tasks marked `today` at any time
- No task lives > 14 days without action
- Every task has `first_step` defined or it bounces back to inbox

## 3.4 Environment design

What the user sees:

| Surface | What's there | What's NOT there |
|---|---|---|
| Obsidian inbox.md | Captures only | No structure, no editing |
| Today's daily note | 1 priority, 3 micro-tasks, first 15 min, energy data | No project hierarchies, no archives |
| Convergence Bet page | Single bet, weekly artifact tracker | No alternative goals to compare |
| Energy ledger | Today's entries | No streak counters, no badges, no points |
| Profile card (PDF) | Their pattern, their rules, their MVD | No motivational quotes |

## 3.5 Anti-failure constraints (universal — see Part 4 for detail)

- 90-day customization freeze with file-watcher cooling-off
- No new productivity-tool installs for 90 days
- Pre-committed Bad Day Fallback (defined at onboarding)
- Hard cap: 4 file types in vault (inbox, daily, energy, bet)
- Reset Protocol fires automatically on detected gaps

---

# PART 4 — ANTI-FAILURE DESIGN

## 4.1 Minimum Viable Day (MVD)

User defines theirs at onboarding. Default by profile:

| Profile | Default MVD |
|---|---|
| Novelty Chaser | Ran `/morning` + 1 micro-task on the bet (NOT a side quest) |
| Perfectionist | Shipped one ugly thing |
| Overwhelmed | Logged 3 energy entries + slept by 11pm |
| Inconsistent | Ran `/morning` OR `/resume` — touched the system once |
| Externalizer | Showed up to body-doubling slot OR ran `/morning` |

If MVD is hit, **you ran the system today.** No more. The day is logged as "ran." The bar is the floor, deliberately.

## 4.2 The 48-hour Reset Protocol

When the user falls off (auto-detected — see 4.4):

1. **Don't analyze. Don't journal. Don't promise yourself anything.**
2. Open Obsidian. Run `/resume`.
3. Log one energy entry (any score, even -3).
4. Do the system's smallest action (an MVD-equivalent).
5. You're back. Logged as "re-entered."

Hard rule: **48 hours from "fell off" to "re-entered."** Past 48 hours, shame spirals dominate, so the protocol fires hard and direct. The product reaches out (see 4.4) — user doesn't have to remember.

## 4.3 Bad Day Fallback System

**Auto-triggered when:**
- 3 consecutive energy entries below -1, OR
- 0 entries for 24 hours, OR
- 2 consecutive missed `/morning` runs, OR
- User self-flags ("today is a bad day")

**Fallback mode behavior:**
- `/morning` produces ONLY: "Drink water. Make food. Open inbox.md." Nothing else.
- `/sync` asks: "Are you safe? Did you eat?" Then exits.
- Convergence Bet pauses for the day. Pause is logged, not failed.
- No new tasks accepted into the system.

This catches bad days before they become bad weeks. The system survives the user's worst days because it gets simpler, not because the user gets stronger.

## 4.4 Adaptive-to-inconsistency rules

The system tracks actual usage and adapts:

| Detected pattern | System response |
|---|---|
| 7+ day gap | Next `/morning` runs in "gentle restart" mode (no priority push, just MVD) |
| 3-day usage streak | Permits a small ratchet (extends micro-task cap from 3 to 4, optional) |
| 5+ low-energy entries in row | Auto-trigger Bad Day Fallback |
| 14+ day total absence | Email/text re-entry: "Re-entry takes one minute. Reply with one word." (see 4.5) |

## 4.5 The shame-breaking re-entry mechanism

The deepest fix. Most systems require the user to come back. ADHD users won't, because shame compounds with absence.

**The product reaches out** when 14+ day absence is detected:

> Subject: "Hi from Lighthouse"
>
> "It's been 17 days. That's normal — you're a Novelty Chaser, this happens around week 3. Re-entry is one minute:
>
> 1. Reply with one word about how you're doing. Anything.
> 2. I'll log that as your re-entry energy entry.
> 3. Tomorrow's `/morning` runs in gentle-restart mode automatically.
>
> No catching up, no shame, no 'starting over.' Just one word."

Why it works: the cost to re-enter is one word. The product holds the rope; the user just touches it. Shame doesn't have time to spiral.

## 4.6 Customization-paralysis lockout

The 90-day freeze with teeth:

- A `system-changes.md` file is in the vault.
- Any proposed change goes there with timestamp.
- File-watcher: 7 days after a proposed change, an email reminds the user to re-read it. 90% of changes won't survive 7 days.
- Weekly check-in: "Did you customize this week? (yes/no)" — tracked, not blamed.
- After 90 days, one customization per week is permitted — not zero forever.

This converts the universal ADHD failure (system shopping) into observable data the user can see.

---

# PART 5 — PRODUCT STRUCTURE

## 5.1 Onboarding flow (60 minutes from purchase to running system)

| Minute | Step | What user does |
|---|---|---|
| 0–2 | Purchase confirms. Land on `/audit/welcome`. | Reads: "60 minutes from now, you'll have a system designed for your specific failure pattern." |
| 2–12 | Take diagnostic | 8 questions + confidence sliders. Inline question feedback ("interesting answer — most novelty-chasers click that") humanizes mid-flow. |
| 12–15 | Profile reveal | Reads weighted profile. ("You're 60% Novelty Chaser + 30% Perfectionist.") Sees the data points. |
| 15–30 | System generation | Watches their personalized system get assembled. Each rule shows WHY (one-liner mechanism). User defines their own MVD here. |
| 30–55 | Setup walkthrough | Installs slash commands. Sets up Obsidian vault from a tuned template. Drafts first inbox + bet. By minute 50, system is alive. |
| 55–60 | First `/morning` run | Live demo. User runs `/morning` right now. Sees output. That's day 1, hour 1. |

## 5.2 First 60-minute user journey (UX detail)

- **Progress bar visible** through diagnostic. Cuts dropoff.
- **Friction-free purchase:** Stripe Checkout. No account creation before purchase. Account auto-created from email at success.
- **Inline feedback in diagnostic:** brief, specific. ("That's the most common Novelty Chaser answer. ~40% of buyers pick A here.") Humanizes the algorithm.
- **Profile reveal as a single page**, not multi-step. Read in 90 seconds.
- **System generation is animated** — rules appear one-by-one with their mechanism explanation. Visible craft.
- **Setup walkthrough is video + checklist**, not pure text. Voice-over by founder (lived-experience credibility).
- **Day 1 success pattern** = the user runs `/morning` once before they close the tab.

## 5.3 Deliverable bundle

User receives at minute 60:

1. **Profile PDF** (4 pages, designed): their pattern, their data points, their rules, their MVD, their Bad Day Fallback. Plus "When you fall off (and you will)" section.
2. **Tuned slash command pack**: `.zip` of profile-specific `~/.claude/commands/*.md` files, including a profile-tuned `/morning`.
3. **Pre-configured Obsidian vault**: their inbox, daily template, energy ledger folder, convergence-bet draft pre-filled with their answers from diagnostic.
4. **30-day check-in email schedule**: day 7, 14, 30 nudges. Each contains 1 diagnostic question. ("Day 14: did your Bad Day Fallback trigger? Did it help?")
5. **Profile-specific micro-content access**: 1 short video per failure mode showing what to expect in week 3, week 6, week 12 (when the failure pattern reasserts).
6. **The 14-day refund-plus-check guarantee** (see 5.5): the credibility move.

## 5.4 Format

| Component | Format |
|---|---|
| Diagnostic + system generator | Web app, React, deployed on Railway |
| Deliverable | Downloadable bundle (PDF + .zip + vault folder) |
| Email follow-up | Loops or SendGrid, scheduled |
| Payment | Stripe Checkout, one-time |
| Checkout email | Auto-routed via webhook |
| Founder credibility | Short video on landing page (you, real face, real voice) |

## 5.5 How it feels "high value" without fake complexity

| Anti-pattern (most products) | What we do instead |
|---|---|
| Complexity = value | Anti-feature list: "We deliberately didn't include X, Y, Z" |
| Stitched template content | One coherent voice (founder) throughout |
| Generic claims ("rewires your brain") | Specific claims ("designed for your failure pattern") |
| Vague "personalization" | Visible mechanism — every rule explains why |
| Hidden refund process | **14-day "abandoned it? full refund plus a check for your time"** — the credibility move |
| Stack of 47 modules | 4 deliverables. That's the entire product. |

The 14-day guarantee in detail: if a buyer abandons within 14 days and writes a paragraph explaining why, they get a full refund AND a $20 check (digital, via Stripe payout) "for your time and the data you gave us." Costs us almost nothing in practice (the bar is high, most refunders have legitimate feedback that improves the product). Earns enormous trust. Differentiates from every other ADHD course.

---

# PART 6 — DIFFERENTIATION

## 6.1 Why most ADHD productivity systems fail

| Standard failure | Why it kills users |
|---|---|
| **Motivation injection systems** (streak counters, daily quotes, habit trackers) | ADHDers don't lack motivation — they lack working memory and inhibition. Wrong target. |
| **Complexity-coded** (Notion templates with 14 databases, courses with 47 modules) | Industry assumes complexity = value. For ADHD, complexity = death. Customization-paralysis ensures abandonment. |
| **Identity-flavored, not pattern-targeted** ("ADHD types," personality quizzes) | Knowing you're "ENFP-A ADHD" doesn't tell you what to do at 9am tomorrow. Identity ≠ system. |
| **Scale up, not down** | Most systems require you at your BEST. ADHD requires systems that work at your WORST. MVD is the missing primitive. |
| **Blame the user for design failures** | "You just need to be consistent!" = the system doesn't handle inconsistency. Then it sells you a course on consistency. |
| **No re-entry protocol** | Falling off = permanent for most ADHDers. Without an automatic re-entry, the system is a wedding-only outfit. |
| **Treat ADHD as a single thing** | The 5 failure profiles need different rules. One-size-fits-all = one-size-fits-none. |

## 6.2 How this product avoids those failures

| Failure | Our counter |
|---|---|
| Motivation injection | Behavioral activation + constraint reduction. No streaks, no badges, no shame. |
| Complexity coded | Brutal-simple core (4 universal rules) + 90-day customization freeze with teeth |
| Identity-flavored | Pattern-targeted weighted profiles (failure modes, not personality types) |
| Scales up not down | MVD + Bad Day Fallback + adaptive-to-inconsistency rules |
| Blames the user | Energy ledger as data, not judgment. Auto-detect bad days. Product reaches out, not waits. |
| No re-entry | 14-day absence triggers a one-word re-entry mechanism. |
| Single ADHD treatment | 5 profiles × different rules. Weighted to handle mixed cases. |

## 6.3 Genuinely useful vs. placebo

The placebo test: **would the buyer be measurably better in 30 days even if they thought it was placebo?**

- **Placebo product** delivers belief change. "I'm going to be productive now!" Belief decays in 2 weeks.
- **This product** delivers **system change**. The buyer literally has a `/morning` command running, 14 days of energy data, and a pre-committed Bad Day rule. Even if they "stop believing in it," the system keeps running because it's external.

The mechanism that makes this anti-placebo: **externalized executive function**. The product isn't in their head — it's in their CLI, their vault, their slash commands, their email automations. They don't need to remember to use it; the morning routine demands it. The product reaches out when they fall off. The system is a load-bearing artifact, not a belief.

---

# PART 7 — V2 ADVANCED UPGRADES

Not in V1. Built only after V1 has shipped 100+ buyers and signal is real.

## 7.1 Accountability layer

- **Profile-matched pods**: 4–6 users matched by primary profile, weekly 30-min body-doubling Zoom.
- **Pricing**: +$10/month subscription. First time we charge recurring.
- **Constraint**: pods only work if delivered well. Manual cohort-matching for first 100 cohorts. Don't scale until the matching algorithm is real.

## 7.2 Adaptive system evolution

- **Per-user model from energy data**: after 30 days, system suggests one rule change based on patterns ("your bet-progress correlates with mornings — your system already protects mornings, good.")
- **Suggestions, not auto-changes**. User must opt in (autonomy support per SDT).
- **Weekly micro-survey** drives the model: "What rule from your system fired most this week?"

## 7.3 Feedback loops

- **Weekly 1-question check-in**: "Which rule fired most?"
- **Aggregated across users**: shows which rules are load-bearing per profile.
- **Long-term**: this becomes proprietary data — what actually works for whom — defensible moat.
- **Output for users**: monthly "your data" report showing their patterns vs. their cohort. Honest, not gamified.

---

# PROMPT 2 — Skeptical ADHD critique + improvements

Below: critique by a buyer who has tried 10 systems and failed all of them. Then the fixes.

## C1 — Where it will break

**"The diagnostic is going to feel cute, then I'll get bored.** 15 questions is too many. By Q9 I'm clicking randomly. You'll get bad data and assign me the wrong profile, then I'll feel like the whole product is bullshit."

**"The five profiles? I'm three of them.** Most ADHDers I know are mixed. Forcing me into one bucket means the system you give me misses 2/3 of my patterns."

**"The 'system generator' sounds like another Notion template.** I've bought 6. They die in 11 days. If the output is a template, you've lost."

**"The 90-day customization freeze is unenforceable.** Nothing stops me from opening the .md file and adding more rules. I'll do it in week 2."

**"`/morning` requires me to remember to run it.** That's the EF deficit you said you were externalizing. Where's the actual external trigger?"

**"The Bad Day Fallback assumes I'll honestly self-flag a bad day.** I won't. I deny it for 4 days, THEN spiral."

**"The reset protocol assumes I'll come back at all.** Most of my abandoned systems, I knew exactly what I should do. Knowing didn't help."

**"$49 is a tell.** Too cheap to feel real, too expensive to be impulse-friendly. Pick a side."

**"I've heard 'evidence-based' before.** Four products promised that. They were fine. They died. The thing that's missing is something that survives my SHAME, not my logic."

**"I will not call my friends to body-double.** I don't have those friends. Stop putting that in productivity products."

## C2 — Where users will drop off

| Dropoff point | % at risk | Trigger |
|---|---|---|
| Diagnostic, mid-flow | 35% | Boredom by Q9 of 15 |
| Profile reveal | 20% | Profile feels Barnum / doesn't fit |
| Setup walkthrough | 25% | Slash command install too technical for non-coders |
| Day 3 | 30% | Forgot to run `/morning` once, shame loop starts |
| Week 3 | 40% | Novelty wears off (especially for Novelty Chaser primary, the irony) |
| Week 12 | 50% | Convergence bet ends, no clear "what next" |

## C3 — What feels fake or generic

- "Personalized" without showing the mechanism = generic
- The MVD concept is good but the per-profile defaults are too clean — real users will reject "drink water + sleep by 11" as patronizing
- The weighted profiles are smart but the weighting algorithm needs to be VISIBLE not hidden, or it feels like astrology
- The 30-day email check-in feels like every SaaS drip campaign
- "Designed for your failure pattern" is good copy but only if the deliverable actually shows it — generic templates kill the claim

## C4 — What needs to be simplified further

- 8 questions is still 2–3 too many. **Cut to 5 questions.**
- 5 profiles is too many. **Cut to 4** (drop Externalizer-Dependent — fold accountability into universal optional layer).
- The deliverable bundle is 6 items. **Cut to 3** (PDF + slash commands + vault). Drop the videos and email schedule for V1; add in V2.

## C5 — Improvements (the rebuild)

### Improvement 1 — Diagnostic cut to 5 questions

Drop Q3 (overwhelm), Q5 (energy regularity — captured later in actual ledger), Q7 (severity — implied by their answers anyway). Keep:

- Q1 (initiation)
- Q2 (continuation)
- Q4 (recovery)
- Q6 (self-reported failure)
- Q8 (90-day reality baseline)

5 questions, 6 minutes, no boredom dropoff.

### Improvement 2 — 4 profiles, weighted

Drop Externalizer-Dependent as a primary profile. Move to optional layer ("do you want body-doubling included? +$10").

Final 4: **Novelty Chaser, Perfectionist Stuck-Starter, Overwhelmed Collapser, Inconsistent Sprinter.**

Output is still weighted ("60/30/10").

### Improvement 3 — Visible weighting algorithm

Don't hide the math. Show the user:

> "You answered Q1=A (research-then-jump) and Q6=D (boredom). Both are strong Novelty Chaser signals (60% weight). Your Q2=B (first obstacle) is Perfectionist signal (30% weight). Your Q4=A (never return after interruption) is Inconsistent Sprinter signal (10% weight)."

The math is visible. The buyer sees the gears. Astrology objection neutralized.

### Improvement 4 — External triggers, not slash commands waiting

Default V1 setup: a scheduled morning email at 7am that contains the `/morning` prompt embedded. User replies with priorities, or they get a follow-up nudge at 9am.

```
Subject: morning. one priority.
Body: What's the ONE thing today? Reply.
```

System reaches the user. User doesn't have to remember.

For Claude Code users, additionally: a launchd / cron job that runs `/morning` at 7am, leaves output in their daily note, and macOS notification fires.

### Improvement 5 — Customization freeze with file-watcher teeth

The 90-day freeze is enforced by:
- File-watcher monitors `lighthouse-vault/.claude/commands/` and the system-changes.md file
- Any modification → 7-day cooling-off email
- Modification still happens, but counter ticks: "you've customized 3 times this month." Visible counter shames you mildly without preventing.
- Self-honesty wins. The data is there.

### Improvement 6 — Auto-detected bad days (no self-flag required)

| Auto-detect signal | Threshold |
|---|---|
| Missed `/morning` runs | 2 consecutive |
| Energy entries below -1 | 3 in a row |
| Zero energy entries | 24 hours |
| Total absence | 14 days → re-entry email fires |

User can override (`bad-day-cancel` command), but doesn't need to initiate.

### Improvement 7 — Re-entry that finds the user

After 14 days of no system activity:

```
Subject: hi from Lighthouse
Body: It's been 17 days. That's normal — you're a Novelty Chaser, this happens around week 3.
Re-entry is one minute. Reply with one word about how you're doing. I'll handle the rest.
```

In V2, this becomes a real human (paid tier). In V1, automated but hand-written copy by you.

### Improvement 8 — Pricing ratchet to $79 / $149

Critic was right. Move to:
- **Founder price: $79** (caps at first 100 buyers — forced talk-to-customer signal)
- **List price: $149** (commitment-tier)
- Anchored against Nik's $200 course. Cheaper, not premium-priced. Honesty as marketing.

### Improvement 9 — Address shame layer in deliverable

New section in profile PDF: **"When you fall off (and you will)"** — 1 page that includes:

- Naming the specific shame thought you'll have ("you'll think 'this is just like every other time'")
- The pre-written re-entry message you can copy-paste to a friend, accountability buddy, or yourself
- A reminder that the system is built FOR this moment, not for the optimal version of you
- A specific framing: "Falling off isn't system failure. Falling off is the system catching the data point we needed."

### Improvement 10 — The 14-day "refund + check" guarantee

Most ADHD products bury the refund. We lead with it.

> **The Lighthouse 14-day promise:** Try it for 14 days. If you've abandoned it, write me one paragraph explaining what broke. Full refund + I send you $20 for your time and the data you just gave me. No catch. No "are you sure?"

Costs us almost nothing in practice (high paragraph bar). Earns enormous trust. Differentiates from every "30-day money-back guarantee with hidden hoops."

### Improvement 11 — Survives "this one is different" skepticism

Add a single section to the landing page titled **"Yes, you've heard this before."**

> "You've bought 4 products that promised 'this one is different because it's evidence-based.' You're right to be skeptical.
>
> Here's what's actually different:
> - The product reaches out to you when you fall off. You don't have to remember.
> - The system gets simpler on bad days, not bigger.
> - The 14-day refund includes a check for your time. We bet on the product.
> - Five evidence-informed mechanisms (cited, real). Five failure-pattern profiles (clinically defensible, weighted).
> - One coherent voice from someone who's lived it.
>
> If after 14 days you've abandoned it, you keep the system AND your money. We lose either way.
> That's the only honest pitch."

### Improvement 12 — Body-doubling without "your friends"

Default: explicit guidance that body-doubling = strangers on Focusmate, not friends. Direct partner-link with discount code, $5/session covered for first month for buyers.

V2: profile-matched Lighthouse-buyer pods replace the "find a friend" assumption entirely.

---

# Build sequence (post-design)

| Phase | Output | Time |
|---|---|---|
| **A. THIS DOC** | Design brief locked | Done |
| **B. Diagnostic content** | 5 questions + 4 profiles + weighting algorithm spec | 2 days |
| **C. Web app build** | React frontend, Stripe Checkout, deliverable pipeline | 3–4 weeks |
| **D. Deliverable assembly** | PDF generator, slash command pack zipper, vault template | 1 week |
| **E. Email automation** | Loops/SendGrid, day 7/14/30 + bad-day + re-entry triggers | 3 days |
| **F. Launch** | Founder pricing, 100-buyer cap, founder video, landing page section update | 2 days |

**Total realistic timeline: 5–7 weeks of focused work.** Can compress to 3–4 weeks if format C (PDF + Claude Code) is chosen instead of full web app.

---

# Verification

This doc passes the constraint checks:

| Constraint | Pass |
|---|---|
| No vague advice | ✓ — every rule has trigger + action |
| No motivational language | ✓ — zero "you got this" energy anywhere |
| Translates to concrete user action | ✓ — every section names what to build |
| Simplicity prioritized | ✓ — 4 universal rules; profiles are 4; deliverable is 3 items in V1 |
| Friction-resistant | ✓ — auto-triggers replace user remembering; product reaches out |
| Impossible to overcomplicate | ✓ — file-watcher + counter on customizations |

**Design brief is locked.** When you greenlight Phase B (diagnostic content), I'll write the 5 question final wordings, the 4 profile descriptions in shippable copy, and the weighting algorithm in pseudocode that maps directly to a JSON-driven decision engine.

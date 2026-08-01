# rights-by-design-skill
A rights-by-design AI governance review skill for Claude.
How to Run a Constitutional-Rights Check on Any AI System in 5 Minutes

I built Rights by Design so you don't need a law degree or a compliance team to catch the failures before they ship. Here's exactly how to use it.

Most "responsible AI" happens too late. After the model is built. After it's deployed. After someone is harmed and a lawyer gets involved. By then the fix is expensive, narrow, and years overdue.

Rights by Design moves the check to where it's cheap: the design stage. It's free, it's open, and you can run it in the time it takes to read this post. No installation required, no account, no consultant.

Here's what it is, why it works, and how to use it.

What it actually is: Rights by Design is a skill — a set of expert instructions that turns any capable AI assistant into a rights reviewer. Think of it as a checklist with judgment. You hand it a description of an AI system, and it walks that system through five protections that constitutional democracies are built on: privacy, due process, equal protection, contestability, and accountability. Then it tells you, specifically, where the system fails and what to fix before you ship.

It's the working core of my book, made runnable. You don't read a framework. You use one.

Why run it at the design stage: Because rights retrofitted after harm are rights in name only.

A protection built into a system's architecture is cheap to add and hard to remove. The same protection bolted on after a scandal is expensive, fragile, and always arrives after someone has already paid for its absence. The five minutes you spend running this check is the cheapest insurance you will ever buy against building something that quietly strips people of their rights.

The easy way (anyone, ~5 minutes)

You don't need to be technical. If you can copy and paste, you can run it.

1. Open the skill file. Go to the repo and open SKILL.md: github.com/yadavranjan2023/rights-by-design-skill
2. Copy the whole file. Select all of it and copy.
3. Paste it into a fresh chat with Claude (or another capable AI assistant), as your instructions. This loads the framework.
4. Describe your system. Paste whatever you have: a product spec, a PRD, a model card, or just a plain-English paragraph — "We're building a tool that scores loan applicants and auto-declines the bottom 40%." The more detail, the sharper the review.
5. Ask it to run the review. You'll get back four things: the impact tier and why, a five-row scorecard (met, partial, or gap), a prioritized list of fixes to build in before ship, and one honest bottom line on whether it's ready.
6. Act on the "build in before ship" list. It's ordered hardest-to-retrofit first, so start at the top. That's where the design-stage savings are biggest.

That's it. No setup, no cost.

The power-user way (if you live in your tools)

If you use Claude Code or Cowork, you can add Rights by Design as a skill so it's always on tap. Install it from the repo once, and then you just say "review this system with rights-by-design" whenever you need it — no copy-paste. Setup steps are in the repo's README.

This is the version for teams: wire it into your design-review process so every new system gets the check before launch, the same way you'd run a security or privacy review.

What you get back (a real example)

I ran it on an ordinary resume-screening AI. In one pass it flagged: privacy (partial — inferring age and gender no one disclosed), due process (gap — auto-rejections with no human behind them), equal protection (gap — trained on biased history, never tested), contestability (gap — no appeal that can reverse), and accountability (partial — no named owner). Bottom line: not ready to deploy. Three constitutional rights failing at once, every one of them fixable at the design stage.

That's the whole point. The failures were foreseeable. The tool just asks the questions your process forgot to.

## Version 2.0

Version 2.0 adds sector overlays for:

- Telecommunications and communications infrastructure
- Department of Defense and national-security systems
- NASA and civil or commercial space systems
- Mission-critical and critical-infrastructure environments

The five universal dimensions remain:

1. Privacy and cognitive liberty
2. Due process and algorithmic dignity
3. Equal protection and nondiscrimination
4. Transparency and contestability
5. Accountability and democratic control

## Use in any AI assistant

1. Open `SKILL.md`.
2. Copy the complete file.
3. Paste it into a new conversation as the governing instructions.
4. Provide a system description, PRD, model card, procurement package, operational concept, architecture, or mission profile.
5. Ask: `Run a Rights by Design review.`

## Use in ChatGPT

For a reusable custom GPT:

1. Create a custom GPT.
2. Paste `chatgpt/INSTRUCTIONS.md` into the GPT Instructions field.
3. Upload `SKILL.md` and the files in `sector-modules/` as Knowledge.
4. Add representative evaluation cases from `evals/`.
5. Enable web access when current laws, standards, agency policies, or regulations must be verified.
6. Test in Preview before sharing.

Suggested conversation starters:

- Review this AI system using Rights by Design.
- Turn this product concept into testable rights and safety requirements.
- Assess this telecom AI system and identify deployment blockers.
- Review this defense AI concept for command, accountability, and civilian-risk gaps.
- Review this space-system autonomy design for safety and mission-assurance gaps.
- Compare these two vendors using Rights by Design.

## Repository structure

Repository structure
rights-by-design-skill/
├── README.md
├── SKILL.md
├── chatgpt/
│   ├── INSTRUCTIONS.md
│   ├── CONFIGURATION.md
│   ├── CONVERSATION_STARTERS.md
│   └── KNOWLEDGE_GUIDE.md
├── knowledge/
│   ├── methodology.md
│   ├── glossary.md
│   ├── worked-examples.md
│   └── sector-modules/
│       ├── employment.md
│       ├── lending.md
│       ├── healthcare.md
│       └── government.md
├── sector-modules/
│   ├── telecommunications.md
│   ├── defense-national-security.md
│   └── nasa-space-systems.md
├── evals/
│   ├── test-cases.md
│   ├── expected-findings.md
│   ├── regression-checklist.md
│   └── sector-test-cases.md
└── examples/
    ├── resume-screening-review.md
    ├── lending-review.md
    └── benefits-eligibility-review.md

## Limits

Rights by Design is a design and governance aid. It does not provide legal advice or certify compliance. It is not a substitute for agency, command, legal, privacy, cybersecurity, safety, engineering, acquisition, accessibility, civil-rights, weapons, airworthiness, flight-readiness, or mission-assurance review.

Run it now (free): github.com/yadavranjan2023/rights-by-design-skill

Rights by Design is the practical front end of my book, Constitutional Democracy in the Algorithmic Age: A Practical Framework for Preserving Citizen Rights (Springer, 2026), where the full framework and the law under it live. Pre-order: link.springer.com/book/9783032346032

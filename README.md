# AI Constitutional Engineering — Rights by Design

**Rights by Design** is an AI Constitutional Engineering Framework for designing, evaluating, and
governing AI systems *before* deployment. Instead of retrofitting protections after harm, it
translates constitutional principles, governance requirements, and organizational accountability
into repeatable engineering controls, evidence requirements, and deployment decisions.

An invariant core of **five universal rights dimensions** — privacy and cognitive liberty, due
process and algorithmic dignity, equal protection, transparency and contestability, and
accountability — combines with **sector-specific modules** to give consistent reviews across
government, healthcare, finance, telecommunications, defense, space systems, critical
infrastructure, manufacturing, and more.

The framework is **platform-neutral**: Claude, ChatGPT, GitHub, and future integrations are
*implementations* of Rights by Design, not the identity of the project.

Based on Rani Yadav-Ranjan's *Constitutional Democracy in the Algorithmic Age* (Springer Nature, 2026).
📖 Book: https://link.springer.com/book/9783032346032 · 🌐 https://yadav-ranjan.com

## What a review produces

- An **impact tier** calibrated to what a wrong or unaccountable decision costs a person.
- A **five-dimension scorecard** (met / partial / gap) with evidence and a build-in fix for each.
- The applicable **sector module's** controls, required evidence, and deployment blockers.
- A prioritized **"build in before ship"** list with named owners and blocker flags.
- An honest **ready / conditional / not-ready** bottom line.

## Use it

### Any AI assistant — no install
Open `plugins/rights-by-design/skills/rights-by-design/SKILL.md`, copy the whole file, paste it into
a fresh chat as instructions, and describe your system (a spec, a model card, or one sentence).

### Claude Code / Claude Cowork — plugin
```
/plugin marketplace add yadavranjan2023/rights-by-design-skill
/plugin install rights-by-design@rights-by-design-marketplace
```
Or add this repository's URL as a marketplace in the Cowork desktop app.

### ChatGPT
See `integrations/chatgpt/` for configuration and instructions.

## Sectors

Government · Law Enforcement · Healthcare · Lending · Insurance · Employment · Education ·
Telecommunications · Defense & National Security · NASA & Space Systems · Critical Infrastructure ·
Energy · Transportation · Robotics · Manufacturing · Biometrics · Smart Cities.

## Standards and legislation

Rights by Design maps to NIST AI RMF, the EU AI Act, ISO/IEC 42001, the OECD AI Principles, and the
U.S. Blueprint for an AI Bill of Rights — see `research/standards-legislation-crosswalk.md`. It is
designed to operationalize the intent of those instruments at the design stage.

## Adopt it

`docs/adoption-brief.md` is a one-page organizational case for using Rights by Design as a
design-stage gate.

## Evaluate it

`evals/` contains a runnable harness (`run-evals.py`) that checks the framework's outputs against
structured expectations across sectors.

## Repository layout

```
.claude-plugin/marketplace.json     # plugin/marketplace manifest (install entry point)
plugins/rights-by-design/           # the installable plugin (this is what ships)
  skills/rights-by-design/SKILL.md
  skills/rights-by-design/references/sectors/
docs/  research/  evals/  examples/  knowledge/  templates/  book/
integrations/                       # Claude and ChatGPT implementations
sector-modules/                     # human-readable sector reference docs
```

## Cite

Use GitHub's "Cite this repository" (`CITATION.cff`). Please cite the book:
*Constitutional Democracy in the Algorithmic Age* (Springer Nature, 2026).

---
*Rights by Design is a design and governance aid, not legal advice, and does not certify compliance
with any law, regulation, or standard.*

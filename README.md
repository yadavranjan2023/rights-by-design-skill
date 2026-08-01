# Rights by Design

## The Open Implementation Framework for Constitutional AI Governance

**Rights by Design** is an **AI Constitutional Engineering Framework** for designing, evaluating, and governing AI systems **before deployment**.

Rather than attempting to retrofit protections after harm occurs, Rights by Design translates constitutional principles, governance requirements, and organizational accountability into **repeatable engineering controls**, **evidence requirements**, and **deployment decisions**.

The framework combines an invariant core of **five universal rights dimensions** with **sector-specific modules**, enabling consistent AI reviews across government, healthcare, finance, telecommunications, defense, space systems, manufacturing, critical infrastructure, and other industries.

Rights by Design is intended for:

- AI Engineers
- Software Architects
- Product Managers
- AI Governance Teams
- Risk & Compliance
- Procurement Organizations
- Public Agencies
- Executive Leadership
- Researchers
- Policymakers

---

# Based On

Rights by Design is based on the framework presented in

**Rani Yadav-Ranjan**

*Constitutional Democracy in the Algorithmic Age*

Springer Nature (2026)

📖 Book

https://link.springer.com/book/9783032346032

🌐 Project Website

https://yadav-ranjan.com

---

# Why Rights by Design?

Most AI governance frameworks describe **what** organizations should consider.

Rights by Design focuses on **how** to operationalize governance.

It provides a repeatable methodology that converts constitutional principles into:

- engineering controls
- deployment criteria
- governance workflows
- evidence requirements
- approval processes
- monitoring requirements
- deployment blockers

The framework is designed to support AI systems throughout their lifecycle—from concept and procurement through deployment, operation, model updates, and retirement.

---

# Five Universal Rights Dimensions

Every AI system is evaluated across five foundational dimensions.

1. Privacy & Cognitive Liberty

2. Due Process & Algorithmic Dignity

3. Equal Protection & Nondiscrimination

4. Transparency & Contestability

5. Accountability & Democratic Control

These dimensions remain constant across industries while sector modules introduce domain-specific controls and evaluation criteria.

---

# Supported Platforms

Rights by Design is platform independent.

Current integrations include:

| Platform | Status |
|-----------|--------|
| ChatGPT | ✅ Supported |
| Claude | ✅ Supported |
| GitHub | ✅ Documentation |
| JSON/YAML Assessments | ✅ Supported |
| VS Code Extension | 🚧 Planned |
| GitHub Action | 🚧 Planned |
| rights-review CLI | 🚧 In Development |
| REST API | 🚧 Planned |

---

# ChatGPT Integration

ChatGPT resources are located in:

```text
integrations/chatgpt/
```

Contents

```text
CONFIGURATION.md

CONVERSATION_STARTERS.md

INSTRUCTIONS.md

KNOWLEDGE_GUIDE.md
```

ChatGPT can review:

- AI architectures
- Product Requirements Documents (PRDs)
- Model Cards
- Procurement packages
- Policies
- System documentation
- Risk assessments
- system.yaml files

Example prompt:

```text
Perform a Rights by Design review of this AI system.
```

---

# Claude Integration

Claude resources are located in:

```text
integrations/claude/
```

### Claude Code

```bash
/plugin marketplace add yadavranjan2023/rights-by-design-skill

/plugin install rights-by-design@rights-by-design-marketplace
```

### Claude Desktop / Claude Cowork

Add:

```
https://github.com/yadavranjan2023/rights-by-design-skill
```

Install

```
Rights by Design
```

Then ask Claude to review:

- AI systems
- architecture documents
- PRDs
- model cards
- procurement packages
- system.yaml

or invoke

```text
/rights-by-design
```

---

# Machine Readable Assessments

Rights by Design supports structured AI assessments.

Template

```text
templates/system.yaml
```

Schema

```text
schemas/system-v1.schema.json
```

Future releases will include

```bash
rights-review validate system.yaml

rights-review assess system.yaml

rights-review report system.yaml
```

---

# Sector Modules

Production sector modules include:

- Biometrics
- Critical Infrastructure
- Defense & National Security
- Education
- Employment
- Energy
- Government
- Healthcare
- Insurance
- Law Enforcement
- Lending
- Manufacturing
- NASA & Space Systems
- Robotics
- Smart Cities
- Telecommunications
- Transportation

---

# Repository Structure

```text
FRAMEWORK_SPEC.md

SKILL.md

README.md

ARCHITECTURE.md

CHANGELOG.md

ROADMAP.md

docs/

knowledge/

research/

templates/

examples/

evals/

sector-modules/

schemas/

integrations/
    chatgpt/
    claude/

assets/
```

---

# Industry Examples

Rights by Design includes production examples covering:

- Resume Screening
- Benefits Eligibility
- Lending
- Healthcare
- Telecommunications
- Defense
- NASA
- Insurance
- Education
- Autonomous Vehicles
- Policing
- Manufacturing
- Robotics
- Smart Cities
- Biometrics
- Critical Infrastructure
- Energy
- Procurement
- Vendor Evaluation
- AI Procurement RFP
- Model Card Review
- AI Incident Review
- Model Update Review
- Continuous Monitoring
- Executive Board Review

---

# Roadmap

## Version 1.0

- Framework Specification
- ChatGPT Integration
- Claude Integration
- 17 Sector Modules
- 25 Industry Examples
- Templates
- Research Crosswalks
- Evaluation Framework

## Version 1.1

- rights-review CLI
- JSON Schema Validation
- Automated Evaluation Engine
- GitHub Action
- Regression Test Suite

## Version 2.0

- Interactive Web Application
- REST API
- VS Code Extension
- Enterprise Dashboard
- Continuous Monitoring Platform

---

# Contributing

Contributions are welcome.

Areas include:

- Sector modules
- Industry examples
- Evaluation cases
- Research
- Templates
- Tooling
- Documentation

Please see

```
CONTRIBUTING.md
```

---

# Citation

If you use Rights by Design in research, publications, or implementations, please cite:

> Rani Yadav-Ranjan. *Constitutional Democracy in the Algorithmic Age.* Springer Nature, 2026.

Citation metadata is available in:

```
CITATION.cff
```

---

# License

See

```
LICENSE
```

---

# Disclaimer

Rights by Design is an engineering and governance framework intended to support the design, evaluation, deployment, and oversight of AI systems.

It is **not legal advice**, does **not certify compliance** with any law, regulation, or standard, and should be used alongside applicable legal, technical, safety, and organizational requirements.

---

## Vision

Our mission is to make constitutional principles, democratic accountability, and human rights **operational** within AI systems through open, transparent, evidence-based engineering practices.

**Build AI worthy of public trust.**
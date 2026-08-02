# Rights by Design — Standards and Legislation Crosswalk

*Conceptual alignment, not a compliance determination. This crosswalk maps the five Rights by
Design dimensions to the themes and obligations of major AI governance frameworks and laws, to
show how the framework can serve as a practical implementation layer over them. It does not
reproduce copyrighted standards and does not establish certification or legal compliance.*

## Positioning

Most AI governance instruments state **what** must be protected (fairness, transparency, human
oversight, accountability). Rights by Design supplies a **repeatable design-stage method** for
building those protections in before ship, with an impact tier, a five-dimension scorecard,
sector modules, and concrete "build in before ship" requirements. It is therefore complementary
to — not competitive with — NIST, the EU AI Act, ISO/IEC 42001, the OECD Principles, and the
U.S. Blueprint for an AI Bill of Rights: it operationalizes their intent at the point of design.

## Master crosswalk

| Rights by Design dimension | NIST AI RMF | EU AI Act (themes) | ISO/IEC 42001 (themes) | OECD AI Principles | U.S. Blueprint for an AI Bill of Rights |
|---|---|---|---|---|---|
| Privacy and cognitive liberty | Map (context, impacts); Measure (privacy); Manage | Data governance; data minimization; transparency of processing | Data governance; impact assessment; operational controls | Human-centred values; privacy | Data Privacy |
| Due process and algorithmic dignity | Govern (accountability); Map (affected parties); Manage (response) | Human oversight; information to deployers; rights protections for affected persons | Roles and responsibilities; operational planning and control | Human-centred values and fairness | Human Alternatives, Consideration, and Fallback |
| Equal protection and nondiscrimination | Measure (fairness, harmful bias); Map (impacts) | Risk management; data quality and representativeness; accuracy; monitoring | Risk and impact assessment; monitoring; corrective action | Human-centred values and fairness | Algorithmic Discrimination Protections |
| Transparency and contestability | Govern (documentation); Measure (explainability); Map (context) | Transparency obligations; instructions for use; record-keeping/logging; human oversight | Documentation; communication; operation; monitoring | Transparency and explainability | Notice and Explanation |
| Accountability and democratic control | Govern; continuous Map–Measure–Manage | Provider/deployer duties; quality management; logging; post-market monitoring | Management-system leadership; roles; internal audit; corrective action | Accountability | Safe and Effective Systems (governance and oversight) |

## EU AI Act — provision-level mapping (thematic)

Rights by Design outputs align with the obligations most relevant to high-risk systems:

- **Risk classification / prohibited practices** — the impact tier and sector selection help
  triage whether a system is likely high-risk or implicates prohibited practices, prompting the
  appropriate legal review.
- **Risk management system** — the scorecard and "build in before ship" list function as a
  design-stage risk-management pass, iterated across the lifecycle.
- **Data and data governance** — the Privacy and Equal Protection dimensions target
  minimization, representativeness, and bias testing on representative data.
- **Technical documentation and record-keeping / logging** — the Accountability dimension
  requires decision, override, and change logs an auditor can reach.
- **Transparency and provision of information** — the Transparency and contestability dimension
  requires notice, an understandable basis, and usable instructions.
- **Human oversight** — the framework's "meaningful human control" test (who, what they see,
  how much time, what authority, ability to reverse) directly operationalizes this.
- **Accuracy, robustness, cybersecurity** — carried by the mission-critical requirements and the
  sector modules (adversarial robustness, fail-safe behavior, bounded autonomy).
- **Fundamental-rights impact assessment** — the whole five-dimension review is a structured
  fundamental-rights impact assessment at the design stage.

## U.S. Blueprint for an AI Bill of Rights — one-to-one

The five Blueprint principles map cleanly onto the five Rights by Design dimensions (see the
master table), which makes Rights by Design a natural implementation of the Blueprint:
Safe and Effective Systems → Accountability and control; Algorithmic Discrimination Protections →
Equal protection; Data Privacy → Privacy and cognitive liberty; Notice and Explanation →
Transparency and contestability; Human Alternatives, Consideration, and Fallback → Due process
and algorithmic dignity.

## Sector modules and high-risk domains

Several Rights by Design sector modules correspond to domains that AI law and policy treat as
elevated-risk (for example, EU AI Act Annex III–style categories): employment, education,
essential public services and benefits, law enforcement, biometrics, critical infrastructure,
and access to essential private services such as credit and insurance. The matching sector
module supplies the domain-specific controls, evidence, and deployment blockers for that domain.

## How to use this crosswalk

- **Procurement / vendor review** — require a Rights by Design assessment as the design-stage
  artifact that evidences intent to meet NIST/EU/Blueprint expectations.
- **Policy and compliance teams** — use the mapping to show where a Rights by Design finding
  supports a specific regulatory obligation, without treating it as a compliance sign-off.
- **Auditors** — use the scorecard and logs as the traceable record the frameworks expect.

## Limitation

This is a conceptual crosswalk to aid human judgment. Frameworks and laws change, apply
differently by jurisdiction and risk tier, and require review by qualified legal, privacy,
security, safety, and domain authorities. Nothing here reproduces a copyrighted standard or
constitutes legal advice or a certification of compliance.

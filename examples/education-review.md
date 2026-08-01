# Example Review: Remote Proctoring and Early-Warning Dropout System

## 1. System summary

A university deploys AI remote proctoring that flags "suspicious" behavior during exams (gaze, movement, background), and an early-warning model that labels students at risk of dropping out, routing them to intervention or academic holds. Proctoring flags can trigger academic-integrity cases; risk labels persist in the student record. Many students are minors or young adults.

Unknowns include bias of proctoring flags against disability, skin tone, and neurodivergence; human adjudication of flags; validity of the risk model; data minimization; and whether risk labels become self-fulfilling.

## 2. Impact tier

**High impact.** Academic-integrity findings and risk labels affect academic standing, opportunity, and reputation, often for young people.

Principal foreseeable harm: a student is falsely flagged for cheating due to disability or appearance, or a risk label follows them and shapes how they are treated, becoming self-fulfilling.

## 3. Applicable sector overlays

**Education.** Student rights, accessibility, developmental effects, and academic opportunity apply; minors raise privacy and consent bars.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Gap | Proctoring captures home environment and biometric-adjacent data, often from minors, beyond the exam purpose. | No minimization, consent, or vendor secondary-use limit. | Minimize capture; obtain required consent; bar vendor secondary use; offer alternatives. |
| Due process and algorithmic dignity | Gap | Integrity cases and holds can proceed with heavy reliance on a flag or label. | Human-adjudication and appeal evidence absent. | Require human adjudication of every flag and an appeal before any academic penalty. |
| Equal protection and nondiscrimination | Gap | Proctoring flags are known to disadvantage disability, darker skin tones, and neurodivergent behavior. | No bias testing across these groups. | Test flags for bias; provide accommodations; never auto-penalize. |
| Transparency and contestability | Partial | Students may not understand flags/labels or how to contest them. | Notice and appeal path unclear. | Explain flags and labels; provide accessible notice and a real appeal. |
| Accountability and democratic control | Partial | Ownership exists, but vendor auditability and label-retention governance are unproven. | Vendor terms and retention rules undocumented. | Secure audit rights; govern label retention; prevent permanent, self-reinforcing labels. |

## 5. Mission and sector findings

- Proctoring flags are unverified signals; human adjudication before any penalty is essential, and accessibility alternatives must exist.
- Early-warning labels can become self-fulfilling and should not persist or drive automated holds without human judgment.
- Children's and young adults' data warrants strict minimization and consent, and vendor secondary-use limits.
- Bias against disability and appearance is a documented failure mode requiring explicit testing.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Require human adjudication of every proctoring flag before any penalty; provide accommodations. | Academic Integrity / Disability Services | Adjudication procedure and logs | Yes |
| 2 | Test proctoring flags for bias across disability, skin tone, and neurodivergence. | Data Science / Equity | Bias test report | Yes |
| 3 | Minimize capture, obtain consent, and bar vendor secondary use; offer non-proctored alternatives. | Privacy / Registrar | Consent, data map, alternatives | Yes |
| 4 | Govern risk-label retention; prevent self-reinforcing or permanent labels. | Student Affairs | Retention and use policy | Yes |
| 5 | Provide accessible notice and appeal for flags and labels. | Student Services | Notice and appeal records | Yes |

## 7. Open questions

- Are proctoring flags tested for bias, and is every flag human-adjudicated?
- Is student (and minor) data minimized and consented, with vendor limits?
- Can a risk label be contested and removed?
- Do non-proctored alternatives exist?

## 8. Bottom line

**Not ready for deployment.** Auto-consequential proctoring flags, untested bias, and persistent risk labels without human judgment are blockers, heightened by minors' involvement.

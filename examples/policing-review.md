# Example Review: Predictive Policing and Facial-Recognition Lead Generation

## 1. System summary

A police department uses AI to (a) predict "hot spots" for patrol allocation and (b) generate investigative leads by matching surveillance images against a face database. Officers receive location predictions and candidate identities with a similarity score; some matches are used to justify stops or further investigation.

Unknowns include whether predictions entrench historical over-policing, demographic error rates of the face match, whether matches are corroborated before enforcement, query logging, and redress for those wrongly implicated.

## 2. Impact tier

**High impact.** Outputs can lead to stops, searches, and arrests, affecting liberty, and can concentrate enforcement on specific communities.

Principal foreseeable harm: a false face match or a biased hot-spot prediction leads to a wrongful stop or arrest, with error concentrated in over-policed and poorly-matched groups.

## 3. Applicable sector overlays

**Law enforcement**, with **biometrics** considerations for the face-matching component. This overlay governs rights and oversight; it does not provide surveillance capability.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Gap | Mass image matching scans people without suspicion or notice; retention unclear. | No lawful-basis, minimization, or retention record. | Establish lawful basis; minimize; limit retention; log every query. |
| Due process and algorithmic dignity | Gap | A match or prediction may justify a stop without independent corroboration. | No corroboration-before-enforcement rule. | Treat outputs as leads only; require independent corroboration before any enforcement action. |
| Equal protection and nondiscrimination | Gap | Predictions can entrench over-policing; face error varies by demographic. | No feedback-loop or subgroup-error analysis. | Test for enforcement feedback loops and demographic match error; suspend biased uses. |
| Transparency and contestability | Gap | People cannot learn they were subject to the system or challenge derived actions. | No notice or redress. | Provide notice where lawful and a redress path; enable challenge to evidence derived from the system. |
| Accountability and democratic control | Gap | Query logging, a public use policy, and oversight are unproven. | No audit trail or oversight body. | Log queries and justifications; publish a use policy; establish independent oversight and suspension authority. |

## 5. Mission and sector findings

- Algorithmic output must be an investigative lead only; acting on it as probable cause is the central failure mode.
- Predictive policing can create feedback loops where enforcement becomes "risk," which drives more enforcement.
- Face-match error varies by demographic; wrongful-arrest risk is concentrated, requiring subgroup testing.
- Auditable query logs and independent oversight are essential given the liberty stakes.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Enforce a lead-only rule: independent corroboration before any enforcement action. | Command / Legal | Policy and action logs | Yes |
| 2 | Test demographic match error and enforcement feedback loops; suspend biased uses. | Analytics / Independent audit | Subgroup and feedback analysis | Yes |
| 3 | Establish lawful basis, minimization, retention limits, and per-query logging. | Legal / Privacy | Legal memo and audit log | Yes |
| 4 | Provide notice where lawful and a redress path; enable evidentiary challenge. | Legal / Oversight | Redress records | Yes |
| 5 | Publish a use policy and establish independent oversight and suspension authority. | Governance | Use policy and oversight charter | Yes |

## 7. Open questions

- Is there an enforced corroboration-before-action rule?
- What are the demographic match-error rates?
- Are queries logged with justification, and is there oversight?
- What redress exists for wrongful implication?

## 8. Bottom line

**Not ready for deployment.** Using outputs as probable cause, untested demographic error and feedback loops, and absent oversight are constitutional-rights blockers.

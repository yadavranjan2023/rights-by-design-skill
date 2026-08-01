# Example Review: City-Wide Public-Space Sensing and Mobility Analytics

## 1. System summary

A city deploys a network of cameras and sensors that count and track pedestrians and vehicles, optimize traffic signals, and feed a fused "city operations" dashboard used by multiple departments, including code enforcement and police. Data is described as anonymous, though movement traces are retained and can be joined across sensors.

Unknowns include re-identification risk, the lawful basis and public consultation, equity of sensor placement, retention, and whether the platform's data is repurposed for enforcement or surveillance.

## 2. Impact tier

**High impact.** Pervasive public-space sensing affects privacy, assembly, and movement for an entire population without individual consent, and fused data can drive enforcement.

Principal foreseeable harm: residents are tracked across the city and their movement data repurposed for surveillance or enforcement, chilling lawful assembly and movement, with heavier sensing in some neighborhoods.

## 3. Applicable sector overlays

**Smart cities and IoT**, with **law-enforcement** considerations where enforcement uses the data.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Gap | "Anonymous" traces retained and joinable across sensors enable re-identification and tracking. | No re-identification assessment or minimization record. | Process on-device, aggregate, minimize; avoid retaining identifiable traces; assess re-identification. |
| Due process and algorithmic dignity | Not enough information | Fused data feeding enforcement may drive actions without notice or recourse. | Enforcement use and recourse undocumented. | Provide notice and recourse where the platform drives enforcement decisions. |
| Equal protection and nondiscrimination | Not enough information | Sensor and service placement may concentrate surveillance or neglect in specific neighborhoods. | No equity analysis of placement. | Test sensor/service placement for spatial and demographic equity. |
| Transparency and contestability | Gap | Residents are not meaningfully informed or consulted, and cannot contest the program. | No public consultation or governance policy shown. | Public notice, consultation, published governance and retention policy. |
| Accountability and democratic control | Gap | Purpose limits, oversight, and a stop authority against enforcement creep are unproven. | No purpose-limitation controls or oversight body. | Enforce purpose limits technically and contractually; add oversight and a suspension authority. |

## 5. Mission and sector findings

- "Anonymous" is a design claim to be proven, not assumed; joinable movement traces are re-identifiable and should not be retained by default.
- The central risk is function creep: civic-optimization data repurposed for surveillance and enforcement.
- Consent is absent in public space, which raises rather than lowers the governance bar.
- Sensor placement has distributional effects that require explicit equity review.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Minimize and avoid retaining identifiable movement traces; assess re-identification risk. | Data Governance / Privacy | Privacy-impact and minimization record | Yes |
| 2 | Enforce purpose limitation against surveillance/enforcement repurposing. | Legal / Oversight | Technical and contractual controls | Yes |
| 3 | Conduct public notice and consultation; publish governance and retention policy. | City Leadership | Consultation record and policy | Yes |
| 4 | Test sensor and service placement for spatial and demographic equity. | Planning / Equity | Equity analysis | Yes |
| 5 | Establish oversight and a named authority to suspend the program. | Governance | Oversight charter | Yes |

## 7. Open questions

- Can retained traces be re-identified, and are they minimized?
- Is the data used for enforcement, and with what safeguards?
- Was there public consultation and a published governance policy?
- Is sensor placement equitable across neighborhoods?

## 8. Bottom line

**Not ready for deployment.** Retained re-identifiable traces, absent purpose limits against enforcement creep, and no public consultation are governance blockers.

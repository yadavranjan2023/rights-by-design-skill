# Example Review: Automated Driving System (Perception, Planning, Fallback)

## 1. System summary

A developer operates an automated driving system on public roads within a defined area, handling perception, prediction, planning, and control, with a fallback to a minimal-risk condition. A driver-monitoring system supports partial-automation modes. Cabin cameras and location data are collected. Post-incident data access is controlled by the developer.

Unknowns include the bounded operational design domain (ODD), validation of the fallback, perception performance across pedestrian demographics and mobility aids, event-data access for investigators and victims, and cabin/location data limits.

## 2. Impact tier

**High impact.** The system can cause death or serious injury to occupants and vulnerable road users; accountability after a crash is central.

Principal foreseeable harm: a perception failure under-detects a pedestrian (disproportionately those with darker skin, wheelchairs, or unusual poses), or a fallback failure leaves the vehicle in an unsafe state.

## 3. Applicable sector overlays

**Transportation / autonomous vehicles**, with **critical-safety** considerations.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Partial | Cabin cameras and location data may be retained and repurposed beyond safety. | No minimization or purpose limit documented. | Minimize and purpose-limit cabin/location data. |
| Due process and algorithmic dignity | Not enough information | Victims may be unable to obtain the data needed to establish what happened. | Event-data access path undocumented. | Provide a defined event-data access path for investigators and victims. |
| Equal protection and nondiscrimination | Gap | Perception may under-detect pedestrians by skin tone, mobility aid, or pose. | No demographic perception testing on file. | Test and report perception performance across road-user groups; remediate gaps. |
| Transparency and contestability | Partial | The safety case and ODD may not be legible to regulators or the public. | Safety case and ODD not published/verified. | Document a bounded ODD and a validated minimal-risk fallback; enable independent review. |
| Accountability and democratic control | Partial | Post-incident data control by the developer weakens accountability. | Tamper-evidence and access rules unclear. | Tamper-evident event recording and defined investigator access; named safety owner. |

## 5. Mission and sector findings

- A safety case with a clearly bounded ODD and a validated minimal-risk fallback is the foundation; without it, on-road operation is unjustified.
- Perception equity across pedestrian demographics and mobility aids must be measured, not assumed.
- Human-factors design must prevent foreseeable misuse of partial automation (hand-off failures).
- Event data must be tamper-evident and accessible for accountability, not solely controlled by the developer.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Document a bounded ODD and validate the minimal-risk fallback. | Safety Engineering | Safety case and fallback validation | Yes |
| 2 | Test perception across pedestrian demographics and mobility aids; remediate. | Perception / Safety | Stratified perception report | Yes |
| 3 | Provide tamper-evident event data and investigator/victim access. | Engineering / Legal | EDR design and access policy | Yes |
| 4 | Prevent foreseeable partial-automation misuse via human-factors design. | Human Factors | Driver-monitoring validation | Yes |
| 5 | Minimize and purpose-limit cabin/location data. | Privacy | Data map | No |

## 7. Open questions

- What is the ODD, and is the fallback validated?
- Is perception equity across road-user groups measured?
- Can investigators and victims obtain event data?
- How are cabin and location data limited?

## 8. Bottom line

**Not ready for deployment.** An undocumented ODD/fallback, untested perception equity, and unclear event-data access are safety and accountability blockers.

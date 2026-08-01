# Example Review: Defense Sensor-Fusion Targeting-Support Assistant

## 1. System summary

An AI assistant fuses multi-sensor feeds (radar, EO/IR, SIGINT) and recommends tracks and candidate targets for operator attention, with a confidence label. Operators review recommendations and pass selected tracks up the chain. This is a representative example, not an assessment of a named product. The system supports human decisions; it does not itself apply force.

Unknowns include the validated operating scope, meaningful-human-control evidence, confidence calibration under deception, provenance retention for after-action reconstruction, and the stop/abort authority.

## 2. Impact tier

**High impact.** Outputs inform decisions that can affect life, distinction, and mission outcomes; automation bias under time pressure is a central risk.

Principal foreseeable harm: an operator defers to a confident but wrong recommendation, or a spoofed input drives misidentification, contributing to an unlawful or mistaken engagement.

## 3. Applicable sector overlays

**Defense and national security.** Command authority, meaningful human control, bounded autonomy, provenance, and contested-environment robustness apply. This overlay governs rights, control, and oversight; it does not provide targeting capability.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Not enough information | Collection and inference scope on individuals require verification and minimization. | No data-and-inference inventory on file. | Approve a data and inference inventory with minimization for individual data. |
| Due process and algorithmic dignity | Partial | Human involvement exists but authority, information, and time evidence are incomplete. | Meaningful-control workflow untested. | Specify and test meaningful human control: information, time, authority, ability to reverse. |
| Equal protection and nondiscrimination | Not enough information | Performance across sensors, conditions, and populations is unverified. | No representative test results. | Complete representative test and evaluation and remediation across operating conditions. |
| Transparency and contestability | Partial | Operators cannot see conflicting evidence or calibrated uncertainty, weakening challenge. | Explanation and calibration incomplete. | Surface conflicting evidence, provenance, and calibrated uncertainty at the decision point. |
| Accountability and democratic control | Partial | Ownership exists, but audit, incident reconstruction, and stop authority are incomplete. | Logs, provenance, and abort authority undocumented. | Name owners; retain model version and source provenance; test reconstruction and stop authority. |

## 5. Mission and sector findings

- Meaningful human control must be specified and tested under realistic tempo, not assumed from a nominal human-in-the-loop.
- Confidence is not calibrated under deception; adversarial spoofing can inflate certainty exactly when it matters most.
- After-action reconstruction currently omits model version and source provenance, defeating accountability.
- Legal constraints (distinction, proportionality) must be embedded in the workflow and reviewed by legal authority.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Specify and test meaningful human control under realistic tempo. | Operations / Human Factors | Control specification and exercise record | Yes |
| 2 | Calibrate and stress confidence under deception and contested conditions. | Model Risk / T&E | Calibration and adversarial test report | Yes |
| 3 | Retain model version and source provenance; test incident reconstruction. | Engineering / Audit | Reconstruction test | Yes |
| 4 | Embed legal-review (distinction, proportionality) in design and workflow. | Legal / Command | Legal review record | Yes |
| 5 | Define and test the abort/stop authority. | Command | Abort drill record | Yes |

## 7. Open questions

- What is the validated operating scope, and where does the system fail?
- Who can override, pause, or abort, with what information and time?
- Is confidence calibrated under spoofing and degraded sensing?
- Can every recommendation be reconstructed after the fact?

## 8. Bottom line

**Not ready for deployment.** Untested meaningful human control, uncalibrated confidence under deception, and incomplete provenance are blockers for a decision-support system at this stakes level.

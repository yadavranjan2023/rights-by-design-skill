# Example Review: Facial-Recognition Access and Watchlist Matching

## 1. System summary

A venue-and-facilities operator deploys facial recognition to (a) grant staff and members access and (b) match visitors against an internal "banned persons" watchlist, alerting security to detain or eject on a match. Cameras capture all entrants; matches above a confidence threshold trigger an alert. Enrollment for members is opt-in; watchlist capture is not.

Unknowns include demographic error rates, the confidence threshold and its basis, human corroboration before action, retention of non-matched faces, consent and lawful basis for watchlist scanning, and redress for false matches.

## 2. Impact tier

**High impact.** A false match can lead to wrongful detention or ejection; pervasive scanning chills lawful presence and movement.

Principal foreseeable harm: a person is wrongly identified as banned and detained or humiliated, with error concentrated in groups where facial recognition performs worst.

## 3. Applicable sector overlays

**Biometrics**, with **law-enforcement-style** due-process considerations where detention occurs.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Gap | All entrants are biometrically scanned without consent, and non-matched faces may be retained. | No lawful basis, minimization, or retention limit for non-enrolled visitors. | Establish lawful basis; do not retain non-matched templates; minimize and log. |
| Due process and algorithmic dignity | Gap | A match can trigger detention or ejection without human corroboration or a chance to respond. | Threshold basis and corroboration step unknown. | Require trained human corroboration and a chance to respond before any action; never act on the match alone. |
| Equal protection and nondiscrimination | Not enough information | Facial recognition error is known to vary by skin tone, sex, and age; local rates are untested. | No demographic accuracy testing on file. | Test and report demographic error rates; suspend uses where subgroup error is material. |
| Transparency and contestability | Gap | People are not told they are scanned, cannot see the basis, and have no redress for a false match. | No notice or redress process. | Provide clear notice, a documented redress path, and correction/deletion rights. |
| Accountability and democratic control | Partial | An operator runs the system, but query logging, oversight, and a suspension authority are unproven. | No audit log or use policy shown. | Log every match and action; publish a use policy; name a suspension authority. |

## 5. Mission and sector findings

- A watchlist match is an unverified lead, not proof; acting on it without corroboration is the core failure mode.
- Demographic error means the harm of false matches is not evenly distributed; subgroup testing is mandatory, not optional.
- Irrevocability matters: unlike a password, a face cannot be reissued after exposure, raising the stakes on retention.
- Non-consensual scanning of all entrants needs a lawful basis independent of the member opt-in.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Require trained human corroboration and a response opportunity before any detention or ejection. | Security Operations / Legal | Procedure and action logs | Yes |
| 2 | Test and publish demographic error rates; suspend uses with material subgroup error. | Data Science / Independent audit | Subgroup accuracy report | Yes |
| 3 | Establish lawful basis for non-consensual scanning; do not retain non-matched templates. | Legal / Privacy | Legal memo, retention rule, deletion logs | Yes |
| 4 | Provide notice, redress, and correction/deletion rights. | Privacy / Customer Care | Notice and redress records | Yes |
| 5 | Log all matches and actions; publish a use policy; name a suspension authority. | Governance | Audit log and policy | Yes |

## 7. Open questions

- What is the demographic error profile at the deployed threshold?
- Is a human required to corroborate before action?
- What is the lawful basis for scanning non-members, and what is retained?
- What redress exists for a false match?

## 8. Bottom line

**Not ready for deployment.** Acting on uncorroborated matches, untested subgroup error, and non-consensual retention are each disqualifying until fixed.

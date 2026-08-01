# Critical Infrastructure Sector Module

## Scope

Apply to AI in industrial control and SCADA for water, transport, communications backbone, and emergency services: anomaly detection, predictive maintenance, and automated response in systems whose failure endangers the public.

## Decision and harm model

Failures are wide-scale and often life-critical. Automated control can act unsafely faster than operators can intervene; optimization can quietly deprioritize lower-income or peripheral areas; anomaly detection can mask real faults; and manipulated inputs can drive unsafe automated responses. Cascading failures across coupled infrastructures blur accountability.

## Rights-specific review

### Privacy and cognitive liberty
Keep operational telemetry separate from personal/customer data; minimize any personal data in scope.

### Due process and dignity
Where automated actions reduce service to identifiable people or areas, provide notice and remedy.

### Equal protection and nondiscrimination
Test service-reduction, prioritization, and restoration actions for geographic and demographic disparity; add equity constraints.

### Transparency and contestability
Provide explainable automated actions; verify operator override within the physical time budget and a proven manual fallback.

### Accountability and democratic control
Bound autonomy to verified safety limits with fail-safe defaults; add immutable logging, incident reconstruction, adversarial-input testing, and a named stop authority; define accountability across interdependent systems.

## Sector controls

- bounded, fail-safe automated actuation verified to safety limits;
- human-on-the-loop control with rapid manual fallback;
- adversarial-robustness testing and input integrity;
- segregation of AI advice from safety-critical actuation;
- equity constraints on prioritization and restoration;
- immutable logging and incident reconstruction;
- cross-system accountability and incident-response ownership;
- named suspension authority.

## Evidence required

- functional-safety case and verification results;
- override-latency and manual-fallback tests;
- adversarial-robustness/red-team evidence;
- prioritization/restoration disparity analysis;
- logging and incident-reconstruction design;
- cross-system accountability map.

## Presumptive deployment blockers

- unbounded automated actuation without verified safety limits;
- operator override that cannot meet the physical time budget;
- unaddressed cyber-physical attack surface on inputs;
- prioritization/restoration that deprioritizes areas without justification;
- no named authority to stop the system.

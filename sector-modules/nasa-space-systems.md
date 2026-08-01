# NASA and Space-Systems Sector Module

## Scope

Apply this module to NASA, civil-space agencies, commercial spaceflight, launch providers, satellite operators, mission control, ground systems, scientific missions, crewed missions, robotic exploration, and space-domain infrastructure.

## Review domains

### 1. Mission and safety classification

Identify mission phase, safety criticality, crew and public exposure, vehicle or payload consequences, reversibility, communication delay, and acceptable risk thresholds.

### 2. Autonomy boundaries

Specify what AI may recommend or execute during launch, ascent, orbit, proximity operations, rendezvous, docking, entry, descent, landing, surface operations, robotics, payload operations, or contingency response.

### 3. Fault management

Assess fault detection, isolation, recovery, redundancy, sensor disagreement, voting logic, safe modes, recovery priorities, and the possibility of common-mode failure.

### 4. Long-duration and delayed-control operations

Evaluate autonomy under intermittent contact, high latency, bandwidth constraints, ground-station loss, stale commands, and limited opportunities for human intervention.

### 5. Environmental resilience

Test radiation effects, thermal extremes, vibration, vacuum, dust, hardware degradation, clock drift, sensor failure, memory corruption, and computational constraints.

### 6. Navigation and conjunction risk

Assess state estimation, uncertainty, ephemeris quality, collision avoidance, orbital-debris mitigation, maneuver authority, proximity safety, and false-positive or false-negative conjunction decisions.

### 7. Telemetry and command integrity

Protect command authentication, encryption, key management, telemetry provenance, time synchronization, replay prevention, ground-segment access, and anomalous-command detection.

### 8. Human-machine interaction

Ensure crews and controllers can understand system state, confidence, constraints, rationale, and recommended actions under nominal and off-nominal conditions.

### 9. Scientific integrity

Protect calibration, provenance, reproducibility, uncertainty, anomaly handling, data transformation, model-generated classifications, and separation between scientific findings and operational convenience.

### 10. Planetary protection

Where applicable, assess forward and backward contamination, autonomous sampling, containment, landing-site constraints, and mission-rule enforcement.

### 11. Verification, validation, and mission assurance

Require requirements traceability, simulation, hardware-in-the-loop testing, edge-case testing, independent verification and validation, configuration control, flight-software assurance, red-team testing, and documented residual risk.

## Deployment blockers

Treat the following as presumptive blockers:

- safety-critical autonomy without verified bounds;
- no safe mode or recoverable state;
- untested loss-of-communications behavior;
- inadequate fault isolation or common-mode failure analysis;
- no configuration traceability;
- inability to reproduce an autonomous decision;
- unvalidated collision-avoidance or navigation behavior;
- inadequate command authentication;
- unresolved crew, public, vehicle, payload, or planetary-protection risk.

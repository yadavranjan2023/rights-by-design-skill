# Example Review: Autonomous Warehouse Mobile Robots Around Workers

## 1. System summary

A fulfillment operator deploys fleets of autonomous mobile robots that move inventory through aisles shared with human workers. Robots plan paths, adjust speed near people, and coordinate as a fleet. Some human-robot interaction is close-proximity; a warehouse-management system also sets human task pace informed by robot throughput.

Unknowns include verified safety separation and speed limits, fail-safe behavior, emergency-stop coverage, liability assignment for injuries, and whether robot-driven pace-setting endangers or penalizes workers.

## 2. Impact tier

**High impact.** Robots operating near people can cause physical injury; robot-driven pacing affects worker safety and livelihood.

Principal foreseeable harm: a robot injures a worker through unsafe speed, motion, or a perception failure, or throughput optimization pushes an unsafe human work pace.

## 3. Applicable sector overlays

**Robotics**, with **manufacturing/warehouse-safety** and **employment** considerations.

## 4. Rights-by-Design scorecard

| Dimension | Status | Finding | Evidence or missing information | Build-in safeguard |
|---|---|---|---|---|
| Privacy and cognitive liberty | Partial | Navigation and monitoring sensors may capture worker location and behavior continuously. | No minimization or purpose limit on worker sensing. | Minimize worker-identifying sensing; limit to navigation/safety purpose. |
| Due process and algorithmic dignity | Not enough information | Robot-informed pacing may drive discipline without review. | Link between throughput and discipline unclear. | Require human review before pace-based discipline; humane, safety-bounded targets. |
| Equal protection and nondiscrimination | Not enough information | Pace targets may disadvantage disability or age. | No disparate-impact analysis of pacing. | Test pacing for disparate impact; provide accommodation. |
| Transparency and contestability | Partial | Workers may not understand robot behavior near them or how to stop it. | Signaling and stop-access unverified. | Clear behavior signaling and accessible emergency stop for any worker. |
| Accountability and democratic control | Gap | Verified safety limits, fail-safes, and injury-liability assignment are unproven. | No robot-safety validation or liability model. | Verify safety separation/speed, fail-safes, e-stop coverage; assign responsibility for robot actions. |

## 5. Mission and sector findings

- Physical safety separation and speed must be verified against collaborative-robot safety standards, with hardware fail-safes and broad emergency-stop coverage.
- Autonomy must be bounded and a responsible human accountable for the fleet's actions.
- Throughput optimization must not set a human pace that raises injury risk; pacing is a safety decision.
- Continuous navigation sensing should not become worker surveillance beyond its safety purpose.

## 6. Build in before ship

| Priority | Requirement | Responsible role | Evidence of completion | Deployment blocker |
|---|---|---|---|---|
| 1 | Verify safety separation, speed limits, fail-safes, and emergency-stop coverage. | Safety Engineering | Robot-safety validation report | Yes |
| 2 | Bound autonomy and assign accountability for robot actions and injuries. | Operations / Legal | Authority and liability model | Yes |
| 3 | Keep human work pace safety-bounded; require review before pace-based discipline. | HR / Safety | Ergonomic targets and review logs | Yes |
| 4 | Test pacing for disparate impact and provide accommodation. | HR / Legal | Disparate-impact analysis | Yes |
| 5 | Minimize worker sensing to the navigation and safety purpose. | Data Governance | Sensor-data map | No |

## 7. Open questions

- Are separation, speed, and fail-safes verified to a recognized robot-safety standard?
- Who is accountable if a robot injures a worker?
- Does robot throughput set human pace, and is that pace safety-bounded?
- Can any worker stop a robot immediately?

## 8. Bottom line

**Not ready for deployment.** Unverified physical safety limits and unbounded pace-setting near workers are physical-safety blockers.

# Vega

**A thrust-vector-controlled (TVC) model rocket that steers itself by tilting its engine.**

> open source gimbal design

Vega gimbal to hold the rocket motor in place
<!-- Drop a render or photo of your gimbal here. Put images in a /docs folder. -->
<img width="1106" height="797" alt="image" src="https://github.com/user-attachments/assets/6878e769-eb95-49ed-9fe1-091da3e7e9a9" />


---

## What is Vega?

Vega is a amateur rocket that keeps itself pointing straight up using **thrust vector control** — instead of fins, it actively **tilts the motor** to steer, the same principle full-scale rockets like the Falcon 9 use.

The heart of the project is a **custom two-axis gimbal**, designed from scratch in Fusion 360, that cradles the motor and swivels it on two perpendicular axes. Two servos drive the gimbal, a microcontroller reads the rocket's tilt from an IMU, and a **PID control loop** commands the servos to correct the rocket's angle in real time.

> **Status:** [e.g. Gimbal design complete and motion-validated in CAD · flight electronics in progress]

---

## Features

- **Two-axis TVC gimbal** — tilts the motor to steer on both pitch and roll axes
- **Fully parametric CAD** — designed in Fusion 360, all parts 3D-printable
- **Servo-driven actuation** — [SERVO MODEL, e.g. 2× SG90 micro servos]
- **Closed-loop stabilization** — [IMU MODEL, e.g. MPU6050] + PID control

---

## How it works

1. An **IMU** ([SENSOR MODEL]) measures the rocket's tilt angle many times per second.
2. A **microcontroller** ([BOARD, e.g. RP2040 / Arduino]) runs a **PID loop** comparing the current angle to "straight up."
3. The PID output commands **two servos**, which tilt the **gimbal** — and therefore the motor — to push the rocket back toward vertical.
4. Because the two gimbal axes are perpendicular, the motor can point anywhere in a cone, correcting drift in any direction.



---

## The gimbal (core of the design)

The gimbal is a nested two-ring mechanism:

| Part | Role |
|------|------|
| **Inner ring** | Holds the rocket motor; pivots on Axis 2 |
| **Outer ring** | Carries the inner ring; pivots on Axis 1 (perpendicular) |
| **Base** | Mounts to the airframe; holds the outer ring on two pillars |


**Key specs** *(fill in your real numbers):*
- Motor bore: `[24.25] mm` diameter
- Inner ring: `[45] mm` tall, `[2] mm` walls
- Outer ring: `[50] mm` tall, `[~17] mm` tilt gap
- Pivot pins: `[3] mm`
- Tilt range: `±[15]°` per axis (validated in CAD)

---

## Repository structure

```
Vega/
├── CAD/                 # Fusion 360 exports / STL files
│   ├── gimbal.stl
└── README.md
```


---

## Bill of materials

| Item | Qty | Notes |
|------|-----|-------|
| Quest Q-Jet Composite Motor - D22-4W | 1 | motor fort the gimbal simulation |
every other part is availaible with me
---

## Build & assembly

1. **Print** all parts in `/CAD` — recommended: [material, e.g. PLA/PETG],
2. **Assemble the gimbal:** [brief steps — inner ring → outer ring → base → pins].
3. **Mount the servos** and link them to the gimbal.





---

---

## About

Built by **[Araadh Singh]** :-.

-  X: [@araadhsingh1](https://x.com/araadhsingh1)

Inspired by [e.g. BPS.space and the open-source rocketry community].

---



---


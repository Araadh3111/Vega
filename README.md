# Vega

A thrust-vector-controlled (TVC) model rocket that steers itself by tilting its engine.

<div align="center">

<img width="1106" height="797" alt="image" src="https://github.com/user-attachments/assets/b4668198-61cc-4ef0-860b-a64c0b2203c9" />


</div>

What is Vega?

Vega is an amateur rocket that keeps itself pointing straight up using thrust vector control. Instead of relying on fins for aerodynamic stability, it actively tilts the motor to steer. This is the exact same principle that full-scale orbital launch vehicles use.

The core of the project is a custom two-axis gimbal. I designed it from scratch in Fusion 360 to cradle the motor and swivel it on two perpendicular axes. Two servos drive the gimbal, a microcontroller reads the rocket's tilt from an IMU, and a PID control loop commands the servos to correct the rocket's angle in real time.

Features

* Two-axis TVC gimbal: Tilts the motor to steer on both pitch and roll axes.
* Fully parametric CAD: Designed in Fusion 360, all structural parts are 3D-printable.
* Servo-driven actuation: Designed for fast-response micro servos (e.g., SG90).
* Closed-loop stabilization: Runs on an MPU6050 IMU and a tuned PID controller.

The Gimbal Mechanism

The gimbal is the mechanical heart of the rocket, acting as a nested two-ring mechanism to provide independent, dual-axis freedom without binding.

* Base: Mounts securely to the rocket airframe and supports the outer ring on two structural pillars.
* Outer Ring: Pivots on Axis 1 and carries the inner ring assembly.
* Inner Ring: Securely houses the rocket motor and pivots on Axis 2, perpendicular to the outer ring.

Key Specs:

* Motor Bore: 24.25 mm diameter
* Inner Ring: 45 mm height, 2 mm wall thickness
* Outer Ring: 50 mm height, ~17 mm tilt clearance gap
* Pivot Pins: 3 mm diameter
* Tilt Range: +/- 15 degrees per axis (validated in CAD)

How It Works

1. An onboard IMU measures the rocket's tilt angle and angular velocity at a high refresh rate.
2. The microcontroller processes this data through a PID control loop, comparing the current orientation against the target "straight up" vector.
3. The PID output calculates the necessary corrections and sends precise PWM signals to the two servos.
4. The servos manipulate the gimbal, redirecting the motor's exhaust within a 15-degree cone to physically push the rocket back toward vertical.

Bill of Materials

| Item | Quantity | Notes |

| :--- | :--- | :--- |
| Quest Q-Jet Composite Motor (D22-4W) | 1 | Used as the primary motor for gimbal physical simulation and testing. |

(Note: Structural components, microcontrollers, servos, and fasteners are currently sourced and available on hand.)

Assembly Guide

1. Print all parts in the /CAD directory. PETG or ABS/ASA 
2. Insert the 3 mm pivot pins to connect the inner ring to the outer ring.
3. Secure the assembled outer ring into the base pillars using the remaining pivot pins.



Repository Structure

```text

Vega/

CAD/ # Fusion 360 export files and 3D-printable STLs

gimbal.stl

README.md # Project documentation

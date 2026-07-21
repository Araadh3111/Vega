# Vega
' Video link to test gimbal angle limits in CAD --> https://youtu.be/oK2FTemJwAE

A thrust-vector-controlled (TVC) model rocket that steers itself by tilting its engine designed by me in CAD in around 2 hours.

<div align="center">

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/ddd1fd97-2fd7-437a-b44f-a0fcf2138734" />


<img width="1713" height="1053" alt="image" src="https://github.com/user-attachments/assets/59cc1e6d-d5bd-4627-80a9-ea53c4bffa9b" />


<img width="1328" height="927" alt="image" src="https://github.com/user-attachments/assets/b75b6727-d21d-4531-b4c8-8263a7f0610d" />

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/aed64f10-30c9-4e99-88fe-7d4d762110b0" />

<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/60f5bac7-a4bd-43c6-913b-94c3a90c25dc" />
# Rocket Tune Control System working:
<img width="1920" height="1080" alt="rocket pid controller" src="https://github.com/user-attachments/assets/61f6c9ac-bfb2-48c6-9b40-9f996344eeeb" />

# CIRCUIT DIAGRAM
<img width="1917" height="1078" alt="image" src="https://github.com/user-attachments/assets/afbad2a3-e38a-407c-a33f-9140f9c04c95" />

# Ejection charge handling
(D22-4W): The Q-Jet D22-4W includes a built-in black-powder ejection charge that fires ~4 seconds after burnout, venting hot gas forward out of the motor. Since this gimbal is a static test article with no recovery system, all static fires are conducted with (1) electronics and wiring mounted off-axis, never above the motor's open end, and (2) an angled metal deflector plate over the motor mouth directing the ejection blast sideways, away from the test article and observers. Motors are never disassembled to remove the charge.
</div>

What is Vega?

Vega is an amateur rocket that keeps itself pointing straight up using thrust vector control. Instead of relying on fins for aerodynamic stability, it actively tilts the motor to steer. This is the exact same principle that full-scale orbital launch vehicles use.

The core of the project is a custom two-axis gimbal. I designed it from scratch in Fusion 360 to cradle the motor and swivel it on two perpendicular axes. Two servos drive the gimbal, a microcontroller reads the rocket's tilt from an IMU, and a PID control loop commands the servos to correct the rocket's angle in real time.

Features

* Two-axis TVC gimbal: Tilts the motor to steer on both pitch and roll axes.
* Servo-driven actuation: Designed for fast-response micro servos (e.g., EMAX ES08MA II).
* Closed-loop stabilization: Runs on an MPU6050 IMU and a tuned PID controller.

The Gimbal Mechanism

What is a gimbal? A gimbal is a thing that can hold an object and allow its movement in multiple axis, allowing to bench lots of stuff mostly used for model rockets and even in real rockets, to know more about gimbals (in model rockets and thrust vector control) u can read this --> https://en.wikipedia.org/wiki/Thrust_vectoring

* Base: Mounts securely to the rocket airframe and supports the outer ring on two structural pillars.
* Outer Ring: Pivots on Axis 1 and carries the inner ring assembly.
* Inner Ring: Securely houses the rocket motor and pivots on Axis 2, perpendicular to the outer ring.

Key Specs:

* Motor Bore: 24.25 mm diameter
* Inner Ring: 45 mm height, 2 mm wall thickness
* Outer Ring: 50 mm height, ~17 mm tilt clearance gap
* Pivot Pins: 3 mm diameter (3.2 in cad for the clearance issues with 3d printers)
* Tilt Range: +/- 15 degrees per axis (validated in CAD) (have to shorten the tilt angle not much of a problem as of now)

How It Works

1. An onboard IMU measures the rocket's tilt angle and angular velocity at a high refresh rate.
2. The microcontroller processes this data through a PID control loop, comparing the current orientation against the target "straight up" vector.
3. The PID output calculates the necessary corrections and sends precise PWM signals to the two servos.
4. The servos manipulate the gimbal, redirecting the motor's exhaust within a 15-degree cone to physically push the rocket back toward vertical.

# Bom:
to check out the parts I will be using for this build refer to BOM.csv

Assembly Guide

1. Print all parts in the /CAD directory. PETG or ABS/ASA 
2. Insert the 3 mm pivot pins to connect the inner ring to the outer ring.
3. Secure the assembled outer ring into the base pillars using the remaining pivot pins.

# Ai Usage
I used claude to get the design reference but the build was done by me myself

Repository Structure

```text

Vega/
├── CAD/
│   ├── gimbal.step     # v1 ground-test gimbal 
│   └── gimbal.stl      # print-ready export
├── vega_controller/    # Pico firmware: IMU read + PID + servo PWM
├── ASSEMBLY.md         # build & assembly guide
├── BOM.csv             # bill of materials
├── README.md
└── gimbal moving video.mp4

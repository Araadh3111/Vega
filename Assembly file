# Vega — Assembly Guide

This guide walks through assembling the Vega two-axis TVC gimbal, from printed parts to a wired, servo-driven mechanism.

---

## 1. Parts checklist

**3D-printed parts** (in `/CAD`):
- [ ] Inner ring (motor holder)
- [ ] Outer ring
- [ ] Base (with pillars)
- [ ] Palm cover / servo mounts *(if separate)*
- [ ] Control horns ×2 *(if separate parts)*

**Hardware:**
- [ ] 3 mm pivot pins ×4 *(2 per axis)*
- [ ] Pushrods (2 mm steel wire) ×2
- [ ] M2 servo screws
- [ ] [Any fasteners for base-to-airframe]

**Electronics:**
- [ ] Microcontroller — [YOUR BOARD]
- [ ] EMAX ES08MA II servos ×2
- [ ] MPU6050 IMU
- [ ] Battery / 5–6 V supply
- [ ] Jumper wires

---

## 2. Gimbal assembly (inside-out)

**Step 1 — Inner ring → Outer ring (Axis 2):**
1. Seat the inner ring inside the outer ring.
2. Line up the inner ring's pivot tabs with the outer ring's holes.
3. Insert a **3 mm pin** through each side. The inner ring should now tilt freely.
4. *Check:* it swings ±[15]° without the tabs hitting the outer wall.

**Step 2 — Outer ring → Base (Axis 1):**
1. Set the outer ring between the base pillars.
2. Align the outer ring's tabs with the pillar holes.
3. Insert a **3 mm pin** through each pillar. The whole gimbal should now tilt on the perpendicular axis.
4. *Check:* the outer ring clears the base through its full tilt (no binding).

> The two axes are perpendicular, so the motor can point anywhere in a ~[15]° cone.

---

## 3. Servo installation

**Outer-ring servo (drives Axis 1):**
1. Press the servo into the **base servo mount** and secure with M2 screws.
2. Attach the servo arm.
3. Connect a **pushrod** from the servo arm to the **control horn on the outer ring**.

**Inner-ring servo (drives Axis 2):**
1. Mount the servo on the **outer ring** *(it must ride on the outer ring so it tilts with it)*.
2. Attach the arm and run a **pushrod** to the **control horn on the inner ring**.

> *Note:* the control horns sit slightly **below the pivot line** — this offset is what lets the pushrod rotate each ring.

---

## 4. Motor & electronics

1. Insert the [motor] into the inner ring bore.
2. Mount the microcontroller and IMU [location].
3. Wire everything per the **[wiring diagram](docs/wiring.png)** — key points:
   - Servo signals → PWM pins
   - Servo power → external 5–6 V supply (**not** the MCU's 5V pin)
   - **All grounds common**
   - IMU → I²C (SDA/SCL)
4. Flash the firmware from `/Code` and calibrate the IMU level.

---

## 5. Function check

- [ ] Both rings tilt smoothly by hand — no binding.
- [ ] Each servo, when driven, tilts its ring ±[15]°.
- [ ] Pushrods clear all parts through full travel.
- [ ] IMU reads a stable angle when the rocket is held vertical.
- [ ] PID loop drives the servos to correct tilt.

---

*Built by [Araadh Singh] · [github.com/Araadh3111/Vega](https://github.com/Araadh3111/Vega)*

import turtle
import time
screen = turtle.Screen()
myturtle = turtle.Turtle()
spinrate = 0
tiltrate = 1

target = 0
error = tiltrate - target
mv1 = 1
total_accumulated_error = 0 

# Add a wind variable to easily test the gimbal limit
wind_force = 0.5 

for i in range (10000):
    time.sleep(0.005)   
    myturtle.setheading(tiltrate)
    
    # 1. Calculate Error
    error = tiltrate - target
    total_accumulated_error += error  
    changeinerror = error - mv1
    
    # 2. Calculate Raw Forces
    D_force = 10 * changeinerror
    I_force = total_accumulated_error * 0.001
    proportionality = error * 2
    
    # 3. Sum the total correction requested by the PID
    total_correction_force = proportionality + D_force + I_force
    
    # 4. CLAMP THE FORCE (Actuator Saturation)
    # If the requested force is beyond the physical limit, clamp it to the limit.
    if total_correction_force > 5:
        total_correction_force = 5
    elif total_correction_force < -5:
        total_correction_force = -5
        
    # 5. Apply Kinematics
    # Subtract the single clamped force, and subtract the wind to test survivability
    spinrate = tiltrate * 0.1 + spinrate - total_correction_force - wind_force
    tiltrate = spinrate * 0.1 + tiltrate
    
    print(error)
    mv1 = error

screen.exitonclick()
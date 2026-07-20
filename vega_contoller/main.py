#Objective to make a program that calculates errors every second
setpoint = 0 #the angle I want my rocket to be at
current_angle = 1
angular_speed = 0
dt = 0.02
Kp = 200
Kd = 25
tracker = -1
for i in range(200):
    error = setpoint-current_angle
    proportional_term = Kp*error
    
    de = error-tracker
    D_term = de/dt * Kd
    accel = 50 * current_angle + proportional_term +D_term +50
    angular_speed += dt * accel
    current_angle += angular_speed*dt 
    tracker=error
    print(f"current angle = {round(current_angle, 2)}")
    

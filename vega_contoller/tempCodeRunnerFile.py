#Objective to make a program that calculates errors every second
setpoint = 0 #the angle I want my rocket to be at
current_angle = 1
angular_speed = 0
dt = 0.02


    
    


for i in range(200):
    accel = 50 & current_angle
    angular_speed = dt * accel
    current_angle = angular_speed*dt
    
    error = setpoint-current_angle 
    print(f"current angle = {current_angle}")

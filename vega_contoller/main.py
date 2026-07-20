#Objective to make a program that calculates errors every second
setpoint = 0 #the angle I want my rocket to be at
current_angle = 1


    
    


for i in range(23):
    current_angle*=0.2
    error = setpoint-current_angle 
    print(f"error = {error}")

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
for i in range (10000):
    
    time.sleep(0.005)   
    myturtle.setheading(tiltrate)
    error = tiltrate - target
    total_accumulated_error +=error  
    changeinerror = error - mv1
    D_force = 10 * changeinerror
    I_force = total_accumulated_error*0.001
    proportionality = error*2
    spinrate= tiltrate * 0.1  + spinrate - proportionality - D_force - 0.5 + I_force
    tiltrate= spinrate * 0.1  + tiltrate
    
    
    print(error)
    mv1 = error





screen.exitonclick()
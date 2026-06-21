import turtle
import time
screen = turtle.Screen()
myturtle = turtle.Turtle()
spinrate = 0
tiltrate = 1

target = 0
error = tiltrate - target

for i in range (10000):
    
    time.sleep(0.005)   
    myturtle.setheading(tiltrate)
    error = tiltrate - target
    
    proportionality = error*2
    spinrate= tiltrate * 0.1  + spinrate - proportionality
    tiltrate= spinrate * 0.1  + tiltrate
    
    
    print(error)





screen.exitonclick()
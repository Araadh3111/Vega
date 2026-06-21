import turtle
import time
screen = turtle.Screen()
myturtle = turtle.Turtle()
spinrate = 0
tiltrate = 1

target = 0
error = tiltrate - target

for i in range (100):
    
    time.sleep(0.005)   
    myturtle.setheading(tiltrate)
    spinrate= tiltrate * 0.1  + spinrate
    tiltrate= spinrate * 0.1  + tiltrate


target = 0
error = tiltrate - target
print(error)


screen.exitonclick()





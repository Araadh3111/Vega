#import matplotlib to see the data in graph 
import matplotlib.pyplot as plt
#Objective to make a program that calculates errors every second


def simulate(Kp, Kd, Ki):
    setpoint = 0 #the angle I want my rocket to be at
    current_angle = 1
    angular_speed = 0
    dt = 0.02
    tracker = -1
    integral = 0
    time_list = []
    time = 0.0
    current_angle_list = []


    for i in range(200):
        error = setpoint-current_angle
        proportional_term = Kp*error
    
        de = error-tracker
        D_term = de/dt * Kd
        integral += error*dt
        I_term = Ki*integral
        accel = 50 * current_angle + proportional_term +D_term +50 +I_term
        angular_speed += dt * accel
        current_angle += angular_speed*dt 
        tracker=error
        time+=dt
        print(f"current angle = {round(current_angle, 2)}")
        current_angle_list.append(current_angle)
        time_list.append(time)

    return time_list, current_angle_list
time_list, current_angle_list = simulate(60, 25, 100)
#print(current_angle_list)    
plt.plot(time_list,current_angle_list)
plt.xlabel("Time (seconds)")
plt.ylabel("Rocket Angle (degrees)")
plt.title("Rocket PID stabilization")
plt.axhline(y=0,color='r',linestyle = '--')
plt.show()
#import matplotlib to see the data in graph 
import matplotlib.pyplot as plt
#Objective to make a program that calculates errors every second
from matplotlib.widgets import Slider

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
        
        current_angle_list.append(current_angle)
        time_list.append(time)

    return time_list, current_angle_list
time_list, current_angle_list = simulate(200, 25, 100)
#print(current_angle_list)    
line, = plt.plot(time_list, current_angle_list, label="angle")
plt.legend()
plt.xlabel("Time (seconds)")
plt.ylabel("Rocket Angle (degrees)")
plt.title("Rocket PID stabilization")
plt.axhline(y=0,color='r',linestyle = '--')
plt.subplots_adjust(bottom=0.35)
ax_kp = plt.axes([0.25, 0.20, 0.5, 0.03])
kp_slider = Slider(ax_kp, "Kp", 0, 500, valinit=200)
ax_kd = plt.axes([0.25, 0.12, 0.5, 0.03])
kd_slider = Slider(ax_kd, "Kd", 0, 100, valinit=25)
ax_ki = plt.axes([0.25, 0.04, 0.5, 0.03])
ki_slider = Slider(ax_ki, "Ki", 0, 299, valinit=100)

def update(val):
    # after moving a slider the graph should also update 
    
    
    time_list, current_angle_list = simulate(kp_slider.val, kd_slider.val, ki_slider.val)
    line.set_ydata(current_angle_list)
    plt.gcf().canvas.draw_idle()

kp_slider.on_changed(update)   
kd_slider.on_changed(update)
ki_slider.on_changed(update)
plt.show()

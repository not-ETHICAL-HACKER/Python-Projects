import turtle
import math
import time
scale = 250
pi_scale = 100
two_pi = int(2*math.pi*pi_scale)*100
t = turtle.Turtle(visible=False)
t.speed(0)
t.color("white")
#e = turtle.Turtle()
#e.color("white")
#e.speed(0)
colors = ["blue", "purple", "red", "cyan"]

def rose(n:float,phase:float=0) -> None:
    turtle.bgcolor("black")
    pi_interval = 0
    for i in range(-two_pi,two_pi):
        phase += math.radians(1)
        r = math.cos(n*(i/pi_scale+phase))*scale
        x = r*math.cos(i/pi_scale+phase)
        y = r*math.sin(i/pi_scale+phase)
        if i>pi_interval*two_pi/4:
            pi_interval += 1
            #t.color(colors[pi_interval%len(colors)])
            #e.color(colors[(pi_interval)%len(colors)])
        if i == -two_pi:
            t.penup()
            #e.penup()
            #e.goto(-x,-y)
            t.pendown()
            t.goto(x,y)
            t.circle(1)
            #e.pendown()
        t.goto(x,y)
        t.circle(1)
        #e.goto(-x,-y)
# for k in [0,30,45,60,90]:
#     for j in range(11):
#         t.clear()
#         turtle.Screen().title(f"Rose curve with n={j} and phase={k} degrees")
#         rose(j,math.radians(k))
#         time.sleep(.01)
rose(math.pi+math.e)
turtle.done()
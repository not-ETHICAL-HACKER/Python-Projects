import turtle
import math
import time

scale = 1
pi_scale = 100
two_pi = int(math.pi*2*pi_scale)

t = turtle.Turtle(shape="turtle")
t.color("red")
turtle.bgcolor("black")
t.speed(0)
turtle.tracer(0)
for j in range(100):
    t.clear()
    t.goto(0,0)
    for i in range(-two_pi,two_pi):
        t.left((math.log(max(abs(i/pi_scale),1))*j)*scale)
        t.forward(math.sin(i/pi_scale)*scale)
    turtle.update()
    time.sleep(.5)

turtle.done()
import turtle
import math
import time
scale = 500
pi_scale = 100
two_pi = int(2*math.pi*pi_scale)*10
t = turtle.Turtle(visible=False)
t.speed(0)
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta"]


def rose(n: float, phase: float = 0) -> None:
    turtle.bgcolor("black")
    interval = 1
    for i in range(-two_pi, two_pi):
        if i % ((two_pi/10)*interval) == 0 or i == -two_pi:
            t.color(colors[(interval-1) % len(colors)])
            interval += 1
        phase += math.radians(1)
        r = math.cos(n*(i/pi_scale+phase))*scale
        x = r*math.cos(i/pi_scale+phase)
        y = r*math.sin(i/pi_scale+phase)
        if i == -two_pi:
            t.penup()
            t.goto(x, y)
            t.pendown()

        t.goto(x, y)


rose(math.pi)
print("done")

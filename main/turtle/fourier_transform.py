"""this file aint acually fourier transform i just wanted to see if i could implement it in py"""
import time
import turtle
import math

t = turtle.Turtle(shape="turtle")
t.speed(0)
turtle.bgcolor("black")
scale_pi = 100
scale = 100
two_pi = int(2*math.pi*scale_pi)
t.color("white")

turtle.tracer(0)
def fourier_transform(wave_args:list[float|int],c:list[str],phase_diff:float=0):
    for _ in range(-two_pi*100,two_pi*100+1):
        phase_diff += math.radians(1)
        for i in range(-two_pi,two_pi+1):
            x = i
            y = math.sin((sum([math.sin((var_theta*(i/scale_pi))+phase_diff) for var_theta in wave_args]))+phase_diff/10)*scale
            t.color(c[_%len(c)])
            if i == -two_pi:
                t.penup()
                t.goto(x,y)
                t.pendown()
            t.goto(x,y)
        turtle.update()
        time.sleep(1/24)
        t.clear()
l:list[float] = [x for x in range(1,10**2)]
colors = ["red","blue","green","yellow"]
fourier_transform(l,colors,math.pi/2)
turtle.done()
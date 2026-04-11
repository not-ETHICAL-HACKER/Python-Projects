"""this file aint acually fourier transform i just wanted to see if i could implement it in py"""
import turtle
import math

t = turtle.Turtle(visible=False)
t.speed(0)
turtle.bgcolor("black")
scale_pi = 100
scale = 100
two_pi = int(2*math.pi*scale_pi)
t.color("white")
t.goto(1000,0)
t.goto(-1000,0)
t.goto(0,1000)
t.goto(0,-1000)

def fourier_transform(wave_args:list[float|int],c:str,phase_diff:float=0):
    
    for i in range(-two_pi,two_pi+1):
        x = i
        y = sum([math.sin((var_theta*(i/scale_pi))+phase_diff) for var_theta in wave_args])*scale
        t.color(c)
        if i == -two_pi:
            t.penup()
            t.goto(x,y)
            t.pendown()
        t.goto(x,y)
l = [x for x in range(1,10**2+2,2)]
colors = ["red","blue","green","yellow"]
fourier_transform(l,colors[0],math.pi/2)
print("done")
turtle.done()
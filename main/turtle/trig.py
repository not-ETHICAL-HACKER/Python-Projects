import turtle
from itertools import product
import math
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.bgcolor("black")
t.color("white")
pi_scale = 10
scale = 100
two_pi = int(2*math.pi*pi_scale)


def sin_wave():
    t.color("cyan")
    for i in range(-two_pi, two_pi + 1):
        new = i / pi_scale
        if i == -two_pi:
            t.penup()
            t.goto(new*scale, math.sin(new)*scale)
            t.pendown()
        t.goto(new*scale, math.sin(new)*scale)


def cos_wave():
    t.color("magenta")
    for i in range(-two_pi, two_pi + 1):
        new = i / pi_scale
        if i == -two_pi:
            t.penup()
            t.goto(new*scale, math.cos(new)*scale)
            t.pendown()
        t.goto(new*scale, math.cos(new)*scale)


def tan_wave():
    t.color("yellow")
    for i in range(-two_pi, two_pi + 1):
        new = i / pi_scale
        try:
            if i == -two_pi:
                t.penup()
                t.goto(new*scale, math.tan(new)*scale)
                t.pendown()
            t.goto(new*scale, math.tan(new)*scale)
        except Exception:
            continue


def sec_wave():
    t.color("orange")
    for i in range(-two_pi, two_pi + 1):
        new = i / pi_scale
        try:
            if i == -two_pi:
                t.penup()
                t.goto(new*scale, (1/math.cos(new))*scale)
                t.pendown()
            t.goto(new*scale, (1/math.cos(new))*scale)
        except Exception:
            continue


def csc_wave():
    t.color("green")
    for i in range(-two_pi, two_pi + 1):
        new = i / pi_scale
        try:
            if i == -two_pi:
                t.penup()
                t.goto(new*scale, (1/math.sin(new))*scale)
                t.pendown()
            
            t.goto(new*scale, (1/math.sin(new))*scale)
        except Exception:
            continue


def cot_wave():
    t.color("purple")
    for i in range(-two_pi, two_pi + 1):
        new = i / pi_scale
        try:
            if i == -two_pi:
                t.penup()
                t.goto(new*scale, (1/math.tan(new))*scale)
                t.pendown()
            t.goto(new*scale, (1/math.tan(new))*scale)
        except Exception:
            continue


sin_wave()
cos_wave()
tan_wave()

# t.clear()

sec_wave()
csc_wave()
cot_wave()

turtle.done()

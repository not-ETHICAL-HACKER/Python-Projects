"""this file aint acually fourier transform i just wanted to see if i could implement it in py"""
import random
import time
import turtle
import math
from typing import Any

t = turtle.Turtle(shape="turtle")
t.speed(0)
turtle.bgcolor("black")
t.color("red")
t2 = turtle.Turtle()
t2.hideturtle()
t.hideturtle()
t2.speed(0)
t2.color("blue")
turtle.tracer(0)


def fourier_transform(wave_args: list[float | int], c: list[str], phase_diff: float = 0):
    for _ in range(-two_pi, two_pi+1):
        phase_diff += math.radians(1)
        for i in range(-two_pi, two_pi+1):
            x = i
            y = sum([math.sin((var_theta*(i/scale_pi))+phase_diff)
                     for var_theta in wave_args])*scale
            t.color(c[_ % len(c)])
            if i == -two_pi:
                t.penup()
                t.goto(x, y)
                t.pendown()
            t.goto(x, y)
        turtle.update()  # remove clear for cool effect
        # time.sleep(1/24)
        t.clear()


def fourier_transform_2(wave1_args: list[float | int], wave2_args: list[float | int], color_list: list[str] = ["red"], phase_diff1: float = 0.0, phase_diff2: float = 0.0) -> None:
    for _ in range(-two_pi*100, two_pi*100+1):
        phase_diff1 += math.radians(1)
        phase_diff2 += math.radians(1)
        stat = True
        for i in range(-two_pi, two_pi+1):
            x = i
            if stat:
                y1 = sum([math.sin(var_theta * (i / scale_pi)+phase_diff1) for var_theta in wave1_args]) * scale
                y2 = sum([math.sin((var_theta * (i/scale_pi))+phase_diff2) for var_theta in wave2_args]) * scale
            else:
                y1 = sum([
                    math.sin(var_theta * (i / scale_pi)) *
                    math.cos(phase_diff1)
                    for var_theta in wave1_args
                ]) * scale
                y2 = sum([
                    math.sin(var_theta * (i / scale_pi)) *
                    math.cos(phase_diff2)
                    for var_theta in wave2_args
                ]) * scale

            t.color(color_list[_ % len(color_list)])
            if i == -two_pi:
                t.penup()
                t2.penup()
                t.goto(x, y1)
                t2.goto(x, y2)
                t2.pendown()
                t.pendown()
            t.goto(x, y1)
            t2.goto(x, y2)
        turtle.update()
        # time.sleep(1/24)
        t.clear()
        t2.clear()


def fourier_transform_3(wave_num: int, colors: list[str], wave_args: list[Any] = [], phase_differences: list[float] = []):
    turts: list[turtle.Turtle] = []
    if len(phase_differences) != wave_num:
        phase_differences = [0 for _ in range(wave_num)]
    if not wave_args:
        wave_args = []
        for i in range(wave_num):
            args = [random.randint(0, 10) for _ in range(10**1)]
            wave_args.append(args)
    for _ in range(wave_num):
        t = turtle.Turtle(visible=False)
        t.color(colors[_ % len(colors)])
        turtle.tracer(0)
        turts.append(t)
    diff = 0
    for _ in range(-two_pi*100, two_pi*100+1):
        diff += math.radians(1)
        phase_differences = [x+diff for x in phase_differences]
        for i in range(-two_pi, two_pi+1):
            for num, t in enumerate(turts):
                x = i
                y = sum([math.sin(var_theta * (i / scale_pi)+phase_differences[num])
                        for var_theta in wave_args[num]]) * scale
                t.goto(x, y)
        turtle.update()
        for t in turts:
            t.clear()    


scale_pi = 100
scale = 25
two_pi = int(2*math.pi*scale_pi)
l: list[float] = [float(random.randint(1, 10)*random.gauss())
                  for _ in range(1, 10**1)]
ll: list[float] = [float(random.randint(1, 10)*random.gauss())
                   for _ in range(1, 10**1)]
l1: list[float] = [_/2 for _ in range(10)]
l2: list[float] = [_ for _ in range(10)]
colors = ["red", "blue", "green", "yellow"]
red = ["red"]
fourier_transform_3(2, colors=colors)
turtle.done()

import time
import turtle
import math
import random
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("white")
scale = 10
turtle.tracer(0)
def gauss(mu:float, sigma:float):
    n = 1
    l:list[tuple[float, float]] = []
    for i in range(10**2):
        y = random.random()*100*n
        s = 0
        for _ in range(10**2):
            x = random.gauss(mu, sigma)
            s += x
            l.append((s,y))
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(2)
        if i % 1_000 == 0:
            turtle.update()
            n+=1
    t.goto(0, 0) 
    turtle.update()
    t.color("red")
    for x,y in l:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(2)
    turtle.update()
    turtle.done()
gauss(0, 1)
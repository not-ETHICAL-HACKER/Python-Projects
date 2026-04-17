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
    for _ in range(10**5):
        y = random.random()*10*n
        x = random.gauss(mu, sigma)*scale*n
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(2)
        if _ % 1_000 == 0:
            #turtle.update()
            n+=.1
    turtle.update()
    turtle.done()
gauss(0, 1)
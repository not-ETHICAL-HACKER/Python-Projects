import time
import turtle
import math
import random
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("white")
scale = 1
def gauss(mu, sigma):
    for _ in range(10**5):
        x = random.gauss(mu, sigma)*scale
        y = random.gauss(mu, sigma)*scale
        t.goto(x, y)
        time.sleep(0.01)  
    turtle.done()
gauss(0, 10)
import turtle
import math
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("white")

for i in range(1,10**2):
    t.left(math.log(i)*i)
    t.forward(math.log(i))
turtle.done()
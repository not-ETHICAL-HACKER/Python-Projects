import turtle
import math
t = turtle.Turtle()
t.hideturtle()
t.speed(10)
t.color("white")
turtle.bgcolor("black")
lim = 10**3
a = 0
b = 1
for i in range(lim):
    theta = i 
    a, b = b, b+a
    t.left(1.61803398875*10)
    t.forward(math.log(1.618**theta))

print("Done")
turtle.done()

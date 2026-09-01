import turtle
import math
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.bgcolor("black")
t.color("purple")

for i in range(270): # arbritary num bcs the graph looks cool
    print(i)
    if i > 314: # pi/4 val
        t.color("blue")
    if i > 314/2: # pi/2 val
        t.color("red")
    t.circle(i*math.sin(i/100),i/100*180/math.pi)
    t.left(i/10)
    t.backward(i/10)

turtle.done()
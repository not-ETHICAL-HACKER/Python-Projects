import turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red","orange","yellow","green","blue","purple"]

for i in range(200):
    t.color(colors[i % len(colors)])
    t.circle(100)
    t.left(5)

turtle.done()
import turtle
turtle.bgcolor("black")
t = turtle.Turtle(visible=False)
t.color("red")
n = 27
while n != 1:
    if n % 2 == 0:
        t.left(5)
        n //= 2
    else:
        t.right(15)
        n = 3*n + 1
    t.forward(5)
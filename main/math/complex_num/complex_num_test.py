import cmath,turtle
turtle.bgcolor("black")
t = turtle.Turtle(visible=False)
t.color("white")
z = 1 + 1j
for i in range(360):
    z = z * (1 + 0.01j)
    t.goto(z.real * 100, z.imag * 100)
turtle.done()
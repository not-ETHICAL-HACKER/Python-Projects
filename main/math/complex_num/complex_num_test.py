import cmath,turtle,winsound
turtle.bgcolor("black")
t = turtle.Turtle(visible=False)
t.color("white")
z = 0 + 1j
for i in range(10_000):
    z *= 1 + 0j
    t.goto(z.real * 100, z.imag * 100)
    #!winsound.Beep(700, 50)  # Beep sound
turtle.done()
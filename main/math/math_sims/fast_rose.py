import turtle
import math

scale = 250
pi_scale = 100
two_pi = int(2 * math.pi * pi_scale) * 10 

t = turtle.Turtle(visible=False)
t.speed(0)
turtle.tracer(0, 0)  # ← disable all animation

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta"]

def rose(n: float, phase: float = 0) -> None:
    turtle.bgcolor("black")

    step = 2  # ← increase for fewer points (try 2-5, visually identical)
    total = two_pi * 2  # range is -two_pi to two_pi
    segment = total // (10 * step)

    interval = 1
    first = True

    for i in range(-two_pi, two_pi, step):
        # colour segmenting
        if i % (segment * step * step) == 0 or first:
            t.color(colors[(interval - 1) % len(colors)])
            interval += 1

        phase += math.radians(10)
        angle = i / pi_scale + phase
        r = math.cos(n * angle) * scale
        x = r * math.cos(angle)
        y = r * math.sin(angle)

        if first:
            t.penup()
            t.goto(x, y)
            t.pendown()
            first = False
        else:
            t.goto(x, y)
        if i % 1_00 == 0:  # ← flush every 100k points (try 10k-1M, visually identical)
            turtle.update()
    turtle.update()  # ← single flush at the end

rose(math.pi)
print("done")
turtle.done()
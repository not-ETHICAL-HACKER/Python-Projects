import turtle, random, math,time

turtle.tracer(0, 0)
turtle.bgcolor("black")

random.seed(0)

helper = turtle.Turtle(visible=False)
helper.color("red")
helper_2 = turtle.Turtle(visible=False)
helper_2.color("white")
helper_3 = turtle.Turtle(visible=False)
helper_3.color("blue")

class Particle:
    def __init__(self, radius, omega, phase):
        self.radius = radius
        self.omega = omega
        self.phase = phase

    def pos(self, t):
        angle = self.omega * t + self.phase
        x = self.radius * math.cos(angle)
        y = self.radius * math.sin(angle)
        return x, y
# Randomised Epicycles
arr = [Particle(random.randint(10, 10), random.uniform(0.1, 1.0), random.uniform(0, math.tau)) for _ in range(100)]
# # Square Wave Generator
arr = [Particle(150 * (4 / (math.pi * i)), i * 0.2, 0) for i in range(1,10**3)]
arr = [
    Particle(150, 1, 0),
    Particle(90, 2, math.pi/6),
    Particle(60, 5, math.pi/4),
    Particle(40, 8, math.pi/3),
    Particle(25, 13, math.pi/2),
    Particle(15, 21, math.pi),
]
arr = [
    Particle(75, 1, 0),
    Particle(25, -3, 0),
]
arr = [
    Particle(120, 1, 0),
    Particle(60, -7, 0),
]
arr = [
    Particle(100, 1, 0),
    Particle(80, math.sqrt(2), math.pi/4),
    Particle(60, math.pi, math.pi/3),
    Particle(40, math.e, math.pi/5),
]
arr = [
    Particle(150, 1, 0),
    Particle(90, 2, math.pi/6),
    Particle(60, 5, math.pi/4),
    Particle(40, 8, math.pi/3),
    Particle(25, 13, math.pi/2),
    Particle(15, 21, math.pi),
]
arr = [
    Particle(100,30,0),
    Particle(100,30*math.pi,0),
    Particle(100,30*math.tau,0)
    
]
t = 0
while True:
    # time.sleep(0.1)
    x = y = 0
    helper.clear()
    helper_3.clear()
    for p in arr:
        dx, dy = p.pos(t)
        #! to see the epicycles
        helper.penup()
        helper.goto(x, y)
        helper.pendown()
        helper.goto(x + dx, y + dy)
        x += dx
        y += dy
    #! to see the path of the last epicycle
    helper_3.penup()
    helper_3.goto(0, 0)
    helper_3.pendown()
    helper_3.goto(x, y)
    if t == 0:
        helper_2.penup()
    else:
        helper_2.pendown()
    helper_2.goto(x, y)

    turtle.update()
    t += 0.001
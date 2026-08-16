import turtle,math,random
turtle.tracer(0)
turtle.bgcolor("black")
class Particle(turtle.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.1)
        self.x = x
        self.y = y
        self.original_x = x
        self.original_y = y
        self.vx = 0 #math.cos(math.sqrt(abs(self.x)))
        self.vy = math.sin(self.x * math.pi/4)
        self.ax = 0
        self.ay = 1
        self.abs_extend_lim = 100
        self.drag = 0.1
    def bounce_back(self):
        dx = self.original_x - self.x
        dy = self.original_y - self.y
        hyp = max(math.hypot(dx,dy),1e-3)
        ux,uy = dx/hyp,dy/hyp
        self.vy += uy * (1 - self.drag) * hyp
        self.vx += ux * (1 - self.drag) * hyp + random.uniform(-1e-3,1e-3)
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if abs(self.y) > self.abs_extend_lim:
            self.y = self.abs_extend_lim * (1 if self.y > 0 else -1)
            self.vy *= -(1 - self.drag)
        self.goto(self.x * scale,self.y * scale)
scale = 100
N = 200
density = 50 #! out of 100
step = 1/density
particles = []
atoms = []
spacing = 5 * step
start_x = (N - 1) * spacing / 2
for i in range(N):
    P = Particle(start_x - i * spacing, 0)
    particles.append(P)
from time import sleep 
while True:
    sleep(1/30)
    for p in particles:
        p.clear()
    for p in particles:
        p.bounce_back()
        p.update()
    turtle.update()
turtle.done()
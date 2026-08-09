import turtle,math,random
turtle.tracer(0)
turtle.bgcolor("black")
class Atom(turtle.Turtle):
    def __init__(self,x,y,interaction_radius,abs_radius) -> None:
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.x = x
        self.y = y
        self.penup()
        self.goto(x,y - interaction_radius)
        self.pendown()
        self.circle(interaction_radius)
        self.penup()
        self.goto(x,y)
        self.interaction_radius = interaction_radius
        self.abs_radius = abs_radius
x_lim = 200
y_lim = 200
out_bounds_sqr = x_lim**2 + y_lim**2
class Particle(turtle.Turtle):
    def __init__(self,y,q,c):
        super().__init__()
        self.color(c)
        self.hideturtle()
        self.shapesize(.125,.125)
        self.x = -250
        self.y = y
        self.is_in = False
        self.penup()
        self.goto(self.x,self.y)
        # self.pendown()
        self.q = q
        self.vx = 1
        self.vy = random.uniform(-1e-9,1e-9)
        # self.m = 1.6 * 10 ** -27 if q > 0 else 9.1 * 10 ** -31
    
    def update(self):
        theta = None
        if self.x**2 + self.y**2 > out_bounds_sqr:
            theta = math.degrees(math.atan2(self.vy, self.vx))
            self.clear()
            self.x = -250
            self.y = random.uniform(-interaction_radius, interaction_radius)
            self.vx = 1
            self.vy = random.uniform(-1e-9, 1e-9)
            self.penup()
            self.goto(self.x,self.y)
            # self.pendown()
        else:
            self.x += self.vx
            self.y += self.vy
            self.goto(self.x,self.y)
        return theta
    
    def move(self,other:Atom):
        dx = other.x - self.x
        dy = other.y - self.y
        hyp = max(math.hypot(dx,dy),1e-9)
        ux = dx / hyp
        uy = dy / hyp
        if hyp <= other.abs_radius:
            k = 10**3 * 1/hyp
            decay = ((k)/hyp ** 2)
            self.vy -= uy * decay
            self.vx -= ux * decay
        elif hyp <= other.interaction_radius:
            self.is_in = True
            k = 10
            decay = ((k)/hyp ** 2)
            self.vy -= uy * decay
            self.vx -= ux * decay
        else:
            if self.is_in:
                self.is_in = False
                return
N = 500
density = 10 #! out of 100
step = 1/density
particles = []
atoms = []
spacing = 5 * step
start_y = (N - 1) * spacing / 2
for i in range(N):
    P = Particle(start_y - i * spacing, 1, "blue")
    P.shape("circle")
    P.showturtle()
    particles.append(P)
interaction_radius = 100
Central = Atom(0,0,interaction_radius,5)
atoms.append(Central)
import time
c = 0
angles = []
while True:
    if len(angles) >= 1_000:
        break
    # time.sleep(.1)
    for A in atoms:
        for p in particles:
            p.move(A)
    for p in particles:
        deg = p.update()
        if deg is not None:
            angles.append(abs(int(deg)))
            turtle.title(f"Angles : {len(angles)}")
    turtle.update()

import matplotlib.pyplot as plt
plt.hist(angles, bins=180, color = "blue" , edgecolor='black', alpha=0.7)
plt.xlabel('Scattering Angle $\\theta$ (degrees)')
plt.ylabel('Number of Particles (Counts)')
plt.title('Rutherford Scattering Simulation')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
turtle.done()
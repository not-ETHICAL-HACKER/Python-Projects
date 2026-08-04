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
        self.vy = random.uniform(-1e-3,1e-3)
        # self.m = 1.6 * 10 ** -27 if q > 0 else 9.1 * 10 ** -31
    
    def update(self):
        theta = None
        if abs(self.x) > 300 or abs(self.y) > 500:
            theta = math.degrees(math.atan2(self.vy, self.vx))
            self.clear()
            self.x = -250
            self.y = random.uniform(-100, 100)
            self.vx = 1
            self.vy = random.uniform(-1e-3, 1e-3)
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
            k = 10**3 * min(10**3,1/hyp)
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
N = 1000
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
Central = Atom(0,0,100,5)
atoms.append(Central)
import time
c = 0
angles = []
import matplotlib.pyplot as plt

while True:
    if len(angles) >= 500:
        break
    # time.sleep(.1)
    for A in atoms:
        for p in particles:
            p.move(A)
    for p in particles:
        deg = p.update()
        if deg is not None:
            angles.append(deg)
    turtle.update()

plt.hist(angles, bins=1000)
plt.show()
turtle.done()
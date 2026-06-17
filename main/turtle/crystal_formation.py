import math,random,turtle

random.seed(1)

class Crystal(turtle.Turtle):
    def __init__(self, x,y):
        super().__init__()
        self.shape("circle")
        self.x = x
        self.y = y
        self.color("blue")
        self.shapesize(0.05,0.05)
        self.penup()
        self.crystal_rad = 10
        self.effective_rad = 100
        self.is_crystal = False
        self.goto(self.x,self.y)

    def browninan(self,other:"Crystal"):
        if not self.is_crystal:
            dx = other.x - self.x
            dy = other.y - self.y
            distance = max(math.hypot(dx,dy),0.1)
            if distance < self.effective_rad and other.is_crystal and random.random() < 0.0:
                ux = dx / distance
                uy = dy / distance
                pwr = 1 - distance/self.effective_rad
                self.x += ux * pwr
                self.y += uy * pwr
            if other.is_crystal and distance < self.crystal_rad:
                self.is_crystal = True
                self.color("red")
                cry.append(self)
                return
            rx = random.choice([-1,0,1])
            ry = random.choice([-1,0,1])
            self.x += rx
            self.y += ry
            self.goto(self.x,self.y)

turts:list[Crystal] = []
cry:list[Crystal] = []
turtle.tracer(0)
turtle.bgcolor("black")

for _ in range(100):
    if _ == 0:
        c = Crystal(0,0) #?seed coords
        c.is_crystal = True
        c.color("purple")
        turts.append(c)
        cry.append(c)
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    turts.append(Crystal(x,y))
max_len = len(turts)
while True:
    turts = [p for p in turts if not p.is_crystal]
    if len(turts) < max_len:
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        turts.append(Crystal(x,y))
    for p in turts:
        for o in cry:
            if p != o:
                p.browninan(o)
    turtle.update()
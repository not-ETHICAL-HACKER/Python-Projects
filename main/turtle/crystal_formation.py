import math,random,turtle

class Crystal(turtle.Turtle):
    def __init__(self, x,y):
        super().__init__()
        self.shape("circle")
        self.x = x
        self.y = y
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.penup()
        self.crystal_rad = 10
        self.effective_rad = 50
        self.is_crystal = False
        self.goto(self.x,self.y)

    def browninan(self,other:"Crystal"):
        if not self.is_crystal:
            dx = other.x - self.x
            dy = other.y - self.y
            distance = max(math.hypot(dx,dy),0.1)
            if distance < self.effective_rad and random.random() < 0.1:
                ux = dx / distance
                uy = dy / distance
                self.x += ux
                self.y += uy
            if other.is_crystal and distance < self.crystal_rad:
                self.is_crystal = True
                self.color("red")
            rx = random.choice([-1,0,1])
            ry = random.choice([-1,0,1])
            self.x += rx
            self.y += ry

turts = []

for _ in range(100):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    turts.append(Crystal(x,y))
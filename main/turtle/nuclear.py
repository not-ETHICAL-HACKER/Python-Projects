import  random,math,turtle

random.seed(1)
turtle.tracer(0)
turtle.bgcolor("black")

types = {
    "H" : {"color":"blue","radius":7.5,"effective_radius":100,"size":0.5},
    "D" : {"color":"red","radius":10,"effective_radius":100,"size":0.75},
    "T" : {"color":"green","radius":15,"effective_radius":100,"size":1},
    "He" : {"color":"yellow","radius":20,"effective_radius":100,"size":1.25},
    "n" : {"color":"purple","radius":5,"effective_radius":100,"size":0.25} #neutron
}

class Particle(turtle.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("circle")
        self.attr = random.choice(list(types.keys()))
        self.x = x
        self.y = y
        self.color(types[self.attr]["color"])
        self.shapesize(0.1,0.1)
        self.penup()
        self.rad = types[self.attr]["radius"]
        self.effective_rad = types[self.attr]["effective_radius"]
        self.goto(self.x,self.y)
    
    def brownian(self,other:"Particle"):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = max(math.hypot(dx,dy),0.1)
        if distance < self.effective_rad and random.random() < 0.1:
            ux = dx / distance
            uy = dy / distance
            pwr = 1 - distance/self.effective_rad
            self.x += ux * pwr
            self.y += uy * pwr
        rx = random.choice([-1,0,1])
        ry = random.choice([-1,0,1])
        self.x += rx
        self.y += ry
        self.goto(self.x,self.y)
    
    def change(self,other:"Particle"):
        
        self.color(types[self.attr]["color"])
        other.color(types[other.attr]["color"])
        self.shapesize(types[self.attr]["size"],types[self.attr]["size"])
        other.shapesize(types[other.attr]["size"],types[other.attr]["size"])
        self.rad = types[self.attr]["radius"]
        other.rad = types[other.attr]["radius"]
        self.effective_rad = types[self.attr]["effective_radius"]
        other.effective_rad = types[other.attr]["effective_radius"]


    def collide(self,other:"Particle"):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = max(math.hypot(dx,dy),0.1)
        if distance < self.rad + other.rad:
            # Simple elastic collision response
            if self.attr == "H" and other.attr == "H":
                self.attr = "D"
                other.attr = "n"
                self.change(other)
            elif self.attr == "D" and other.attr == "H":
                self.attr = "T"
                other.attr = "D"
                self.change(other)
            elif self.attr == "T" and other.attr == "D":
                self.attr = "He"
                other.attr = "H"
                self.change(other)
            elif self.attr == "H" and other.attr == "n":
                self.attr = "D"
                other.attr = "H"
                self.change(other)

particles = [Particle(random.randint(-200,200),random.randint(-200,200)) for _ in range(50)]

while True:
    for p in particles:
        for other in particles:
            if p != other:
                p.brownian(other)
                p.collide(other)
    turtle.update()
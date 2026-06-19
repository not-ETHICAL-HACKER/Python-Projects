import  random,math,turtle,statistics as stat

random.seed(1)
turtle.tracer(0)
turtle.bgcolor("black")

types = {
    "H" : {"color":"blue","radius":7.5,"effective_radius":50,"size":0.5,"mass":1},
    "D" : {"color":"red","radius":10,"effective_radius":50,"size":0.75,"mass":2},
    "T" : {"color":"green","radius":15,"effective_radius":50,"size":1,"mass":3},
    "He" : {"color":"yellow","radius":20,"effective_radius":100,"size":1.25,"mass":4},
    "n" : {"color":"purple","radius":5,"effective_radius":0,"size":0.25,"mass":1} #neutron
}

class Particle(turtle.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape("circle")
        self.attr = random.choice(list(types.keys()))
        self.x = x
        self.y = y
        self.mass = types[self.attr]["mass"]
        self.energy_released = 0
        self.str = 1#6.6*1e-34
        self.color(types[self.attr]["color"])
        self.shapesize(0.1,0.1)
        self.penup()
        self.rad = types[self.attr]["radius"]
        self.effective_rad = types[self.attr]["effective_radius"]
        self.goto(self.x,self.y)
    
    def density_check(self,other:"Particle"):
    
        dx = other.x - self.x
        dy = other.y - self.y
        distance = max(math.hypot(dx,dy),0.1)
        if distance < self.rad + other.rad:
            ux = dx / distance
            uy = dy / distance
            pwr = -min(10,(self.rad+other.rad)/distance) / 2
            self.x += ux * pwr
            self.y += uy * pwr
            other.x += ux * -pwr
            other.y += uy * -pwr
        self.goto(self.x,self.y)
            
    def brownian(self):
        rx = random.choice([-1,0,1]) * self.str
        ry = random.choice([-1,0,1]) * self.str
        self.x += rx
        self.y += ry
        self.goto(self.x,self.y)
        
    def update(self,other:"Particle"):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = max(math.hypot(dx,dy),0.1)
        if distance < self.effective_rad and random.random() < .1:
            ux = dx / distance
            uy = dy / distance
            factor = random.uniform(-.1,0)
            pwr = (1 - (distance/self.effective_rad-factor))
            self.x += ux * pwr
            self.y += uy * pwr
    
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
            total_mass = self.mass + other.mass
            if self.attr == "H" and other.attr == "H":
                self.attr = "D"
                other.attr = "n"
                energy = 1.44 # in Mev
                self.energy_released += energy * other.mass/total_mass
                other.energy_released += energy * self.mass/total_mass 
                self.change(other)
            elif self.attr == "D" and other.attr == "H":
                self.attr = "T"
                other.attr = "D"
                energy = 0 # in Mev
                self.energy_released += energy * other.mass/total_mass
                other.energy_released += energy * self.mass/total_mass 
                self.change(other)
            elif self.attr == "T" and other.attr == "D":
                self.attr = "He"
                other.attr = "H"
                energy = 19.8 # in Mev
                self.energy_released += energy * other.mass/total_mass
                other.energy_released += energy * self.mass/total_mass 
                self.change(other)
            elif self.attr == "H" and other.attr == "n":
                self.attr = "D"
                other.attr = "H"
                energy = 2.22 # in Mev
                self.energy_released += energy * other.mass/total_mass
                other.energy_released += energy * self.mass/total_mass
                self.change(other)

particles = [Particle(random.randint(-200,200),random.randint(-200,200)) for _ in range(50)]

while True:
    arr = [p.energy_released for p in particles]
    turtle.title(f"mean:{stat.mean(arr):.2f},median:{stat.median(arr):.2f},std_dev:{stat.stdev(arr):.2f}")
    for p in particles:
        p.brownian()
        for other in particles:
            if p != other:
                p.density_check(other)
                
                p.update(other)
                p.collide(other)
                
    turtle.update()
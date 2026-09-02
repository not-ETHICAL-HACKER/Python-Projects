"""This is just  a prototype for pygame model"""
#! prey should have greater fov than predators
#! children should be born after enough time AND energy
#! children inherit genes using random.gauss(parent_trait, mutation)
#! predators lose energy while moving
#! prey gain energy by grazing
#! predators gain energy by eating prey
#! aging system (older organisms reproduce less efficiently)
#! memory/cooldown so predators don't switch targets every frame
#! camouflage: prey detected only within a reduced range
import turtle,random,math,statistics
turtle.bgcolor("black")
"""
# Forward vector (fx, fy) = the direction the particle is facing.
# It should NOT be the particle's position (x, y).
#
# If you know the previous position:
#     dx = current_x - previous_x
#     dy = current_y - previous_y
#
# Or if you already have velocity:
#     dx = vx
#     dy = vy
#
# Then normalize it:
#     dist = sqrt(dx*dx + dy*dy)
#     fx = dx / dist
#     fy = dy / dist
#
# fx, fy can then be used for:
# - Checking if prey is in front (dot product)
# - Determining whether to turn left or right (cross product)
# - Rotating the predator sprite to face the movement direction
#
# If the predator stops moving (dist == 0), keep the previous fx, fy
# so it continues facing the last direction it moved.
"""

def mex_hat(r,sigma = 50):
    x = r/sigma
    return - (1 - x*x) * math.exp(-x*x/2)

interaction_matrix = {
    "prey" : {
        "prey" : 1,
        "pred" : -1
    },
    "pred":{
        "prey" : 1,
        "pred" : 1
    }
}

colors = {
    "prey" : "blue",
    "pred" : "red"
}

fov = {
    "prey" : 120,
    "pred" : 45
}

import csv
with open("particle_log.csv","w") as f:
    w = csv.writer(f)
    w.writerow(("time","pop","prey","pred"))
def log(file:str,arr):
    with open(file,"a",newline="") as f:
        w = csv.writer(f)
        w.writerow(arr)

class Food(turtle.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.x = x
        self.y = y
        self.shape("circle")
        self.shapesize(1,1)
        self.rad = 10
        self.hp = 100
        self.color("green")
        self.exhausted = False
        self.goto(x,y)
        self.strength = 100
    
    def eat(self,prey:"Particle"):
        if prey.type != "prey":
            return
        dx = self.x - prey.x
        dy = self.y - prey.y
        
        hyp = max(0.1,math.hypot(dx,dy))
        
        ux = dx/hyp
        uy = dy/hyp
        food_range = 100

        if hyp < food_range:
            force = 0.05 * (1 - hyp / food_range)

            prey.vx += force * ux
            prey.vy += force * uy
        
        if hyp < self.rad:
            self.hp -= 1
            prey.energy += 10
            if self.hp < 0:
                self.hideturtle()
                self.exhausted = True

class Particle(turtle.Turtle):
    
    def __init__(self,x,y,id):
        super().__init__()
        self.type = random.choices(list(colors.keys()),weights=(8/10,2/10))[0]
        self.particle_size = 1
        
        self.penup()
        self.shape("circle")
        self.shapesize(self.particle_size/10, self.particle_size/10)
        self.color(colors[self.type])
        
        self.dead = False
        self.age = 0
        self.id = id
        self.t_id = None
        self.drag = 0.01
        self.max_energy = random.gauss(9_00,100)
        self.target_dist = -1
        self.energy = self.max_energy
        self.energy_efficiency = (1 - random.uniform(0,0.8) + (0.2 if self.type == "prey" else 0))
        
        self.x = x
        self.y = y
        self.fx = random.uniform(-1,1)
        self.fy = random.uniform(-1,1)
        
        dist = math.hypot(self.fx,self.fy)
        if dist > 0 :
            self.fx = self.fx/dist
            self.fy = self.fy/dist

        self.mutation_chance = random.random()
        self.aggression = 1 - random.random()
        self.hp = random.gauss(100,10)
        
        self.max_time = 10
        self.sex_timer = 0
        self.had_sex = False
        self.time = 0
        
        self.vx = 0
        self.vy = 0
        self.max_vel = 5

        self.inner_radius = abs(random.gauss(20,5))
        self.max_radius = random.gauss(100,10)
        self.abs_radius = self.particle_size * 2
        #! ignore fov for now bcs  its kinda diff to implement
        self.fov = fov[self.type] #? in degrees
        self.limit = math.cos(math.radians(self.fov/2))

    def defend(self,other:"Particle"):
        if self.type == "prey" and other.type == "pred":
            #! add aggresion to sex ,ie more aggresion more sex
            if random.random() < self.aggression:
                other.hp -= random.uniform(5,10)

    def browninan_motion(self):
        self.vx += random.uniform(-0.05,0.05)
        self.vy += random.uniform(-0.05,0.05)
        
    def border_check(self, width, height,circle=False):
        if not circle:
            if self.x < -width//2:
                self.x = -width//2
                self.vx *= -0.95
            elif self.x > width//2:
                self.x = width//2
                self.vx *= -0.95
            if self.y < -height//2:
                self.y = -height//2
                self.vy *= -0.95
            elif self.y > height//2:
                self.y = height//2
                self.vy *= -0.95
    
    def  die(self):
        self.hideturtle()
        self.dead = True
        return f"{self.id} ,type:{self.type} ,age:{self.age}"
        
    
    def survive(self):
        #! add grazing or idk smth
        if self.type == "prey":
            ...
    def calculate_sigma(self, elements):
        """Calculates standard deviation. Returns 0 if not enough elements."""
        if len(elements) < 2:
            return 0.0
        # statistics.stdev uses sample standard deviation (N-1)
        # Use statistics.pstdev(elements) if you want strict population standard deviation (N)
        return statistics.stdev(elements)

    def sex(self, other: "Particle", arr: list["Particle"]):
        if self.type != other.type or self.age < 50:
            return
        
        combined_energy = self.energy + other.energy
        if combined_energy < 2000:
            return
        
        self.had_sex = other.had_sex = True
        
        avg_x = (self.x + other.x) / 2
        avg_y = (self.y + other.y) / 2
        
        child_mutation = self.calculate_sigma((self.mutation_chance , other.mutation_chance))
        
        # Safe ID allocation
        next_id = (arr[-1].id + 1) if arr else 0
        
        parent_genes = {
            "max_energy": (self.max_energy, other.max_energy, self.calculate_sigma((self.max_energy, other.max_energy))*child_mutation),  # (ParentA, ParentB, Sigma/MutationRate)
            "max_radius": (self.max_radius, other.max_radius, self.calculate_sigma((self.max_radius, other.max_radius))*child_mutation),
            "energy_efficiency" : (self.energy_efficiency,other.energy_efficiency , self.calculate_sigma((self.energy_efficiency, other.energy_efficiency))*child_mutation),
            "drag" : (self.drag,other.drag,self.calculate_sigma((self.drag,other.drag))*child_mutation),
            "inner_radius" : (self.inner_radius,other.inner_radius,self.calculate_sigma((self.inner_radius,other.inner_radius))*child_mutation),
            "max_vel" : (self.max_vel,other.max_vel,self.calculate_sigma((self.max_vel,other.max_vel))*child_mutation),
            "hp" : (self.hp,other.hp,self.calculate_sigma((self.hp,other.hp))*child_mutation),
            "aggresion" : (self.aggression,other.aggression,self.calculate_sigma((self.aggression,other.aggression))*child_mutation)
        }
        
        child_genes = {}
        weight = random.random()  # Shared blend factor for this child's genetic makeup
        
        for trait, (val_a, val_b, mutation_rate) in parent_genes.items():
            # Crossover midpoint
            midpoint = (val_a * weight) + (val_b * (1.0 - weight))
            child_genes[trait] = random.normalvariate(midpoint, mutation_rate)

        child = Particle(avg_x, avg_y, next_id)
        child.type = self.type  # Inherit type directly
        child.mutation_chance = child_mutation
        
        # Assign mutated genes
        child.max_energy = child_genes["max_energy"]
        child.max_radius = child_genes["max_radius"]
        child.energy_efficiency = child_genes["energy_efficiency"]
        child.drag = child_genes["drag"]
        child.inner_radius = child_genes["inner_radius"]
        child.max_vel = child_genes["max_vel"]
        child.hp = child_genes["hp"]
        child.aggression = min(1,max(0,child_genes["aggresion"]))
        
        # Metabolic Tax: Parents split energy to gift to the child
        energy_gift = 400.0
        self.energy -= energy_gift / 2
        other.energy -= energy_gift / 2
        child.energy = energy_gift
        child.color("purple")
        
        # Add to ecosystem array
        arr.append(child)
        
    def update(self,other:"Particle"):
            # if self.age > 250 and self.max_energy*0.25 > self.energy:
            #     self.die()
            #! find the distance between the two particles
            dx = other.x - self.x
            dy = other.y - self.y

            dist = math.hypot(dx, dy)
            
            if dist < 1:
                dist = 1 #! avoid division by zero
            
            ux = dx / dist
            uy = dy / dist
            
            
            if self.time == self.max_time or dist > self.max_radius:
                self.time = 0
                self.t_id = None
            
            if other.type != self.type:
                if self.t_id is None or dist < self.target_dist:
                    self.t_id = other.id
                    self.target_dist = dist
            
            if dist < self.inner_radius and self.type == "pred" and other.type == "prey" and self.t_id == other.id:
                other.defend(self)
                self.energy += other.energy/10
                other.energy -= other.energy/20 - 10
                self.t_id = None
                return
            
            if self.t_id == other.id:
                dot = self.fx*ux +self.fy*uy
                if self.type == other.type:
                    pwr = interaction_matrix[self.type][other.type] * mex_hat(dist) #* (1 - dist/(self.max_radius + 1)) #! the closer they are the stronger the interaction
                else:
                    pwr = max(0,interaction_matrix[self.type][other.type] * (1 - dist/(self.max_radius + 1)))
                if dot > self.limit and self.t_id == other.id: #! target in fov
                    self.vx += pwr * ux
                    self.vy += pwr * uy
        
    def drag_force(self):
        
            self.vx *= (1-self.drag)
            self.vy *= (1-self.drag)

                
    def move(self):
        
            #! update position based on velocity
            
            self.vx = max(-self.max_vel,min(self.max_vel,self.vx))
            self.vy = max(-self.max_vel,min(self.max_vel,self.vy))
            
            self.x += self.vx
            self.y += self.vy
            
            dist = math.hypot(self.vx, self.vy)
            if dist > 0:
                self.fx = self.vx / dist
                self.fy = self.vy / dist
            else:
                self.fx = random.uniform(-1e-3,1e-3)
                self.fy = random.uniform(-1e-3,1e-3)
                
            #! update the turtle's position
            self.goto(self.x, self.y)
    def tick(self):
        self.age += 1
        self.time += 1
        self.energy += -random.uniform(0,0.1)*(self.age/100)*self.energy_efficiency
        if self.type == "pred":
            self.energy += -abs(max(self.vx,self.vy))*self.energy_efficiency

        if self.energy < 0:
            print(self.die())
            
        self.energy -= (
            random.uniform(0, 0.01)
            * math.log10(max(self.age, 10))
            * self.energy_efficiency
        )
num = 250
f_num = 10

turtle.tracer(0,0)

foods = [Food(random.uniform(-200,200),random.uniform(-200,200)) for _ in range(f_num)]
particles = [Particle(random.uniform(-200,200),random.uniform(-200,200),i) for i in range(num)]
CELL_SIZE = 100    
counter = 0
while True:
    # if random.random() < 0.01 and len(particles) < 250:
    #     particles.append(Particle(random.uniform(-200,200),random.uniform(-200,200),len(particles)))
    grid = {}
    particles = [p for p in particles if not p.dead]
    prey_num = sum([1 for p in particles if p.type == "prey"])
    pred_num = sum([1 for p in particles if p.type == "pred"])
    foods = [f for f in foods if not f.exhausted]
    if counter % 10 == 0:
        log("particle_log.csv",(counter,len(particles),prey_num,pred_num))
    counter += 1
    
    born = []
    for p in particles:

        cx = int(p.x // CELL_SIZE)
        cy = int(p.y // CELL_SIZE)

        if (cx, cy) not in grid:
            grid[(cx, cy)] = []

        grid[(cx, cy)].append(p) 
        
    for particle in particles:
                    
            cx = int(particle.x // CELL_SIZE)
            cy = int(particle.y // CELL_SIZE)

            particle.browninan_motion()
            particle.tick()
            if random.random() > 0.9:
                turtle.title(f"{len(particles)},{...}")
            for dx_cell in (-1, 0, 1):
                for dy_cell in (-1, 0, 1):

                    nearby = grid.get(
                        (cx + dx_cell, cy + dy_cell),
                        []
                    )

                    for other in nearby:

                        if particle is other:
                            continue
                        
                        if random.random() > 0.99 and not (particle.had_sex and other.had_sex):
                            particle.sex(other,born)
                        particle.update(other)
            
            for f in foods:
                f.eat(particle)
            particle.border_check(600, 600, circle=False)
            particle.drag_force()
            particle.move()
    
    particles.extend(born)
    
    turtle.update()
        
turtle.done()
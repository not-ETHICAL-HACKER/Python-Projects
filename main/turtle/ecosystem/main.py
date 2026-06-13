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

interaction_matrix = {
    "prey" : {
        "prey" : 2,
        "pred" : -1
    },
    "pred":{
        "prey" : 0.5,
        "pred" : -0.1
    }
}

colors = {
    "prey" : "blue",
    "pred" : "red"
}

fov = {
    "prey" : 180,
    "pred" : 45
}

class Food(turtle.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(2,2)
        self.hp = 100
        self.color("green")
        self.goto(x,y)

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
        self.max_energy = random.gauss(1_000)
        self.energy = self.max_energy
        self.energy_efficiency = (1 - random.random())
        self.x = x
        self.y = y
        self.fx = random.uniform(-1,1)
        self.fy = random.uniform(-1,1)
        dist = math.hypot(self.fx,self.fy)
        if dist > 0 :
            self.fx = self.fx/dist
            self.fy = self.fy/dist

        self.mutation_chance = random.random()
        
        self.max_time = 10
        self.time = 0
        
        self.vx = 0
        self.vy = 0

        self.inner_radius = 5
        self.max_radius = 100
        self.abs_radius = self.particle_size * 2
        #! ignore fov for now bcs  its kinda diff to implement
        self.fov = fov[self.type] #? in degrees
        self.limit = math.cos(math.radians(self.fov/2))

    def browninan_motion(self):
        self.vx += random.uniform(-0.05,0.05)
        self.vy += random.uniform(-0.05,0.05)
        
    def border_check(self, width, height,circle=False):
        if not circle:
            if self.x < -width//2:
                self.x = -width//2
                self.vx *= -1.05
            elif self.x > width//2:
                self.x = width//2
                self.vx *= -1.05
            if self.y < -height//2:
                self.y = -height//2
                self.vy *= -1.05
            elif self.y > height//2:
                self.y = height//2
                self.vy *= -1.05
    
    def  die(self):
        self.hideturtle()
        self.dead = True
    
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
        if self.type != other.type:
            return
            
        combined_energy = self.energy + other.energy
        if combined_energy < 2000:
            return

        avg_x = (self.x + other.x) / 2
        avg_y = (self.y + other.y) / 2
        
        child_mutation = self.calculate_sigma((self.mutation_chance , other.mutation_chance))
        
        # Safe ID allocation
        next_id = (arr[-1].id + 1) if arr else 0
        
        parent_genes = {
            "max_energy": (self.max_energy, other.max_energy, self.calculate_sigma((self.max_energy, other.max_energy))*child_mutation),  # (ParentA, ParentB, Sigma/MutationRate)
            "max_radius": (self.max_radius, other.max_radius, self.calculate_sigma((self.max_radius, other.max_radius))*child_mutation),
            "energy_efficiency" : (self.energy_efficiency,other.energy_efficiency , self.calculate_sigma((self.energy_efficiency, other.energy_efficiency))*child_mutation)
            
        }
        
        child_genes = {}
        weight = random.random()  # Shared blend factor for this child's genetic makeup
        
        for trait, (val_a, val_b, mutation_rate) in parent_genes.items():
            # Crossover midpoint
            midpoint = (val_a * weight) + (val_b * (1.0 - weight))
            # Apply Gaussian variation
            child_genes[trait] = random.normalvariate(midpoint, mutation_rate)

        child = Particle(avg_x, avg_y, next_id)
        child.type = self.type  # Inherit type directly
        child.mutation_chance = child_mutation
        
        # Assign mutated genes
        child.max_energy = child_genes["max_energy"]
        child.max_radius = child_genes["max_radius"]
        
        # Metabolic Tax: Parents split energy to gift to the child
        energy_gift = 400.0
        self.energy -= energy_gift / 2
        other.energy -= energy_gift / 2
        child.energy = energy_gift
        
        # Add to ecosystem array
        arr.append(child)
    
    def update(self,other:"Particle"):
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
                
            if self.t_id is None and other.type != self.type and dist < self.max_radius:
                self.t_id = other.id
            
            if dist < self.inner_radius and self.type == "pred" and other.type == "prey" and self.t_id == other.id:
                self.energy += 10
                other.energy -= 20
                self.t_id = None
                return
            
            if self.energy < 0:
                self.die()
            
            if dist > self.max_radius:
                return
            if self.t_id == other.id:
                dot = self.fx*ux +self.fy*uy
                pwr = interaction_matrix[self.type][other.type] * (1 - dist/(self.max_radius + 1)) #! the closer they are the stronger the interaction
                if dot > self.limit and self.t_id == other.id: #! target in fov
                    self.vx += pwr * ux
                    self.vy += pwr * uy
        
    def drag_force(self):
        
            self.vx *= (1-self.drag)
            self.vy *= (1-self.drag)

                
    def move(self):
        
            #! update position based on velocity
            
            self.x += self.vx
            self.y += self.vy
            
            dist = math.hypot(self.vx, self.vy)
            if dist > 0:
                self.fx = self.vx / dist
                self.fy = self.vy / dist
            else:
                self.fx = 0
                self.fy = 0
                
            #! update the turtle's position
            self.goto(self.x, self.y)
    def tick(self):
        self.age += 1
        
        self.time += 1
        self.energy += -random.uniform(0,0.01)*math.log10(self.age)*self.energy_efficiency

        self.energy -= (
            random.uniform(0, 0.01)
            * math.log10(max(self.age, 10))
            * self.energy_efficiency
        )
        if random.random() > 0.9:
            particle.sex(other,particles)
num = 250
turtle.tracer(0,0)
particles = [Particle(random.uniform(-200,200),random.uniform(-200,200),i) for i in range(num)]
CELL_SIZE = 100    
while True:
    if random.random() < 0.01 and len(particles) < 250:
        particles.append(Particle(random.uniform(-200,200),random.uniform(-200,200),len(particles)))
    grid = {}
    particles = [p for p in particles if not p.dead]
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
            for dx_cell in (-1, 0, 1):
                for dy_cell in (-1, 0, 1):

                    nearby = grid.get(
                        (cx + dx_cell, cy + dy_cell),
                        []
                    )

                    for other in nearby:

                        if particle is other:
                            continue
                        particle.update(other)
            particle.border_check(600, 600, circle=False)
            particle.drag_force()
            particle.move()
    turtle.update()
        
turtle.done()
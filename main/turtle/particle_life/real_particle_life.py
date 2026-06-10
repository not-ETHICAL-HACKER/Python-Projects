import random,turtle,math
n_c = 3

t_colors = ["red", "green", "blue", "yellow", "purple", "orange", "cyan", "magenta"]
charges = {
    c1: random.uniform(-1, 1) for c1 in t_colors
}
mass = {
    c1: random.uniform(0.1,1) for c1 in t_colors
}
# charges = {
#     c1: random.choice([-1.6,0,1.6]) for c1 in t_colors 
# }
# mass = {
#     c1: random.choice([1.6,1.6,0.09]) for c1 in t_colors
# }
turtle.tracer(0)
turtle.bgcolor("black")

def fix_probs(prob, n, max_len):
    if not prob:
        prob = [random.random() for _ in range(n)]

    prob = prob[:max_len]
    prob.extend([0] * (max_len - len(prob)))

    return prob

prob_col = fix_probs([], n_c, len(t_colors))

class Particle(turtle.Turtle):
    def __init__(self,x,y,color_name,rgb_color):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.1, 0.1)
        self.color_name = color_name
        self.color(color_name)
        self.rgb_color = rgb_color    
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.mass = mass[color_name]
        self.charge = charges[color_name]
        self.particle_size = 1
        self.inner_radius = 25
        self.abs_radius = self.particle_size * 2
        self.drag = 0.1
        self.density = 0.0 # only for testing remove if too complex
        self.density_limit = 2.0 # only for testing remove if too complex
        self.dist = 0
        self.G = 6.6743 #! gravitational constant
        self.K = 8.9873 #! electrostatic constant
    
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
        else:
            w2 = width//2
            h2 = height//2
            radius = min(w2, h2)
            dx = self.x - w2
            dy = self.y - h2
            self.dist = math.hypot(dx, dy)
            if self.dist > radius:
                angle = math.atan2(dy, dx)
                self.x = w2 + radius * math.cos(angle)
                self.y = h2 + radius * math.sin(angle)
                self.vx *= -1
                self.vy *= -1

    def gravity(self,other:"Particle",attraction=True):
        dx = other.x - self.x
        dy = other.y - self.y
        
        if attraction:
            sign = 1
        else:
            sign = -1
        
        self.dist = (self.x-other.x)**2 + (self.y-other.y)**2
        if self.dist < self.abs_radius**2:
            ...
        if self.dist < self.inner_radius**2:
            ...
        if self.dist > self.inner_radius**2:
            
            F = self.G * self.mass * other.mass / self.dist
            hyp = math.sqrt(self.dist)
            
            ux = dx / hyp
            uy = dy / hyp
            
            self.vx += sign * F * ux / self.mass 
            self.vy += sign * F * uy / self.mass    
        
    def electrostatic(self,other:"Particle",attraction=True):
        dx = other.x - self.x
        dy = other.y - self.y
        if attraction:
            sign = 1
        else:
            sign = -1
        self.dist = (self.x-other.x)**2 + (self.y-other.y)**2
        if self.dist < self.abs_radius**2:
            ...
        if self.dist < self.inner_radius**2:
            ...
        if self.dist > self.inner_radius**2:
            
            F =  - self.K * sign * self.charge * other.charge / self.dist#! minus is used to make like charges repel and opposite charges attract
            hyp = math.sqrt(self.dist)
            
            ux = dx / hyp
            uy = dy / hyp
            
            self.vx +=  F * ux / self.mass
            self.vy +=  F * uy / self.mass
    
    def interact(self,other:"Particle"):
        
        if self.dist < self.abs_radius:
            dx = other.x - self.x
            dy = other.y - self.y
            
            hyp = math.sqrt(self.dist)
            
            ux = dx / hyp
            uy = dy / hyp
            
            
            overlap_factor = 1.0 - (hyp / self.abs_radius)
            
            repulsion_force = overlap_factor * 2.0  # Adjust 2.0 to make them softer or stiffer
            
            self.vx += - repulsion_force * ux
            self.vy += - repulsion_force * uy
            
        
        if self.color_name == other.color_name:
            self.density += 1 - self.dist/(self.inner_radius**2)
        else:
            self.density += (1 - self.dist/(self.inner_radius**2)) * 0.5
    
    def forces(self,other:"Particle"):
        self.gravity(other)
        self.electrostatic(other)
        self.interact(other)
        
        density_factor = 1 - min(max(0, self.density - self.density_limit),2.0)
            
        if self.vx > 0:
            self.vx *= density_factor
        if self.vy > 0:
            self.vy *= density_factor
            
    
    def drag_force(self):
        self.vx *= (1 - self.drag)
        self.vy *= (1 - self.drag)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.goto(self.x, self.y)
    
    def show_rad(self):
        self.goto(x,y-self.inner_radius)
        self.pendown()
        self.circle(self.inner_radius)
        self.penup()
    
particles: list[Particle] = []
   
for _ in range(2_00):
    x = random.uniform(-300, 300)
    y = random.uniform(-300, 300)
    color = random.choices(t_colors, k=1, weights=prob_col)[0]
    rgb_color = (0, 0, 0) # placeholder for rgb color
    particles.append(Particle(x, y,color,rgb_color))
CELL_SIZE = 100    
while True:
    for i, p1 in enumerate(particles):
        p1.density = 0.0
        for j, p2 in enumerate(particles):
            if i != j:
                p1.forces(p2)
        p1.border_check(800, 700, circle=False)
        p1.drag_force()
        p1.update()
    turtle.update()

    density = 0.0
    
    grid = {}

    for p in particles:
        # Check this cell and its 8 neighboring cells.
        # Since CELL_SIZE ~= interaction radius,
        # particles farther than one cell away cannot interact.
        # This reduces the search from all particles
        # to only nearby particles.
        cx = int(p.x // CELL_SIZE)
        cy = int(p.y // CELL_SIZE)

        if (cx, cy) not in grid:
            grid[(cx, cy)] = []

        grid[(cx, cy)].append(p)    
        for particle in particles:
            
            particle.density = 0.0 # only for testing remove if too complex  
                    
            cx = int(particle.x // CELL_SIZE)
            cy = int(particle.y // CELL_SIZE)

            for dx_cell in (-1, 0, 1):
                for dy_cell in (-1, 0, 1):

                    nearby = grid.get(
                        (cx + dx_cell, cy + dy_cell),
                        []
                    )

                    for other in nearby:

                        if particle is other:
                            continue
                        
                        
                        p1.forces(p2)
            p1.border_check(800, 700, circle=False)
        p1.drag_force()
        p1.update()
    turtle.update()
        
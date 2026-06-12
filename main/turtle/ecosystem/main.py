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
import turtle,random,math
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
        "prey" : 0.1,
        "pred" : -1
    },
    "pred":{
        "prey" : 1,
        "pred" : 0.1
    }
}

colors = {
    "prey" : "blue",
    "pred" : "red"
}

fov = {
    "prey" : 30,
    "pred" : 45
}
class Particle(turtle.Turtle):
    
    def __init__(self,x,y,id):
        super().__init__()
        self.type = random.choice(list(colors.keys()))
        self.particle_size = 1
        
        self.penup()
        self.shape("circle")
        self.shapesize(self.particle_size/10, self.particle_size/10)
        self.color(colors[self.type])
        
        self.dead = False
        self.id = id
        self.t_id = 0
        self.drag = 0.1
        
        self.x = x
        self.y = y

        self.prev_x = 0
        self.prev_y = 0
        
        self.max_time = 100
        self.time = 0
        
        self.vx = 0
        self.vy = 0

        #! avoid using fx and fy bcs its too hard for me to implement
        self.fx = random.uniform(-1, 1) #! this is where the particle is pointing by finding (new x - old x)/hyp do some dot or cross product shenanigans to find resultant between these vectors and vector pointing to other particle
        self.fy = random.uniform(-1, 1) #! fx means forward vector ie where particle is moving irrespective of where its target is
        dist = math.hypot(self.fx, self.fy)
        if dist > 0:
            self.fx /= dist
            self.fy /= dist
        else:
            self.fx = 0
            self.fy = 0

        self.inner_radius = 25
        self.max_radius = 100
        self.abs_radius = self.particle_size * 2
        #! ignore fov for now bcs  its kinda diff to implement
        self.fov = fov[self.type] #? in degrees
        self.limit = math.cos(math.radians(self.fov))

    def browninan_motion(self):
        ...
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
                
    def update(self,other:"Particle"):
            #! find the distance between the two particles
            dx = other.x - self.x
            dy = other.y - self.y

            dist = math.hypot(dx, dy)
            
            if dist < 1:
                dist = 1 #! avoid division by zero
            
            ux = dx / dist
            uy = dy / dist
            
            if dist < self.inner_radius and self.type == "pred" and other.type == "prey":
                other.die()
                return
            if dist > self.max_radius:
                return
            
            dot = self.fx*ux +self.fy*uy
            pwr = interaction_matrix[self.type][other.type] * (1 - dist/(self.max_radius + 1)) #! the closer they are the stronger the interaction
            if dot > self.limit: #! target in fov
                self.vx += pwr * ux
                self.vy += pwr * uy
            
    def move(self):
        
            #! update position based on velocity

            self.vx *= (1-self.drag)
            self.vy *= (1-self.drag)

            self.fx = self.prev_x - self.x
            self.fy = self.prev_y - self.y
            
            self.prev_x = self.x
            self.prev_y = self.y
            
            self.x += self.vx
            self.y += self.vy
            
            dist = math.hypot(self.fx, self.fy)
            if dist > 0:
                self.fx /= dist
                self.fy /= dist
            else:
                self.fx = 0
                self.fy = 0
                
            #! update the turtle's position
            self.goto(self.x, self.y)
num = 100
turtle.tracer(0,0)
particles = [Particle(random.uniform(-200,200),random.uniform(-200,200),i) for i in range(num)]
CELL_SIZE = 100    
while True:
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

            for dx_cell in (-1, 0, 1):
                for dy_cell in (-1, 0, 1):

                    nearby = grid.get(
                        (cx + dx_cell, cy + dy_cell),
                        []
                    )

                    for other in nearby:

                        if particle is other:
                            continue
                        
                        
                        p.update(other)
            p.border_check(800, 700, circle=False)
        p.move()
    turtle.update()
        
turtle.done()
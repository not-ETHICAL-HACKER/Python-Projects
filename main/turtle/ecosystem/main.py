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
        "prey" : 0.5,
        "pred" : -1
    },
    "pred":{
        "prey" : 1,
        "pred" : 0.1
    }
}

colors = {
    "prey" : "red",
    "pred" : "blue"
}

fov = {
    "prey" : 60,
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
        self.ax = 0#! use vx * dt to find ax and store it ig? 
        self.ay = 0#! also use clock func in pygame to acccuratelay find dt
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
                
    def update(self,other:"Particle"):
            #! find the distance between the two particles
            dx = other.x - self.x
            dy = other.y - self.y

            dist = math.hypot(dx, dy)
            
            if dist < 1:
                dist = 1 #! avoid division by zero
            
            ux = dx / dist
            uy = dy / dist
            
            if dist < self.inner_radius:
                #! do something when they are close enough (e.g. eat, reproduce, etc.)
                pass
            if dist > self.max_radius:
                return
            
            dot = self.fx*ux +self.fy*uy
            pwr = interaction_matrix[self.type][other.type]
            if dot > self.limit: #! target in fov
                self.ax += pwr * ux
                self.ay += pwr * uy
            
    def move(self):
        
            #! update position based on velocity
            self.x += self.vx
            self.y += self.vy
            
            self.fx = self.prev_x - self.x
            self.fy = self.prev_y - self.y
            dist = math.hypot(self.fx, self.fy)
            if dist > 0:
                self.fx /= dist
                self.fy /= dist
            else:
                self.fx = 0
                self.fy = 0
                
            #! update the turtle's position
            self.goto(self.x, self.y)
num = 10
particles = [Particle(random.uniform(-200,200),random.uniform(-200,200),i) for i in range(num)]
turtle.done()
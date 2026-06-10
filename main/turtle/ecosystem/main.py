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
class Particle(turtle.Turtle):
    
    def __init__(self,x,y,color_name,rgb_color):
        super().__init__()
        self.particle_size = 1
        self.rgb_color = rgb_color    
        self.color_name = color_name
        
        self.penup()
        self.shape("circle")
        self.shapesize(self.particle_size/10, self.particle_size/10)
        self.color(color_name)
        
        self.x = x
        self.y = y
        
        self.vx = 0
        self.vy = 0
        self.ax = 0#! use vx * dt to find ax and store it ig? 
        self.ay = 0#! also use clock func in pygame to acccuratelay find dt
        #! avoid using fx and fy bcs its too hard for me to implement
        self.fx = 0 #! this is where the particle is pointing by finding (new x - old x)/hyp
        self.fy = 0 #! do some dot or cross product shenanigans to find resultant between these vectors and vector pointing to other particle
        
        self.inner_radius = 25
        self.abs_radius = self.particle_size * 2
        #! ignore fov for now bcs  its kinda diff to implement
        self.fov = 0 #? in degrees

        
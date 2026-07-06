import turtle,math,random,time
turtle.tracer(0,0)
turtle.bgcolor("black")
turtle.colormode(255)
random.seed(0)
scale_factor = 10

class Particle(turtle.Turtle):
    def __init__(self,x,y,z,angle):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.angle = angle
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.s_z = 1/(0.1 + max(0, self.z))
        self.s_z = max(0.1, 1 + self.z/50)
        self.shapesize(0.1+math.log10(1+abs(self.s_z)),0.1+math.log10(1+abs(self.s_z)))
        self.speed(0)
    
    def brownian_motion(self):
        self.x += random.randint(-1, 1)*scale_factor
        self.y += random.randint(-1, 1)*scale_factor
        self.z += random.randint(-1, 1)*scale_factor
    
    def rotate(self,angle):
        scale = 100
        self.angle += angle
        rad = math.radians(self.angle)
        self.x = math.cos(rad)*scale
        self.y = math.sin(rad)*scale
        self.z = math.sin(rad)*scale
        
    def rotate_y(self, angle):
        rad = math.radians(angle)

        new_x = self.x*math.cos(rad) - self.z*math.sin(rad)
        new_z = self.x*math.sin(rad) + self.z*math.cos(rad)

        self.x = new_x
        self.z = new_z
    
    def rotate_x(self, angle):
        rad = math.radians(angle)

        new_y = self.y*math.cos(rad) - self.z*math.sin(rad)
        new_z = self.y*math.sin(rad) + self.z*math.cos(rad)

        self.y = new_y
        self.z = new_z
    
    def rotate_z(self, angle):
        rad = math.radians(angle)

        new_x = self.x*math.cos(rad) - self.y*math.sin(rad)
        new_y = self.x*math.sin(rad) + self.y*math.cos(rad)

        self.x = new_x
        self.y = new_y
        
    def update(self):
        self.s_z = max(0.1, 1 + self.z/50)
        # depth = 300
        # factor = depth / (depth + self.z + 300)#!commented code is ai

        # self.goto(self.x * factor, self.y * factor)
        self.goto(self.x, self.y)
        self.shapesize(0.1+math.log10(1+abs(self.s_z)),0.1+math.log10(1+abs(self.s_z)))
    
    def color_(self):
        v = int(self.s_z * 75) % 256

        # Near = blue, far = red
        self.color(255-v, 0, v)
    
    def randomiser(self,angle):
        roll = random.random()
        if roll < 0.33:
            self.rotate_x(angle)
        if roll > 0.33 and roll < 0.66:
            self.rotate_y(angle)
        else:
            self.rotate_z(angle)
arr = [Particle(random.randint(-100,100),random.randint(-100,100),random.randint(-100,100),random.randint(0,360)) for _ in range(1)]
angle = 1
while True:
    # time.sleep(0.01)
    if random.random() < 0.1:
        arr.append(Particle(random.randint(-100,100),random.randint(-100,100),random.randint(-100,100),random.randint(0,360)))
    for p in arr:
        p.rotate_x(angle)
        p.rotate_y(angle)
        p.rotate_z(angle)
    for p in arr:
        p.update()
        p.color_()
    turtle.update()
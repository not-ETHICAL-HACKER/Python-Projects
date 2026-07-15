import turtle,math,time
turtle.tracer(0, 0)
turtle.bgcolor("black")
pov = turtle.Turtle(shape = "turtle")
pov.color("red")
pov.penup()
pov.shapesize(2,2)
obj = turtle.Turtle(shape="circle")
obj.color("blue")
obj.penup()
obj.setx(100)

vy = 1e-3
g = 9.81
#!v(t) = v_t * tanh((g*t)/v_t)
#!v_t = sqrt((2*m*g)/(rho*C_d*A))
class FallingObject(turtle.Turtle):#? to implement multiple objs falling at same time
    def __init__(self, mass, radius, density_obj,color,shape, g=9.81, rho=1.225, C_d=0.47):
        super().__init__(shape=shape)
        self.mass = mass
        self.radius = radius
        self.density_obj = density_obj
        self.g = g
        self.rho = rho
        self.C_d = C_d
        self.area = math.pi * radius**2  # Cross-sectional area of the sphere
        self.v_t = self.calculate_terminal_velocity()
        self.penup()
        self.color(color)

    def calculate_terminal_velocity(self):
        """Calculate the terminal velocity of the object."""
        return math.sqrt((2 * self.mass * self.g) / (self.rho * self.C_d * self.area))

    def add_drag(self, t):
        """Calculate the velocity with drag at time t."""
        return self.v_t * math.tanh((self.g * t) / self.v_t)
    
def calculate_terminal_velocity(mass, g, rho, C_d, A):
    """Calculate the terminal velocity of an object."""
    return math.sqrt((2 * mass * g) / (rho * C_d * A))

#! let us assume the object is a sphere
materials = {
    "test1" : 100,
    "steel": 7800,
    "aluminum": 2700,
    "wood": 700,
    "ice": 917,
    "gold": 19300,
    "neutron_star_core":10 ** 18,
    "star_core": 1.4 * 10 **5, #? main sequence stars
    "white_dwarf": 10 ** 9
}
radius = 1  # in meters
density_obj = materials["gold"] # in kg/m^3
mass = (4/3) * math.pi * radius**3 * density_obj  # Mass of the sphere
area = math.pi * radius**2  # Cross-sectional area of the sphere

v_t = calculate_terminal_velocity(mass, g, rho=1.225, C_d=0.47, A=area)  # Example values for air density, drag coefficient, and cross-sectional area
def add_drag(v_t, t):
    """Calculate the velocity with drag at time t."""
    return v_t * math.tanh((g * t) / v_t)

t = 0

def rotate(angle,t:turtle.Turtle,v):
    ratio = v/v_t
    shake = 100 * (1 - ratio) ** 2  # Shake factor based on velocity
    shake_angle = (math.cos(angle)*shake - math.sin(angle)*shake) - 90
    ux = math.cos(math.radians(shake_angle))
    uy = math.sin(math.radians(shake_angle))
    t.seth(shake_angle)
    uy = math.sin(math.radians(angle))
    return ux,uy
angle = 0
diff = 1
time_diff = .001
dist = 0

print(f"Both Objects start falling at same time with initial velocity of {vy} m/s and terminal velocity of {v_t} m/s")
flag = True
def calc_energy(m,v):
    return 1/2 * m * v**2
while True:
    turtle.title(f"Time: {t:.1f}s, Velocity: {vy:.2f} m/s or {vy * 3.6:.2f} Kmph , Distance traveled {dist:.2f} m,Terminal Velocity: {v_t:,.2f} m/s")
    if vy/v_t > 0.95 and flag:
        energy = calc_energy(mass,vy) / 1000
        flag = False
        exp = 0
        tnt_energy = (energy*1000)/(4.14 * 10 ** 9)#! one ton tnt 4.184 × 10¹² joules
        print(f"Reached Terminal Velocity (mach {vy/343:.2f}) at {t:.2} s and dist {dist:.2} m  with rad {radius} m and density {density_obj} kg/m^3 with KE = {energy:.2f} KJ")
    t += time_diff
    vy = add_drag(v_t, t)
    dist += vy * time_diff
    angle += math.radians(diff)
    ux, uy = rotate(angle,pov,vy)
    pov.setx(pov.xcor() + ux)
    obj.sety(obj.ycor() + vy * time_diff)
    if obj.ycor() > 400:
        obj.sety(-400)
    # time.sleep(time_diff)
    turtle.update()
"""
project idea: procedural village generator

make a complete 2d village procedurally.

stuff it could have:
#!- terrain
#!- roads / paths
#!- houses and buildings
#!- farms / fields
#?- trees / forests
#!- rivers / lakes
#?- wells and random landmarks
#!- village center
#!!- buildings that actually make sense where they are
#!- houses mostly near roads
#?- farms near good land / water
#!!!!- seeds so the same village can be generated again

progression:
v1.x: random terrain + buildings
v2.x: roads connecting buildings
v3.x: make the placement actually logical
v4.x: multiple villages connected by roads
v5.x: simulate the village growing over time
v6.x: population, resources, migration, expansion, etc.

#!main goal:
make it look like an actual village that people built,
not just a bunch of random shit scattered around.

2d only for now.(use turtle for now later use pygame or smth)
#!!!!!!!!! IF USING TURTLE DO NOT MAKE A SHIT TON OF TURT OBJS OR THE PC WILL CRASH.

#//DO NOT START THIS BEFORE EXAMS.
"""
import turtle,math,random,time
random.seed(0) #seed for reproducibility
turtle.tracer(0)
turtle.colormode(255)
turtle.bgcolor((0,0,0))

class Helper(turtle.Turtle):
    def __init__(self,x,y,pen_c:tuple[int,int,int],h_size,h_shape):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color(pen_c)
        self.shapesize(h_size)
        self.shape(h_shape)
        self.x = x
        self.y = y
    def __repr__(self):
        return f"(x={self.x},y={self.y},color={self.color()},size={self.shapesize()},shape={self.shape()})"
    
    def print(self,tx,ty):
        self.goto(tx,ty)
        self.pendown()
        self.stamp()
        self.penup()
scale = .5
path_helpers = [
    Helper(0, 0, (255, 255, 255), scale * 1, "circle"),  #house 1.1
    Helper(0, 0, (127, 127, 127), scale * 2, "circle"),  #house 1.2
    Helper(0, 0, (255, 255, 255), scale * 1, "square"),  #house 2.1
    Helper(0, 0, (127, 127, 127), scale * 2, "square"),  #house 2.2
    Helper(0,0,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),scale * 1,"triangle"), # random landmark
    Helper(0,0,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),scale * 1,"turtle") # random landmark
]
Path = Helper(0,0,(240, 209, 110),scale * 1,"circle")
W = H = 200
cell_size = 10
cell_grid = {}
#! these loops are to seed building throught the world, but they are not very smart and will just place them randomly. v2.x will fix this.
for i in range(-W//cell_size, W//cell_size):
    for j in range(-H//cell_size, H//cell_size):
        if random.random() < 0.01: #? 1% chance to have a building in this cell
            cell_grid[(i, j)] = [random.choice(path_helpers)]
        else:
            cell_grid[(i, j)] = []
for x in cell_grid:
    for helper in cell_grid[x]:
        helper.print(x[0]*cell_size,x[1]*cell_size)
turtle.update()
buildings = [
    pos
    for pos, contents in cell_grid.items()
    if contents
]

while True:#! this loop to build paths from buildings is not very smart and will just connect them randomly. v2.x will fix this.
    for i, a in enumerate(buildings):
        for b in buildings[i + 1:]:
                    # if random.random() < 0.01: #? commented out bcs it just connected shortest path
                    #     Path.penup()
                    #     Path.goto(x[0]*cell_size,x[1]*cell_size)
                    #     Path.pendown()
                    #     Path.goto(y[0]*cell_size,y[1]*cell_size)
                    if random.random() < 0.01: #? 1% chance to connect these two buildings with a path
                        Path.penup()
                        x1,y1 = a
                        x2,y2 = b
                        dx = x2 - x1
                        dy = y2 - y1
                        hyp = math.hypot(dx,dy)
                        ux = dx/hyp
                        uy = dy/hyp
                        Path.goto(x1 * cell_size * ux,y1 * cell_size * uy) #! tring to simulate \operatorname{polygon}\left(\left(0,0\right),\left(\cos \left(a\right),0\right),\left(\cos \left(a\right),\sin \left(a\right)\right)\right) from desmos, but it is not working as intended. v2.x will fix this.
                        Path.goto(x1 * cell_size * ux,0)
                        Path.pendown()
                        Path.goto(x2 * cell_size * ux,y2 * cell_size * uy)
                        time.sleep(0.01)
    turtle.update()
    time.sleep(1/240) #? this is just to make it look like the village is being built over time, can be removed later
    if random.random() < 0.1:
        break
print([(x,cell_grid[x]) for x in cell_grid if cell_grid[x]])
turtle.done()
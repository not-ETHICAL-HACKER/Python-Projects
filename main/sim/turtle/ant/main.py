import math,turtle,random

turtle.bgcolor("black")
turtle.tracer(0)
helper_1 = turtle.Turtle(visible=False)
helper_2 = turtle.Turtle(visible=False)
#!!ants
"""
food      → (fx, fy)
pheromone → (px, py)
random    → (rx, ry)
wall      → (wx, wy)
home      → (hx, hy)
"""
#! example:
"""
dx = 3*fx + 1.5*px + 0.2*rx + 5*wx
dy = 3*fy + 1.5*py + 0.2*ry + 5*wy
"""
def stamp(t:turtle.Turtle,x_arr:list[int],y_arr:list[int],color:str):
    t.clear()
    t.color(color)
    for x,y in zip(x_arr,y_arr):
        t.penup()
        t.goto(x,y)
        t.dot(3)
    turtle.update()
    
def brownian_motion(i):
    x_arr[i] += random.randint(-1, 1)
    y_arr[i] += random.randint(-1, 1)

def angle_motion(i):
    rad = angles[i]
    x_arr[i] += math.cos(rad)
    y_arr[i] += math.sin(rad)
    
def make_grid(grid):
    
    for x,y in zip(x_arr,y_arr):

            cx = int(x // pheromone_cell_size)
            cy = int(y // pheromone_cell_size)

            if (cx, cy) not in grid:
                grid[(cx, cy)] = []

            grid[(cx, cy)].append((x,y)) 

def trail_grid(grid):
    #? Evaporate trails globally so old paths disappear
    for cell in list(grid.keys()):
        grid[cell] *= 0.99 
        if grid[cell] < 0.01:#! ie when 0.99^{x} < 0.01 where x is number of time trail_grid is called
            grid[cell] = 0
            
    for i,(x,y) in enumerate(zip(x_arr,y_arr)):

            cx = int(x // pheromone_cell_size)
            cy = int(y // pheromone_cell_size)

            pher = leave_trail(i)
            
            grid[(cx, cy)] = grid.get((cx, cy), 0) + pher


def leave_trail(i):
        # strength = max(0, 1 - time_arr[i]/MAX_TIME)
        # time_arr[i] += 1
        # return strength
        return 1

def pheromone_vector(i,grid,angle = False):
    k = 1 
    x,y = x_arr[i],y_arr[i]
    rx,ry = 0,0 #! candidate pop
    cx = int(x // pheromone_cell_size)
    cy = int(y // pheromone_cell_size)
    max_intensity = 0
    target_cell = None
    for dx_cell in (-1, 0, 1):
        for dy_cell in (-1, 0, 1):
            if dy_cell == dx_cell == 0:
                continue

            nearby = grid.get(
                        (cx + dx_cell, cy + dy_cell),
                        0
                    )
            if not nearby:
                continue
            if nearby > max_intensity:
                max_intensity = nearby
                target_cell = cx + dx_cell,cy + dy_cell
    if target_cell and angle:
        rx = target_cell[0] * pheromone_cell_size + (pheromone_cell_size / 2)
        ry = target_cell[1] * pheromone_cell_size + (pheromone_cell_size / 2)
        
        angle = math.atan2(ry - y, rx - x)
        angles[i] = angle
        # angle_motion(i)
        return
    if target_cell:
            # Calculate destination coordinate (center of target cell)
            rx = target_cell[0] * pheromone_cell_size + (pheromone_cell_size / 2)
            ry = target_cell[1] * pheromone_cell_size + (pheromone_cell_size / 2)
            
            dist = max(0.1,math.hypot(rx - x,ry - y))
            
            fx = (rx - x)/dist
            fy = (ry - y)/dist
            
            strength = 1 - math.exp(-max_intensity * k)
            
            x_arr[i] += fx * strength 
            y_arr[i] += fy * strength
            
def make_food_grid(grid):
    
    for x,y in zip(food_x,food_y):

            cx = int(x // food_cell_size)
            cy = int(y // food_cell_size)

            if (cx, cy) not in grid:
                grid[(cx, cy)] = []

            grid[(cx, cy)].append((x,y)) 

def consume_food(i,j):
    weight = 2
    x,y = x_arr[i],y_arr[i]
    fo_x,fo_y = food_x[j],food_y[j]
    if not return_nest[i]:
        dist = math.hypot(fo_x - x,fo_y - y)
        angle = math.atan2(fo_y - y, fo_x - x)
        decay = math.exp(-dist * 0.01)
        ux =  math.cos(angle) * decay * weight
        uy = math.sin(angle) * decay * weight

        x_arr[i] += ux
        y_arr[i] += uy

        if dist < 10:
            return_nest[i] = True
            food_hp[j] -= 1 #! change const later
            return
        
def move_to_nest(i,weight):
    x,y = x_arr[i],y_arr[i]
    
    dist = max(0.1,math.hypot(nx - x,ny - y))
    if dist < 20:
        return_nest[i] = False
        return
    if return_nest[i]:
            k = 2
            
            fx = (nx - x)/dist + random.uniform(-weight, weight)
            fy = (ny - y)/dist + random.uniform(-weight, weight)
            
            strength = k
            
            x_arr[i] += fx * strength 
            y_arr[i] += fy * strength
            
def border_check(i):
    x,y = x_arr[i],y_arr[i]
    w2,h2 = WIDTH//2,HEIGHT//2
# Reflect velocity without touching vx, vy directly.
#
# v = (cos θ, sin θ)
#
# Vertical wall:
#   (-cos θ, sin θ) = (cos(π-θ), sin(π-θ))
#   => θ = π - θ
#
# Horizontal wall:
#   (cos θ, -sin θ) = (cos(-θ), sin(-θ))
#   => θ = -θ
    if x > w2 or x < -w2:
        angles[i] = math.pi - angles[i]

    if y > h2 or y < -h2:
        angles[i] = -angles[i]
    x = max(-w2, min(w2, x))
    y = max(-h2, min(h2, y))
    x_arr[i],y_arr[i] = x,y 
"""
TODO:

?[ ] Remove time_arr (ants should always leave pheromone)
![ ] Add nest (nest_x, nest_y)
?[ ] Add has_food[] state for each ant
![ ] Create food_grid (same idea as pheromone_grid)
![ ] Food >> pheromone >> random weighting
?[ ] Use TWO pheromone grids:
        - home_pheromone (searching ants follow)
        - food_pheromone (returning ants leave)
?[ ] Replace Brownian motion with angle-based steering
        (front, front-left, front-right sensors)
*[ ] Later: walls/obstacles
*[ ] Later: optimize rendering (Pygame)
"""
num_ant = 1_000
num_food = 10
pheromone_cell_size = 10
food_cell_size = 10
MAX_TIME = 10
FOOD_HP = 100
WIDTH = 501
HEIGHT = 501
pheromone_grid = {}
food_grid = {}
x_arr = [random.randint(-WIDTH//2,WIDTH//2) for _ in range(num_ant)]
y_arr = [random.randint(-HEIGHT//2,HEIGHT//2) for _ in range(num_ant)]
angles = [random.uniform(0,math.tau) for _ in range(num_ant)]
return_nest = [False for _ in range(num_ant)]
return_food = [False for _ in range(num_ant)]
food_x = [random.randint(-WIDTH//2,WIDTH//2) for _ in range(num_food)]#! try to implement food and the attraction must be strong
food_y = [random.randint(-HEIGHT//2,HEIGHT//2) for _ in range(num_food)]
food_hp = [FOOD_HP for _ in range(num_food)]
nx,ny = 0,0
make_food_grid(food_grid)
stamp(helper_2,food_x,food_y,"green")
c=-1
while True:
    c+=1
    if c % 10 == 0:
        turtle.title(f"{c}")
            
    stamp(helper_2,food_x,food_y,"green")
    grid = {}
    make_grid(grid)
    trail_grid(pheromone_grid)
    stamp(helper_1,x_arr,y_arr,"red")
    for j in range(len(food_hp)-1, -1, -1):
        if food_hp[j] <= 0:
            del food_x[j]
            del food_y[j]
            del food_hp[j]
    for i in range(num_ant):

        for j in range(len(food_hp)):
            consume_food(i, j)

        pheromone_vector(i, pheromone_grid, angle=True)
        angle_motion(i)
        move_to_nest(i, 0.1)
        border_check(i)
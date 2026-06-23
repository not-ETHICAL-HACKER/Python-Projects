import math,turtle,random

turtle.bgcolor("black")
turtle.tracer(0)
helper = turtle.Turtle(visible=False)
helper.color("red")
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
def stamp(t:turtle.Turtle,x_arr:list[int],y_arr:list[int]):
    t.clear()
    for x,y in zip(x_arr,y_arr):
        t.penup()
        t.goto(x,y)
        t.dot(3)
    turtle.update()
    
def brownian_motion(i):
    x_arr[i] += random.randint(-1, 1)
    y_arr[i] += random.randint(-1, 1)

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
        grid[cell] *= 0.95 
        if grid[cell] < 0.01:#! ie when 0.95^{x} < 0.01 where x is number of time trail_grid is called
            grid[cell] = 0
            
    for i,(x,y) in enumerate(zip(x_arr,y_arr)):

            cx = int(x // pheromone_cell_size)
            cy = int(y // pheromone_cell_size)

            pher = leave_trail(i)
            
            grid[(cx, cy)] = grid.get((cx, cy), 0) + pher


def leave_trail(i):
        strength = max(0, 1 - time_arr[i]/MAX_TIME)
        time_arr[i] += 1
        return strength

def pheromone_vector(i,grid):
    k = 0.1 
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
    if target_cell:
            # Calculate destination coordinate (center of target cell)
            rx = target_cell[0] * pheromone_cell_size + (pheromone_cell_size / 2)
            ry = target_cell[1] * pheromone_cell_size + (pheromone_cell_size / 2)
            
            fx = rx - x
            fy = ry - y
            
            strength = 1 - math.exp(-max_intensity * k)
            
            x_arr[i] += fx * strength 
            y_arr[i] += fy * strength
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
MAX_TIME = 10
pheromone_grid = {}
x_arr = [random.randint(-500,500) for _ in range(num_ant)]
y_arr = [random.randint(-500,500) for _ in range(num_ant)]
time_arr = [0 for _ in range(num_ant)]
food_x = [0 for _ in range(num_food)]#! try to implement food and the attraction must be strong
food_y = [0 for _ in range(num_food)]

while True:
    grid = {}
    make_grid(grid)
    trail_grid(pheromone_grid)
    stamp(helper,x_arr,y_arr)
    for i in range(num_ant):
        pheromone_vector(i,pheromone_grid)
        brownian_motion(i)
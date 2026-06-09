"""
------------------------------------------------------------
CELLULAR AUTOMATA (CA) NOTES
------------------------------------------------------------

What it is:
- A simulation made of a grid of cells
- Each cell has a value (0/1 or number/state)
- Time evolves in discrete steps

Core idea:
    new_state = f(current_cell, neighbors)

------------------------------------------------------------
NEIGHBOR RULES
------------------------------------------------------------
Each cell usually looks at its 8 neighbors:

    . . .
    . X .
    . . .

So update depends on surrounding cells only.

------------------------------------------------------------
GAME OF LIFE EXAMPLE
------------------------------------------------------------
Rules:
- If alive:
    survives if 2 or 3 neighbors
- If dead:
    becomes alive if exactly 3 neighbors

This creates:
- gliders
- oscillators
- stable structures

------------------------------------------------------------
IMPLEMENTATION STRUCTURE
------------------------------------------------------------

grid[y][x] = current state

For each frame:
    create new_grid

    for each cell:
        count neighbors (8 surrounding cells)
        apply rule
        store result in new_grid

    replace grid = new_grid

------------------------------------------------------------
WHY IT WORKS
------------------------------------------------------------
- No particles or physics
- Just local rules
- Global patterns emerge from simple rules

------------------------------------------------------------
1 CELL = 10 PIXEL VERSION
------------------------------------------------------------
- Grid size = screen resolution
- Each cell = 10x10 pixel
- Value maps directly to color

Results:
- patterns
- growth
- waves
- textures

------------------------------------------------------------
KEY IDEA
------------------------------------------------------------
Cellular automata = grid + local rules + time steps
"""
#! only use balck and white for now, ie, 0 and 1, or dead and alive
#! black background, white cells
import pygame,random,math

pygame.init()
WIDTH = 1200
HEIGHT = 1000

cell_size = 4
chance = 0.25
alive_pos = set()  # store alive cell positions as (x, y) tuples
dead_pos = set()   # store dead cell positions as (x, y) tuples
screen = pygame.display.set_mode((WIDTH, HEIGHT))

for i in range(int((WIDTH//cell_size))):
    for j in range(int((HEIGHT//cell_size))):
            if random.random() < chance:  
                pygame.draw.rect(screen, (255,255,255),
                 (i*cell_size, j*cell_size,
                  cell_size, cell_size))
                alive_pos.add((i, j))  # store grid position
            else:
                pygame.draw.rect(screen, (0,0,0),
                 (i*cell_size, j*cell_size,
                  cell_size, cell_size))
                dead_pos.add((i, j))  # store grid position

running = True
CONWAY = True
VON = False
CROSS = False

# TODO: Recreate the diamond fractal automaton from the reference image.

#* Observations:
#? - Uses a Von Neumann neighborhood (N, S, E, W).
# - Starts from a single live cell.
# - Produces self-similar growth and nested holes.
#? - Population does not simply expand as a solid diamond.
# - Pattern appears related to parity (odd/even) rather than threshold rules like Conway's 2/3 neighbors.
# - Investigate modulo-2 / XOR-like behavior.
# - Compare generations at powers of two (2, 4, 8, 16, 32, ...).
# - Check whether the current cell's state affects the update, or if only neighboring states matter.
# - Candidate-cell approach may be useful since activity remains sparse.
#! - cells dont appear to die once alive, but rather only new cells are born, so maybe only check dead cells with 2 alive neighbors to become alive, and never kill alive cells, ie, no need to check alive cells at all, just check dead cells with 2 alive neighbors to become alive. This would be a very simple rule that could produce the observed pattern.

#* Goal:
# Starting from one cell, recover the rule that reproduces
# the fractal diamond seen in the reference image.


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_pos = set()
    
    for (x, y) in alive_pos:
        # Count alive neighbors
        neighbors = 0
        if CONWAY:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if (dx, dy) != (0, 0) and (x + dx, y + dy) in alive_pos:
                        neighbors += 1

            # Apply rules
            if neighbors in (2, 3): #change to make new behavior
                new_pos.add((x, y))  # stays alive or becomes alive
            else:
                dead_pos.add((x, y))  # becomes dead
        if VON:
            for dx in  (-1,0,1):
                for dy in  (-1,0,1):
                    if abs(dx) + abs(dy) == 1:
                        if (x + dx, y + dy) in alive_pos:
                            neighbors += 1
                    
            if neighbors in (2,): #change to make new behavior
                new_pos.add((x, y))  # stays alive or becomes alive
            else:
                dead_pos.add((x, y))  # becomes dead
        if CROSS:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if abs(dx)+abs(dy) == 1 and (x + dx, y + dy) in alive_pos:
                        neighbors += 1
            if neighbors in (2,3):
                new_pos.add((x,y))
            else:
                dead_pos.add((x,y))
    
    new_dead_pos = dead_pos.copy()

    for (x,y) in  new_dead_pos:
        neighbors = 0
        if CONWAY or VON:
            for dx in  (-1,0,1):
                for dy in  (-1,0,1):
                    if (dx, dy) != (0, 0) and (x + dx, y + dy) in alive_pos:
                        neighbors += 1
                
            if neighbors == 3:
                new_pos.add((x, y))  # becomes alive
                dead_pos.discard((x,y)) # remove discarf if it doesnt produce conways gaem of life
        if CROSS:
            for dx in  (-1,0,1):
                for dy in  (-1,0,1):
                    if abs(dx)+abs(dy) == 1 and (x + dx, y + dy) in alive_pos:
                        neighbors += 1
            if neighbors in(2,):
                new_pos.add((x,y)) # becomes alive
                dead_pos.discard((x,y))
            


    alive_pos = new_pos
    
    screen.fill((0, 0, 0))  # clear screen
    for (x, y) in alive_pos:
        pygame.draw.rect(screen, (255,255,255),
         (x*cell_size, y*cell_size,
          cell_size, cell_size))
    pygame.display.flip()
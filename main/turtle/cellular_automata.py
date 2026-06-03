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
- Grid size = screen resolution/10
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
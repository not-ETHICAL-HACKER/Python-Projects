import numpy as np
import time
from colorama import Style, Back, Fore, init 
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.path import Path 
from matplotlib.patches import PathPatch # We'll use this to create a clean initial fill object

# --- Setup ---
init(autoreset=True)
num = 2**10
a = np.array([round(float(x), 3) for x in np.linspace(0, 1, num)])
np.random.shuffle(a)
a_list = list(a) 
# Max frames is number of passes (N-1) + initial state + final state
max_frames = len(a_list) + 1 

# --- Bubble Sort Generator (Same as before) ---
def bubble_sort_generator(List: list):
    """
    Implements the bubble sort algorithm and yields the list state *only* after an outer pass.
    """
    n = len(List)
    
    # Initial yield of the unsorted list (Frame 0)
    yield List.copy()

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if List[j] > List[j + 1]:
                List[j], List[j + 1] = List[j + 1], List[j]
                swapped = True
        
        yield List.copy()

        if not swapped:
            break

# --- Matplotlib Setup and Animation ---
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_ylim(0, 1)
ax.set_title(f"Bubble Sort Animation ({num} elements)")
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_ylabel("Value")

x = np.arange(num)
y_initial = np.array(a_list)

# Initial Path setup for the fill area
# Vertices: [data points] + [closing points at y=0]
verts_initial = np.concatenate([
    np.array([x, y_initial]).T,
    np.array([[x[-1], 0], [x[0], 0]])
])

# Codes: MOVETO (1) for the first data point, then LINETO (2) for the rest, 
# and finally CLOSEPOLY (79)
codes_initial = np.concatenate([
    [Path.MOVETO],                  # Start at the first data point
    [Path.LINETO] * (num - 1),      # Line to all subsequent data points
    [Path.LINETO, Path.CLOSEPOLY]   # Close the path along y=0
])

initial_path = Path(verts_initial, codes_initial)

# Add the fill area as a PathPatch for clean blitting
fill = PathPatch(
    initial_path, 
    facecolor='skyblue', 
    alpha=0.7, 
    edgecolor='blue', # Add edge color for better definition
    lw=1.5
)
ax.add_patch(fill)

# Plot the line (we'll update this)
line, = ax.plot(x, y_initial, color='black', lw=1.5)


frames_generator = bubble_sort_generator(a_list)

def update_plot(frame_data):
    """
    Update function for the animation. Called once per yield from the generator.
    """
    y_data = np.array(frame_data)
    
    # 1. Update the line plot's y-data
    line.set_ydata(y_data)
    
    # 2. Update the fill area's vertices
    # Recalculate vertices for the closed path
    verts = np.concatenate([
        np.array([x, y_data]).T,
        np.array([[x[-1], 0], [x[0], 0]])
    ])
    
    # The codes array remains constant, only the verts change
    codes = np.concatenate([
        [Path.MOVETO],                  # START
        [Path.LINETO] * (num - 1),
        [Path.LINETO, Path.CLOSEPOLY]   # END
    ])
    
    # Create the new Path object
    new_path = Path(verts, codes)
    
    # Update the existing PathPatch
    fill.set_path(new_path)
    
    # Return the updated artists for blitting
    return line, fill

# Create the animation object
ani = animation.FuncAnimation(
    fig, 
    update_plot, 
    frames=frames_generator, 
    interval=10, 
    repeat=False, 
    blit=True,
    save_count=max_frames 
)

plt.show()
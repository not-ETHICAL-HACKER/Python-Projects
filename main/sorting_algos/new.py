import numpy as np
import time
import sys
from typing import Generator
from colorama import Fore,Style,init,Back
init(autoreset=True)
a = [round(float(x), 2) for x in np.linspace(0, 1, 30)]
np.random.shuffle(a)

def bubble_sort_with_indices(arr: list[float]) -> Generator[tuple[list[float], int, int, int], None, None]:
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                # We yield: current state, swap indices, and how many are sorted at the end (i)
                yield arr[:], j, j+1, i
        if not swapped:
            # If we exit early, everything is sorted
            yield arr[:], -1, -1, n
            break

# ANSI Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

for state, idx1, idx2, sorted_count in bubble_sort_with_indices(a):
    output:list[str] = []
    # n - sorted_count is the boundary where numbers are permanently sorted
    boundary = len(state) - sorted_count
    
    for i, val in enumerate(state):
        str_val = f"{val:.2f}" 
        
        if i >= boundary:
            # Numbers that have reached their final position
            output.append(f"{Fore.GREEN+Style.BRIGHT+Back.BLACK}{str_val}{Style.RESET_ALL}")
        elif i == idx2:
            # The two numbers currently being swapped
            output.append(f"{Fore.RED+Style.BRIGHT+Back.BLACK}[{str_val}]{Style.RESET_ALL}")
        else:
            output.append(str_val)
    sys.stdout.write("\r" + f"{Back.BLACK}, ".join(output) + "      ")
    sys.stdout.flush()
    time.sleep(0.1)

print("\n\nSorting Complete!")
import numpy as np
import time
from colorama import Style, Back, Fore, init
import os
import matplotlib.pyplot as plt
init(autoreset=True)
num=10**3
a = [round(float(x), 3) for x in np.linspace(0, 1, num)]
np.random.shuffle(a)
sorted_l = sorted(a)
c_1 = Fore.GREEN+Back.BLACK+Style.BRIGHT
c_2 = Fore.RED+Back.BLACK+Style.BRIGHT


def bubble_sort(List: list):
    """
    The function `bubble_sort` implements the bubble sort algorithm in Python and displays the sorting
    process step by step.

    :param List: The code you provided is a basic implementation of the bubble sort algorithm in Python.
    It sorts a given list in ascending order
    :type List: list
    :return: The function `bubble_sort` is returning the sorted list after performing the bubble sort
    algorithm on the input list.
    """
    c = 1
    for i in range(len(List)):
        if sorted_l == List:
            break
        #? remove comments to see the sorting process in terminal
        #os.system('cls' if os.name == 'nt' else 'clear')
        #print("The Green tells us the number of times the buble moves and the red is the list.")
        #print(f"{c_1}{c:4d}{c_2}=>{List}")
        for j in range(len(List)-1-i):
            #time.sleep(0.01)
            c += 1
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
                #yield List #! put yield here to show every swap 
        #! put yield here to show every pass
        yield List
    #print()



plt.ion()
fig, ax = plt.subplots()

# Set background colors to black
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

# Initial bar plot with white fill and black edges
bars = ax.bar(range(len(a)), a, color="white", edgecolor="white")

ax.set_ylim(0, 1)

# Make title and ticks white for visibility
ax.set_title("Bubble Sort Animation (Bars)", color="white")
ax.tick_params(colors="white")

# Remove y-axis numbers
ax.set_yticklabels([])      # hide labels
ax.set_yticks([])           # hide tick marks

# Animation loop
for frame in bubble_sort(a):
    # Update bar heights
    for bar, height in zip(bars, frame):
        bar.set_height(height)

    plt.draw()
    plt.pause(1/num)

plt.ioff()
plt.show()
#! add a way to count iterations and show it in the plot title and the number of swaps too
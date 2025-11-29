import math
from colorama import init, Fore, Style, Back
import time
import sys
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import shutil
from colorama import Fore, Style, init, Back
init(autoreset=True)
green = Fore.GREEN+Style.BRIGHT+Back.BLACK

init(autoreset=True)

# fonts for hello before/after wall
hello1 = "hello"
hello2 = "world"   # italic unicode font


def movin_wall():
    c, r = shutil.get_terminal_size()
    i = c - 1           # wall starts on the right
    hello_x = 10        # position of "hello"

    print()             # reserve 1 line
    os.system("cls")
    while True:
        # move cursor up
        print("\x1b[1F", end="")

        # determine which hello to display
        if i <= hello_x:     # wall passed hello
            text = Fore.GREEN+hello2
        else:
            text = hello1

        # assemble the full line
        line = [" "] * c
        # draw hello
        for idx, ch in enumerate(text):
            if hello_x + idx < c:
                line[hello_x + idx] = ch

        # draw wall (a '|')
        if 0 <= i < c:
            line[i] = "|"

        print(Back.BLACK+Fore.BLUE+Style.BRIGHT+"".join(line))

        i -= 1
        if i < -1:   # wall fully gone → reset
            i = c - 1

        time.sleep(0.03)


def sin_wave(inv=False):
    """
    The function `sin_wave` generates a sine wave plot with optional inversion of axes.

    :param inv: The `sin_wave` function generates a sine wave plot. When `inv` is set to `False`
    (default), it plots the sine wave with x values increasing linearly and y values being the sine of
    x/100. When `inv` is set to `True`, it plots the, defaults to False (optional)
    """
    x = []
    y = []
    t=np.linspace(0,10,2000)
    a = np.sin(3 * t)
    b = np.sin(4 * t + np.pi/2)
    for i in range(0, 629):
        y.append(math.sin(i/100))
        x.append(i/100)
    plt.plot(a,b)
    plt.plot(b,a)
    plt.plot(x, y) if not inv else plt.plot(y, x)
    plt.title("Example Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


sin_wave()

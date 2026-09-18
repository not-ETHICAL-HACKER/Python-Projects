import math
import numpy as np
import matplotlib.pyplot as plt
import shutil
from colorama import Fore, Back, Style, init
import os
import re
os.system("cls" if os.name=="nt" else "clear")
init(autoreset=True)
def clean_equation(eq: str):
    eq = eq.replace(" ", "")                     # remove spaces
    eq = re.sub(r"(\d)(x)", r"\1*x", eq)         # 3x → 3*x
    eq = eq.replace("^", "**")                   # ^ → **
    return eq
norm = Fore.WHITE+Back.BLACK
b_red = Fore.RED+Style.BRIGHT+Back.BLACK
b_gre = Fore.GREEN+Style.BRIGHT+Back.BLACK
b_blu = Fore.BLUE+Style.BRIGHT+Back.BLACK
b_mag = Fore.MAGENTA+Style.BRIGHT+Back.BLACK
cols, rows = shutil.get_terminal_size()
print("\033[?25l", end="")
print(b_gre+f"This is the information grapher.".center(cols, " "))
print(b_red+f"=".center(cols, "="))
while True:
    try:
        x_val = float(input(b_mag+"Enter the value for x :"))
        break
    except ValueError:
        print("invalid_marker")
while True:
    equ = input(b_blu+"Enter an equation :")
    if equ.count("=") == 1:
        print(norm+"The input is acceptable.")
        break
    else:
        print("\033[?25h", end="")
        print(f"The input can only have one '=' \n{equ} is invalid")
# split equation
left, right = equ.split("=")
# NEGATE right side
combined = f"{left} - ({right})"
# clean whole thing
clean = clean_equation(combined)
# substitute x
clean_eval = re.sub(r"x", f"({x_val})", clean)
value = eval(clean_eval)
print("Combined (python):", clean)
print("Evaluated result:", value)
# Generate x points to graph
x_points = np.linspace(-10, 10, 1000)

# Build Python expression version
clean_no_x = clean_equation(f"{left} - ({right})")

# Evaluate for every x
y_points = []
for xv in x_points:
    expr = re.sub(r"x", f"({xv})", clean_no_x)
    y_points.append(eval(expr))

plt.plot(x_points, y_points)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

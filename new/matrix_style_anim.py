import math
from colorama import Back, Fore, Style, init
import time
import os
import random
import sys

init(autoreset=True)


def matrix(txt: str = "Hello World!!!", cd: float = 1e-6) -> int:
    alpha = "".join(chr(i) for i in range(32, 128))
    alpha = "".join(random.sample(alpha, len(alpha)))
    c = 0
    counter = 0
    out = ""
    while True:
        for ch in alpha:
            counter += 1
            time.sleep(cd)
            sys.stdout.write(f"\r{out}{ch}")
            sys.stdout.flush()
            if ch == txt[c]:
                alpha = "".join(random.sample(alpha, len(alpha)))
                out += ch
                c += 1
                break
        if c == len(txt):
            print()
            return counter
#!matrix("Hello World")


def wheel():
    frames = ["█", "▓", "▒", "░"]
    while 6 < 7:
        for f in frames:
            for _ in range(len(frames)):
                print("\r" + Fore.GREEN + Style.BRIGHT +
                      Back.BLACK + f, flush=True, end="")
            print()


def spinning_square(size=10, delay=0.1):
    frames = ["|", "╱", "-", "╲", "|", "/", "-", "\\"]
    while True:
        for ch in frames:
            # move back to top-left of the block
            sys.stdout.write("\033[F" * (size))  # cursor up N lines
            for _ in range(size):
                row = (ch * size)
                print(Fore.GREEN + Style.BRIGHT + Back.BLACK + row)
            time.sleep(delay)


def cube():
    A = 0
    points = [[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
              [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]

    while True:
        print("\033[H")
        proj = []
        for x, y, z in points:
            X = x*math.cos(A) - z*math.sin(A)
            Z = x*math.sin(A) + z*math.cos(A)
            Y = y
            f = 20 / (Z+5)
            proj.append((int(X*f+40), int(Y*f+12)))

        canvas = [[" "]*80 for _ in range(25)]
        for a, b in edges:
            x1, y1 = proj[a]
            x2, y2 = proj[b]
            try:
                canvas[y1][x1] = "#"
                canvas[y2][x2] = "#"
            except:
                pass

        print("\n".join("".join(r) for r in canvas))
        A += 0.05
        time.sleep(0.05)


def flag(text="@@@@@@@@@@@@@@@@@@@@"):
    w = len(text)
    t = 0
    while True:
        print("\033[H")
        for y in range(15):
            offset = int(3*math.sin(y/2+t))
            print(" "*offset+text)
        t += 0.3
        time.sleep(0.05)


def fire(w=80, h=40):
    import numpy as np
    buf = np.zeros((h, w))
    chars = " .:-=+*#%@"
    while True:
        buf[-1] = np.random.randint(0, 2, w)*9
        for y in range(h-1):
            for x in range(1, w-1):
                buf[y][x] = (
                    buf[y+1][x-1]+buf[y+1][x]+buf[y+1][x+1]
                )/3.03
        print("\033[H")
        for y in range(h):
            line = "".join(chars[int(buf[y][x])] for x in range(w))
            print(Fore.RED+line)
        time.sleep(0.03)


def static_noise(w=80, h=30):
    while True:
        print("\033[H")
        for _ in range(h):
            line = "".join(random.choice(["█", " "]) for _ in range(w))
            print(line)
        time.sleep(0.03)


def explosion(size=40, particles=50):
    parts = []
    for _ in range(particles):
        angle = random.random()*math.tau
        speed = random.random()*0.5+0.2
        parts.append([0, 0,
                      math.cos(angle)*speed,
                      math.sin(angle)*speed])

    while True:
        print("\033[H")
        canvas = [[" "]*80 for _ in range(30)]
        for p in parts:
            p[0] += p[2]
            p[1] += p[3]
            x = int(p[0]+40)
            y = int(p[1]+15)
            if 0 < x < 79 and 0 < y < 29:
                canvas[y][x] = "*"
        print("\n".join("".join(r) for r in canvas))
        time.sleep(0.03)


def ripple():
    t = 0
    while True:
        print("\033[H")
        for y in range(25):
            row = ""
            for x in range(80):
                d = ((x-40)**2 + (y-12)**2)**0.5
                v = math.sin(d/2 - t)
                row += "~" if v > 0 else " "
            print(row)
        t += 0.3
        time.sleep(0.03)


def earthquake(txt="THE EARTH IS SHAKING!"):
    while True:
        offset = random.randint(-3, 3)
        print("\r" + " "*abs(offset) + txt, end="")
        time.sleep(0.03)


def ufo():
    ship="   ___\n _/___\\_\n(_______)"
    while True:
        print("\033[H")
        print(ship)
        for _ in range(10):
            print("   " + random.choice(["|","!","/","\\" ]))
        time.sleep(0.1)

ufo()


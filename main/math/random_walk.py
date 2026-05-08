import math
import time
import random
import turtle
from itertools import product
t = turtle.Turtle()
t.hideturtle()

vectors : list[tuple[float,float]] = []
angles : list[float] = []

def walk(steps: int) -> float:
    x = y = 0
    #!path=[]
    dir = list("UDRL")
    t = time.time()
    for i in range(steps):
        random.shuffle(dir)
        a = [dir[0]]
        #!path+=a
        if a == ['U']:
            y += 1
        elif a == ['D']:
            y -= 1
        elif a == ['R']:
            x += 1
        elif a == ['L']:
            x -= 1
    sun = (x**2+y**2)**0.5
    print(f"(x : {x}, y : {y})\nTime taken: {time.time()-t:e} seconds")
    #!print(path[:100])
    print(f"Distance from origin: {sun}")
    return sun


def wander(pos: tuple[int, int, int], time_t: int, target: tuple[int, int, int] | bool = False) -> tuple[int, int, int]:
    x, y, z = pos

    steps: list[tuple[int, ...]] = list(product([-1, 0, 1], repeat=3))
    if not target:
        t = time.time()
        for _ in range(time_t):
            r_c: tuple[int, int, int] = random.choice(steps)
            dx, dy, dz = r_c
            x += dx
            y += dy
            z += dz
        print(
            f"(x : {x}, y : {y}, z : {z})\nTime taken: {time.time()-t:e} seconds")
        print(f"Distance from origin: {(x**2+y**2+z**2)**0.5:,.2f}")
        return (x, y, z)
    else:
        e_t = 0
        while (x, y, z) != target:
            e_t += 1
            r_c: tuple[int, int, int] = random.choice(steps)
            dx, dy, dz = r_c
            x += dx
            y += dy
            z += dz
        print(f"Reached target: {target} in {e_t} steps")


def turt_walk(steps: int, scale: float = 4,vectors:list[tuple[float, float]] = None,angles:list[float] = None) -> None:
    permu: list[tuple[int, ...]] = list(product([-1, 0, 1], repeat=2))
    x = y = 0
    log_num = 0
    t.speed(0)
    t.hideturtle()
    turtle.bgcolor("black")
    colors = ["red", "blue", "green", "yellow", "cyan",
              "magenta", "orange", "purple", "pink"]
    for i in range(steps):
        if math.log10(i+1) >= log_num:
            log_num += 1
            t.color(colors[log_num%len(colors)])

        r_c: tuple[int, int] = random.choice(permu)
        dx, dy = r_c
        if dx == 0 and dy == 0:
            continue
        x += dx
        y += dy
        sx, sy = x*scale, y*scale  # simulated coordinates
        t.goto(sx, sy)
    vectors.append((x, y))
    angles.append(t.heading())
    t.color("white")
    t.goto(0, 0)

def cross_product(vectors:list[tuple[float, float]], angles:list[float]) -> list[tuple[ float, float]]:
    for i in range(len(vectors)-1):
        x = vectors[i][0]*vectors[i+1][0]*math.sin(angles[i])
        y = vectors[i][1]*vectors[i+1][1]*math.sin(angles[i])
for _ in range(10):
    turt_walk(10**2,10,vectors,angles)
    time.sleep(1)
    
turtle.done()
# walk(10**6)
# wander((0, 0, 0), 10**6)

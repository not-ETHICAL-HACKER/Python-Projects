import time
import random
import turtle
from itertools import product
t=turtle.Turtle()

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

def turt_walk(steps:int):
    permu: list[tuple[int, ...]] = list(product([-1, 0, 1], repeat=2))
    x=y=0
    t.speed(0)
    for i in range(steps):
            r_c: tuple[int, int] = random.choice(permu)
            dx, dy = r_c
            x += dx
            y += dy
            sx,sy = x*10,y*10 # simulated coordinates
            t.goto(sx,sy)
    time.sleep(10)
turt_walk(10**6)
# walk(10**6)
# wander((0, 0, 0), 10**6)

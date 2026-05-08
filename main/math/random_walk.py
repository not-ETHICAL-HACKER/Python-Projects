import math
import time
import random
import turtle
from itertools import product
t = turtle.Turtle()
t.hideturtle()

vectors: list[tuple[float, float]] = []


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
def wanderin_target(prev: tuple[int, int], target: tuple[int, int], pos: tuple[int, int], scale: float = 4) -> None:
    x, y = pos
    t.color("white")
    t.penup()
    t.goto(prev[0]*scale, prev[1]*scale)
    t.pendown()
    t.dot(10, "black")
    t.penup()
    t.goto(target[0]*scale, target[1]*scale)
    t.pendown()
    t.dot(10, "yellow")
    t.penup()
    t.goto(x*scale, y*scale)
    t.pendown()
def wander_2d_target(pos: tuple[int, int], target: tuple[int, int], scale: float = 4) -> tuple[float, int]:
    x, y = pos
    steps: list[tuple[int, ...]] = list(product([-2,-1, 0, 1,2], repeat=2))
    tim = time.time()
    i = 0 
    turtle.bgcolor("black")
    tx,ty = target
    prev = (0, 0)
    wanderin_target(prev,target, (x, y), scale)
    while math.hypot(tx - x, ty - y) > 10:
        turtle.title(f"Distance to target: {math.hypot(tx - x, ty - y):.2f}")
        if random.random() < 0.35:
            prev = target
            dtx = (x < tx) - (x > tx) #! ts bcs ints also wrk as bools
            dty = (y < ty) - (y > ty) 
            tx += dtx
            ty += dty
            target = tx, ty
            wanderin_target(prev,target, (x, y), scale)
        i += 1
        r_c: tuple[int, int] = random.choice(steps)
        dx, dy = r_c
        dx += random.random()*(1 if tx > x else -1)
        dy += random.random()*(1 if ty > y else -1)
        x += dx
        y += dy
        sx, sy = x*scale, y*scale  # simulated coordinates
        t.goto(sx, sy)
    print(f"reached target {target} in {i} steps\nTime taken: {time.time()-tim:e} seconds")
    return (time.time()-tim, i)

def wander(pos: tuple[int, int, int], time_t: int, target: tuple[int, int, int] | bool = False) -> tuple[int, int, int]:
    x, y, z = pos

    steps: list[tuple[int, ...]] = list(product([-1, 0, 1], repeat=3))
    if not target:
        tim = time.time()
        for _ in range(time_t):
            r_c: tuple[int, int, int] = random.choice(steps)
            dx, dy, dz = r_c
            x += dx
            y += dy
            z += dz
        print(
            f"(x : {x}, y : {y}, z : {z})\nTime taken: {time.time()-tim:e} seconds")
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


def turt_walk(steps: int, scale: float = 4, vectors: list[tuple[float, float]] = None) -> None:
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
            t.color(colors[log_num % len(colors)])

        r_c: tuple[int, int] = random.choice(permu)
        dx, dy = r_c
        if dx == 0 and dy == 0:
            continue
        x += dx
        y += dy
        sx, sy = x*scale, y*scale  # simulated coordinates
        t.goto(sx, sy)
    vectors.append((sx, sy))
    t.color("white")
    t.goto(0, 0)

# walk() simulates a basic random walk / Brownian-motion-like process.
# eventual_dist_dir(vectors) computes the summed/average drift of many walks.
# For an unbiased walk, the average final displacement trends toward (0,0)
# as the number of simulations increases due to statistical cancellation.
# The endpoint spread from repeated turt_walk() simulations should form an
# approximately Gaussian distribution centered near the origin.
# Average squared displacement grows roughly linearly with number of steps.
# Future idea:
# add a function to visualize the average of many random-walk endpoints
# and the overall endpoint distribution / diffusion cloud.
def eventual_dist_dir(vectors: list[tuple[float, float]]) -> tuple[float, float]:
    x = sum([v1 for v1, _ in vectors])
    y = sum([v2 for _, v2 in vectors])
    return (x, y)

def main():
    for _ in range(10):
        turt_walk(10**2, 10, vectors)
        time.sleep(1)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color("red")
    t.goto(eventual_dist_dir(vectors))
    turtle.done()
# walk(10**6)
# wander((0, 0, 0), 10**6)
print(wander_2d_target((-100, -100), (100, 100),1))
turtle.done()
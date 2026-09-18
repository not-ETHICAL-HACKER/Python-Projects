import math
import time
import random
import turtle
from itertools import product
t = turtle.Turtle()
t.hideturtle()

vectors: list[tuple[float, float]] = []
res_vectors:list[tuple[float, float]] = []


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
def wander_2d_target(pos: tuple[int, int], target: tuple[int, int], scale: float = 4, reverse_bias: float = 0.00) -> tuple[float, int]:
    x, y = pos
    steps: list[tuple[int, ...]] = list(product([-1,0, 1], repeat=2))
    steps.remove((0, 0))
    tim = time.time()
    i = 0 
    dist = 1
    turtle.bgcolor("black")
    tx,ty = target
    prev = (0, 0)
    straight_line = math.hypot(tx - pos[0], ty - pos[1])
    wanderin_target(prev,target, (x, y), scale)
    while math.hypot(tx - x, ty - y) > 10:
        displacement = math.hypot(tx - x, ty - y)
        turtle.title(f"Efficiency: {straight_line / dist * 100:.2f}%Displacement: {displacement:.2f},distance traveled: {dist:2e}, steps: {i}")
        if random.random() < 0.00:
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
        dx += random.random()*(1 if tx > x else -1)*(-1 if random.random() < reverse_bias else 1)
        dy += random.random()*(1 if ty > y else -1)*(-1 if random.random() < reverse_bias else 1)
        x += dx
        y += dy
        sx, sy = x*scale, y*scale  # simulated coordinates
        dist += math.hypot(dx, dy)
        t.goto(sx, sy)
    print(f"reached target {target} in {i} steps\nTime taken: {time.time()-tim:e} seconds")
    return (time.time()-tim, i,dist)

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
        x += dx + random.random()* (1 if random.random() < 0.5 else -1) 
        y += dy + random.random()* (1 if random.random() < 0.5 else -1) 
        sx, sy = x*scale, y*scale  # simulated coordinates
        t.goto(sx, sy)
    vectors.append((sx, sy))
    t.color("white")
    t.goto(0, 0)

def eventual_dist_dir(vectors: list[tuple[float, float]]) -> tuple[float, float]:
    x = sum([v1 for v1, _ in vectors])
    y = sum([v2 for _, v2 in vectors])
    res_vectors.append((x,y))
    return (x, y)

def res_vector(vectors: list[tuple[float, float]]) -> tuple[float, float]:
    x = sum([v1 for v1, _ in vectors])
    y = sum([v2 for _, v2 in vectors])
    return (x, y)
def gauss_vector_distri(res_vectors: list[tuple[float, float]], scale: float) -> tuple[float, float]:
    data_set = res_vectors
    (x_sigma, y_sigma), (x_mean, y_mean) = sigma_mean(data_set)
    for v in res_vectors:
        x,y=v
        normalized_dist = math.hypot((x - x_mean) / x_sigma, (y - y_mean) / y_sigma)
        if normalized_dist > 3:
            color = "red"    # Beyond 3-sigma
        elif normalized_dist > 2:
            color = "yellow" # 2 to 3 sigma
        elif normalized_dist > 1:
            color = "green"  # 1 to 2 sigma
        else:
            color = "white"  # Inner core (0 to 1 sigma)
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.dot(5, color)
def sigma_mean(data_set:list[tuple[float,float]])->tuple[tuple[float,float],tuple[float,float]]:
    n = len(data_set)
    x_mean = sum([x for x,_ in data_set])/n
    y_mean = sum([y for _,y in data_set])/n
    x_temp = 0
    y_temp = 0
    for x,y in data_set:
        x_temp += (x - x_mean)**2
        y_temp += (y - y_mean)**2
    x_sigma = (x_temp/n)**0.5
    y_sigma = (y_temp/n)**0.5
    return (x_sigma,y_sigma),(x_mean,y_mean)
paths = 10**2
scale = 2
iters = 10**3
turtle.tracer(0, 0)


def main():
    for i in range(iters):
        if not i % 2:
            t.clear()
        vectors.clear()
        turtle.title(f"Path {(i+1)/iters*100:,} %")
        for _ in range(2):
            turt_walk(paths, scale, vectors)
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.color("red")
        t.goto(eventual_dist_dir(vectors))
        t.penup()
        t.color("magenta")
        t.pendown()
    turtle.update()
    time.sleep(.5)
    t.clear()
    gauss_vector_distri(res_vectors,scale)
    turtle.update()
# walk(10**6)
# wander((0, 0, 0), 10**6)
# for _ in range(10):
#     t.penup()
#     t.goto(0, 0)
#     t.pendown()
#     print(wander_2d_target((-100, -100), (100, 100),1))
main()
import csv

with open("random_walk_mean_sigma.csv", "a", newline="") as f:
    data = sigma_mean(res_vectors)
    writer = csv.writer(f)
    x_sigma, y_sigma = data[0]
    x_mean, y_mean = data[1]
    writer.writerow([iters,paths,x_sigma, y_sigma, x_mean, y_mean])
with open("random_walk_data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for v in res_vectors:
        writer.writerow([v[0], v[1]])
turtle.done()
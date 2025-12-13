import time
import random


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


walk(10**6)

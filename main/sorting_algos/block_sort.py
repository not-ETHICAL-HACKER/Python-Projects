import time
from typing import Generator
import numpy as np
import matplotlib.pyplot as plt

num = 10**3
np.random.seed(0)
a = [round(float(x), 9) for x in np.linspace(-10, 10, num)]
# a = [x for x in np.random.random(num)] + [-x for x in np.random.random(num)]
np.random.shuffle(a)
tim = 0.0


def block_sort(arr: list[float], block_size: int) -> Generator[tuple[list[float], int, int, float], None, None]:
    c = 0
    s = sorted(arr)
    for _ in range(0, len(arr)+1, block_size*2):
        for i in range(len(arr)):
            tit = time.time()
            blo = block_size+_
            if arr == s:
                return
            if i % 2 == 0:
                var = not False
                sign=1/np.log(blo)
            else:
                var = not True
                sign=np.log(blo)
            temp = arr[i:i+blo]
            old = temp[:]
            temp.sort(reverse=var)
            if temp == old:
                c += 1
                continue
            arr[i:i+blo] = [x*sign for x in temp]
            c += 1
            tit = time.time() - tit
            if c % 1 == 0:
                yield arr, c, blo, tit


plt.ion()
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

x = np.arange(len(a))
vlines = ax.vlines(x, 0, a, linewidth=1, edgecolor="white")

ax.set_ylim(-10**2, 10**2)
ax.tick_params(colors="white")

d = 0
t = time.time()
block = len(a)//10
for frame, i, blo, ti in block_sort(a, block):

    colors = ["white"] * len(frame)

    colors[i % len(frame)] = "red"
    colors[(i + blo) % len(frame)] = "red"

    vlines.set_color(colors)

    tim += ti

    ax.set_title(
        f"67 Block Sort | Iterations : {i:,} | Time Elapsed: {time.time()-t:.2f}s| Actual Algorithm Time : {tim:+e}s",
        color="white"
    )
# Only update the plot every 10 iterations to speed up the simulation
    if d % 10 == 0:
        vlines.set_segments([((j, 0), (j, h)) for j, h in enumerate(frame)])
        plt.pause(1e-6)
    d += 1
    
vlines.set_segments([((j, 0), (j, h)) for j, h in enumerate(frame)])
plt.pause(1e-6)


# ---- FINAL PASS: array is sorted → turn everything green ----
vlines.set_color(["lime"] * len(a))
t = time.time()-t
ax.set_title(
    f"67 Block Sort | Sorted ✔ | Time Elapsed in simulation: {t:.2f}s | Actual Algorithm Time : {tim:e}s | Dialtion of about {t / (tim):,.0f}x",
    color="lime"
)

plt.ioff()
plt.show()
print(tim)

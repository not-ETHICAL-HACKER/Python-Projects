import time
from typing import Generator
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors

timothy=time.time()
num = 10**3
np.random.seed(67)
a = [float(x) for x in np.linspace(-0, 1, num)]
np.random.shuffle(a)
tim = 0.0


def block_sort(arr: list[float], block_size: int) -> Generator[tuple[list[float], int, int, float], None, None]:
    c = 0
    s = sorted(arr)
    for _ in range(0, len(arr)+1): # block_size*2):
        for i in range(len(arr)):
            tit = time.time()
            blo = block_size+_
            if arr == s:
                return
            # if i % 2 == 0:
            #     var = False
            # else:
            #     var = True
            temp = arr[i:i+blo]
            old = temp[:]
            temp.sort()#reverse=var)
            if temp == old:
                c += 1
                continue
            arr[i:i+block_size+_] = temp
            c += 1
            tit = time.time() - tit
            # if c % 1 == 0:
            yield arr, c, blo, tit


plt.ion()
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

x = np.arange(len(a))
colors = ["white"] * len(a)
vlines = ax.vlines(x, 0, a, colors="white", linewidth=1)

ax.set_ylim(-0, 1)
ax.tick_params(colors="white")

d = 0
t = time.time()
block = len(a)//10
norm = mcolors.Normalize(vmin=0, vmax=1)
# norm = mcolors.TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1)
# cmap = cm.seismic  # or coolwarm
cmap = cm.viridis  # try plasma, inferno, turbo, etc.

for frame, i, blo, ti in block_sort(a, block):
    tim += ti
    ax.set_title(f" Block Sort | Iterations : {i:,} | Time Elapsed: {time.time()-t:.2f}s| Actual Algorithm Time : {tim:+e}s",color="white")

    colors = cmap(norm(frame))

    if round(timothy,0) % 2 == 0:
        segments = [((i, 0), (i, h)) for i, h in enumerate(frame)]
        vlines.set_segments(segments)
        vlines.set_color(cmap(norm(frame)))

    plt.pause(1e-3)
    d += 1
vlines.set_segments(
        [((i, 0), (i, h)) for i, h in enumerate(frame)]
    )
ax.set_title(
    f" Block Sort | Sorted ✔ | Time Elapsed in simulation: {t:.2f}s | Actual Algorithm Time : {tim:e}s | Dialtion of about {t / (tim):,.0f}x",
    color="lime"
)
plt.ioff()
plt.show()
print(tim)

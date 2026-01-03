from typing import Generator
import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.cm as cm
import matplotlib.colors as mcolors

t=time.time()
num = 10**3
np.random.seed(67)
a = [float(x) for x in np.linspace(-0, 1, num)]
np.random.shuffle(a)


def block_sort(arr: list[float], block_size: int) -> Generator[tuple[list[float], int], None, None]:
    c = 0
    for _ in range(0, block_size*10+1, block_size*2):
        for i in range(0, len(arr)):
            if i % 1 == 0:
                var = False
            else:
                var = True
            temp = arr[i:i+block_size+_]
            old = temp[:]
            temp.sort(reverse=var)
            if temp == old:
                c += 1
                continue
            arr[i:i+block_size+_] = temp
            c += 1
            yield arr, c


plt.ion()
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

x = np.arange(len(a))
colors = ["white"] * len(a)
vlines = ax.vlines(x, 0, a, colors="white", linewidth=.5)

ax.set_ylim(-0, 1)
ax.tick_params(colors="white")
ax.set_title("67 Block Sort (VLines Only)", color="white")

d = 0
norm = mcolors.Normalize(vmin=0, vmax=1)
cmap = cm.viridis  # try plasma, inferno, turbo, etc.

for frame, idx in block_sort(a, len(a)//10):

    colors = cmap(norm(frame))

    # color the sorted element blue
    if idx % 2 == 0:
        segments = [((i, 0), (i, h)) for i, h in enumerate(frame)]
        vlines.set_segments(segments)
        vlines.set_color(cmap(norm(frame)))

    plt.pause(1e-3)
    d += 1
vlines.set_segments(
        [((i, 0), (i, h)) for i, h in enumerate(frame)]
    )
plt.ioff()
plt.show()

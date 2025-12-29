from typing import Generator
import numpy as np
import matplotlib.pyplot as plt

num = 10**1*2
np.random.seed(67)
a = [float(x) for x in np.linspace(-1, 1, num)]
np.random.shuffle(a)


def block_sort(arr: list[float], block_size: int) -> Generator[tuple[list[float], int], None, None]:
    c = 0
    s = sorted(arr)
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
            arr = arr[:i]+temp+arr[i+block_size+_:]
            c += 1
            yield arr, c


plt.ion()
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

x = np.arange(len(a))
colors = ["white"] * len(a)
vlines = ax.vlines(x, 0, a, colors="white", linewidth=.67)

ax.set_ylim(-1, 1)
ax.tick_params(colors="white")
ax.set_title("67 Block Sort (VLines Only)", color="white")

d = 0
for frame, idx in block_sort(a, len(a)//10):

    # update heights
    vlines.set_segments(
        [((i, 0), (i, h)) for i, h in enumerate(frame)]
    )
    e = int("".join([hex(np.random.randint(0, 255))[2:]]), 16)
    b = int("".join([hex(np.random.randint(0, 255))[2:]]), 16)
    c = int("".join([hex(np.random.randint(0, 255))[2:]]), 16)
    # color the sorted element blue
    colors[idx % len(a)] = (f"#{e:02x}{b:02x}{c:02x}" if idx < len(a) else "lime")
    vlines.set_color(colors)

    plt.pause(5 if d == 0 else 6e-7)
    d += 1
plt.ioff()
plt.show()

from typing import Generator
import numpy as np
import matplotlib.pyplot as plt

num = 10**3
a = [round(float(x), 3) for x in np.linspace(0, 1, num)]
np.random.shuffle(a)
sorted_l = sorted(a.copy())


def stalin_sort(arr: list[float]) -> Generator[tuple[list[float], int], None, None]:
    c = 0
    if not arr:
        return [], c

    result = [arr[0]]
    for num in arr[1:]:
        if num >= result[-1]:
            result.append(num)
            c += 1
            yield result, c


plt.ion()
fig, ax = plt.subplots()

fig.patch.set_facecolor("black")
ax.set_facecolor("black")

# Line plot instead of bars
line, = ax.plot(range(len(a)), a, color="white", linewidth=1.5)

ax.tick_params(colors="white")

# -----------------------
#   ANIMATION LOOP
# -----------------------
c = 0
for frame, iters in stalin_sort(a):
    plt.pause(5 if c == 0 else 1e-6)
    line.set_ydata(frame)
    ax.set_title(
        f"Stalin Sort Animation \n Iterations: {iters:,}", color="white")
    c += 1

# Finish in green
line.set_color("green")
plt.pause(0.5)

plt.ioff()
plt.show()

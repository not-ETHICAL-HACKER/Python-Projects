from typing import Generator, List, Tuple
import numpy as np
import matplotlib.pyplot as plt
import time

num = 10**3
a = [round(float(x), 3) for x in np.linspace(0, 1, num)]
np.random.shuffle(a)


def stalin_sort(arr: List[float]) -> Generator[Tuple[List[float], int], None, None]:
    i = 0
    c = 0

    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            arr.pop(i)  # remove current element
        else:
            i += 1

        c += 1
        yield arr.copy(), c   # IMPORTANT: use copy


def bogo_sort(arr: List[float]) -> Generator[Tuple[List[float], int], None, None]:
    c = 0
    a = sorted(arr)
    while True:
        if arr == a or c == 1_000:
            break
        np.random.shuffle(arr)
        c += 1
        yield arr.copy(), c


def quad_bubble_sort(arr: list[float]) -> Generator[tuple[list[float], int]]:
    n = len(arr)
    l_mid = r_mid = n//2
    start = old_1 = 0
    end = old_2 = n-1
    c = 0
    swap = True
    t = time.time()
    while True:
        if not swap:
            for i in range(old_1, old_2):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swap = True
                    c += 1
            yield arr, c
            old_2 -= 1
            swap = False
            for j in range(old_2, old_1, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    swap = True
                    c += 1
            yield arr, c
            old_1 += 1
            if not swap:
                print(time.time()-t)
                return (arr, c)
        swap = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
                c += 1
        yield arr, c
        end -= 1
        swap = False
        for j in range(end, start, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swap = True
                c += 1
        yield arr, c
        start += 1
        swap = False
        for k in range(l_mid, start-1, -1):
            if arr[k] < arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]
                swap = True
                c += 1
        yield arr, c
        l_mid -= 1
        swap = False
        for l in range(r_mid, end):
            if arr[l] > arr[l+1]:
                arr[l], arr[l+1] = arr[l+1], arr[l]
                swap = True
                c += 1
        yield arr, c
        r_mid += 1


def bubble_sort(arr: List[float]) -> Generator[Tuple[List[float], int], None, None]:
    n = len(arr)
    c = 0

    for i in range(n):
        flag = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            c += 1
        yield arr.copy(), c
        if not flag:
            break


plt.ion()
fig, ax = plt.subplots()

fig.patch.set_facecolor("black")
ax.set_facecolor("black")

line, = ax.plot(range(len(a)), a, color="white", linewidth=1)
ax.tick_params(colors="white")

# -----------------------
#   ANIMATION LOOP
# -----------------------
c = 0
b = a.copy()
for frame, iters in stalin_sort(b):  # use copy to preserve original
    plt.pause(0.5 if c == 0 else 1e-3)

    padded = frame + [np.nan] * (len(a) - len(frame))
    line.set_ydata(padded)

    ax.set_title(
        f"??? Sort\nIterations: {iters:,}",
        color="white"
    )

    c += 1

for frame, iters in bogo_sort(b):  # use copy to preserve original
    plt.pause(1e-30)

    padded = frame + [np.nan] * (len(a) - len(frame))
    line.set_ydata(padded)

    ax.set_title(
        f"??? Sort\nIterations: {iters:,}",
        color="white"
    )

    c += 1
for frame, iters in quad_bubble_sort(b):  # use copy to preserve original
    plt.pause(1e-3)

    padded = frame + [np.nan] * (len(a) - len(frame))
    line.set_ydata(padded)

    ax.set_title(
        f"??? Sort\nIterations: {iters:,}",
        color="white"
    )

    c += 1

for frame, iters in bubble_sort(b):  # use copy to preserve original
    plt.pause(1e-3)

    padded = frame + [np.nan] * (len(a) - len(frame))
    line.set_ydata(padded)

    ax.set_title(
        f"??? Sort\nIterations: {iters:,}",
        color="white"
    )

    c += 1

# Finish in green
line.set_color("green")
plt.pause(0.5)

plt.ioff()
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(10)
# a = [float(x) for x in np.linspace(-1, 10, int(10**2**3.5))]
# np.random.shuffle(a)


# def bogo_bubble_sort(arr: list[float]) -> tuple[list[float], int]:
#     n = len(arr)
#     c = 1
#     for _ in range(1, n+1):
#         swap = False
#         for i in range(n - 1):
#             #c += 1
#             if arr[i] > arr[i + 1]:
#                 c += 1
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 swap = True
            
#         if not swap:
#             return arr,c
#         #yield arr.copy(), c
#         new = arr[:n-_]
#         np.random.shuffle(new)
#         arr[:n-_] = new
#     return arr,c

# bogo_bubble_sort(a.copy())

# plt.ion()
# fig, ax = plt.subplots()
# fig.patch.set_facecolor("black")
# ax.set_facecolor("black")

# x = np.arange(len(a))
# vlines = ax.vlines(x, 0, a, colors="white", linewidth=.5)

# ax.set_ylim(-1, 10)
# ax.tick_params(colors="white")

# d = 0
# for frame, idx in bogo_bubble_sort(a):

#     # update heights
#     ax.set_title(f"Bubble Bogo Sort | Iterations {idx:,}", color="white")
#     vlines.set_segments([((i, 0), (i, h)) for i, h in enumerate(frame)])
#     plt.pause(5 if d == 0 else 6e-7)
#     d += 1
# plt.ioff()
# plt.show()

import timeit
import numpy as np

def run(seed,surt=False):
    np.random.seed(seed)
    a = [float(x) for x in np.linspace(-1, 10, 10**5)]
    np.random.shuffle(a)
    if surt == True:
        return sorted(a)
    def bogo_bubble_sort(arr):
        n = len(arr)
        for _ in range(1, n+1):
            swap = False
            for i in range(n - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swap = True
            if not swap:
                return arr

    bogo_bubble_sort(a.copy())
l = []
ll = []
for i in range(10**1):
    #t = timeit.timeit(lambda: run(i), number=1)
    tt = timeit.timeit(lambda: run(i,True), number=10)
    print(f"Sorted time -> seed {i}: {tt:.4f}",end="\r")# Bubble sort -> seed {i}: {t}",end="\r")
    #l.append((i, t))
    ll.append((i, tt))
#print("\n",min(l, key=lambda x: x[1]))
print("\n",min(ll, key=lambda x: x[1]))
print(max(ll, key=lambda x: x[1]))

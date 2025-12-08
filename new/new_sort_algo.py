import numpy as np
import matplotlib.pyplot as plt

num = 10**3
a = [round(float(x), 3) for x in np.linspace(0, 1, num)]
np.random.shuffle(a)
sorted_l = sorted(a.copy())

def cocktail_sort(nums):
    n = len(nums)
    start = 0
    end = n - 1
    iter = l_swaps = r_swaps = 0

    while True:
        swapped = False
        
        # Forward pass
        for i in range(start, end):
            iter += 1
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                l_swaps += 1
                swapped = True
        yield nums, iter, l_swaps, r_swaps

        if not swapped:
            return
        
        swapped = False
        end -= 1
        
        # Backward pass
        for j in range(end, start, -1):
            iter += 1
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                r_swaps += 1
                swapped = True
        yield nums, iter, l_swaps, r_swaps

        start += 1

        if not swapped:
            return


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
for frame, iters, l_swaps, r_swaps in cocktail_sort(a):
    plt.pause(5) if c == 0 else plt.pause(1e-6)
    line.set_ydata(frame)
    ax.set_title(
        f"Dual Bubble Sort Animation \n Iterations: {iters:,} | Left swaps: {l_swaps:,} | Right swaps: {r_swaps:,}", color="white")
    c += 1

# Finish in green
line.set_color("green")
plt.pause(0.5)

plt.ioff()
plt.show()

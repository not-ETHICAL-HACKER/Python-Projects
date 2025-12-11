import numpy as np
import matplotlib.pyplot as plt

def quad_bubble_sort(arr: list):
    n = len(arr)
    l_mid = r_mid = n//2
    start = old_1=0
    end =old_2= n-1
    c=0
    swap = True
    while True:
        if not swap:
            for i in range(old_1, old_2):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    swap = True
                    c+=1
            #yield arr, c
            old_2 -= 1
            swap = False
            for j in range(old_2, old_1, -1):
                if arr[j] < arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    swap = True
                    c+=1
            #yield arr, c
            old_1 += 1
            if not swap:
                break
        swap = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
                c+=1
        #yield arr, c
        end -= 1
        swap = False
        for j in range(end, start, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swap = True
                c+=1
        #yield arr, c
        start += 1
        swap = False
        for k in range(l_mid, start-1, -1):
            if arr[k] < arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]
                swap = True
                c+=1
        #yield arr, c
        l_mid -= 1
        swap = False
        for l in range(r_mid, end):
            if arr[l] > arr[l+1]:
                arr[l], arr[l+1] = arr[l+1], arr[l]
                swap = True
                c+=1
        yield arr, c
        r_mid += 1
        
    return arr,c


a = [float(i)for i in np.linspace(0, 1, 10**4)]
np.random.shuffle(a)
print(quad_bubble_sort(a))
plt.ion()
fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

x = np.arange(len(a))
bars = ax.bar(x, a, color="white", width=0.8)

ax.set_title("Quad Bubble Sort Animation (Bars)", color="white")
ax.tick_params(colors="white")
ax.set_ylim(0, 1)   # IMPORTANT for stable animation

# --------------------------
#   ANIMATION LOOP
# --------------------------

for frame, iters in quad_bubble_sort(a):
    for rect, h in zip(bars, frame):
        rect.set_height(h)

    ax.set_title(f"Quad Bubble Sort | Iterations: {iters:,}", color="white")
    plt.pause(1e-6)

# Finish in green
c=-1
for k in range(2):
    for rect in bars:
        if c==0: 
            rect.set_color("lime")     
        else:
            rect.set_color("red")
            plt.pause(1e-6)
            rect.set_color("white")
        plt.pause(1e-6)
    else:
        c+=1

plt.pause(0.5)
plt.ioff()
plt.show()
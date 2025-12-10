import matplotlib.pyplot as plt
import numpy as np

def bubble_sort_graph():

    num = 100
    a = [float(x) for x in np.linspace(0, 1, num)]
    np.random.shuffle(a)
    sorted_l = sorted(a)
    
    # -----------------------------
    #       BUBBLE SORT (GEN)
    # -----------------------------
    def bubble_sort(List: list):
        iterations = 0
        swaps = 0

        for i in range(len(List)):
            if List == sorted_l:
                break

            for j in range(len(List) - 1 - i):

                if List[j] > List[j + 1]:
                    swaps += 1
                    List[j], List[j + 1] = List[j + 1], List[j]

            iterations += 1
            yield List, iterations, swaps


    # -----------------------------
    #       ANIMATION SETUP
    # -----------------------------
    plt.ion()
    fig, ax = plt.subplots()

    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # LINE instead of bars
    line, = ax.plot(range(len(a)), a, color="white", linewidth=1)

    ax.set_title("Bubble Sort Animation (Line)", color="white")
    ax.tick_params(colors="white")


    # -----------------------------
    #       FRAME UPDATE LOOP
    # -----------------------------
    for frame, iters, swaps in bubble_sort(a):
        line.set_ydata(frame)

        ax.set_title(
            f"Bubble Sort Animation | Iterations: {iters:,} | Swaps: {swaps:,}",
            color="white"
        )

        plt.pause(10/num)

    # -----------------------------
    #       FINISH IN GREEN
    # -----------------------------
    line.set_color("green")
    plt.pause(0.5)

    plt.ioff()
    plt.show()
bubble_sort_graph()

# todo: make a new sort algo like bogo sort for nxt time ig?
def bogo_sort_graph():
    num = 5
    iter = 0
    original = [x for x in np.linspace(0, 1, num)]
    Lines = original.copy()   # list used for sorting
    sorted_l = sorted(original)
    np.random.shuffle(Lines)

    iter = 0
    num = 50  # you can change this

    # sample data
    Lines = np.linspace(0, 1, num).tolist()
    sorted_l = sorted(Lines.copy())
    np.random.shuffle(Lines)

    def bogosort(List: list):
        nonlocal iter
        while True:
            iter += 1
            if List == sorted_l:
                return List, iter

            np.random.shuffle(List)
            yield List, iter


    # -----------------------
    #   MATPLOTLIB SETUP
    # -----------------------

    plt.ion()
    fig, ax = plt.subplots()

    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")

    # Line plot instead of bars
    line, = ax.plot(range(len(Lines)), Lines, color="white", linewidth=1.5)

    ax.set_title("Bogo Sort Animation (Line)", color="white")
    ax.tick_params(colors="white")


    # -----------------------
    #   ANIMATION LOOP
    # -----------------------

    for frame, iters in bogosort(Lines):
        line.set_ydata(frame)
        ax.set_title(f"Bogo Sort Animation | Iterations: {iters}", color="white")
        plt.pause(1e-6)

    # Finish in green
    line.set_color("green")
    plt.pause(0.5)

    plt.ioff()
    plt.show()

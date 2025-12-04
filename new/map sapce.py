import numpy as np
import time
from colorama import Style, Back, Fore, init
import os
init(autoreset=True)
a = [round(float(x), 3) for x in np.linspace(0, 1, 50)]
np.random.shuffle(a)
sorted_l = sorted(a)
c_1 = Fore.GREEN+Back.BLACK+Style.BRIGHT
c_2 = Fore.RED+Back.BLACK+Style.BRIGHT


def bubble_sort(List: list) -> list:
    """
    The function `bubble_sort` implements the bubble sort algorithm in Python and displays the sorting
    process step by step.

    :param List: The code you provided is a basic implementation of the bubble sort algorithm in Python.
    It sorts a given list in ascending order
    :type List: list
    :return: The function `bubble_sort` is returning the sorted list after performing the bubble sort
    algorithm on the input list.
    """
    c = 1
    for i in range(len(List)):
        if sorted_l == List:
            break
        os.system("cls")
        print("The Green tells us the number of times the buble moves and the red is the list.")
        print(f"{c_1}{c:4d}{c_2}=>{List}")
        for j in range(len(List)-1-i):
            time.sleep(0.001)
            c += 1
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    print()
    return List


bubble_sort(a)

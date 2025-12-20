import numpy as np


class Tree:
    @staticmethod
    def treeify(vals: list[int | float]) -> list[int | float]:
        i = 0
        tree = [vals[len(vals)//2]]
        h = sorted(vals)[vals.index(tree[0])+1:]
        l = sorted(vals)[:vals.index(tree[0])]
        while len(tree) < len(vals) and i < 100:
            for j, k in enumerate(vals):
                if j == len(vals)//2 or k in tree:
                    continue

                i += 1
        return tree


a = [float(x) for x in np.linspace(0, 1, 10**2)]
# print(Tree.treeify(a))


def alt_vals(arr: list[int | float]) -> list[int | float]:
    arr.sort()
    h: list[int | float] = []
    l: list[int | float] = []
    f: list[int | float] = []
    m = arr[len(arr)//2]
    for i in range(len(arr)):
        if arr[i] > m:
            h.append(arr[i])
        elif arr[i] < m:
            l.append(arr[i])
    for i in range(min(len(h), len(l))):
        f.append(h[i])
        f.append(l[i])

    return [m] + f

def sorter(arr:list)->None:
    arr.sort()
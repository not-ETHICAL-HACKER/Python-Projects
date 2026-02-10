import random
random.seed(0)  # Set a fixed seed for reproducibility


def rand_gen(n: int):
    return random.randint(10**(n-1), 10**(n)-1)
print(int("100",base=4))

def tetra_equidistant_nums(start: int, end: int) -> list[int]:
    from math import floor
    step = floor((start+end)/3)
    return [start, start+step, start+step*2, end]


def main():
    print(tetra_equidistant_nums(1, 7))


if __name__ == "__main__":
    main()

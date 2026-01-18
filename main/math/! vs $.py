def Wrapper(func):
    def Inner(*args, **kwargs):
        print(f"Calling function -> {func.__name__}", end=" ")
        return func(*args, **kwargs)
    return Inner


@Wrapper
def fac(n: int) -> int:
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result


@Wrapper
def super_fac(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= fac(i)
    return result


print(f"{super_fac(5):,} vs {fac(5)**(fac(5)**0.5):,}")

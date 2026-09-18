import math


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


x = 10


def compare_growth(x: int, k: float = 0.0625):
    # Log base 10 of Superfactorial
    log_sf = sum(math.lgamma(i + 1) for i in range(1, x + 1)) / math.log(10)

    # Log base 10 of (x!)^(x!^k)
    # Formula: (x!^k) * log10(x!)
    log_fac_x = math.lgamma(x + 1) / math.log(10)
    log_formula = (10**(log_fac_x * k)) * log_fac_x

    print(f"x={x} | SF Digits: {log_sf:,.0f} | Formula Digits: {log_formula:,.0f}")


compare_growth(10**3)

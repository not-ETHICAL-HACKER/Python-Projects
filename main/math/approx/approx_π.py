from math import e, sqrt, factorial, pi


def convergin_iter_approx(n: int) -> float:
    pi = 0
    for _ in range(1, n+1):
        pi += 6/_**2
    return sqrt(pi)


def liebnitz_approx(x: int) -> float:
    p1 = 0
    for n in range(x+1):
        p1 += 8/((4*n+1)*(4*n+3))
    return p1


def wallis_approx(x: int) -> float:
    p2 = 1
    for n in range(1, x+1):
        p2 *= (4*n**2)/((4*n**2)-1)
    return 2*p2


def taylor_series_approx(x: int) -> float:
    pi = 0
    for k in range(x+1):
        pi += ((-3)**-k)/(2*k+1)
    return pi*sqrt(12)
# print(taylor_series_approx(10**1))

def ramanjuam_approx(x:int)->float:
    pi=0
    for k in range(x+1):
        pi+=(factorial(4*k)*(1103+26390*k))/((factorial(k)**4)*396**(4*k))
    return (((2*sqrt(2))/9801)*pi)**-1
# print(((ramanjuam_approx(10**0)-pi)/pi)*100)
def e_approx(x:int)->float:
    pi=0
    for k in range(x+1):
        pi+=((2+k)/(e**k))
    return pi
# print(e_approx(10**2))

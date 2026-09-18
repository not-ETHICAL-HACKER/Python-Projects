def e_verify(a:float)->str:
    from math import e
    err=abs(a/e)/e
    return f"{err:+.12f} %"
def e_approx_iter_fac(x:int)->float:
    """
    The function calculates an approximation of the mathematical constant 'e' using an iterative
    factorial approach.
    
    :param x: The parameter `x` in the `e_approx_iter_fac` function represents the number of terms to
    include in the approximation of the mathematical constant 'e' using the iterative factorial method
    :type x: int
    :return: The function `e_approx_iter_fac(x)` is returning an approximation of the mathematical
    constant e using an iterative approach based on factorials.
    """
    def fac(n:int)->int:
        c=1
        for i in range(1,n+1):
            c*=i
        return c
    s=0
    for k in range(x):
        s+=1/fac(k)
    return s
def e_approx_form_pwr(x:int)->float:
    return (1+1/x)**x
n=1
print(e_verify(e_approx_iter_fac(n)))
print(e_verify(e_approx_form_pwr(n)))
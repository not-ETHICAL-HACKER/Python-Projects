import time
t=time.time()
def prime_checker(lim:int)->bool:
    if lim==2:
        return True
    if lim<2 or lim%2==0:
        return False
    for i in range(3,int((lim**0.5))+1,2):
        if lim%i==0:
            return False
    return True
def mersenne_primes_up_to(limit:int)->list[int]:
    result:list[int] = []

    p = 2
    while True:
        M = (1 << p) - 1
        if M > limit:
            break

        if p == 2:
            result.append(M)
        else:
            s = 4
            for _ in range(p - 2):
                s = (s * s - 2) % M
            if s == 0:
                result.append(M)

        p += 1

    return result

b=[x for x in range(10**3) if mersenne_primes_up_to(x)]
print(b,time.time()-t)
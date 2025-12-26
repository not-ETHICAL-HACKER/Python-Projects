def tribonnacci_series(i:int)->int:
    a=b=0;c=1
    if i in (a,b):
        return a
    #f(n)=f(n-1)+f(n-2)+f(n-3)
    k=1
    while k<i:
        print(c,end=" ")
        a,b,c=b,c,c+a+b
        k+=1
    return c
print(tribonnacci_series(10))
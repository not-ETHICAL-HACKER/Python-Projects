import time,math,random
#!Constants
inf = float('inf')

#todo: improve the game increment function to include more functions
#! Functions
def fib(x:int)->int:
    a,b=0,1
    for _ in range(x):
        a,b=b,a+b
    return a

def fac(x:int)->int:
    if x==0 or x==1:
        return 1
    else:
        return x*fac(x-1)

def two_pwr(x:int)->int:
    return 2**x

def game_inc(choice:str, n:int)->int|None:
    if choice=="fib":
        return fib(n)
    elif choice=="fac":
        return fac(n)
    elif choice=="2pwr":
        return two_pwr(n)
    else:
        return None
def lvl_up(type_func:str,lvl:int)->int:
    #! i have implemented ts badly but it works for now
    #? idk man mabye the lvl should be a progress bar or time based
    #* copy idea from cookie clicker and idle rvolution

    exp=game_inc(type_func,int(math.log(lvl)))
    return exp

def int_ps(exp:int):
    while True:
        #!int_ps is integer per second
        exp+=exp
        time.sleep(1)
        yield exp
print(game_inc("fac",5))
print(lvl_up("fib",10))
#? add a way to choose which function to use for exp gain
#! mabye even add a way to combine functions for exp gain
for val in int_ps(lvl_up("2pwr",300)):
    print(val)
    if val>1000:
        print("limit reached starting stronger again.......")
        break
        #? maybe add a lvl up system after every break
        #* or add a way to spend exp on upgrades
        #* exp should lvl up only when exp reaches a certain threshold(ie,10**6)
        #* copy the progression in idle revolution
#! from gpt
"""def cube(x: int) -> int:
    return x ** 3

def tri(x: int) -> int:
    return x * (x + 1) // 2

def game_inc(choice: str, n: int) -> int | None:
    funcs = {
        "fib": fib,
        "fac": fac,
        "2pwr": two_pwr,
        "cube": cube,
        "tri": tri
    }
    func = funcs.get(choice)
    return func(n) if func else None


    

import json

def save_progress(lvl, exp):
    with open("save.json", "w") as f:
        json.dump({"lvl": lvl, "exp": exp}, f)

        

def check_level_up(exp, lvl):
    threshold = 10 ** (lvl // 2)  # scalable threshold
    if exp >= threshold:
        lvl += 1
        exp = 0
        print(f"🎉 Level up! New level: {lvl}")
    return exp, lvl

"""
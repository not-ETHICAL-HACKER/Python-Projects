import time
import math
import random
import json
from colorama import Fore, Back, Style, init
import os

#//saving and loading progress
def save_progress(lvl:int=1, exp:int=1, filename="save.json"):
    try:
        with open(filename, "w") as f:
            json.dump({"lvl": lvl, "exp": exp}, f, indent=4)
        print("Progress saved successfully!")
    except Exception as e:
        print(f"Error saving progress: {e}") 

def load_progress(filename="save.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            print("Progress loaded successfully!")
            return data["lvl"], data["exp"]
    except FileNotFoundError:
        print("No save file found — starting fresh.")
        return 1, 0

inp = input("Have you played this game before? (y|n) ")
if inp.lower() == "y":
    lvl, exp = load_progress()
else:
    lvl, exp = 1, 0

# Move cursor up 1 line and clear it
print("\033[F\033[K", end="")

a=Fore.MAGENTA+Style.BRIGHT+"Welcome TO My Game."+Fore.RESET+Style.NORMAL
print(a.center(100))
print("\n"*3)

#//claering screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#!Constants

inf = 1.7976931348623157e308  #? maximum float value
speed=1.0 #! time between increments
expo=1 #! exponent for increment function
init(autoreset=True)
diff=1
skin=Fore.WHITE + Style.BRIGHT
c=0
stages=5


#* storages
total=[] #! list to store FINAL total experience points

#todo: improve the game increment function to include more functions
#! Functions
def fib(x:int)->int:
    """Returns the xth Fibonacci number."""
    a,b=0,1
    for _ in range(x):
        a,b=b,a+b
    return a**expo
#! 67 lol
def fac(x: int) -> int:
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result ** expo

def two_pwr(x:int)->int:
    """Returns 2 raised to the power of x."""
    return (2**x)**expo

def game_inc(choice: str, n: int) -> int:
    """Returns the result of the chosen function applied to n."""
    choices = {
        "fib": fib,
        "fac": fac,
        "2pwr": two_pwr
    }
    if choice not in choices:
        return 1
    return choices[choice](n)

#? idk man mabye the lvl should be a progress bar or time based
#* copy idea from cookie clicker and idle rvolution 

def lvl_up(type_func: str, lvl: int,early_game:bool=True) -> int:
    """
    Calculates experience gain based on level and selected function.\n
    Uses a smooth, non-zero scaling function.
    """

    # Prevent math domain errors (e.g. log(0))
    if lvl < 1:
        lvl = 1

    # Smoothed growth: logarithmic-ish, but always >= 1
    if early_game:
        scaled_lvl = max(1, int(math.sqrt(lvl)))  
    else:
        scaled_lvl = max(1, int(math.log(lvl + 1) * 2))  # tweak the *2 to change scaling speed
    exp = game_inc(type_func, scaled_lvl)
    return exp

def xp_per_second_multi(choices, lvl, speed):
    if speed <= 0:
        return inf/1  # Infinite XP per second
    total_exp = sum(game_inc(choice, lvl) for choice in choices)
    return total_exp / speed


def int_ps(exp_func, lvl):
    """
    Infinite XP generator that resets to 0 each cycle.
    
    - exp_func: function to calculate XP gain (e.g., game_inc("fib", lvl))
    - lvl: current level (can be updated externally)
    """
    global speed, diff
    while True:
        tot = 0  # reset XP for each cycle
        while True:
            current_exp = exp_func(lvl)
            tot += current_exp
            yield tot
            time.sleep(speed)
            
            # Optional: break this inner loop when threshold is reached
            if tot >= 10**diff:  # for example, level-up threshold
                break



#? add a way to choose which function to use for exp gain
#! mabye even add a way to combine functions for exp gain
#// animation for lvl up
def lvl_up_animation(lvl:int)->None:
    animation = list("|/-\\")
    for _ in range(int(random.random()*20)):
        for frame in animation:
            print(f"\r{Fore.GREEN}Level Up! New Level: {lvl} {frame}", end="")
            time.sleep(0.1)
        print(end = "")
    print()
#//shop fucyions
class Shop:
    @staticmethod
    def upgrade_speed(current:int|float)->float:
        """Way to reduce time between every interval"""
        r=random.random()
        R=random.random()
        if current-abs(r - R)>0:
            return current-abs(r - R)
        else:
            return 0
    @staticmethod
    def upgrade_exponent(current:int|float)->float:
        """This is a way to upgrade the exponent"""
        exp=random.random()
        return current+exp




#! Main Game Loop
for infinity in range(1):
    while True:
        choice = input("Enter a style of gaining exp (fac, fib, 2pwr): ")
        if choice in ("fac", "fib", "2pwr"):
            break
        else:
            # erase only the last invalid line
            print("\033[F\033[K", end="")
            print(f"{Fore.RED}Invalid choice, please choose again.")
    for main_loop in range(stages):
        clear_screen()
        #todo: add a way to choose early game or late game scaling

        for i in range(1):
            #// error in loop values
            #! fixed
            for val in int_ps(lvl_up(choice,lvl+i),lvl+i):
                print(skin+str(val)+"\r",end="")
                if val>=10**diff and val<inf:
                    lvl+=1
                    total.append(val)
                    print(Fore.CYAN + f"Level {lvl}: Gaining XP via {choice} mode...")
                    print(Fore.YELLOW + f"Speed: {speed:.5f}s | Exponent: {expo}")
                    print("limit reached starting stronger again.......")
                    xp_per_second_multi([choice], lvl, speed)
                    lvl_up_animation(lvl)
                    save_progress(lvl, val)
                    break
                    #? maybe add a lvl up system after every break
                    #* or add a way to spend exp on upgrades
                    #* exp should lvl up only when exp reaches a certain threshold(ie,10**6)
                    #* copy the progression in idle revolution
                if val>=inf:
                    print(f"{Fore.RED}You have reached the maximum limit of experience points.")
                    print(f"{Fore.MAGENTA+Style.BRIGHT}Congratulations on reaching infinity!\nThe game will now reset your experience points to continue playing.")
                    print("You will get a gift of your current experience points multiplied by 2 as a bonus for reaching infinity.")
                    money *= 2
                    total.append(inf)
                    break
        money=sum(total)
        for i in range(1):
            print(f"{Style.BRIGHT}{Fore.MAGENTA}You have {money} experience points.")
            a=input("Do you wawnt to to spend your exp?\n(Y|N):")
            if a in ("Y","y"):
                print("Shop is under construction......")
                print("THers only speed upgrades")
                while True:
                    try:
                        a=int(input(f"1. Upgrade Speed\n2. Upgrade Exponent\n3. Increase difficulty\nEnter your choice{Style.BRIGHT}(in int){Style.NORMAL}:"))
                        break
                    except ValueError:
                        print(f"{Fore.RED}Invalid statement.")
                if a==1:
                    print("Upgrading Speed for 10 exp")
                    if 10>money:
                        print(f"{Style.BRIGHT}{Fore.BLUE}Not enough exp to spend!")
                    else:
                        money-=10
                        speed=Shop.upgrade_speed(current=speed)
                        print(f"New speed interval is {speed}")
                elif a==2:
                    print("Upgrading Exponent for 10 exp")
                    if 10>money:
                        print(f"{Style.BRIGHT}{Fore.BLUE}Not enough exp to spend!")
                    else:
                        money-=10
                        expo=Shop.upgrade_exponent(current=expo)
                        if expo>3:
                            print("Limit Reached")
                            expo=3
                        print(f"New exponent is {expo}")
                elif a==3:
                    if inf<=10**diff:
                        print("Reached infinty.\nCannot increase difficulty")
                        print(1)
                    diff+=1
                    print(f"New difficulty is {diff}\n and a gift of {money*2}")
                else:
                    print(f"{a} is an invalid choice")
            else:
                print("Saving exp for now",money)
            print(f"{Fore.RED}Current Level: {lvl}{Fore.RESET}\n{Fore.BLUE}Current Speed: {speed}{Fore.RESET}\n{Fore.CYAN}Current Exponent: {expo}{Fore.RESET}\n{Fore.RED}Current Difficulty: {diff}{Fore.RESET}\n{Fore.GREEN}Current exp: {money}{Fore.RESET}")
            time.sleep(1)

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
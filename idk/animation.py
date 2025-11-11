import time,sys,random
def marquee(txt:str=" Hello World ",dir:str="left",cd:float=0.1,num:int=10)->None:
    """Creates a marquee animation in the console."""
    if dir not in ["left","right"]:
        raise ValueError("Direction must be 'left' or 'right'")
    if dir=="left":
        while True:
            sys.stdout.write((txt)*num+"\r")
            sys.stdout.flush()
            time.sleep(cd)
            txt=txt[1:]+txt[0]
    else:
        while True:
            sys.stdout.write((txt)*num+"\r")
            sys.stdout.flush()
            time.sleep(cd)
            txt=txt[-1]+txt[:-1]
def bouncy(txt:str=" Hello World ",cd:float=0.1)->None:
    """creates a bouncy animation in the console."""
    while True:
        for i in range(len(txt)//2):
            sys.stdout.write(" "*i+txt+"\r")
            sys.stdout.flush()
            time.sleep(cd)
        for i in range(len(txt)//2,0,-1):
            sys.stdout.write(" "*i+txt+"\r")
            sys.stdout.flush()
            time.sleep(cd)
def majic(txt:str):
    txt=" "*5+txt
    while True:
        for i,ch in enumerate(txt):
            sys.stdout.write(" "* (len(txt)-i) + txt[-i] + "\r")
            sys.stdout.flush()
            time.sleep(0.1)
def magnet(frames:list=list("Hello World"),fps:float=60,Alt:bool=False):
    a=0
    new=False
    if not Alt:
        while True:
            if new:
                print()
                new=False
            for i in range(len(frames)):
                sys.stdout.write((" "*(i-a))+(frames[i-a])+("\r"))
                sys.stdout.flush()
                time.sleep(1/fps)
            a+=1
            if a==len(frames):
                a=0
                new=True
    else:
        while True:
            for i in range(len(frames)):
                a=len(frames)-1
                #for alternate animation ie,|\-/ at the same time at diff animate times ig
def powers_of_2(x: int):
    import math
    RESET = "\033[39m"   # reset only text color (no background flash)
    BG_BLACK = "\033[40m"

    colors = [
        "\033[38;5;196m",  # red
        "\033[38;5;202m",  # orange
        "\033[38;5;226m",  # yellow
        "\033[38;5;82m",   # green
        "\033[38;5;45m",   # cyan
        "\033[38;5;21m",   # blue
        "\033[38;5;201m",  # magenta
    ]

    universe_atoms = 10**78

    print(BG_BLACK, end="")  # force dark background once

    if 2**x > 2**(2**8):
        print(f"\033[1;91mts too large to comprehend 🤯{RESET}")
        ratio = 2**x / universe_atoms
        print(f"\033[2mthis has {ratio:.2e} times more atoms than the universe{RESET}\n")

    t = 0
    while x > 8 - 1:
        x //= 2
        t += 1

    var = "|"
    color = colors[t % len(colors)]

    print(f"Visualizing 2^{2**t * x}:")

    for i in range(x + 1):
        print(f"{color}{var * (2**i)}{RESET}")

    if t > 0:
        print(f"\n{color}This graph has been shrinked {t} time(s) for readability!{RESET}")
while True:
    break
    a=int(input("Enter a number to visualize its power of 2 (or -1 to exit): "))
    if a==-1:
        break
    powers_of_2(a)
bouncy()
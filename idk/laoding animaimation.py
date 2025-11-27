from colorama import Fore, Style, init
import time
import random

frames = "|\\-/"
arr = "←↖↑↗→↘↓↙"
cir = "◜◠◝◞◡◟"
circ = "◐◓◑◒"
block = "▓▒░"
blocks = "▉▊▋▌▍▎▏▎▍▌▋▊▉"
a = "▖▘▝▗"
b = "┤┘┴└├┌┬┐"
d = "◰◳◲◱"
e = "◴◷◶◵"
#f1 = "◡◡⊙⊙◠◠"
g = "⣾⣽⣻⢿⡿⣟⣯⣷"
h = "⠁⠂⠄⡀⢀⠠⠐⠈"
init(autoreset=True)

c = Fore.GREEN+Style.BRIGHT
colors = [Fore.RED+Style.BRIGHT, Fore.YELLOW+Style.BRIGHT, Fore.GREEN+Style.BRIGHT,
          Fore.CYAN+Style.BRIGHT, Fore.BLUE+Style.BRIGHT, Fore.MAGENTA+Style.BRIGHT]
i = j = 0

lis = [frames, arr, cir, circ, block, blocks, a, b, d, e, g, h]
try:
    while True:
        break
        lis= random.sample(lis, len(lis))
        j += 1
        for f in lis[j % len(lis)]:
            print(f"{c}Loading... {colors[i]+(f*1)}", flush=True, end="\r")
            time.sleep(0.1)
            i += 1
            if i == len(colors):
                i = 0
except KeyboardInterrupt or SystemExit:
    print(f"{c}Loading... Done!   ")
def iterative_chrs(n: int):
    for i in range(n+1):
        print(f"\\U{i:08X} -> {chr(i)}")
iterative_chrs(10**3)
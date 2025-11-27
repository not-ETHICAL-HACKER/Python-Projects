import math, os, time, random
from colorama import Style, Fore, Back, init
init(autoreset=True)

# === Color combos ===
colors = [
    Fore.BLUE+Style.BRIGHT+Back.BLACK,
    Fore.GREEN+Style.BRIGHT+Back.BLACK,
    Fore.MAGENTA+Style.BRIGHT+Back.BLACK,
    Fore.CYAN+Style.BRIGHT+Back.BLACK,
    Fore.RED+Style.BRIGHT+Back.BLACK,
    Fore.YELLOW+Style.BRIGHT+Back.BLACK,
    Fore.WHITE+Style.BRIGHT+Back.BLACK,
    Fore.LIGHTBLUE_EX+Style.BRIGHT+Back.BLACK,
    Fore.LIGHTCYAN_EX+Style.BRIGHT+Back.BLACK,
    Fore.LIGHTMAGENTA_EX+Style.BRIGHT+Back.BLACK,
    Fore.LIGHTGREEN_EX+Style.BRIGHT+Back.BLACK,
    Fore.RED+Back.BLUE+Style.BRIGHT,
    Fore.YELLOW+Back.BLUE+Style.BRIGHT,
    Fore.GREEN+Back.BLUE+Style.BRIGHT,
    Fore.CYAN+Back.BLUE+Style.BRIGHT,
    Fore.MAGENTA+Back.BLUE+Style.BRIGHT,
    Fore.WHITE+Back.BLUE+Style.BRIGHT,
    Fore.RED+Back.GREEN+Style.BRIGHT,
    Fore.YELLOW+Back.GREEN+Style.BRIGHT,
    Fore.BLUE+Back.GREEN+Style.BRIGHT,
    Fore.CYAN+Back.GREEN+Style.BRIGHT,
    Fore.MAGENTA+Back.GREEN+Style.BRIGHT,
    Fore.WHITE+Back.GREEN+Style.BRIGHT,
]

symbols = ["#", "@", "&", "%", "$", "*", "♥", "♪", "∞"]

# === Rainbow chaos loop ===
l = colors.copy()
rows = 10  # number of rows

try:
    for _ in range(1000):
        if _ % 50 == 0:
            os.system("cls")
        for r in range(rows):
            for i in range(len(l)):
                # pulsing color effect
                idx = int((math.sin(time.time()*5 + i/5) + 1)/2 * len(l))
                color = l[idx]
                symbol = random.choice(symbols)
                print(color + symbol, end="")
            print()
        l = random.sample(l, len(l))  # shuffle for chaos
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\n💀 Terminal chaos ended!")

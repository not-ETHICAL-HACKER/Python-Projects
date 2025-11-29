def powers_of_2(x: int):
    import math

    RESET = "\033[39m"   # reset foreground only (no white flash)
    BG_BLACK = "\033[40m"  # dark background
    print(BG_BLACK, end="")

    # rainbow color generator (256-color ANSI range 16–231)
    def color_wave(i, total, phase=0):
        # smooth hue cycle based on position
        hue = int(16 + (i / total) * 215 + phase) % 231
        return f"\033[38;5;{hue}m"

    universe_atoms = 10**78

    if 2**x > 2**(2**8):
        print(f"\033[1;91mts too large to comprehend 🤯{RESET}")
        ratio = 2**x / universe_atoms
        print(
            f"\033[2mthis has {ratio:.2e} times more atoms than the universe{RESET}\n")

    t = 0
    while x > 8 - 1:
        x //= 2
        t += 1

    var = "|"

    print(f"Visualizing 2^{2**t * x} (rainbow mode):\n")

    # Draw wave-colored bars
    for i in range(x + 1):
        bar = var * (2**i)
        color = color_wave(i, x + 1, phase=t * 20)  # shift hue per reduction
        print(f"{color}{bar}{RESET}")

    if t > 0:
        print(
            f"\n{color_wave(x, x)}This graph has been shrinked {t} time(s) for readability!{RESET}")


while True:
    p = int(input("Enter a number:"))
    powers_of_2(p)

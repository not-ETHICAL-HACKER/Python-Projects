import math
import time
import sys

A = 0.0
B = 0.0

while True:
    # cursor home
    sys.stdout.write("\x1b[H")

    z = [0.0] * 1760
    b = [' '] * 1760

    j = 0
    while j < 6.28:
        i = 0
        while i < 6.28:
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e

            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))

            o = x + 80 * y

            if 0 <= o < 1760:
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                if D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[max(N, 0)]

            i += 0.07
        j += 0.02

    # Print full frame INCLUDING newlines so old content disappears
    frame = ""
    for k in range(0, 1760, 80):
        frame += "".join(b[k:k+80]) + "\n"

    sys.stdout.write(frame)
    sys.stdout.flush()

    A += 0.04
    B += 0.02
    time.sleep(0.01)

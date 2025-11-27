import random
import time
import os
import sys


def format_time(t: float) -> str:
    original = t  # seconds

    units = [
        ("billion years", 31536000 * 10**9),
        ("millennia",     31536000 * 1000),
        ("centuries",     31536000 * 100),
        ("years",         31536000),
        ("days",          86400),
        ("hours",         3600),
        ("minutes",       60),
        ("seconds",       1),
    ]

    for name, secs in units:
        if original >= secs:
            value = original / secs
            return f"Which is approximately {value:.3f} {name}"

    return "Which is approximately 0 seconds"


def bogo_password_cracker(password: str = "2000", time_interval: int = 1, dialation: float = 10**6) -> float:
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    easy = "1234567890"
    medium = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mid_medium = medium+easy
    hard = medium+easy+"!@#$%^&*() _+-=[]{}|;:',.<>?/"
    l = len(password)
    t1 = time.perf_counter()
    chars = mid_medium
    i = d = 0
    while True:
        i += 1
        for j in range(1000):
            a=""
            for k in range(l):
                a += random.choice(chars)
            if d % 1000 == 0:
                sys.stdout.write(a)
                sys.stdout.flush()
                sys.stdout.write("\r")
            d += 1
            if a == password:
                print("\n"*2)
                t2 = time.perf_counter()
                t = t2-t1
                print(
                    f"Password cracked: {a} in {round(t,3)} seconds of {dialation:,} x speed")
                print(format_time(t))
                return t
    return -1.0

def password_generator(length: int = 12, complexity: str = "hard") -> str:
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer")
    if not isinstance(complexity, str):
        raise TypeError("Complexity must be a string")
    if complexity not in ["easy", "medium", "hard"]:
        raise ValueError("Complexity must be 'easy', 'medium', or 'hard'")
    easy = "1234567890"
    medium = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hard = medium+easy+"!@#$%^&*()_+-=[]{}|;:',.<>?/\\"
    if complexity == "easy":
        chars = easy
    elif complexity == "medium":
        chars = medium
    else:
        chars = hard
    return "".join(random.choice(chars) for _ in range(length))


def big():
    c = 0
    for i in range(100):
        for j in range(i*i):
            m = j*j
            c += (m-1) * m * (2*m - 1) // 6
    return c


print(f"{big():,}")
bogo_password_cracker()

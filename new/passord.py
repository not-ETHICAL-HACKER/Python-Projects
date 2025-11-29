from math import factorial, log
import random
import time
import os
import sys


def format_time(t: float) -> str:
    """
    The `format_time` function converts a given time in seconds into a more human-readable format such
    as years, days, hours, minutes, or seconds.
    
    :param t: The function `format_time` takes a float value `t` as input, which represents a duration
    in seconds. The function then converts this duration into a more human-readable format by expressing
    it in terms of different time units such as years, days, hours, minutes, and seconds. The function
    returns
    :type t: float
    :return: The `format_time` function takes a float `t` as input, which represents a time duration in
    seconds. It then converts this time duration into a more human-readable format by expressing it in
    terms of different time units such as years, days, hours, etc.
    """
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


def bogo_password_cracker(password: str = "2000", time_interval: int = 1) -> float:
    """
    The function `bogo_password_cracker` attempts to crack a given password using a brute-force approach
    by generating random permutations of characters and comparing them to the password.
    
    :param password: The `password` parameter in the `bogo_password_cracker` function is the target
    password that you want to crack. By default, it is set to "2000", but you can provide any string
    value as the password that you want to crack, defaults to 2000
    :type password: str (optional)
    :param time_interval: The `time_interval` parameter in the `bogo_password_cracker` function is used
    to specify the time interval for which the password cracker will run. It is an integer value that
    determines how long the function will attempt to crack the password before stopping. The default
    value for `time_interval`, defaults to 1
    :type time_interval: int (optional)
    :return: The function `bogo_password_cracker` returns a float value representing the time taken to
    crack the password.
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    easy="1234567890"
    medium="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mid_medium=medium+easy
    hard=list(chr(ch) for ch in range(32,128))
    l=len(password)
    chars=mid_medium
    i=d=0
    print(f"Your password is of length {l} and it would aproximately have {len(chars)**l:,} permutations")
    t1=time.time()
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
                t=time.time()-t1
                print(f"Password cracked: {a} in {round(t,12)} seconds of {round((i*1000+d)/t,3):3e} x speed")
                print(f"Total attempts (Rounded down in the thousands): {i*1000+d:,}")
                t=t*time_interval
                print(format_time(t))
                return t

def password_generator(length: int = 12, complexity: str = "hard") -> str:
    """
    The function `password_generator` generates a random password of a specified length and complexity
    level.
    
    :param length: The `length` parameter in the `password_generator` function specifies the length of
    the password to be generated. By default, if no length is provided, the function will generate a
    password of length 12 characters. You can also specify a custom length when calling the function,
    defaults to 12
    :type length: int (optional)
    :param complexity: The `complexity` parameter in the `password_generator` function determines the
    level of complexity for the generated password. It can take three values: 'easy', 'medium', or
    'hard', defaults to hard
    :type complexity: str (optional)
    :return: The function `password_generator` returns a randomly generated password based on the
    specified length and complexity.
    """
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
print(f"{308 * log(1.8, 2)}")
print(password_generator())
time.sleep(100)

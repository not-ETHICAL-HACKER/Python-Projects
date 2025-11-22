import time
import os
import random


def matrix(txt: str) -> None:
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = 0
    out = ""
    while True:
        for ch in alpha:
            time.sleep(0.1)
            print(ch)
            a = ch
            if a == txt[c]:
                print(out+"\r",end="")
                out += a
                c += 1
                break
        if c == len(txt):
            print(out)
            break


matrix("Hello")

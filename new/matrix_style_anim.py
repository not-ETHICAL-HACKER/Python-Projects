import time
import os
import random


def matrix(txt: str) -> None:
    alpha = [chr(i) for i in range(32, 127)]
    c = 0
    out = ""
    i=0
    while True:
        for ch in alpha:
            i+=1
            time.sleep(1e-3)
            print(out+ch,end="\r")
            if ch == txt[c]:
                out += ch
                c += 1
                alpha=random.sample(alpha,len(alpha))
                break
        if c == len(txt):
            print(out,i)
            break


matrix("Hello,WorldgfhdgvrfdhxddCTSDYGFRGEHGNGNNHJKDFH8RYHT8Hiohrhg21ty4783@#^%@#^")

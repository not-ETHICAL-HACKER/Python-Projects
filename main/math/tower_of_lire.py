#! this python program mathematically tells us the maximum possible overhang in n blocks if each block is of 
#! length and height 1 unit. this function reaches the most optimal overhang possible by stacking the blocks in a
#! most balanced way.
import math
def twr_o_l(x:int)->float:
    if x in (1,0):
        return 0.0
    c:float = 0.0
    for i in range(1,x+1):
        c+=1/(i*2)
    return c
print(twr_o_l(10))
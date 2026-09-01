import math
import time
import turtle
import numpy as np
import pygame
pygame.init()
from scipy.linalg import fractional_matrix_power as frac
t = turtle.Turtle(shape="square")
t.color("blue")
turtle.bgcolor("black")
turtle.tracer(0)

matrix = np.array([
    [1,-1],
    [1,1]
], dtype=float)

def matrix_taylor(A,n:int):
    S = np.eye(2)
    
    for i in range(1,n):
        fac = math.factorial(i)
        S += np.linalg.matrix_power(A,i)/fac
        
        S = S.real
        t.shapetransform(
                S[0,0], S[0,1],
                S[1,0], S[1,1]
            )
        time.sleep(.1)
        turtle.update()
        
matrix_taylor(matrix,100)
print("done")
turtle.done()
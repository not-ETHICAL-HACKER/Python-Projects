import math
import turtle
import time

t = turtle.Turtle()
t.color("blue")
t.speed(0)
turtle.bgcolor("black")
scale = 1

#If the number is even, divide it by 2.
#If the number is odd, multiply it by 3 and add 1.
def collatz_sequence(n:int)->list[tuple[int, int]]:
    """
    The function `collatz_sequence` generates a Collatz sequence starting from a given number and
    returns the sequence along with the number of iterations taken to reach 1.
    
    :param n: The function `collatz_sequence` takes an integer `n` as input and generates a Collatz
    sequence starting from that number. The Collatz sequence is generated based on the following rules:
    :type n: int
    :return: The function `collatz_sequence` returns a list of tuples representing the Collatz sequence starting from the input number `n`.
    """
    seq:list[tuple[int, int]]=[]
    prev = 0
    seq.append((prev, n))
    if n == 0:
        return seq
    if n > 0:
        while True:
            prev = n
            if n%2==0:
                n//=2
            elif n%2==1:
                n=3*n+1
            seq.append((prev,n))
            if 1 == n:
                return seq
    else:
        for i in range(100):
            prev = n
            if n%2==0:
                n//=2
            elif n%2==1:
                n=3*n+1
            seq.append((prev,n))
            if n == -1:
                return seq
        return seq

def draw_collatz(n:int):
    seq = collatz_sequence(n)
    for i in range(len(seq)-1):
        if seq[i][1]%2==0:
            t.color("blue")
        else:
            t.color("red")
        t.goto(seq[i][0]*scale, seq[i][1]*scale)
        time.sleep(1/240)

def alt_draw_collatz(n:int):
    global scale
    seq = collatz_sequence(n)
    # if len(seq) > 50:
    #     scale = 50/len(seq)
    t.setheading(90)
    for i in range(len(seq)-1):
        t.forward(10)
        # t.forward(math.log((seq[i][0]+1))*scale)
        if seq[i][1]%2==0:
            t.color("blue")
            t.right(30)
        else:
            t.color("red")
            t.left(45)
        t.forward(math.log((seq[i][1]+1))*scale)
        time.sleep(1/240)
for i in range(100):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    if not i%2:
        continue
    turtle.title(f"Collatz Conjecture: {i}")
    scale = 1
    alt_draw_collatz(i)
    time.sleep(1/2)
    t.clear()
turtle.done()
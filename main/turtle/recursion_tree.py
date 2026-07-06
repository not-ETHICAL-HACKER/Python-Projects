import random
import time
import turtle,math
turtle.speed(0)
turtle.bgcolor("black")
t = turtle.Turtle(visible=False)
t.color("green")
turtle.tracer(0, 0)
c =  00
def tree(length):
    if length < 10:
        global c
        c += 1
        turtle.update()
        t.dot(4,random.choice(["blue","yellow","red","purple"]))
        return
    weight = 0.75
    angle = math.pi*10
    thin = 10
    height =  1
    t.pensize(length/thin)
    t.forward(length/height)
    t.left(angle)
    tree(length*weight)
    t.pensize(length /thin)

    t.right(2*angle)
    tree(length*weight)
    t.pensize(length / thin)

    t.left(angle)
    t.backward(length/height)

def sqr(side):
    for i in range(4):
        t.forward(side)
        t.left(90)

def recur_sqr(side):
    if side < 10:
        return
    phi =  (1 + math.sqrt(5)) / 2
    t.left(math.e)
    t.forward(side * 0.01)
    sqr(side)
    time.sleep(.1)
    turtle.update()
    # t.forward(side/100)
    # sqr(side)
    recur_sqr(side*0.99)        
t.pendown()
recur_sqr(500)
print(c)
turtle.done()
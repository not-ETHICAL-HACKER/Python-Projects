import random
import time
import turtle,math
turtle.speed(0)
turtle.bgcolor("black")
t = turtle.Turtle(visible=False)
t.color("green")
turtle.tracer(0, 0)
c =  00
t.setheading(90)
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

def poly(side):
    n = 10
    for _ in range(n):
        t.forward(side)
        t.left(360/n)

def recur_shape(side):
    if side < 10:
        return
    phi =  (1 + math.sqrt(5)) / 2
    t.left(math.e)
    t.forward(side * 0.01)  
    poly(side)
    time.sleep(.01)
    turtle.update()
    # t.forward(side/100)
    # poly(side)
    recur_shape(side*0.99)
recur_shape(200)
print(c)
turtle.done()